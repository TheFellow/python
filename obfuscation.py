class CustomerObfuscation:
    def __init__(self, *steps) -> None:
        self.steps = steps

    def Process(self, customerList):
        return [self.processCustomer(c) for c in customerList]

    def processCustomer(self, customer):
        for step in self.steps:
            customer = step.Process(customer)
        return customer

class NameObfuscater:
    def Process(self, customer):
        nameParts = customer["name"].split()
        newNameParts = [name[0] + '*' * (len(name) - 1) for name in nameParts]
        customer["name"] = ' '.join(newNameParts)
        return customer

class EmailObfuscater:
    def __init__(self):
        self.emailCounter = 0

    def Process(self, customer):
        self.emailCounter += 1
        customer["email"] = f"some.user{self.emailCounter}@example.com"
        return customer

CustomerObfuscater = CustomerObfuscation(
        NameObfuscater(),
        EmailObfuscater())