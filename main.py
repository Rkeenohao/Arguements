def greeting(name,message = "hi"):
    print (f"{message} {name}")
greeting("KEENO")

def subtract(x,y):
    '''demonstrate position arguments'''

    print(f"{x-y}")
subtract(4,3)

print(subtract.__doc__)