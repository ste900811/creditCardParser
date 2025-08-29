def expensesHandler(textArray, amount):

  if textArray[0][:10] == "AMAZON.COM" and textArray[0][-4:] == "BILL":
    return "Amazon"
  if textArray[0] == "AMAZON.COM":
    return "Amazon"
  if textArray[0] == "AMAZON":
    return "Amazon"
  if textArray[0] == "L'IDEA":
    return "Baby"
  if textArray[0] == "LAGRAPPA" and "LUCCA" in textArray:
    return "Dining"
  if textArray[0] == "WASHPOST":
    return "Others/YL"
  if textArray[0] == "L'OSTE" and "LUCCA" in textArray:
    return "Dining"
  if textArray[0] == "OSTERIA" and "LUCCA" in textArray:
    return "Dining"
  if textArray[0] == "LIBRERIA" and "LUCCA" in textArray:
    return "Baby"
  if textArray[0] == "PIZZERIA...IN":
    return "Dining"
  if textArray[0] == "SOUVENIR" and "LUCCA" in textArray:
    return "Others/YL"
  if textArray[0] == "SUMUP*GALLACCI":
    return "Dining"
  if textArray[0] == "PEPEROSA":
    return "Dining"
  if textArray[0] == "RICORDO" and "LUCCA" in textArray:
    return "Others/YL"
  if textArray[0] == "AIRALO":
    return "Travel"
  if textArray[0] == "SUMUP*EDOTOURING" and "LUCCA" in textArray:
    return "Travel"
  if textArray[0] == "EXXONMOBIL":
    return "Gas"
  if textArray[0] == "FREETAXUSA.COM":
    return "Bus Exp/Prof Fee"
  if textArray[0] == "UBER":
    return "Travel"
  if textArray[0] == "CLICKPAY=FIRSTSERVICFAIRFAX":
    return "HOA"
  if textArray[0] == "DAYCAREFEE*":
    return "Daycare"
  if textArray[0] == "LOWE'S":
    return "Amazon"
  if textArray[0] == "LIDL":
    return "Grocery"
  if textArray[0] == "AIRBNB":
    return "Travel"
  if textArray[0] == "REMARKABLE":
    return "Other/HY"
  if textArray[0] == "Courtyard":
    return "Travel"
  if textArray[0] == "GIANT":
    return "Grocery"
  if textArray[0] == "FIRSTENERGY":
    return "1888 lillian electric"
  if textArray[0] == "GRUBHUB*BURGER7":
    return "Dining"
  if textArray[0] == "PIZZICHERIA":
    return "Dining"
  if textArray[0] == "SOTTO":
    return "Dining"
  if textArray[0] == "WALGREENS":
    return "Medical Expense"
  if textArray[0] == "CVS":
    return "Medical Expense"
  if textArray[0] == "CHARGEPOINT":
    return "Charge"
  if textArray[0] == "SHEETZ":
    return "Gas"
  if textArray[0] == "STARBUCKS":
    return "Dining"
  if textArray[0] == "PARKMOBILE":
    return "Parking"
  if textArray[0] == "THSRC":
    return "Travel"
  if textArray[0] == "CLEAR":
    return "Travel"
  if textArray[0] == "APPLE.COM/BILINTERNET":
    return "Other/HY"
  if textArray[0] == "WHOLEFDS":
    return "Grocery"
  if textArray[0] == "McDonald's":
    return "Dining"
  if textArray[0] == "UNIQLO":
    return "Others/YL"
  if textArray[0] == "LAWSON":
    return "Grocery"
  if textArray[0] == "SHINOBIYA1":
    return "Others/YL"
  if textArray[0] == "SUNDRUG":
    return "Others/YL"
  if textArray[0] == "NAMBACITY":
    return "Others/YL"
  if textArray[0] == "MCDONALD'S":
    return "Dining"
  if textArray[0] == "ORDER.NOODLES.COM":
    return "Dining"
  if textArray[0] == "DOLPAN":
    return "Dining"
  if textArray[0] == "Starbucks":
    return "Dining"
  if textArray[0] == "CPC" and "KAOHSIUNG" in textArray:
    return "Gas"
  if textArray[0] == "NYAJOES":
    return "Dining"
  if textArray[0] == "STORE" and "MCLEAN" in textArray and "VA" in textArray:
    return "Dining"
  if textArray[0] == "TABACCHI" and "FIRENZE" in textArray:
    return "Travel"
  if textArray[0] == "IDEXE'" and "LUCCA" in textArray:
    return "Baby"

  if len(textArray) == 1:
    return False

  if textArray[0] == "UNITED" and textArray[1] == "AIRLINES":
    return "Travel"
  if textArray[0] == "ESSELUNGA" and textArray[1] == "LUCCA":
    return "Grocery"
  if textArray[0] == "GELATERIA" and textArray[1] == "VENETA":
    return "Dining"
  if textArray[0] == "FRENCH" and textArray[1] == "TASTE":
    return "Dining"
  if textArray[0] == "FCPA" and textArray[1] == "PARK":
    return "fcpa"
  if textArray[0] == "MARUFUJI" and textArray[1] == "MARKET":
    return "Grocery"
  if textArray[0] == "TST*" and textArray[1] == "PULCINELLA":
    return "Dining"
  if textArray[0] == "K" and textArray[1] == "MARKET":
    return "Grocery"
  if textArray[0] == "MEMBERSHIP" and textArray[1] == "FEE":
    return "AMEX FEE"
  if textArray[0] == "MID" and textArray[1] == "ATLANTIC":
    return "Dining"
  if textArray[0] == "HUNAN" and textArray[1] == "EXPRESSMCLEAN":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "PULCINELMCLEAN":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "CHIANG":
    return "Dining"
  if textArray[0] == "FAES" and textArray[1] == "BOOKSTORBETHESDA":
    return "Other/HY"
  if textArray[0] == "NIH" and textArray[1] == "BLDG":
    return "Other/HY"
  if textArray[0] == "VIRGIN" and textArray[1] == "HOTELS":
    return "Travel"
  if textArray[0] == "STARLUX" and textArray[1] == "AIRLINES":
    return "Travel"
  if textArray[0] == "MEDSTAR" and textArray[1] == "CAPITARLINGTON":
    return "Entertainment"
  if textArray[0] == "99" and textArray[1] == "RANCH":
    return "Grocery"
  if textArray[0] == "WEEE" and textArray[1] == "INC.":
    return "Grocery"
  if textArray[0] == "PAYPAL" and textArray[1] == "*ALLSTATEINS":
    return "House Expense"
  if textArray[0] == "TAROKO" and textArray[1] == "PARK" and amount <= 10:
    return "Entertainment"
  if textArray[0] == "TAROKO" and textArray[1] == "PARK" and amount > 10:
    return "Dining"
  if textArray[0] == "TUNG" and textArray[1] == "JENG" and amount <= 10:
    return "Entertainment"
  if textArray[0] == "TUNG" and textArray[1] == "JENG" and amount > 10:
    return "Dining"
  if textArray[0] == "HAN" and textArray[1] == "SHEN" and amount <= 10:
    return "Entertainment"
  if textArray[0] == "HAN" and textArray[1] == "SHEN" and amount > 10:
    return "Dining"
  if textArray[0] == "SHIN" and textArray[1] == "KONG" and amount <= 10:
    return "Entertainment"
  if textArray[0] == "SHIN" and textArray[1] == "KONG" and amount > 10:
    return "Dining"
  if textArray[0] == "OSAKAMETRO" and textArray[1] == "FAOSAKA":
    return "Travel"
  if textArray[0] == "OSAKA" and textArray[1] == "MONORAIOSAKA":
    return "Travel"
  if textArray[0] == "FAMILY" and textArray[1] == "MART":
    return "Grocery"
  if textArray[0] == "KITASHINCHIMAGCHE" and textArray[1] == "AIOSAKA":
    return "Dining"
  if textArray[0] == "SEVEN" and textArray[1] == "ELEVEN":
    return "Grocery"
  if textArray[0] == "DAIKOKU" and textArray[1] == "DRUG":
    return "Others/YL"
  if textArray[0] == "SUGI" and textArray[1] == "PHARMACY":
    return "Others/YL"
  if textArray[0] == "TEPPANYAKI" and textArray[1] == "RIO":
    return "Dining"
  if textArray[0] == "GOOGLE" and textArray[1] == "*YOUTUBEPREMI":
    return "Youtube"
  if textArray[0] == "BEST" and textArray[1] == "BUY":
    return "Other/HY"
  if textArray[0] == "LILLYS" and textArray[1] == "DUMPLIFAIRFAX":
    return "Dining"
  if textArray[0] == "MOMO" and textArray[1] == "CAFE":
    return "Dining"
  if textArray[0] == "H" and textArray[1] == "MART":
    return "Grocery"
  if textArray[0] == "MARKET" and textArray[1] == "EXPRESBALTIMORE":
    return "Dining"
  if textArray[0] == "MERA" and textArray[1] == "CORPORATCANCÚN":
    return "Entertainment"
  if textArray[0] == "KAOHSIUNG" and textArray[1] == "RAPKAOHSIUNG":
    return "Grocery"
  if textArray[0] == "MING" and textArray[1] == "YUAN":
    return "Dining"
  if textArray[0] == "SMARTRIP" and textArray[1] == "WASHWASHINGTON":
    return "Travel"
  if textArray[0] == "MR.LEE'S" and textArray[1] == "HAIRANNANDALE":
    return "Other/HY"
  if textArray[0] == "TJ" and textArray[1] == "CAFE":
    return "Dining"
  if textArray[0] == "HAAGEN" and textArray[1] == "DAZS":
    return "Dining"
  if textArray[0] == "TERIYAKI" and textArray[1] == "WAY" and "MCLEAN" in textArray and "VA" in textArray:
    return "Dining"
  if textArray[0] == "CPI*CANTEEN" and textArray[1] == "VSUITLAND" and "MD" in textArray:
    return "Dining"
  if textArray[0] == "FALAFEL" and textArray[1] == "INC":
    return "Dining"
  if textArray[0] == "VENCHI" and textArray[1] == "TYSONSMCLEAN":
    return "Dining"
  if textArray[0] == "BURLINGTON" and textArray[1] == "STORES":
    return "Others/YL"
  if textArray[0] == "MARUFUJI" and textArray[1] == "MARKVIENNA":
    return "Grocery"
  if textArray[0] == "GRUBHUB*PULCINEW" and textArray[1] == "YORK":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "MARUICHIVIENNA":
    return "Dining"
  if textArray[0] == "ARAMARK" and textArray[1] == "EPICUWASHINGTON":
    return "Dining"
  if textArray[0] == "525310" and textArray[1] == "SSPFRIROISSY":
    return "Dining"
  if textArray[0] == "CARREFOUR" and textArray[1] == "EXPRESS":
    return "Grocery"
  if textArray[0] == "PERCHE" and textArray[1] == "NO":
    return "Dining"
  if textArray[0] == "GELATERIA" and textArray[1] == "PASCO":
    return "Dining" 
  if textArray[0] == "L'OPERA" and textArray[1] == "CAFFE'":
    return "Dining"
  if textArray[0] == "CONAD" and textArray[1] == "CITY":
    return "Dining"
  if textArray[0] == "LUCCA" and textArray[1] == "SS" and textArray[2] == "DPR":
    return "Dining"
  if textArray[0] == "MC" and textArray[1] == "DONALD'S":
    return "Dining"
  if textArray[0] == "VARRONE" and textArray[1] == "PASTA":
    return "Dining"

  if len(textArray) == 2:
    return False
  
  if textArray[0] == "APPLE" and textArray[1] == "ONLINE" and textArray[2] == "STORE":
    return "Other/HY"
  if textArray[0] == "IL" and textArray[1] == "POOM" and textArray[2] == "HYANG":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "MARUICHI" and textArray[2] == "SELECTVIENNA":
    return "Grocery"
  if textArray[0] == "FLEXIBLE" and textArray[1] == "BUSINESS" and textArray[2] == "CREDIT":
    return "Dining"
  if textArray[0] == "PAYPAL" and textArray[1] == "*WASHINGTONG" and textArray[2] == "4029357733":
    return "1333 gas"
  if textArray[0] == "MCLEAN" and textArray[1] == "COMMUNITY" and textArray[2] == "CENMCLEAN":
    return "RY Class"
  if textArray[0] == "IL" and textArray[1] == "POOM" and textArray[2] == "HYANGFAIRFAX":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "VIENNA" and textArray[2] == "IVIENNA":
    return "Dining"
  if textArray[0] == "YUAN" and textArray[1] == "DUNG" and textArray[2] == "JIUHSINCHU":
    return "Dining"
  if textArray[0] == "Hilton" and textArray[1] == "Resort" and textArray[2] == "Credit":
    return "Travel"
  if textArray[0] == "AMEX" and textArray[1] == "Flight" and textArray[2] == "Credit":
    return "AMEX FEE"
  if textArray[0] == "LALA" and textArray[1] == "PORT" and textArray[2] == "EXPOCITY":
    return "Others/YL"
  if textArray[0] == "KIX" and textArray[1] == "CHOKUEI" and textArray[2] == "MENZEI":
    return "Others/YL"
  if textArray[0] == "TST*" and textArray[1] == "TEASN" and textArray[2] == "YOVIENNA":
    return "Dining"
  if textArray[0] == "SHIN" and textArray[1] == "CHUN" and textArray[2] == "SULANNANDALE":
    return "Dining"
  if textArray[0] == "GA" and textArray[1] == "INST" and textArray[2] == "TECH":
    return "Steven"
  if textArray[0] == "SO" and textArray[1] == "GONG" and textArray[2] == "DONG":
    return "Dining"
  if textArray[0] == "BANH" and textArray[1] == "CUON" and textArray[2] == "SAIFALLS":
    return "Dining"
  if textArray[0] == "EL" and textArray[1] == "TIO" and textArray[2] == "MCLEANMCLEAN":
    return "Dining"
  if textArray[0] == "PAYPAL" and textArray[1] == "*KARDO" and textArray[2] == "SRL":
    return "Other/HY"
  if textArray[0] == "FAR" and textArray[1] == "EASTERN" and textArray[2] == "DHSINCHU":
    return "Dining"
  if textArray[0] == "CHARM" and textArray[1] == "SIROO" and textArray[2] == "IANNANDALE":
    return "Dining"
  if textArray[0] == "Flower" and textArray[1] == "Child" and textArray[2] == "Bethesda":
    return "Dining"
  if textArray[0] == "DR" and textArray[1] == "UPPASNA" and textArray[2] == "CHMCLEAN":
    return "Medical Expense"
  if textArray[0] == "GOOGLE*YOUTUBEPREMIU" and textArray[1] == "G.CO" and textArray[2] == "HELPPAY#":
    return "Youtube"
  if textArray[0] == "MICRO" and textArray[1] == "CENTER" and textArray[2] == "81":
    return "Other/HY"
  if textArray[0] == "HOTEL" and textArray[1] == "PORTRAIT" and textArray[2] == "FIRENFIRENZE":
    return "Dining"
  if textArray[0] == "NEW" and textArray[1] == "BAHIA" and textArray[2] == "CAFE":
    return "Dining"
  if textArray[0] == "ANTICA" and textArray[1] == "GIOSTRA" and textArray[2] == "TOSCAFIRENZE":
    return "Dining"
  if textArray[0] == "RISTORANTE" and textArray[1] == "SANTA" and textArray[2] == "MARFIRENZE":
    return "Dining"
  if textArray[0] == "AUTOLINEE-TOSBORGO" and textArray[1] == "SAN" and textArray[2] == "LORENZO":
    return "Travel"
  if textArray[0] == "PROPAY" and textArray[1] == "RESIDENTIAL" and textArray[2] == "RNewton":
    return "Condo Fee"
  if textArray[0] == "OPERA" and textArray[1] == "DELLA" and textArray[2] == "PPISA":
    return "Dining"
  if textArray[0] == "OPERA" and textArray[1] == "DELLA" and textArray[2] == "PRIMAZIAPISA":
    return "Entertainment"

  if len(textArray) == 3:
    return False

  if textArray[0] == "ADJ" and textArray[1] == "REDIST" and textArray[2] == "CASH" and textArray[3] == "ADV" and textArray[4] == "BAL":
    return "AMEX FEE"
  if textArray[0] == "DR" and textArray[1] == "ADJ" and textArray[2] == "REDIST" and textArray[3] == "PURCH" and textArray[4] == "PRIN":
    return "AMEX FEE"
  if textArray[0] == "AUTOPAY" and textArray[1] == "PAYMENT" and textArray[2] == "-" and textArray[3] == "THANK":
    return "AMEX FEE"
  if textArray[0] == "DOMINION" and textArray[1] == "WINE" and textArray[2] == "AND" and textArray[3] == "BEFalls" and textArray[4] == "Church":
    return "Dining"
  if textArray[0] == "FAR" and textArray[1] == "EASTERN" and textArray[2] == "DKAOHSIUNG" and textArray[3] == "CIT":
    return "Dining"
  if textArray[0] == "HONG" and textArray[1] == "KONG" and textArray[2] == "PALFALLS" and textArray[3] == "CHURCH":
    return "Dining"
  if textArray[0] == "NIC*-" and textArray[1] == "DTA" and textArray[2] == "-" and textArray[3] == "TAX":
    return "Car Expense"
  if textArray[0] == "OPENAI" and textArray[1] == "*CHATGPT" and textArray[2] == "SUBSSAN" and textArray[3] =="FRANCISCO":
    return "Software"
  if textArray[0] == "GOOD" and textArray[1] == "FORTUNE" and textArray[2] == "FALLS" and textArray[3] == "CHURCH":
    return "Grocery"
  if textArray[0] == "TST*" and textArray[1] == "PETER" and textArray[2] == "CHANG" and textArray[3] == "MCLMCLEAN":
    return "Dining"
  if textArray[0] == "TST*" and textArray[1] == "PARIS" and textArray[2] == "BAGUETTE" and textArray[3] == "MCLEAN":
    return "Dining"
  if textArray[0] == "766" and textArray[1] == "JGILBERT" and textArray[2] == "MCLEAN" and textArray[3] == "MCLEAN":
    return "Dining"
  if textArray[0] == "PAYPAL" and textArray[1] == "*DOMINION" and textArray[2] == "EN" and textArray[3] == "8048192917":
    return "Utility"
  if textArray[0] == "BOTTEGA" and textArray[1] == "DEL" and textArray[2] == "TARTUFO" and textArray[3] == "FIRENZE":
    return "Dining"
  if textArray[0] == "ANTICA" and textArray[1] == "E" and textArray[2] == "PREMIATA" and textArray[3] == "TILUCCA":
    return "Dining"
  if textArray[0] == "LA" and textArray[1] == "BOTTEGA" and textArray[2] == "DEL" and textArray[3] == "TARTULUCCA":
    return "Dining"
  if textArray[0] == "SUMUP*LAZZARONI" and textArray[1] == "DI" and textArray[2] == "TSANGIULIANO" and textArray[3] == "TERME":
    return "Dining"

  if len(textArray) == 4:
    return False

  if textArray[0] == "PISA" and textArray[1] == "S." and textArray[2] == "ROSSORE" and textArray[3] == "SS" and textArray[4] == "DPISA":
    return "Dining"

  return False
