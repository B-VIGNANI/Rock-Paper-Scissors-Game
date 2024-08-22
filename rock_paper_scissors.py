import tkinter as tk
import random
# To determine the computer's choice
def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])
# To determine the winner
def determine_winner(user, computer):
    if user == computer:
        return 'Draw'
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Scissors' and computer == 'Paper') or \
         (user == 'Paper' and computer == 'Rock'):
        return 'User'
    else:
        return 'Computer'
# To play the game
def play(user_choice):
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    if result == 'User':
        scores['User'] += 1
        result_text.set(f"You chose {user_choice}, computer chose {comp_choice}. You are Fabulous!")
    elif result == 'Computer':
        scores['Computer'] += 1
        result_text.set(f"You chose {user_choice}, computer chose {comp_choice}. Don't give up!")
    else:
        result_text.set(f"You chose {user_choice}, computer chose {comp_choice}. It's a draw!")
    
    score_text.set(f"Scores - User: {scores['User']}, Computer: {scores['Computer']}")

# To reset the game
def reset_game():
    scores['User'] = 0
    scores['Computer'] = 0
    result_text.set("let's play!")
    score_text.set("Scores - User: 0\n, Computer: 0\n")
# Initialize scores
scores = {'User': 0, 'Computer': 0}
# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
# Create a frame for the game
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)
# label for the result
result_text = tk.StringVar()
result_text.set("Let's play!")
result_label = tk.Label(frame, textvariable=result_text, font=("Arial", 14))
result_label.pack(pady=10)
# Add buttons for user choices
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("Rock"), bg="lightblue", font=("Arial", 12))
rock_button.grid(row=0, column=0, padx=5)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"), bg="lightgreen", font=("Arial", 12))
paper_button.grid(row=0, column=1, padx=5)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"), bg="lightcoral", font=("Arial", 12))
scissors_button.grid(row=0, column=2, padx=5)
# label for the scores
score_text = tk.StringVar()
score_text.set("Scores - User: 0\n, Computer: 0\n")
score_label = tk.Label(frame, textvariable=score_text, font=("Arial", 14))
score_label.pack(pady=10)
# Add a reset button
reset_button = tk.Button(frame, text="Play Again", command=reset_game, bg="yellow", font=("Arial", 12))
reset_button.pack(pady=10)
# Run the application
root.mainloop()
