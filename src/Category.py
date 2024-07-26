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

def add_category(name, goal):

    # Create cateogry
    category = Category(global_vars.year, global_vars.month, name, goal, 0)

    # Add category to list
    global_vars.categories.append(category)
