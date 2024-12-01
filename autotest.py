from function import salary, hello_who

assert hello_who("q") == "Hello, q", "AAAAAAA"
assert hello_who("qq") == "Hello, qq", "AAAAAAA"
assert hello_who("qqq") == "Hello, qqq", "AAAAAAA"
assert hello_who("qqqq") == "Hello, qqqq", "AAAAAAA"
assert salary(2, 10) == 20, "AAAAAA"
assert salary(3, 10) == 30, "AAAAAA"
assert salary(4, 10) == 40, "AAAAAA"
