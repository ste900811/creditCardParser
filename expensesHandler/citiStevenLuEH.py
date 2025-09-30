def expensesHandler(textArray, amount):

  if textArray[0] == "McDonalds":
    return "餐飲", "McDonalds", amount
  if textArray[0] == "STARBUCKS":
    return "點心飲料", "Starbucks", amount
  if textArray[0] == "Groupon" or textArray[0] == "Groupon,":
    return "待分類", "Groupon", amount
  if textArray[0] == "KFC":
    return "餐飲", "KFC", amount
  if textArray[0] == "REGAL":
    return "休閒娛樂", "Regal", amount
  if textArray[0] == "O'CHARLEY'S":
    return "餐飲", "O'Charley's", amount
  if textArray[0] == "SKECHERS-USA":
    return "治裝費", "Skechers", amount
  if textArray[0] == "WENDY'S":
    return "餐飲", "Wendy's", amount
  if textArray[0] == "WAL-MART":
    return "日常用品", "Walmart", amount
  if textArray[0] == "VIOC":
    return "交通工具", "Valvoline", amount
  if textArray[0] == "SAMSCLUB":
    return "青菜水果", "Sam's Club", amount
  if textArray[0] == "STAPLES":
    return "日常用品", "Staples", amount
  if textArray[0] == "MARC'S":
    return "青菜水果", "Marc's", amount
  if textArray[0] == "SUNOCO":
    return "交通工具", "Gas", amount
  if textArray[0] == "PUCCINI":
    return "餐飲", "Puccini", amount
  if textArray[0] == "WALGREENS":
    return "生活開銷", "Walgreens", amount

  if len(textArray) == 1:
    return False, False, 0.0

  if textArray[0] == "MEMBERSHIP" and textArray[1] == "FEE":
    return "休閒娛樂", "Citi Membership", amount
  if textArray[0] == "UEP*LU" and textArray[1] == "CHA":
    return "點心飲料", "Lu Cha", amount
  if textArray[0] == "DAIRY" and textArray[1] == "QUEEN":
    return "點心飲料", "Dairy Queen", amount
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount <= 20:
    return "餐飲", "Sam's Club", amount
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount > 20:
    return "青菜水果", "Sam's Club", amount
  if textArray[0] == "KOREA" and textArray[1] == "HOUSE":
    return "餐飲", "Korea House", amount
  if textArray[0] == "BURGER" and textArray[1] == "KING":
    return "餐飲", "Burger King", amount
  if textArray[0] == "STORMING" and textArray[1] == "CRAB":
    return "餐飲", "Storming Crab", amount
  if textArray[0] == "PROGRESSIVE" and textArray[1] == "*INSURANCE":
    return "交通工具", "Progressive Insurance", amount
  if textArray[0] == "WM" and textArray[1] == "SUPERCENTER":
    return "日常用品", "Walmart", amount
  if textArray[0] == "CLATTER" and textArray[1] == "Frostburg":
    return "餐飲", "Clatter", amount
  if textArray[0] == "TRADER" and textArray[1] == "JOE":
    return "青菜水果", "Trader Joe", amount
  if textArray[0] == "BEST" and textArray[1] == "BUY":
    return "生活開銷", "Best Buy", amount
  if textArray[0] == "BANGKOK" and textArray[1] == "THAI":
    return "餐飲", "Bangkok Thai", amount
  if textArray[0] == "TINK" and textArray[1] == "HOLL":
    return "青菜水果", "Tink Holl", amount
  if textArray[0] == "UMAMI" and textArray[1] == "NOODLE":
    return "餐飲", "Umami Noodle", amount
  if textArray[0] == "OLIVE" and textArray[1] == "GARDEN":
    return "餐飲", "Olive Garden", amount

  if len(textArray) == 2:
    return False, False, 0.0

  if textArray[0] == "Hunan" and textArray[1] == "of" and textArray[2] == "Stow":
    return "餐飲", "Hunan of Stow", amount
  if textArray[0] == "CITI" and textArray[1] == "TRAVEL" and textArray[2] == "HOTEL":
    return "休閒娛樂", "Citi Travel Hotel", amount
  if textArray[0] == "PARK" and textArray[1] == "TO" and textArray[2] == "SHOP":
    return "青菜水果", "Park to Shop", amount
  if textArray[0] == "TEXAS" and textArray[1] == "GRILL" and textArray[2] == "HOUSE":
    return "餐飲", "Texas Grill House", amount
  if textArray[0] == "BALTIMORE" and textArray[1] == "ST" and textArray[2] == "GRILL":
    return "餐飲", "Baltimore St Grill", amount
  if textArray[0] == "HARVARD" and textArray[1] == "BUS" and textArray[2] == "EDUCATION":
    return "生活開銷", "Georgia Tech", amount
  if textArray[0] == "CAM" and textArray[1] == "ASIA" and textArray[2] == "SUPERMARKET":
    return "青菜水果", "Cam Asia Supermarket", amount

  if len(textArray) == 3:
    return False, False, 0.0
  
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOW":
    return "餐飲", "The Cafe in Stow", amount
  if textArray[0] == "Merchant" and textArray[1] == "Offers" and textArray[2] == "Credit" and textArray[3] == "NY":
    return "休閒娛樂", "Citi Merchant Offers", amount


  if len(textArray) == 4:
    return False, False, 0.0

  if textArray[0] == "FH*" and textArray[1] == "WESTERN" and textArray[2] == "MARYLAND" and textArray[3] == "S" and textArray[4] == "CUMBERLAND":
    return "休閒娛樂", "FH Western Maryland", amount
  if textArray[0] == "SPLURGE" and textArray[1] == "CREDIT" and textArray[2] == "BESTBUY" and textArray[3] == "Rebate":
    return "生活開銷", "Best Buy Rebate", amount
  if textArray[0] == "ANANA" and textArray[1] == "FAMILY," and textArray[2] == "LLC" and textArray[3] == "CLEVELAND":
    return "餐飲", "Anana Family", amount
  if textArray[0] == "CITY" and textArray[1] == "OF" and textArray[2] == "CUYAHOGA" and textArray[3] == "FALLS":
    return "交通工具", "Parking", amount

  return False, False, 0.0
