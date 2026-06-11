import random


sub = ["Shah Rukh Khan", "Salman Khan", "Aamir Khan", "Amitabh Bachchan", "Virat Kohli", "MS Dhoni", "Narendra Modi", "Elon Musk", "Bill Gates", "Mark Zuckerberg",
       "Taylor Swift", "Cristiano Ronaldo", "Lionel Messi", "MrBeast", "Tom Cruise", "Dwayne Johnson", "Donald Duck", "Batman", "Spider-Man", "SpongeBob"]
action = ["spotted being a cowboy in", "passed by", "crying over", "got a job in", "wants to go to", "accidentally bought", "got banned from", "started a food fight in", "lost a slipper in", "opened a tea stall in", "challenged a goat in",
          "became principal of", "was caught dancing in", "is hiding from taxes in", "mistook for their house", "declared war on", "got trapped inside", "tried to sell Wi-Fi in", "adopted 37 pigeons from", "started a rock band in"]
places = ["Delhi", "Mumbai", "Furfuri Nagar", "India Gate", "the Moon", "Mars", "Antarctica", "Area 51", "the Sahara Desert", "Mount Everest", "a random WhatsApp group",
          "a Minecraft village", "the backrooms", "Hogwarts", "Gotham City", "Spongebob's Home", "a potato farm", "a haunted railway station", "an abandoned shopping mall", "a secret underground bunker"]
sentence = (
    f"\"{random.choice(sub)} {random.choice(action)} {random.choice(places)}\"")
print(f"Today's Headline Is:\n{sentence}")
