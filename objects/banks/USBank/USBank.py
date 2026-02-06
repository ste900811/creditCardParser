from objects.banks.banks import Banks
from PyPDF2 import PdfReader

class USBank(Banks):
  def __init__(self, bankName, cardType, statementDate, cardNum):
    super().__init__(bankName, cardType, statementDate, cardNum)
    self.previousBalance = None
    self.payments = None
    self.otherCredits = None
    self.purchases = None
    self.newBalance = None

  def getStatmentPDFBalance(self, filePath):
    # print(f"Getting statement balance from PDF file: {filePath}")

    reader = PdfReader(filePath)
    for i in range(len(reader.pages)):
      flag = False
      page = reader.pages[i]
      for line in page.extract_text().split("\n"):
        if "Previous Balance " in line:
          self.previousBalance = float(line.split("$")[-1].replace(",", ""))
        if line.startswith("Payments "):
          self.payments = float(line.split("$")[-1].replace(",", ""))
        if line.startswith("Other Credits "):
          self.otherCredits = float(line.split("$")[-1].replace(",", ""))
        if line.startswith("Purchases "):
          self.purchases = float(line.split("$")[-1].replace(",", ""))
        if line.startswith(".New Balance $"):
          self.newBalance = float(line.split("$")[-1].replace(",", ""))
          flag = True
      if flag: break

    if self.PDFInfoCheck():
      return self.newBalance

    assert False, f'{self.bankName}_{self.cardType}: getStatmentPDFBalance: No balance found in PDF file\n \
                    self.previousBalance: {self.previousBalance}\n \
                    self.payments: {self.payments}\n \
                    self.otherCredits: {self.otherCredits}\n \
                    self.purchases: {self.purchases}\n \
                    self.newBalance: {self.newBalance}'

  def PDFInfoCheck(self):
    return self.otherCredits is not None and self.payments is not None and \
           self.previousBalance is not None and self.newBalance is not None and self.purchases is not None
