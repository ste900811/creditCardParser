import sys

from objects.banks.discover.discover import Discover
from objects.banks.capitalOne.capitalOne import CapitalOne
from objects.banks.AMEX.AMEX import AMEX

from objects.people.stevenLuHome.stevenLuHome import stevenLuHome
from objects.people.amyLuHome.amyLuHome import amyLuHome

def createObjects(bankName, cardType, statementDate, personName):
  # create the object of the bank class
  if bankName == "discover" and cardType == "cashBack" and personName == "stevenLu":
    bankObj = Discover(bankName, cardType, statementDate)
    personObj = stevenLuHome()
  elif bankName == "capitalOne" and cardType == "ventureX" and personName == "maridaCheng":
    bankObj = CapitalOne(bankName, cardType, statementDate)
    personObj = stevenLuHome()
  elif bankName == "AMEX" and cardType == "BusinessGoldCard" and personName == "maridaCheng":
    bankObj = AMEX(bankName, cardType, statementDate)
    personObj = amyLuHome()
  elif bankName == "AMEX" and cardType == "HiltonHonorsAspireCard" and personName == "amyLu":
    bankObj = AMEX(bankName, cardType, statementDate)
    personObj = amyLuHome()
  elif bankName == "AMEX" and cardType == "HiltonHonorsAspireCard" and personName == "howardYao":
    bankObj = AMEX(bankName, cardType, statementDate)
    personObj = amyLuHome()
  else:
    print(f'createObject failed: Bank: {bankName}, Card Type: {cardType}, Person: {personName}')
    sys.exit(1)

  return bankObj, personObj
