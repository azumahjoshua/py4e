class Employee:
    # firstName, lastName, pay

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstName, self.lastName)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.firstName, self.lastName, self.pay)
