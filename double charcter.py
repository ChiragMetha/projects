def character(input_string):
    doubledstring = ''.join(char * 2 for char in input_string)
    return doubledstring

result1= character("now")
print(result1)
result2 = character("123a!")
print(result2)