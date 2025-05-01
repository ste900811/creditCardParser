import sys
from objects.discover import Discover
from objects.capitalOne import CapitalOne

def main(bankName, statementDate):

  if bankName == "discover":
    parserObj = Discover(statementDate)
  elif bankName == "capitalOne":
    parserObj = CapitalOne(statementDate)
  else:
    print(f'Bank not supported: {bankName}')
    sys.exit(1)

  print(parserObj.bankType)
  print(parserObj.StatementBalance)
  print(parserObj.StatementDate)
  return

if __name__ == "__main__":

  if len(sys.argv) < 3:
    print("Command line arguments not enough")
    sys.exit(1)
  elif len(sys.argv) > 3:
    print("Command line arguments too many")
    sys.exit(1)

  bankName, statementDate = sys.argv[1], sys.argv[2]
  # print(f"Bank Name: {bankName}, type: {type(bankName)}")
  # print(f"Statement Date: {statementDate}, type: {type(statementDate)}")
  main(bankName, statementDate)
  print("Done")
