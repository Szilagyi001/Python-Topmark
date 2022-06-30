#Assesment program
#L.Silaghi
#17/03/2021

print ("Welcome to my Assessment program")
print('*********Liviu Silaghi**********')
input("\nPress Enter to run the program")

def readFile():
    #Import
    import csv

    input("Press Enter to read the files")

    #Opem file in read mode
    f=open("J27C76 File for students.csv")
    csvFile=csv.reader(f)

    #Create empty arrays
    firstnames=[]
    surnames=[]
    marks=[]

    #Loop through each row in the file
    for row in csvFile:
        #Append each item to arrays
        firstnames.append(row[0]) #colum A
        surnames.append(row[1]) #colom B
        marks.append(int(row[2])) #colom C

    #Close the file
    f.close()
    return firstnames, surnames, marks


#find the highest number
def findtheTopmark(marks, firstnames, surnames):
    #set the search value to 0
    topMark= marks[0]
    topName=firstnames[0]
    topsurName=surnames[0]
    #loop for the lenght of array
    for counter in range(1,len(firstnames)):
        #if bigger valu was found make it equals to counter
       if  marks[counter] > topMark:
           topMark=marks[counter]
           topName=firstnames[counter]
           topsurName=surnames[counter]
    return topMark, topName, topsurName


#display
def display(topMark, topName, topsurName):
    #Print the result
    print("\nStudent with the top mark is:",topName,topsurName,"with mark of",topMark,"")
    f=open("Exam-TheResult.txt","w")
    input("\nPress Enter to save the file")
    #Write the result to the file
    f.write("Student with the top mark is: " +topName+ " "+topsurName+" with mark of " +str(topMark)+".") 
    print("\nThe file has been written successfully")
    #Close the file
    f.close()                                                                               
    input("Press Enter to exit")

   
#run
firstnames, surnames, marks=readFile()
topMark, topName, topsurName=findtheTopmark(marks, firstnames, surnames)

display(topMark, topName, topsurName)




