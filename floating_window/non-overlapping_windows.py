# Непересекающиеся окна
def compress_ranges(nums: list[int]) -> list[str]:
    #  Инициализация
    l = 0 
    r = 0
    result = []
    #  Внешний цикл
    while l < len(nums):
        #  Расширяем правую границу
        #  Раширяем окно
        while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
            r += 1
        # Обрабатываем окно [l, r]
        if r != l:
            result.append(f"{nums[l]}->{nums[r]}")
        else:
            result.append(f"{nums[l]}")
        # Переходим к следующей группе
        l = r + 1
        r = r + 1
        
    return result

print(compress_ranges([1, 2, 3, 5, 6, 9, 11]))

#  Время: O(n)
#  Память: O(n)