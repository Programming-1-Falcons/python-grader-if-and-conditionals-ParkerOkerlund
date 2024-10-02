possible_points = int(input("Total points possible: "))
points_achieved = int(input("How many points did they get?: "))
percent = points_achieved /possible_points  * 100



if percent <= 50:
    print("F")
elif percent <= 60 and percent > 50:
    print("D")
elif percent <= 75 and percent > 60:
    print("C")
elif percent <= 88 and percent > 75:
    print("B")
elif percent >= 100 and percent > 89:
    print("A")