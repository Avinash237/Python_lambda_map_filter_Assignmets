salary = [20000,3500,6000,10000,5000]
def change(amt):
    if amt>5000:
        return amt+amt*10/100
    else:
        return amt+amt*20/100
print(list(map(lambda num:change(salary),salary)))