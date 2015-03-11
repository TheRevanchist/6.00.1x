import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        return self.lastName
        
    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        return (datetime.date.today() - self.birthday).days
        
    def __str__(self):
        return self.name
        
    def __ls__(self, other):
       if self.lastName == other.lastName:
           return self.name < other.name
       else:
           return self.lastName < other.lastName  
           
             
class CaFoscarini(Person):
    
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = CaFoscarini.nextIdNum
        CaFoscarini.nextIdNum += 1  
        
    def getIdNum(self):
        return self.idNum   
        
    def __ls__(self, other):
        return self.getIdNum() < other.getIdNum()
        
class UG(CaFoscarini):
    def __init__(self, name, classYear):
        CaFoscarini.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
        
class Grad(CaFoscarini):
    pass
    
def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)    
    
class TransferStudent(CaFoscarini):
    pass
    
    
class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade) 
        except KeyError:
            raise ValueError('Student not in grade book')
            
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
            
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        
def gradeReport(course):
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is '
                          + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
        return '\n'.join(report)                
        
        
ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('John Henry')
g2 = Grad('George Steinbrenner')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)

six00.addStudent(ug3)

print gradeReport(six00)        
            
            
            
            
        
               
                
                    
                                          
    
                                                                                                                                                                                                                                                                                                                                          
                  