def balance():
    c=int(input("enter the deposit amount: "))
    d=int(input("enter the withdrawal amount: "))
    balance=c-d
    return balance
print("the balabce is:",balance())