import pandas as pd
import random
import string
import os

# generate random names
def randon_name():
    first_name = random.choice(["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Isabella", "Jack"])
    last_name = random.choice(["Johnson", "Smith", "Brown", "Lee", "Williams", "Martin", "Martinez", "Taylor", "Adams", "Anderson"])
    return f"{first_name} {last_name}"

# generate random address
def random_address():
    street_name = random.choice(["Main St", "Elm St", "Oak St", "Pine St", "Maple St", "Birch St", "Cedar St", "Walnut St", "Spruce St", "Cherry St"])
    number = random.randint(1,300)
    return f"{number}, {street_name}"

# cities list
city_name = ["London", "Manchester", "Birmingham", "Edinburgh", "Liverpool", "Glasgow", "Leeds", "Bristol", "Newcastle", "Sheffield"]

# generate random postal code ex:SL6 8EL
def random_postal_code():
    first = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)  + random.choice(string.digits)
    last = random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    return f"{first} {last}"

# generate random phone number 4+6
def random_phone_number():
    number = ''.join(random.choices(string.digits, k=10))
    return f"{number[:4]} {number[4:]}"

# generate the dataframe
data = {
    'name': [randon_name() for _ in range(10)],
    'address': [random_address() for _ in range(10)],
    'postal_code': [random_postal_code() for _ in range(10)],
    'city': [random.choice(city_name) for _ in range(10)],
    'phone_number': [random_phone_number() for _ in range(10)]
}

df_address = pd.DataFrame(data)

# export to Excel
output_folder = 'C:/temp/export/'
output_file = 'full_address_uk.xlsx' 
output_file_path = output_folder + output_file

df_address.to_csv(output_file_path, index=False)

if os.path.exists(output_file_path):
    print(f"File '{output_file_path}' was successfully created.")
else:
    print(f"File '{output_file_path} was not created.")




# print(randon_name())
# print(random_address())
# print(random_postal_code())
# print(random.choice(city_name))
# print(random_phone_number())
# print(df_address)
