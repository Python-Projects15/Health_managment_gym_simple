#health management system
#3 clients -harry , vsibhav , samarth

def getdate():
    import datetime
    return datetime.datetime.now()

# Excersixe Functions
def harry_exc():
    Excersize_name = input("Which Excersize You Complete mr harry ==>>")
    date = getdate()
    f = open("he.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()
def Vaibhav_exc():
    Excersize_name = input("Which Excersize You Complete mr Vaibhav ==>>")
    date = getdate()
    f = open("ve.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()
def samarth_exc():
    Excersize_name = input("Which Excersize You Complete mr Samrth ==>>")
    date = getdate()
    f = open("se.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()

def harry_exc_show():
    f = open("he.txt")
    content = f.read()
    print(content)

    f.close()

def Vaibhav_exc_show():
    f = open("ve.txt")
    content = f.read()
    print(content)

    f.close()

def samarth_exc_show():
    f = open("se.txt")
    content = f.read()
    print(content)

    f.close()



#FoodFunctions


def harry_food():
    Excersize_name = input("Which Food You ate Mr Harry ==>>")
    date = getdate()
    f = open("hf.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()
def Vaibhav_food():
    Excersize_name = input("Which Food You ate mr Vaibhav ==>>")
    date = getdate()
    f = open("vf.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()
def samarth_food():
    Excersize_name = input("Which Food You ate mr Samrth ==>>")
    date = getdate()
    f = open("sf.txt", "a")
    f.write("\n")
    f.write(str(date) + Excersize_name)
    f.close()

def harry_food_show():
    f = open("hf.txt")
    content = f.read()
    print(content)

    f.close()

def Vaibhav_food_show():
    f = open("vf.txt")
    content = f.read()
    print(content)

    f.close()

def samarth_food_show():
    f = open("sf.txt")
    content = f.read()
    print(content)

    f.close()



work=1
while (work <= 9):
 print("What do You Want To Chnage Or Show  ")
 print("press 1 for Excersize ")
 print("press 2 for Food ")
 print("press 3 for EXIT")
 user_input1 = int(input("==>>>"))

#Excersize Data

 if(user_input1 == 1):
           print("Whos excersixe You want to retrive\n")
           print("1-retrive or 11-Show For Harry ")
           print("2-retrive or 22-Show for Vaibhav")
           print("3-retrive or 33-Show for Samrth")

           user_name = int(input("==>>>"))
           if(user_name == 1):
               harry_exc()
               print("well Done Keep up\n")
           if (user_name == 2):
               Vaibhav_exc()
               print("well Done Keep up\n")
           if (user_name == 3):
               samarth_exc()
               print("well Done Keep up\n")
           if (user_name == 11):
               harry_exc_show()
               print("well Done Keep up\n")
           if (user_name == 22):
               Vaibhav_exc_show()
               print("well Done Keep up\n")
           if (user_name == 33):
               samarth_exc_show()
               print("well Done Keep up\n")


# food data

 if(user_input1 == 2):
         print("Whos Food You want to retrive or Show\n")
         print("1-retrive or 11-Show For Harry ")
         print("2-retrive or 22-Show for Vaibhav")
         print("3-retrive or 33-Show for Samrth")

         user_name = int(input("==>>>"))
         if (user_name == 1):
             harry_food()
             print("follow the food chart giver by Gym\n")
         if (user_name == 2):
             Vaibhav_food()
             print("follow the food chart giver by Gym\n")
         if (user_name == 3):
             samarth_food()
             print("follow the food chart giver by Gym\n")
         if (user_name == 1):
             harry_food_show()
             print("follow the food chart giver by Gym\n")
         if (user_name == 2):
             Vaibhav_food_show()
             print("follow the food chart giver by Gym\n")
         if (user_name == 3):
             samarth_exc_show()
             print("follow the food chart giver by Gym\n")







 if(user_input1 != 1 and user_input1 != 2 and user_input1 != 3):
    print("You Enter Wrong one")

 if(user_input1 == 3):
     exit()