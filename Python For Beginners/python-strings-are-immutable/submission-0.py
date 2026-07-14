def remove_fourth_character(word: str) -> str:
    first_three_character = word[:3]
    remaining_characters = word[4:]
    result_string = first_three_character + remaining_characters
    return result_string


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
