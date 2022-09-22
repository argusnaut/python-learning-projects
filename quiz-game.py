import json


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def show_questions():
    score = 0

    question_array = read_json()

    for q in question_array:
        answer = input(q.question)
        if answer.lower() == q.answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    percentage = (score / len(question_array)) * 100

    return [score, percentage]


def read_json():
    with open("data/questions.json") as file:
        return json.loads(file.read(), object_hook=lambda d: Question(**d))


def main():
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ")

    if any(playing.lower() == a for a in ["yes", "y"]):
        print("Ok! Let's play :) ")

        score_data = show_questions()

        print("You got " + str(score_data[0]) + " questions correct!")
        print("You got " + str(score_data[1]) + "%")

    else:
        quit()


if __name__ == "__main__":
    main()
