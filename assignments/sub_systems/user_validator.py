import re
from datetime import datetime

pattern = ''
logs = []

# TO STORE LOGS
def log(f_name = 'FUNCTION()', status = False, msg = 'NO MESSAGE'):
    timestamp = datetime.now().strftime('%Y/%M/%D %H:%M:%S')
    logs.append({
        "timestamp": timestamp,
        "function": f_name,
        "status": 'SUCCESS' if status else 'ERROR',
        "message": '\''+msg+'\''
    })
    
# VIEW ALL SAVED LOGS
def view_logs():
    for l in logs:
        print()
        for v in l.values():
            print(v, end=' ')
    print()

# VALIDATE USERNAME
def validate_username(value = ''):
    # Must start with a letter, no spaces, no trailing underscore.
    # Extra: Minimum 4 characters, and maximum 15 characters.
    f_name = f'validate_username(\'{value}\')'
    pattern = re.compile(r'^[A-Za-z][A-Za-z0-9_]{2,13}[A-Za-z0-9]$')
    if pattern.match(value):
        log(f_name, True, 'Valid Username')
        return True
    log(f_name, False, 'Invalid Username')
    return False

# VALIDATE PASSWORD
def validate_password(value = ''):
    # Min 10 characters, must have atleast one uppercase, digit and special characters (not comma).
    # Extra: Max 15 characters.
    f_name = f'validate_password(\'{value}\')'
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9,])[^,\s]{10,15}$')
    if pattern.match(value):
        log(f_name, True, 'Valid Password')
        return True
    log(f_name, False, 'Invalid Password')
    return False

# VALIDATE EMAIL
def validate_email(value = ''):
    # Must be in a standard email format.
    f_name = f'validate_email(\'{value}\')'
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$')
    if pattern.match(value):
        log(f_name, True, 'Valid Email')
        return True
    log(f_name, False, 'Invalid Email')
    return False

def validate_user(value = ''):
    f_name = f'validate_user(\'{value}\')'
    try:
        username, password, email = [x.strip() for x in value.split(',')]
        log(f_name, True, 'Valid CSV Format')
        if(validate_username(username) and validate_password(password) and validate_email(email)):
            log(f_name, True, 'Valid Inputs')
            return True
        else:
            log(f_name, False, 'Invalid Inputs')
    except ValueError:
        log(f_name, False, "Invalid CSV Format")
    return False
    
# MAIN METHOD
# def main():
#     validate_user('alice1,Password@123,alice@gmail.com') 
#     validate_user('1bob,short,bob@mail') 
#     validate_user('charlie_,ValidPass#99,charlie@yahoo.com') 
#     validate_user('Daisy,NoSpecial123,daisy@mail.com') 
#     view_logs()

# if __name__ == '__main__':
#     main()