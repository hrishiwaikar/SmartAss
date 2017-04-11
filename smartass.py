from reportlab.pdfgen import canvas
import PyPDF2
import os

batchMode = False #Change this to True to create assignments for an entire class else keep it False for personal use

from excelreader import getStudentList

name=None
rollno = None
batch = None
classdiv = None

elective1=None
elective2 = None

directory=None
classdirectory = None

sourcefolder_1 ='CL3/'

assignments_1 = {
    'A1 BinarySearch':["Binary Search using Divide And Conquer Strategy",1],
    'A2 Quicksort':["Concurrent Quicksort using Divide And Conquer", 1],
    'A3 Booths':["Web Tool for Booth's Multiplication",1],
    'A4 DiningPhilosopher' :["Algorithm for Dining Philosopher's Problem",1],
    'A5 Calculator':["Create Mobile App for Calculator",1] ,
    'B1 8Queen':["Backtracking to solve Eight Queen Problem",1],
    'B2 Odd Even':["Concurrent Odd Even Merge sort using ROOM ",1],
    'B3 Plagiarism':["Web Application to Check Plagiarism",1],
    'B4 Calculator':["Mobile App for Calculator with Memory",1],
    'C6 Openstack':["Installation of Opensource Cloud Infrastructure",1],

}


cloud_assignments={'A6 Docker' :["Cloud Tool Docker - Use and Demonstration",1],
    'Google App':["Deployment of Web App on Google App Engine",0],

}

cybersecurity_assignments={

    'A6 Encryption':["Implement Password Data Encryption",1],
    'B5 SHA1':["Message Transmission using Hash value of SHA1",1],
    'B6 Pseudorandom':["Long term Key generation using Pseudorandom Number",1],
    'C1 IDS':["Install and Use latest IDS",1],

}

moblilecomp_assignments={
 'A6 Music Player':["Mobile Application to fetch and play music files",0],
 'Group B A2 Image Modification':["Mobile App to upload,rename and delete Image",0],
 'Group B A3 File Upload':["Mobile App to upload and download files",0],
 'Group B A4 Employee Details':["Mobile App to manage Employee Details",0]
}


bai_assignments={
    'B6 Regression': ["Linear regression on a problem using R programming", 1],
    'B3 KNN': ["Recommendation System for Training and Placement using KNN", 1],
    'Kettle BAI':["BAI Tool Kettle Use and Computation",0]
}

mobileapp_assignments={
 'B3 Palindrome':["Android App to check if a strng is Palindrome",1],
 'Camera Snapshot':["Snapshot using Camera App",1],
 'B6 Emergency Call':["Android App for Emergency call using Gyroscope",1],
 'Group A 6C Scientific Calculator':["Mobile Application for Scientific Calculator",1],
}

sourcefolder_2 ='CL4/'

assignments_2={
    'A1 Quicksort':["Concurrent Quick Sort using Divide And Conquer ",1],
    'A2 BST':["BST using Divide and Conquer on a computer cluster",1],
    'A4 MPI':["MPI program for calculating coverage",1],
    'A5 MPINODES': ["MPI program to run on varying number of nodes", 1],
    'A6 Booths':["Booths Multiplication Algorithm",1],
    'B2 VTune':["Develop a stack sampling using threads using VTune Amplifier",1],

    'B4 Gprof':["A program to check task distribution using Gprof",1],
    'B5 OddEven':["Concurrent Odd-Even Merge sort using HPC infrastructure",1],

    'B1 8QUEEN':["8 Queen Problem Using HPC Architecture",1],

}



def draw(c,astring,x,y):
    c.drawString(x, y, astring)




def createIntro(assno,title):
    global name,rollno,classdiv,batch
    c = canvas.Canvas("intro_"+assno+".pdf")
    draw(c,"Assignment No : "+assno,200,580)
    draw(c,"Title : "+title,200,550)
    draw(c,"Name : "+name,200,520)
    draw(c,"Roll No : "+rollno ,200,490)
    draw(c,"Class : "+ classdiv + "    Batch : "+batch,200,460)
    draw(c,"Remarks :",200,430)

    c.save()


def createFile(directory,introname,sourcefolder, remainingname,startpage):

    introFile = open(introname,'rb')
    remainingAssignemntFile = open(sourcefolder+remainingname,'rb')

    introReader = PyPDF2.PdfFileReader(introFile)
    remainingReader = PyPDF2.PdfFileReader(remainingAssignemntFile)

    pdfWriter = PyPDF2.PdfFileWriter()

    introPageObj = introReader.getPage(0)
    pdfWriter.addPage(introPageObj)

    for pageNum in range(startpage,remainingReader.numPages):
        pageObj = remainingReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOutputFile = open(os.path.join(directory,remainingname),'wb')
    pdfWriter.write(pdfOutputFile)
    introFile.close()
    remainingAssignemntFile.close()


def manager(assignments,sourcefolder,directory):
    #global assignments
    print rollno
    for assno in assignments:
        title = assignments[assno][0]
        startpage=assignments[assno][1]
        createIntro(assno,title)
        introname = "intro_"+assno+".pdf"
        remainingname = assno+".pdf"
        print remainingname
        createFile(directory,introname,sourcefolder,remainingname,startpage)


def acceptDetails():   #this is used in individual mode
    global name,rollno,classdiv,batch
    global assignments_1, sourcefolder_1, assignments_2, sourcefolder_2, directory_1,directory_2
    name = raw_input('Your Name : ')
    rollno = raw_input('Roll No : ')
    classdiv = raw_input('Class and Div : ')
    batch = raw_input('Batch : ')
    print 'Elective 1 :\nEnter for Cloud : 1, CS : 2 and MC: 3\n'
    elective1=raw_input()
    print 'Elective 2:\nEnter for BAI : 1 , MA : 2'
    elective2 = raw_input()

    filepath = os.path.join(os.path.dirname(__file__) + '/' + str(name) + '/' + sourcefolder_1 + '/')
    directory_1 = os.path.dirname(filepath)

    if not os.path.exists(directory_1):
        os.makedirs(directory_1)

    filepath = os.path.join(os.path.dirname(__file__) + '/' + str(name) + '/' + sourcefolder_2 + '/')
    directory_2 = os.path.dirname(filepath)

    if not os.path.exists(directory_2):
        os.makedirs(directory_2)


        # CL3 Assignments
    manager(assignments_1, sourcefolder_1, directory_1)

    if elective1 == '1':
        manager(cloud_assignments, sourcefolder_1, directory_1)
    elif elective1 == '3':
        manager(moblilecomp_assignments, sourcefolder_1, directory_1)
    elif elective1 == '2':
        manager(cybersecurity_assignments, sourcefolder_1, directory_1)

    # CL4 Assignments
    manager(assignments_2, sourcefolder_2, directory_2)

    if elective2 == '1':
        manager(bai_assignments, sourcefolder_2, directory_2)
    elif elective2 == '2':
        manager(mobileapp_assignments, sourcefolder_2, directory_2)


def addDetails(student):
    #used in batch mode
    global name,rollno,classdiv,batch,elective1,elective2,assignments_1,sourcefolder_1,assignments_2,sourcefolder_2
    name = student.name
    rollno = student.rollno
    classdiv = 'BE '+student.div
    batch = student.batch
    elective1=student.elective1
    if elective1=='Web Technology (IoT)':
        elective1=student.elective11

    elective2=student.elective2


    filepath = os.path.join(os.path.dirname(__file__) +'/'+student.div+ '/' + str(name) + '/' + sourcefolder_1 + '/')
    directory_1 = os.path.dirname(filepath)

    if not os.path.exists(directory_1):
        os.makedirs(directory_1)

    filepath = os.path.join(os.path.dirname(__file__) +'/'+student.div+ '/' + str(name) + '/' + sourcefolder_2 + '/')
    directory_2 = os.path.dirname(filepath)

    if not os.path.exists(directory_2):
        os.makedirs(directory_2)

    #CL3 Assignments
    manager(assignments_1,sourcefolder_1,directory_1)

    if elective1=='Cloud Computing':
        manager(cloud_assignments,sourcefolder_1,directory_1)
    elif elective1=='Mobile Computing':
        manager(moblilecomp_assignments,sourcefolder_1,directory_1)
    elif elective1=='Cyber Security':
        manager(cybersecurity_assignments,sourcefolder_1,directory_1)

    #CL4 Assignments
    manager(assignments_2,sourcefolder_2,directory_2)

    if elective2=='Business Analytics & Intelligence':
        manager(bai_assignments,sourcefolder_2,directory_2)
    elif elective2=='Mobile Applications':
        manager(mobileapp_assignments,sourcefolder_2,directory_2)




##### Main program starts here #####


if batchMode==False:
    global assignments_1,sourcefolder_1,assignments_2,sourcefolder_2,directory_1,directory_2
    acceptDetails()

    #filepath = '/home/hrishikesh/another/'+str(rollno)+'/'



else:

    studentlist = getStudentList()
    print studentlist[1].div
    filepath = os.path.join(os.path.dirname(__file__) + '/' + str(studentlist[2].div) + '/')
    classdirectory = os.path.dirname(filepath)

    if not os.path.exists(classdirectory):
        os.makedirs(classdirectory)

    for student in studentlist:
        addDetails(student)



