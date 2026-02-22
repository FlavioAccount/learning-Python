# Hangman in python
import random
long_words = [
"absolutely", "acceptable", "accessible", "accidental", "accomplish", "accountable",
"acquisition", "adaptation", "additional", "adolescence", "advantageous", "adventurous",
"affectionate", "aggression", "agriculture", "alliance", "alteration", "ambassador",
"amendments", "ammunition", "analytical", "anniversary", "anticipation", "apartment",
"appearance", "applicable", "appointment", "appreciate", "appropriate", "architecture",
"argumentative", "artificial", "association", "atmosphere", "attachment", "attendance",
"attraction", "authority", "automatic", "background", "bachelor", "bacteria",
"battleground", "beautifully", "believable", "beneficial", "biography", "bilingual",
"borderline", "boundaries", "breakfast", "brightness", "broadcast", "brotherhood",
"calculation", "campaigner", "cancellation", "capabilities", "capitalism", "categorical",
"celebration", "certificate", "challenging", "character", "charitable", "chemistry",
"childhood", "circumstance", "citizenship", "civilization", "clarification", "classification",
"climatic", "collection", "combination", "comfortable", "committee", "communication",
"comparison", "compensation", "competition", "complimentary", "composition", "comprehensive",
"concentration", "conceptual", "conclusion", "condition", "conference", "confidence",
"consequence", "consideration", "consistent", "constellation", "construction", "consultation",
"consumption", "containment", "contemporary", "contentment", "continuation", "contribution",
"controversial", "conversation", "cooperation", "coordination", "correction", "corruption",
"creativity", "criticism", "cultural", "curiosity", "curriculum", "customary",
"dangerous", "database", "dedication", "definition", "delegation", "democratic",
"dependable", "description", "destruction", "determination", "development", "dictionary",
"disagreement", "disciplinary", "discussion", "discovery", "discrimination", "distribution",
"distinction", "distinguished", "diversity", "documentary", "donations", "education",
"effectiveness", "efficiency", "electrical", "electricity", "elimination", "emotional",
"empowerment", "encouragement", "endorsement", "engineering", "entertainment", "environment",
"equipment", "establishment", "evaluation", "examination", "exceptional", "excitement",
"exercise", "expedition", "experience", "explanation", "exploration", "expression",
"extraordinary", "facilitation", "fascinating", "favorable", "feedback", "fellowship",
"fertilizer", "fictional", "finalization", "flexibility", "fluctuation", "foundation",
"framework", "friendship", "functionality", "fundamental", "furniture", "generosity",
"geography", "government", "graduation", "guidelines", "happiness", "harassment",
"headquarters", "healthcare", "hesitation", "historical", "hospitality", "household",
"identification", "illustration", "imagination", "implementation", "importance", "impression",
"improvement", "inclusion", "independence", "individual", "industrial", "information",
"innovation", "inspection", "installation", "inspiration", "instruction", "instrumentation",
"integration", "intelligence", "interaction", "interesting", "interpretation", "intervention",
"introduction", "investment", "involvement", "journalism", "judgmental", "justification",
"knowledgeable", "leadership", "legislation", "liberation", "lightweight", "literature",
"maintenance", "management", "manuscript", "marvelous", "mathematics", "measurement",
"mechanical", "meditation", "membership", "methodology", "migration", "moderation",
"modification", "motivation", "navigation", "negotiation", "networking", "noteworthy",
"observation", "opportunity", "optimistic", "organization", "originality", "participation",
"particular", "partnership", "perception", "performance", "personality", "philosopher",
"photography", "placement", "playground", "population", "positively", "possession",
"practical", "preparation", "presentation", "preservation", "prevention", "principle",
"prioritize", "probability", "procedure", "production", "professional", "programming",
"progressive", "projection", "promotional", "pronunciation", "proportion", "protection",
"psychology", "publication", "punishment", "qualification", "quantitative", "questionnaire",
"realization", "recognition", "reduction", "reflection", "regulation", "relationship",
"repetition", "replacement", "representation", "reputation", "residential", "resistance",
"resolution", "responsibility", "restoration", "restriction", "revolution", "satisfaction"
] #List of words
def sort_char():
    random.shuffle(long_words)
    computer = random.choice(long_words)
    return computer
#dictionary of key:()

line = {0: (" "), 
               1: (" o ",
                   "   ",
                   "   "), 
               2: (" o ",
                   " | ",
                   "   "), 
               3: (" o ",
                   " | ",
                   "/  "), 
               4: (" o ",
                   " | ",
                   "/ \\"),#Note, if you use one backslash it will rise an error. Will be necessary to put two backslashes
               5: (" o ",
                   "/| ",
                   "/ \\"),
               6: (" o ",
                   "/|\\",
                   "/ \\")}
def display_man(wrong_guesses):
    for element in line[wrong_guesses]:
        print(element)

def create_word(word):
    element = list(word)
    num_elem = []
    is_running = True
    count_rights = 0
    count_error = 0
    for position in element:
        num_elem.append("_")
    while is_running:
        print("  ".join(num_elem))
        print(f"Number of mistakes {count_error}")
        guess = input("Enter your guess here: ")
        check_char = False
        for i, unit in enumerate(element): #The enumerate method returns index and value [0:'a']
            if unit == guess:
                num_elem[i] = guess
                check_char = True
                count_rights = count_rights + 1  
        if check_char == False:
            count_error = count_error + 1
        display_man(count_error)
        if count_rights == len(word):
            print("  ".join(num_elem))
            print("You won! 🎉 😁")
            play = input("Type y to play again: ").lower()
            if play == "y":
                count_error = 0
            else:
                is_running = False
        if count_error == 6:
            print(f"The correct aswer is {word}")
            print("You loose! 👎 😒")
            play = input("Type y to play again: ").lower()
            if play == "y":
                count_error = 0
            else:
                is_running = False

    print("Thanks for playing")

def main():
    computer = sort_char()
    create_word(computer)


if __name__ == '__main__':
    main()
