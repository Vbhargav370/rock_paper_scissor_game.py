import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.user_score = 0
        self.computer_score = 0
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 20))
        self.title_label.pack(pady=10)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.rock_button = tk.Button(self.button_frame, text="Rock", width=15, command=lambda: self.play_game("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(self.button_frame, text="Paper", width=15, command=lambda: self.play_game("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=15, command=lambda: self.play_game("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
        self.score_label = tk.Label(self.root, text="Score: You 0 - 0 Computer", font=("Helvetica", 14))
        self.score_label.pack(pady=10)
        
        self.play_again_button = tk.Button(self.root, text="Play Again", width=15, command=self.reset_game)
        self.play_again_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", width=15, command=self.root.quit)
        self.quit_button.pack(pady=5)
        
    def play_game(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = self.determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1
        
        self.result_label.config(
            text=f"You chose: {user_choice} | Computer chose: {computer_choice}\nResult: {self.get_result_message(winner)}"
        )
        
        self.score_label.config(
            text=f"Score: You {self.user_score} - {self.computer_score} Computer"
        )
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "user"
        else:
            return "computer"
        
    def get_result_message(self, winner):
        if winner == "tie":
            return "It's a tie!"
        elif winner == "user":
            return "You win!"
        else:
            return "You lose!"
    
    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You 0 - 0 Computer")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
