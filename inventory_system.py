"""
COMP 163 - Project 3: Quest Chronicles
Inventory System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles inventory management, item usage, and equipment.
"""

from custom_exceptions import (
    InventoryFullError,
    ItemNotFoundError,
    InsufficientResourcesError,
    InvalidItemTypeError
)

# Maximum inventory size
MAX_INVENTORY_SIZE = 20

# ============================================================================
# INVENTORY MANAGEMENT
# ============================================================================
def ensure_character_keys(character):
    """
    Ensure the character dictionary has all required keys
    for inventory, equipment, and game_data.
    """
    if "inventory" not in character:
        character["inventory"] = []
    if "equipped_weapon" not in character:
        character["equipped_weapon"] = None
    if "equipped_armor" not in character:
        character["equipped_armor"] = None
    if "gold" not in character:
        character["gold"] = 0
    if "health" not in character:
        character["health"] = 100
    if "max_health" not in character:
        character["max_health"] = 100
    if "strength" not in character:
        character["strength"] = 10
    if "magic" not in character:
        character["magic"] = 10
    if "game_data" not in character:
        character["game_data"] = {"items": {}}


def add_item_to_inventory(character, item_id):
    """
    Add an item to character's inventory
    
    Args:
        character: Character dictionary
        item_id: Unique item identifier
    
    Returns: True if added successfully
    Raises: InventoryFullError if inventory is at max capacity
    """
    if len(character['inventory']) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Cannot add item: Inventory is full.")
    character['inventory'].append(item_id)
    return True
    # TODO: Implement adding items
    # Check if inventory is full (>= MAX_INVENTORY_SIZE)
    # Add item_id to character['inventory'] list
    

def remove_item_from_inventory(character, item_id):
    """
    Remove an item from character's inventory
    
    Args:
        character: Character dictionary
        item_id: Item to remove
    
    Returns: True if removed successfully
    Raises: ItemNotFoundError if item not in inventory
    """
    if item_id not in character['inventory']:
        raise ItemNotFoundError(f"Item {item_id} not found in inventory.")
    character['inventory'].remove(item_id)
    return True
    # TODO: Implement item removal
    # Check if item exists in inventory
    # Remove item from list
    

def has_item(character, item_id):
    """
    Check if character has a specific item
    
    Returns: True if item in inventory, False otherwise
    """
    if item_id in character['inventory']:
        return True
    return False
    # TODO: Implement item check
    

def count_item(character, item_id):
    """
    Count how many of a specific item the character has
    
    Returns: Integer count of item
    """
    return character['inventory'].count(item_id)
    # TODO: Implement item counting
    # Use list.count() method
    

def get_inventory_space_remaining(character):
    """
    Calculate how many more items can fit in inventory
    
    Returns: Integer representing available slots
    """
    if MAX_INVENTORY_SIZE - len(character['inventory']) >= 0:
        return MAX_INVENTORY_SIZE - len(character['inventory'])
    else:
        return 0
    # TODO: Implement space calculation
    

def clear_inventory(character):
    """
    Remove all items from inventory
    
    Returns: List of removed items
    """
    removed_items = character['inventory']
    character['inventory'] = []
    return removed_items
    # TODO: Implement inventory clearing
    # Save current inventory before clearing
    # Clear character's inventory list
    

# ============================================================================
# ITEM USAGE
# ============================================================================

def use_item(character, item_id, item_data):
    """
    Use a consumable item from inventory
    
    Args:
        character: Character dictionary
        item_id: Item to use
        item_data: Item information dictionary from game_data
    
    Item types and effects:
    - consumable: Apply effect and remove from inventory
    - weapon/armor: Cannot be "used", only equipped
    
    Returns: String describing what happened
    Raises: 
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'consumable'
    """
    if item_id not in character['inventory']:
        raise ItemNotFoundError(f"Item {item_id} not found in inventory.")
    if item_data['type'] != 'consumable':
        raise InvalidItemTypeError(f"Item {item_id} is not a consumable.")
    stat_name, value = parse_item_effect(item_data['effect'])
    apply_stat_effect(character, stat_name, value)
    remove_item_from_inventory(character, item_id)
    
    # Use item name if available, otherwise use item_id
    item_name = item_data.get('name', item_id)
    return f"Used {item_name}, {stat_name} increased by {value}."
    
    # TODO: Implement item usage
    # Check if character has the item
    # Check if item type is 'consumable'
    # Parse effect (format: "stat_name:value" e.g., "health:20")
    # Apply effect to character
    # Remove item from inventory
    

def equip_weapon(character, item_id, item_data):
    """
    Equip a weapon
    
    Args:
        character: Character dictionary
        item_id: Weapon to equip
        item_data: Item information dictionary
    
    Weapon effect format: "strength:5" (adds 5 to strength)
    
    If character already has weapon equipped:
    - Unequip current weapon (remove bonus)
    - Add old weapon back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'weapon'
    """
    ensure_character_keys(character)  # Ensure character has equipment keys
    
    if item_id not in character["inventory"]:
        raise ItemNotFoundError(f"Item {item_id} not found in inventory.")
    if item_data["type"] != "weapon":
        raise InvalidItemTypeError(f"Item {item_id} is not a weapon.")
    
    # Unequip old weapon
    if character["equipped_weapon"] is not None:
        old_weapon_id = unequip_weapon(character)
        add_item_to_inventory(character, old_weapon_id)
    
    # Apply new weapon bonus
    stat_name, value = parse_item_effect(item_data["effect"])
    character[stat_name] += value
    
    # Equip it
    character["equipped_weapon"] = item_id
    remove_item_from_inventory(character, item_id)
    
    # Use item name if available, otherwise use item_id
    item_name = item_data.get('name', item_id)
    return f"Equipped {item_name}, {stat_name} increased by {value}."
    
    # TODO: Implement weapon equipping
    # Check item exists and is type 'weapon'
    # Handle unequipping current weapon if exists
    # Parse effect and apply to character stats
    # Store equipped_weapon in character dictionary
    # Remove item from inventory
    

def equip_armor(character, item_id, item_data):
    """
    Equip armor
    
    Args:
        character: Character dictionary
        item_id: Armor to equip
        item_data: Item information dictionary
    
    Armor effect format: "max_health:10" (adds 10 to max_health)
    
    If character already has armor equipped:
    - Unequip current armor (remove bonus)
    - Add old armor back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'armor'
    """
    ensure_character_keys(character)  # Ensure character has equipment keys
    
    if item_id not in character["inventory"]:
        raise ItemNotFoundError(f"Item {item_id} not found in inventory.")
    if item_data["type"] != "armor":
        raise InvalidItemTypeError(f"Item {item_id} is not armor.")
    
    # Unequip old armor
    if character["equipped_armor"] is not None:
        old_armor_id = unequip_armor(character)
        add_item_to_inventory(character, old_armor_id)
    
    # Apply new armor bonus
    stat_name, value = parse_item_effect(item_data["effect"])
    character[stat_name] += value
    
    # Equip it
    character["equipped_armor"] = item_id
    remove_item_from_inventory(character, item_id)
    
    # Use item name if available, otherwise use item_id
    item_name = item_data.get('name', item_id)
    return f"Equipped {item_name}, {stat_name} increased by {value}."
    # TODO: Implement armor equipping
    # Similar to equip_weapon but for armor
    

def unequip_weapon(character):
    """
    Remove equipped weapon and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no weapon equipped
    Raises: InventoryFullError if inventory is full
    """
    weapon_id = character["equipped_weapon"]
    if weapon_id is None:
        return None

    # Inventory full?
    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Cannot unequip weapon: Inventory is full.")

    # Remove stat bonus
    weapon_data = character["game_data"]["items"][weapon_id]
    stat, val = parse_item_effect(weapon_data["effect"])
    character[stat] -= val

    # Unequip it
    character["equipped_weapon"] = None
    return weapon_id
    
    # TODO: Implement weapon unequipping
    # Check if weapon is equipped
    # Remove stat bonuses
    # Add weapon back to inventory
    # Clear equipped_weapon from character
    

def unequip_armor(character):
    """
    Remove equipped armor and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no armor equipped
    Raises: InventoryFullError if inventory is full
    """
    armor_id = character["equipped_armor"]
    if armor_id is None:
        return None

    if len(character["inventory"]) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Cannot unequip armor: Inventory is full.")

    # Remove stat bonus
    armor_data = character["game_data"]["items"][armor_id]
    stat, val = parse_item_effect(armor_data["effect"])
    character[stat] -= val

    character["equipped_armor"] = None
    return armor_id
    # TODO: Implement armor unequipping
    

# ============================================================================
# SHOP SYSTEM
# ============================================================================

def purchase_item(character, item_id, item_data):
    """
    Purchase an item from a shop
    
    Args:
        character: Character dictionary
        item_id: Item to purchase
        item_data: Item information with 'cost' field
    
    Returns: True if purchased successfully
    Raises:
        InsufficientResourcesError if not enough gold
        InventoryFullError if inventory is full
    """
    if character['gold'] < item_data['cost']:
        raise InsufficientResourcesError("Not enough gold to purchase item.")
    if len(character['inventory']) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Cannot purchase item: Inventory is full.")
    character['gold'] -= item_data['cost']
    character['inventory'].append(item_id)
    return True
    # TODO: Implement purchasing
    # Check if character has enough gold
    # Check if inventory has space
    # Subtract gold from character
    # Add item to inventory
    

def sell_item(character, item_id, item_data):
    """
    Sell an item for half its purchase cost
    
    Args:
        character: Character dictionary
        item_id: Item to sell
        item_data: Item information with 'cost' field
    
    Returns: Amount of gold received
    Raises: ItemNotFoundError if item not in inventory
    """
    if item_id not in character['inventory']:
        raise ItemNotFoundError(f"Item {item_id} not found in inventory.")
    
    sell_price = item_data['cost'] // 2
    remove_item_from_inventory(character, item_id)
    character['gold'] += sell_price
    return sell_price
    # TODO: Implement selling
    # Check if character has item
    # Calculate sell price (cost // 2)
    # Remove item from inventory
    # Add gold to character
    

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_item_effect(effect_string):
    """
    Parse item effect string into stat name and value
    
    Args:
        effect_string: String in format "stat_name:value"
    
    Returns: Tuple of (stat_name, value)
    Example: "health:20" → ("health", 20)
    """
    parts = effect_string.split(":")
    return parts[0], int(parts[1])
    # TODO: Implement effect parsing
    # Split on ":"
    # Convert value to integer
    

def apply_stat_effect(character, stat_name, value):
    """
    Apply a stat modification to character
    
    Valid stats: health, max_health, strength, magic
    
    Note: health cannot exceed max_health
    """
    character[stat_name] += value
    if stat_name == "health" and character["health"] > character["max_health"]:
        character["health"] = character["max_health"]
    

    # TODO: Implement stat application
    # Add value to character[stat_name]
    # If stat is health, ensure it doesn't exceed max_health
    

def display_inventory(character, item_data_dict):
    """
    Display character's inventory in formatted way
    
    Args:
        character: Character dictionary
        item_data_dict: Dictionary of all item data
    
    Shows item names, types, and quantities
    """
  
    lines = ["=== INVENTORY ==="]

    # Count how many of each item
    counts = {}
    for item_id in character["inventory"]:
        if item_id in counts:
            counts[item_id] += 1
        else:
            counts[item_id] = 1

    # Empty inventory
    if len(counts) == 0:
        lines.append("Inventory is empty.")
        return "\n".join(lines)

    # Build display for each item
    for item_id in counts:
        if item_id in item_data_dict:
            item_info = item_data_dict[item_id]

            if "name" in item_info:
                name = item_info["name"]
            else:
                name = item_id

            if "type" in item_info:
                item_type = item_info["type"]
            else:
                item_type = "Unknown"
        else:
            # item not found in data file
            name = item_id
            item_type = "Unknown"

        qty = counts[item_id]
        lines.append(f"{name} (Type: {item_type}) x{qty}")

    return "\n".join(lines)

    
    # TODO: Implement inventory display
    # Count items (some may appear multiple times)
    # Display with item names from item_data_dict
    

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== INVENTORY SYSTEM TEST ===")
    
    # Test adding items
    # test_char = {'inventory': [], 'gold': 100, 'health': 80, 'max_health': 80}
    # 
    # try:
    #     add_item_to_inventory(test_char, "health_potion")
    #     print(f"Inventory: {test_char['inventory']}")
    # except InventoryFullError:
    #     print("Inventory is full!")
    
    # Test using items
    # test_item = {
    #     'item_id': 'health_potion',
    #     'type': 'consumable',
    #     'effect': 'health:20'
    # }
    # 
    # try:
    #     result = use_item(test_char, "health_potion", test_item)
    #     print(result)
    # except ItemNotFoundError:
    #     print("Item not found")

