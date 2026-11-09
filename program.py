import random

# Brennan Bates & CJ Harrison
# 11/9/2026
# We used ChatGPT for coding - we gave it a general idea of NFL Trivia.
# It gaves us multiple versions to decide what we liked and what we didn't like.
# We took the sample code and ran it and told AI what we liked and what we did not like.
# ChatGPT continued to make changes as we asked it to until we got to the final product.
# This prograam is NFL Trivia. There are multiple levels: Easy, Medium and Hard.
# Once you finish one round it gives you a score and asks if you would like to play again.
# After choosing to be done, the program outputs an overall score and thanks the user for playing.

easy_questions = [
    ["How many points is a touchdown worth?",
     "3", "6", "7", "8", "B"],

    ["How many players from each team are on the field?",
     "9", "10", "11", "12", "C"],

    ["What does NFL stand for?",
     "National Football League", "National Football Line",
     "North Football League", "National Federation League", "A"],

    ["How many points is a field goal worth?",
     "1", "2", "3", "6", "C"],

    ["How many quarters are in a standard NFL game?",
     "2", "3", "5", "4", "D"]
]

medium_questions = [
    ["Which team won Super Bowl 42?",
     "New England Patriots", "Pittsburgh Steelers",
     "New York Giants", "Green Bay Packers", "C"],

    ["Which player was nicknamed Megatron?",
     "Randy Moss", "Calvin Johnson",
     "Terrell Owens", "Larry Fitzgerald", "B"],

    ["Which team won Super Bowl 57?",
     "Philadelphia Eagles", "Kansas City Chiefs",
     "Los Angeles Rams", "San Francisco 49ers", "B"],

    ["Who was the quarterback for the Giants in Super Bowl 46?",
     "Peyton Manning", "Tom Brady",
     "Eli Manning", "Daniel Jones", "C"],

    ["Which team plays its home games at Lambeau Field?",
     "Chicago Bears", "Minnesota Vikings",
     "Detroit Lions", "Green Bay Packers", "D"]
]

hard_questions = [
    ["Who holds the NFL record for career receiving yards?",
     "Randy Moss", "Jerry Rice",
     "Terrell Owens", "Larry Fitzgerald", "B"],

    ["Which team completed the only perfect season including playoffs in the Super Bowl era through 2025?",
     "New England Patriots", "Chicago Bears",
     "Miami Dolphins", "Pittsburgh Steelers", "C"],

    ["Who was selected first overall in the 1998 NFL Draft?",
     "Ryan Leaf", "Peyton Manning",
     "Charles Woodson", "Randy Moss", "B"],

    ["Which team won the first Super Bowl?",
     "Kansas City Chiefs", "New York Jets",
     "Dallas Cowboys", "Green Bay Packers", "D"],

    ["Who was named MVP of Super Bowl 42?",
     "Tom Brady", "Michael Strahan",
     "Eli Manning", "David Tyree", "C"]
]


# Ask a question and return whether the player was correct.
def ask_question(question, number, total):
    print()
    print("------------------------------------")
    print("Question", number, "of", total)
    print("------------------------------------")

    print(question[0])
    print("A.", question[1])
    print("B.", question[2])
    print("C.", question[3])
    print("D.", question[4])

    answer = input("Your answer (A, B, C, D): ").strip().upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Enter A, B, C, or D.")
        answer = input("Your answer: ").strip().upper()

    if answer == question[5]:
        print("Correct!")
        return 1
    else:
        correct_index = ["A", "B", "C", "D"].index(question[5]) + 1
        print("Incorrect!")
        print("Correct answer:", question[correct_index])
        return 0


# Play one round of trivia.
def play_game():
    print()
    print("Choose your difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = input("Enter 1, 2, or 3: ")

    while difficulty not in ["1", "2", "3"]:
        print("Invalid selection.")
        difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        questions = easy_questions.copy()
        difficulty_name = "Easy"
    elif difficulty == "2":
        questions = medium_questions.copy()
        difficulty_name = "Medium"
    else:
        questions = hard_questions.copy()
        difficulty_name = "Hard"

    # Shuffle the question order each game.
    random.shuffle(questions)

    score = 0
    question_number = 1

    for question in questions:
        score += ask_question(question, question_number, len(questions))
        question_number += 1

    percentage = (score / len(questions)) * 100

    print()
    print("====================================")
    print("             GAME OVER")
    print("====================================")
    print("Final Score:", score, "out of", len(questions))
    print("Percentage:", round(percentage, 1), "%")

    if percentage == 100:
        print("Perfect score! You're an NFL expert!")
    elif percentage >= 80:
        print("Great job! You really know football!")
    elif percentage >= 60:
        print("Not bad! Keep studying your NFL trivia!")
    else:
        print("Keep practicing! You'll get better!")

    # Return the results so the main menu can track them.
    return [difficulty_name, score, len(questions), percentage]


# Main menu allows the player to replay or exit.
def main():
    session_results = []

    while True:
        print()
        print("====================================")
        print("       NFL TRIVIA CHALLENGE")
        print("====================================")
        print("1. Play Trivia")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = play_game()
            session_results.append(result)

        elif choice == "2":
            print()
            print("====================================")
            print("       TOTAL SESSION RESULTS")
            print("====================================")

            total_correct = 0
            total_questions = 0

            for number, result in enumerate(session_results, start=1):
                difficulty, score, questions, percentage = result

                print("Quiz", number, "(" + difficulty + "):",
                      score, "out of", questions,
                      "(" + str(round(percentage, 1)) + "%)")

                total_correct += score
                total_questions += questions

            print()
            print("Total Quizzes Played:", len(session_results))
            print("Total Correct Answers:", total_correct)
            print("Total Questions Answered:", total_questions)

            if total_questions > 0:
                overall_percentage = (total_correct / total_questions) * 100
                print("Overall Percentage:",
                      round(overall_percentage, 1), "%")
            else:
                print("Overall Percentage: N/A")

            print()
            print("Thanks for playing NFL Trivia Challenge!")
            break

        else:
            print("Invalid selection. Please enter 1 or 2.")


# Start the program.
main()

