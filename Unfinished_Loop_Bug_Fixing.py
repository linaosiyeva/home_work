#Unfinished Loop - Bug Fixing #1

#Oh no, Timmy's created an infinite loop! 
#Help Timmy find and fix the bug in his unfinished For Loop!

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res += [i]
        i += 1
    return res

def create_array(n):
    return [i for i in range(1,n+1)]
create_array = lambda n: list(range(1,n+1))
