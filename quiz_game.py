import time
import random
import math

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

def display_question(q, idx):
    print(f"\n🧠 Question {idx + 1}: {q['question']}")
    for i, opt in enumerate(q['options']):
        print(f"   {chr(65 + i)}. {opt}")

def get_user_answer(timeout=10):
    print(f"⏱️ You have {timeout} seconds to answer.")
    start = time.time()
    while time.time() - start < timeout:
        try:
            answer = input("👉 Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print("⚠️ Invalid choice. Use A, B, C or D.")
        except:
            break
    print("⌛ Time's up! Marked as unanswered.")
    return None

def evaluate_answer(q, user_choice):
    if user_choice is None:
        return False
    index = ord(user_choice) - 65
    return q['options'][index] == q['answer']

def calculate_results(answers):
    correct = sum([1 for ans in answers if ans['correct']])
    total = len(answers)
    score = math.floor((correct / total) * 100)
    return correct, total, score

def save_results(filename, user, correct, total, score):
    with open(filename, 'a') as file:
        file.write(f"{user}|{correct}/{total}|{score}%\n")

def find_improvement_areas(answers):
    return list({ans['subdomain'] for ans in answers if not ans['correct']})

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

def start_quiz():
    name = input("Enter your name: ").strip()
    questions = load_questions("questions.txt")
    selected = random.sample(questions, 5)

    print("\n📘 Welcome to the Python Quiz Game!")
    print("📝 Answer 5 questions within 10 seconds each.\n")

    results = []
    for i, q in enumerate(selected):
        display_question(q, i)
        answer = get_user_answer(timeout=10)
        correct = evaluate_answer(q, answer)
        results.append({
            'subdomain': q['subdomain'],
            'correct': correct
        })

    correct, total, score = calculate_results(results)
    save_results("results.txt", name, correct, total, score)
    improvements = find_improvement_areas(results)
    show_final_result(name, correct, total, score, improvements)

# Run the game
if __name__ == "__main__":
    start_quiz()
