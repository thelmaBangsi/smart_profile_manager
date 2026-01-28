def get_user_profile():
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    height = float(input("Enter your height in cm:"))
    country = input("Enter your country:")
    favorite_color = input("Enter your favorite color:")

    return name, age, height, country, favorite_color 



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


#main program
name, age, height, country, favorite_color = get_user_profile()

print("\n---PROFILE SUMMARY---") 
print(full_profile(name, age, height, country, favorite_color))   
