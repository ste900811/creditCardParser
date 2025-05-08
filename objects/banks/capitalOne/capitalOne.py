from objects.banks.banks import Banks
from pypdf import PdfReader
import pandas as pd

class CapitalOne(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.cardType = cardType
    self.PDFCreditsAmount = 0.0

  def getStatmentPDFBalance(self, filePath):
    print("CapitalOne: getStatmentPDFBalance")

    readingFlag = False

    reader = PdfReader(filePath)
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):

        # Using three if statements to read the Credits amount
        if line == "YI-YANG LU #1052: Transactions ":
          readingFlag = False
          continue

        if readingFlag:
          if line == "Trans Date Post Date Description Amount ":
            continue
          else:
            amount = line.split("$")
            self.PDFCreditsAmount += float(amount[1][:-1])

        if line == "YI-YANG LU #1052: Payments, Credits and Adjustments ":
          readingFlag = True
          continue
          
        # Find the balance in the PDF file
        if line[:36] == "YI-YANG LU #1052: Total Transactions":
          return float(line[38:39]+line[40:46])

    assert False, "CapitalOne: getStatmentPDFBalance: No balance found in PDF file"
