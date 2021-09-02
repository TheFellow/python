import re

def passThru(s):
    return lambda d: d[s]

def passThruWhen(s, predicate):
    def whenTrue(d):
        if d[s] is not None and predicate(d[s]):
            return d[s]
        return ""
    return whenTrue

def isStateCode(s):
    return re.match("^[a-zA-Z]{2}$", s)

customerMap = {
    "address1": passThru("address1"),
    "address2": passThru("address2"),
    "address3": passThru("attention_to"),
    "city": passThru("city"),
    "country": passThru("country"),
    "email": passThru("email"),
    "company_name": passThru("name"),
    "notes": passThru("notes"),
    "id": passThru("number"),
    "telephone": passThru("phone"),
    "postal_code": passThru("postal_code"),
    "state_code": passThruWhen("state", isStateCode),
    "state": passThruWhen("state", lambda s: not isStateCode(s)),
}

def InvoicedCustomerToBillingCustomer(invoicedCustomer):
    billedCustomer = {}
    for key in customerMap:
        billedCustomer[key] = customerMap[key](invoicedCustomer)

    return billedCustomer

# Testing
if __name__ == "__main__":
    customer = {
        "address1": "123 Main St",
        "address2": "Suite A",
        "attention_to": "John Smith",
        "city": "San Francisco",
        "country": "USA",
        "email": "username@domain.com",
        "name": "John Customer",
        "notes": "",
        "number": "ABC-123",
        "phone": "(650)430-4876",
        "postal_code": "90123",
        "state": "PA"
    }
    print(InvoicedCustomerToBillingCustomer(customer))