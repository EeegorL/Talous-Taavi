from random import randint;
from datetime import datetime;
import os;
home = os.path.expanduser("~");
csv = os.path.join(home, "Documents", "talous-taavi-data.csv");

def uniqueId():
    ids = {};
    with open(csv, "r") as t:
        for r in t:
            if(";" in r):
                uid = r.split(";")[0];
                ids[uid] = "";
    t.close();

    while(True):
        rand = randint(1, 10**5);
        if(rand in ids):
            continue;
        return rand;


def add():
    print("Lisää talletus: \n");
    while(True):
        amount = input("Määrä: ").replace(",",".");

        if(amount == "0"): break;

        if(not amount.isnumeric() and not float(amount)): # not an integer or a decimal
            print("Väärä syöte. Syötä numero");
            continue;
        
        note = input("Kirjaus, paina Enteriä jos ei kirjausta: ");
        
        if(note == "0"): break;

        if(";" in note):
            print("';' ei ole sallittu merkki. yritä uudelleen");
            continue;
        break;
    
    if(amount != "0" and note != "0"):
        t = datetime.today();
        date = f"{t.day}.{t.month}.{t.year}-{t.hour}:{t.minute}";
        uid = uniqueId();

        with open(csv, "a") as t:
            t.write(f"{uid};{date};{amount};{note}\n");
        t.close();

        print(f"\nTallennettu: {uid};{date};{amount};{note}\n");

def listAll():
    print("Näytä talletukset: \n");
    l = 25;
    i=0;
    with open(csv, "r") as t:
        for row in t:
            i+=1;
            spl = row.split(";");
            uid = spl[0];
            d = spl[1];
            amt = spl[2];
            notes = spl[3];
            print(f"id: {uid} {"-"*l}")
            print(f"   {d}: {amt} € {f" | {notes}" if notes != "\n" else "\n"}");
        t.close();
    if(i == 0):
        print("Ei talletuksia");
    print();

def total():
    print("Tilin summa: \n");
    _sum = 0.0;
    with open(csv, "r") as t:
        for r in t:
            spl = r.split(";");
            s = float(spl[2]);
            _sum += s;
    print(f"{_sum} €\n");

def delete():
    print("Poista talletus ID:llä: \n");
    print("Millä ID:llä poistetaan?\nSelvität ID:n katsomalla listan talletuksista \n");
    print("- Voit poistaa KAIKKI talletukset syöttämällä: -kaikki-");
    print("- Voit palata valikkoon syöttämällä: 0")
    while(True):
        inp = input("ID: ");
        if(not inp.isnumeric() and inp != "-kaikki-"):
            print("ID on väärää muotoa. Tarkista syöte");
            continue;
        break;
    
    if(inp != "0"):
        if(inp == "-kaikki-"):
            open(csv, "w").close();
        
        else:
            arr = [];
            
            with open(csv, "r") as t:
                for r in t:
                    spl = r.split(";");
                    uid = spl[0];

                    if(uid != inp):
                        arr.append(r);
                t.close();
            
            open(csv, "w").close();
            
            with open(csv, "a") as t:
                for x in arr:
                    t.write(x);
            t.close();
        
        print();
        print(f"Poistettu id:llä {inp}" if inp != "-kaikki-" else "Kaikki poistettu");
    print();