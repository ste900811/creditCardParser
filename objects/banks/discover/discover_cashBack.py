from objects.banks.discover.discover import Discover

class DiscoverCashBack(Discover):
  def __init__(self, bankName, cardType, statementDate):
    super().__init__(bankName, cardType, statementDate)
