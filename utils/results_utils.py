import constants as c

from app import Formdata
from app import db


def fetch_data(*columns):
    return db.session.query(*columns).all()


def prepare_personal_data():
    # store the available options representations
    age_options = c.age_options
    home_options = c.home_options
    gender_options = c.gender_options
    education_options = c.education_options
    # query the personal data
    personal_data = fetch_data(Formdata.age, Formdata.home, Formdata.gender, Formdata.education)
    # create data for rendering
    ages = [[age_options[opt], len([x[0] for x in personal_data if x[0] == opt])] for opt in age_options.keys()]
    homes = [[home_options[opt], len([x[1] for x in personal_data if x[1] == opt])] for opt in home_options.keys()]
    genders = [[gender_options[opt], len([x[2] for x in personal_data if x[2] == opt])]
               for opt in gender_options.keys()]
    educations = [[education_options[opt], len([x[3] for x in personal_data if x[3] == opt])]
                  for opt in education_options.keys()]

    return ages, homes, genders, educations


def calculate_sentiment():
    answers = fetch_data(Formdata.corona, Formdata.easter, Formdata.feeling, Formdata.alcohol, Formdata.eat,
                         Formdata.selfimpr, Formdata.job)
    sentiments = map(map_answer_to_sentiment, answers)
    return list(sentiments)


def prepare_government_status():
    answers = fetch_data(Formdata.status)
    scores = [answer[0] for answer in answers]
    return scores


def prepare_age_comparison():
    view_options = c.view_options
    badfeeling_options = c.badfeeling_options

    ages_view = link_age_with_answer(Formdata.view, view_options)
    ages_badfeeling = link_age_with_answer(Formdata.badfeeling, badfeeling_options)
    return ages_view, ages_badfeeling


def link_age_with_answer(answer, options):
    age_options = c.age_options
    answers = fetch_data(Formdata.age, answer)

    # group the answers by age
    age_1 = [x[1] for x in answers if x[0] == 1]
    age_2 = [x[1] for x in answers if x[0] == 2]
    age_3 = [x[1] for x in answers if x[0] == 3]
    age_4 = [x[1] for x in answers if x[0] == 4]

    ages_answer = [[age_options[1], *[len([1 for x in age_1 if x==opt]) for opt in range(1, len(options)+1)]],
                   [age_options[2], *[len([1 for x in age_2 if x==opt]) for opt in range(1, len(options)+1)]],
                   [age_options[3], *[len([1 for x in age_3 if x==opt]) for opt in range(1, len(options)+1)]],
                   [age_options[4], *[len([1 for x in age_4 if x==opt]) for opt in range(1, len(options)+1)]]]

    return ages_answer


def map_answer_to_sentiment(answers):
    # mark responses to chosen questions as positive, negative and neutral in the same order as they are fetched
    sentiments_dict = c.sentiments_dict

    positive_cnt = 0
    for i, answer in enumerate(answers):
        if answer in sentiments_dict[i]["Positive"]:
            positive_cnt +=1
        elif answer in sentiments_dict[i]["Negative"]:
            positive_cnt -=1
    return positive_cnt


