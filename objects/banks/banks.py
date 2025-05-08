from abc import ABC, abstractmethod
import pandas as pd

class Banks:
  def __init__(self, bankName, statementDate):
    self.bankName = None
    self.statmentPDFBalance = -1
    self.statmentCSVBalance = -1
    self.StatementDate = statementDate

  @abstractmethod
  def getStatmentPDFBalance(self, filePath):
    pass

  @abstractmethod
  def getStatmentCSVBalance(self, filePath):
    pass
