import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root, total_rounds=5):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.total_rounds = total_rounds
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 20))
        self.title_label.pack(pady=10)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.rock_button = tk.Button(self.button_frame, text="Rock", width=15, command=lambda: self.play_game(0))
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(self.button_frame, text="Paper", width=15, command=lambda: self.play_game(1))
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=15, command=lambda: self.play_game(2))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        
        self.score_label = tk.Label(self.root, text="Score: You 0 - 0 Computer", font=("Helvetica", 14))
        self.score_label.pack(pady=10)
        
        self.round_label = tk.Label(self.root, text=f"Round 1 of {self.total_rounds}", font=("Helvetica", 12))
        self.round_label.pack(pady=10)
        
        self.play_again_button = tk.Button(self.root, text="Play Again", width=15, command=self.reset_game, state='disabled')
        self.play_again_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", width=15, command=self.root.quit)
        self.quit_button.pack(pady=5)
        
    def play_game(self, user_choice):
        if self.rounds_played < self.total_rounds:
            computer_choice = random.randint(0, 2)
            result = self.check_winner(user_choice, computer_choice)
            
            if result == "win":
                self.user_score += 1
            elif result == "lose":
                self.computer_score += 1
            
            self.rounds_played += 1
            choices = ["Rock", "Paper", "Scissors"]
            
            self.result_label.config(
                text=f"You chose: {choices[user_choice]} | Computer chose: {choices[computer_choice]}\nResult: {self.get_result_message(result)}"
            )
            
            self.score_label.config(
                text=f"Score: You {self.user_score} - {self.computer_score} Computer"
            )
            
            if self.rounds_played < self.total_rounds:
                self.round_label.config(text=f"Round {self.rounds_played + 1} of {self.total_rounds}")
            else:
                self.end_game()
    
    def check_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
            return "win"
        else:
            return "lose"
        
    def get_result_message(self, result):
        if result == "tie":
            return "It's a tie!"
        elif result == "win":
            return "You win!"
        else:
            return "You lose!"
    
    def end_game(self):
        final_result = "It's a Draw!"
        if self.user_score > self.computer_score:
            final_result = "Congratulations, You Win the Game!"
        elif self.user_score < self.computer_score:
            final_result = "Computer Wins the Game!"
        
        self.result_label.config(
            text=f"Game Over!\nFinal Score: You {self.user_score} - {self.computer_score} Computer\n{final_result}"
        )
        
        self.rock_button.config(state='disabled')
        self.paper_button.config(state='disabled')
        self.scissors_button.config(state='disabled')
        
        self.play_again_button.config(state='normal')
    
    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.score_label.config(text="Score: You 0 - 0 Computer")
        self.round_label.config(text=f"Round 1 of {self.total_rounds}")
        
        self.rock_button.config(state='normal')
        self.paper_button.config(state='normal')
        self.scissors_button.config(state='normal')
        
        self.play_again_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root, total_rounds=5)
    root.mainloop()
