import time
import random
from colorama import init, Fore, Back

def run_typing_test():
    try:
        with open('prompts.txt', 'r') as file:
            prompts = file.readlines()
    except FileNotFoundError:
        print(Fore.RED + 'Error: Could not find file prompts.txt.')
        return

    prompt = random.choice(prompts).strip()

    print(f'"{prompt}"\n')

    start_time = time.time()
    input_string = input('> ')
    elapsed_time = time.time() - start_time
    word_count = len(prompt.split())
    typing_speed = word_count / elapsed_time

    print('\nResult:\n')
    for c_prompt, c_input in zip(prompt, input_string):
        if c_prompt == c_input:
            print(Back.GREEN + c_prompt, end='')
        else:
            print(Back.RED + c_input, end='')
            print(Back.GREEN + prompt[len(input_string):], end='')
            break
    else:
        print(Back.GREEN + prompt[len(input_string):], end='')
    
    print(Back.RESET + '\n')
    print(f'Time elapsed: {elapsed_time:.2f} seconds.')
    print(f'Write speed: {typing_speed:.2f} words for second\n')

    try:
        with open('typing_results.txt', 'a') as f:
            f.write(f'Prompt: {prompt}\n')
            f.write(f'Time elapsed: {elapsed_time:.2f} seconds\n')
            f.write(f'Write speed: {typing_speed:.2f} words for second\n\n')
    except PermissionError:
        print(Fore.RED + 'Error: Could not write to file typing_results.txt.')

if __name__ == '__main__':
    init()

    run_typing_test()
