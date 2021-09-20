class Game():
    def __init__(self, choice_1, choice_2):
        self.choice_1=choice_1
        self.choice_2=choice_2
        

    def get_results(self, choice_1, choice_2):
        if choice_1 == "rock" and choice_2 == "scissors":
            return "Rock wins!"
    
        if choice_1 == "rock" and choice_2 == "paper":
            return "Paper wins!"

        if choice_1 == "paper" and choice_2 == "scissors":
            return "Scissors wins!"
    
        if choice_1 == "paper" and choice_2 == "rock":
            return "Paper wins!"
    
        if choice_1 == "scissors" and choice_2 == "rock":
            return "Rock wins!"
    
        if choice_1 == "scissors" and choice_2 == "paper":
            return "Scissors wins!"
    
        if choice_1 == choice_2:
            return "Its a draw!"

    