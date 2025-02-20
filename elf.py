import character

class Elf(character.Character):

  def __init__(self, n):
    super().__init__(n + " the Elf")

  def abilities(self):
  #returns the starting list of levels of the four different abilities.
    return [1,0,0,0]
    
  def constitution(self):
  #returns the starting stats.
    return 13

  def strength(self):
  #returns the starting stats.
    return 10

  def wisdom(self):
  #returns the starting stats.
    return 15