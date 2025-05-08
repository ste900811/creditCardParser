from abc import ABC, abstractmethod
import pandas as pd

class Banks:
  def __init__(self, statementDate):
    self.statmentPDFBalance = -1
    self.statmentCSVBalance = -1
    self.StatementDate = statementDate
    self.transactionList = []

  @abstractmethod
  def getStatmentPDFBalance(self, filePath):
    pass

  @abstractmethod
  def getStatmentCSVBalance(self, filePath):
    pass

  def outputCSVStatement(self, personName, bankName, date):
    print("Banks: outputCSVSatatement")
    df = pd.DataFrame(self.transactionList, columns=["日期", "支出項目", "明細", "金額"])
    df.sort_values(by=["日期"], inplace=True)
    df.to_excel(f'./statements/{personName}/outputFile/{bankName}{date}.xlsx', index=False)
