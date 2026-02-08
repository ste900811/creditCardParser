from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class Citi(Banks):
  def __init__(self, bankName, cardType, statementDate, cardNum):
    super().__init__(bankName, cardType, statementDate, cardNum)
    self.newBalance = None
    self.previousBalance = None
    self.payments = None
    self.credits = None
    self.purchases = None
    self.purchasesCSV = 0
    self.creditsCSV = 0

  def getStatmentPDFBalance(self, filePath):
    print("Citi: getStatmentPDFBalance")

    reader = PdfReader(filePath)
    curL, p1L, p2L = None, None, None # Current Line, Previous 1 Line, Previous 2 Line

    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        curL, p1L, p2L = line, curL, p1L
        if p2L is None:
          continue
        if p2L.startswith("New balance as of"):
          self.newBalance = float(line.split("$")[-1].replace(",", ""))
        if p2L == "Previous balance":
          self.previousBalance = float(line.split("$")[-1].replace(",", ""))
        if p2L == "Payments":
          self.payments = float(line.split("$")[-1].replace(",", ""))
        if p2L == "Credits":
          self.credits = float(line.split("$")[-1].replace(",", ""))
        if p2L == "Purchases":
          self.purchases = float(line.split("$")[-1].replace(",", ""))
    
    if self.PDFInfoCheck():
      return self.newBalance

    assert False, f'{self.bankName}_{self.cardType}: Citi: getStatmentPDFBalance: No balance found in PDF file\n \
                    self.PDFCreditsAmount: {self.PDFCreditsAmount}\n \
                    self.previousBalance: {self.previousBalance}\n \
                    self.payments: {self.payments}\n \
                    self.credits: {self.credits}\n \
                    self.purchases: {self.purchases}'
    
  def PDFInfoCheck(self):
    return self.newBalance is not None and self.previousBalance is not None and \
           self.payments is not None and self.credits is not None and self.purchases is not None
  