def read_template(file_path):

  with open(file_path) as template_file:
    template = template_file.read()

  return template

def parse_template(template):

  template_stripped = ''
  template_parts = []

  part_start_index = template.find('{')
  part_end_index = template.find('}')
  template_stripped += template[:part_start_index + 1]
  template_parts.append(template[part_start_index + 1:part_end_index])

  while template.find('{', part_end_index) != -1:
    part_start_index = template.find('{', part_end_index)
    template_stripped += template[part_end_index:part_start_index + 1]
    part_end_index = template.find('}', part_start_index)
    template_parts.append(template[part_start_index + 1:part_end_index])

  template_stripped += template[part_end_index:]

  return (template_stripped, tuple(template_parts))

def merge(template_stripped, input_words):
  
  template_merged = template_stripped.format(*input_words)

  return template_merged

def get_input_words(input_parts):

  input_words = []

  for part in input_parts:
    part_input = input(f'{part} > ')
    input_words.append(part_input)

  return tuple(input_words)

def save_completed_madlib(template_completed):

  with open('assets/completed_madlib.txt', 'w') as completed_madlib:
    completed_madlib.write(template_completed)

def main(file_path):

  template = read_template(file_path)

  template_stripped, input_parts = parse_template(template)

  input_words = get_input_words(input_parts)

  template_completed = merge(template_stripped, input_words)

  save_completed_madlib(template_completed)

  print(f'\n**** Your Completed Mad Lib ****\n\n{template_completed}\n')


###############
## Start App ##
###############
  
if __name__ == '__main__':

  file_path = 'assets/make_me_a_video_game.txt'

  print("""
  Welcome to command line Mad Lib! The game is super simple ;) There is a story that is missing a bunch of pieces and you are going to complete it by filling in the blanks. At each prompt, provide a word that matches the requirement and hit enter. The point of the game is to create a fun and silly story so get creative you with your responses!
  """)

  main(file_path)
