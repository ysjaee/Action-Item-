# 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만들기

class Knight:
    def __init__(self,health,mana,armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health,x.mana,x.armor)
x.slash()