import random

def magic_8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    return random.choice(responses)

# Main function
if __name__ == "__main__":
    print("Welcome to the Magic 8 Ball!")
    while True:
        input("Ask your question: ")
        print(magic_8_ball())
        play_again = input("Do you want to ask another question? (yes/no): ")
        if play_again.lower() != "yes":
            print("Goodbye!")
            break

