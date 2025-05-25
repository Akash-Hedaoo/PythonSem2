def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 6:
                question = {
                    'subdomain': parts[0],
                    'question': parts[1],
                    'options': parts[2:6],
                    'answer': parts[2]  # Always assume first option is correct
                }
                questions.append(question)
    return questions
print(load_questions('try_Questions.txt'))
