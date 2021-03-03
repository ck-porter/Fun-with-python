"""
Student Name: CK Porter  
Program Title:  The Itsy Bitsy Aardvark
Description:  A program that presents the user with a "mad libs" style of game, give them a random
choice of words read from a file, then injected into the story from another file
"""
"""
start program
open connection to choices in csv file
create list for choices
open connection to story text
create list for story text
display choices pulling info form choices list
get user input
    -loop to ensure correct input is given (call function)
if structure to determine which value on the list user selected
run loop over newstory list to replace placeholders with user input
print each line in new story list
end program
"""

#tried to figure out how to loop through the cvs file to display output one at a time, couldn't
#figure it out, so there is a large ugly section of code which I am certain will hurt your head
#my apologizes in advance


import csv

#function to check to make sure user entered valid input
def checkChoice ():
    while True:
                userChoice=input("Enter choice (a-e): ")
                if userChoice == "a":
                    break
                if userChoice == "b":
                    break
                if userChoice == "c":
                    break
                if userChoice == "d":
                    break
                if userChoice == "e":
                    break
    return userChoice

def main(): 

    
    fileName ="Files\\the_story_file.txt"
    accessMode= "r"
    

    story = open(fileName,accessMode)
    storyList=list(story) 
    
    with open("Files\\the_choices_file.csv","r") as theChoices:

            #new story list, runs len of story to replace all words
            newStory= []

            print("The Itsy Bitsy Aardvark")

            choices= csv.reader(theChoices)
            lines= list(choices)        #this takes the return of the csv file and puts it into a list
                    
            #choices from the choices csv file
            choice1 = print("\nPlease choose " + lines[0][0] + 
                                    "\n a)" +lines[0][1] +
                                    "\n b)" +lines[0][2] +
                                    "\n c)" + lines[0][3] +
                                    "\n d)" + lines[0][4] +
                                    "\n e)" + lines[0][5] + ": ")
            userChoice1=checkChoice()   #this calls the while loop to check user input/collect/return input

            choice2 = print("\nPlease choose " + lines[1][0] + 
                                "\n a)" +lines[1][1] +
                                "\n b)" +lines[1][2] +
                                "\n c)" + lines[1][3] +
                                "\n d)" + lines[1][4] +
                                "\n e)" + lines[1][5] + ": ")
            userChoice2=checkChoice()

            choice3 = print("\nPlease choose " + lines[2][0] + 
                                "\n a)" +lines[2][1] +
                                "\n b)" +lines[2][2] +
                                "\n c)" + lines[2][3] +
                                "\n d)" + lines[2][4] +
                                "\n e)" + lines[2][5] + ": ")
            userChoice3=checkChoice()

            choice4 = print("\nPlease choose " + lines[3][0] + 
                                "\n a)" +lines[3][1] +
                                "\n b)" +lines[3][2] +
                                "\n c)" + lines[3][3] +
                                "\n d)" + lines[3][4] +
                                "\n e)" + lines[3][5] + ": ")
            userChoice4=checkChoice()

            choice5 = print("\nPlease choose " + lines[4][0] + 
                                "\n a)" +lines[4][1] +
                                "\n b)" +lines[4][2] +
                                "\n c)" + lines[4][3] +
                                "\n d)" + lines[4][4] +
                                "\n e)" + lines[4][5] + ": ")
            userChoice5=checkChoice()

            choice6 = print("\nPlease choose " + lines[5][0] + 
                                "\n a)" +lines[5][1] +
                                "\n b)" +lines[5][2] +
                                "\n c)" + lines[5][3] +
                                "\n d)" + lines[5][4] +
                                "\n e)" + lines[5][5] + ": ")
            userChoice6=checkChoice()

            choice7 = print("\nPlease choose " + lines[6][0] + 
                                "\n a)" +lines[6][1] +
                                "\n b)" +lines[6][2] +
                                "\n c)" + lines[6][3] +
                                "\n d)" + lines[6][4] +
                                "\n e)" + lines[6][5] + ": ")
            userChoice7=checkChoice()
         
            print("\nYour Completed Story: ")
            print()

            #the if structure for determining user choice via choices list
            #this is a long chunk of code, would have liked a better way to do this
            if userChoice1 == "a":
                userChoice1= lines[0][1]
            elif userChoice1 == "b":
                userChoice1=lines[0][2]
            elif userChoice1 == "c":
                userChoice1=lines[0][3]
            elif userChoice1 == "d":
                userChoice1=lines[0][4]
            elif userChoice1 == "e":
                userChoice1=lines[0][5]

            if userChoice2 == "a":
                userChoice2 = lines[1][1]
            elif userChoice2 == "b":
                userChoice2=lines[1][2]
            elif userChoice2 == "c":
                userChoice2=lines[1][3]
            elif userChoice2 == "d":
                userChoice2=lines[1][4]
            elif userChoice2 == "e":
                userChoice2=lines[1][5]
            
            if userChoice3 == "a":
                userChoice3 = lines[2][1]
            elif userChoice3 == "b":
                userChoice3=lines[2][2]
            elif userChoice3 == "c":
                userChoice3=lines[2][3]
            elif userChoice3 == "d":
                userChoice3=lines[2][4]
            elif userChoice3 == "e":
                userChoice3=lines[2][5]

            if userChoice4 == "a":
                userChoice4 = lines[3][1]
            elif userChoice4 == "b":
                userChoice4=lines[3][2]
            elif userChoice4 == "c":
                userChoice4=lines[3][3]
            elif userChoice4 == "d":
                userChoice4=lines[3][4]
            elif userChoice4 == "e":
                userChoice4=lines[3][5]

            if userChoice5 == "a":
                userChoice5 = lines[4][1]
            elif userChoice5 == "b":
                userChoice5=lines[4][2]
            elif userChoice5 == "c":
                userChoice5=lines[4][3]
            elif userChoice5 == "d":
                userChoice5=lines[4][4]
            elif userChoice5 == "e":
                userChoice5=lines[4][5]

            if userChoice6 == "a":
                userChoice6 = lines[5][1]
            elif userChoice6 == "b":
                userChoice6=lines[5][2]
            elif userChoice6 == "c":
                userChoice6=lines[5][3]
            elif userChoice6 == "d":
                userChoice6=lines[5][4]
            elif userChoice6 == "e":
                userChoice6=lines[5][5]

            if userChoice7 == "a":
                userChoice7 = lines[6][1]
            elif userChoice7 == "b":
                userChoice7=lines[6][2]
            elif userChoice7 == "c":
                userChoice7=lines[6][3]
            elif userChoice7 == "d":
                userChoice7=lines[6][4]
            elif userChoice7 == "e":
                userChoice7=lines[6][5]

            #looping over the storyList , making replacements, writing to newStory list
            for word in storyList:
                newString= word.replace("_1_", userChoice1.upper()).replace("_2_", userChoice2.upper())\
                           .replace("_3_", userChoice3.upper()).replace("_4_", userChoice4.upper())\
                           .replace("_5_", userChoice5.upper()).replace("_6_", userChoice6.upper())\
                           .replace("_7_", userChoice7.upper())         
                newStory.append(newString)
            
            #loops through the list, displays to screen
            for line in newStory:
                print(line, end="")           
  
            
                        

        
    story.close()
    
if __name__ == "__main__":
    main()