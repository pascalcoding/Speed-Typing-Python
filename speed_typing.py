import curses, random
from curses import wrapper
import time

random_text = [
                "The rusty nail stood erect, angled at a 45-degree angle, just waiting for the perfect barefoot to come along.",
                "Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?",
                "No matter how beautiful the sunset, it saddened her knowing she was one day older.",
                "He turned in the research paper on Friday; otherwise, he would have not passed the class.",
                "A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.",
                "She was disgusted he couldn’t tell the difference between lemonade and limeade.",
                "The hawk didn’t understand why the ground squirrels didn’t want to be his friend."
                ]

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress Any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def test(stdscr):
    test_text = random_text[random.randint(0,6)]
    count_of_words = len(test_text.split(" "))
    list_test_text = list(test_text)
    current_text = []


    stdscr.clear()
    stdscr.addstr(test_text)
    stdscr.refresh()

    start_time = time.time()

    while len(current_text) != len(test_text):
        key = stdscr.getkey()
        current_text.append(key)
        tries = 0
        correct = 0
        for i in range(len(current_text)):
            if current_text[i] == list_test_text[i]:
                stdscr.addstr(0,i, current_text[i], curses.color_pair(2))
                correct += 1
            else:
                if list_test_text[i] == ' ':
                    stdscr.addstr(0,i,'_', curses.color_pair(3))
                else:
                    stdscr.addstr(0,i,list_test_text[i], curses.color_pair(3))
            tries += 1

    end_time = time.time()

    words_per_minute = round(count_of_words / (end_time-start_time) * 60,2)
    accruazy = round(correct/tries * 100,2)

    stdscr.addstr(f'\nYou typed with a speed of {words_per_minute} words per minute and with an accruazy of {accruazy}%.')
    stdscr.getkey()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        test(stdscr)
        stdscr.addstr("\nDo you want try again? Type y/n")
        key = stdscr.getkey()
        if key.lower() == 'n':
            break

wrapper(main)
