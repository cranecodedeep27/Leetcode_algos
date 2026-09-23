def is_palindrome_permutations(s: str) -> bool:
    count = {} # ключ - символ, значение - частота
    
    for char in s:
        # Подсчитываем частоту
        count[char] = count.get(char, 0) + 1
        
    odd_count = 0
    # проверяем условие
    for freq in count.values():
        if freq % 2 == 1:
            odd_count += 1
            
    return odd_count <= 1
# Два примера
print(is_palindrome_permutations("abddab"))
print(is_palindrome_permutations("absqqs"))

# Время: O(n)
# Память: O(k) k - количество разных символов