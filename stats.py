from collections import Counter

def get_num_words(file):
  num_words = file.split()
  return len(num_words)

def get_num_characters(file):
  char_count = {}
  dict_list = []
  for item in file:
    character = item.lower()
    char_count[character] = char_count.get(character, 0) + 1
  
  for key, value in char_count.items():
    if key.isalpha():
      dict_list.append({'char': key, 'num': value})
  return dict_list

def sort_list(data):
  return data['num']
