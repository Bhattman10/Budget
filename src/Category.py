# Category.py

# Import global_vars.py
import global_vars

class Category:
    def __init__(self, year, month, name, goal, value):
        self.year = year
        self.month = month
        self.name = name
        self.goal = goal
        self.value = value

def add_category(year, month, name, goal, value):

    # Create cateogry
    category = Category(year, month, name, goal, value)

    # Add category to list
    global_vars.categories.append(category)

def edit_category(pos_to_edit, name, goal):
    
    #take category at position and edit attributes
    global_vars.categories[int(pos_to_edit)].name = name
    global_vars.categories[int(pos_to_edit)].goal = goal

def delete_category(pos_to_delete):
    global_vars.categories.pop(int(pos_to_delete))

def category_write_to_file():
    
    #open file for writing
    f = open("Categories", "w")

    #write the number of elements in categories
    f.write(str(len(global_vars.categories)))
    f.write("|")

    #iterate through cateogories, adding each element seperated by a "|"
    for category in global_vars.categories:
        f.write(category.year)
        f.write("|")
        f.write(category.month)
        f.write("|")
        f.write(category.name)
        f.write("|")
        f.write(category.goal)
        f.write("|")
        f.write(str(category.value))
        f.write("|")

    #close file
    f.close()

def category_read_from_file():

    #open file for reading
    f = open("Categories", "r")

    #read entire text file into string txt variable
    txt = f.read()

    #close file
    f.close()

    #read num categories from first element of txt
    char_pos_1 = txt.index("|")
    number_of_categories = txt[0:char_pos_1]

    #create categories based on the number of elements listed at the beginning of file
    for x in range(int(number_of_categories)):

        #collect year of category
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        year = txt[char_pos_1+1:char_pos_2]

        #collect month of cateogry
        char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
        month = txt[char_pos_2+1:char_pos_1]

        #collect day of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        name = txt[char_pos_1+1:char_pos_2]

        #collect type of transaction
        char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
        goal = txt[char_pos_2+1:char_pos_1]

        #collect amount of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        value = txt[char_pos_1+1:char_pos_2]

        #set char_pos_1 with value of ending indent, for reseting the loop
        char_pos_1 = char_pos_2

        #create the category
        add_category(year, month, name, goal, value)

def add_Category_values(name, amount, type):
    #first, find instance of category
    for category in global_vars.categories:
        if category.name == name:
            if type == 0:
                category.value = float(category.value) - float(amount)
            else:
                category.value = float(category.value) + float(amount)

def remove_Category_values(name, amount, type):
    #first, find instance of category
    for category in global_vars.categories:
        if category.name == name:
            if type == 0:
                category.value = float(category.value) + float(amount)
            else:
                category.value = float(category.value) - float(amount)