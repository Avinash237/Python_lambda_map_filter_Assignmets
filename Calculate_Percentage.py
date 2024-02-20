
def cal_per(per):
    if per > 75:
        print("Destinction")
    elif per > 65:
        print('First class')
    elif per > 55:
        print('Second Calss')
    elif per > 45:
        print('Third Calss')
    else:
        print('Failed')



per = [78, 45, 69, 80, 90, 93, 96, 98, 35]
print(list(map(cal_per,per)))