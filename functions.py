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



# name = input("What is your name? ")

# def hi(person: str):
#     print(f"Hi {person}")

# hi(name)
# hi("anamika")

# age = int(input("How old are you? "))

# def bio(person: str, old: int):
#     print(f"Hi {person}! You are {old} years old!")

# bio(name, age)
# bio(name, 110)

# name = bio(kf)

# def add(num1: int, num2: int) -> str:
#     return str(num1+num2)

# total = add(2, 4)
# print(total)

# def difference(num1: float, num2: float) -> float:
#     return float(abs(num1-num2))
    

# total = difference(6 , 9)
# print(total)

# for y in range(10,0,-1):
#     print(y)
    
    
# print("ITS TIME")



# def countdown(num1: int):
#     for y in range(num1,0,-1):
#         print(y)
#     print("ITS TIME")
    
# countdown(7)

title = input("What is your name?\n")
years = int(input("How old are you?\n"))

def person(age: int, name: str) -> str:
    # print(f"Hi, {name}, you are {age}!")
    if age > 16:
        return "Bro, instead of being here, get a life"
    elif age < 16:
        return "Focus on school, lil kid."
    else:
        return "Get a job."
ans = person(years, title)
print(f"{ans}")

