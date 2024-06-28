import random


def main():
    """
    ########################################
    Code Your Program here
    """
    numbers = []
    count = 0
    total = 0
    
    while count < 5:
        numRan = random.randint(0,100)
        numbers.append(numRan)
        total
        count += 1
        
    
    
    
    """
    ########################################
    """

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
