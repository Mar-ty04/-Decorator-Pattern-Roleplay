import character 

class Halfling(character.Character):

  def __init__(self, n):
    super().__init__(n + " the Halfling")

  def abilities(self):
  #returns the starting list of levels of the four different abilities.
    return [0,0,0,1]

  def constitution(self):
  #returns the starting stats.
    return 15

  def strength(self):
  #returns the starting stats
    return 10

  def wisdom(self):
  #returns the starting stats.
    return 13