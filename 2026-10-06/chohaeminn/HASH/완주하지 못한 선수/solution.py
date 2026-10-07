from collections import Counter

def solution(partipicant, completion):
    # 참가자와 완주자의 이름을 카운트
    answer = Counter(partipicant) - Counter(completion)
    #Counter({'leo': 1, 'kiki': 1, 'eden': 1})
    #Counter(Counter({'eden': 1, 'kiki': 1})
    #Counter({'leo': 1, 'kiki': 1, 'eden': 1}) - Counter({'eden': 1, 'kiki': 1})
    #Counter({'leo': 1})


    return list(answer.keys())[0]
    #dict_keys(['leo'])
    #['leo']
    "leo"