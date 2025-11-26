"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    base_stats = {
        'Warrior': {'health': 120, 'strength': 15, 'magic': 5},
        'Mage': {'health': 80, 'strength': 5, 'magic': 15},
        'Rogue': {'health': 100, 'strength': 12, 'magic': 8},
        'Cleric': {'health': 90, 'strength': 8, 'magic': 10},
    }

    if character_class not in base_stats:
        raise ValueError(f"Class '{character_class}' is not recognized.")

    stats = base_stats[character_class]

    character = {
        'name': name,
        'class': character_class,
        'level': 1,
        'experience': 0,
        'gold': 100,
        'health': stats['health'],
        'max_health': stats['health'],
        'strength': stats['strength'],
        'magic': stats['magic'],
        'inventory': [],
        'equipment': {},
        'active_quests': [],
        'completed_quests': []
    }

    return character
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    #Verifies there is a directory to save the file in
    os.makedirs(save_directory, exist_ok=True)
    filename = f"{character['name']}_save.txt"
    filepath = os.path.join(save_directory, filename)

    inventory = ",".join(character.get('inventory', []))
    active_quests = ",".join(character.get('active_quests', []))
    completed_quests = ",".join(character.get('completed_quests', []))

    try:
        with open(filepath, 'w') as f:
            f.write(f"NAME: {character['name']}\n")
            f.write(f"CLASS: {character['class']}\n")
            f.write(f"LEVEL: {character['level']}\n")
            f.write(f"HEALTH: {character['health']}\n")
            f.write(f"MAX_HEALTH: {character['max_health']}\n")
            f.write(f"STRENGTH: {character['strength']}\n")
            f.write(f"MAGIC: {character['magic']}\n")
            f.write(f"EXPERIENCE: {character['experience']}\n")
            f.write(f"GOLD: {character['gold']}\n")
            f.write(f"INVENTORY: {inventory}\n")
            f.write(f"ACTIVE_QUESTS: {active_quests}\n")
            f.write(f"COMPLETED_QUESTS: {completed_quests}\n")
        return True
    except (IOError, PermissionError) as e:
        print(f"Error saving character: {e}")
        return False

    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    #Verifies the file exists
    filename = f"{character_name}_save.txt"
    filepath = os.path.join(save_directory, filename)

    #Raises CharacterNotFoundError if the file does not exist

    if not os.path.exists(filepath):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")
    #Tries to read the file, raises SaveFileCorruptedError if it cannot

    try:
        with open (filepath, "r") as file:
            lines = file.readlines()
    except:
        raise SaveFileCorruptedError(f"Save file for character '{character_name}' is corrupted.")
    character = {}

    #Parses the file line by line into a dictionary, raises InvalidSaveDataError if the format is wrong
    for line in lines:
        if ": " not in line:
            raise InvalidSaveDataError(f"Invalid data format in save file for '{character_name}'.")
        parts = line.strip().split(": ", 1)
        if len(parts) != 2:
            raise InvalidSaveDataError(f"Invalid data format in save file for '{character_name}'.")
        key = parts[0]
        value = parts[1]
        character[key] = value

    #Goes through the character dictionary and makes them correct lists and handles if the lsit is empty 
    inventory = character["INVENTORY"].split(",") if character["INVENTORY"] else []
    active_quests = character["ACTIVE_QUESTS"].split(",") if character["ACTIVE_QUESTS"] else []
    completed_quests = character["COMPLETED_QUESTS"].split(",") if character["COMPLETED_QUESTS"] else []

    #Sets the dictionary up to how we want it to be returned
    character_dict = {
        "name": character["NAME"],
        "class": character["CLASS"],
        "level": int(character["LEVEL"]),
        "health": int(character["HEALTH"]),
        "max_health": int(character["MAX_HEALTH"]),
        "strength": int(character["STRENGTH"]),
        "magic": int(character["MAGIC"]),
        "experience": int(character["EXPERIENCE"]),
        "gold": int(character["GOLD"]),
        "inventory": inventory,
        "active_quests": active_quests,
        "completed_quests": completed_quests
    }
    return character_dict

        
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    Returns: List of character names (without _save.txt extension)
    """
    #Makes sure the directory exists
    if not os.path.exists(save_directory):
        return []
    #Puts all the files in one spot
    files = os.listdir(save_directory)
    #Creates the empty list to hold the names
    character_names = []
    #Goes through the files and adds the names to the list
    for file in files:
        if file.endswith("_save.txt"):
            character_name = file[:-9]  # Remove '_save.txt'
            #Adds the name to the list without txt
            character_names.append(character_name)
    return character_names
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    #Calls the file path to a variable
    filename = f"{character_name}_save.txt"
    #Puts the file path together
    filepath = os.path.join(save_directory, filename)
    #Checks if the file exists, raises CharacterNotFoundError if it does not
    if not os.path.exists(filepath):
        raise CharacterNotFoundError(f"Character '{character_name}' not found.")
    #This is the deleting function of the file
    os.remove(filepath)

    return True
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    if character['health'] <= 0:
        raise CharacterDeadError(f"Character '{character['name']}' is dead the opps got em!")
    #Sets the amount of xp needed to level up
    level_up_xp = character['level'] * 100
    character['experience'] += xp_amount
    #Once character reaches the xp threshold, their stats go up by these amounts
    while character['experience'] >= level_up_xp:
        #This rolls over any extra xp after leveling up
        character['experience'] -= level_up_xp
        character['level'] += 1
        character['max_health'] += 10
        character['strength'] += 2
        character['magic'] += 2
        character['health'] = character['max_health']
        level_up_xp = character['level'] * 100
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    character['gold'] += amount
    if character['gold'] < 0:
        raise ValueError("Gold amount cannot be negative.")
    return character['gold']
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    #How much health the character could gain
    before_healing = character['health'] + amount
    #This handles if its too much healing
    if before_healing > character['max_health']:
        #This shows how much is needed to get to max health if over
        actual_healed = character['max_health'] - character['health']
        #Sets health to max health if over the limit
        character['health'] = character['max_health']
    #This if it's within the healing limit
    else:
        actual_healed = amount
        character['health'] += amount

    return actual_healed
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    if character['health'] <= 0:
        return True
    else:
        return False
    # TODO: Implement death check
    

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    if character['health'] <= 0:
        character['health'] = character['max_health'] // 2
        return True
    # TODO: Implement revival
    # Restore health to half of max_health
    

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    valid_character = {
        "name": str,
        "class": str,
        "level": int,
        "health": int,
        "max_health": int,
        "strength": int,
        "magic": int,
        "experience": int,
        "gold": int,
        "inventory": list,
        "active_quests": list,
        "completed_quests": list
    }
    if character == valid_character:
        return True
    else:
        raise InvalidSaveDataError("Character data is invalid.")
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")
    
    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")
    
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")

