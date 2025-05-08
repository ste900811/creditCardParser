import pandas as pd

from objects.people.people import people
from expensesHandler.discoverStevenLuEH import expensesHandler as discoverEH
from expensesHandler.capitalOneStevenLuEH import expensesHandler as captialOneEH

class stevenLuHome(people):
  def __init__(self):
    self.transactionList = []

  def outputCSVStatement(self, personName, bankName, date):
    df = pd.DataFrame(self.transactionList, columns=["日期", "支出項目", "明細", "金額"])
    df.sort_values(by=["日期"], inplace=True)
    df.to_excel(f'./statements/{personName}/outputFile/{bankName}{date}.xlsx', index=False)

    return

  def getStatmentCSVBalance(self, filePath, bankName):
    if bankName == "discover":
      return self.processDiscoverCSV(filePath)
    elif bankName == "capitalOne":
      return self.processCapitalOneCSV(filePath)
    else:
      print(f"getStatmentCSVBalance failed: Bank: {bankName}")
      return -1

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
  