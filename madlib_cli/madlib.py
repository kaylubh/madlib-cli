def read_template(file_path):

  with open(file_path) as template_file:
    template = template_file.read()

  return template

def parse_template(template):
  
  template_list = template.split()
  parts = []

  for i, word in enumerate(template_list):
    if word[0] == '{':
      end = word.find('}')
      part = word[1:end]
      parts.append(part)
      stripped = word[0] + word[end:]
      template_list[i] = stripped

  template_stripped = ' '.join(template_list)
  template_parts = tuple(parts)
  parsed_template = (template_stripped, template_parts)

  return parsed_template

def merge(template_stripped, input_words):
  
  template_completed = template_stripped.format(*input_words)

  return template_completed


# def test():

#   template = read_template('../assets/dark_and_stormy_night_template.txt')

#   parsed = parse_template(template)

#   return parsed

# print(test())
