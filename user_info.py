users = ['admin','john' , 'sara' , 'milke']
user_info = {}

name = input("enter name:")
if name in users:
    age = input("enter age:")
    country = input("entr country:")
    user_info[name] ={
       "age" : age,
       "country" :country
    }
    print(user_info)
else:
    print("enter notfound!")



