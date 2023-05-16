# Define three dictionaries containing name and phone_number information
dict1 = {'name': 'Maha', 'phone_number': '0553002204'}
dict2 = {'name': 'Ibraheem', 'phone_number': '0505136375'}
dict3 = {'name': 'Yara', 'phone_number': '0504285001'}

# Make a list of dictionaries
dict_list = [dict1, dict2, dict3]

# Add one more dictionary to the list
dict4 = {'name': 'Suliman', 'phone_number': '0554499281'}
dict_list.append(dict4)

# Delete the name key from the first dictionary
del dict_list[0]['name']

# Update the phone number of the last person in the list
dict_list[-1]['phone_number'] = '0556786543'

# Check if the first dictionary has a key called "name"
if 'name' in dict_list[0]:
    print("The first dictionary has a key called 'name'")
else:
    print("The first dictionary does not have a key called 'name'")
