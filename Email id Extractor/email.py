import re      #For Regex
sf=input("Enter the file name with extension:")
f=open("clean"+sf,'w') # Outputs as clean"sf value"
e=list()    #To store the email ids
with open(sf,"r") as filestream:
    for line in filestream:
        e.append(re.findall('\S+@\S+',line)) #Regex to find email id and store in the list e
for i in e:
    f.write(str(i)+'\n')    #Code to output the email ids
f.close()
    
