# Exercise_86
# Luong Hoang Quan; 20203850
# Purpose: displays the complete lyrics for The Twelve Days of Christmas

def ordinal_number(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

# Function to display a verse of the song
def display_verse(verse_number):
    ordinal = ordinal_number(verse_number)
    print(f"On the {ordinal} day of Christmas")
    print("my true love sent to me:")
    
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]
    
    # Display the gifts in reverse order for the current verse
    for i in range(verse_number - 1, -1, -1):
        print(gifts[i])

    print()  # Empty line after the verse

# Display all 12 verses of the song
def main():
    for i in range(1, 13):
        display_verse(i)

if __name__ == "__main__":
    main()
