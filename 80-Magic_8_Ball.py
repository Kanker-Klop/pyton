import random
import time
magic_ball_answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
vraag = "kaka"
while vraag != "":
    print("VRAAG MIJ, DE ALMACHTIGE, ALWETENDE MAGISCHE 8-BAL IETS, EN IK ZAL JE BEANTWOORDEN (zorg da uw vraag een ja-nee vraag is met een '?', anders roep ik tegen u)")
    vraag = input()
    if vraag == "":
        break
    if "?" in vraag:
        print(magic_ball_answers[random.randint(1,20)])
    else:
        for fout in range(8000):
            print("GAST, IK ZEI EEN JA-NEE VRAAG MET EEN '?'")
        kaka = "kaka"
        while kaka != "":
            print("MONGOOL")
    try:
        flakka = "umoeder"
    except KeyboardInterrupt:
        print("\nJAMA JEZUSZ")
        exit()


print("EN DIT WAS HET")