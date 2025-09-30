import sys
import math

from mainFunctions.createObjects import createObjects

def main(bankName, cardType, nameOnStatement, statementDate):
  print(f"Bank Name: {bankName}")
  print(f"Card Type: {cardType}")
  print(f"Name on Statement: {nameOnStatement}")
  print(f"Statement Date: {statementDate}", end="\n\n")

  # create the object of the bank and people class
  bankObj, personObj = createObjects(bankName, cardType, statementDate, nameOnStatement)

  # get the statement balance from PDF file
  try:
    pdfFilePath = f'./statements/{nameOnStatement}/{bankName}/{cardType}/{statementDate}.pdf'
    bankObj.statmentPDFBalance = bankObj.getStatmentPDFBalance(pdfFilePath)
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)
  
  # get the statement balance from CSV file
  try:
    csvFilePath = f'./statements/{nameOnStatement}/{bankName}/{cardType}/{statementDate}.csv'
    bankObj.statmentCSVBalance = personObj.getStatmentCSVBalance(csvFilePath, bankName)
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)

  # check if the statement balance from PDF and CSV file are same
  if bankName == "capitalOne":
    assert round(bankObj.statmentPDFBalance - bankObj.PDFCreditsAmount, 2) == round(bankObj.statmentCSVBalance, 2), \
      f"CapitalOne: PDF balance: {bankObj.statmentPDFBalance}, CSV balance: {bankObj.statmentCSVBalance}, Credits amount: {bankObj.PDFCreditsAmount}"
  elif bankName == "discover":
    assert round(bankObj.statmentPDFBalance, 2) == round(bankObj.statmentCSVBalance, 2), \
      f"Discover: PDF balance: {bankObj.statmentPDFBalance}, CSV balance: {bankObj.statmentCSVBalance}"
  elif bankName == "AMEX":
    assert math.isclose(bankObj.statmentPDFBalance, 
                        bankObj.statmentCSVBalance + bankObj.PDFPreviousBalance \
                        - bankObj.creditAmount + bankObj.payments), \
      f'{bankObj.bankName}_{bankObj.cardType}: PDF and CSV statement balance do not match\n \
        PDF balance: {bankObj.statmentPDFBalance}\n \
        CSV balance: {bankObj.statmentCSVBalance}\n \
        Previous balance: {bankObj.PDFPreviousBalance}\n \
        Payments amount: {bankObj.payments}\n \
        Credits amount: {bankObj.creditAmount}'
  elif bankName == "Citi":
    assert math.isclose(bankObj.statmentPDFBalance, 
                        bankObj.previousBalance + bankObj.creditsAmount \
                        + bankObj.paymentsAmount + bankObj.purchasesAmount), \
      f"{bankObj.bankName}_{bankObj.cardType}: PDF and CSV statement balance do not match\n \
        PDF balance: {bankObj.statmentPDFBalance}\n \
        Previous balance: {bankObj.previousBalance}\n \
        Payments amount: {bankObj.paymentsAmount}\n \
        Credits amount: {bankObj.creditsAmount}\n \
        Purchases amount: {bankObj.purchasesAmount}"
  else:
    assert False, f"Bank not supported: {bankName}"

  # output CSV file
  personObj.outputCSVStatement(bankObj)
  return

# Example: python main.py stevenLu discover 250120
if __name__ == "__main__":

  if len(sys.argv) < 5:
    print("Command line arguments not enough")
    sys.exit(1)
  elif len(sys.argv) > 5:
    print("Command line arguments too many")
    sys.exit(1)

  bankName, cardType, nameOnStatement, statementDate = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
  main(bankName, cardType, nameOnStatement, statementDate)
  print("Done")
