import pandas as pd

from objects.people.people import people
from expensesHandler.discoverStevenLuEH import expensesHandler

class stevenLuHome(people):
  def __init__(self):
    self.transactionList = []

  def outputCSVStatement(self, personName, bankName, date):
    df = pd.DataFrame(self.transactionList, columns=["日期", "支出項目", "明細", "金額"])
    df.sort_values(by=["日期"], inplace=True)
    df.to_excel(f'./statements/{personName}/outputFile/{bankName}{date}.xlsx', index=False)
    
    return

  def getStatmentCSVBalance(self, filePath):
    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Category"] == "Awards and Rebate Credits" or row["Category"] == "Payments and Credits":
        continue

      category, detail = expensesHandler(row["Description"].split(" "), row["Amount"])

      if category == False:
        print(row["Description"].split(" "), row["Amount"])
        continue
      
      csvTotalAmount += row["Amount"]
      self.transactionList.append([row["Trans. Date"][:-5], category, detail, row["Amount"]])

    return csvTotalAmount