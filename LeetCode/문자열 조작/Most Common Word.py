# https://leetcode.com/problems/most-common-word/


# 리스트 컴프리헨션, Counter 객체 사용
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        splits = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        # paragraph의 각각 문자를 돌면서 [\w]에 해당하지 않는 문자가 발견된다면 그 문자를 Space Bar로 변환한다는 뜻
        # 그니까 "b,b,b,c" 같은건 "b b b c"가 된다는 뜻

        # 정규식 표현
        # [abc] : a || b || c
        # [a-c] : a ~ c ([abc]와 같다)
        # [a-zA-Z0-9] : 모든 알파벳 대/소문자와 숫자
        # . : 모든 문자 1개
        # [p.g]에는 pig, pug 모두 대응되지만, piig는 대응되지 않는다.
        # [^\d] = [^0-9] = [\D]
        # [^\w] = [^0-9a-zA-Z] = [\W]

        # 정규식 r prefix
        # r은 raw string의 의미 \을 탈출 문자로 보지 않음
        # print(r"Hello World!\n")
        # Hello World!\n

        dic = {}
        for spl in splits:
            if spl in dic:
                dic[spl] += 1
            else:
                dic[spl] = 1

            for ban in banned:
                if spl == ban:
                    dic[spl] = 0


        return max(dic, key=dic.get)
        # 딕셔너리 변수인 dic에서 값이 가장 큰 키를 가져옴

        # Counter 객체
        '''
        counts = collections.Counter(dic)
        # c = Counter({'red':4,'blue':2}) 
        # dict객체를 넣어주면 dict 그대로 count를 만들어준다
        # Counter({'red': 4, 'blue': 2})

        return counts.most_common(1)[0][0] 
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴 
        # Counter('abracadabra').most_common(3)
        # [('a', 5), ('b', 2), ('r', 2)]
        # >>> Counter('abracadabra').most_common(1)
        # [('a', 5)]

        '''