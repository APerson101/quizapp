import random

def generate_question(operation):
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)

  if operation == '1':
    return f"What is {num1} + {num2}?", num1 + num2
  elif operation == '4':
    return f"What is {num1} - {num2}?", num1 - num2
  elif operation == '3':
    return f"What is {num1} / {num2}?", num1 / num2
  elif operation == '2':
    return f"What is {num1} * {num2}?", num1 * num2


def take_quiz(operations):
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    scores = 0
    total_questions = 0
    for operation in operations:
        op = "addition" if operation == '1' else \
          "multiplication" if operation == '2' else \
            "division" if operation == '3' else \
              "subtraction"
        print(f"\n--- {op.capitalize()} Quiz ---")
        for _ in range(3):  # Asking 3 questions per operation
            question, answer = generate_question(operation)
            print(question)
            user_answer = input("Your answer: ")
            try:
                if float(user_answer) == answer:
                    scores += 1
            except ValueError:
                pass
            total_questions += 1
    print("\n--- Quiz Summary ---")
    print(f"Total Score: {scores}/{total_questions}")
    retry = input("Do you want to retry? (yes/no): ")
    if retry.lower() == 'yes':
        operations = input("Enter the operations you want to include (comma-separated): ").split(',')
        take_quiz(operations)
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    operations = input("Enter the operations you want to include \n(comma-separated use 1 for addition, 2 for multiplication, 3 for division, and 4 for subtraction): ").split(',')
    take_quiz(operations)