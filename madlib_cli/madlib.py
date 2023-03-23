from textwrap import dedent
import re
import random

global lib_collector

greeting = dedent(
    f"""
    {'*' * 35}
    ** Welcome to the Mad Lib Game! **
    **                              **
    **  Help me create an amazing   **
    **           Story              **
    {'*' * 35}
    """
)

def read_template(text_file):
    with open( text_file, "r") as test_lib:
        template = test_lib.read()
        return template

def parse_template(template):
    # print(template)
    pattern = r'\{.*?\}'
    stripped_template = re.sub(pattern, '{}', template)

    parts = re.findall(pattern, template)

    stripped_parts = list()

    for part in parts:
        stripped_parts.append(part.strip('{}'))

    stripped_parts = tuple(stripped_parts)

    return stripped_template, stripped_parts

def prompt_user(tuple):
    prompts = list(tuple)
    user_answers_list = list()
    for prompt in prompts:
        user_answers_list.append(input(f"""
    ++ Enter {prompt} ++
    """))
    return user_answers_list

def merge(template, parts):
    merged = template.format(*parts)
    print(merged)
    return merged

def create_story(story):
    num = random.randint(0,1000)
    with open(f'assets/story{num}.txt' , 'w') as new_file:
        new_file.write(story)

def main():
    print(greeting)
    template = read_template("assets/madlib.txt")
    stripped_items = parse_template(template)
    user_answers = prompt_user(stripped_items[1])
    finished_story = merge(stripped_items[0], user_answers)
    create_story(finished_story)

if __name__ == "__main__":
    main()

