#Description: A simple game that allows the user to choose a move, attack and get attacked. Attacks result in the loss of lives.

lifecount = [1,1,1]
lifecount2 = [1,1,1]
lifecount3 = [1,1,1]
mylifecount = [1,1,1]
print('Welcome to the game. Your goal is to defeat your enemies by attacking them. But be careful, as they will attack you, too! '
      'There are 3 enemies. '
      'You and they have 3 lives each. If you attack Enemy 1, they will loose a life, but will not attack you. '
      'If you attack Enemy 2, you will both loose one life. If you attack Enemy 3, it will only cost you a life. '
      'You can only defeat Enemy 2 and 3 with a special move. In order to unlock it, defeat Enemy 1. Ready? Let us begin!')
class Enemy:
    def attack(self):
        lifecount.pop(0)
    def lifecount(self):
        print('Enemy 1 lives left:')
        print(len(lifecount))
class Enemy2(Enemy):
    def attack(self):
        lifecount2.pop(0)
    def lifecount(self):
        print('Enemy 2 lives left:')
        print(len(lifecount2))
class Enemy3(Enemy):
    def attack (self):
        lifecount3.pop(0)
    def lifecount(self):
        print('Enemy 3 lives left:')
        print(len(lifecount3))
class Player:
    def attack(self):
        mylifecount.pop(0)
    def lifecount(self):
        print('Your lives left:')
        print(len(mylifecount))

while True:
    enemy1 = Enemy()
    enemy2 = Enemy2()
    enemy3 = Enemy3()
    player = Player()
    move = input('Choose an enemy to attack (1,2,3):')
    if move == '1':
        enemy1.attack()
        enemy1.lifecount()
        player.lifecount()
    elif move == '2':
        enemy2.attack()
        player.attack()
        enemy2.lifecount()
        player.lifecount()
    elif move == '3':
        player.attack()
        enemy3.lifecount()
        player.lifecount()
    if len(lifecount) == 0:
        print('Enemy 1 defeated. Special move unlocked! If you attack enemy 1 or 2 now, only they will loose lives.')
        while True:
            enemy2 = Enemy2()
            enemy3 = Enemy3()
            player = Player()
            move = input('Choose an enemy to attack (2,3):')
            if move == '2':
                enemy2.attack()
                enemy2.lifecount()
                player.lifecount()
            elif move == '3':
                enemy3.attack()
                enemy3.lifecount()
                player.lifecount()
            if len(lifecount2) == 0 and len(lifecount3) == 0:
                print('You defeated all enemies. You won!')
                break
            if len(mylifecount) == 0:
                print('You were defeated. The enemies won!')
                break
        break
    if len(mylifecount) == 0:
        print('You were defeated. The enemies won!')
        break




