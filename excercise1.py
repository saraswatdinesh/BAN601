def get_inputs():
    hours = float(input("Enter Hours : "))
    rate = float(input("Enter Rate : "))
    return(hours, rate)


def pay_calculate(ot_hour, rate):
    if ot_hour > 40:
        pay = (40* rate ) + ((ot_hour - 40) * rate * 1.5)
    else :
        pay = ot_hour * rate
    return pay

def main():
    hours, rate = get_inputs()
    #hours = float(input("Enter Hours : "))
    #45rate = float(input("Enter Rate : "))
    pay = pay_calculate(hours, rate)
    print("Pay : ", pay)

if __name__ = "__main__":
    main()

