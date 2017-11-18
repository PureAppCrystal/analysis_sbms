import numpy as np
import numpy.random as rnd
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def ex1():
    # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
    plt.plot([10, 20, 30, 40])
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [10, 20, 30, 40])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(rnd.random(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(rnd.random(100), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * rnd.random(100))

    plt.show()


def ex4():
    fig, subplots = plt.subplots(2, 2)

    subplots[0, 0].plot(rnd.random(50).cumsum(), 'k--')
    subplots[0, 1].hist(rnd.random(100), bins=20, color='k', alpha=0.3)
    subplots[1, 0].scatter(np.arange(100), np.arange(100) + 3 * rnd.random(100))

    plt.show()


def ex5():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([10, 20, 30, 40])

    plt.show()


def ex6():
    fig, subplots = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha=0.3)

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


def ex7():
    fig, subplots = plt.subplots(1, 1)
    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], '.')
    plt.show()


def ex8():
    fig, subplots = plt.subplots(1, 1)
    # subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], color='#000000', marker='o', linestyle='-')
    subplots.plot([8, 5, 7, 3, 2, 6], color='#000000', marker='o', linestyle='-')
    subplots.set_xticks([0, 1, 2, 3, 4, 5])
    subplots.set_xticklabels(
        ['2012', '2013', '2014', '2015', '2016', '2017'],
        rotation=0,
        fontsize='small'
    )
    subplots.set_title('사고이력')
    plt.show()


def ex9():
    fig, subplots = plt.subplots(1, 1)
    # subplots.plot(rnd.randn(50).cumsum(), 'ko--')
    subplots.plot(randn(50).cumsum(), color='#34ff22', marker='o', linestyle='-.')
    plt.show()


def ex10():
    data = randn(50).cumsum()

    fig, subplots = plt.subplots(1, 1)
    subplots.plot(data, color='#aaaaaa', linestyle='--', label='Default')
    subplots.plot(data, 'k-', drawstyle='steps-mid', label='steps-mid')

    plt.legend(loc='best')
    plt.show()


def ex11():
    flg, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum(), 'k')

    subplots.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small'
    )
    subplots.set_xlabel('Positions')
    subplots.set_title('My First Matplotlib Plot')

    plt.show()


def ex12():
    flg, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum(), 'k', label='one')
    subplots.plot(randn(100).cumsum(), 'k--', label='two')
    subplots.plot(randn(100).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


def ex13():
    # font_options = {'family': 'Malgun Gothic'}
    # plt.rc('font', ** font_options)
    # plt.rc('font', family='Malgun Gothic')
    # plt.rc('axes', unicode_minus=False)

    flg, subplots = plt.subplots(1, 1)
    subplots.plot(randn(100).cumsum(), 'k')

    subplots.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small'
    )
    subplots.set_xlabel('포인트')
    subplots.set_title('예제13 한글처리')

    plt.savefig('ex13-plot.png', dpi=400, bbox_inches='tight')
    # plt.savefig('ex13-plot.jpg', dpi=400, bbox_inches='tight')
    plt.savefig('ex13-plot.pdf', dpi=400, bbox_inches='tight')
    plt.savefig('ex13-plot.svg', dpi=400, bbox_inches='tight')

    plt.show()


def ex14():
    fontfile = 'c:/windows/fonts/malgun.ttf'
    fontname = font_manager.FontProperties(fname=fontfile).get_name()
    print(fontname)


def ex15():
    data_x = [20]


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    # ex13()
    # ex14()
