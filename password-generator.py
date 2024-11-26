import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
print("Генерация случайного пароля с заданными условиями.")
    
    #набор символов по умолчанию:
    chars = string.ascii_letters
    
    #добавляем цифры, если нужно:
    if use_digits:
        chars += string.digits
    
    #добавляем спец символы, если нужно:
    if use_special_chars:
        chars += string.punctuation
    
    #генерируем пароль:
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

if __name__ == "__main__":
    #пример использования:
    length = int(input("Введите длину пароля: "))
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special_chars = input("Использовать специальные символы? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_digits, use_special_chars)
    print("Сгенерированный пароль:", password)
