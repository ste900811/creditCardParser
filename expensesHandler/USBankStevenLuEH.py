def expensesHandler(textArray, amount):
  
  if textArray[0] == "ParkWhiz,":
    return "交通工具", "Parking"
  if textArray[0] == "SAMSCLUB" and amount <= 20:
    return "餐飲", "Sams Club"
  if textArray[0] == "McDonalds":
    return "餐飲", "McDonalds"
  if textArray[0] == "FANDANGO":
    return "休閒娛樂", "Fandango"
  if textArray[0] == "COLDSTONE":
    return "餐飲", "Cold Stone"
  if textArray[0] == "WAL-MART":
    return "日常用品", "Walmart"
  if textArray[0] == "MARC'S":
    return "青菜水果", "Marc's"
  if textArray[0] == "USPS":
    return "生活開銷", "USPS"
  if textArray[0] == "WINGSTOP":
    return "餐飲", "Wingstop"
  if textArray[0] == "MEIJER":
    return "日常用品", "Meijer"
  if textArray[0] == "GIANT-EAGLE":
    return "青菜水果", "Giant Eagle"
  if textArray[0] == "WALGREENS":
    return "生活開銷", "Walgreens"
  if textArray[0] == "DUNKIN":
    return "點心飲料", "Dunkin Donuts"
  if textArray[0] == "SEATS.AERO":
    return "休閒娛樂", "Seats.Aero"
  if textArray[0] == "CHICK-FIL-A":
    return "餐飲", "Chick-Fil-A"
  if textArray[0] == "BUC-EE'S":
    return "餐飲", "Buc-ee's"
  if textArray[0] == "GONGCHA":
    return "點心飲料", "Gong Cha"
  if textArray[0] == "Popeyes":
    return "餐飲", "Popeyes"
  if textArray[0] == "Groupon,":
    return "Checking", "Groupon"
  if textArray[0] == "ACME":
    return "青菜水果", "Acme"
  if textArray[0] == "WENDYS":
    return "餐飲", "Wendus"
  if textArray[0] == "LEGO":
    return "休閒娛樂", "LEGO"
  
  if len(textArray) == 1:
    return False, False
  
  if textArray[0] == "RUI" and textArray[1] == "TEA":
    return "點心飲料", "Rui Tea"
  if textArray[0] == "GONG" and textArray[1][:3] == "CHA":
    return "點心飲料", "Gong Cha"
  if textArray[0] == "MR." and textArray[1] == "WISH":
    return "點心飲料", "Mr. Wish"
  if textArray[0] == "COSTCO" and textArray[1] == "GAS":
    return "交通工具", "Gas"
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount > 20:
    return "青菜水果", "Sam's Club"
  if textArray[0] == "TASTY" and textArray[1] == "K":
    return "餐飲", "Tasty K"
  if textArray[0] == "COSTCO" and textArray[1] == "WHSE" and amount > 20:
    return "青菜水果", "Costco"
  if textArray[0] == "COSTCO" and textArray[1] == "WHSE" and amount <= 20:
    return "餐飲", "Costco"
  if textArray[0] == "BOB" and textArray[1] == "EVANS":
    return "餐飲", "Bob Evans"
  if textArray[0] == "KOKO" and textArray[1] == "BAKERY":
    return "點心飲料", "Koko Bakery"
  if textArray[0] == "YY" and textArray[1] == "TIME":
    return "餐飲", "YY Time"
  if textArray[0] == "UMAMI" and textArray[1] == "NOODLE":
    return "餐飲", "Umami Noodle"
  if textArray[0] == "WM" and textArray[1] == "SUPERCENTER":
    return "日常用品", "Walmart"
  if textArray[0] == "BANGKOK" and textArray[1] == "THAI":
    return "餐飲", "Bangkok Thai"
  if textArray[0] == "ACE" and textArray[1] == "HARDWARE":
    return "生活開銷", "Ace Hardware"
  if textArray[0] == "IN" and textArray[1] == "*PEKING":
    return "餐飲", "Peking"
  if textArray[0] == "DOKI" and textArray[1] == "DOKI":
    return "點心飲料", "Doki Doki"
  if textArray[0] == "CRAFTY" and textArray[1] == "CRAB":
    return "餐飲", "Crafty Crab"
  if textArray[0] == "MIAMI" and textArray[1] == "GRILL":
    return "餐飲", "Miami Grill"
  if textArray[0] == "COSTCO" and textArray[1][:4] == "WHSE":
    return "青菜水果", "Costco"
  if textArray[0] == "COSTCO" and textArray[1][:3] == "GAS":
    return "交通工具", "Gas"
  if textArray[0] == "SUNS" and textArray[1] == "KITCHEN":
    return "餐飲", "Suns Kitchen"
  if textArray[0] == "TSAOCAA" and textArray[1] == "(CENTRAL)":
    return "點心飲料", "Tsaocaa"
  if textArray[0] == "PAPA" and textArray[1] == "JOHN'S":
    return "餐飲", "Papa John's"
  
  if len(textArray) == 2:
    return False, False
  
  if textArray[0] == "Hyatt" and textArray[1] == "Regency" and textArray[2] == "Hudson":
    return "休閒娛樂", "Hyatt Staying"
  if textArray[0] == "MMs" and textArray[1] == "New" and textArray[2] == "York":
    return "點心飲料", "MMs"
  if textArray[0] == "BIBBLE" and textArray[1] == "&" and textArray[2] == "SIP":
    return "點心飲料", "Bibble & Sip"
  if textArray[0] == "BLUE" and textArray[1] == "BOTTLE" and textArray[2] == "COFFEE":
    return "點心飲料", "Blue Bottle Coffee"
  if textArray[0] == "858" and textArray[1] == "JAPANESE" and textArray[2] == "MARKET":
    return "餐飲", "858 Japanese Market"
  if textArray[0] == "GULP" and textArray[1] == "JERSEY" and textArray[2] == "CITY":
    return "餐飲", "Gulp"
  if textArray[0] == "TADASHI" and textArray[1] == "JAPANESE" and textArray[2] == "RESTA":
    return "餐飲", "Tadashi Japanese"
  if textArray[0] == "GOOD" and textArray[1] == "HARVEST" and textArray[2] == "MARKET":
    return "青菜水果", "Good Harvest Market"
  if textArray[0] == "NERVOUS" and textArray[1] == "DOG" and textArray[2] == "COFFEE":
    return "點心飲料", "Nervous Dog Coffee"
  if textArray[0] == "THE" and textArray[1] == "COLLINS" and textArray[2] == "QUARTE":
    return "餐飲", "The Collins Quarte"
  if textArray[0] == "THE" and textArray[1] == "COFFEE" and textArray[2] == "FOX":
    return "點心飲料", "The Coffee Fox"

  if len(textArray) == 3:
    return False, False
  
  if textArray[0] == "ONCE" and textArray[1] == "UPON" and textArray[2] == "A" and textArray[3] == "CHILD":
    return "養育費", "Once Upon a Child"
  if textArray[0] == "MASON'S" and textArray[1] == "FAMOUS" and textArray[2] == "LO" and textArray[3] == "CHARLESTON":
    return "餐飲", "Mason's Famous"
  if textArray[0] == "PLAY" and textArray[1] == "IT" and textArray[2] == "AGAIN" and textArray[3] == "SPORTS":
    return "休閒娛樂", "Play It Again Sports"

  if len(textArray) == 4:
    return False, False

  if textArray[0] == "FB" and textArray[1] == "-" and textArray[2] == "HR" and textArray[3] == "JERSEY" and textArray[4] == "CITY":
    return "休閒娛樂", "Hyatt Staying"

  return False, False
