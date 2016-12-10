import ClimbingGame
trials = 5000

def main2():
    game = ClimbingGame.ClimbingGame(0)
    actionsA = [0,1,2]
    count_actionA = [0]*3
    count_actionB = [0]*3
    actionsB = [0,1,2]
    Q_playerA = [[0]*3 for i in range(3)]
    Q_playerB = [[0]*3 for i in range(3)]
    print(game.get(1,1))

if __name__ == '__main__':
    main2()