# Метод точек
def count_meeting_rooms(segments: list[list[int]]) -> int:
    points = []
    for seg in segments:
        points.append([seg[0], +1])
        points.append([seg[1], -1])
        
    points.sort()
    
    max_rooms = 0
    curr_rooms = 0
    for point in points:
        curr_rooms += point[1]
        max_rooms = max(max_rooms, curr_rooms)
        
    return max_rooms

print(count_meeting_rooms([[2, 3], [1, 7], [8, 13], [1, 100]]))

#Время: O(n*log(n))
# Память: O(n)