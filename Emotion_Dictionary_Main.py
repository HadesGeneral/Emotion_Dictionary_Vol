
def while_check(emotion, list_of_feelings):
    """
    checks the users input against the main emotion lists or asks them again to answer with an answer I want
    :param emotion:
    :param list_of_feelings:
    :return:
    """
    while emotion.lower() not in list_of_feelings:
        emotion = input("Please choose the specific emotion that relates to you most: " + ', '.join(list_of_feelings))
    return emotion


def secondary_emotion(emotion):
    """
    checks the input from user and uses the corresponding list m
    :param emotion:
    :return:
    """
    if emotion == "sad":
        list_of_secondary = ["guilty", "depressed", "lonely", "bored", "abandoned", "despair"]
    elif emotion == "happy":
        list_of_secondary = ["joyful", "interested", "proud", "accepted", "powerful", "peaceful", "intimate", "optimistic"]
    elif emotion == "angry":
        list_of_secondary = ["hurt", "threatened", "hateful", "mad", "aggressive", "frustrated", "distant", "critical"]
    elif emotion == "fear":
        list_of_secondary = ["humiliated", "rejected", "submissive", "insecure", "anxious", "scared"]
    return list_of_secondary


def tertiary(emotion):
    """
    Prints out the definition of the secondary emotion for sad, along with similar feelings
    :param emotion:
    :return:
    """

# start of happy emotions
    if emotion == "joyful":
        print()
        print("People who feel joyful have a feeling of great pleasure and happiness. They feel ecstatic and/or ")
        print("liberated from what they have done.")
    elif emotion == "interested":
        print()
        print("People who feel interested show curiosity or concern about something or someone. They might also ")
        print("feel amused and or inquisitive about said thing.")
    elif emotion == "proud":
        print()
        print("People who feel proud show deep pleasure or satisfaction as a result of one's own achievements, ")
        print("qualities, or possessions or those of someone with whom one is closely associated. They feel ")
        print("important/confident from what they achieved.")
    elif emotion == "accepted":
        print()
        print("People who feel accepted generally feel believed in or recognized to be valid or correct. They also feel")
        print("recognized and fulfilled byt what they have done or achieved.")
    elif emotion == "powerful":
        print()
        print("People who feel powerful feel courageous and empowering from something they achieved. They sometimes feel")
        print("on top of the world")
    elif emotion == "peaceful":
        print()
        print("People who feel peaceful or at peace feel free from disturbances or a sense of tranquil. They might even")
        print("feel hopeful about what they're doing.")
    elif emotion == "intimate":
        print()
        print("People who feel intimate about something or someone this is because they feel very familiar and very ")
        print("acquainted with them. They are usually playful or sensitive about the topic also.")
    elif emotion == "optimistic":
        print()
        print("People who feel optimistic feel hopeful and confident about the future events. They might feel inspired ")
        print("or more inspired to do something.")
# start of sad emotions
    elif emotion == "guilty":
        print()
        print("People who feel guilty are feeling their effects of a specific wrongdoing.")
        print("They might also feel remorseful or ashamed for what they have done.")
    elif emotion == "abandoned":
        print()
        print("People who feel abandoned feel like they have deserted or given up on. ")
        print("They might also feel ignored or victimized by someone.")
    elif emotion == "despair":
        print()
        print("People who feel despair usually feel at a loss or a sense of hopelessness. ")
        print("They also feel powerless or vulnerable to what is happening around them.")
    elif emotion == "depressed":
        print()
        print("People who feel depressed feel general unhappiness or despondency. They may")
        print("also feel inferior or empty at times about themselves.")
    elif emotion == "lonely":
        print()
        print("People who feel lonely feel without company or in complete solitude. They may also feel")
        print("abandoned or isolated from people.")
    elif emotion == "bored":
        print()
        print("People who feel bored feel weary because one is unoccupied in something or lacks interest in current")
        print("activity. They may also feel indifferent or apathetic about the current activity.")
# Start of fear emotions
    elif emotion == "humiliated":
        print()
        print("People who feel humiliated feel ashamed or their dignity and self-respect is .")
        print("They might also feel ridiculed or disrespected by someone.")
    elif emotion == "rejected":
        print()
        print("People who feel rejected are dismissed as inadequate to someone else's taste. ")
        print("They might also feel alienated by the person too.")
    elif emotion == "submissive":
        print()
        print("People who feel submissive are passive or ready to conform to the authority or will of others. ")
        print("They might also feel insignificant or worthless compared to the other person..")
    elif emotion == "insecure":
        print()
        print("")
        print("People who feel insecure may not feel confident or assured. They feel unsafe, inadequate, or inferior.")
    elif emotion == "anxious":
        print()
        print("People who feel anxious experience worry, unease, or nervousness about an imminent event or an uncertain")
        print("outcome of something. They might also feel overwhelmed about said thing.")
    elif emotion == "scared":
        print()
        print("People who feel scared are scared or frightened from something or someone. They might also feel")
        print("frightened about something.")
# start of anger emotions
    elif emotion == "hurt":
        print()
        print("People who feel hurt feel emotionally attacked or injured by someone or by an event that happened. ")
        print("They might feel devastated or embarrassed by what the person did or event effected them.")
    elif emotion == "threatened":
        print()
        print("People who feel threatened fear the possibility of someone's intention to harm or hurt them. ")
        print("They might feel jealous or insecure by the person too.")
    elif emotion == "hateful":
        print()
        print("People who feel hateful are filled by hate or feel very unpleasant. ")
        print("They might feel resentful of others.")
    elif emotion == "mad":
        print()
        print("People who feel mad are generally very angry at someone or an event that effected them.")
        print("They might also feel enraged or furious about what someone done or what an event had an effect on them.")
    elif emotion == "aggressive":
        print()
        print("People who feel aggressive feel likely to confront or attack someone about something and they pursue an")
        print("interest forcefully. They also might act hostile in general.")
    elif emotion == "frustrated":
        print()
        print("People who feel frustrated express distress and annoyance for someone or an event that is happening.")
        print("They might also feel irritated or infuriated by said someone or event")
    elif emotion == "distant":
        print()
        print("People who feel distant have the sense of feeling faraway or withdrawn from others.")
        print("They might not be intimate or might seem suspicious of others.")
    elif emotion == "critical":
        print()
        print("People who feel critical analyzes things extensively about something or someone.")
        print("They might also be skeptical about said person or thing and be sarcastic to them or it.")


def main():
    """
    asks the user what they are feeling and runs the appropriate function
    :return:
    """
    print("Hello, want to better understand how you or someone else is feeling? Which one best relates to how ")
    emotion = input("you or someone else feels: fear, angry, happy, or sad ")
    primary_emotions = ["sad", "happy", "angry", "fear"]
    first_emotion = while_check(emotion, primary_emotions)
    print()
    second_emotion = while_check(emotion, secondary_emotion(first_emotion))
    tertiary(second_emotion)


main()      # this is main function
