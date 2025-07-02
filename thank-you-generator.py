f = open("gifts.txt")
x = f.readlines()

# print(x)
y = ", ".join(x)

# print(y)
z = y.split(",")


# print(z)
n = open("notes.txt", "w")
try:
    for i in z:
        k = i.split(":")
        template = f'\n\n\n\n{k[0]},\n\nThank you so much for the{k[1]}!\n\nWe loved seeing you at the baby shower and are very excited for you to meet our baby girl in September. We are very grateful to have you in our lives and appreciate the time you took to celebrate with us at the shower.\n\nThank you again for your generosity! Sending our best wishes for you and your family,\n\nMason, Bailey, and Baby Rose Adrales'
        print(template)
        n.write(template)
except IndexError:
    print("Index out of range")
f.close()
n.close()