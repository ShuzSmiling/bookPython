# this program show work '*'

def main():
    # print 9 lines of
    # increasing length
    for count in range(1, 10):
        print('w' * count)
        
    # print 9 lines of
    # decreasing length
    for count in range(8, 0, -1):
        print('w' * count)
        

if __name__ == '__main__':
    main()