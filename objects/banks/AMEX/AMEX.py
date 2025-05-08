from objects.banks.banks import Banks
from pypdf import PdfReader

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

  # def setUpCategories(self, df):

  #   # Filter out the months
  #   month = set()
  #   for date in df["Date"]:
  #     month.add(date.split("/")[0])

  #   # Create a dictionary for each month
  #   for m in month:
  #     self.categoriesTotal[m] = self.categories.copy()

  #   return

  # def getStatmentCSVBalance(self, filePath):
  #   # print(f"Getting statement balance from CSV file: {filePath}")

  #   df = pd.read_csv(filePath)

  #   # Since there are two different months, need to add the two months separately
  #   self.setUpCategories(df)

  #   csvTotalAmount = 0.0    
  #   for index, row in df.iterrows():
      
  #     # Update the total amount
  #     csvTotalAmount += row["Amount"]

  #     # Update the categories total amount
  #     description = row["Description"].split(" ")
  #     if description[0] == "AplPay" or description[0] == "TN":
  #       description = description[1:]
  #     category = expensesHandler(description, row["Amount"])
  #     month = row["Date"].split("/")[0]

  #     if category == False:
  #       print(description, row["Amount"])
  #       continue

  #     self.categoriesTotal[month][category] += row["Amount"]

  #   return csvTotalAmount
