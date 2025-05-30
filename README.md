Currently only run on the Windows machine, using below example terminal code to run the main file:
python main.py discover cashBack stevenLu 250216
  discover = name of the bank
  cashBack = credit card type
  stevenLu = credit card holder
  250216 = date of the creaditcard statment

bankName and cardType:
  capitalOne
    ventureX
  discover
    cashBack
  AMEX
    BusinessGoldCard
    HiltonHonorsAspireCard
    HiltonHonorsSurpassCard

name:
  amyLu
  howardYao
  maridaCheng
  stevenLu

expensesHanddler Folder is holding all the expenses parsing places
mainFunctions Folder is the function using in the main.py
objects Folder is the place holding all the calsses
  banks = banks such as discover, capitalOne, etc
  people = group by the household, because different household will has different way to extract and output data
statements Folder is the place holding all the credit card statement, it then group by card holder name
