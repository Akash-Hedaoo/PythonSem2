import time
import random
import math
import os

def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 7:
                question = {
                    'subdomain': parts[0],
                    'question': parts[1],
                    'options': parts[2:6],
                    'answer': parts[6],
                }
                questions.append(question)
    return questions

def display_question(q, idx):
    print(f"\n🧠 Question {idx + 1}: {q['question']}")
    i = 0
    for opt in q['options']:
        print(f"   {chr(65 + i)}. {opt}")
        i += 1

def get_user_answer(timeout=10):
    print(f"⏱️ You have {timeout} seconds to answer.")
    start = time.time()
    while True:
        answer = input("👉 Your answer (A/B/C/D): ").strip().upper()
        if time.time() - start >= 10:
            print("⌛ Time's up! Marked as unanswered.")
            return None
        elif answer not in ['A', 'B', 'C', 'D']:
            print("⚠️ Invalid choice. Use A, B, C or D.")
        else:
            return answer
    return None

def evaluate_answer(q, user_choice):
    if user_choice is None:
        return False
    index = ord(user_choice) - 65
    return q['options'][index] == q['answer']

def calculate_results(answers):
    correct = 0
    for ans in answers:
        if ans['correct']:
            correct += 1
    total = len(answers)
    score = math.floor((correct / total) * 100)
    return correct, total, score

def save_results(filename, user, correct, total, score):
    with open(filename, 'a') as file:
        file.write(f"{user}|{correct}/{total}|{score}%\n")

def find_improvement_areas(answers):
    improvement_areas = []
    for ans in answers:
        if not ans['correct'] and ans['subdomain'] not in improvement_areas:
            improvement_areas.append(ans['subdomain'])
    return improvement_areas

def show_final_result(name, correct, total, score, improvements):
    print("\n" + "=" * 60)
    print("🎯 " + "QUIZ SUMMARY".center(50, '-') + " 🎯")
    print("=" * 60)
    print(f"👤 Participant: {name}")
    print(f"✅ Correct Answers: {correct}/{total}")
    print(f"📊 Score: {score}%")
    print("\n📌 Areas of Improvement:")
    if improvements:
        for area in improvements:
            print(f"   🔻 {area}")
    else:
        print("   🟢 None. Excellent Work!")
    print("=" * 60)
    print("🎓 Thank you for participating. Keep learning Python!\n")
    print("=" * 60)

def save_report_card(name, correct, total, score, improvements, results):
    os.makedirs('report_cards', exist_ok=True)
    filename = f"report_cards/{name}_report_card.txt"
    with open(filename, 'w') as file:
        file.write(f"Student Name: {name}\n")
        file.write(f"Correct Answers: {correct}/{total}\n")
        file.write(f"Score: {score}%\n")
        file.write("=" * 60 + "\n")
        file.write("Detailed Question Report:\n")
        for i, result in enumerate(results):
            file.write(f"Q{i + 1}: {result['question']}\n")
            user_answer_content = result['user_answer'] if result['user_answer'] == "Unanswered" else result['options'][ord(result['user_answer']) - 65]
            file.write(f"   Your Answer: {user_answer_content}\n")
            file.write(f"   Correct Answer: {result['correct_answer']}\n")
            file.write("-" * 60 + "\n")
        file.write("Areas of Improvement:\n")
        if improvements:
            for area in improvements:
                file.write(f"   - {area}\n")
        else:
            file.write("   None. Excellent Work!\n")
        file.write("=" * 60 + "\n\n")

def main():
    name = input("Enter your name: ").strip()
    questions = load_questions("questions.txt")
    selected = random.sample(questions, 5)
    print("\n📘 Welcome to the Python Quiz Game!")
    print("📝 Answer 5 questions within 10 seconds each.\n")
    results = []
    for i in range(len(selected)):
        q = selected[i]
        display_question(q, i)
        answer = get_user_answer(timeout=10)
        correct = evaluate_answer(q, answer)
        results.append({
            'question': q['question'],
            'user_answer': answer if answer else "Unanswered",
            'correct_answer': q['answer'],
            'options': q['options'],
            'subdomain': q['subdomain'],
            'correct': correct
        })
    correct, total, score = calculate_results(results)
    save_results("results.txt", name, correct, total, score)
    improvements = find_improvement_areas(results)
    show_final_result(name, correct, total, score, improvements)
    save_report_card(name, correct, total, score, improvements, results)

if __name__ == "__main__":
    main()
