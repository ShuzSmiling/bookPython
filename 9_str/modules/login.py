# get_login accept name, surname, id
# return full name for login

def get_login_name(first, last, idnumber):
    # get 3 sym in name
    set1 = first[0:3]
    
    # get 3 sym in surname:
    set2 = last[0:3]
    
    # get last 3 sym in idnumber
    set3 = idnumber[-3:]
    
    # return idnumber
    return f'{set1}{set2}{set3}'


# valid_password accepts password
# and return True or False
# password must contain:
# * len(password) >= 7
# * 1 sym and 1 num
# * 1 sym upper case and lower case

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_alpha = False
    
    # start validate
    if len(password) >= 7:
        correct_length = True
        
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
            if ch.isalpha():
                has_alpha = True
                
        if correct_length and has_uppercase and \
            has_lowercase and has_digit and \
                has_alpha:
            return True 
        
        return False