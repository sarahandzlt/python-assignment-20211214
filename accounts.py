import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


# 总要交稿的，交稿前删掉大部分的没用的注释
class BasicAccount:
    account_number_static = 0

    @staticmethod
    def get_new_account_num():
        BasicAccount.account_number_static += 1
        return BasicAccount.account_number_static

    def __init__(self, acName: string, openingBalance: float, overdraftLimit=0,
                 # acNum='',
                 cardNum='', cardExp=None, overdraft=0):
        self.name = acName
        self.acNum = BasicAccount.get_new_account_num()
        # if acNum is None or len(acNum) <= 0:
        #     self.acNum = random.randint(1000000000000000, 9999999999999999).__str__()
        # else:
        #     self.acNum = acNum

        self.balance = openingBalance

        if cardNum is None or len(cardNum) == 0:
            self.cardNum = random.randint(1000000000000000, 9999999999999999).__str__()
        else:
            self.cardNum = cardNum
        if cardExp is None or len(cardExp) == 0:
            d1 = datetime.now()
            expiry_date = d1 + relativedelta(years=+3)
            stryear = expiry_date.__format__('%y')
            self.cardExp = (expiry_date.month, int(stryear))
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
        # if self.overdraft > 0:
        #     return -self.overdraft
        return self.balance + self.overdraftLimit - self.overdraft

    def getBalance(self):
        # 基础类应该一直都是没有overdraft，不知道理解对不对
        if self.overdraft > 0:
            return - self.overdraft  # 'a negative value'
            # return self.getAvailableBalance()
        else:
            return self.balance

    def printBalance(self):
        # 这个是print方法
        str_out = 'Account[{acNum}] - {name} , {type}  Balance = {balance}'.format(
            acNum=self.acNum, name=self.name, type=self.type, balance=self.balance)
        if self.overdraft > 0:
            # self.overdraft = self.balance - amount
            str_out += ' overdraft is: ' + self.overdraft.__str__()
        print(str_out)


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
        # self.acNum数据类型变了，IDE提醒你，颜色都变了
        # return 'Account[' + self.acNum + '] - ' + \
        #        self.name + ', ' + self.type + ' account = ' + str(self.balance)
        # 应该这样
        # return 'Account[' + self.acNum.__str__() + '] - ' + \
        #        self.name + ', ' + self.type + ' account = ' + str(self.balance)
        # 或者str(***)也行，但我觉得这个并非万能，万能应该是
        return 'Account[{acNum}] - {name} , {type}  account = {balance}'.format(
            acNum=self.acNum, name=self.name, type=self.type, balance=self.balance)
        #测试一把再放上去，这个是核心方法，报错会全局都错


class PremiumAccount(BasicAccount):

    def __init__(self, acName: string, openingBalance: float, initialOverdraft: float, overdraftLimit=0,
                 acNum='', cardNum='', cardExp=''):
        super().__init__(acName=acName, #acNum=acNum,
                         openingBalance=openingBalance, cardNum=cardNum,
                         cardExp=cardExp, overdraftLimit=overdraftLimit)
        self.overdraft = initialOverdraft
        self.type = 'premium'

    # 只能猜测deposit有bug了
    def deposit(self, amount):
        if amount < 0:
            print('cannot deposit negative amounts')
            return

        if self.overdraft > 0:
            if amount > self.overdraft:
                diff = amount - self.overdraft
                self.overdraft = 0
                self.balance += diff
            else:
                self.overdraft -= amount   # 存钱把overdraft恢复
        else:
            self.balance += amount


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

    # 基础类做就可以了
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
