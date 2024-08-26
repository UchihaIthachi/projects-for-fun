import json
import os

def load_questions():
    questions_answers_dict = {}

    # Check if quizoutput.txt exists
    if not os.path.exists('quizoutput.txt'):
        print('quizoutput.txt does not exist. Make sure to create the quiz first.')
        return questions_answers_dict

    try:
        with open('quizoutput.txt', 'r') as f:
            lines = f.readlines()

        if lines:
            # Parse JSON data
            try:
                json_output = json.loads(lines[0])

                number_of_questions = 0
                for item in json_output:
                    if 'question' in item:
                        number_of_questions += 1
                
                print(f'Number of questions: {number_of_questions}')

                for i, item in enumerate(json_output, start=1):
                    if 'question' in item and 'answers' in item and 'correct_answers' in item:
                        question = item['question']
                        answers = item['answers']
                        correct_answer = next((key for key, value in item['correct_answers'].items() if value == 'true'), None)

                        questions_answers_dict[f'question_{i}'] = {
                            'question': question,
                            'answers': answers,
                            'correct_answer': correct_answer[:8] if correct_answer else None
                        }
                    else:
                        print(f'Skipping item {i} due to missing data')

            except json.JSONDecodeError:
                print('Error: Invalid JSON format in quizoutput.txt')
    except FileNotFoundError:
        print('quizoutput.txt does not exist. Run python3 createquiz.py then run python3 jsonify_quiz_output.py then python3 app.py')

    return questions_answers_dict

# Example usage
questions_dict = load_questions()
print("Hello")
print(questions_dict)
