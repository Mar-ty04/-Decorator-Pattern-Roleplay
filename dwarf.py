import character

class Dwarf(character.Character):

  def __init__(self, n):
    super().__init__(n + " the Dwarf")

  def abilities(self):
  #returns the starting list of levels of the four different abilities.
    return[0,1,0,0]

  def constitution(self):
  #returns the starting stats.
    return 13

  def strength(self):
  #eturns the starting stats. 
    return 15

  def wisdom(self):
  #returns the starting stats.
    return 10
  