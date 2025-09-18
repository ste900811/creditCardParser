def expensesHandler(textArray, transactionAmount):
  # Section only need one word to categorize
  if textArray[0] == "WALMART":
    return "日常用品", "Walmart"
  if textArray[0] == "ACME":
    return "青菜水果", "Acme"
  if textArray[0] == "GIANT-EAGLE":
    return "青菜水果", "Giant Eagle"
  if textArray[0] == "CHIPOTLE":
    return "餐飲", "Chipotle"
  if textArray[0] == "ALDI":
    return "青菜水果", "Aldi"
  if textArray[0] == "APPLE.COM/BILL":
    return "休閒娛樂", "Apple.com"
  if textArray[0] == "MEIJER":
    return "青菜水果", "Meijer"
  if textArray[0] == "AMAZON":
    return "日常用品", "Amazon"
  if textArray[0][:10] == "AMAZON.COM":
    return "日常用品", "Amazon"
  if textArray[0] == "TARGET":
    return "日常用品", "Target"
  if textArray[0] == "MCDONALDS" or textArray[0] == "MCDONALD'S":
    return "餐飲", "McDonalds"
  if textArray[0] == "GRAETERS38":
    return "點心飲料", "Graeter's ice cream"
  if textArray[0] == "LOWE'S" or textArray[0] == "LOWES.COM":
    return "日常用品", "Lowe's"
  if textArray[0] == "DUNKIN":
    return "點心飲料", "Dunkin"
  if textArray[0] == "KFC":
    return "餐飲", "KFC"
  if textArray[0] == "MARC'S":
    return "青菜水果", "Marc's"
  if textArray[0] == "SHEETZ" and transactionAmount < 20:
    return "餐飲", "Sheetz"
  
  # Section need two sections to categorize
  if textArray[0] == "DAIRY" and textArray[1] == "QUEEN":
    return "點心飲料", "Dairy Queen"
  if textArray[0] == "RAISING" and textArray[1] == "CANES":
    return "餐飲", "Raising Cane's"
  if textArray[1] == "STATEMENT" and textArray[2] == "CREDIT":
    return "移除", "Statement Credit"
  if textArray[0] == "SAM'S" and textArray[1] == "CLUB" and transactionAmount > 20:
    return "日常用品", "Sam's Club"
  if textArray[0] == "SAM'S" and textArray[1] == "CLUB" and transactionAmount <= 20:
    return "餐飲", "Sam's Club"
  if textArray[0] == "WELLNESS" and textArray[1] == "CENTRE":
    return "養育費", "Swimming Lesson"
  if textArray[0] == "LAZ" and textArray[1] == "PARKING":
    return "交通工具", "Parking"
  if textArray[0] == "AMZN" and textArray[1] == "MKTP":
    return "日常用品", "Amazon"
  if textArray[0] == "YY" and textArray[1] == "TIME":
    return "餐飲", "YY Time"
  if textArray[0] == "ASIA" and textArray[1] == "GARDENS":
    return "餐飲", "Asia Gardens"
  if textArray[0] == "KING" and textArray[1] == "DRAGON":
    return "餐飲", "King Dragon"
  if textArray[0] == "BANGKOK" and textArray[1] == "THAI":
    return "餐飲", "Bangkok Thai"
  if textArray[0] == "UEP*PACIFIC" and textArray[1] == "EAST":
    return "餐飲", "Pacific East"
  if textArray[0] == "PANERA" and textArray[1] == "BREAD":
    return "餐飲", "Panera Bread"
  if textArray[0] == "ACE" and textArray[1] == "HDWE":
    return "日常用品", "Ace Hardware"
  if textArray[0] == "BURGER" and textArray[1] == "KING":
    return "餐飲", "Burger King"
  if textArray[0] == "WENDYS" and textArray[1] == "1793":
    return "餐飲", "Wendys"
  if textArray[0] == "UMAMI" and textArray[1] == "NOODLE":
    return "餐飲", "Umami Noodle"
  if textArray[0] == "KOREA" and textArray[1] == "HOUSE":
    return "餐飲", "Korea House"
  if textArray[0] == "TST*SPAGHETTI" and textArray[1] == "WAREHOUS":
    return "餐飲", "Spaghetti Warehouse"
  if textArray[0] == "PANDA" and textArray[1] == "EXPRESS":
    return "餐飲", "Panda Express"
  if textArray[0] == "TRADER" and textArray[1] == "JOE":
    return "青菜水果", "Trader Joe's"
  if textArray[0] == "TINK" and textArray[1] == "HOLL":
    return "青菜水果", "Tink Holl"
  if textArray[0] == "GET" and textArray[1] == "GO":
    return "交通工具", "Get Go"
  if textArray[0] == "SAMS" and textArray[1] == "FUEL":
    return "交通工具", "Gas"
  if textArray[0] == "SAMS" and textArray[1] == "STORE" and transactionAmount < 20:
    return "餐飲", "Sam's Club"
  if textArray[0] == "SAMS" and textArray[1] == "STORE" and transactionAmount >= 20:
    return "日常用品", "Sam's Club"
  if textArray[0] == "CIRCLE" and textArray[1] == "K" and transactionAmount >= 50:
    return "Checking", "Circle K"
  if textArray[0] == "CIRCLE" and textArray[1] == "K" and transactionAmount < 50:
    return "交通工具", "Gas"
  if textArray[0] == "SQ" and textArray[1] == "*TENSUKE" and textArray[2] == "RAMEN":
    return "餐飲", "Tensuke Ramen"
  if textArray[0] == "ACE" and textArray[1] == "HARDWARE" and textArray[2] == "CORPORATION":
    return "日常用品", "Ace Hardware"
  if textArray[0] == "THE" and textArray[1] == "HOME" and textArray[2] == "DEPOT":
    return "日常用品", "The Home Depot"
  if textArray[0] == "TST*" and textArray[1] == "MANGO" and textArray[2] == "MANGO":
    return "點心飲料", "Mango Mango"
  if textArray[0] == "LINVILLE" and textArray[1] == "FOOD" and textArray[2] == "SERVICE":
    return "餐飲", "Linville Food Service"
  if textArray[0] == "MRS" and textArray[1] == "YODERS" and textArray[2] == "KITCHEN":
    return "餐飲", "Mrs Yoder's Kitchen"
  if textArray[0] == "TST*" and textArray[1] == "ALADDIN'S" and textArray[2] == "EATERY":
    return "餐飲", "Aladdin's Eatery"
  
  # Section need more than four sections to categorize
  if textArray[0] == "CITY" and textArray[1] == "OF" and textArray[2] == "CUYAHOGA" and textArray[3] == "FALLS":
    return "休閒娛樂", "City of Cuyahoga Falls"
  if textArray[0] == "PARK" and textArray[1] == "TO" and textArray[2] == "SHOP" and textArray[3] == "CLEVELAND":
    return "青菜水果", "Park to Shop"
  if textArray[0] == "PY" and textArray[1] == "*KUNG" and textArray[2] == "FU" and textArray[3] == "TEA":
    return "點心飲料", "Kung Fu Tea"
  if textArray[0] == "GOGI" and textArray[1] == "EN" and textArray[2] == "K" and textArray[3] == "BBQ":
    return "餐飲", "Gogi En K BBQ"
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOW":
    return "餐飲", "The Cafe In Stow"
  if textArray[0] == "SQ" and textArray[1] == "*MING'S" and textArray[2] == "BUBBLE" and textArray[3] == "TEA":
    return "餐飲", "Ming's Bubble Tea"

  # if didn't find the category, return False
  return False, False
