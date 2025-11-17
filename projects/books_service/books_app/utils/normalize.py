import unicodedata

def normalize(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return ''.join(c for c in normalized if unicodedata.category(c) != "Mn").lower()
