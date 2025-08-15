import pandas as pd

from objects.people.people import people
from expensesHandler.discoverStevenLuEH import expensesHandler as discoverEH
from expensesHandler.capitalOneStevenLuEH import expensesHandler as captialOneEH
from expensesHandler.AMEXStevenLuEH import expensesHandler as amexEH

class stevenLuHome(people):
  def __init__(self, nameOnStatement):
    super().__init__(nameOnStatement)
    self.transactionList = []

  def outputCSVStatement(self, bankObj):
    print("check")
    df = pd.DataFrame(self.transactionList, columns=["日期", "支出項目", "明細", "金額"])
    df.sort_values(by=["日期"], inplace=True)
    df.to_excel(f'./statements/{self.nameOnStatement}/outputFile/{bankObj.bankName}_{bankObj.cardType}_{bankObj.StatementDate}.xlsx', index=False)
    return

  def getStatmentCSVBalance(self, filePath, bankName):
    if bankName == "discover":
      return self.processDiscoverCSV(filePath)
    elif bankName == "capitalOne":
      return self.processCapitalOneCSV(filePath)
    elif bankName == "AMEX":
      return self.processAMEXCSV(filePath)
    else:
      print(f"getStatmentCSVBalance failed: Bank: {bankName}")
      assert False, f"getStatmentCSVBalance failed: Bank: {bankName}"

  def processDiscoverCSV(self, filePath):
    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Category"] == "Awards and Rebate Credits" or row["Category"] == "Payments and Credits":
        continue

      category, detail = discoverEH(row["Description"].split(" "), row["Amount"])

      if category == False:
        print(row["Description"].split(" "), row["Amount"])
        continue
      
      csvTotalAmount += row["Amount"]
      self.transactionList.append([row["Trans. Date"][:-5], category, detail, row["Amount"]])

    return csvTotalAmount
  
  def processCapitalOneCSV(self, filePath):
    print("CapitalOne: getStatmentCSVBalance")

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Card No."] == 1052 and row["Credit"] > 0:
        category, detail, amount = captialOneEH(row["Description"].split(" "), -row["Credit"])
        csvTotalAmount += amount
      elif row["Card No."] == 1052 and row["Debit"] > 0:
        category, detail, amount = captialOneEH(row["Description"].split(" "), row["Debit"])
        csvTotalAmount += amount
      else:
        continue
    
      if category == False:
        # print(category, detail)
        print(row["Description"].split(" "), row["Debit"], row["Credit"])
        continue

      month, date = row["Transaction Date"][5:].split("-")
      self.transactionList.append([f'{month}/{date}', category, detail, amount])

    return csvTotalAmount
  
  def processAMEXCSV(self, filePath):

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if "ONLINE PAYMENT" in row["Description"]:
        continue
      
      descriptionArray = row["Description"].split(" ")
      descriptionArray = [item for item in descriptionArray if item != '']
      while descriptionArray[0] == "AplPay" or descriptionArray[0] == "UPSIDE*" or descriptionArray[0] == "TST*":
        descriptionArray = descriptionArray[1:]
        
      category, detail, amount = amexEH(descriptionArray, row["Amount"])

      if category == False:
        print(descriptionArray, row["Amount"])
        continue

      month, date, year = row["Date"].split("/")
      self.transactionList.append([f'{month}/{date}', category, detail, amount])
      csvTotalAmount += amount

    return csvTotalAmount
  