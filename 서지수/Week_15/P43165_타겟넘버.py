def solution(numbers, target) :
    array = [0] 
    for i in range(len(numbers)) :
        value = []
        for j in range(len(array)) :
            value.append(array[j] - numbers[i]) 
            value.append(array[j] + numbers[i])

        array = value

    answer = array.count(target)

    return answer