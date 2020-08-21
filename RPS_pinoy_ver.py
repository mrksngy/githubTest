from random import randint

i = ["Rock", "Paper", "Scissors"]
computer = i[randint(0,2)]
player = False
score = 0
score1 = 0



while player == False:
    print("Welcome to Rock, Paper, Scissors Game")
    player = input("Rock,Paper,Scissors:")
    if player == computer:
        print("\nTabla!!" + " Comp pick the same as yours")
        print("\nPlayer: {} Computer: {}\n".format(score, score1))
        computer = i[randint(0, 2)]
        player = False
    elif player == "Rock":
        if computer == "Paper":
            print("Talo ako" + " Ang pinili ng kalaban ay Papel")
            score1 += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False

        else:
            print("Panalo ako")
            score += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False
    elif player == "Paper":
        if computer == "Scissors":
            print("Talo ako tangina" + " Ang pinili ng kalaban ay Gunting")
            score1 += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False
        else:
            print("Panalo ang papel sa bato!")
            score += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False
    elif player == "Scissors":
        if computer == "Rock":
            print("Comp win bobo" + "Ang pinili ng kalaban ay Bato putanginaka")
            score1 += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False
        else:
            print("Tangina mo panalo ako gago")
            score += 1
            print("\nPlayer: {} Computer: {}\n".format(score, score1))
            computer = i[randint(0, 2)]
            player = False
    else:
        print("Ano yan? Ayusin mo")
        player = False
    if score == 5:
        print("Player WinS!")
        break
    if score1 == 5:
        print("You lose!!")
        break