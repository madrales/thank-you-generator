f = open("gifts.txt")
n = open("notes.txt", "w")
x = f.readlines()
y = ", ".join(x)
z = y.split(",")
try:
    for i in z:
        k = i.split(":")
        template = f'\n\n\n\n{k[0]},\n\nWe wanted to reach out and say thank you so much for the{k[1]}!\n\nWe loved seeing you at the baby shower and are very excited for you to meet our baby girl in September. We are very grateful to have you in our lives and appreciate the time you took to celebrate with us at the shower.\n\nThank you again for your generosity!'
        print(template)
        n.write(template)
except IndexError:
    print("Index out of range")
f.close()
n.close()