from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class AMEX(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.previousBalance = 0.0
    self.cardType = cardType

  def getStatmentPDFBalance(self, filePath):
    # print(f"Getting statement balance from PDF file: {filePath}")

    previousLine, currentLine = "", ""

    reader = PdfReader(filePath)
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        previousLine, currentLine = currentLine, line
        if previousLine == "New Balance" and currentLine[0] == "$":
          amountStr = line[1:].replace(",", "")
          pdfStatementBalance = float(amountStr)
        if line[:17] == "Interest Charged$":
          self.previousBalance = float(line[17:].replace(",", ""))
          return pdfStatementBalance
           
    assert False, f'{self.bankName}_{self.cardType}: getStatmentPDFBalance: No balance found in PDF file'
