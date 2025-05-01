import sys
from objects.discover import Discover
from objects.capitalOne import CapitalOne

def main(bankName, statementDate):

  # create the object of the bank class
  if bankName == "discover":
    parserObj = Discover(statementDate)
  elif bankName == "capitalOne":
    parserObj = CapitalOne(statementDate)
  else:
    print(f'Bank not supported: {bankName}')
    sys.exit(1)

  # get the statement balance from PDF file
  try:
    parserObj.statmentPDFBalance = parserObj.getStatmentPDFBalance(f'./statements/{bankName}/{statementDate}.pdf')
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)
  
  # get the statement balance from CSV file
  try:
    parserObj.statmentCSVBalance = parserObj.getStatmentCSVBalance(f'./statements/{bankName}/{statementDate}.csv')
  except FileNotFoundError as e:
    print(e)
    sys.exit(1)

  # check if the statement balance from PDF and CSV file are same
  if bankName == "capitalOne":
    assert round(parserObj.statmentPDFBalance - parserObj.PDFCreditsAmount, 2) == round(parserObj.statmentCSVBalance, 2), \
      f"CapitalOne: PDF balance: {parserObj.statmentPDFBalance}, CSV balance: {parserObj.statmentCSVBalance}, Credits amount: {parserObj.PDFCreditsAmount}"


  # output CSV file
  parserObj.outputCSVStatement(bankName, statementDate)
  return

if __name__ == "__main__":

  if len(sys.argv) < 3:
    print("Command line arguments not enough")
    sys.exit(1)
  elif len(sys.argv) > 3:
    print("Command line arguments too many")
    sys.exit(1)

  bankName, statementDate = sys.argv[1], sys.argv[2]
  main(bankName, statementDate)
  print("Done")
