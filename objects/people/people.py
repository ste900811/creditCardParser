class people:
  def __init__(self, nameOnStatement):
    self.nameOnStatement = nameOnStatement
    self.bankObj = None

  def addbankObj(self, bankObj):
    self.bankObj = bankObj

  def filterOutPaymentsMethod(self, array):
    array0Set = {"TST*", "AplPay", "TN", "SQ", "GDP*", "UPSIDE*", "DD", "SNACK*", ""}
    startWithTuple = ("TST*", "UEP*", "FIV*")
    while array[0] in array0Set or array[0].startswith(startWithTuple):
      if array[0].startswith(startWithTuple) :
        array[0] = array[0].split("*")[-1]
      else:
        array.pop(0)

    if array[0].startswith("*"):
      array[0] = array[0][1:]
    
    return array
