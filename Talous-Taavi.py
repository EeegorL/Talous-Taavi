from CommandHandler import heed;
import os;
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Talous-Taavi");
os.system("COLOR F1");

os.system("cls");

home = os.path.expanduser("~");
loc = os.path.join(home, "Documents");

if(not os.path.isfile(os.path.join(loc, "talous-taavi-data.csv"))):
    open(os.path.join(loc, "talous-taavi-data.csv"), "x").close();

s = "Talous-Taavi";
l=25;

print("-"*(len(s) + 2*l)); # title printing
print(f"|{" "*l}{s}{" "*(l - 2)}|");
print("-"*(len(s) + 2*l));

while(True):
    print("Toiminto: (1-4)");
    print("Numero 0 missä tahansa vaiheessa palaa takaisin valikkoon.")
    inp = input("1: Lisää talletus\n2: Näytä talletukset\n3: Tilin summa\n4: Poista talletus ID:llä\n5: Sulje\n  => ");
    print();

    if(inp.isnumeric()):
        k = int(inp);
        heed(k);
    
    else:
        print("Väärä komento");