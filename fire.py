import decorator

class Fire(decorator.Decorator):

  def abilities(self):
  #add 1 to this ability level
    list = super().abilities()
    list[2] += 1
    return list

  def constitution(self):
    #modify based on fire
    return super().constitution() - 3

  def strength(self):
    #modify based on fire
    return super().strength() - 1

  def wisdom(self):
    #modify based on fire
    return super().wisdom() + 5