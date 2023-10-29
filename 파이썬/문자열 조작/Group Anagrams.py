# https://leetcode.com/problems/group-anagrams/
# https://www.youtube.com/watch?v=8T8U-vcQ3JU
# https://www.youtube.com/watch?v=3YqPKLZF_WU

# 내가 푼거

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = []
        for k,v in enumerate(strs):
            anagrams.append([''.join(sorted(v)),k])
        anagrams.sort(key = lambda x : x[0])

        dic = {}
        #print(anagrams)
        for anagram in anagrams:
            if anagram[0] in dic:
                dic[anagram[0]].append(anagram[1])
                continue
            else:
                dic[anagram[0]] = [anagram[1]]

        lists = list(dic.values())
        
        for li in range(len(lists)):
            for idx in range(len(lists[li])):
                lists[li][idx] = strs[lists[li][idx]]

        # lists.sort(key = lambda x: len(x)) 안해도 되네?

        return lists
        # return can possible any order!


# 정렬하여 딕셔너리에 추가

# ''.join(리스트)
# ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 
# 를 'abc'의 문자열로 합쳐서 반환

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        # anagrams[aet] = ate, eat, tea

        return list(anagrams.values())

        # return can possible any order!