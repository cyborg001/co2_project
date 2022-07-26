def parentesis(arr):
    # if s =='': return False
    # arr = [e  for e in s]
    
    t = []
    for n in arr:
        
        if t == []:
            if n == ')': return False
            else: t.append(n)
        else:
            if n != t[-1]:
                t.pop(-1)
            else: t.append(n)
        # print(t)
    if t ==[]: return True

    return False
# arr = ['(', '(', '(', ')', ')', ')', ')', '(']
# print(parentesis(arr))

# # def f(s,i):
#     if i == len(s-1):
        
    

s = ''
# print(parentesis(s))

def f(a,t,i=0):
    if i == len(a)-1:
        if parentesis(a.copy()):
            s = ''
            for n in a.copy():
                s+=n
            t.append(s)
        if a[i] == '(': a[i] = ')'
        else: a[i] = '('
        if parentesis(a.copy()):
            s = ''
            for n in a.copy():
                s+=n
            t.append(s)
    else:
        # t.append(a.copy())
        f(a.copy(),t,i+1)
        if a[i] == ')': 
            a[i] = '('
        else:
            a[i] = ')'
        # t.append(a.copy())
        f(a.copy(),t,i+1)
        
        

    return t
    

# print(f('(())))'))
s = '((()))'
arr = [e for e in s]
# t = []
print(f(arr,t=[],i=0))
# print(t,'hola')