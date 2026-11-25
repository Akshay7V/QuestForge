from domain.character import Character

def run_special_round(attacker:Character ,defender:Character)->None:
    """Works for ANY Character subclass — this is polymorphism in action."""
    attacker.special_ability(defender)
    
    
    
    
# def total_party_damage(attacker:list[Character],defender:Character)->None:
#     """Works for ANY Character subclass — this is polymorphism in action."""

#     attacker.take_damage(defender)


def total_party_damage(party: list[Character], target: Character) -> int:
  """Works for ANY Character subclass — this is polymorphism in action."""
  total_damage = 0
  for member in party:
    before_hp = target.health
    member.attack(target)
    total_damage += before_hp - target.health
  return total_damage

