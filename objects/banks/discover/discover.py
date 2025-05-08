from objects.banks.banks import Banks

class Discover(Banks):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, statementDate)
    self.cardType = cardType
