import time
print("MY CHRISTMAS LIST\n")

#import time
import datetime

now = time.time()

birthday = time.strptime("25 Dec 19", "%d %b %y")
how_long_to_wait = time.mktime(birthday) - now

print("Today is {}.".format(time.asctime()))
time.sleep(3)

print("Christmas is on {} ".format(time.asctime(birthday)))
time.sleep(3)

print("That's {} to go ...".format(
    datetime.timedelta(seconds=how_long_to_wait)))
time.sleep(3)

print(" ")
time.sleep(1)
print("1. THINGS HAPPENING")
time.sleep(1)
print("* NOBODY BEING ANOYING ")
time.sleep(0.5)
print("* Get a dog PLEEEEEEEEEAAAAAAAAASE ")
time.sleep(0.3)
print("* NO ANGRY, SHOUTING OR ANOYED ALIVE THINGS")
time.sleep(0.3)
print("* Ice Scating PLEEEEEEEEEAAAAAAAAASE")
time.sleep(4)
print(" ")
print("2. BOOKS")
time.sleep(3)
print("- WARRIORS - THE NEW PROPHECY; THE NEXT BOOK")
time.sleep(2)
print("- Aru Shah and the tree of wishes(Roshani Chokshi)")
print("- Something I haven't heard of that I'll like (I want to try some thing new)")
time.sleep(1)
print("- A sherlock holmes book")
time.sleep(1)
print("- Pocket eyewitness mammals (toppings)")
time.sleep(2)
print("- ")
time.sleep(2)
print(" ")
time.sleep(5)
print("3. SPORTY THINGS")
print("* ")
print("* Larkhall football socks")
print(" ")
time.sleep(5)
print("4. OTHER")
print("- Phone (Apple) ")
print(" ")
time.sleep(5)
print("6. DVDs")
print("- more Hiccup and toothless")
print("- and more hiccup and toothless")
print(" ")
time.sleep(5)
print("7, 8, 9 & 10. ANYTHING ELSE YOU CAN THINK OF")