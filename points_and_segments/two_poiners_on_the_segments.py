# Два указателя на отрезках
def is_overlapping(a: list[int], b: list[int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])

def overlap_two_segments(a: list[int], b: list[int]) -> list[int]:
    return [max(a[0], b[0]), min(a[1], b[1])]

def intersect(s1: list[list[int]], s2: list[list[int]]) -> list[list[int]]:
    result = []
    p1 = 0
    p2 = 0
    
    while p1 < len(s1) and p2 < len(s2):
        if is_overlapping(s1[p1], s2[p2]):
            result.append(overlap_two_segments(s1[p1], s2[p2]))
        
        if s1[p1][1] < s2[p2][1]:
            p1 += 1
        else:
            p2 += 1
            
    return result

print(intersect(s1=[[1, 3], [5, 7], [9, 12]], s2=[[2, 6], [8, 10]]))

# Время: O(n+m)
# Память: O(max(n, m))