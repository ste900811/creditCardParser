import sys
import math

from mainFunctions.createObjects import createObjects

def main(bankName, cardType, nameOnStatement, statementDate_cardNum):
  statementDate, cardNum = statementDate_cardNum.split("_")[0], statementDate_cardNum.split("_")[1]
  print(f"Bank Name: {bankName}")
  print(f"Card Type: {cardType}")
  print(f"Name on Statement: {nameOnStatement}")
  print(f"Statement Date: {statementDate}")
  print(f'Card Last 4 Digits: {cardNum}', end="\n\n")

  # create the object of the bank and people class
  bankObj, personObj = createObjects(bankName, cardType, statementDate, nameOnStatement, cardNum)

  # get the statement balance from PDF file
  try:
    pdfFilePath = f'./statements/{nameOnStatement}/{bankName}/{cardType}/{statementDate_cardNum}.pdf'
    bankObj.statmentPDFBalance = bankObj.getStatmentPDFBalance(pdfFilePath)
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)
  
  # get the statement balance from CSV file
  try:
    csvFilePath = f'./statements/{nameOnStatement}/{bankName}/{cardType}/{statementDate_cardNum}.csv'
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
  elif bankName == "USBank":
    pass
    # assert math.isclose(bankObj.newBalance, bankObj.statmentCSVBalance), \
    # f'bankObj.statmentPDFBalance: {bankObj.statmentPDFBalance}\n \
    #   bankObj.statmentCSVBalance: {bankObj.statmentCSVBalance}\n \
    #   bankObj.previousBalance: {bankObj.previousBalance}\n \
    #   bankObj.payments: {bankObj.payments}\n \
    #   bankObj.otherCredits: {bankObj.otherCredits}\n \
    #   bankObj.purchases: {bankObj.purchases}\n \
    #   bankObj.newBalance: {bankObj.newBalance}'
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

  bankName, cardType, nameOnStatement, statementDate_cardNum = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
  main(bankName, cardType, nameOnStatement, statementDate_cardNum)
  print("Done")
