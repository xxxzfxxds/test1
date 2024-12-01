from function import salary, hello_who
if salary(hours=2, salary_by_hour=10) != 20:
    print("Error")
else:
    print("qqqq")
if salary(hours=3, salary_by_hour=10) != 30:
    print("Error1")
else:
    print("qq")
if hello_who("aaaa") != "Hello, aaaa":
    print("Error2")
else:
    print("Good")
if hello_who("aaa") != "Hello, aaa":
    print("Error3")
else:
    print("Good2")
