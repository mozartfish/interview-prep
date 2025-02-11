def divide_numbers(a: str, b: str) -> None:
    try:
        num1, num2 = int(a), int(b)
        print(f"{num1 / num2}")
    except ValueError:
        print(f"Error: Invalid value!")
    except ZeroDivisionError:
        print(f"Error: Division by zero!")
    except Exception as error:
        print(f"An error occured:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
