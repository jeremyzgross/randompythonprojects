# List of bad chars that we want to get rid of. 
# NOTE: During testing there was a weird quote and double quote ("')
bad_chars = r"~`!@#$%^&*()-{}[]|\\/:;\"'"'+=<>,.?"

# Take data from input column name and remove the bad characters
clean_name = input_data['name'].translate(str.maketrans('', '', bad_chars))

output = [{"name": clean_name}]
