import pandas as pd

from objects.people.people import people
from expensesHandler.AMEXAmyLuEH import expensesHandler as AMEXEH

class amyLuHome(people):
  def __init__(self, nameOnStatement):
    super().__init__(nameOnStatement)
    self.categories = {
      "Phone": 0,
      "Grocery": 0,
      "Dining": 0,
      "Gas": 0,
      "Charge": 0,
      "Travel": 0,
      "Entertainment": 0,
      "Car Expense": 0,
      "Parking": 0,
      "Baby": 0,
      "Daycare": 0,
      "CY Class": 0,
      "RY Class": 0,
      "Others/YL": 0,
      "Computer/Cloud": 0,
      "Other/HY": 0,
      "Medical Expense": 0,
      "Bus Exp/Prof Fee": 0,
      "House Expense": 0,
      "Amazon": 0,
      "fcpa": 0,
      "AMEX FEE": 0,
      "HOA": 0,
      "1888 lillian electric": 0,
      "1333 gas": 0,
      "1333 electricity": 0,
      "Youtube": 0,
      "Steven": 0,
      "Software": 0,
      "Medical Expense": 0,
      "Condo Fee": 0
    }
    self.categoriesTotal = dict()

  def outputCSVStatement(self, bankObj):

    outputFilePath = f'./statements/{self.nameOnStatement}/outputFile/{bankObj.bankName}_{bankObj.cardType}_{bankObj.StatementDate}_{bankObj.cardLast5Digits}.csv'

    keys = [key for key in self.categories]
    title = ["Month"] + keys

    data = []
    for key, value in self.categoriesTotal.items():
      tempArray = [key]
      for k in keys:
        tempArray.append(value[k])
      data.append(tempArray)
    
    df = pd.DataFrame(data, columns=title)
    df.sort_values(by=["Month"], inplace=True)
    df.to_csv(outputFilePath, index=False)

    return
  
  def setUpCategories(self, df):

    # Filter out the months
    month = set()
    for date in df["Date"]:
      month.add(date.split("/")[0])

    # Create a dictionary for each month
    for m in month:
      self.categoriesTotal[m] = self.categories.copy()

    return
  
  def getStatmentCSVBalance(self, filePath, bankName):
    if bankName == "AMEX":
      return self.processAMEXCSV(filePath)
    else:
      print(f"getStatmentCSVBalance failed: Bank: {bankName}")
      return -1

  def processAMEXCSV(self, filePath):
    # print(f"Getting statement balance from CSV file: {filePath}")

    df = pd.read_csv(filePath)

    # Since there are two different months, need to add the two months separately
    self.setUpCategories(df)

    csvTotalAmount = 0.0    
    for index, row in df.iterrows():

      if row["Description"] == "AUTOPAY PAYMENT - THANK YOU":
        self.bankObj.payments += row["Amount"]
        continue

      # Update the categories total amount
      description = row["Description"].split(" ")
      if description[0] == "AplPay" or description[0] == "TN":
        description = description[1:]
      category = AMEXEH(description, row["Amount"])
      month = row["Date"].split("/")[0]

      if category == False:
        print(description, row["Amount"])
        continue
      else:
        if row["Amount"] < 0:
          self.bankObj.creditAmount += row["Amount"]
          csvTotalAmount += row["Amount"]
        # Update the total amount
        csvTotalAmount += row["Amount"]
      
      try:
        self.categoriesTotal[month][category] += row["Amount"]
      except KeyError:
        print(f'No category found: {description} {row["Amount"]}')
        continue

    return csvTotalAmount
  