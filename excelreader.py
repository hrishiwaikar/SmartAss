from openpyxl import load_workbook

class Student :
    def __init__(self):
        self.name=None
        self.rollno=None
        self.div = None
        self.batch = None
        self.elective1 = None
        self.elective11=None
        self.elective2 = None
        self.elective22=None

studentlist=[]

def getStudentList():

    wb = load_workbook('beA.xlsx')
    ws = wb.active
    for row in ws:

        if row[4].value!=None:
            stud = Student()
            stud.rollno = str(int(row[0].value))
            stud.name = row[1].value
            stud.batch=row[3].value
            stud.div=row[2].value
            stud.elective1=row[4].value
            stud.elective11=row[5].value
            stud.elective2=row[6].value
            stud.elective22=row[7].value

            studentlist.append(stud)
    return studentlist

getStudentList()

for s in studentlist:
    print s.batch

