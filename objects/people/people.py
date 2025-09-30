class people:
  def __init__(self, nameOnStatement):
    self.nameOnStatement = nameOnStatement
    self.bankObj = None

  def addbankObj(self, bankObj):
    self.bankObj = bankObj

  def filterOutPaymentsMethod(self, array):
    while array[0] == "TST*" or array[0] == "AplPay" or array[0] == "TN" or array[0] == "SQ":
      array.pop(0)

    if array[0].startswith("*"):
      array[0] = array[0][1:]
    
    return array
