# Volume of a sphere with radius r Formula
pi = 3.14
r = float(input("Enter Radius: "))

volume = (4/3) * pi * (r ** 3)
print("The volume of the sphere is:", volume)

#Total Wholesale cost for 60 copies
Cover_Price = 24.95
discount = .4
shipping_costs_1st_copy = 3
shipping_costs_extra_copies = .75
Number_books_bought = float(input("number of books being bought: "))

Wholesale_cost = (Number_books_bought * (1 - discount)) + (shipping_costs_1st_copy + (shipping_costs_extra_copies * (Number_books_bought - 1)))
print(Wholesale_cost)

# Time calculations for running
start_time_hr = 6
start_time_min = 52
easy_pace_min = 8
easy_pace_sec = 15
tempo_pace_min = 7
tempo_pace_sec = 12
total_min = 2 * (easy_pace_min + easy_pace_sec / 60) + 3 * (tempo_pace_min + tempo_pace_sec / 60)

end_time_hr = start_time_hr + int((start_time_min + total_min) / 60)
end_time_min = (start_time_min + total_min) % 60

print(f"Return time for breakfast: {end_time_hr}:{int(end_time_min)}")

#calculate percentage increase in average grade
old_average = 82
new_average = 89

increase = ((new_average - old_average) / old_average) * 100
print(f"Percentage increase: {increase:.1f}%")
