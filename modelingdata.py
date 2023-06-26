from enum import Enum

class Name:
    first:str
    middle:str
    last:str

    def __init__(self, first:str, middle:str, last:str):
        self.first = first
        self.middle = middle
        self.last = last


class Address:
    mesto: str
    ulica: str
    psc: str
    popisne: str

    def __init__(self, mesto:str, ulica:str, psc:str, popisne:str):
        self.mesto = mesto
        self.ulica = ulica
        self.psc = psc
        self.popisne = popisne


class BankNumber:
    pre_num:str
    main_num:str
    bank_num:str
    swift:str
    iban:str

    def __init__(self, pre_num:str, main_num:str, bank_num:str, swift:str, iban:str):
        self.pre_num = pre_num
        self.main_num = main_num
        self.bank_num = bank_num
        self.swift = swift
        self.iban = iban

class Coop_type(Enum):
    INTERN = 1
    EXTERN = 2

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class Payout:
    monthly:str
    hourly:str
    efort_based:str

    def __init__(self, monthly:str):
        self.monthly = monthly
        self.hourly = None
        self.efort_based = None

class TypeOfContract(Enum):
    HPP = 1
    INTERN = 2
    DPP = 3
    DPC = 4
    OSVC = 5
    PART_TIME = 6

class Ozp(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3



class Employee:
    name:Name
    bank_number:BankNumber
    email:str
    id:str
    address:Address
    is_active:bool
    coop_type:Coop_type
    position:str
    start_date:str
    gender:Gender
    payout:Payout
    type_of_contract:TypeOfContract
    is_student:bool
    on_childcare:bool
    ozp:Ozp


    def __init__(self, name:str, bank_number:BankNumber, email:str, id:str, address:Address, is_active:bool, coop_type:Coop_type, position:str,
            start_date:str, gender:Gender, payout:Payout, type_of_contract:TypeOfContract, is_student:bool, on_childcare:bool, ozp:Ozp):

        self.name = name
        self.bank_number = bank_number
        self.email = email
        self.id =id
        self.address = address
        self.is_active =is_active
        self.coop_type = coop_type
        self.position = position
        self.start_date = start_date
        self.gender = gender
        self.payout = payout
        self.type_of_contract = type_of_contract
        self.is_student = is_student
        self.on_childcare = on_childcare
        self.ozp = ozp

class Type(Enum):
    GROCERIES = 1
    SPORT = 2
    OTHER = 3

class Size:
    lenght:int
    width:int
    height:int

    def __init__(self, lenght:int, width:int, height:int):
        self.lenght = lenght
        self.width = width
        self.height = height

class Perishability:
    is_perishable:bool
    date_of_exp:str

    def __init__(self, is_perishable:bool, date_of_exp:str):
        self.is_perishable = is_perishable
        self.date_of_exp = date_of_exp


class Product:
    price:str
    amount:int
    id:str
    name:str
    note:str
    type_of:Type
    weight:str
    size:Size
    perishability:Perishability
    is_fair_trade:bool

    def __init__(self,price:str, amount:str, id:str, name:str, note:str, type_of:Type, weight:str, size:Size, perishability:Perishability, is_fair_trade:bool):

        self.price = price
        self.amount = amount
        self.id = id
        self.name = name
        self.note = note
        self.type = type_of
        self.weight = weight
        self.size = size
        self.perishability = perishability
        self.is_fair_trade = is_fair_trade

class Purchase:
    product:list[Product]
    date:str

    def __init__(self, product:list[Product], date:str):
        self.product = product
        self.date = date

class RegularCustomer:
    purchase:Purchase
    name:Name
    email:str
    id:str
    phone_num:str

    def __init__(self, purchase:Purchase, name:Name, email:str, id:str, phone_num:str):
        self.purchase = purchase
        self.name = name
        self.email = email
        self.id = id
        self.phone_num = phone_num

class Sale:
    date:str
    product:Product
    employee:Employee

    def __init__(self, date:str, product:Product, employee:Employee):
        self.date = date
        self.product = product
        self.employee = employee

class Store:
    address:Address
    brand:str
    name:str
    employees:list[Employee]
    products:list[Product]
    regularcustomers:list[RegularCustomer]
    purchases:list[Purchase]

    def __init__(self, address:Address, brand:str, name:str, ) -> None:
        
        self.address = address
        self.brand = brand
        self.name = name
        self.employees = []
        self.products = []
        self.regularcustomers = []
        self.sales = []

    def add_employee(self, employee:Employee):
        self.employees.append(employee)

    def add_product(self, product:Product):
        self.products.append(product)

    def add_customer(self, customer:RegularCustomer):
        self.regularcustomers.append(customer)

    def add_sale(self, sale:Sale):
        self.sales.append(sale)

class Salary:
    employee:Employee
    date:str
    amount:str

    def __init__(self, employee:Employee, date:str, amount:str) -> None:
        self.employee = employee
        self.date = date
        self.amount = amount





employee1_name = Name("Anna", "Magdalenka", "Ferenciova")
employee1_bank = BankNumber("45456456", "4545", "54545", "4545", "5454")
employee1_address = Address("Brno", "Raklovska", "61800", "65")
employee1_payout = Payout("656")
employee1_typeofcontract = TypeOfContract(1)

employee2_name = Name("Ani", "Magdalenka", "Ferenciova")
employee2_bank = BankNumber("45456", "46665", "5565", "4555", "6654")
employee2_address = Address("Praha", "Raklovska", "12000", "65")
employee2_payout = Payout("888")

employee1 = Employee(employee1_name, employee1_bank, "raklo@email.cz", "655", employee1_address, True, Coop_type.INTERN, 
                     "manager", "28.2.2022", Gender.FEMALE, employee1_payout, TypeOfContract.HPP, False, False, Ozp.ONE)

employee2 = Employee(employee2_name, employee2_bank, "rsdsdo@email.cz", "656", employee2_address, True, Coop_type.INTERN, 
                     "ceo", "28.2.2020", Gender.MALE, employee2_payout, TypeOfContract.HPP, False, False, Ozp.ONE)

size1 = Size(10,20,30)
size2 = Size(30,20,10)
perishability1 = Perishability(True, "28.12.2023")
perishability2 = Perishability(True, "27.12.2021")

product1 = Product("22", 3, "587", "mrtkos","nope", Type.GROCERIES, "6", size1, perishability1, True)
product2 = Product("24", 6, "664", "mrtkoska","nope", Type.GROCERIES, "7", size2, perishability2, True)

purchase1 = Purchase("28.6.2022", product1)
purchase2 = Purchase("24.5.2023", product2)

cus_name1 = Name("Marian", "", "Hoss")
cus_name2 = Name("Marta", "", "Mala")

customer1 = RegularCustomer(purchase1, cus_name1, "sds@gmail.com", "54", "9562648")
customer2 = RegularCustomer(purchase2, cus_name2, "ssadasd@gmail.com", "51", "95695656")

sale1 = Sale("24.11.2022", product1, employee1)
sale2 = Sale("24.12.2021", product2, employee2)

address3 = Address("Prague", "stromovka", "120 00", "54")


store = Store(address3, "Ultimate_shop", "Ultimated")
store.add_product(product1)
store.add_product(product2)
store.add_customer(customer1)
store.add_customer(customer2)
store.add_employee(employee1)
store.add_employee(employee2)
store.add_sale(sale1)
store.add_sale(sale2)


salary1 = Salary(employee1, "15.5.2023", "30000")
salary2 = Salary(employee2, "15.5.2023", "60000")



