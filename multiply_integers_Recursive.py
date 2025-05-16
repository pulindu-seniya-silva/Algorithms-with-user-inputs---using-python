def multiply(M, n):
    if n == 1:
        return M
    else:
        return (M + multiply(M, n - 1))


def main():
    while True:
        try:
            M = int(input("Enter 1st interger: (enter -1 to exit)"))
            if M == -1:
                break
        except ValueError:
            print("Invalid input")
            continue

        try:
            n = int(input("Enter 2nd interger: (enter -1 to exit)"));
            if n == -1:
                break
        except ValueError:
            print("Invalid input")
            continue
        x = multiply(M, n)
        print("result is", x)


if __name__ == "__main__":
    main()



