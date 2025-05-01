from objects.banks import Banks

class CapitalOne(Banks):
  def __init__(self, statementDate):
    super().__init__(statementDate)
    self.bankType = "capitalOne"
