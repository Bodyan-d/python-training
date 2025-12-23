numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([n * 10 for n in numbers if n%2 == 0])

words = ["apple", "hi", "banana", "cat", "kiwi"]

print([word.upper() for word in words if len(word) > 3])

words = ["apple", "banana", "kiwi"]

print({word: len(word) for word in words})

grades = {
    "math": 80,
    "english": 65,
    "history": 90,
    "biology": 55
}

print({subject: score + 5 for subject, score in grades.items() if score >= 70})

def get_even_sum(numbers):
    return sum(n for n in numbers if n % 2 == 0)

print(get_even_sum([1,2,32,4124,4,5,1]))

with open("numbers.txt", "r") as numbers:
    print([int(n)**2 for n in numbers if int(n)%2 == 0])
    
    
class Counter:
    def __init__(self):
        self._value = 0
        
    def increment(self):
        self._value += 1
    
    def decrement(self):
        self._value = max(0, self._value - 1)
    
    def get_value(self):
        return self._value