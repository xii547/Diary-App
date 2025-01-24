import json

with open("data.json", 'r') as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["questions_text"])
    for index, answer in enumerate(question["answers_text"]):
        print(index + 1, "-", answer)

    user_answer = int(input("Please enter your answer: "))
    question["user_choice"] = user_answer

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer."
    else:
        result = "Wrong answer."

    message = f"{index + 1}. Question: {question['questions_text']}, " \
              f"Correct answer: {question['correct_answer']} , Your answer: {user_answer}"

    print(message)

print("Score: ", score, "/", len(data))