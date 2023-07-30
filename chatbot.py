import random

var_1 = ['Hi', 'Hello']
var_2 = ['How are you?', 'How are you doing?']
var_3 = ['What is your name?', 'How do I call you?', 'Your Name?']
var_4 = ['Which programming language you like the most?', 'Which programming language should I learn?']
var_5 = ['What are your hobbies?', 'What you do in your free time?']
var_6 = ['Bye', 'ok', 'Take care']
var_7 = ['What is the weather like today?', 'Tell me about yourself.']
var_8 = ['What do you do for a living?', 'Do you have any siblings?']
var_9 = ['Where are you from?', 'What is your favorite color?']
try:
    while True:
        user_input = input('User Replied To Bot: ')
        if user_input in var_1:
            bot1 = ['Hello', 'Hi']
            print('Bot Replied To User: ' + random.choice(bot1) + '\n')
        elif user_input in var_2:
            bot2 = ['I am good', 'I am doing good']
            print('Bot Replied To User: ' + random.choice(bot2) + '\n')
        elif user_input in var_3:
            bot3 = ['My name is Bot', 'You can call me Bot', 'Bot']
            print('Bot Replied To User: ' + random.choice(bot3) + '\n')
        elif user_input in var_4:
            bot4 = ['I like the Java language', 'You should learn the programming language according to your field of interest']
            print('Bot Replied To User: ' + random.choice(bot4) + '\n')
        elif user_input in var_5:
            bot5 = ['Learning a programming language', 'I used to do searching on new programming languages']
            print('Bot Replied To User: ' + random.choice(bot5) + '\n')
        elif user_input in var_6:
            bot6 = ['Bye', 'Thank you']
            print('Bot Replied To User: ' + random.choice(bot6) + '\n')
        elif user_input in var_7:
            bot7 = ['The weather is sunny today.', 'I am an AI chat bot.']
            print('Bot Replied To User: ' + random.choice(bot7) + '\n')
        elif user_input in var_8:
            bot8 = ['I am a chat bot programmed to assist users.', 'I am an only child.']
            print('Bot Replied To User: ' + random.choice(bot8) + '\n')
        elif user_input in var_9:
            bot9 = ['I am from the digital world.', 'My favorite color is blue.']
            print('Bot Replied To User: ' + random.choice(bot9) + '\n')
        elif user_input in var_10:
            bot10 = ['Sure! "The Alchemist" is a great book.', 'The capital of France is Paris.']
            print('Bot Replied To User: ' + random.choice(bot10) + '\n')
        # Add more elif blocks for additional questions
        else:
            print('Bot Replied To User: Sorry, I am not sure how to respond to that question.' + '\n')
except:
    print('Program End')
