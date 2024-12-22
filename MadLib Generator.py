#MadLib Generator

def mad_libs_generator():
    template = """
    Once upon a time in a {adjective} land, there lived a {noun} who loved to {verb}.
    Every day, the {noun} would {verb} with its friends, and they would have {adjective} adventures.
    One day, they found a {noun} that was {adjective} and decided to {verb} it.
    And they all lived {adverb} ever after!
    """

    # Get user input for the placeholders
    print("Let's create a Mad Libs story!")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    adverb1 = input("Enter an adverb: ")
    noun2 = input("Enter another noun: ")

    # Replace placeholders with user input
    story = template.format(adjective=adjective1, noun=noun1, verb=verb1, adverb=adverb1)

    # Print the final story
    print("\nHere is your Mad Libs story:")
    print(story)


mad_libs_generator()