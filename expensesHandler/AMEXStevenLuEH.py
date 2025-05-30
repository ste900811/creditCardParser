def expensesHandler(textArray, amount):

  if textArray[0] == "MCDONALD'S":
    return "餐飲", "McDonalds", amount
  if textArray[0] == "STORE" and amount < 15:
    return "餐飲", "McDonalds", amount
  if textArray[0] == "WENDY'S":
    return "餐飲", "Wendy's", amount
  if textArray[0] == "APPB":
    return "餐飲", "Applebee's", amount

  if len(textArray) == 1:
    return False, False, amount
  
  if textArray[0] == "DAIRY" and textArray[1] == "QUEEN":
    return "點心飲料", "DairyQueen", amount
  if textArray[0] == "YY" and textArray[1] == "TIME":
    return "餐飲", "YY Time", amount
  if textArray[0] == "BANGKOK" and textArray[1] == "THAI":
    return "餐飲", "Bangkok Thai", amount
  if textArray[0] == "MEKONG" and textArray[1] == "LLC":
    return "餐飲", "Mekong LLC", amount
  if textArray[0] == "AMAZON" and textArray[1] == "MARKEPLACE":
    return "日常用品", "Amazon Marketplace", amount
  if textArray[0] == "BUFFALO" and textArray[1] == "WILD":
    return "餐飲", "Buffalo Wild Wings", amount
  if textArray[0] == "MEMBERSHIP" and textArray[1] == "FEE":
    return "休閒娛樂", "AMEX Membership Fee", amount


  if len(textArray) == 2:
    return False, False, amount
  

  if len(textArray) == 3:
    return False, False, amount

  if textArray[0] == "TST*" and textArray[1] == "KPOT" and textArray[2] == "KOREAN" and textArray[3] == "BBQCANTON":
    return "餐飲", "K-Pot Korean BBQ", amount

  if len(textArray) == 4:
    return False, False, amount


  # if didn't find the category, return False
  return False, False, amount