# This is recusrion


def message(times):
    if times > 0:
        print(f'{times}: This is recursion')
        message(times-1)


def main():
    message(5)

    
if __name__ == '__main__':
    main()