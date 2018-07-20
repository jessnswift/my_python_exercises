class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

# Create a class that contains information about employees
# of a company and define methods to get/set employee name,
# job title, and start date.

class Employee(object):

    def __init__(self, employee_name, job_title, start_date, salary):
        self.employee_name = employee_name
        self.job_title = job_title
        self.start_date = start_date
        self.salary = salary

    def get_employee_name(self):
        """Returns the name of the employee"""

        return self.employee_name

# Consider the concept of aggregation, and modify the Company
# class so that you assign employees to a company.

# Create a company
Avo = Company('Avo', '2018')

# three employees
Jessica = Employee('Jess', 'Web Developer', 'September 26', '100000')
Zach = Employee('Zach', 'Web Developer', 'September 26', '100000')
Olivia = Employee('Olivia', 'Web Developer', 'September 26', '100000')

# then assign the employees to the company.
Avo.employee.add(Jessica)
Avo.employee.add(Zach)
Avo.employee.add(Olivia)

# print(Avo.employee)

# for employees in Avo.employees:
#     print(employee_name, job_title, start_date, salary)