# 확장자가.jpg .png인 이미지 파읾나 출력되게 만들기
# 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태여야 함
# 람다 표현식에서 확장자 검사할 때는 문자열 메서드 활용
files = ['font','1.png','10.jpg','11.gif','2.jpg','3.png','table.xslx','spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1,files)))