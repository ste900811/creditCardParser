import sys

from objects.banks.discover.discover import Discover
from objects.banks.capitalOne.capitalOne import CapitalOne
from objects.banks.AMEX.AMEX import AMEX
from objects.banks.Citi.citi import Citi
from objects.banks.USBank.USBank import USBank

from objects.people.stevenLuHome.stevenLuHome import stevenLuHome
from objects.people.amyLuHome.amyLuHome import amyLuHome

def createObjects(bankName, cardType, statementDate, personName, cardNum):
  # create the object of the bank class
  if bankName == "discover" and cardType == "cashBack" and personName == "stevenLu":
    bankObj = Discover(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  elif bankName == "capitalOne" and cardType == "ventureX" and personName == "maridaCheng":
    bankObj = CapitalOne(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  elif bankName == "AMEX" and cardType == "BusinessGoldCard" and personName == "maridaCheng":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = amyLuHome(personName)
  elif bankName == "AMEX" and cardType == "HiltonHonorsAspireCard" and personName == "amyLu":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = amyLuHome(personName)
  elif bankName == "AMEX" and cardType == "HiltonHonorsAspireCard" and personName == "howardYao":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = amyLuHome(personName)
  elif bankName == "AMEX" and cardType == "HiltonHonorsSurpassCard" and personName == "stevenLu":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  elif bankName == "AMEX" and cardType == "HiltonHonorsAspireCard" and personName == "stevenLu":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  elif bankName == "Citi" and cardType == "strataElite" and personName == "stevenLu":
    bankObj = Citi(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  elif bankName == "AMEX" and cardType == "AMEXGoldCard" and personName == "howardYao":
    bankObj = AMEX(bankName, cardType, statementDate, cardNum)
    personObj = amyLuHome(personName)
  elif bankName == "USBank" and cardType == "BusinessTripleCashRewards" and personName == "howardYao":
    bankObj = USBank(bankName, cardType, statementDate, cardNum)
    personObj = stevenLuHome(personName)
  else:
    print(f'createObject failed: Bank: {bankName}, Card Type: {cardType}, Person: {personName}')
    sys.exit(1)

  personObj.addbankObj(bankObj)

  return bankObj, personObj
