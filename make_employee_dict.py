#Kai Geller
#GitHub Username: KaiGeller
#5/17/2022
#This code will make a dictionary with the employees name, id, salary, and email
class Employee:
    _name=""
    _ID_number=""
    _sals=0
    _emails=""
    def __init__(self,emp_names,emp_ids,emp_sals,emp_emails):
        """This will create an employee object"""
        self._name = emp_names
        self._ID_number = emp_ids
        self._sals = emp_sals
        self._emails = emp_emails
    def get_name(self):
        """This will return the employee name"""
        return self._name
    def get_ID_number(self):
        """This will return the employee ID number"""
        return self._ID_number
    def get_salary(self):
        """This will return the employee salary"""
        return self._sals
    def get_email_address(self):
        """This will return the employee email address"""
        return self._emails
def make_employee_dict(names,ids,sals,emails):
    """This will make a dictionary with the employees information"""
    employee_dict={}
    for i in range(len(names)):
        employee_dict[ids[i]]=Employee(names[i],ids[i],sals[i],emails[i])
    return employee_dict
