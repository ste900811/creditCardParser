from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class AMEX(Banks):
  def __init__(self, bankName, cardType, statementDate, cardNum):
    super().__init__(bankName, cardType, statementDate, cardNum)
    self.newBalance = None
    self.previousBalance = None
    self.paymentsCredits = None
    self.newCharges = None

  def getStatmentPDFBalance(self, filePath):
    # print(f"Getting statement balance from PDF file: {filePath}")

    reader = PdfReader(filePath)
    interestChargedLineCount = None
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if line.startswith("Account Ending"):
          self.cardLast5Digits = line.split("-")[1][:5]
        if "New Balance $" in line:
          self.newBalance = float(line.split("$")[-1].replace(",", ""))
        if line.startswith("Interest Charged$"):
          self.previousBalance = float(line.split("$")[-1].replace(",", ""))
          interestChargedLineCount = 0
        if "Account Ending" in line and "Closing Date" in line:
          self.cardLast5Digits = line.split("Account Ending")[-1].split("-")[1][:5]
        if interestChargedLineCount == 1:
          self.paymentsCredits = float(line.replace("$", "").replace(",", ""))
        if interestChargedLineCount == 2:
          self.newCharges = float(line.replace("$", "").replace(",", ""))

        if interestChargedLineCount is not None: interestChargedLineCount += 1

    if self.PDFInfoCheck():
      return self.newBalance

    assert False, f'{self.bankName}_{self.cardType}: getStatmentPDFBalance: No balance found in PDF file\n \
                    self.newBalance: {self.newBalance}\n \
                    self.previousBalance: {self.previousBalance}\n \
                    self.paymentsCredits: {self.paymentsCredits}\n \
                    self.newCharges: {self.newCharges}'

  def PDFInfoCheck(self):
    return self.newBalance is not None and self.previousBalance is not None and \
           self.paymentsCredits is not None and self.newCharges is not None

