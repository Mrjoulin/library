from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from src.db.db import *

app = Flask(__name__)

OGEDirections = {
    "Devotion": "Преданность",
    "Humanity": "Человечность",
    "Love": "Любовь",
    "RealArt": "Настоящее искусство",
    "Compassion": "Сострадание",
    "Kindness": "Доброта",
    "SelfEducation": "Самовоспитание",
    "Feat": "Подвиг",
    "Conscience": "Совесть"
}

EGEDirections = {
    "HumanAndNature": "Человек и природа",
    "FamilyProblems": "Проблемы семьи",
    "ProblemsAssociatedWithNegativePersonalityTraits": "Проблемы, связанные с отрицательными качествами личности",
    "ProblemsAssociatedWithPositiveMoralQualitiesOfAPerson":
        "Проблемы, связанные с положительными нравственными качествами личности",
    "ProblemsRelatedToTheRoleOfArtAndLiteratureInHumanLife":
        "Проблемы, связанные с ролью искусства и литературы в жизни человека",
    "HumanAndSociety": "Человек и общество",
    "MilitaryIssues": "Военная проблематика",
    "SocialResponsibilityOfScientistsForTheirInventions": "Социальной ответственности ученых за их изобретения",
    "TheProblemOfLoneliness": "Проблема одиночества",
    "ManAndStatePower": "Человек и государственная власть (политическая)"
}

EssayDirections = {
    "GoodAndEvil": "Добро и зло",
    "HopeAndDespair": "Надежда и отчаяние",
    "PrideAndHumility": "Гордость и смирение",
    "FathersAndSons": "Отцы и дети",
    "WarAndPeace": "Война и мир"
}

Section = {
    "BiographiesOfRussianCelebrities": "Биографии российских знаменитостей",
    "MilitaryLiterature": "Военная литература",
    "Housekeeping": "Домоводство",
    "AdditionalTutorial": "Дополнительное учебное пособие",
    "ForeignLiterature": "Зарубежная литература",
    "HistoricalProse": "Историческая проза",
    "HistoricalNovels": "Исторические романы",
    "HistoryAndTheoryOfLiterature": "История и теория литературы",
    "HistoryArcheologyEthnography": "История. Археология. Этнография",
    "ClassicalAndContemporaryProse": "Классическая и современная проза",
    "LiteratureForChildren": "Литература для детей",
    "LiteratureForSchoolchildren": "Литература для школьников",
    "LiteraryCriticism": "Литературная критика",
    "StoriesAndStoriesAboutAnimals": "Повести и рассказы о животных",
    "CognitiveLiterature": "Познавательная литература",
    "Poetry": "Поэзия",
    "AdventureNovels": "Приключенческие романы",
    "Publicism": "Публицистика",
    "TravelsHobbyPhotoSport": "Путешествия. Хобби. Фото. Спорт",
    "ShortStories": "Рассказы",
    "Transport": "Транспорт",
    "FantasticFantasyMystic":  "Фантастика. Фэнтези. Мистика"
}


@app.route("/")
def main():
    return render_template("index.html", OGEDirections=OGEDirections, EssayDirections=EssayDirections,
                           EGEDirections=EGEDirections, Section=Section)


@app.route("/book/<direction>")
def book(direction):
    if direction in Section.keys():
        books = get_book_on_direction('Section', Section[direction])
        return render_template('book.html', books=books)
    elif direction in OGEDirections.keys():
        books = get_book_on_direction('OGEDirection', OGEDirections[direction])
    elif direction in EGEDirections.keys():
        books = get_book_on_direction('EGEDirection', EGEDirections[direction])
    elif direction in EssayDirections.keys():
        books = get_book_on_direction('EssayDirection', EssayDirections[direction])
    else:
        return "URL NOT FOUND"
    return render_template('book.html', books=books)


@app.route('/all')
def all_books():
    books = get_all_books()
    return render_template('book.html', books=books)


@app.route('/create_database')
def create_database():
    create()
    return "Database create"


@app.route('/update_database')
def update_database():
    update_from_excel()
    return "Database updated"


@app.route('/drop_table')
def drop():
    drop_table('library')
    return "Table library is removed"


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
