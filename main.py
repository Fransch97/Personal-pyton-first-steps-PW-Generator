print("Ciao user !")

print("Pronto a creare una password sicura?")

def gen_pw(name,lstname, age):
    passwordList = set()
    finish_pw = ""
    for i in name :
        passwordList.update(i)
    for i in lstname :
        passwordList.update(i)
    for i in age :
        passwordList.update(i)
    for x in passwordList :
        finish_pw += x
    return finish_pw

name, lastname, age = input("Inserisci il tuo nome : "),input("Inserisci il tuo cognome : "),input("Inserisci la tua età : ")

print("il tuo nome è " , name , "\nil tuo cognome è", lastname,"\ne la tua età è ", age)

approval = input("tutto giusto? : ")

aprove = ["si","perfetto","esatto","grande","ok","yes","tutto giusto"]
not_aprove = ["no","nope","not","sbagliato","sbagliatissimo"]
err_name_list = ["nome", "name", "nomi"]
err_lstname_list = ["cognome", "cognom", "cognomi","lastname"]
err_age_list = ["cognome", "cognom", "cognomi"]
err_everthing = ["tutti", "tutte", "tutto","ovunque"]

print("\n\n\n\n\n\n\n\n\n\n")

if approval in aprove :
    print("ottimo generiamo la tua password dammi un attimo...")
if approval in not_aprove :
    print("riproviamo allora!")
    print("al prossimo sbaglio dovrai ricaricare il programma!")
    ask_err = input("in qualle domanda abbiamo sbagliato? nome cognome oppoure nella età?: ")
    if ask_err in err_name_list :
        name = input("Reinscerisci il tuo nome : ")
    if ask_err in err_lstname_list :
        lastname = input("Reinscerisci il tuo cognome : ")
    if ask_err in err_lstname_list :
        age = input("Reinscerisci il tuo età : ")
    if ask_err in err_everthing :
        name, lastname, age = input("Inserisci il tuo nome : "),input("Inserisci il tuo cognome : "),input("Inserisci la tua età : ")
    else :
        print("\nattualmente non abbiamo una soluzione al tuo problema riavvia il sofware")


password = gen_pw(name, lastname, age)

print("bi bo bi...")
print("Chi è il bot migliore...")
print("a giusto sono io...")
print("cosa stavo facendo?")
print("LOL quasi dimenticavo la tua password...")

print("La tua nuova password : " ,password )