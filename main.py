# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import TestTask1
from accounts import BasicAccount
from accounts import PremiumAccount


def main():
    list = TestTask1.generatePerferences([
        [0.29617759, 0.434362233, 0.033033194, 0.758968209],
        [0.559322784, 0.455791536, 0.770423104, 0.770423104],
        [0.590959915, 0.519580134, 0.731606088, 0.767473037],
        [0.555107939, 0.344284876, 0.543483969, 0.396020991],
        [0.83627928, 0.950927664, 0.871995522, 0.852851116],
        [0.79342723, 1.509148129, 0.700621254, 0.659306216]
    ])
    print(list)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    # # 写个测试，别无脑进去送死
    # teacher = BasicAccount("TEACHER", 500)
    # student = PremiumAccount("STUDENT", 500, 0, 5000)
    #
    # teacher.deposit(5000)
    # student.deposit(5000)
    #
    # #测试简单取钱，都会成功
    # teacher.withdraw(1250)
    # student.withdraw(1250)
    #
    # #测试超额取钱，都会失败
    # teacher.withdraw(10000)
    # student.withdraw(10000)
    #
    # #测试只有premium成功的情况
    # teacher.withdraw(6000)
    # student.withdraw(6000)
    #
    # print("{name} Balance: {balance}, {abalance}".format(name=teacher.getName(),
    #                                                      balance=teacher.getBalance(),
    #                                                      abalance=teacher.getAvailableBalance()))
    #
    # print("{name} Balance: {balance}, {abalance}".format(name=student.getName(),
    #                                                      balance=student.getBalance(),
    #                                                      abalance=student.getAvailableBalance()))
    # #在这里premium应该关不掉
    # teacher.closeAccount()
    # student.closeAccount()
    #
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
