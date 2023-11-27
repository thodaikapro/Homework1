# Exercise_89
# Luong Hoang Quan; 20203850
# Purpose: write a function that capitalizes the appropriate characters in a string


def capitalize_string(sentence):
    words = sentence.split()
    capitalized_words = []

    capitalize_next = True  # Flag to indicate whether the next word should be capitalized

    for word in words:
        if capitalize_next:
            word = word.capitalize()
            capitalize_next = False

        # Capitalize the first non-space character after '.', '!', or '?'
        if word.endswith('.') or word.endswith('!') or word.endswith('?'):
            capitalize_next = True

        capitalized_words.append(word)

    return ' '.join(capitalized_words)

def main():
    user_input = input("Enter a sentence: ")
    capitalized_result = capitalize_string(user_input)
    print(capitalized_result)

if __name__ == "__main__":
    main()