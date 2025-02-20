import decorator

class Archery (decorator.Decorator):

  def abilities(self):
  #add 1 to the ability level for this ability.
    list = super().abilities()
    list[0] += 1
    return list 

  def constitution(self):
  #modify based on archery 
    return super().constitution() - 2

  def strength(self):
  #modify based on archery 
    return super().strength() + 5 

  def wisdom(self):
    #modify based on archery 
    return super().wisdom() - 2