from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class Citi(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.cardType = cardType
    self.PDFCreditsAmount = None
    self.previousBalance = 0.0
    self.paymentsAmount = 0.0
    self.creditsAmount = 0.0
    self.purchasesAmount = 0.0

  def getStatmentPDFBalance(self, filePath):
    print("Citi: getStatmentPDFBalance")

    reader = PdfReader(filePath)

    for i in range(len(reader.pages)):
      page = reader.pages[i]
      SBdummyIndex, PBdummyIndex = float('-inf'), float('-inf')
      for index, line in enumerate(page.extract_text().split("\n")):
        if line[:17] == "New balance as of":
          SBdummyIndex = index
        if SBdummyIndex + 2 == index:
          self.PDFCreditsAmount = float(line[1:].replace(",", ""))
        if line.startswith("Previous balance"):
          PBdummyIndex = index
        if PBdummyIndex + 2 == index:
          self.previousBalance = float(line[1:].replace(",", ""))
    
    if self.PDFCreditsAmount != None:
      return self.PDFCreditsAmount

    assert False, "Citi: getStatmentPDFBalance: No balance found in PDF file"
    