from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
 
class Recipe:
    db_name='recipesss'
    def __init__(self,data):
        self.id = data['id'],
        self.name = data['name'],
        self.description = data['description'],
        self.instruction = data['instruction'],
        self.dateMade = data['dateMade'],
        self.under30 = data['under30'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def getAllRecipes(cls):
        query= 'SELECT * FROM recipes;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        if results:
            for row in results:
                recipes.append(row)
            return recipes
        return recipes

    @classmethod
    def get_recipe_by_id(cls, data):
        query= 'SELECT * FROM recipes WHERE recipes.id = %(recipe_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(recipe_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_recipe(cls,data):
        query = 'UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, dateMade=%(dateMade)s, under30=%(under30)s, user_id=%(user_id)s WHERE recipes.id=%(recipe_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    #Class Method to create a user
    @classmethod
    def create_recipe(cls,data):
        query = 'INSERT INTO recipes (name, description, instruction, dateMade, under30, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(dateMade)s, %(under30)s, %(user_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 2:
            flash("Name must be at least 3 characters.", 'name')
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Recipe description be at least 3 characters.", 'description')
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("Recipe instruction must be at least 3 characters.", 'instruction')
            is_valid = False
        if recipe['dateMade'] == '':
            flash("Date made is required", 'dateMade')
            is_valid = False
        if 'under30' not in recipe:
            flash("Please check", 'under30')
            is_valid = False
        return is_valid