import abc

class Character(abc.ABC):
#rather than an interface, the Character class should be abstract since the
#character has a name attribute
  
  def __init__(self, n):
  #set the name attribute using the parameter n
    self._name = n
  
  @property 
  def name(self):
    return self._name
    
  @abc.abstractmethod
  def abilities(self):
  #abstract methods (no code)
    raise NotImplementedError()

  @abc.abstractmethod
  def constitution(self):
  #abstract methods (no code)
    raise NotImplementedError()

  @abc.abstractmethod
  def strength(self):
  #abstract methods (no code)
    raise NotImplementedError()

  @abc.abstractmethod
  def wisdom(self):
  #abstract methods (no code)
    raise NotImplementedError()

  def __str__(self):
    ab_str = ''
    if self.abilities()[0] > 0:
      ab_str += f'Archery: Level {self.abilities()[0]}\n'

    if self.abilities()[1] > 0:
      ab_str += f'Fighting: Level {self.abilities()[1]}\n'

    if self.abilities()[2] > 0:
      ab_str += f'Fire Magic: Level {self.abilities()[2]}\n'

    if self.abilities()[3] > 0:
      ab_str += f'Healing: Level {self.abilities()[3]}\n'

    return f'{self.name}\n-Abilities-\n' + ab_str + f'-Stats-\nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}'