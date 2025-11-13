import sys
from stats import get_num_words, get_num_characters, sort_list

if len(sys.argv) != 2:
  print(f"Usage: python3 main.py <path_to_book>")
  sys.exit(1)
  
path_to_book = sys.argv[1]
  
def get_book_text(path_to_book):
  with open(path_to_book) as f:
    # f is a file object
    file_contents = f.read()
    return file_contents
  
def main():
  file = get_book_text(path_to_book)
  num_words = get_num_words(file)
  num_characters = get_num_characters(file)
  num_characters.sort(reverse=True, key=sort_list)
  
  print("============ BOOKBOT ============\n" 
        f"Analyzing book found at {path_to_book}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------")
  
  for item in num_characters:
    print(f"{item['char']}: {item['num']}")
    
  print("============= END ===============")
  
  
main()