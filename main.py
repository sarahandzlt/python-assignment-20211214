# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from accounts import BasicAccount
from accounts import PremiumAccount


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 写个测试，别无脑进去送死
    teacher = BasicAccount("TEACHER", 500)
    student = PremiumAccount("STUDENT", 500, 0, 5000)

    teacher.deposit(5000)
    student.deposit(5000)

    #测试简单取钱，都会成功
    teacher.withdraw(1250)
    student.withdraw(1250)

    #测试超额取钱，都会失败
    teacher.withdraw(10000)
    student.withdraw(10000)

    #测试只有premium成功的情况
    teacher.withdraw(6000)
    student.withdraw(6000)

    print("{name} Balance: {balance}, {abalance}".format(name=teacher.getName(),
                                                         balance=teacher.getBalance(),
                                                         abalance=teacher.getAvailableBalance()))

    print("{name} Balance: {balance}, {abalance}".format(name=student.getName(),
                                                         balance=student.getBalance(),
                                                         abalance=student.getAvailableBalance()))
    #在这里premium应该关不掉
    teacher.closeAccount()
    student.closeAccount()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
