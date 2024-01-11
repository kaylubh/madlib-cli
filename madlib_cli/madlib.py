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
    part_input = input(f'Give me a {part} > ')
    input_words.append(part_input)

  return tuple(input_words)

def save_completed_madlib(template_completed):

  with open('assets/completed_madlib.txt', 'w') as completed_madlib:
    completed_madlib.write(template_completed)

def play_madlib(file_path):

  template = read_template(file_path)

  template_stripped, input_parts = parse_template(template)

  input_words = get_input_words(input_parts)

  template_merged = merge(template_stripped, input_words)

  print(template_merged)

# file_path = 'assets/dark_and_stormy_night_template.txt'
# play_madlib(file_path)
