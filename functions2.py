#write a login function which accepts the user only when username and password are matched and display a message login successful otherwise it keeps asking the user to enter the credentials until they are correct
def func():
    a=input("enter username:")
    b=input("enter password")
    if(a==b):
        print("login success")
    else:
        print("enter the credentials again")
        while(a!=b):
            func()
            break
func()
    
        
            
        
    


        
