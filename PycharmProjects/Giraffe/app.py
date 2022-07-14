# print(x)
#
# monthConversions = {
#      'jan': 'January',
#      'Feb': 'Feb'
#  }
# print(monthConversions.get('Feb','not a valid key'))

# secret_word = 'giraffe'
# guess= ''
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input('Enter guess: ')
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print('Out of guesses')
# else:
#     # print('You win!')



# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(3,2))
#

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
#     ]
#
# for row in number_grid:
#     for col in row:
#         print(col)

#vowel  - g
# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter in 'AEIOUaeiou':
#             translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input('Enter a phrase: ')))
#
# print(translate('aeiou'))

# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter in 'aeiou':
#             if letter.isupper():
#                 translation = translation + 'G'
#             else:
#                 translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation
# print(translate('Aeiou'))
#
#
# try:
#     number = int(input('Enter a num'))
#     print(number)
# except ZeroDivisionError:
#     print('divided by zero')
# except:
#     print('invalid')

#
# from students import Student
# student1 = Student('jin','art',3.1, False)
# print(student1.gpa)
#
# from Question import Question
# question_prompts = [
#     'what color are apples?\n(a) Red/Green \n(b) Purple\n(c) Orange\n\n',
#     'what color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
#     'what color are strawberries?\n(a) Teal\n(b) Red\n(c) Blue\n\n',
# ]
# questions = [
#     Question(question_prompts[0], 'a'),
#     Question(question_prompts[1], 'c'),
#     Question(question_prompts[2], 'b')
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print('You got ' + str(score) + '/' + str(len(questions)) + ' Correct')
#
# run_test(questions)

from students import Student
student1 = Student('jin','art',3.8, False)
print(student1.on_honor_roll())


# inheritance