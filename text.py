''' file to process text entered by user '''
WORD_LIMIT = 50
def get_text():
  text = input('Enter text: ')
  return text

def show_text(text):
  if count_word_in_text(text) >= WORD_LIMIT:
    get_text()
  print(text)
 
def count_word_in_text(text):
  return text.count()
  

def main():
  user_entered_text = get_text()
  show_text()
 

if __name__ == "__main__":
  main()
  
