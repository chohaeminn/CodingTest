def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        w_values = max(w,h)
        h_values = min(w,h)
        
        max_w = max(max_w, w_values)
        max_h = max(max_h, h_values)
    return max_w * max_h