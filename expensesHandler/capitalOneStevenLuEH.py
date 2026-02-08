def expensesHandler(textArray, amount):
  # print(f'checking {textArray}')

  # Section only need one word to categorize
  if textArray[0] == "McDonalds" or textArray[0] == "MCDONALD'S":
    return "餐飲", "McDonalds", amount
  if textArray[0] == "STARBUCKS":
    return "點心飲料", "Starbucks", amount
  if textArray[0][:10] == "Amazon.com":
    return "日常用品", "Amazon", amount
  if textArray[0][:8] == "Spectrum":
    return "通訊費", "Spectrum", amount
  if textArray[0] == "USCIS":
    return "生活開銷", "USCIS", amount
  if textArray[0] == "APPLEBEES":
    return "餐飲", "Applebees", amount
  if textArray[0] == "WAL-MART":
    return "日常用品", "Walmart", amount
  if textArray[0] == "POPEYES":
    return "餐飲", "Popeyes", amount
  if textArray[0] == "GIANT-EAGLE":
    return "青菜水果", "Giant Eagle", amount
  if textArray[0] == "DUNKIN":
    return "點心飲料", "Dunkin Donuts", amount
  if textArray[0][:9] == "HOTELSCOM":
    return "休閒娛樂", "Hotels cost", amount
  if textArray[0] == "AMAZON":
    return "日常用品", "Amazon", amount
  if textArray[0] == "Subway":
    return "餐飲", "Subway", amount
  if textArray[0] == "WALGREENS":
    return "生活開銷", "Walgreens", amount
  if textArray[0] == "EXXON":
    return "交通工具", "Gas", amount
  if textArray[0] == "KFC":
    return "餐飲", "KFC", amount
  if textArray[0] == "EZPASS":
    return "交通工具", "Toll", amount
  if textArray[0] == "CHIPOTLE":
    return "餐飲", "Chipotle", amount
  if textArray[0] == "TSAOCAA":
    return "點心飲料", "Tsaocaa Tea", amount
  if textArray[0] == "WEEE":
    return "青菜水果", "Weee", amount
  if textArray[0] == "PARCHMENT-UNIV":
    return "生活開銷", "Parchment University", amount
  if textArray[0] == "RSVP":
    return "生活開銷", "RSVP", amount
  if textArray[0][:10] == "AMAZON.COM":
    return "日常用品", "Amazon", amount
  if textArray[0] == "SUNOCO":
    return "交通工具", "Gas", amount
  if textArray[0] == "MARC'S":
    return "青菜水果", "Marc's", amount
  if textArray[0] == "ALDI":
    return "青菜水果", "Aldi", amount
  if textArray[0] == "FANDANGOFANDANGO.COMCA":
    return "休閒娛樂", "Movie", amount
  if textArray[0] == "MIDWAY":
    return "休閒娛樂", "Midway drive in theater", amount
  if textArray[0] == "TARGET" or textArray[0] == "TARGET.COM":
    return "日常用品", "Target", amount
  if textArray[0] == "SHERWIN-WILLIAMS701315STOWOH":
    return "日常用品", "Sherwin Williams", amount
  if textArray[0] == "IMG":
    return "生活開銷", "IMG insurance", amount
  if textArray[0] == "WENDYS":
    return "餐飲", "Wendys", amount
  if textArray[0] == "LOWES":
    return "日常用品", "Lowes", amount
  if textArray[0][:8] == "HOTELCOM" and textArray[0][-12:] == "HOTELS.COMWA":
    return "休閒娛樂", "Hotel", amount
  if textArray[0] == "CHEDDAR'S":
    return "餐飲", "Cheddars", amount
  if textArray[0] == "SAMSCLUB" and amount > 20:
    return "日常用品", "Sams Club", amount
  if textArray[0] == "SAMSCLUB" and amount <= 20:
    return "餐飲", "Sams Club", amount
  if textArray[0] == "KOHL'S":
    return "日常用品", "Kohls", amount
  if textArray[0] == "HEINEN'S":
    return "青菜水果", "Heinens", amount
  if textArray[0] == "WWW.TRAINSHOW.COM":
    return "休閒娛樂", "Train Show", amount
  if textArray[0] == "CVS/PHARMACY":
    return "生活開銷", "CVS Pharmacy", amount
  if textArray[0] == "5GUYS":
    return "餐飲", "Five Guys", amount
  if textArray[0] == "COT*HTL":
    return "休閒娛樂", "Hotel", amount
  if textArray[0] == "SHEETZ":
    return "交通工具", "Gas", amount
  if textArray[0] == "PARKMOBILE":
    return "交通工具", "Parking", amount
  if textArray[0] == "GOMOBILEPGH":
    return "交通工具", "Parking", amount
  if textArray[0] == "ETOLLAVIS":
    return "交通工具", "Toll", amount
  if textArray[0] == "IHOP":
    return "餐飲", "IHOP", amount 
  if textArray[0] == "WALMART.COM":
    return "日常用品", "Walmart", amount
  if textArray[0] == "THEKOOP":
    return "餐飲", "The Koop", amount
  if textArray[0] == "BP#9597931COGO'S":
    return "交通工具", "Gas", amount

   
  if len(textArray) == 1:
    return False, False, amount
  
  # Section need two sections to categorize
  if textArray[0] == "AMZN" and textArray[1] == "Mktp":
    return "日常用品", "Amazon", amount
  if textArray[0] == "AMZN" and textArray[1] == "MKTP":
    return "日常用品", "Amazon", amount
  if textArray[0] == "COSTCO" and textArray[1][:3] == "GAS":
    return "交通工具", "Gas", amount
  if textArray[0] == "COSTCO" and textArray[1] == "WHSE" and 0 < amount < 20:
    return "餐飲", "Costco", amount
  if textArray[0] == "COSTCO" and textArray[1] == "WHSE" and (amount < 0 or amount > 20):
    return "青菜水果", "Costco", amount
  if textArray[0] == "GOOGLE" and textArray[1][:16] == "*YouTubePremiumg":
    return "休閒娛樂", "YouTube Premium", amount
  if textArray[0] == "PANDA" and textArray[1] == "EXPRESS":
    return "餐飲", "Panda Express", amount
  if textArray[0] == "SZECHUAN" and textArray[1] == "GOURMETCLEVELANDOH":
    return "餐飲", "Szechuan Gourmet", amount
  if textArray[0] == "ACE" and textArray[1][:4] == "HDWE":
    return "日常用品", "Ace Hardware", amount
  if textArray[0] == "PROGRESSIVE" and textArray[1][:3] == "INS":
    return "交通工具", "Insurance", amount
  if textArray[0] == "MASA" and textArray[1] == "ASIAN":
    return "餐飲", "Masa Asian", amount
  if textArray[0] == "GET" and textArray[1] == "GO":
    return "交通工具", "Gas", amount
  if textArray[0] == "UMAMI" and textArray[1] == "NOODLE":
    return "餐飲", "Umami Noodle", amount
  if textArray[0] == "FIVE" and textArray[1] == "GUYS":
    return "餐飲", "Five Guys", amount
  if textArray[0] == "PAPA" and textArray[1] == "JOHN'S":
    return "餐飲", "Papa John's", amount
  if textArray[0] == "Paulas" and textArray[1] == "Choice":
    return "治裝費", "Paulas Choice", amount
  if textArray[0] == "YAMA" and textArray[1] == "JAPANESE":
    return "餐飲", "Yama Japanese", amount
  if textArray[0] == "PIZZA" and textArray[1] == "ALS":
    return "餐飲", "Pizza Als", amount
  if textArray[0] == "KING" and textArray[1] == "DRAGON":
    return "餐飲", "King Dragon", amount
  if textArray[0] == "SLYMAN'S" and textArray[1] == "RESTAURANTCLEVELANDOH":
    return "餐飲", "Slymans Restaurant", amount
  if textArray[0] == "BURGER" and textArray[1] == "KING":
    return "餐飲", "Burger King", amount
  if textArray[0] == "SPAGHETTI" and textArray[1] == "WAREHOUSE":
    return "餐飲", "Spaghetti Warehouse", amount
  if textArray[0] == "ACME" and textArray[1] == "NO.":
    return "青菜水果", "Acme", amount
  if textArray[0] == "SWENSON'S" and textArray[1] == "DRIVE-IN":
    return "餐飲", "Swensons Drive-In", amount
  if textArray[0] == "RAISING" and textArray[1] == "CANES":
    return "餐飲", "Raising Canes", amount
  if textArray[0] == "BURLINGTON" and textArray[1] == "STORES":
    return "日常用品", "Burlington", amount
  if textArray[0] == "SUNRISE" and textArray[1] == "KITCHENSTOWOH":
    return "餐飲", "Sunrise Kitchen", amount
  if textArray[0] == "RITTMAN" and textArray[1] == "ORCHARDSDOYLESTOWNOH":
    return "青菜水果", "Rittman Orchards", amount
  if textArray[0] == "EVERYDAY" and textArray[1] == "NOODLESPITTSBURGHPA":
    return "餐飲", "Everyday Noodle", amount
  if textArray[0] == "MEIJER" and textArray[1] == "STORE":
    return "青菜水果", "Meijer", amount
  if textArray[0] == "WM" and textArray[1] == "SUPERCENTER":
    return "日常用品", "Walmart", amount
  if textArray[0] == "TRI" and textArray[1] == "ASIAN":
    return "餐飲", "Tri Asian", amount
  if textArray[0] == "Columbia" and textArray[1] == "Aurora":
    return "治裝費", "Columbia Aurora", amount
  if textArray[0] == "BUFFALO" and textArray[1] == "WILD":
    return "餐飲", "Buffalo Wild Wings", amount
  if textArray[0] == "K" and textArray[1][:6] == "MARKET":
    return "青菜水果", "K Market", amount
  if textArray[0] == "HCW" and textArray[1] == "FOODSERVICE/RETAILHERSHEYPA":
    return "休閒娛樂", "Hershey Park", amount
  if textArray[0] == "CORNERSTONE" and textArray[1] == "MARKET":
    return "青菜水果", "Cornerstone Market", amount
  if textArray[0][:2] == "BP" and textArray[1][:2] == "BP":
    return "交通工具", "Gas", amount
  if textArray[0] == "METROPARKS" and textArray[1] == "ZOO":
    return "休閒娛樂", "Metroparks Zoo", amount
  if textArray[0] == "Kumo" and textArray[1] == "buffetparmaOH":
    return "餐飲", "Kumo Buffet", amount
  if textArray[0] == "SQ" and textArray[1] == "*FARMERS" and textArray[2] == "DAUGHTERStowOH":
    return "青菜水果", "Stow Farmers Market", amount
  if textArray[0] == "TEXAS" and textArray[1] == "ROADHOUSE":
    return "餐飲", "Texas Roadhouse", amount
  if textArray[0] == "TST*SUPERIOR" and textArray[1] == "PHO":
    return "餐飲", "Superior Pho", amount
  if textArray[0] == "UEP*KOKO" and textArray[1] == "BAKERYCLEVELANDOH":
    return "點心飲料", "Koko Bakery", amount
  if textArray[0] == "OLD" and textArray[1] == "NAVY":
    return "治裝費", "Old Navy", amount
  if textArray[0] == "WELLNESS" and textArray[1] == "CENTRE":
    return "養育費", "Swimming Lesson", amount
  if textArray[0] == "STOW" and textArray[1] == "TRAVEL":
    return "養育費", "Stow Travel Sport", amount
  if textArray[0] == "SQ" and textArray[1] == "*PARKING.COM":
    return "交通工具", "Parking", amount
  if textArray[0] == "SEOUL" and textArray[1] == "GARDENPARMAOH":
    return "餐飲", "Seoul Garden", amount
  if textArray[0] == "THERESA'S" and textArray[1] == "BAKERYCLEVELANDOH":
    return "點心飲料", "Theresa's Bakery", amount
  if textArray[0] == "BELLES" and textArray[1] == "BREAD":
    return "點心飲料", "Belles Bread", amount
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount < 20:
    return "餐飲", "Sams Club", amount
  if textArray[0] == "YY" and textArray[1] == "TIME131-27305592IL":
    return "餐飲", "Dagu Rice Noodle", amount
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount > 20:
    return "日常用品", "Sams Club", amount
  if textArray[0] == "SAMS" and textArray[1] == "CLUB" and amount <= 20:
    return "餐飲", "Sams Club", amount
  if textArray[0] == "SQ" and textArray[1] == "*MASAAkronOH":
    return "餐飲", "Masa", amount
  if textArray[0] == "JOANN" and textArray[1] == "STORES":
    return "日常用品", "Joann", amount
  if textArray[0] == "KOREA" and textArray[1] == "HOUSECLEVELANDOH":
    return "餐飲", "Korea House", amount
  if textArray[0] == "Groupon," and textArray[1][0:4] == "Inc.":
    return "休閒娛樂", "Groupon", amount
  if textArray[0] == "MR." and textArray[1] == "WISHFALLS":
    return "點心飲料", "Mr. Wish", amount
  if textArray[0] == "GABRIEL" and textArray[1] == "BROS":
    return "治裝費", "Gabriel Bros", amount
  if textArray[0] == "ASIA" and textArray[1] == "FOOD":
    return "青菜水果", "Asia Food", amount
  if textArray[0] == "SHELL" and textArray[1] == "OIL":
    return "交通工具", "Gas", amount
  if textArray[0] == "CASTAWAY" and textArray[1][0:3] == "BAY":
    return "休閒娛樂", "Castaway Bay", amount
  if textArray[0] == "FRONTIER" and textArray[1] == "AI":
    return "休閒娛樂", "Frontier Airline", amount
  if textArray[0] == "USPS" and textArray[1] == "PO":
    return "生活開銷", "USPS", amount
  if textArray[0] == "UEP*PACIFIC" and textArray[1] == "EASTKENTOH":
    return "餐飲", "Pacific East", amount
  if textArray[0] == "CIRCLE" and textArray[1] == "K":
    return "交通工具", "Gas", amount
  if textArray[0] == "GULF" and textArray[1] == "OIL":
    return "交通工具", "Gas", amount
  if textArray[0] == "TST*ROOSTER" and textArray[1] == "TREATS":
    return "點心飲料", "Rooster Treats", amount
  if textArray[0] == "DENNYS" and textArray[1] == "LIQUORS":
    return "點心飲料", "Dennys Liquors", amount
  if textArray[0] == "FAMILY" and textArray[1] == "DOLLAR":
    return "青菜水果", "Family Dollar", amount
  if textArray[0] == "PEKING" and textArray[1] == "CHEF":
    return "餐飲", "Peking Chef", amount
  if textArray[0] == "TENSUKE" and textArray[1] == "MARKET":
    return "餐飲", "Tensuke Market", amount
  if textArray[0] == "SGT" and textArray[1] == "CLEAN":
    return "交通工具", "Sgt Clean", amount
  if textArray[0] == "BANGKOK" and textArray[1] == "THAI":
    return "餐飲", "Bangkok Thai", amount
  if textArray[0] == "SUNRISE" and textArray[1] == "KITCHEN":
    return "餐飲", "Sunrise Kitchen", amount
  if textArray[0] == "OLIVE" and textArray[1] == "GARDEN":
    return "餐飲", "Olive Garden", amount
  if textArray[0] == "SPICY" and textArray[1] == "SOMBRERO":
    return "餐飲", "Spicy Sombroso", amount
  if textArray[0] == "PF" and textArray[1] == "CHANGS":
    return "餐飲", "PF Changs", amount
  if textArray[0] == "DD" and textArray[1] == "*WUSHILANDBOBA":
    return "點心飲料", "DD Wushiland Boba", amount
  if textArray[0] == "MARUFUJI" and textArray[1] == "MARKET":
    return "青菜水果", "Marufuji Market", amount
  if textArray[0] == "STUDENTREASURES" and textArray[1] == "PUBLISHI":
    return "養育費", "Student Treasures Publishing", amount
  if textArray[0] == "INTER-STATE" and textArray[1] == "STUDIO":
    return "養育費", "Inter State Studio", amount
  if textArray[0] == "LEVI'S":
    return "治裝費", "Levis", amount
  if textArray[0] == "DUMA" and textArray[1] == "MEATS":
    return "青菜水果", "Duma Meats", amount
  if textArray[0] == "SQ" and textArray[1] == "*LUCHA":
    return "點心飲料", "Lucha", amount
  if textArray[0] == "SQ" and textArray[1] == "*MIDWAYFOODSLLC":
    return "點心飲料", "Midway Foods", amount
  if textArray[0] == "AKRON" and textArray[1] == "ZOO":
    return "休閒娛樂", "Akron Zoo", amount
  if textArray[0] == "GO!" and textArray[1] == "CALENDARS,GAMES,BOOKS":
    return "養育費", "Go! Calendars", amount
  if textArray[0] == "SkyZoneBoston" and textArray[1] == "Heights":
    return "養育費", "Sky Zone", amount
  if textArray[0] == "DAIRY" and textArray[1] == "QUEEN":
    return "餐飲", "Dairy Queen", amount
  if textArray[0] == "AVIS" and textArray[1] == "RENT-A-CAR":
    return "休閒娛樂", "Avis", amount
  if textArray[0] == "SAFELITE" and textArray[1] == "AUTOGLASS":
    return "交通工具", "Safelite Auto Glass", amount
  if textArray[0] == "CEDAR" and textArray[1] == "POINT":
    return "休閒娛樂", "Cedar Point", amount
  if textArray[0] == "ASIA" and textArray[1] == "GARDENS":
    return "餐飲", "Asia Gardens", amount
  if textArray[0] == "PARK" and textArray[1] == "MOBILE":
    return "交通工具", "Parking", amount
  if textArray[0] == "SAVANNAH" and textArray[1] == "PARKING":
    return "交通工具", "Parking", amount
  if textArray[0] == "WINGS" and textArray[1] == "ETC.":
    return "餐飲", "Wings Etc", amount
  if textArray[0] == "FRONTIER" and textArray[1] == "AIRLINES":
    return "休閒娛樂", "Frontier Airlines", amount
  if textArray[0] == "AHRI'S" and textArray[1] == "KITCHEN":
    return "餐飲", "Ahri's Kitchen", amount
  if textArray[0] == "STOW" and textArray[1] == "SOCCER":
    return "養育費", "Stow Soccer Club", amount

  if len(textArray) == 2:
    return False, False, amount

  # Section need three sections to categorize
  if textArray[0] == "CAM" and textArray[1] == "ASIA" and textArray[2] == "SUPERMARKET":
    return "青菜水果", "CAM Asia", amount
  if textArray[0] == "WHERE" and textArray[1] == "YA" and textArray[2] == "BIN":
    return "日常用品", "Where Ya Bin", amount
  if textArray[0] == "TST*" and textArray[1] == "MANGO" and textArray[2] == "MANGO":
    return "點心飲料", "Mongo Mongo", amount
  if textArray[0] == "AKRON" and textArray[1] == "CHILDRENS" and textArray[2][:6] == "MUSEUM":
    return "休閒娛樂", "Akron Childrens Museum", amount
  if textArray[0] == "SQ" and textArray[1] == "*SPARK!" and textArray[2] == "IMAGINATION":
    return "休閒娛樂", "Spark! Imagination", amount
  if textArray[0] == "CHA" and textArray[1] == "LI" and textArray[2] == "TEA":
    return "點心飲料", "Cha Li Tea", amount
  if textArray[2] == "CHICK" and textArray[3] == "FIL" and textArray[4] == "A":
    return "餐飲", "Chick Fil A", amount
  if textArray[0] == "TRADER" and textArray[1] == "JOE" and textArray[2] == "S":
    return "青菜水果", "Trader Joes", amount
  if textArray[0] == "CWRU" and textArray[1] == "CMVMS" and textArray[2] == "DEPOSITCASE.EDUOH":
    return "生活開銷", "CWRU CMVMS", amount
  if textArray[0] == "U" and textArray[1] == "AKRON" and textArray[2] == "FRESHENSAKRONOH":
    return "餐飲", "U Akron Freshens", amount
  if textArray[0] == "SQ" and textArray[1] == "*JOE?S" and textArray[2] == "BARBECUEKentOH":
    return "餐飲", "Joe's Barbecue", amount
  if textArray[0] == "DON" and textArray[1] == "PATRON" and textArray[2] == "MEXICAN":
    return "餐飲", "Don Patron Mexican Grill", amount
  if textArray[0] == "SQ" and textArray[1] == "*RITTMAN" and textArray[2] == "ORCHARDSAkronOH":
    return "休閒娛樂", "Rittman Orchards", amount
  if textArray[0] == "THE" and textArray[1] == "GRANDVIEW" and textArray[2] == "SALOONPITTSBURGHPA":
    return "交通工具", "Parking", amount
  if textArray[0] == "ON" and textArray[1] == "STREET" and textArray[2][:5] == "METER":
    return "交通工具", "Parking", amount
  if textArray[0] == "THE" and textArray[1] == "HOME" and textArray[2] == "DEPOT":
    return "日常用品", "Home Depot", amount
  if textArray[0] == "THE" and textArray[1] == "CHILDRENS" and textArray[2] == "PLACE":
    return "治裝費", "The Childrens Place", amount
  if textArray[0] == "SQ" and textArray[1] == "*CC" and textArray[2] == "FOODSGARRETTSVILLEOH":
    return "餐飲", "CC Foods", amount
  if textArray[0] == "KENT" and textArray[1] == "FOOD" and textArray[2] == "MARKET":
    return "青菜水果", "Kent Food Market", amount
  if textArray[0] == "PY" and textArray[1] == "*KUNG" and textArray[2] == "FU":
    return "點心飲料", "Kung Fu Tea", amount
  if textArray[0] == "BOB" and textArray[1] == "EVANS" and textArray[2] == "REST":
    return "餐飲", "Bob Evans", amount
  if textArray[0] == "KIMS" and textArray[1] == "ORIENTAL" and textArray[2] == "FOOD":
    return "青菜水果", "Kims Oriental Food", amount
  if textArray[0] == "TOUS" and textArray[1] == "LES" and textArray[2] == "JOURS":
    return "點心飲料", "Tous Les Jours", amount
  if textArray[0] == "TST*PAD" and textArray[1] == "THAI" and textArray[2] == "HUDSONHudsonOH":
    return "餐飲", "Pad Thai", amount
  if textArray[0] == "CP" and textArray[1] == "QUAKER" and textArray[2] == "STEAK":
    return "餐飲", "Quaker Steak", amount
  if textArray[0] == "TINK" and textArray[1] == "HOLL" and textArray[2] == "ENTERPRISES":
    return "青菜水果", "Tink Holl", amount
  if textArray[0] == "LITTLE" and textArray[1] == "HAVANA" and textArray[2] == "VISITORS":
    return "點心飲料", "Little Havana", amount
  if textArray[0] == "EVERGLADES" and textArray[1] == "NATL" and textArray[2] == "PARK": 
    return "交通工具", "Parking", amount
  if textArray[0] == "TST*THE" and textArray[1] == "SEASIDE" and textArray[2] == "CAFE": 
    return "餐飲", "Seaside Cafe", amount
  if textArray[0] == "CTLP*BAR" and textArray[1] == "PARTNERS" and textArray[2] == "INC":
    return "休閒娛樂", "Bar Partners", amount
  if textArray[0] == "SQ" and textArray[1] == "*TENSUKE" and textArray[2] == "RAMENColumbusOH":
    return "餐飲", "Tensuke Ramen", amount
  if textArray[0] == "PMUSA" and textArray[2] == "CUMBERLAN":
    return "交通工具", "Parking", amount
  if textArray[0] == "GO!" and textArray[1] == "CALENDARS":
    return "養育費", "Go Retail Group", amount
  if textArray[0] == "SQ" and textArray[1] == "*BELLE'S" and textArray[2] == "BREAD":
    return "點心飲料", "Belles Bread", amount
  if textArray[0] == "Hunan" and textArray[1] == "of" and textArray[2] == "Stow":
    return "餐飲", "Hunan of Stow", amount
  if textArray[0] == "SQ" and textArray[1] == "*DREAMSICLE" and textArray[2] == "CONCESSION":
    return "點心飲料", "Dreamsicle Concession", amount
  if textArray[0] == "METRO" and textArray[1] == "AIRPORT" and textArray[2] == "PARKING":
    return "交通工具", "Parking", amount
  if textArray[0] == "SQ" and textArray[1] == "*TENSUKE" and textArray[2] == "MARKET":
    return "點心飲料", "Tensuke Market", amount
  if textArray[0] == "PARK" and textArray[1] == "TO" and textArray[2] == "SHOP":
    return "青菜水果", "Park to Shop", amount
  if textArray[0] == "THE" and textArray[1] == "UPS" and textArray[2] == "STORE":
    return "生活開銷", "The UPS Store", amount
  if textArray[0] == "ONLINE" and textArray[1] == "LIQUIDATION" and textArray[2] == "AUC":
    return "日常用品", "Online Liquidation Auction", amount
  if textArray[0] == "KINGS" and textArray[1] == "ISLAND" and textArray[2] == "FOOD":
    return "餐飲", "Kings Island Food", amount
  if textArray[0] == "ERAWAN" and textArray[1] == "THAI" and textArray[2] == "KITCHEN":
    return "餐飲", "Erawan Thai Kitchen", amount
  if textArray[0] == "AKAHANA" and textArray[1] == "ASIAN" and textArray[2] == "BISTRO":
    return "餐飲", "Akahana Asian Bistro", amount
  if textArray[0] == "LOS" and textArray[1] == "REYES" and textArray[2] == "MEXICAN":
    return "餐飲", "Los Reyes Mexican", amount
  
  if len(textArray) == 3:
    return False, False, amount

  # Section need four sections to categorize
  if textArray[0] == "THE" and textArray[1] == "CAFE" and textArray[2] == "IN" and textArray[3] == "STOWSTOWOH":
    return "餐飲", "The Cafe In Stow", amount
  if textArray[0] == "TST*" and textArray[1] == "STOW" and textArray[2] == "NUT" and textArray[3] == "DONUT":
    return "餐飲", "Stow Nut", amount
  if textArray[0] == "GOGI" and textArray[1] == "EN" and textArray[2] == "K" and textArray[3] == "BBQSOLONOH":
    return "餐飲", "Gogi En K BBQ", amount
  if textArray[0] == "TST*" and textArray[1] == "JOLLY" and textArray[2] == "ROGER" and textArray[3] == "SEAFOODPort":
    return "餐飲", "Jolly Rogers Seafood House", amount
  if textArray[0] == "SQ" and textArray[1] == "*FLURY'S" and textArray[2] == "CAFECuyahoga" and textArray[3] == "FallOH":
    return "餐飲", "Flury's Cafe", amount
  if textArray[0] == "CITY" and textArray[1] == "OF" and textArray[2] == "CF-METERCUYAHOGA" and textArray[3] == "FALLOH":
    return "交通工具", "Parking", amount
  if textArray[0] == "SQ" and textArray[1] == "*PINK" and textArray[2] == "BOX" and textArray[3] == "BAKERY":
    return "點心飲料", "Pink Box Bakery", amount
  if textArray[0] == "TST*" and textArray[1] == "NOTHING" and textArray[2] == "BUNDT" and textArray[3] == "CAKESSTOWOH":
    return "點心飲料", "Nothing Bundt Cakes", amount
  if textArray[0] == "SQ" and textArray[1] == "*ICE" and textArray[2] == "CREAM" and textArray[3] == "TRUCKStowOH":
    return "點心飲料", "Ice Cream Truck", amount
  if textArray[0] == "THE" and textArray[1] == "CHILDRENS" and textArray[2] == "MUSEUM" and textArray[3] == "OFCLEVELANDOH":
    return "休閒娛樂", "The Childrens Museum", amount
  if textArray[0] == "SQ" and textArray[1] == "*KINGSWAY" and textArray[2] == "PUMPKIN" and textArray[3] == "FARMHARTVILLEOH":
    return "休閒娛樂", "Kingsway Pumpkin Farm", amount
  if textArray[0] == "SQ" and textArray[1] == "*MITCHELL'S" and textArray[2] == "ICE" and textArray[3] == "CREAMBeachwoodOH":
    return "點心飲料", "Mitchell's Ice Cream", amount
  if textArray[0] == "95497" and  textArray[1] == "-" and textArray[2] =="STANDARD" and textArray[3] == "PARKING":
    return "交通工具", "Parking", amount
  if textArray[0] == "HYATT" and textArray[1] == "CENTRIC" and textArray[2] == "MIAMI" and textArray[3] == "BRIK":
    return "休閒娛樂", "Hyatt Hotels", amount
  if textArray[0] == "CITY" and textArray[1] == "OF" and textArray[2] == "MIAMI" and textArray[3] == "BEACH":
    return "交通工具", "Parking", amount
  if textArray[0] == "BUDGET" and textArray[1] == "RENT" and textArray[2] == "A" and textArray[3] == "CAR":
    return "休閒娛樂", "Car rental", amount
  if textArray[0] == "SQ" and textArray[3] == "FLAVOR":
    return "點心飲料", "Just Chillin", amount
  if textArray[0] == "SQ" and textArray[1] == "*EL" and textArray[2] == "PUB" and textArray[3] == "RESTAURANT":
    return "餐飲", "El Pub Restaurant", amount
  if textArray[0] == "SANDAL" and textArray[1] == "FACTORY" and textArray[2] == "KEY" and textArray[3] == "LARGO":
     return "休閒娛樂", "Sandal Factory", amount
  if textArray[0] == "VAL*BAYSIDE" and textArray[1] == "INN" and textArray[2] == "KEY" and textArray[3] == "LA":  
    return "休閒娛樂", "Bayside Inn", amount
  if textArray[0] == "KEY" and textArray[1] == "LIME" and textArray[2] == "PIE" and textArray[3] == "BAKERY": 
    return "點心飲料", "Lime Pie", amount
  if textArray[0] == "KEY" and textArray[1] == "WEST" and textArray[2] == "PARKING" and textArray[3] == "METERS":
    return "交通工具", "Parking", amount
  if textArray[0] == "SQ" and textArray[1] == "*BASECAMP" and textArray[2] == "COFFEE" and textArray[3] == "COMPA":
    return "點心飲料", "Basecamp Coffee", amount
  if textArray[0] == "YIFANG" and textArray[1] == "TAIWAN" and textArray[2] == "FRUIT" and textArray[3] == "TE":
    return "點心飲料", "Yifang Taiwan Fruit Tea", amount
  if textArray[0] == "ROYAL" and textArray[1] == "BUFFET" and textArray[2] == "&" and textArray[3] == "GRILL":
    return "餐飲", "Royal Buffet & Grill", amount
  if textArray[0] == "SQ" and textArray[1] == "*MING'S" and textArray[2] == "BUBBLE" and textArray[3] == "TEA":
    return "點心飲料", "Ming's Bubble Tea", amount
  if textArray[0] == "SQ" and textArray[1] == "*ICE" and textArray[2] == "CREAM" and textArray[3] == "TRUCK":
    return "點心飲料", "Ice Cream Truck", amount
  if textArray[0] == "NIAGARA" and textArray[1] == "FALLS" and textArray[2] == "ST" and textArray[3] == "PK":
    return "交通工具", "Parking", amount
  if textArray[0] == "ROYAL" and textArray[1] == "DRAGON" and textArray[2] == "NOODLE" and textArray[3] == "BAR":
    return "餐飲", "Royal Dragon Noodle Bar", amount
  if textArray[0] == "BLUE" and textArray[1] == "RHINO" and textArray[2] == "" and textArray[3] == "PROPANE":
    return "生活開銷", "Blue Rhino Propane", amount

  if len(textArray) == 4:
    return False, False, amount

  if textArray[0] == "ADRENALIN" and textArray[1] == "PARK" and textArray[2] == "MH" and textArray[3] == "LLCMIDDLEBURG" and textArray[4] == "HTOH":
    return "休閒娛樂", "Get Air", amount
  if textArray[0] == "MPA" and textArray[1] == "PARKING" and textArray[2] == "PAY" and textArray[3] == "BY" and textArray[4] == "PHONE":
    return "交通工具", "Parking", amount
  if textArray[0] == "SQ" and textArray[1] == "*THE" and textArray[2] == "OHIO" and textArray[3] == "STATE" and textArray[4] == "REFORM":
    return "生活開銷", "The Ohio State Reform", amount
  if textArray[0] == "93898" and textArray[1] == "-" and textArray[2] == "UNIVERSITY" and textArray[3] == "OF" and textArray[4] == "AKR":
    return "生活開銷", "University of Akron", amount
  if textArray[0] == "CITY" and textArray[1] == "OF" and textArray[2] == "CUYAHOGA" and textArray[3] == "FALLS" and textArray[4] == "P":
    return "休閒娛樂", "The Natatorium", amount
  if textArray[0] == "PT" and textArray[1] == "AUTHY" and textArray[2] == "ALLEG" and textArray[3] == "TKT" and textArray[4] == "VEND":
    return "休閒娛樂", "Pittsburgh Authority", amount
  if textArray[0] == "MAID" and textArray[1] == "OF" and textArray[2] == "THE" and textArray[3] == "MIST" and textArray[4] == "CORPO":
    return "休閒娛樂", "Maid of the Mist", amount
  if textArray[0] == "UEP*KINTARO" and textArray[1] == "ALL" and textArray[2] == "YOU" and textArray[3] == "CAN" and textArray[4] == "E":
    return "餐飲", "Kintaro", amount
  if textArray[0] == "SQ" and textArray[1] == "*THE" and textArray[2] == "TUNNEL" and textArray[3] == "HOTEL" and textArray[4] == "AND":
    return "點心飲料", "The Tunnel Hotel", amount
  if textArray[0] == "ETANG" and textArray[1] == "NOODLE" and textArray[2] == "AND" and textArray[3] == "HOT" and textArray[4] == "POT":
    return "餐飲", "Etang Noodle And Hot Pot", amount


  # if didn't find the category, return False
  return False, False, amount
