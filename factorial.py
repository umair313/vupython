def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def main():
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is {factorial(n)}")


if __name__ == "__main__":
    main()
