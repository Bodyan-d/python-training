import operations

def main():
    first_num = int(input("Enter first number > "))
    second_num = int(input("Enter second number > "))
    
    summ = first_num + second_num
    division = operations.divide(first_num, second_num)
    mult = operations.multiply(first_num, second_num)
    
    print(f"Summ is: {summ}")
    print(f"Devision is: {division}")
    print(f"Multiplication is: {mult}")
    
    with open("history.txt", "a") as file:
        file.write(
            f"{first_num} + {second_num} = {summ}\n"
            f"{first_num} / {second_num} = {division}\n"
            f"{first_num} * {second_num} = {mult}\n"
            "------\n"
        )
        

if __name__ == "__main__":
    main()