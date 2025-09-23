# # def solution(sizes):
    
# #     w_list = []
# #     h_list = []
# #     for i in range(len(sizes)):
# #         w_list.append(sizes[i][0])
# #         h_list.append(sizes[i][1])
# #     w = max(w_list)
# #     h = max(h_list)
# #     result = w * h
    
# #     return result

# def solution(sizes):
#     answer = 0
#     w = []
#     h = []
    
#     for i in range(len(sizes)):
#         w.append(max(sizes[i]))
#         h.append(min(sizes[i]))
    
#     answer = max(w) * max(h)
#     return answer

def solution(sizes):
    
    W = []
    H = []
    
    for size in sizes:
        w = size[0]
        h = size[1]
        if size[1] > size[0]:
            size[0] = h
            size[1] = w
        W.append(size[0])
        H.append(size[1])
    
    max_W = max(W)
    max_H = max(H)
        
    return max_W * max_H
    