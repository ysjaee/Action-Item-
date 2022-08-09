# 표준 입력으로 게임 캐릭터 능력치(체력,마나,AP)가 입력
# 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의 피해량이 출력되게 만들기
# 티버의 피해량은 AP * 0.65 + 400 (AP는 ability power, 주문력)

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        damage = 0
        damage = ability_power * 0.65 + 400
        damage = float(damage)
        print("티버 : 피해량 %1f"%damage)

health, mana, ability_power = map(float,input().split())

x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()