import requests
import json


def validator():  
            while True:
                try:
                    user_id = int(input("Please enter the user ID: "))
                    break
                except ValueError:
                    print("Invalid User ID")
                    continue
            url = "https://jsonplaceholder.typicode.com/users/"
            r = requests.get(url+str(user_id))

            if r.status_code == 200:
                data = r.json()
                return data
            else:
                validator()
            
            


result = validator()   # Mistake> I creates the Validator function but didn't store it as result!!!!!



info = {
      "name" : result["name"],
      "City" : result["address"]["city"],
      "Company name" : result["company"]['name'],
      "Email" : result["email"]

}


  
with open("Info.json", "w") as f:
    data = json.dump(info,f, indent = 4)


        






