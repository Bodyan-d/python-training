
def text_counter(text):
    counter = 0
    for word in text.split():
        counter += 1
        
    return counter

def analyze_numbers(numbers):
    try:
        max_num = numbers[0]
        min_num = numbers[0]
        avg = 0
        
        for n in numbers:
            avg += n
            if n > max_num:
                max_num = n
            if n < min_num:
                min_num = n
                
        avg = round(avg /  len(numbers))
    except IndexError:
        raise IndexError("Objesct is empty")
        
    return {"max": max_num, "min": min_num, "avg": avg}

def sum_all(*args):
    summ = 0 
    for i in args:
        summ += i
    return summ     

def create_user(**kwargs):
    try:
        # 1. Перевірка обовʼязкових полів
        if "name" not in kwargs or "age" not in kwargs:
            raise ValueError("Missing required fields: name or age")

        name = kwargs["name"]
        age = kwargs["age"]

        # 2. Перевірка типу age
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a number")

        # 3. Створення користувача
        user = {
            "name": name,
            "age": age
        }

        # 4. Додаємо всі інші поля
        for key, value in kwargs.items():
            if key not in user:
                user[key] = value

        return user

    except Exception as e:
        return f"Error: {e}"

def main():
    
    # print("Words in text is: ", text_counter("My words counter test"))

    # print(analyze_numbers([]))
    print(create_user(name="Anna", age=25))
    print(create_user(name="Bob"))
    print(create_user(age=30))
    print(create_user(name="Mike", age="twenty"))
    print(create_user(name="Kate", age=28, email="kate@mail.com"))
    
    return 0
    
    
if __name__ == "__main__":
    main()