def text_formater(text:str,suffix=True,preffix=True,capitalize=False):
    text=text.capitalize()
    print("the formatted text is as follows :",f"{suffix}{text}{preffix}")
text=input("please enter a text to formate: ")
suffix=input("enter the suffix :")
preffix=input("please enter your prefed preffix :")

a=text_formater(text,suffix,preffix,capitalize=True)
