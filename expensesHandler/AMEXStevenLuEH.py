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
  if textArray[0] == "POPEYES":
    return "餐飲", "Popeyes", amount
  if textArray[0] == "EXXONMOBIL":
    return "交通工具", "Gas", amount
  if textArray[0] == "DENNY'S":
    return "餐飲", "Denny's", amount
  if textArray[0] == "SPECTRUM":
    return "通訊費", "Spectrum", amount
  if textArray[0] == "DUNKIN":
    return "點心飲料", "Dunkin Donuts", amount
  if textArray[0] == "PANINIS":
    return "餐飲", "Paninis", amount
  if textArray[0] == "TARGET":
    return "日常用品", "Target", amount
  if textArray[0] == "MARC'S":
    return "青菜水果", "Marc's", amount
  if textArray[0] == "RSVP":
    return "休閒娛樂", "RSVP", amount

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
  if textArray[0] == "BURGER" and textArray[1] == "KING":
    return "餐飲", "Burger King", amount
  if textArray[0] == "HAMPTON" and textArray[1] == "INN":
    return "休閒娛樂", "Hampton Inns", amount
  if textArray[0] == "RITTMAN" and textArray[1] == "ORCHADoylestown":
    return "休閒娛樂", "Rittman Orchard", amount
  if textArray[0] == "CAFE" and textArray[1] == "MARK":
    return "點心飲料", "Cafe Mark", amount
  if textArray[0] == "GIANT" and textArray[1] == "EAGLE":
    return "青菜水果", "Giant Eagle", amount
  if textArray[0] == "KYURAMEN" and textArray[1] == "(STRSTRONGSVILLE":
    return "餐飲", "KyuRamen", amount
  if textArray[0] == "UNITED" and textArray[1] == "AIRLINES":
    return "生活開銷", "United Airlines", amount
  if textArray[0] == "NOODLE" and textArray[1] == "KING":
    return "餐飲", "Noodle King", amount
  if textArray[0] == "SAKURA" and textArray[1] == "SUSHI" and "OH" in textArray:
    return "餐飲", "Sakura Sushi", amount
  if textArray[0] == "PANERA" and textArray[1] == "BREAD":
    return "餐飲", "Panera Bread", amount
  if textArray[0] == "CEDAR" and textArray[1] == "POINT":
    return "休閒娛樂", "Cedar Point", amount
  if textArray[0] == "APPLE" and (textArray[1] == "STORE" or textArray[1] == "ONLINE"):
    return "通訊費", "Apple Store", amount
  if textArray[0] == "SAM'S" and textArray[1] == "CLUB":
    return "青菜水果", "Sam's Club", amount
  if textArray[0] == "GET" and textArray[1] == "GO":
    return "交通工具", "Gas", amount
  if textArray[0] == "NYX=PORTAGE" and textArray[1] == "CGARRETTSVILLE":
    return "生活開銷", "Printing", amount

  if len(textArray) == 2:
    return False, False, amount
  
  if textArray[0] == "TST*" and textArray[1] == "ANCHOR" and textArray[2][:3] == "BAM":
    return "餐飲", "Anchor Bar", amount
  if textArray[0] == "PY" and textArray[1] == "*KUNG" and textArray[2] == "FU":
    return "點心飲料", "Kung Fu Tea", amount
  if textArray[0] == "ROUTE" and textArray[1] == "220" and textArray[2] == "DINER":
    return "餐飲", "Route 220 Diner", amount
  if textArray[0] == "A" and textArray[1] == "PLUS" and textArray[2] == "CRAB":
    return "餐飲", "A Plus Crab", amount
  if textArray[0] == "STOW" and textArray[1] == "SOCCER" and textArray[2] == "CLUB":
    return "養育費", "Stow Soccer Club", amount
  if textArray[0] == "TINK" and textArray[1] == "HOLL" and textArray[2] == "ENTERPRISECLEVELAND":
    return "青菜水果", "Tink Holl Enterprise", amount
  if textArray[0] == "STOW-MUNOE" and textArray[1] == "FALLS" and textArray[2] == "BOOSTOW":
    return "餐飲", "Game dining", amount

  if len(textArray) == 3:
    return False, False, amount

  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOW":
    return "餐飲", "The Cafe In Stow", amount
  if textArray[0] == "TST*" and textArray[1] == "KPOT" and textArray[2] == "KOREAN" and textArray[3] == "BBQCANTON":
    return "餐飲", "K-Pot Korean BBQ", amount
  if textArray[0] == "SP" and textArray[1] == "MAEVERLY" and textArray[2] == "STOW" and textArray[3] == "OH":
    return "治裝費", "Maeve", amount
  if textArray[0] == "TOMINI" and textArray[1] == "LLC" and textArray[2] == "Stow" and textArray[3] == "OH":
    return "餐飲", "Phoenix Express", amount
  if textArray[0] == "PARK" and textArray[1] == "TO" and textArray[2] == "SHOP" and textArray[3] == "CLEVELAND":
    return "青菜水果", "Park to Shop", amount
  
  if len(textArray) == 4:
    return False, False, amount

  if textArray[0] == "J" and textArray[1] == "&" and textArray[2] == "K" and textArray[3] == "SUBWAYNORTH" and textArray[4] == "CANTON":
    return "餐飲", "J&K Subway", amount
  if textArray[0] == "GOGI" and textArray[1] == "EN" and textArray[2] == "K" and textArray[3] == "BBQ":
    return "餐飲", "Gogi En K", amount
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "SSTOW":
    return "餐飲", "The Cafe In Stow", amount
  if textArray[0] == "AMEX" and textArray[1] == "Hilton" and textArray[2] == "Honors" and textArray[3] == "Aspire" and textArray[4] == "Flight" and textArray[5] == "Credit":
    return "休閒娛樂", "AMEX Hilton Flight Credit", amount
  if textArray[0] == "MIDWAY" and textArray[1] == "TWIN" and textArray[2] == "DRIVE" and textArray[3] == "INRAVENNA":
    return "餐飲", "Midway Twin Drive In", amount

  # if didn't find the category, return False
  return False, False, amount


# ["SAM'S", 'CLUB', '4750', '4750CUYAHOGA', 'FALLS', 'OH'] 73.5
# ['GET', 'GO', 'STOW', 'OH'] 14.69
# ['STOW', 'SOCCER', 'CLUB', 'INCSTOW', 'OH'] 150.0
# ['TOMINI', 'LLC', 'Stow', 'OH'] 38.5
# ['MOBILE', 'PAYMENT', '-', 'THANK', 'YOU'] -731.62
# ['RSVP', 'NO.', '36', 'STOW', 'OH'] 12.27
# ['STOW-MUNOE', 'FALLS', 'BOOSTOW', 'OH'] 18.0
# ['NYX=PORTAGE', 'CGARRETTSVILLE', 'OH'] 0.5
# ['NYX=PORTAGE', 'CGARRETTSVILLE', 'OH'] 0.5
# ['PARK', 'TO', 'SHOP', 'CLEVELAND', 'OH'] 49.94
# ['TINK', 'HOLL', 'ENTERPRISECLEVELAND', 'OH'] 38.01