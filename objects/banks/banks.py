from abc import ABC, abstractmethod
import pandas as pd

class Banks:
  def __init__(self, bankName, cardType, statementDate, cardNum):
    self.bankName = bankName
    self.cardType = cardType
    self.StatementDate = statementDate
    self.cardLast4Digits = cardNum
    self.statmentPDFBalance = None
    self.statmentCSVBalance = None
    
  @abstractmethod
  def getStatmentPDFBalance(self, filePath):
    pass

  @abstractmethod
  def getStatmentCSVBalance(self, filePath):
    pass

  @abstractmethod
  def PDFInfoCheck(self):
    pass
