# Quest Chronicles - A Modular RPG Adventure

**Name:** Ethan Hall  
**Course:** COMP 163 - Project 3

## AI Usage

Used Claude AI to help fix:

- Character dictionary formatting errors with equipped_weapon and equipped_armor keys
- Save/load file formatting issues with empty values and the ": " separator
- Quest validation order (checking if quest exists before accessing it)
- Item name handling when 'name' key is missing from item_data

## What Each Module Does

**character_manager.py** - Creates characters, saves/loads them, handles leveling up and gold

**inventory_system.py** - Manages inventory, items, equipment, and shop

**quest_handler.py** - Handles accepting, completing, and tracking quests

**combat_system.py** - Runs battles between character and enemies

**game_data.py** - Loads quest and item data from text files

**main.py** - Main game loop and menus that ties everything together

## Exception Handling

Each module raises specific exceptions for different errors:

- Character errors: InvalidCharacterClassError, CharacterNotFoundError, CharacterDeadError
- Inventory errors: InventoryFullError, ItemNotFoundError, InsufficientResourcesError
- Quest errors: QuestNotFoundError, InsufficientLevelError, QuestRequirementsNotMetError
- File errors: SaveFileCorruptedError, InvalidSaveDataError, MissingDataFileError

## Design Choices

**Save files** - Used simple KEY: VALUE format because it's easy to read and debug

**Leveling** - XP needed = current_level \* 100. Simple formula that's easy to calculate

**Combat** - Turn-based with damage = attacker strength - (defender strength // 4). Minimum 1 damage

**Inventory** - 20 slot limit to make inventory management matter

## How to Play

1. Run `python main.py`
2. Choose New Game or Load Game
3. Pick a class: Warrior (high strength), Mage (high magic), Rogue (balanced), Cleric (balanced + healing)
4. Use game menu to view stats, manage inventory, do quests, explore for battles, or visit shop
5. Complete quests and defeat enemies to level up
6. Save and quit when done

## Classes and Special Abilities

- **Warrior**: Power Strike - 2x strength damage
- **Mage**: Fireball - 2x magic damage
- **Rogue**: Critical Strike - 50% chance for 3x damage
- **Cleric**: Heal - restore 30 HP

## Testing

Run with: `python -m pytest tests/`

All integration tests pass.

```

```
