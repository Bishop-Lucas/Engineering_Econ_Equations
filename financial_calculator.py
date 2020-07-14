#import numpy
import math

active = 'y'
### Creating the functions for 
def get_interest():
    # interest rate
    print("What is the rate of return: ")
    i = input()
    return i
def get_periods():
    # number of periods
    print("What is the total number of terms: ")
    n = input()
    return n
def get_present():
    # Present sum of money
    print("What is the present sum of money: ")
    p = input()
    return p
def get_future(): 
    # Future sum of money
    print("What is the future sum of money: ")
    f = input()
    return f
def get_add():
    # money to be added per term
    print("What is the sum of money you want to add per term: ")
    a = input()
    return a
def compound_f():
    i = float(get_interest())
    n = int(get_periods())
    p = int(get_present())
    # The equation for compound interest
    cf = p*((1+i)**n)
    cfr = round(cf,2)
    return cfr
def compound_p():
    i = float(get_interest())
    n = int(get_periods())
    f = int(get_future())
    # The equation for determining the present value of compounded interest
    cp = f*((1+i)**(-n))
    cpr = round(cp,2)
    return cpr
def compound_s():
    i = float(get_interest())
    n = int(get_periods())
    a = int(get_add())
    # The equation for determing value with equal monthly payments
    cs = a*((((1+i)**n)-1)/i)
    csr = round(cs,2)
    return csr
def compound_sf():
    i = float(get_interest())
    n = int(get_periods())
    f = int(get_future())
    # The equation for determing value with equal monthly payments
    csf = f*(i/(((1+i)**n)-1))
    csfr = round(csf,2)
    return csfr

while active == 'y':
    print("This tool lets you calculate various values of money based upon compounding interest for various terms and conditions.")
    print("If you would like to know the value of a future sum of money given a present sum, the interest rate anumber of terms please press f")
    print("If you would like to know the value of a present sum of money given a future sum, the interest rate anumber of terms please press p")
    print("If you would like to know the value of a future sum of money given a set amount added every term, the interest rate anumber of terms please press a")
    print("If you would like to know the value needed every term for given a future sum, the interest rate anumber of terms please press r")
    response = input()
    if response == 'f':
        fv = compound_f()
        print("The future value is " + str(fv))
    elif response == 'p':
        pv = compound_p()
        print("The present value is " + str(pv))
    elif response == 'a':
        av = compound_s()
        print("The present value is " + str(av))
    elif response == 'r':
        rv = compound_sf()
        print("The present value is " + str(rv))
    else:
        print('Your selection was not valid')
        
    print("Would you like to calculate another value?(y/n)")
    active = input()