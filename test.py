looper = 19
try:

    f = open('Working_Accounts.txt', 'r')
    x = f.readlines()
    y = len(x)-1
    last_line = 19
    print("The last line is: ", last_line)
    print('looper is ', looper)
            
except:

    last_line = 0

print(last_line)
if looper == last_line:
    f = open('Working_Accounts.txt', 'w')
    f.truncate() 
    print("txt file is cleared")
else:
    print("txt file is not cleared")
