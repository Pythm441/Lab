def display_info(**schools):   #The ** operator used to unpack dictionaries into arguments
    for key, value in schools.items():
        print(key, ":", value)

display_info(name = "Ahmed", grade = "Grade 12 Adv",school =  "Al Ebtikar school")