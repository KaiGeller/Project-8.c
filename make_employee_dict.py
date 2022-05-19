#Kai Geller
#GitHub Username: KaiGeller
#5/17/2022
#This code will make a dictionary with the employees name, id, salary, and email
class Employee:
    def __init__(self,emp_names,emp_ids,emp_sals,emp_emails):
        """This will create an employee object"""
        self.__name = emp_names
        self.__ids = emp_ids
        self.__sals = emp_sals
        self.__emails = emp_emails
    def get_name(self):
        """This will return the employee name"""
        return self.__name
    def get_ID_number(self):
        """This will return the employee ID number"""
        return self.__ids
    def get_salary(self):
        """This will return the employee salary"""
        return self.__sals
    def get_email_address(self):
        """This will return the employee email address"""
        return self.__emails
def make_employee_dict(names,ids,sals,emails):
    """This will make a dictionary with the employees information"""
    employee_dict={}
    for i in range(len(names)):
        employee_dict[ids[i]]=Employee(names[i],ids[i],sals[i],emails[i])
    return employee_dict
