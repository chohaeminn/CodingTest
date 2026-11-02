def solution(array, commands):
    answer = []

    for command in commands:
        i,j,k = command

        sliced_array = array[i-1:j]
        sliced_array.sort()
        target = sliced_array[k-1]

        answer.append(target)
    return answer