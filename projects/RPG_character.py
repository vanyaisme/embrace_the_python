# =============================================================================
# RPG CHARACTER CREATOR
# =============================================================================
# A character creation system for role-playing games with full input validation.
# This implementation:
# - Validates character names (type, length, format)
# - Validates stat values (type, range, total points)
# - Creates a visual character sheet with dot-based stat bars
# - Follows PEP 8 style guidelines and best practices
# =============================================================================

# Constants for character creation rules
FULL_DOT = '●'              # Symbol for filled stat points
EMPTY_DOT = '○'             # Symbol for empty stat points
MAX_NAME_LENGTH = 10        # Maximum characters allowed in name
MIN_STAT = 1                # Minimum value for any stat
MAX_STAT = 4                # Maximum value for any stat
TOTAL_STAT_POINTS = 7       # Total points that must be distributed across all stats


def create_character(name, strength, intelligence, charisma):
    """
    Create an RPG character with name and stats.

    Validates all inputs and returns a formatted character sheet if valid,
    or an error message if any validation fails.

    Args:
        name (str): Character name (max 10 chars, no spaces)
        strength (int): Strength stat (1-4)
        intelligence (int): Intelligence stat (1-4)
        charisma (int): Charisma stat (1-4)

    Returns:
        str: Formatted character sheet with visual stat bars, or error message

    Example:
        >>> create_character('ren', 4, 2, 1)
        'ren\\nSTR ●●●●○○○○○○\\nINT ●●○○○○○○○○\\nCHA ●○○○○○○○○○'
    """

    # === NAME VALIDATION ===
    # Check if name is a string (not int, float, list, etc.)
    if not isinstance(name, str):
        return 'The character name should be a string'

    # Check if name is not empty
    if len(name) == 0:
        return 'The character should have a name'

    # Check if name exceeds maximum length
    if len(name) > MAX_NAME_LENGTH:
        return 'The character name is too long'

    # Check if name contains spaces (single-word names only)
    if ' ' in name:
        return 'The character name should not contain spaces'

    # === STAT VALIDATION ===
    # Group all stats into a list for easier validation
    stats = [strength, intelligence, charisma]

    # Check if all stats are integers (not strings, floats, etc.)
    # all() returns True only if ALL items satisfy the condition
    if not all(isinstance(stat, int) for stat in stats):
        return 'All stats should be integers'

    # Check if any stat is below minimum value
    # any() returns True if AT LEAST ONE item satisfies the condition
    if any(stat < MIN_STAT for stat in stats):
        return 'All stats should be no less than 1'

    # Check if any stat exceeds maximum value
    if any(stat > MAX_STAT for stat in stats):
        return 'All stats should be no more than 4'

    # Check if total points equals exactly 7 (game balance requirement)
    if sum(stats) != TOTAL_STAT_POINTS:
        return 'The character should start with 7 points'

    # === CHARACTER SHEET GENERATION ===
    # Helper function to create visual stat bars
    def format_stat_line(stat_name, stat_value, max_dots=10):
        """
        Create a visual stat line with filled and empty dots.

        Args:
            stat_name (str): Abbreviation of the stat (e.g., 'STR', 'INT')
            stat_value (int): Current value of the stat
            max_dots (int): Total number of dots to display (default: 10)

        Returns:
            str: Formatted stat line (e.g., 'STR ●●●●○○○○○○')
        """
        # Create filled dots for the stat value, then fill remaining with empty dots
        return f'{stat_name} {FULL_DOT * stat_value + EMPTY_DOT * (max_dots - stat_value)}'

    # Build and return the complete character sheet
    # Multi-line f-string creates clean, properly formatted output
    return f"""{name}
{format_stat_line("STR", strength)}
{format_stat_line("INT", intelligence)}
{format_stat_line("CHA", charisma)}"""


# Main guard: Code below only runs when file is executed directly
# Not when imported as a module
if __name__ == '__main__':
    # Example: Create a character named 'ren' with stats 4, 2, 1
    print(create_character('ren', 4, 2, 1))
