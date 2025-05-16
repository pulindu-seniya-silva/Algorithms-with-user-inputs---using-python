#1, 2, 4, 7,11...

def recursiveSolution(n):
    if n == 1:
        return 1
    else:
        return recursiveSolution(n - 1) + (n - 1)

def main():
    while True:
        try:
            n = int(input('Enter the number'))
        except ValueError:
            print('Invalid input')
            continue
        if n == -1:
            print('program terminated')
            break
        print(f"{recursiveSolution(n)}")
    
if __name__ == "__main__":
    main()



    
    
        
