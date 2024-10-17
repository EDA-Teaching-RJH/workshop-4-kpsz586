cIn = input("Enter the name of your variable in camel case: ")
def change_case(str):
    res = [cIn[0].lower()]
    for c in cIn[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)
     
print(change_case(str))