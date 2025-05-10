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