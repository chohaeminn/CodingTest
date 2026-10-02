def solution(progresses, speeds):
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    
    answer = []
    current_day = days[0]
    count = 0
    
    for day in days:
        if day <= current_day:
            count += 1
        else:
            answer.append(count)
            current_day = day
            count = 1
            
    answer.append(count)
    
    return answer