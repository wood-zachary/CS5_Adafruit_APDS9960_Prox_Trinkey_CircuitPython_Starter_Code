from .symbols import MORSE_SYMBOL_TO_LETTER, InvalidSymbolError


def append_morse_symbol(message: str, symbol: str) -> str:
    """
    Decodes a Morse code symbol and appends the corresponding character to the 
    message.

    Args:
        message (str): current message string being built.
        symbol (str): morse code symbol to be translated 
        (e.g., ".-", ".----", "del").

    Returns:
        str: The updated message with the translated symbol appended, or with
        the last character removed if the symbol is "del".

    Raises:
        InvalidSymbolError: If the symbol is not a valid Morse code character.
    """
    # Your Code Here!
    raise InvalidSymbolError()


def translate_message(morse: str) -> str:
    """
    Translates a Morse code message into an English string.

    Args:
        morse (str): A series of Morse code symbols separated by "/". Each 
        symbol can represent a letter, number, or space.

    Returns:
        str: The translated English message. If any invalid symbols are 
        encountered, they are ignored. If the last potential symbol is not 
        valid, it is appended as is (i.e., as dots and dashes).
    """
    # Your Code Here!