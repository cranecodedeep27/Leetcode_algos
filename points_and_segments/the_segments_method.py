# Метод отрезков
def is_overlapping(a: list[int], b: list[int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])

def merge_two(a: list[int], b: list[int]) -> list[int]:
    return [min(a[0], b[0]), max(a[1], b[1])]

def merge(segments: list[list[int]]) -> list[list[int]]:
    if not segments:
        return []
    # Сортировка
    segments.sort()
    
    # Инициализация
    result = [segments[0]]
    
    for i in range(1, len(segments)):
        # прозод по остальным отрезкам
        last = result[-1]
        current = segments[i]
        
        if is_overlapping(last, current):
            result[-1] = merge_two(last, current)
        else:
            result.append(current)
        
    return result

print(merge([
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
]))

# Время: O(n*log(n))
# Память: O(n)
