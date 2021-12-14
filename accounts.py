import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BasicAccount:
    def __init__(self, acName: string, openingBalance: float, overdraftLimit=0,
                 acNum='', cardNum='', cardExp=None, overdraft=0):
        self.name = acName
        if acNum is None or len(acNum) <= 0:
            self.acNum = random.randint(1000000000000000, 9999999999999999).__str__()
        else:
            self.acNum = acNum
        self.balance = openingBalance
        if cardNum is None or len(cardNum) == 0:
            self.cardNum = random.randint(1000000000000000, 9999999999999999).__str__()
        else:
            self.cardNum = cardNum
        if cardExp is None or len(cardExp) == 0:
            d1 = datetime.now()
            expiry_date = d1 + relativedelta(years=+3)
            cardExp = (expiry_date.month, expiry_date.year)
        else:
            self.cardExp = cardExp
        self.overdraft = overdraft
        self.overdraftLimit = overdraftLimit
        self.type = 'basic'

    # cardNum = []
    # for i in range(1, 101):
    #     s = '6109261775700087'
    #     cardNum.append(s)
    # print('The cardNum should be containing a string containing a 16-digit number:', cardNum)
    # from datetime import datetime
    # date = str("December,2021")
    # cardExp = datetime.strftime(date, '%m,%y')
    # print(cardExp)

    def deposit(self, amount):
        if amount < 0:
            print('cannot deposit negative amounts')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            # and amount > (self.balance + self.overdraftLimit):
            # 后面这个应该是premium的逻辑
            print('An amount is considered to be invalid')
            print('Can not withdraw £{amount}'.format(amount=amount))
            return 'terminate'
        else:
            self.balance -= amount
            print('{Name} has withdrawn £{amount}, New balance is £{balance}'
                  .format(Name=self.name, amount=amount, balance=self.getBalance()))

    def balance(self):
        """ Provides the current balance """
        return self.balance

    def getAvailableBalance(self):
        if self.overdraft > 0:
            return -self.overdraft
        return self.balance

    def getBalance(self):
        if self.overdraft > 0:
            return self.getAvailableBalance()  # 'a negative value'
        else:
            return self.balance

    def printBalance(self):
        if self.overdraft > 0:
            # self.overdraft = self.balance - amount
            print('overdraft ie remaining:', self.overdraftLimit - self.overdraft)
        else:
            return self.balance

    def getName(self):
        return str(self.name)

    def getAcNum(self):
        return str(self.acNum)

    def issueNewCard(self):
        print('a new card with the expiry date being 3 years to the month from now')
        d1 = datetime.now()
        expiry_date = d1 + relativedelta(years=+3)
        # import datetime as datetime
        # d1 = datetime.datetime.now()
        # expiry_date = d1 + datetime.datetime.timedelta(years=3)
        print(expiry_date)

    def closeAccount(self):
        if self.overdraft > 0:
            print('Can not close account due to customer being overdrawn by £<amount>')
            return False
        # 已经隐含这个条件 if self.overdraft <= 0:
        self.withdraw(self.balance)
        return True


    def del_BasicAccount_acNum(self):
        del self.acNum
        return False

    print('Can not close account due to customer being overdrawn by £<amount>')

    def __str__(self):
        return 'Account[' + self.acNum + '] - ' + \
               self.name + ', ' + self.type + ' account = ' + str(self.balance)


class PremiumAccount(BasicAccount):

    def __init__(self, acName: string, openingBalance: float, initialOverdraft: float, overdraftLimit=0,
                 acNum='', cardNum='', cardExp=''):
        super().__init__(acName=acName, acNum=acNum,
                         openingBalance=openingBalance, cardNum=cardNum,
                         cardExp=cardExp, overdraftLimit=overdraftLimit)
        self.overdraft = initialOverdraft
        self.type = 'premium'

    def withdraw(self, amount):
        if amount > self.balance and amount > (self.balance + self.overdraftLimit - self.overdraft):
            # 后面这个应该是premium的逻辑
            print('An amount is considered to be invalid')
            print('Can not withdraw £<amount>')
            return 'terminate'
        else:
            # 判断是不是overdraft
            if amount > self.balance:  # 走到这里已经隐含amount < (self.balance + self.overdraftLimit - self.overdraft)
                if self.balance <= 0:
                    self.overdraft += amount
                else:  # self.balance还有钱，一部分overdraft
                    self.overdraft = amount - self.balance
                    self.balance = 0
            else:
                self.balance -= amount
            print('{Name} has withdrawn £{amount}, New balance is £{balance}'
                  .format(Name=self.name, amount=amount, balance=self.getBalance()))

    def setoverdraftLimit(self, amount):
        self.overdraftLimit = amount  # self.balance - amount
        return self.overdraftLimit  # 'state amount'

    # 基础类里做
    # def getAvailableBalance(self):
    #     if self.overdraft > 0:
    #         return -self.overdraft
    #     return self.balance
    #
    # def printBalance(self, amount):
    #     if self.overdraft > 0:
    #         self.overdraft = self.balance - amount
    #         print('overdraft ie remaining:', self.overdraft)
    #     else:
    #         return self.balance

    #基础类做就可以了
    # def closeAccount(self):
    #     if self.overdraft <= 0:
    #         self.balance.withdraw()
    #         return True
    #     if self.overdraft > 0:
    #         return False
    #     print('Can not close account due to customer being overdrawn by £<amount>')

    # base class
    # def __str__(self):
    #     return 'Account[' + self.acNum + '] - ' + self.name + ', ' + self.type + ' account = ' + str(self.balance)
