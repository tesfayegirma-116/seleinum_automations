
import pandas as pd
# convert into dataframe
df = pd.read_excel("accounts.xlsx")
usernames=df['username'].tolist()
passwords=df['password'].tolist()

for i in range(0,len(usernames)):
    
    print(usernames[i]+passwords[i])