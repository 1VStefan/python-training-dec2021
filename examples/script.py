"""
This is a docstring for module `script` - containing some introductory notions
about Python
"""

print('hello world!')  # inline comment

# comment
print('A very')
print('good idea')

my_shopping_list = [
    'apples',
    'bananas',
    'oranges',
    'pears',
    'peaches',
    'cherries'
]
print(my_shopping_list)
for item in my_shopping_list:
    if item == 'pears':
        continue
    print(item)

x = (
        200 + 300 + 400 + 500 + 600 + 700 + 800 + 900 +
        1000 + 1100 + 1200 + 1300 + 1400
)

hour = 13
if hour < 18:
    greeting = "good day"
    print('hour is less than 18')
else:
    greeting = "good evening"

message = f"Current time: {hour - 3}:00. {greeting.capitalize()}!"
print(message)

multiline_str = """
Textual data in Python is handled with str objects, or strings.
Strings can be created with string literals. 
String literals are characters enclosed by single quotes, 
double quotes or triple quotes:
"""

print(multiline_str)

