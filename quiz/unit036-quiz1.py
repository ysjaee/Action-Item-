# 리스트에 기능 추가하기
# list에 relace 메서드를 추가한 AdvancedList 클래스를 작성
# AdvancedList는 list를 상속받아서 만들고, replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾸도록 만들기

class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new
x = AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)