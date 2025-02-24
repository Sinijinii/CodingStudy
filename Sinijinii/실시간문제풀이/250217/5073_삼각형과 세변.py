pr = True

while pr:
    r1,r2,r3 = map(int,input().split())
    if r1 == 0:
            break
    if r1 == r2 == r3:
        print("Equilateral")
    
    elif max(r1,r2,r3)*2 >= r1+r2+r3:
        print("Invalid")

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("Isosceles")

    elif r1 != r2 != r3:
        print("Scalene")   
    

    