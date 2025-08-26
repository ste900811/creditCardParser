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

  if len(textArray) == 2:
    return False, False, 0.0

  if textArray[0] == "Hunan" and textArray[1] == "of" and textArray[2] == "Stow":
    return "餐飲", "Hunan of Stow", amount
  if textArray[0] == "CITI" and textArray[1] == "TRAVEL" and textArray[2] == "HOTEL":
    return "休閒娛樂", "Citi Travel Hotel", amount
  if textArray[0] == "PARK" and textArray[1] == "TO" and textArray[2] == "SHOP":
    return "青菜水果", "Park to Shop", amount

  if len(textArray) == 3:
    return False, False, 0.0
  
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOW":
    return "餐飲", "The Cafe in Stow", amount

  if len(textArray) == 4:
    return False, False, 0.0

  if textArray[0] == "FH*" and textArray[1] == "WESTERN" and textArray[2] == "MARYLAND" and textArray[3] == "S" and textArray[4] == "CUMBERLAND":
    return "休閒娛樂", "FH Western Maryland", amount

  return False, False, 0.0