import codecademylib
import pandas as pd

# Read CSV file
orders = pd.read_csv('shoefly.csv')

# Print top 5
print orders.head(5)

# Extract "email" column of DataFrame
emails = orders.email

print emails

# Extract orders from "Frances Palmer"
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

print frances_palmer

# Extract orders have a shoe_type value set to "clogs", "boots" or "flats"
comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]

print comfy_shoes

# Add a column named "shoe_source" describing if material is from an animal.
orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

# Add a column named "salutation" composing a welcome message according to user's gender.
orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)

print orders.head(5)
