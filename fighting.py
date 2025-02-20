import decorator

class Fighting(decorator.Decorator):

  def abilities(self):
  #add one to level for this ability 
    list = super().abilities()
    list[1] += 1
    return list 

  def constitution(self):
  #modify based on fighting
    return super().constitution() + 2

  def strength(self):
  #modify based on fighting 
    return super().strength() + 2

  def wisdom(self):
  #modify based on fighting
    return super().wisdom() - 3