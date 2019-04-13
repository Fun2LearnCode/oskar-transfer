basicStringInputVariable = input("This is a basic input statement here we can ask the user to put in any variable. This is a string variable input(y).").lower()
if(basicStringInputVariable == "y"):
    print("The .lower()takes whatever the user puts,then puts it in lowercase making easier to check.")
else:
    basicStringInputVariable=input("You put in the wrong character but it's ok we can try again. make sure you put in (y)")
basicLoopRepeat=0
while(basicLoopRepeat<10):
    print("This will repeat till BasicRepeat is greater than 10 or(9 since machine start at 0.)right now BasicRepeat is at",basicLoopRepeat,".")
    basicLoopRepeat=basicLoopRepeat+1
