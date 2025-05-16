#a

def fibonacci(n):
    if n <= 1:
        return n
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)  


def main():
        while True:
            try:
                n = int(input("Enter a non negative integer (enter '-1' to quit): "))
                
                if n == -1:
                    print('Program finished')
                    break
                
                if n < 0:
                    print('Enter a non-negative number')
                    continue
                
            except ValueError:
                print('Invalid input')
                continue
            print(f"the fibonacci number is:  {fibonacci(n)}")
            

            

if __name__ == "__main__":
    main()
    


    
