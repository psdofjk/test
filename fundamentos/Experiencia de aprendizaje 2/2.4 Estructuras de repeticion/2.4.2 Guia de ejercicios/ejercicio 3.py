try:
    num = float(input("num: "))
    div = float(input("div: "))

    if div == 0:
        raise ValueError("test")
    
    res = num / div

    print(f"res: {res}")

except ValueError as ve:
    print(f"error: {ve}")

except ZeroDivisionError:
    print("mal 0")

finally:
    print("fin")