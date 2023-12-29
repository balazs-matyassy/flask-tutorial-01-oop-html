from flask import Flask, render_template

app = Flask(__name__)


class Recipe:
    def __init__(self, category='', name='', difficulty=1, recipe_id=None):
        self.recipe_id = recipe_id
        self.category = category
        self.name = name
        self.difficulty = difficulty

    @property
    def difficulty_description(self):
        if self.difficulty == 1:
            return 'Very easy'
        elif self.difficulty == 2:
            return 'Easy'
        elif self.difficulty == 3:
            return 'Medium'
        elif self.difficulty == 4:
            return 'Difficult'
        elif self.difficulty == 5:
            return 'Very difficult'

        return 'Unknown'

    @staticmethod
    def create_from_line(line):
        values = line.strip().split('\t')

        return Recipe(
            recipe_id=int(values[0].strip()),
            category=values[1].strip(),
            name=values[2].strip(),
            difficulty=int(values[3].strip())
        )


def find_all():
    with open('recipes.txt', encoding='utf-8') as file:
        recipes = []

        file.readline()  # header

        for line in file:
            recipe = Recipe.create_from_line(line)
            recipes.append(recipe)

        return recipes


@app.route('/')
def list_all():
    return render_template('list.html', recipes=find_all())


if __name__ == '__main__':
    app.run()
