import requests
import json
import quiz_load

# Function to send quiz questions to a Telegram chat
def send_quiz_questions(bot_token, chat_id, questions):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    for question_number, question_data in questions.items():
        question_text = f"{question_data['question']}\n\n"
        options = question_data['answers']
        keyboard = {"keyboard": [[option for option in options.values() if option is not None]]}
        data = {
            "chat_id": chat_id,
            "text": question_text,
            "reply_markup": json.dumps(keyboard)
        }
        response = requests.post(base_url, data=data)
        if response.status_code != 200:
            print(f"Failed to send question {question_number} to chat. Status code: {response.status_code}")

# Main function to run the bot
def main():
    # Telegram bot token
    bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    # Telegram chat ID (you can obtain it from the chat with your bot)
    chat_id = "YOUR_CHAT_ID"
    # Quiz API token
    api_token = "c19gwHdliDpvGTrSQFFHg74ai0W0hR7Tn8e2s5Sl"
    # Number of quiz questions to fetch
    num_questions = 5

    # Load quiz questions
    questions = quiz_load.load_questions()
    
    # Check if questions were loaded successfully
    if questions:
        print(questions)
        # Send quiz questions to Telegram chat
        """ send_quiz_questions(bot_token, chat_id, questions) """
    else:
        print("Failed to load quiz questions.")

if __name__ == "__main__":
    main()
