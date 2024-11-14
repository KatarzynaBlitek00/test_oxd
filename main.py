# pip install openai
import openai




openai.api_key = 'YOUR_OPENAI_API_KEY'

def read_text_file(file_path):
    """Odczytuje zawartość pliku tekstowego."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def ask_openai(question):
    """Wysyła pytanie do API OpenAI i zwraca odpowiedź."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Główna funkcja aplikacji
if __name__ == "__main__":
    try:
        # Odczytaj treść zapytania z pliku
        user_question = read_text_file(r"C:\Users\katar\backend-recruitment-task-master\test_oxd\text")
        print("Treść zapytania:\n", user_question)

        # Wyślij zapytanie do API OpenAI
        answer = ask_openai(user_question)
        print("\nOdpowiedź od OpenAI:\n", answer)
    
    except FileNotFoundError:
        print("Plik text.txt nie został znaleziony. Upewnij się, że plik znajduje się we wskazanej lokalizacji.")
    except Exception as e:
        print("Wystąpił błąd:", e)


# import os

# file_path = r'C:\Users\katar\backend-recruitment-task-master\test_oxd\text'

# # Sprawdzanie pełnej ścieżki
# print("Sprawdzamy ścieżkę: ", file_path)

# # Sprawdzenie, czy plik istnieje
# if os.path.exists(file_path):
#     print("Plik znaleziony.")
# else:
#     print("Plik NIE został znaleziony.")
