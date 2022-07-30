import os
os.chdir("./Documents/temp/")
os.listdir()
['list.txt']
dictionary={}
with open("list.txt") as file:
    for i in file:
        (key,value)=i.split()
        dictionary[key]=value
    file.close()
print(dictionary['word'])
 
meaning
def search():
    try: 
        key=input("Enter the word for which menaing is to be found:")
        print("The meaning of", key, "is", dictionary[key])
    except:
        print("Sorry! Our Dictionary does not have this word which you are looking for")

#output
#search()
 
'''Enter the word for which meaning is to be found:a
The meaning of a is b
search()
 
Enter the word for which meaning is to be found:b
Sorry! Our Dictionary does not have this word which you are looking for'''

 
