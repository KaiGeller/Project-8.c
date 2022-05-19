#Kai Geller
#GitHub Username: KaiGeller
#5/17/2022
#This code will make a dictionary with the employees name, id, salary, and email
class employee:
    def __init__(self,emp_names,emp_ids,emp_sals,emp_emails):
        self.name = emp_names
        self.ids = emp_ids
        self.sals = emp_sals
        self.emails = emp_emails
    def get_name(self):
        return self.name
    def get_ID_number(self):
        return self.ids
    def get_salary(self):
        return self.sals
    def get_email_address(self):
        return self.emails
def make_employee_dict(names,ids,sals,emails):
    employee_dict={}
    for i in len(names):
        employee_dict[ids[i]]=employee(names[i],ids[i],sals[i],emails[i])
