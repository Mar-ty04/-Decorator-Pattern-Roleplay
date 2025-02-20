import decorator

class Healing(decorator.Decorator):

  def abilities(self):
  #add one to the level for this ability
    list = super().abilities()
    list[3] += 1
    return list 

  def constitution(self):
  #modify based on healing
    return super().constitution() + 3

  def strength(self):
  #modify based on healing 
    return super().strength() - 4

  def wisdom(self):
  #modify based on healing
    return super().wisdom() + 2