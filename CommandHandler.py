from CsvHandler import add, listAll, total, delete;
from sys import exit;

def heed(comm):
    match(comm):
        case 1: # Lisää talletus
            add();
        case 2:
            listAll();
        case 3:
            total();
        case 4:
            delete();
        case 5:
            exit(0);
        case 0:
            pass;
        case _:
            print("Väärä komento");
            print();