# def greeting():
#     print("Good morning!")

# greeting()

# def night():
#     print("Good night!")

# night()
# night()
# night()

# def square(num: int):
#     print(num**2)


# # square(2)

# def repeat(word: str, num: int ):
#     print(word*num)

# repeat("hi", 4)

# def add(num1: int, num2: int):
#     print(num1+num2)

# add(2, 4)

name = input("What is your name? ")

# def hi(person: str):
#     print(f"Hi {person}")

# hi(name)
# hi("anamika")

age = input("How old are you? ")

def bio(person: str, old: int):
    print(f"Hi {person}! You are {old} years old!")

bio(name, age)
bio(name, 110)