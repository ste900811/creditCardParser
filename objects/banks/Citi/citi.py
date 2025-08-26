from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class Citi(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.cardType = cardType
    self.PDFCreditsAmount = 0.0

  def getStatmentPDFBalance(self, filePath):
    print("Citi: getStatmentPDFBalance")

    reader = PdfReader(filePath)

    for i in range(len(reader.pages)):
      page = reader.pages[i]
      dummyIndex = -5
      for index, line in enumerate(page.extract_text().split("\n")):
        if line[:17] == "New balance as of":
          dummyIndex = index
        if dummyIndex + 2 == index:
          return float(line[1:].replace(",", ""))

    assert False, "Citi: getStatmentPDFBalance: No balance found in PDF file"
    