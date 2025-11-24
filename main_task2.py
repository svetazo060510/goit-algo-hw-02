from collections import deque

def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є заданий рядок паліндромом, 
    використовуючи двосторонню чергу (deque).
    Нечутлива до регістру та пробілів.
    """
    # 1. Підготовка тексту: переведення до нижнього регістру та видалення пробілів
    processed_text = "".join(char for char in text if char.isalnum()).lower()
    
    if not processed_text:
        # Порожній рядок або рядок лише з пробілів/символів, що не є літерами/цифрами, 
        # вважаємо паліндромом
        return True

    # 2. Перетворення до символів для двосторонньої черги
    char_deque = deque(processed_text)
    
    # 3. Порівняння символів з обох кінців
    while len(char_deque) > 1:
        # Видаляємо та порівнюємо символи з початку (ліворуч) та кінця (праворуч)
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        
        if first_char != last_char:
            return False
            
    # Якщо залишився один елемент (непарна довжина) або жодного (парна довжина), це паліндром
    return True

# Приклади
print("\n--- Перевірка Паліндрому ---")
print(f"'Madam, I'm Adam': {is_palindrome('Madam, I\'m Adam')}") # True
print(f"'A man, a plan, a canal: Panama': {is_palindrome('A man, a plan, a canal: Panama')}") # True
print(f"'Python': {is_palindrome('Python')}") # False
print(f"'ротор': {is_palindrome('ротор')}") # True