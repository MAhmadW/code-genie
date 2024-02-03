import sys
import os
import time
import datetime

import openai

from prompts.basic import BASIC_PROMPT
from env import OPENAI_API_KEY, SOLUTIONS_PATH, MODEL
from languages import LANG_MAP

OPENAI_CLIENT = openai.OpenAI(api_key=OPENAI_API_KEY)

def num_args():
    num_args = len(sys.argv)-1
    return num_args

def get_arg(num):
    return sys.argv[num]

def build_prompt(question,lang):
    prompt = f' The question is \n {question}.\n'+ f' The programming language of the solution needs to be {lang}.'
    return prompt

def generate_response(user_message):
    response = OPENAI_CLIENT.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": BASIC_PROMPT},
        {"role": "user", "content": user_message}
    ]
    )

    return response.choices[0].message.content

def main():
    try:
        os.mkdir(SOLUTIONS_PATH)
    except:
        print(f'Solutions directory already exists as {SOLUTIONS_PATH}')

    if num_args() == 1:
        command = get_arg(1)
        if command == "languages":
            print("The supported languages are: ")
            for lang in LANG_MAP.keys():
                print (lang)

    elif num_args() == 2:
        q_file = get_arg(1)

        lang = get_arg(2)

        q = ''

        with open(q_file,'r') as f:
            q = f.read()

        script = generate_response(build_prompt(q, lang))

        with open(os.path.join(SOLUTIONS_PATH,f'solution.{LANG_MAP[lang]}'),'w') as f:
            f.write(script)

        



if __name__=='__main__':
    main()