열거하다는 뜻의 함수로 여러 가지 자료형(list, set, tuple등)을 인덱스를 포함한 enumerate 객체로 리턴한다.

사용방법은 다음과 같다.

>>> a = [1,2,3,2]
>>> a
[1,2,3,2]
>>> list(enumerate(a))
[(0,1),(1,2),(2,3),(3,2)]

이처럼 list로 결과를 추출하며, 인덱스를 자동으로 부여해준다.

다음은 enumerate를 사용해 list a에 대하여 각각 인덱스와 인덱스에 해당하는 요소를 출력하는 구문이다.

for i, v in enumerate(a):
    print(i, v)