def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")
# READ UP ON f-strings and return

def dollars_to_float(d):
    return float(d.lstrip('$'))
#important to code "return"

def percent_to_float(p):
    return float(p.rstrip('%'))

main()