from bs4 import BeautifulSoup

#load the file for chosen answers
choices_soup = BeautifulSoup(open('./chosen.html'), 'html.parser')

choices_tables = choices_soup.find_all("table", class_="menu-tbl")

choices = {}

for ct in choices_tables:
    body = ct.tbody
    
    ques_id = body.contents[1].find("td", class_="bold").string.strip()
    chosen = body.contents[7].find("td", class_="bold").string.strip()
    
    if chosen != "--":
        chosen_id = body.contents[int(chosen)+1].find("td", class_="bold").string.strip()
    else:
        chosen_id = None

    choices[ques_id] = chosen_id

#load the file for correct answers
table_id = "ctl00_ContentPlaceHolder1_grAnswerKey"


answers_soup = BeautifulSoup(open('./answers.html'), 'html.parser')

answers_table = answers_soup.find("table", id=table_id).tbody

answers = {}

for row in answers_table.find_all("tr"):
    cols = row.find_all("span")
    if len(cols) >= 3:    
        ques_id = cols[1].string
        answer_id = cols[2].string
        answers[ques_id] = answer_id

print("AMSWERS:")
score = 0
correct = 0
incorrect = 0
unanswered = 0
for q,a in answers.items():
    if a == choices[q]:
        score += 4
        correct += 1
    elif choices[q] == None:
        unanswered += 1
    else:
        score -= 1
        incorrect += 1

print("Score: {}".format(score))
print("Correct: {}, Incorrect: {}, Unanswered: {}".format(correct, incorrect, unanswered))
