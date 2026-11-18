""" A Python program that reverses a list using two pointers, swapping values from the left and right ends and moving inward until the pointers meet."""

li=[1,2,3,4,5,6,7,8,9]

x = 0
y = len(li)-1

for i in range(len(li)):
    if x == y:
        break
    li[x], li[y]=li[y], li[x]
    x+=1
    y-=1

print(li)
