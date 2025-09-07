from abc import ABC, abstractmethod
import pandas as pd

class Banks:
  def __init__(self, bankName, statementDate):
    self.bankName = None
    self.statmentPDFBalance = -99999.99
    self.statmentCSVBalance = -99999.99
    self.StatementDate = statementDate
    self.bankName = bankName
    self.cardLast5Digits = ""
    
  @abstractmethod
  def getStatmentPDFBalance(self, filePath):
    pass

  @abstractmethod
  def getStatmentCSVBalance(self, filePath):
    pass

  def filterOutPaymentsMethod(self, array):
    while array[0] == "TST*" or array[0] == "AplPay" or array[0] == "TN":
      array.pop(0)
    return array
