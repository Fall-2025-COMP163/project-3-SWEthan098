"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""

from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    goblin_stats = {
        "name": "goblin",
        "health": 50,
        "max_health": 50,
        "strength": 8,
        "magic": 2,
        "xp_reward": 25,
        "gold_reward": 10
    }
    orc_stats = {
        "name": "orc",
        "health": 80,
        "max_health": 80,
        "strength": 12,
        "magic": 5,
        "xp_reward": 50,
        "gold_reward": 25
    }
    dragon_stats = {
        "name": "dragon",
        "health": 200,
        "max_health": 200,
        "strength": 25,
        "magic": 15,
        "xp_reward": 200,
        "gold_reward": 100
    }

    if enemy_type == "goblin":
        return goblin_stats
    elif enemy_type == "orc":
        return orc_stats
    elif enemy_type == "dragon":
        return dragon_stats
    else:
        raise InvalidTargetError(f"Enemy type '{enemy_type}' is not recognized.")
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    

def get_random_enemy_for_level(character_level):
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    
    Returns: Enemy dictionary
    """
    if character_level <= 2:
        return create_enemy("goblin")
    elif 3 <= character_level <= 5:
        return create_enemy("orc")
    else:
        return create_enemy("dragon")

    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type
    

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    
    def __init__(self, character, enemy):
        """Initialize battle with character and enemy"""
        
        self.character = character
        self.enemy = enemy
        #This allows me to track if combat is happening
        self.combat_active = True
        #Sets up the counter for turns
        self.turn_counter = 0

        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
        pass
    
    def start_battle(self):
        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        if self.character['health'] <= 0:
            raise CharacterDeadError("Character is dead and cannot fight.")
        else:
            print(f"enemy '{self.enemy['name']}' appears!")
        #Tracks the turns of the battle
        while self.combat_active:
            self.turn_counter += 1
        #Handles if combat ends
            if not self.combat_active:
                break

        if self.enemy['health'] <= 0:
            xp += 50
            gold += 20
            print("Enemy defeated!")
            return {
                'winner': 'player',
                'xp_gained': xp,
                'gold_gained': gold
            }
        else:
            return {'winner': {self.enemy}, 'xp_gained': 0, 'gold_gained': 0}
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins
        
    
    def player_turn(self):
        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        if not self.combat_active:
            raise CombatNotActiveError("Cannot take player turn when combat is not active.")
        else:
            print("1. Basic Attack")
            print("2. Special Ability")
            print("3. Try to Run")
            choice = input("Enter choice (1-3): ")
            if choice == '1':
                print("You chose to attack!")
            elif choice == '2':
                print("You chose to use a special ability!")
            elif choice == '3':
                print("You chose to try to run away!")
            
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        
    
    def enemy_turn(self):
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        if not self.combat_active:
            raise CombatNotActiveError("Cannot take enemy turn when combat is not active.")
        else:
            print(f"The {self.enemy['name']} attacks!")
            self.calculate_damage(self.enemy, self.character)
            print(f"The {self.enemy['name']} dealt damage to you!")
            self.character["health"] -= self.calculate_damage(self.enemy, self.character)
            if self.character["health"] <= 0:
                #Sets health to 0 because it doesn't make sense to have negative health
                self.character["health"] = 0
                #Ends combat if character dies
                self.combat_active = False
                print("You have been defeated!")
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        
    
    def calculate_damage(self, attacker, defender):
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        self.damage = attacker['strength'] - (defender['strength'] // 4)
        if self.damage < 1:
            self.damage = 1
        return self.damage
        # TODO: Implement damage calculation
        
    
    def apply_damage(self, target, damage):
        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        target['health'] -= damage
        if target['health'] < 0:
            target['health'] = 0
        # TODO: Implement damage application
    
    def check_battle_end(self):
        """
        Check if battle is over
        
        Returns: 'player' if enemy dead, 'enemy' if character dead, None if ongoing
        """
        if self.enemy['health'] <= 0:
            return 'player'
        elif self.character['health'] <= 0:
            return 'enemy'
        return None
        # TODO: Implement battle end check
    
    def attempt_escape(self):
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        import random
        if random.random() < 0.5:
            self.combat_active = False
            print("You successfully escaped!")
            return True
        else:
            print("Escape failed!")
            return False
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    if character['class'] == 'Warrior':
        return warrior_power_strike(character, enemy)
    elif character['class'] == 'Mage':
        return mage_fireball(character, enemy)
    elif character['class'] == 'Rogue':
        return rogue_critical_strike(character, enemy)
    elif character['class'] == 'Cleric':
        return cleric_heal(character)
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    

def warrior_power_strike(character, enemy):
    """Warrior special ability"""
    character_damage = character['strength'] * 2 - (enemy['strength'] // 4)
    if character_damage < 1:
        character_damage = 1
    # TODO: Implement power strike
    # Double strength damage
    

def mage_fireball(character, enemy):
    """Mage special ability"""
    # TODO: Implement fireball
    # Double magic damage
    pass

def rogue_critical_strike(character, enemy):
    """Rogue special ability"""
    # TODO: Implement critical strike
    # 50% chance for triple damage
    pass

def cleric_heal(character):
    """Cleric special ability"""
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    pass

# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    pass

def get_victory_rewards(enemy):
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    pass

def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    print(f"\n{character['name']}: HP={character['health']}/{character['max_health']}")
    print(f"{enemy['name']}: HP={enemy['health']}/{enemy['max_health']}")
    pass

def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    print(f">>> {message}")
    pass

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    
    # Test enemy creation
    # try:
    #     goblin = create_enemy("goblin")
    #     print(f"Created {goblin['name']}")
    # except InvalidTargetError as e:
    #     print(f"Invalid enemy: {e}")
    
    # Test battle
    # test_char = {
    #     'name': 'Hero',
    #     'class': 'Warrior',
    #     'health': 120,
    #     'max_health': 120,
    #     'strength': 15,
    #     'magic': 5
    # }
    #
    # battle = SimpleBattle(test_char, goblin)
    # try:
    #     result = battle.start_battle()
    #     print(f"Battle result: {result}")
    # except CharacterDeadError:
    #     print("Character is dead!")

