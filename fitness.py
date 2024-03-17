# from IPython.display import clear_output

def bmi(height, weight):
    bmi_calc = weight / (height * height)
    return round(bmi_calc,2)

def bmi_rating(bmi):
    if bmi < 18.9:
        return "Underweight"
    elif bmi >= 18.9 and bmi <= 24.9:
        return "Healthy"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

#how many calories burnt per day
def bmr(height, weight, age, sex):
    if sex[0].lower() == 'm':
        bmr_calc = (10 * weight) + (6.25 * height * 100) - (5 * age) +5
    else:
        bmr_calc = (10 * weight) + (6.25 * height * 100) - (5 * age) - 161

    return round(bmr_calc,0)

# how many calories needed for these tasks
def calories_burn(bmr):
    sedentary = round(bmr * 1.2, 0)
    light = round(bmr * 1.375, 0)
    moderate = round(bmr * 1.55, 0)
    very_active = round(bmr * 1.725, 0)
    extra_active = round(bmr * 1.9, 0) 
    
    calories_burn ={1: sedentary, 2: light, 3: moderate, 4: very_active, 5: extra_active}

    print("To maintain your weight, follow these daily calorie guidances:")
    print("1. Little to no exercise:                 You need = {} k/cals".format(sedentary))
    print("2. Light exercise (1-3 days per week):    You need = {} k/cals".format(light))
    print("3. Moderate exercise (3-5 days per week): You need = {} k/cals".format(moderate))
    print("4. Heavy exercise (6-7 days per week):    You need = {} k/cals".format(very_active))
    print("5. Very heavy exercise (twice per day):   You need = {} k/cals".format(extra_active)) 

    return calories_burn

#To acheive the goal in a specified time, how many calories should be burnt per day  
def target_weight():
    delta_weight = weight_goal - weight

    if delta_weight < 0:
        deficit_surplus = 'deficit'
    else:
        deficit_surplus = 'surpuls'   

    delta_pounds =  abs(delta_weight * 2.2)
    delta_calories =  delta_pounds * 3500
    pounds_per_day = delta_pounds / (weeks * 7)

    if deficit_surplus == 'deficit':
        calories_per_day = round((delta_calories / (weeks * 7)) -1,0)
    else:
        calories_per_day = round((delta_calories / (weeks * 7)),0)
       
    return {'delta_weight': delta_weight, 'deficit_surplus': deficit_surplus, 'delta_pounds': delta_pounds, 'delta_calories': delta_calories, 'pounds_per_day': pounds_per_day, 'calories_per_day': calories_per_day}


def use_again():
    replay = input("Would you like it use this again? (Yes/No): ") 
    if replay.lower() == 'y':
        return True
    else:
        return False     

while True:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    sex = input("What is your sex? (Male or female) ")
    height = float(input("What is your height in meters? "))
    weight = float(input("What is your weight in kg? "))

    bmi_result = bmi(height, weight)
    bmr_result = bmr(height, weight, age, sex)
    
    print('''Hello {}!) Here is your fitness report: 
    You are a {} year old {}. You are {}m tall and weigh {}kg. Here are your body statistics:'''.format(name,age,sex,height,weight))

    print("------------------------")
    print("Your BMI is {}".format(bmi_result))
    print("")
    print("Based on your BMI, you are classified as {}".format(bmi_rating(bmi_result)))
    print("------------------------")
    print("Your BMR is {}".format(bmr_result))
    print("")
    calorie_consumption = calories_burn(bmr_result)
    print("")   
    activity_level = int(input("Which activity level are you? (1-5) "))
    print("------------------------")
    weight_goal = int(input("What is your weight goal (kg)? "))
    weeks = int(input("In how many weeks would you like to achieve this goal? "))
    calorie_info = target_weight()
    print("------------------------")
    print('''To achieve a target weight of {} kg in {} weeks, you will need to consume a {} of 
    {} calories. This means your daily calorie intake should be {} calories! Good luck in achieving your weight goal!'''.format(weight_goal,weeks,calorie_info['deficit_surplus'], abs(calorie_info['calories_per_day']), calorie_consumption[activity_level] + calorie_info['calories_per_day']))
    print("------------------------")

    if not use_again():
        break

           