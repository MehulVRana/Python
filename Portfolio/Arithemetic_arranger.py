# -*- coding: utf-8 -*-
"""
Created on Sat Feb    5 14:33:27 2022

@author: jindo
"""


def arithmetic_arranger(problems, Answer = None):
    
    ''' 
    Prints out the formulas in a pretty format, can display the answer 
    
    Args:
        problems (list, str): Up to 4 equations can be inputted in the form of a 
        list, each equation must have spaces around the operator, the operator
        can only be + or -, all the numbers must be less than 10,000 and 
        numerical.

        Answer (bool, optional): Affects whether answers are displayed.
    
    Returns:
        str : formatted equations, with answers if Answer == True
    '''

    no_of_problems = len(problems)

    if no_of_problems > 5:
        return 'Error: Too manproblem problems.'

    # Cycle through questions
    problem_count = 0
    question_sections = []
    
    while problem_count < no_of_problems:
        # Split the question into separate parts
        problem = problems[problem_count]
        split_problem = problem.split(' ')
        num_1 = split_problem[0]
        operator = split_problem[1]
        num_2 = split_problem[2]
        
        try:
            num_1_int = int(num_1)
            num_2_int = int(num_2)
        except:
            return 'Error: Numbers must only contain digits.'

        larger_number = max([num_1_int, num_2_int])

        if larger_number > 9999:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == '+':
            num_3_int = num_1_int + num_2_int
        elif operator == '-':
            num_3_int = num_1_int - num_2_int
        else:
            return 'Error: Operator must be \'+\' or \'-\'.'

        num_3 = str(num_3_int)
        len_num_1, len_num_2, len_num_3 = len(num_1), len(num_2), len(num_3)

        # Identify the space required for each question
        leng_max = max([len_num_1, len_num_2]) + 2
        
        # Identify the numbers of spaces in each segment
        num_1_len = leng_max - len_num_1
        num_2_len = leng_max - len_num_2
        num_3_len = leng_max - len_num_3

        question_sections.append([num_1_len * ' ' + num_1, 
                                operator + (num_2_len - 1)* ' ' + num_2, 
                                leng_max * '-', 
                                num_3_len * ' ' + num_3])
        problem_count += 1
        
    formatted_questions = []
    # Identify whether the answer is revealed
    if Answer is True:
        number_of_lines = 4
    else:
        number_of_lines = 3

    # Arrange the sequence by cycling through questions, selecting line no.
    line_number = 0
    while line_number < number_of_lines:
        # All lines but the first need need a new line break
        if line_number != 0:
            formatted_questions.append('\n')
        
        problem = 0 
        while problem < no_of_problems:
            formatted_questions.append(question_sections[problem][line_number])
            # All questions but the last need need a spacer
            if problem != no_of_problems - 1:
                formatted_questions.append(4*' ')
            problem += 1
        line_number += 1

    # Append the strings in the arranged order
    arranged_problems = ''
    for fragment in formatted_questions:
        arranged_problems += fragment
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))