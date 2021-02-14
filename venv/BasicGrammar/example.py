print("CRAPS赌博游戏")
from random import randint
'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
设定游戏开始时玩家有1000元的赌注
'''
money = 1000
while money > 0:
    print(f'您的总资产为{money}元')
    go_on = False
    while True:
        dept = int(input("请下注："))
        if 0 < dept <= money:
            print("下注金额大于现有资产")
            break
    first = randint(1,6) + randint(1,6)#randint()生成指定范围内的随机整数
    print(f'玩家摇出了{first}点')
    if first == 7 or first == 11:
        print("玩家胜")
        money += dept
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜")
        money -= dept
    else:
        go_on = True
    while go_on:
        go_on = False
        current = randint(1,6) + randint(1,6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print("庄家胜")
            money -= dept
        elif current == first:
            print("玩家胜")
            money += dept
        else:
            go_on = True
print('您破产了，游戏结束！')

