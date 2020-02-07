# coding: utf-8
# Your code here!
import math
import random

light_num,ave_num = map(int, input().split())
light_list = list(map(int, input().split()))
interval_num = int(input())
interval_list = [list(map(int,input().split())) for _ in range(interval_num)]
#print(light_num)
#print(ave_num)
#print(light_list)
#print(interval_list)
all_interval_list = []
print(interval_list)
for k in range(math.factorial(interval_num)):
    all_interval_list = (random.shuffle(interval_list))
    print(k)
    print(all_interval_list)
    """
    for in_list in all_interval_list:
        #print(in_list)
        sum = 0
        for i in range(in_list[1]-in_list[0]+1):
            #print(i+in_list[0]-1)
            sum += int(light_list[i])
        ave = sum/(in_list[1]-in_list[0]+1)
        if ave < ave_num:
            for j in range(in_list[1]-in_list[0]+1):
                light_list[j] += int(ave_num - ave + 1)
        
        #print("ave : ")
        #print(sum/(in_list[1]-in_list[0]+1))
     """




print(*light_list)


