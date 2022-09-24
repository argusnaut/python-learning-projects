import itertools
import json


class Question:
    new_id = itertools.count()

    def __init__(self, question, answer):
        self.id = next(Question.new_id)
        self.question = question
        self.answer = answer


def show_questions():
    score = 0

    question_array = read_json()

    for q in question_array:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    percentage = (score / len(question_array)) * 100

    return [score, percentage]


def read_json(add_question=False):
    with open("data/questions.json") as file:
        data = json.load(file)
        if not data and not add_question:
            print("No question was found. :(")
            quit()

        elif not data and add_question:
            return []

        else:
            return data["questions"]


def write_json(array):
    json_array = []
    for q in array:
        json_array.append(q.__dict__)

    out = {"questions": json_array}

    with open("data/questions.json", "w") as file:
        json.dump(out, file, indent=4)


def main():
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? ")

    if any(playing.lower() == a for a in ["yes", "y"]):
        print("Ok! Let's play :) ")

        score_data = show_questions()

        print("You got " + str(score_data[0]) + " questions correct!")
        print("You got " + str(score_data[1]) + "%")
    elif any(playing.lower() == a for a in ["a", "add", "n", "new"]):
        while True:
            while True:
                input_question = input("Please write the new question:\n").capitalize()
                if input_question == "":
                    print("Question cannot be empty:\n")
                    continue
                else:
                    break

            while True:
                input_answer = input("Please enter the answer:\n").lower()
                if input_answer == "":
                    print("An answer cannot be empty:\n")
                    continue
                else:
                    break

            questions = read_json(True)
            new_question = Question(str(input_question), str(input_answer))
            questions.append(new_question)

            write_json(questions)

            repeat = input("Do you want to add another question: ")
            if any(repeat.lower() == a for a in ["yes", "y"]):
                continue
            else:
                quit()
    else:
        quit()


if __name__ == "__main__":
    main()
