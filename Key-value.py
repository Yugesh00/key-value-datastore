import threading 
from threading import*
import time
import json

datastore={} 
master={}
n=input('Do you want to import master datastore and perform operation on it yes/no: ')
if(n=='yes'):
    print('Loading datastore...')
    with open('master.json','r') as masteropen:
        data_load = json.load(masteropen)
    datastore = data_load
    print('Loaded master datastore')
    print(datastore)


n=datastore
   
def show():
    return n

def create(key,value,timeout=0):
    if key in n:
        print("Error! Key already exits") 
    else:
        if(key.isalpha()):
            if len(n)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    n[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("Error!! Invalid key name!! key name must contain only alphabets and no special characters or numbers")

def read(key):
    if key not in n:
        print("Error!! Given key does not exist in datastore. Please enter a valid key") 
    else:
        b=n[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri



def delete(key):
    if key not in n:
        print("Error!! Given key does not exist in database. Please enter a valid key") 
    else:
        b=n[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del n[key]
                print("Key is successfully deleted")
            else:
                print("Error!! time-to-live of",key,"has expired") 
        else:
            del n[key]
            print("Key is successfully deleted")


while(-1):
    m=int(input("Enter 1. Create 2. Read 3. Delete 4. Show 5. Exit "))
    if(m==5):
        break
    if(m==1):
        i=input("Enter a key ")
        j=int(input("Enter its value "))
        create(i,j)
        
    if(m==2):
        i=input("Enter the key to read ")
        print(read(str(i)))

    if(m==3):
        i=input("Enter the key to delete ")
        delete(i)

    if(m==4):
        print(datastore)


import json
datastore=n
with open('datastore.json','w') as fp:
    json.dump(datastore,fp)

print('Your datastore after operations are: ')
print(datastore)

x=input('Do want to save this in new temporary datastore? yes/no ')
if(x=='yes'):
    data={}
    import json
    with open('datastore.json','w') as fp:
        json.dump(datastore,fp)
    print("thank you")
    exit()

x=input('Do you want to save this in the master datastore? yes/no :')
if(x=='yes'):
    data={}
    import json
    with open('master.json','r') as fp:
        data = json.load(fp)

    master = dict(data)
    master.update(datastore)
    with open('master.json','w') as fp:
        json.dump(master,fp)
print('All task done, thanks')






