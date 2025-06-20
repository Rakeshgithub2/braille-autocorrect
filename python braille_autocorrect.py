import difflib

# Braille QWERTY mapping (dot number -> QWERTY key)
key_to_dot = {
    'D': 1, 'W': 2, 'Q': 3,
    'K': 4, 'O': 5, 'P': 6
}

# Braille representation (dot positions) for a-z
braille_dict = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6],
}

# Create a reverse dictionary: dot pattern -> character
dot_to_char = {tuple(sorted(v)): k for k, v in braille_dict.items()}

# Dictionary of valid words (can expand this list)
word_list = ["hello", "help", "helicopter", "hero", "habit", "honey", "good", "go", "gone", "gift", "giraffe"]

def qwerty_to_dots(qwerty_keys):
    return sorted([key_to_dot.get(k.upper(), 0) for k in qwerty_keys if k.upper() in key_to_dot])

def convert_input_to_text(qwerty_braille_input):
    # Each letter is typed as keys pressed together, separated by space
    letters = qwerty_braille_input.strip().split(" ")
    result = ""
    for l in letters:
        dots = tuple(sorted([key_to_dot.get(c.upper(), 0) for c in l if c.upper() in key_to_dot]))
        result += dot_to_char.get(dots, "?")  # ? = unknown character
    return result

def suggest_words(input_word, dictionary):
    suggestions = difflib.get_close_matches(input_word, dictionary, n=3, cutoff=0.5)
    return suggestions

def main():
    print("Enter Braille (QWERTY Braille format, each letter separated by space):")
    print("Example for 'hello': DW DO DK DK KO")
    user_input = input("> ").strip()
    interpreted = convert_input_to_text(user_input)
    print(f"\nInterpreted Word: {interpreted}")

    suggestions = suggest_words(interpreted, word_list)
    if suggestions:
        print("Did you mean:")
        for s in suggestions:
            print(" -", s)
    else:
        print("No suggestions found.")

if __name__ == "__main__":
    main()
