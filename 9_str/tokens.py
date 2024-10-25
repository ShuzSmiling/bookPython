# this programm show tokenization stroke

def main():
    # stroke values for tokenization
    str1 = 'one two three four' 
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'
    
    # show on display tokens in values stroke
    display_tokens(str1, ' ')
    print()
    input('Продолжить?')
    display_tokens(str2, ':')
    print()
    input('Продолжить?')
    display_tokens(str3, '/')
    print()
    

def display_tokens(data, delimeter):
    tokens = data.split(delimeter)
    for item in tokens:
        print(f'Токен: {item}')
        

if __name__ == '__main__':
    main()
