class people:
  def __init__(self, nameOnStatement):
    self.nameOnStatement = nameOnStatement
    self.bankObj = None

  def addbankObj(self, bankObj):
    self.bankObj = bankObj
