import random
import os
from hangman_words import word_list

def clear_screen():
    # Verifică sistemul de operare pentru a determina comanda de curățare a ecranului
    if os.name == 'posix':
        # Pentru sistemele de operare de tip Unix/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':
        # Pentru sistemele de operare Windows
        os.system('cls')

# Poți apoi să folosești această funcție în locul lui clear()
clear_screen()

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
#Testing code
print(f'Solutia este {chosen_word}.')

#Creaza blanks
display = []
for _ in range(word_length):
    display += "_"
  
while not end_of_game:
    guess = input("Introdu o litera: ").lower()

    clear_screen()
    if guess in display:
      print(f"Deja ai ghicit litera {guess}")
    
    #Verifica litera ghicita
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
      
    #Verifica daca utilizatorul a gresit
    if guess not in chosen_word:
        print(f"Litera {guess} nu este in cuvant, ai pierdut o viata.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Ai pierdut.")
      
    print(f"{' '.join(display)}")
    
    #Verifica daca utilizatorul are toate literele.
    if "_" not in display:
        end_of_game = True
        print("Ai castigat.")
      
    from hangman_art import stages
    print(stages[lives])