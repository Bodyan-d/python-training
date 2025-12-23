
def save_logs(res):
    with open("log.txt", "a") as logs:
        logs.write(f"Sum: {res}\n")

def main():
    summ = 0

    with open("input.txt", "r") as file:
        for line in file:
            summ += int(line)
            
    save_logs(summ)
    return summ


if __name__ == "__main__":
    print(main())