# =============================================================================
# CAESAR CIPHER WORKSHOP
# =============================================================================
# A complete implementation of the Caesar cipher encryption/decryption algorithm.
# The Caesar cipher shifts each letter in the text by a fixed number of positions
# in the alphabet. For example, with shift=3: A→D, B→E, C→F, etc.
#
# This implementation:
# - Handles both uppercase and lowercase letters
# - Preserves non-alphabetic characters (spaces, punctuation)
# - Uses modulo arithmetic to wrap any shift value
# - Provides both encryption and decryption functions
# =============================================================================

# Define the alphabet as a constant for reusability
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def caesar(text, shift, encrypt=True):
    """
    Encrypt or decrypt text using the Caesar cipher algorithm.

    The Caesar cipher works by shifting each letter in the alphabet by
    a fixed number of positions. For encryption, we shift forward; for
    decryption, we shift backward.

    Args:
        text (str): The message to process
        shift (int): Number of positions to shift (can be any integer)
        encrypt (bool): True to encrypt, False to decrypt (default: True)

    Returns:
        str: The processed text

    Raises:
        TypeError: If shift is not an integer

    Example:
        >>> caesar("Hello", 3)
        'Khoor'
        >>> caesar("Khoor", 3, encrypt=False)
        'Hello'
    """
    # Validate that shift is an integer
    if not isinstance(shift, int):
        raise TypeError('Shift must be an integer value.')

    # Use modulo to wrap any shift value to 0-25 range
    # This allows shift=27 to become 1, shift=52 to become 0, etc.
    shift = shift % 26

    # For decryption, reverse the shift direction
    if not encrypt:
        shift = -shift

    # Create the shifted alphabet by slicing and concatenating
    # Example: shift=3 → 'defghijklmnopqrstuvwxyzabc'
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]

    # Create a translation table that maps each character to its shifted version
    # Handles both lowercase and uppercase letters
    translation_table = str.maketrans(
        ALPHABET + ALPHABET.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply the translation to the text (preserves non-alphabetic characters)
    processed_text = text.translate(translation_table)

    return processed_text


def encrypt(text, shift):
    """
    Convenience function to encrypt text using Caesar cipher.

    Args:
        text (str): The message to encrypt
        shift (int): Number of positions to shift

    Returns:
        str: The encrypted text
    """
    return caesar(text, shift)


def decrypt(text, shift):
    """
    Convenience function to decrypt text using Caesar cipher.

    Args:
        text (str): The encrypted message to decrypt
        shift (int): Number of positions to shift (same as used for encryption)

    Returns:
        str: The decrypted text
    """
    return caesar(text, shift, encrypt=False)


# Main guard: This code only runs when the file is executed directly,
# not when it's imported as a module by another script
if __name__ == '__main__':
    # Example: Decrypt a ROT13 cipher (shift=13)
    # ROT13 is a special case where encrypt and decrypt use the same shift
    encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
    decrypted_text = decrypt(encrypted_text, 13)

    print(f'Encrypted Text: {encrypted_text}')
    print(f'Decrypted Text: {decrypted_text}')
