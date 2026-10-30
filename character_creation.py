def create_character(name, strength, intelligence, charisma):
    # 1. Name validation
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."
        
    # 2. Stats validation
    stats = [strength, intelligence, charisma]
    
    for stat in stats:
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers."
            
    for stat in stats:
        if stat < 1:
            return "All stats should be no less than 1."
            
    for stat in stats:
        if stat > 4:
            return "All stats should be no more than 4."
            
    if sum(stats) != 7:
        return "The character should start with 7 points."
        
    # 3. Formatting the output string
    str_dots = "●" * strength + "○" * (10 - strength)
    int_dots = "●" * intelligence + "○" * (10 - intelligence)
    cha_dots = "●" * charisma + "○" * (10 - charisma)
    
    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"


# --- Interactive Input for VS Code ---
if __name__ == "__main__":
    print("--- RPG Character Creator ---")
    name_input = input("Enter character name (max 10 chars, no spaces): ")
    
    try:
        # input() returns text, so we wrap it in int() to convert it to a number
        str_input = int(input("Enter Strength (1 to 4): "))
        int_input = int(input("Enter Intelligence (1 to 4): "))
        cha_input = int(input("Enter Charisma (1 to 4): "))
        
        print("\n--- Result ---")
        result = create_character(name_input, str_input, int_input, cha_input)
        print(result)
        
    except ValueError:
        print("\nError: Stats must be numbers (integers)!")