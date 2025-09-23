# def solution(array, commands):
    
#     arr = []
#     for t in range(len(commands)):
#         val = commands[t]
#         i = val[0]
#         j = val[1]
#         k = val[2]
        
#         val2 = array[i-1:j]
#         val2.sort()
#         arr.append(val2[k-1])
        
#     return arr

def solution(array, commands):
    
    arr = []
    for n in commands:
        i = n[0]
        j = n[1]
        k = n[2]
        extract = array[i-1:j]
        extract.sort()
        num = extract[k-1]
        arr.append(num)
    
    return arr