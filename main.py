from RenameData import rename
from Search import search
from SearchDuplicateData import search_duplicates

path = ""  # The Path where you want do store your images
out_path = ""
search_terms = []  # This is where your searchterms go

for term in search_terms:
    search(term, path)  # Fist the term and then the Path

rename(path)  # Here goes just the path as an argument
search_duplicates(path, out_path)  # Here goes the path and an output path where the duplicates should be saved
