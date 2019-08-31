## Reduction
print((lambda x: x + 1)(2)) # 3

## Lambda can be named
add_one = lambda x: x + 1
print(add_one(4)) # 5

## Multple arguments
full_name = lambda first, last: f"Full name: {first} {last}"
print(full_name("Tanawit", "Pattanaveerangkoon")) # Tanawit Pattanaveerangkoon

## Immediately Invoked Function Expression
x = (lambda x, y: x + y)(2, 3)
print(x) # 5

## Higher-order function
high_ord_func = lambda x, func: x + func(x)

x = high_ord_func(2, lambda x: x * x)
print(x) # 6

x = high_ord_func(2, lambda x: x + 3)
print(x) # 7

## Arguments
x = (lambda x, y, z: x + y + z)(1, 2, 3)
print(x) # 6

x = (lambda x, y, z=3: x + y + z)(1, y=2)
print(x) # 6

x = (lambda *args: sum(args))(1,2,3)
print(x) # 6

x = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print(x) # 6

x = (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
print(x) # 6