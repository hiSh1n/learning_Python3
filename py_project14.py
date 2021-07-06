#program for searching a word in some text

#defining a function, asking user to enter text and the word to be found in that text.
def search(text, word):
  if word in text:
    print("word found")
  else:
    print("word not found")
text = input()
word = input()

print(search(text, word))
