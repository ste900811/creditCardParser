from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class AMEX(Banks):
  def __init__(self, bankName, cardType, statementDate, cardNum):
    super().__init__(bankName, cardType, statementDate, cardNum)
    self.creditAmount = 0.0
    self.payments = 0.0
    self.PDFPreviousBalance = -99999.99

  def getStatmentPDFBalance(self, filePath):
    # print(f"Getting statement balance from PDF file: {filePath}")

    reader = PdfReader(filePath)
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if line.startswith("Account Ending"):
          self.cardLast5Digits = line.split("-")[1][:5]
        if "New Balance $" in line:
          self.PDFNewBalance = float(line.split("$")[-1].replace(",", ""))
        if line.startswith("Interest Charged$"):
          self.PDFPreviousBalance = float(line.split("$")[-1].replace(",", ""))
        if "Account Ending" in line and "Closing Date" in line:
          self.cardLast5Digits = line.split("Account Ending")[-1].split("-")[1][:5]

    if self.PDFInfoCheck():
      return self.PDFNewBalance

    assert False, f'{self.bankName}_{self.cardType}: getStatmentPDFBalance: No balance found in PDF file'
