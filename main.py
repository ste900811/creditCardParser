import sys

from mainFunctions.createObjects import createObjects

def main(personName, bankName, cardType, statementDate):
  print(f"Bank Name: {bankName}")
  print(f"Card Type: {cardType}")
  print(f"Statement Date: {statementDate}")
  print(f"Person Name: {personName}")

  bankObj, personObj = createObjects(bankName, cardType, statementDate, personName)

  # get the statement balance from PDF file
  try:
    bankObj.statmentPDFBalance = bankObj.getStatmentPDFBalance(f'./statements/{personName}/{bankName}/{cardType}/{statementDate}.pdf')
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)
  
  # get the statement balance from CSV file
  try:
    bankObj.statmentCSVBalance = personObj.getStatmentCSVBalance(f'./statements/{personName}/{bankName}/{cardType}/{statementDate}.csv')
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
  else:
    assert False, f"Bank not supported: {bankName}"

  # output CSV file
  personObj.outputCSVStatement(personName, bankName, statementDate)
  return

# Example: python main.py stevenLu discover 250120
if __name__ == "__main__":

  if len(sys.argv) < 5:
    print("Command line arguments not enough")
    sys.exit(1)
  elif len(sys.argv) > 5:
    print("Command line arguments too many")
    sys.exit(1)

  personName, bankName, cardType, statementDate = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
  main(personName, bankName, cardType, statementDate)
  print("Done")
