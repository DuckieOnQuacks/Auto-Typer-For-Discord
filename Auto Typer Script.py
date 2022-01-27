import keyboard
import time
import random

sentence_list = ["These designs are crazy",
"Man i hope i can get that waitlist",
"I really like the community here",
"This is the best NFT collection ive seen",
"We got this everyone!",
"Have a nice day everyone",
"This WL is my dream",
"Hey all",
"Hello!",
"hows everyone doing?",
"lets get to level 10",
"Hopefully we can all get this!",
"Absolutely amazing collection"]


min_time = 6
max_time = 12

def deftype_mes(sentence):
    for letters in sentence:
        time.sleep((random.randint(0,5)/10))
        keyboard.write(letters)
    keyboard.press_and_release("enter")

if __name__ =="__main__":

    time.sleep(5)
    while True:
        index = random.randint(0,len(sentence_list) - 1)
        sentence = sentence_list[index]
        deftype_mes(sentence)
        #sentence_list.pop(index)
        time.sleep(random.randint(min_time,max_time))


    

