
import time
import random
import sys

def show_delay(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def scene_setup():
    show_delay("It was a dark and stormy night.")
    show_delay("The rain pattered against the window, but a lone cursor blinked on a screen, ready to write the next chapter.")
    print()

def introduce_charles():
    show_delay("This lone cursor belonged to Charles, a renowned thriller author who captivated his audience with stories of mystery and murder.")
    show_delay("On this dark and stormy night, he was working on his next novel, possibly his biggest one yet.")
    print()

def describe_story_within_story():
    show_delay("He was writing about a character in a house, on a night much like this one, who was stalked and attacked by unseen hackers trying to steal his identity and every secret file.")
    print()

def computer_troubles():
    show_delay("As Charles typed, his computer began to slow.Strange applications appeared out of nowhere; the writing app crashed and rebooted.")
    show_delay('"What is going on?" he muttered, fingers hovering over the keys.')
    print()

def the_email():
    show_delay("Then an email arrived. No subject. Unknown sender.")
    show_delay("Curiosity edged into unease as Charles hovered the mouse over the message.")
    show_delay("The storm outside rumbled, echoing the pressure in his chest.")
    show_delay("He clicked.")
    print()
    
    time.sleep(0.7)
    show_delay('The screen flickered, then the message displayed:')
    show_delay('"We\'re already inside."')
    print()

   
def main():
    scene_setup()
    introduce_charles()
    describe_story_within_story()
    computer_troubles()
    the_email()
    

main()
