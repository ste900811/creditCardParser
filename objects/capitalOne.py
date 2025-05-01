from objects.banks import Banks
from pypdf import PdfReader
import pandas as pd
from expensesHandler.capitalOneEH import expensesHandler

class CapitalOne(Banks):
  def __init__(self, statementDate):
    super().__init__(statementDate)
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

  def getStatmentCSVBalance(self, filePath):
    print("CapitalOne: getStatmentCSVBalance")

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Card No."] == 1052 and row["Credit"] > 0:
        category, detail, amount = expensesHandler(row["Description"].split(" "), -row["Credit"])
        csvTotalAmount += amount
      elif row["Card No."] == 1052 and row["Debit"] > 0:
        category, detail, amount = expensesHandler(row["Description"].split(" "), row["Debit"])
        csvTotalAmount += amount
      else:
        continue
    
      if category == False:
        # print(category, detail)
        print(row["Description"].split(" "), row["Debit"], row["Credit"])
        continue

      month, date = row["Transaction Date"][5:].split("-")
      self.transactionList.append([f'{month}/{date}', category, detail, amount])

    return csvTotalAmount


