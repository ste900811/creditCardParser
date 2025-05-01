from objects.banks import Banks

class Discover(Banks):
  def __init__(self, statementDate):
    super().__init__(statementDate)
    self.bankType = "discover"
