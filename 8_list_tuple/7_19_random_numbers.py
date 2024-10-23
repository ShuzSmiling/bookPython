# This programm assign random num
# two-dimensional list
import random

# Constant for row and column
ROWS = 3
COLS = 4

def main():
    # Create two-dimensional list
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    # fill list random num
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
            
    # Show random num
    print(values)
    

if __name__ == '__main__':
    main()
    