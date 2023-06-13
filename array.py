num = [9,1,2,5,7,4,6,8,6,9,8,4,2,6,7]


def sort(num):
    sorted_num=[]
    while num:
     for i in num:
         for j in num:
             if j<i:
                 break
         else:
          sorted_num.append(i)
          del num[num.index(i)]
    return sorted_num            
print(sort(num))