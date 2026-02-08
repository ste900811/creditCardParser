import pandas as pd
from pypdf import PdfReader

from objects.people.people import people
from expensesHandler.discoverStevenLuEH import expensesHandler as discoverEH
from expensesHandler.capitalOneStevenLuEH import expensesHandler as captialOneEH
from expensesHandler.AMEXStevenLuEH import expensesHandler as amexEH
from expensesHandler.citiStevenLuEH import expensesHandler as citiEH
from expensesHandler.USBankStevenLuEH import expensesHandler as usEH

class stevenLuHome(people):
  def __init__(self, nameOnStatement):
    super().__init__(nameOnStatement)
    self.transactionList = []

  def outputCSVStatement(self, bankObj):
    print("check")
    df = pd.DataFrame(self.transactionList, columns=["日期", "支出項目", "明細", "金額"])
    df.sort_values(by=["日期"], inplace=True)
    df.to_excel(f'./statements/{self.nameOnStatement}/outputFile/{bankObj.bankName}_{bankObj.cardType}_{bankObj.StatementDate}_{bankObj.cardLast4Digits}.xlsx', index=False)
    return

  def getStatmentCSVBalance(self, filePath, bankName):
    if bankName == "discover":
      return self.processDiscoverCSV(filePath)
    elif bankName == "capitalOne":
      return self.processCapitalOneCSV(filePath)
    elif bankName == "AMEX":
      return self.processAMEXCSV(filePath)
    elif bankName == "Citi":
      return self.processCitiCSV(filePath)
    elif bankName == "USBank":
      return self.processUSBankCSV(filePath)
    else:
      print(f"getStatmentCSVBalance failed: Bank: {bankName}")
      assert False, f"getStatmentCSVBalance failed: Bank: {bankName}"

  def processDiscoverCSV(self, filePath):
    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Category"] == "Awards and Rebate Credits" or (row["Category"] == "Payments and Credits" and row["Description"] == "INTERNET PAYMENT - THANK YOU"):
        continue

      category, detail = discoverEH(row["Description"].split(" "), row["Amount"])

      if category == False:
        print(row["Description"].split(" "), row["Amount"])
        continue
      
      if row["Amount"] > 0:
        csvTotalAmount += row["Amount"]

      self.transactionList.append([row["Trans. Date"][:-5], category, detail, row["Amount"]])

    return csvTotalAmount
  
  def processCapitalOneCSV(self, filePath):
    print("CapitalOne: getStatmentCSVBalance")

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      description = self.filterOutPaymentsMethod(row["Description"].split(" "))
      if row["Card No."] == 1052 and row["Credit"] > 0:
        category, detail, amount = captialOneEH(description, -row["Credit"])
        csvTotalAmount += amount
      elif row["Card No."] == 1052 and row["Debit"] > 0:
        category, detail, amount = captialOneEH(description, row["Debit"])
        csvTotalAmount += amount
      else:
        continue
    
      if category == False:
        # print(category, detail)
        print(description, row["Debit"], row["Credit"])
        continue

      month, date = row["Transaction Date"][5:].split("-")
      self.transactionList.append([f'{month}/{date}', category, detail, amount])

    return csvTotalAmount
  
  def processAMEXCSV(self, filePath):
    print("AMEX: getStatmentCSVBalance")

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if "ONLINE PAYMENT" in row["Description"] or "MOBILE PAYMENT - THANK YOU" in row["Description"]:
        self.bankObj.payments += row["Amount"]
        continue

      descriptionArray = row["Description"].split(" ")
      descriptionArray = [item for item in descriptionArray if item != '']
      descriptionArray = self.filterOutPaymentsMethod(descriptionArray)
        
      category, detail, amount = amexEH(descriptionArray, row["Amount"])

      if category == False:
        print(descriptionArray, row["Amount"])
        continue

      month, date, year = row["Date"].split("/")
      self.transactionList.append([f'{month}/{date}', category, detail, amount])
      csvTotalAmount += amount

    return csvTotalAmount
  
  def processCitiCSV(self, filePath):

    df = pd.read_csv(filePath)

    for index, row in df.iterrows():

      if "ONLINE PAYMENT, THANK YOU" in row["Description"]:
        self.bankObj.paymentsAmount = row["Credit"]
        continue

      descriptionArray = row["Description"].split(" ")
      descriptionArray = self.filterOutPaymentsMethod(descriptionArray)

      if pd.isna(row["Debit"]) == False:
        category, detail, amount = citiEH(descriptionArray, row["Debit"])
        if category != False:
          self.bankObj.purchasesCSV += amount
      elif pd.isna(row["Credit"]) == False:
        category, detail, amount = citiEH(descriptionArray, -row["Credit"])
        if category != False:
          self.bankObj.creditsCSV -= amount

      if category == False:
        print(f'{descriptionArray} {row["Debit"]} {row["Credit"]}')
        continue

      month, date, year = row["Date"].split("/")
      if pd.isna(row["Debit"]) == False:
        self.transactionList.append([f'{month}/{date}', category, detail, amount])    
      elif pd.isna(row["Credit"]) == False:
        self.transactionList.append([f'{month}/{date}', category, detail, -amount])
      else:
        assert False, "processCitiCSV failed: Neither Debit nor Credit has value"

  def processUSBankCSV(self, filePath):
    filePath = filePath.replace(".csv", ".pdf")
    csvTotalAmount = 0.0

    reader = PdfReader(filePath)
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if line == "MERCHANDISE/SERVICE RETURN":
          for index, transaction in enumerate(self.transactionList):
            self.transactionList[index][3] = -transaction[3]
            csvTotalAmount -= amount * 2
        if line.count("/") == 2 and line.count("$") == 1 \
          and "your bank account" not in line and "your account" not in line:
          month, date, amount = line[6:8], line[9:11], float(line.split("$")[-1])
          descriptionArray = line[17:line.index('$')-1].split(" ")
          descriptionArray = self.filterOutPaymentsMethod(descriptionArray)

          category, detail = usEH(descriptionArray, amount)

          if descriptionArray[-2:] == ["THANK", "YOU"]:
            csvTotalAmount -= amount
            continue

          if category == False:
            print(f'{descriptionArray} {amount}')
            continue
          
          csvTotalAmount += amount
          self.transactionList.append([f'{month}/{date}', category, detail, amount])

    return csvTotalAmount
