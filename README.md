# python
Python coding for fun

# Dependencies
* Conda - download miniconda https://docs.conda.io/en/latest/miniconda.html 

# Installation
* git clone this repo
* conda env create -f environment.yml
* conda activate python-exercise1
* pip install -r requirements.txt 
* python main.py "pP37fGxOKzCJlM5V5Joeyttiv2dEcg5M" 

# Notes
Invoiced API Key "pP37fGxOKzCJlM5V5Joeyttiv2dEcg5M" is only temporary. If this fails, create a new account and add replace with your own key.

# Coding Challenge
* Set up the project and verify you can get a list of Customers. https://www.invoiced.com/resources/docs/api/?python#list-all-customers
* Obfuscate the Customer's Name, only keeping the first and last letters. The rest can be asterix or random characters
* Replace the email address with something randomized @example.com. The emails should be unique.
* If the InvoicedCustomer state value is two letters, write it into the NewBillingSystem.state_code, if it's longer, write it into the NewBillingSystem.state
* "Migrate" the data based on the following rules and write to a csv file.

```
Invoiced Customer 
    "address1": "342 Amber St",
    "address2": null,
    "attention_to": "Sarah Fisher",
    "city": "Hill Valley",
    "country": "US",
    "email": "billing@acmecorp.com",
    "id": 1234,
    "name": "Acme",
    "notes": null,
    "number": "CUST-0001",
    "phone": "(820) 297-2983",
    "postal_code": "94523",
    "sign_up_url": null,
    "state": "CA",
    "statement_pdf_url": "https://dundermifflin.invoiced.com/statements/t3NmhUomra3g3ueSNnbtUgrr/pdf
```

## Data Mapping between systems.
    NewBillingSystem.address1: InvoicedCustomer.address1
    NewBillingSystem.address2: InvoicedCustomer.address2
    NewBillingSystem.address3: InvoicedCustomer.attention_to
    NewBillingSystem.city: InvoicedCustomer.city
    NewBillingSystem.country : InvoicedCustomer.country
    NewBillingSystem.email: InvoicedCustomer.email
    NewBillingSystem:company_name: InvoicedCustomer.name
    NewBillingSystem.notes: InvoicedCustomer.notes
    NewBillingSystem:id: InvoicedCustomer.number
    NewBillingSystem.telephone: InvoicedCustomer.phone
    NewBillingSystem.postal_code:InvoicedCustomer.postal_code
    NewBillingSystem.state_code : InvoicedCustomer.state (See logic in Coding Challenge notes)
    NewBillingSystem.state : InvoicedCustomer.state (See logic in Coding Challenge notes)
    
 
