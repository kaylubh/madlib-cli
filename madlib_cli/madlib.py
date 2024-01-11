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
  
  template_completed = template_stripped.format(*input_words)

  return template_completed


def get_template(file_path):

  template = read_template(file_path)

  return template


# test = get_template('assets/make_me_a_video_game.txt')
# print(test)
