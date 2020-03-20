''' file to process text entered by user '''

def get_text():
  text = input('Enter text: ')
  return text

def show_text(text):
  print(text)

def main():
  user_entered_text = get_text()
  show_text()
  
if __name__ == "__main__":
  main()
  
