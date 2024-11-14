
# pip install openai
import openai
import os

# Ustawienie klucza API OpenAI
# 'sk-proj-_ntxXZZ329_VcNkuyZ94k6wlb4vS9I24lZBoQTvOSX-yEE1GUbh4qvmuhVtT**eAqHICmcFAIUrl88OmgIAJ3tXzjFLsA'  nie udostepniam klucza publicznie


# Wskazanie pliku z kluczem API
openai.api_key = 'C:\Users\katar\backend-recruitment-task-master\api_key'

def read_text_file(file_path):
    """Odczytuje zawartość pliku tekstowego."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()  # Zwraca zawartość pliku jako tekst
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None

def ask_openai(question):
    """Wysyła pytanie do API OpenAI i zwraca odpowiedź w formie HTML."""
    try:
        # Wywołanie OpenAI API z odpowiednimi parametrami
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Użycie modelu GPT-3.5
            prompt=question,  # Przekazanie artykułu z zapytaniem o generowanie HTML
            max_tokens=2000  # Zwiększenie limitu tokenów, aby uzyskać długie odpowiedzi
        )
        return response['choices'][0]['text'].strip()  # Zwracamy odpowiedź
    except Exception as e:
        print(f"Wystąpił błąd podczas komunikacji z OpenAI: {e}")
        return None

def save_to_html(content, output_path):
    """Zapisuje treść do pliku HTML."""
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Artykuł zapisany do {output_path}.")
    except Exception as e:
        print(f"Błąd podczas zapisywania pliku HTML: {e}")

# Główna funkcja aplikacji
if __name__ == "__main__":
    file_path = r"C:\Users\katar\backend-recruitment-task-master\test_oxd\text"  # Ścieżka do pliku z artykułem
    output_path = r"C:\Users\katar\backend-recruitment-task-master\test_oxd\artykul.html"  # Ścieżka, gdzie zapisujemy HTML

    # Odczytanie treści artykułu z pliku
    article_content = read_text_file(file_path)
    
    if article_content:
        print("Treść zapytania:\n\n", article_content)

        # Przygotowanie zapytania do OpenAI
        question = f"""
        Przekształć poniższy artykuł na stronę internetową w HTML. Użyj odpowiednich tagów HTML, takich jak <h1>, <h2>, <p>, <ul>, <li>, <img>. 
        Dodaj tagi <img> z atrybutem src="image_placeholder.jpg" oraz alt, które zawierają dokładny prompt do generowania obrazu (np. "A beautiful landscape").
        Każdy obrazek powinien mieć podpis w tagu <figcaption>.
        
        Proszę o wygenerowanie wyłącznie kodu HTML, bez nagłówków HTML, <head>, <body>. Zwróć tylko zawartość do umieszczenia pomiędzy tagami <body> i </body>.

        Artykuł:
        {article_content}
        """

        # Wyślij zapytanie do OpenAI
        article_html = ask_openai(question)
        
        if article_html:
            # Zapisz otrzymany wynik w pliku HTML
            save_to_html(article_html, output_path)
