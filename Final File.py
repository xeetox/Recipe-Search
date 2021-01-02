import requests

# RECIPE SEARCH CODE
def recipe_search(ingredient):  # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '9bc8ac06'
    app_key = '5c66158bf122be9926fdbd3afd09590b'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

# PROGRAM CODE
def program():
    # INGREDIENT FILTER
    ingredient = input('What ingredient do you want to use in your cooking today? ')
    print()

    # EMPTY STRINGS
    dietary_requirements = ''
    enter_dietary_requirments = ''

    # SPELLING ERROR (YES/NO) - INFINITE LOOP UNTIL TRUE
    while not (dietary_requirements == 'yes' or dietary_requirements == 'no'):
        dietary_requirements = input(
            'List of dietary requirements we can filter results for: Vegetarian, Vegan, Nut-free or Halal \nDo you '
            'have a dietary requirement? (yes/no): ')

    # DIETARY FILTER
    if dietary_requirements == 'yes':

        # SPELLING ERROR (DIETARY FILTER) - INFINITE LOOP UNTIL TRUE
        while not (
                enter_dietary_requirments == 'vegetarian' or enter_dietary_requirments == 'veggie' or
                enter_dietary_requirments == 'Vegetarian' or enter_dietary_requirments == 'Veggie' or
                enter_dietary_requirments == 'vegan' or enter_dietary_requirments == 'Vegan' or
                enter_dietary_requirments == 'halal' or enter_dietary_requirments == 'Halal' or
                enter_dietary_requirments == 'nut free' or enter_dietary_requirments == 'Nut free' or
                enter_dietary_requirments == 'nut-free' or enter_dietary_requirments == 'Nut-free'):
            print(
                'List of dietary requirements we can filter results for: Vegetarian, Vegan, Nut-free or Halal')
            enter_dietary_requirments = input('Enter your dietary requirement: ')

        # VEGETARIAN FILTER
        if enter_dietary_requirments == 'vegetarian' or 'veggie':
            results = recipe_search(ingredient)
            print()
            for result in results:
                recipe = result['recipe']
                if 'Vegetarian' in recipe['healthLabels']:
                    print(recipe['label'])
                    print('Photo: ' + recipe['image'])
                    print('Recipe: ' + recipe['url'])
                    print()

        # VEGAN FILTER
        elif enter_dietary_requirments == 'vegan':
            results = recipe_search(ingredient)
            print()
            for result in results:
                recipe = result['recipe']
                if 'Vegan' in recipe['healthLabels']:
                    print(recipe['label'])
                    print('Photo: ' + recipe['image'])
                    print('Recipe: ' + recipe['url'])
                    print()

        # NUT-FREE FILTER
        elif enter_dietary_requirments == 'nut-free' or 'nut free':
            results = recipe_search(ingredient)
            print()
            for result in results:
                recipe = result['recipe']
                if 'Peanut-Free' and 'Tree-Nut-Free' in recipe['healthLabels']:
                    print(recipe['label'])
                    print('Photo: ' + recipe['image'])
                    print('Recipe: ' + recipe['url'])
                    print()

        # HALAL FILTER
        elif enter_dietary_requirments == 'halal':
            results = recipe_search(ingredient)
            print()
            for result in results:
                recipe = result['recipe']
                if 'Alcohol-Free' in recipe['healthLabels'] and 'pork' not in recipe['ingredients']:
                    print(recipe['label'])
                    print('Photo: ' + recipe['image'])
                    print('Recipe: ' + recipe['url'])
                    print()

    # DIETARY FILTER NOT REQUIRED
    elif dietary_requirements == 'no':
        results = recipe_search(ingredient)
        print()
        for result in results:
            recipe = result['recipe']
            print(recipe['label'])
            print('Photo: ' + recipe['image'])
            print('Recipe: ' + recipe['url'])
            print()

program()