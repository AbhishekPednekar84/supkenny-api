import random

messages = [
    "Thank you so much for your message!",
    "Thanks a bunch for your message!",
    "Thank you for brightening our day!",
    "You just made our day. Thanks!",
    "Many thanks for writing to us!",
    "Your message means a lot to us. Thanks!",
    "Thanks a million for your message!",
    "We're so stoked that you wrote to us!",
    "Your message has made this day special. Thanks!",
]


def return_random_message():
    random.choice(messages)
