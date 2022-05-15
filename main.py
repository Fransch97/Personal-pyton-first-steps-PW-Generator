print("Ciao user !")

print("Pronto a creare una password sicura?")

#functions
def gen_pw(name,lstname, age):
    passwordList = set()
    finish_pw = ""
    for i in name :
        if " " == i :
            i = ""
        passwordList.update(i)
    for i in lstname :
        if " " == i :
            i = ""
        passwordList.update(i)
    for i in age :
        if " " == i :
            i = ""
        passwordList.update(i)
    for x in passwordList :
        finish_pw += x
    return finish_pw

#list's
aprove = ["si","perfetto","esatto","grande","ok","yes","tutto giusto"]
not_aprove = ["no","nope","not","sbagliato","sbagliatissimo"]
err_name_list = ["nome", "name", "nomi"]
err_lstname_list = ["cognome", "cognom", "cognomi","lastname"]
err_age_list = ["età", "age", "anni", "eta"]
err_everthing = ["tutti", "tutte", "tutto","ovunque"]

running = False

name, lastname, age = input("Inserisci il tuo nome : "),input("Inserisci il tuo cognome : "),input("Inserisci la tua età : ")

while not running :
    print("il tuo nome è " , name , "\nil tuo cognome è", lastname,"\ne la tua età è ", age)
    approval = input("tutto giusto? : ")

    if approval in aprove :
        print("ottimo generiamo la tua password dammi un attimo...")
        running = True
    if approval in not_aprove :
        ask_err = input("in qualle domanda abbiamo sbagliato? nome cognome oppoure nella età?: ")
        if ask_err in err_name_list :
            name = input("Reinscerisci il tuo nome : ")
        elif ask_err in err_lstname_list :
            lastname = input("Reinscerisci il tuo cognome : ")
        elif ask_err in err_age_list :
            age = input("Reinscerisci il tuo età : ")
        elif ask_err in err_everthing :
            name, lastname, age = input("Inserisci il tuo nome : "),input("Inserisci il tuo cognome : "),input("Inserisci la tua età : ")
        else :
            print("\nattualmente non abbiamo una soluzione al tuo problema riavvia il sofware")


password = gen_pw(name, lastname, age)

print("La tua nuova password : " ,password )