import re

text = "apple,banana,orange,grape"

pattern = r","

new_text = re.split(pattern, text)

print(new_text)