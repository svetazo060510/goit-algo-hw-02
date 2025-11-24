def check_brackets_symmetry(s: str) -> str:
    """
    Перевіряє симетричність та коректність пар символів-розділювачів 
    ({, [, ( ) за допомогою стеку.
    """
    # 
    stack = []
    # Словник для швидкої перевірки відповідності пар
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    # Множина, що містить тільки відкриваючі символи
    open_brackets = set(matching_brackets.values())

    for char in s:
        # Ігноруємо пробіли та інші символи
        if char in '()[]{}':
            
            if char in open_brackets:
                # 1. Якщо це відкриваюча дужка, додаємо її до стеку
                stack.append(char)
            
            elif char in matching_brackets:
                # 2. Якщо це закриваюча дужка:
                # а) Стек пустий (немає відповідної відкритої дужки)
                if not stack:
                    return f"Несиметрично: Зайва закриваюча дужка {char}"
                
                # б) Перевіряємо відповідність
                last_open = stack.pop()
                if last_open != matching_brackets[char]:
                    return f"Несиметрично: Неправильна пара ({last_open}{char})"
                    
    # 3. Після проходу всього рядка, перевіряємо чи залишилися відкриті дужки
    if not stack:
        return "Симетрично"
    else:
        # Якщо стек не пустий, є зайві відкриті дужки
        return f"Несиметрично: Зайві відкриті дужки ({len(stack)} шт.)"

# Приклади
print("\n--- Завдання 3: Перевірка Дужок (Стек) ---")
test_cases = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}", # Симетрично
    "( 23 ( 2 - 3)", # Несиметрично
    "( 11 }", # Несиметрично
    "({[]})",
    "((()))",
    "(( )"
]

# Виділяємо "чистий" рядок перед виведенням результату
# Цей код для естетики, він не є необхідним для роботи самого алгоритму перевірки дужок
for test_case in test_cases:
    # Видаляємо пробіли для коректного виводу
    clean_test_case = "".join(c for c in test_case if c in '()[]{}' or c.isdigit() or c == ' ' or c in '+-;')
    result = check_brackets_symmetry(test_case)
    print(f"'{clean_test_case}': {result}")