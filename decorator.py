import abc
import character

class Decorator(character.Character, abc.ABC):
  
  def __init__(self, c):
  #call super init so the decoration has the name attribute
  #pass it the name of the character parameter, then set the character attribute to c
    super().__init__(c.name)
    self._char = c

  def abilities(self):
  #call the same method on your character attribute
    return self._char.abilities()

  def constitution(self):
  #call the same method on your character attribute
    return self._char.constitution()

  def strength(self):
  #call the same method on your character attribute
    return self._char.strength()

  def wisdom(self):
  #call the same method on your character attribute
    return self._char.wisdom()