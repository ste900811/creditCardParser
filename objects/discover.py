from objects.banks import Banks
from pypdf import PdfReader
import pandas as pd
from expensesHandler.discoverEH import expensesHandler

class Discover(Banks):
  def __init__(self, statementDate):
    super().__init__(statementDate)

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

  def getStatmentCSVBalance(self, filePath):
    print("Discover: getStatmentCSVBalance")

    csvTotalAmount = 0.0
    df = pd.read_csv(filePath)

    for index, row in df.iterrows():
      if row["Category"] == "Awards and Rebate Credits" or row["Category"] == "Payments and Credits":
        continue

      category, detail = expensesHandler(row["Description"].split(" "), row["Amount"])

      if category == False:
        print(row["Description"].split(" "), row["Amount"])
        continue
      
      csvTotalAmount += row["Amount"]
      self.transactionList.append([row["Trans. Date"][:-5], category, detail, row["Amount"]])

    return csvTotalAmount
