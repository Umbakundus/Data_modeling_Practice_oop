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

    def __init__(self, monthly:str, hourly:str, efort_based:str):
        self.monthly = monthly
        self.hourly = hourly
        self.efort_based = efort_based

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
    product:Product
    date:str

    def __init__(self, product:Product, date:str):
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