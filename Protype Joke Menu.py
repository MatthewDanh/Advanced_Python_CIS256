

def get_joke(type, topic):
    jokes = {
        'knock-knock': {
            'animal': 'Knock knock. Who’s there? Lettuce. Lettuce who? Lettuce in, it’s freezing out here!',
            'food': 'Knock knock. Who’s there? Olive. Olive who? Olive you and I miss you!'
        },
        'dad': {
            'animal': 'Why don/’t some animals play cards? Because they/’re afraid of cheetahs.',
            'food': 'Why did the tomato turn red? Because it saw the salad dressing!'
        },
        'pun': {
            'animal': 'What do you call a fish without eyes? Fsh.',
            'food': 'I used to be a baker, but I couldn/’t make enough dough.'
        },
        'quote': {
            'animal': 'I/’m suspicious of people who don’t like dogs, but I trust a dog when it doesn’t like a person.',
            'food': 'Life is uncertain. Eat dessert first.'
        }
    }

    return jokes[type][topic]

def main():
    joke_types = ['knock-knock', 'dad', 'pun', 'quote']
    joke_topics = ['animal', 'food']

    while True:
        print("Choose a type of joke: knock-knock, dad, pun, quote")
        joke_type = input().lower()
        if joke_type in joke_types:
            break
        print("Invalid choice. Please try again.")

    while True:
        print("Choose a topic: animal, food")
        joke_topic = input().lower()
        if joke_topic in joke_topics:
            break
        print("Invalid choice. Please try again.")

    joke = get_joke(joke_type, joke_topic)
    print("Here's your joke: " + joke)

main()

import sqlite3

conn = sqlite3.connect('jokes.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE jokes (
        id INTEGER PRIMARY KEY,
        type TEXT,
        topic TEXT,
        joke TEXT
    )
''')

conn.commit()
conn.close()



db = SQLAlchemy()

class User(UserMixin, db.Model):
    '''This class creates a user table in the database. It inherits from UserMixin and db.Model.'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))