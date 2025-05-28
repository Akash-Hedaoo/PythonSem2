
improvement_areas = ['Variables', 'Loops']
results = [
    {
        'question': 'What is the correct way to declare a variable in Python?',
        'user_answer': 'B',  # User selected option B
        'correct_answer': 'x = 10',  # Correct answer content
        'options': ['let x = 10', 'x = 10', 'int x = 10', 'declare x = 10'],
        'subdomain': 'Variables',
        'correct': True  # User's answer is correct
    },
    {
        'question': 'Which data type is immutable in Python?',
        'user_answer': 'C',  # User selected option C
        'correct_answer': 'tuple',  # Correct answer content
        'options': ['set', 'list', 'tuple', 'dictionary'],
        'subdomain': 'Data Types',
        'correct': True  # User's answer is correct
    },
    {
        'question': 'What is the output of 3 ** 2?',
        'user_answer': 'A',  # User selected option A
        'correct_answer': '9',  # Correct answer content
        'options': ['6', '9', '8', '5'],
        'subdomain': 'Operators',
        'correct': False  # User's answer is incorrect
    },
    {
        'question': 'Which keyword exits a loop prematurely?',
        'user_answer': 'Unanswered',  # User did not answer
        'correct_answer': 'break',  # Correct answer content
        'options': ['continue', 'break', 'exit', 'pass'],
        'subdomain': 'Loops',
        'correct': False  # User's answer is incorrect
    },
    {
        'question': 'What is the default return value of a function that does not return anything?',
        'user_answer': 'D',  # User selected option D
        'correct_answer': 'None',  # Correct answer content
        'options': ['0', 'None', 'Error', 'Empty string'],
        'subdomain': 'Functions',
        'correct': False  # User's answer is incorrect
    }
]

save_report_card("Ashik" , 5,5,20,improvement_areas,results)