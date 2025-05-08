from objects.banks.discover.discover import Discover
from pypdf import PdfReader

class DiscoverCashBack(Discover):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, cardType, statementDate)

  def getStatmentPDFBalance(self, filePath):
    print("Discover: getStatmentPDFBalance")

    reader = PdfReader(filePath)

    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if line[:9] == "Purchases":
          tempArray = line.split("$")
          return float(tempArray[1])

    assert False, "discover: getStatmentPDFBalance: No balance found in PDF file"
