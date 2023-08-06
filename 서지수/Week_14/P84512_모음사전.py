def solution(word):

    stack=["A"]
    next_word_alphabet={"A":"E", "E":"I","I":"O", "O":"U"}
    prev_word_alphabet=None
    count=0
    
    while True:
        count+=1
        dictionary_word=''.join(stack)
        
        if dictionary_word==word:
            break
            
        if len(stack)<5:
            stack.append("A")
        elif len(stack)==5:
            prev_word_alphabet=stack.pop()
            
            while prev_word_alphabet=="U":
                prev_word_alphabet=stack.pop()
            
        #다음 알파벳 추가
            stack.append(next_word_alphabet[prev_word_alphabet])
    
    return count