# Instalamos la API de Wikipedia
# pip install wikipedia
import wikipedia
from wikipedia.exceptions import PageError
# Para selecionar el idimoa español
wikipedia.set_lang("es")

def searh(keyword):
    try:
        return wikipedia.summary(keyword, sentences = 1)
    except PageError:
        return f"Upss no pude encontrar {keyword}"

keyword = input("Buscar: ")
print(searh(keyword))