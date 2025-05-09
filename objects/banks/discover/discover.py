from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class Discover(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.cardType = cardType

  def getStatmentPDFBalance(self, filePath):
    reader = PdfReader(filePath)

    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if line[:9] == "Purchases":
          tempArray = line.split("$")
          return float(tempArray[1])

    assert False, "discover: getStatmentPDFBalance: No balance found in PDF file"
