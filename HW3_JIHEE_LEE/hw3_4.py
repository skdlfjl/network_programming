'''4. 다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.

Employee 클래스에 employeeID 속성을 추가하고 getID() 메소드를 정의하라. 
getID() 메소드는 employeeID를 반환하는 메소드이다.

최종적으로 Employee 클래스를 이용하여 Employee(“IoT", 65, 2018)로 생성된 객체의 이름, 나이, ID를 출력하는 프로그램을 작성하라.'''

class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    
    def getName(self): 
        print(self.name) 
    
    def getAge(self): 
        print(self.age)


class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID
    
    def getID(self):
        print(self.employeeID)


employee = Employee("IoT", 65, 2018)
#print(employee.getName(), employee.getAge(), employee.getID())
employee.getName()
employee.getAge()
employee.getID()

