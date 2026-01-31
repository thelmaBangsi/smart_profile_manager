def get_user_profile():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    height = float(input("Enter your height in cm:"))
    country = input("Enter your country:")
    favorite_color = input("Enter your favorite color:")

    return name, age, height, country, favorite_color 
#key idea: variables inside the funtion don't exist outside the function unless returned 


def full_profile(name, age, height, country, favorite_color):
    if age >= 18: 
        category = "Adult"
    else:
        category = "Minor"

    profile_summary = ( 
        f"Your name is {name} and you are {age} years old ({category}).\n "
        f"You have a height of {height} cm and you are from {country}. \n"
        f"Your favorite color is {favorite_color}. \n"
        f"Thank you for sharing your information!"
        )

    return profile_summary

def save_profile(profile_text): #this line is to create a reusable tool called save_profile that receives some text.
    with open("profile.txt", "a") as file: #this create file if it doesnt exist
        #with open safely opens and automatically closes the file 
        #"a" append mode (add, doesn't delete old data)
        #'with' means open safely then close instead of file = open(), file.write(), file.close()
        file.write(profile_text + "\n\n")
        #.writes text into file 
        #"file" opens the file 
        #'write' puts text inside the file 
        #'\n\n' adds empty lines between profiles 




#main program
name, age, height, country, favorite_color = get_user_profile()

print("\n---PROFILE SUMMARY---") 

summary = full_profile(name, age, height, country, favorite_color)

print (summary)
save_profile(summary)

all_profiles = [] # empty list to store every profile summary

#using a while loop so that users can enter as many options as they want 

while True: #notice that the 'T' in True is 'majiscules'

    print("\n Enter new proiles (or type 'q' to quit):")
    name = input("Enter your name: ")
    if name.lower() == 'q': # .lower() turns any string into lowercase letters so you 
                            #can type either 'Q' or 'q' to quit it works both ways 
                            #and it will work the same for Uppper too mostlikely .upper!
        break #break stops the current loop immediately, without it, 'while True' will run for ever 

    age = int(input("Enter your age:"))
    height = float(input("Enter your height in cm: "))
    country = input("Enter your country: ")
    favorite_color = input("Enter your favorite color: ") 
    #we rewriting all this input again because  each iteratian of the loop is for one new user 
    #variables inside the loop get overwritten with each new user. you can't jus reuse old values 
    #because we want fresh input every time.

    #create the profile summary
    profile = full_profile(name, age, height, country, favorite_color)

    #store it in the list
    all_profiles.append(profile)

    save_profile(profile) #i added this line because without it, only the first profile is saved and the 
    #other profiles are only added in the list but now all the profiles are saved in the file.

    print("\nProfile saved!")

    print("\n---ALL PROFILES ---")
    for p in all_profiles:
        print("\n" + p)




