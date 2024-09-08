def return_true():
    
    return True

print(return_true())

a = False
if a and return_true():
    print('True')
else:
    print('False')