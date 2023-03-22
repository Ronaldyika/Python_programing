#provide different info about an employee {employee name with first letters in caps}
#{hourly wage,hours of work per weak}
Employee_Name = input("what is your name: ");

hourly_wage = float(input("enter your hourly wage: "));

work_hours_perweak = float(input("how many hours do you work per weak?: "));

Total_Earnings = (hourly_wage * work_hours_perweak);

print(f'{Employee_Name.title()} earns {Total_Earnings}$ each week ');
