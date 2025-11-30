"""
COMP 163 - Project 3: Quest Chronicles
Quest Handler Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles quest management, dependencies, and completion.
"""

from custom_exceptions import (
    QuestNotFoundError,
    QuestRequirementsNotMetError,
    QuestAlreadyCompletedError,
    QuestNotActiveError,
    InsufficientLevelError
)

# ============================================================================
# QUEST MANAGEMENT
# ============================================================================

def accept_quest(character, quest_id, quest_data_dict):
    """
    Accept a new quest
    
    Args:
        character: Character dictionary
        quest_id: Quest to accept
        quest_data_dict: Dictionary of all quest data
    
    Requirements to accept quest:
    - Character level >= quest required_level
    - Prerequisite quest completed (if any)
    - Quest not already completed
    - Quest not already active
    
    Returns: True if quest accepted
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        InsufficientLevelError if character level too low
        QuestRequirementsNotMetError if prerequisite not completed
        QuestAlreadyCompletedError if quest already done
    """
    #check if quest exists
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' not found.")
    
    #Gives access to quest_data_dict[quest_id] and checks requirements
    if character['level'] < quest_data_dict[quest_id]['required_level']:
        raise InsufficientLevelError(f"Level {quest_data_dict[quest_id]['required_level']} required to accept this quest.")
    #check prerequisite
    if quest_data_dict[quest_id]['prerequisite'] != "NONE":
        prereq = quest_data_dict[quest_id]['prerequisite']
        if prereq not in character['completed_quests']:
            raise QuestRequirementsNotMetError(f"Prerequisite quest '{prereq}' not completed.")
    
    #check if quest already completed
    if quest_id in character['completed_quests']:
        raise QuestAlreadyCompletedError(f"Quest '{quest_id}' has already been completed.")
    #check if quest already active
    if quest_id not in character['active_quests']:
        character['active_quests'].append(quest_id)
        return True
    

    # TODO: Implement quest acceptance
    # Check quest exists
    # Check level requirement
    # Check prerequisite (if not "NONE")
    # Check not already completed
    # Check not already active
    # Add to character['active_quests']
    

def complete_quest(character, quest_id, quest_data_dict):
    """
    Complete an active quest and grant rewards
    
    Args:
        character: Character dictionary
        quest_id: Quest to complete
        quest_data_dict: Dictionary of all quest data
    
    Rewards:
    - Experience points (reward_xp)
    - Gold (reward_gold)
    
    Returns: Dictionary with reward information
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        QuestNotActiveError if quest not in active_quests
    """
    #check if quest exists
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' not found.")
    #check if quest is active
    if quest_id not in character['active_quests']:
        raise QuestNotActiveError(f"Quest '{quest_id}' is not active and cannot be completed.")
    #If it does exist and is active, complete it and grant rewards
    character['active_quests'].remove(quest_id)
    character['completed_quests'].append(quest_id)
    reward_xp = quest_data_dict[quest_id]['reward_xp']
    reward_gold = quest_data_dict[quest_id]['reward_gold']
    character['experience'] += reward_xp
    character['gold'] += reward_gold
    return {'reward_xp': reward_xp, 'reward_gold': reward_gold}
    # TODO: Implement quest completion
    # Check quest exists
    # Check quest is active
    # Remove from active_quests
    # Add to completed_quests
    # Grant rewards (use character_manager.gain_experience and add_gold)
    # Return reward summary
    

def abandon_quest(character, quest_id):
    """
    Remove a quest from active quests without completing it
    
    Returns: True if abandoned
    Raises: QuestNotActiveError if quest not active
    """
    if quest_id not in character['active_quests']:
        raise QuestNotActiveError(f"Quest '{quest_id}' is not active and cannot be abandoned.")
    else:
        character['active_quests'].remove(quest_id)
        return True
    # TODO: Implement quest abandonment
    

def get_active_quests(character, quest_data_dict):
    """
    Get full data for all active quests
    
    Returns: List of quest dictionaries for active quests
    """
    #returns list of active quests
    #qid is quest id
    active_quests = [quest_data_dict[qid] for qid in character['active_quests']]
    return active_quests

    # TODO: Implement active quest retrieval
    # Look up each quest_id in character['active_quests']
    # Return list of full quest data dictionaries
    

def get_completed_quests(character, quest_data_dict):
    """
    Get full data for all completed quests
    
    Returns: List of quest dictionaries for completed quests
    """
    completed_quests = [quest_data_dict[qid] for qid in character['completed_quests']]
    return completed_quests
    # TODO: Implement completed quest retrieval
    

def get_available_quests(character, quest_data_dict):
    """
    Get quests that character can currently accept
    
    Available = meets level req + prerequisite done + not completed + not active
    
    Returns: List of quest dictionaries
    """

    #returns list of available quests and checks if player can accept 
    available_quests = []
    for quest_id, quest_data in quest_data_dict.items():
        if can_accept_quest(character, quest_id, quest_data_dict):
            #if available, add to list
            available_quests.append(quest_data)

    return available_quests

    # TODO: Implement available quest search
    # Filter all quests by requirements
    

# ============================================================================
# QUEST TRACKING
# ============================================================================

def is_quest_completed(character, quest_id):
    """
    Check if a specific quest has been completed
    
    Returns: True if completed, False otherwise
    """

    if quest_id in character['completed_quests']:
        return True

    # TODO: Implement completion check
    

def is_quest_active(character, quest_id):
    """
    Check if a specific quest is currently active
    
    Returns: True if active, False otherwise
    """

    if quest_id in character['active_quests']:
        return True

    # TODO: Implement active check
    

def can_accept_quest(character, quest_id, quest_data_dict):
    """
    Check if character meets all requirements to accept quest
    
    Returns: True if can accept, False otherwise
    Does NOT raise exceptions - just returns boolean
    """

    if quest_id not in quest_data_dict:
        return False
    quest = quest_data_dict[quest_id]
    if character['level'] < quest['required_level']:
        return False

    # TODO: Implement requirement checking
    # Check all requirements without raising exceptions
    

def get_quest_prerequisite_chain(quest_id, quest_data_dict):
    """
    Get the full chain of prerequisites for a quest
    
    Returns: List of quest IDs in order [earliest_prereq, ..., quest_id]
    Example: If Quest C requires Quest B, which requires Quest A:
             Returns ["quest_a", "quest_b", "quest_c"]
    
    Raises: QuestNotFoundError if quest doesn't exist
    """
    #check if quest exists
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' not found.")
    else:
        #trace prerequisite chain
        chain = []
        current_quest_id = quest_id
        while current_quest_id != "NONE":
            #insert at start of list to build in correct order
            chain.insert(0, current_quest_id)
            current_quest_id = quest_data_dict[current_quest_id]['prerequisite']
        return chain

    # TODO: Implement prerequisite chain tracing
    # Follow prerequisite links backwards
    # Build list in reverse order
    

# ============================================================================
# QUEST STATISTICS
# ============================================================================

def get_quest_completion_percentage(character, quest_data_dict):
    """
    Calculate what percentage of all quests have been completed
    
    Returns: Float between 0 and 100
    """
    #Does the math for percentage completed
    completed = len(character['completed_quests'])
    total = len(quest_data_dict)
    if total == 0:
        return 0.0
    else:
        return (completed / total) * 100
    

    # TODO: Implement percentage calculation
    # total_quests = len(quest_data_dict)
    # completed_quests = len(character['completed_quests'])
    # percentage = (completed / total) * 100
    

def get_total_quest_rewards_earned(character, quest_data_dict):
    """
    Calculate total XP and gold earned from completed quests
    
    Returns: Dictionary with 'total_xp' and 'total_gold'
    """
    #Does the math for total quest completed rewards
    reward_dict = {'total_xp': 0, 'total_gold': 0}
    for quest_id in character['completed_quests']:
        quest = quest_data_dict[quest_id]
        reward_dict['total_xp'] += quest['reward_xp']
        reward_dict['total_gold'] += quest['reward_gold']

    # TODO: Implement reward calculation
    # Sum up reward_xp and reward_gold for all completed quests
    

def get_quests_by_level(quest_data_dict, min_level, max_level):
    """
    Get all quests within a level range
    
    Returns: List of quest dictionaries
    """
    #Creates a dict for filtered quests
    filtered_quests = []
    for quest in quest_data_dict.values():
        if min_level <= quest['required_level'] <= max_level:
            #Checks if able to get put into that dict then if able it gets added
            filtered_quests.append(quest)

    # TODO: Implement level filtering
    

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_quest_info(quest_data):
    """
    Display formatted quest information
    
    Shows: Title, Description, Rewards, Requirements
    """
    # TODO: Implement quest display
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    print(f"Required Level: {quest_data['required_level']}")
    print(f"Prerequisite: {quest_data['prerequisite']}")
    print(f"Rewards: {quest_data['reward_xp']} XP, {quest_data['reward_gold']} Gold")
    # ... etc

def display_quest_list(quest_list):
    """
    Display a list of quests in summary format
    
    Shows: Title, Required Level, Rewards
    """

    for quest in quest_list:
        print(f"- {quest['title']} (Level {quest['required_level']}): {quest['reward_xp']} XP, {quest['reward_gold']} Gold")

    # TODO: Implement quest list display
    

def display_character_quest_progress(character, quest_data_dict):
    """
    Display character's quest statistics and progress
    
    Shows:
    - Active quests count
    - Completed quests count
    - Completion percentage
    - Total rewards earned
    """

    active_count = len(character['active_quests'])
    completed_count = len(character['completed_quests'])
    completion_percentage = get_quest_completion_percentage(character, quest_data_dict)
    total_rewards = get_total_quest_rewards_earned(character, quest_data_dict)

    print(f"Active Quests: {active_count}")
    print(f"Completed Quests: {completed_count}")
    print(f"Completion Percentage: {completion_percentage:.2f}%")
    print(f"Total XP Earned: {total_rewards['total_xp']}")
    print(f"Total Gold Earned: {total_rewards['total_gold']}")

    # TODO: Implement progress display
    

# ============================================================================
# VALIDATION
# ============================================================================

def validate_quest_prerequisites(quest_data_dict):
    """
    Validate that all quest prerequisites exist
    
    Checks that every prerequisite (that's not "NONE") refers to a real quest
    
    Returns: True if all valid
    Raises: QuestNotFoundError if invalid prerequisite found
    """


    for quest_id, quest_data in quest_data_dict.items():
        prereq = quest_data['prerequisite']
        if prereq != "NONE" and prereq not in quest_data_dict:
            raise QuestNotFoundError(f"Quest '{quest_id}' has invalid prerequisite '{prereq}'.")
    return True


    # TODO: Implement prerequisite validation
    # Check each quest's prerequisite
    # Ensure prerequisite exists in quest_data_dict
    


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEST HANDLER TEST ===")
    
    # Test data
    # test_char = {
    #     'level': 1,
    #     'active_quests': [],
    #     'completed_quests': [],
    #     'experience': 0,
    #     'gold': 100
    # }
    #
    # test_quests = {
    #     'first_quest': {
    #         'quest_id': 'first_quest',
    #         'title': 'First Steps',
    #         'description': 'Complete your first quest',
    #         'reward_xp': 50,
    #         'reward_gold': 25,
    #         'required_level': 1,
    #         'prerequisite': 'NONE'
    #     }
    # }
    #
    # try:
    #     accept_quest(test_char, 'first_quest', test_quests)
    #     print("Quest accepted!")
    # except QuestRequirementsNotMetError as e:
    #     print(f"Cannot accept: {e}")

