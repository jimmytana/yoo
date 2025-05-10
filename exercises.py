def pascal_to_camel(text:str):
    # text=" "
    # for i in text:
    #     if text[0].capitalize==True :
    #         b=text[0].lower()
    #         text=text.append(b)
    return text[0].lower()+text[1:]
            
            
text=input("please enter your  pascal text format :")
a=pascal_to_camel(text)
print(f"the converted string is as follows : {a}")
another case 


def calmel_to_snake(calmel):
    snake=" "
    for char in calmel:
        if char. isupper():
            snake+="_"+char.lower()
        else :
            snake+=char
    return snake.lstrip('_')
calmel=input("please enter the text to convert in snake case :")
a=calmel_to_snake(calmel)
print (f"the converted string is :{a}")
