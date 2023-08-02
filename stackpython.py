# s = (input().split())

# print(s)

# print("stack length : ",len(s))

# s2 = []
# for x in s:
#     s2.append(x)

# s2.pop()
# print(len(s2))
# print("-----------------------------------")
# i = len(s2)-1
# while i>=0:
#     print(s2[i])
#     i=i-1
# for x in range(len(s2)-1,-1,-1):
#     print(s2[x])
# print("-----------------------------------")
# print("stack num 2 length :",len(s2))

# if len(s2)==0:
#     print("s2 is empty")
# else :
#     print("s2 is not empty")

stack = [] #declare the array of stack

#add items to stack
stack.append(input("Enter * after the last input : "))
while stack[len(stack)-1] != '*':
    stack.append(input())

stack.pop() #delete the last item of stack
print(stack)

print("stack length :",len(stack))#length of stack

if len(stack)==0:
    print("stack is empty")
else:
    print("Not empty")