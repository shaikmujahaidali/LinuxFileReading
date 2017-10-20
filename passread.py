import os
def passopen():
    myuserfile= open ("/home/ec2-user/passwd","r+")
    s=myuserfile.read()
    print s
    myuserfile.close()
passopen()
