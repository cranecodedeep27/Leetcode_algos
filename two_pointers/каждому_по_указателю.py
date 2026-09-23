def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # Инициализация
    p1 = 0
    p2 = 0
    result = []
    # Цикл логика движения указателей
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
    return result

print(intersect([1, 2, 5, 6, 8, 12, 13], [2, 8, 12, 99, 101]))

#  Время: O(n+m)
#  Память: O(min(n, m))
