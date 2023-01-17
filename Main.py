num=int(input("what's the pass?"))

def login (password):
    set_pass=num
    if set_pass==password:
        return True

        
    else:
        return False

    

for i in range(10):
    for j in range(10):
        for k in range(10):
            a=login(int((str(i)+str(j)+str(k))))
            if a==True:
                print("you did it")
                print(str(i)+str(j)+str(k))
                break
            else:
                print("you noob")
                continue
        else:
            continue
        break
    else:
        continue
    break



