def expensesHandler(textArray, amount):

  if textArray[0] == "MCDONALD'S":
    return "餐飲", "McDonalds", amount
  if textArray[0] == "STORE" and amount < 15:
    return "餐飲", "McDonalds", amount
  if textArray[0] == "WENDY'S" or textArray[0] == "WENDYS":
    return "餐飲", "Wendy's", amount
  if textArray[0] == "APPB":
    return "餐飲", "Applebee's", amount
  if textArray[0] == "ACME":
    return "青菜水果", "Acme", amount
  if textArray[0] == "CHICK-FIL-A":
    return "餐飲", "Chick-fil-A", amount
  if textArray[0] == "KFC":
    return "餐飲", "KFC", amount
  if textArray[0] == "CHIPOTLE" and textArray[1] == "MEX":
    return "餐飲", "Chipotle Mexican Grill", amount
  if textArray[0] == "PARKMOBILE":
    return "交通工具", "Parking", amount
  if textArray[0] == "WAL-MART":
    return "日常用品", "Walmart", amount
  if textArray[0] == "SPAGHETTAKRON":
    return "餐飲", "Spaghetti Warehouse", amount

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
  if textArray[0] == "PAPA" and textArray[1] == "JOHN'S":
    return "餐飲", "Papa John's", amount
  if textArray[0] == "TEXAS" and textArray[1][:7] == "ROADHOU":
    return "餐飲", "Texas Roadhouse", amount
  if textArray[0] == "UEP*PACIFIC" and textArray[1] == "EAST":
    return "餐飲", "Pacific East", amount
  if textArray[0] == "TENSUKE" and textArray[1] == "MARKET":
    return "餐飲", "Tensuke Market", amount
  if textArray[0] == "TENSUKE" and textArray[1] == "RAMEN":
    return "餐飲", "Tensuke Ramen", amount
  if textArray[0] == "HOME2" and textArray[1] == "SUITES":
    return "休閒娛樂", "Home2 Suites", amount
  if textArray[0] == "Hilton" and textArray[1] == "Statement":
    return "休閒娛樂", "Hilton Statement", amount
  if textArray[0] == "CAFE" and textArray[1] == "33":
    return "餐飲", "Cafe 33", amount
  if textArray[0] == "HAMPTON" and textArray[1] == "INNS":
    return "休閒娛樂", "Hampton Inns", amount
  if textArray[0] == "MARKET" and textArray[1] == "DISTRICT":
    return "青菜水果", "Giant Eagle", amount
  if textArray[0] == "KOREA" and textArray[1] == "HOUSE":
    return "餐飲", "Korea House", amount
  if textArray[0] == "ROI" and textArray[1] == "ET":
    return "餐飲", "ROI ET", amount
  if textArray[0] == "UEP*LU" and textArray[1] == "CHA":
    return "點心飲料", "Lu Cha", amount
  if textArray[0] == "UMAMI" and textArray[1] == "NOODLE":
    return "餐飲", "Umami Noodle", amount
  if textArray[0] == "OLIVE" and textArray[1] == "GARDEN":
    return "餐飲", "Olive Garden", amount
  if textArray[0] == "BOB" and textArray[1] == "EVANS":
    return "餐飲", "Bob Evans", amount
  if textArray[0] == "BONCHON-" and textArray[1] == "SEVEN":
    return "餐飲", "Bonchon Seven", amount
  if textArray[0] == "KING" and textArray[1] == "DRAGON":
    return "餐飲", "King Dragon", amount
  
  if len(textArray) == 2:
    return False, False, amount
  
  if textArray[0] == "TST*" and textArray[1] == "ANCHOR" and textArray[2][:3] == "BAM":
    return "餐飲", "Anchor Bar", amount
  if textArray[0] == "PY" and textArray[1] == "*KUNG" and textArray[2] == "FU":
    return "點心飲料", "Kung Fu Tea", amount

  if len(textArray) == 3:
    return False, False, amount

  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOW":
    return "餐飲", "The Cafe In Stow", amount
  if textArray[0] == "TST*" and textArray[1] == "KPOT" and textArray[2] == "KOREAN" and textArray[3] == "BBQCANTON":
    return "餐飲", "K-Pot Korean BBQ", amount
  
  if len(textArray) == 4:
    return False, False, amount

  if textArray[0] == "J" and textArray[1] == "&" and textArray[2] == "K" and textArray[3] == "SUBWAYNORTH" and textArray[4] == "CANTON":
    return "餐飲", "J&K Subway", amount
  if textArray[0] == "GOGI" and textArray[1] == "EN" and textArray[2] == "K" and textArray[3] == "BBQ":
    return "餐飲", "Gogi En K", amount
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "SSTOW":
    return "餐飲", "The Cafe In Stow", amount

  # if didn't find the category, return False
  return False, False, amount