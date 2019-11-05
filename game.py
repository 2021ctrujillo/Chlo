import random

class Player:
  # Class variables that are shared among ALL players
  player_list = [] #Each time we create a player, we will push them into this list.
  player_count = 0

  def __init__(self, name):
    ## These instance variables should be unique to each user. Every user will HAVE a name, but each user will probably have a different name.
    self.name = name
    self.strength = random.randint(8, 12) # The stat values will all be random, but within a range of reasonableness
    self.defense = random.randint(8, 12)
    self.speed = random.randint(8, 12)
    self.max_health = random.randint(18, 24) # The max health value will be random, but higher than the others.
    self.health = self.max_health # Set the current health equal to the max health.
    self.alive = True
    print("Player " + self.name + " has entered the game. \n  Strength: " + str(self.strength) + "\n  Defense: " + str(self.defense) + "\n  Speed: " + str(self.speed) + "\n  Maximum health: " + str(self.max_health) + ".\n")
    ## We're going to also manipulate the two class variables - While each user has their own specific defense or strength, the users all share the class variables defined above this method.
    Player.player_list.append(self) ## The player will be added to the list of players.
    Player.player_count += 1 ## The player count should go up by one.
    print("There are currently " + str(Player.player_count) + " player(s) in the game.\n\n")

## create a decrease_health_by object and pass in arguments self and damage
  def decrease_health_by(self, damage):
    ## if the damage done on the target is less than the amount of health they have left...
    if damage < self.health:
      ## decrease the player's health by the amount of damage done
      self.health -= damage
      ## print how much strength and health the player has left
      print(self.name + " now has " + str(self.health) + "/" + str(self.max_health) + " health remaining.\n\n")
    else:
      ## if the damage done on the player's health decreases their health to 0, print that the player has lost the game
      self.health = 0 
      print(self.name + " has lost! Retry the game.")


  def attack(self, target):
    ## With a CLI, we want to print out all the information our users need to play this game.
    ## Let's show the attacker and defender's names here.
    print("Player " + self.name + " attacks " + target.name + "!!!")
    print(self.name + "'s strength is " + str(self.strength) + " and target " + target.name + "'s defense is " + str(target.defense) + ".")
    ## The battle will go differently depending on who is stronger.
    if self.strength < target.defense:
      print("Due to the target's strong defense, the attack only does half damage...")
      damage = self.strength / 2
        #call the decrease_health_by method and pass in the target object and the damage value
      target.decrease_health_by(damage)
    elif self.strength > target.defense:
      print("Since the target is weaker than you are, the attack does double damage!")
      damage = self.strength * 2
      target.decrease_health_by(damage)
    else:
      print("These players are evenly matched. The attack goes through normally.")
      damage = self.strength
      target.decrease_health_by(damage)
    #target.health -= damage

## create a new class called Battle that will initilize the battle between the two arguments: player1 and player2
class Battle:
  #create the init method, and the Battle class takes the arguments of two players who are battling, so there is player1 and player2
  def __init__ (self, player1, player2):
    self.player1 = player1
    self.player2 = player2
  def start(self):
    ## while the two players' healths are above 0...
    while self.player1.health > 0 and self.player2.health > 0:
      ## the players will attack each other until one dies. then the battle will stop
      self.player1.attack(self.player2)
      self.player2.attack(self.player1)
      #use this line to make sure it is running
      print("This battle is crazy!")
    
    # if self.player1.health < 0 or self.player2.health < 0:
    #   breakpoint
