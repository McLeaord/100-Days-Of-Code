
x = { 'csk': ["Dhoni , Raina , Jadeja , Utappa , Ruthuraj , Bravo , Imran , Faf , Sam , Vijay , Albe"],
"rcb":["Virat , Abd , Chahal , Devdutt , Maxwell , Kyle , Allen , Daniel , Sundar , Harshal , Adam"],
"mi":["Rohit , Hardik , Krunal , Pollard , Surya , Jasprit , Kulkarni , Ishan , Quinton , Rahul , James"],
"kkr":["Gill , Morgon , Rusell , Dinesh , Cummins , Varun , Shakib , Narine , Sunil , Nitish , Harbajan"],
"srh":["Warner , Jhonny , Kane , Rashid , Manish , Kumar , Roy , Abdul , Natarajan , Vijay , Saha"],
"kxip":["Rahul , Mayank , Gayle , Karun , Sharukh , Malan , Miller , Deepak , Harpreet , Pooran , Shami"],
"dc":["Pant , Iyer , Shikhar , Smith , Shaw , Ashwin , Rahane , Mishra , Heytmar , Avesh , Cris"],
"rr":["Sanju , Buttler , Stokes , Jofra , Rahman , Sakariya , Riyan , Morris , Dube , Tyagi , Gopal"]}
print("     ******* I P L *******    ")
print()
key = input("Enter Name Of The Team   :   ")
print()
print("Players Are    :   ")
print()
if key in x:
    print(','.join(x[key]))

print()
print("   ***** End Of Information *****   ")
print()
