import sys

from objects.banks.discover.discover_cashBack import DiscoverCashBack
from objects.banks.capitalOne.capitalOne import CapitalOne
from objects.people.stevenLuHome.stevenLuHome import stevenLuHome

def createObjects(bankName, cardType, statementDate, personName):
  # create the object of the bank class
  if bankName == "discover" and cardType == "cashBack":
    bankObj = DiscoverCashBack(bankName, cardType, statementDate)
  elif bankName == "capitalOne":
    bankObj = CapitalOne(bankName, cardType, statementDate)
  else:
    print(f'Bank not supported: {bankName}')
    sys.exit(1)

  # create the object of the people class
  if personName == "stevenLu":
    personObj = stevenLuHome()
  else:
    print(f'Person not supported: {personName}')
    sys.exit(1)

  return bankObj, personObj
