from RenameData import rename
from Search import search
from SearchDuplicateData import search_duplicates
from SortData import sort
from variables import *

for term in search_terms:
    search()  # Fist the term and then the Path

rename()  # Here goes just the path as an argument
search_duplicates()  # Here goes the path and an output path where the duplicates should be saved
sort()  # Fist the path for the images you want to sort the path with images you want to use then wich you are not sure and last the path with images you dont want to use
