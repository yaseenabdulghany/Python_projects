def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print('Invalid input, Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid input, Try again!')
            else:
                return int(inp)
        else:
            return int(inp)


class Employee:
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary

    def __str__(self):
        return f'Employee : {self.name} has age {self.age} and salary {self.salary}'

    def __repr__(self):
        return F'Employee(name="{self.name}", age={self.age}, salary={self.salary})'


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nEnter employee data: ')
        name = input('Enter the name: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')
        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return

        print('\n**Employees list**')
        for e in self.employees:
            print(e)

    def delete_employees_with_age(self, age_from, age_to):
        for idx in range(len(self.employees) - 1, -1, -1):
            e = self.employees[idx]
            if age_from <= e.age <= age_to:
                print('\tDeleting', e.name)
                self.employees.pop(idx)

    def find_employee_by_name(self, name):
        for e in self.employees:
            if e.name == name:
                return e
        return None

    def update_salary_by_name(self, name, salary):
        e = self.find_employee_by_name(name)
        if e is None:
            print('Error: No employee with such a name')
        else:
            e.salary = salary


class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeesManager()

    def print_menu(self):
        print('\nprogram options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.EmployeesManager.add_employee()
            elif choice == 2:
                self.EmployeesManager.list_employees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                self.EmployeesManager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input('Enter a name: ')
                salary = input_valid_int('Enter new salary: ')
                self.EmployeesManager.update_salary_by_name(name, salary)
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()
