from tkinter import *
import mysql.connector
db = mysql.connector.connect(host='localhost', port=3306, user='Bildesjef', passwd='oblig2024', db='oblig2024')

def brukerhåndtering_vindu():
    def legg_til_bruker_vindu():
        def legg_til_bruker():
            #Oppretter variabler for å hente verdiene
            brukerid = brukerid_entry.get()
            fornavn = fornavn_entry.get()
            etternavn = etternavn_entry.get()
            epost = epost_entry.get()
            
            #Oppretter cursor
            cursor = db.cursor()

            #SQL-spørring for å legge til i Bruker-tabellen
            sql_kode = "INSERT INTO Bruker (brukerid, fornavn, etternavn, epost) VALUES(%s, %s, %s, %s)"
            
            #Verdiene
            verdier = (brukerid, fornavn, etternavn, epost)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)
            
            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            # Lukk vinduet etter å ha lagt til bruker
            bruker_vindu.destroy()

        #Oppretter vindu
        bruker_vindu = Toplevel()
        bruker_vindu.title("Legg til ny bruker")

        #Legger til etiketter og inndatafelt
        brukerid_label = Label(bruker_vindu, text="BrukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5,sticky=W)
        brukerid_entry = Entry(bruker_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5,sticky=W)

        fornavn_label = Label(bruker_vindu, text="Fornavn:")
        fornavn_label.grid(row=1, column=0, padx=5, pady=5,sticky=W)
        fornavn_entry = Entry(bruker_vindu)
        fornavn_entry.grid(row=1, column=1, padx=5, pady=5,sticky=W)

        etternavn_label = Label(bruker_vindu, text="Etternavn:")
        etternavn_label.grid(row=2, column=0, padx=5, pady=5,sticky=W)
        etternavn_entry = Entry(bruker_vindu)
        etternavn_entry.grid(row=2, column=1, padx=5, pady=5,sticky=W)

        epost_label = Label(bruker_vindu, text="E-post:")
        epost_label.grid(row=3, column=0, padx=5, pady=5,sticky=W)
        epost_entry = Entry(bruker_vindu)
        epost_entry.grid(row=3, column=1, padx=5, pady=5,sticky=W)

        #Legger til en knapp for å legge til ny bruker
        legg_til_button = Button(bruker_vindu, text="Legg til bruker", command=legg_til_bruker)
        legg_til_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(bruker_vindu,text="Tilbake til brukermeny", command=bruker_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def endre_epost_vindu():
        def endre_epost():
            # Funksjon for å endre e-post på eksisterende bruker
            brukerid = brukerid_entry.get()
            ny_epost = ny_epost_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å oppdatere bruker-tabellen med ny epost
            sql_kode="UPDATE Bruker SET epost = %s WHERE brukerid = %s"

            #Verdier
            verdier=(ny_epost,brukerid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()

            #Lukker vinduet når eposten er oppdatert
            epost_vindu.destroy()

        #Oppretter vindu
        epost_vindu = Toplevel()
        epost_vindu.title("Endre e-post")

        #Oppretter label og inndatafelt i GUI
        brukerid_label = Label(epost_vindu, text="BrukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(epost_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        ny_epost_label = Label(epost_vindu, text="Ny epost:")
        ny_epost_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        ny_epost_entry = Entry(epost_vindu)
        ny_epost_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        endre_button = Button(epost_vindu,text="Endre e-post", command=endre_epost)
        endre_button.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(epost_vindu,text="Tilbake til brukermeny", command=epost_vindu.destroy)
        avslutt_button.grid(row=3, column=2, padx=5, pady=5, sticky=E)
    
    # GUI for brukerhåndterings-vindu
    brukerhåndtering_vindu = Toplevel()
    brukerhåndtering_vindu.title('Brukerhåndtering')

    # Legg til knapper for å legge til bruker og endre e-post
    legg_til_bruker_button = Button(brukerhåndtering_vindu, text="Legg til bruker", command=legg_til_bruker_vindu)
    legg_til_bruker_button.grid(row=0, column=0, padx= 5, pady=5, sticky=W)

    endre_epost_button = Button(brukerhåndtering_vindu, text="Endre e-post", command=endre_epost_vindu)
    endre_epost_button.grid(row=1, column=0, padx= 5, pady=5, sticky=W)

    avslutt_button = Button(brukerhåndtering_vindu, text="Tilbake til meny", command=brukerhåndtering_vindu.destroy)
    avslutt_button.grid(row=4, column=4, padx= 25, pady=5, sticky=E)

def bildehåndtering_vindu():
    def legg_til_bilde_vindu():
        def legg_til_bilde():
            #Oppretter variabler for å hente verdiene
            bildeid = bildeid_entry.get()
            beskrivelse = beskrivelse_entry.get()
            opplastetdato = opplastetdato_entry.get()
            fotograf = fotograf_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-koden for å legge inn nytt bilde i Bilde-tabellen
            sql_kode = "INSERT INTO Bilde (bildeid, beskrivelse, opplastetdato, fotograf) VALUES(%s, %s, %s, %s)"

            #Verdiene
            verdier = (bildeid, beskrivelse, opplastetdato, fotograf)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Comitter
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet etter å ha lagt til bilde
            bilde_vindu.destroy()

        #Oppretter vindu
        bilde_vindu = Toplevel()
        bilde_vindu.title("Legg til nytt bilde")

        #Legger til etiketter og inndatafelt for å legge til nytt bilde
        bildeid_label = Label(bilde_vindu, text="BildeID:")
        bildeid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(bilde_vindu)
        bildeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        beskrivelse_label = Label(bilde_vindu, text="Beskrivelse:")
        beskrivelse_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        beskrivelse_entry = Entry(bilde_vindu)
        beskrivelse_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        opplastetdato_label = Label(bilde_vindu, text="Opplastetdato:")
        opplastetdato_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        opplastetdato_entry = Entry(bilde_vindu)
        opplastetdato_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        fotograf_label = Label(bilde_vindu, text="Fotograf sin BrukerID:")
        fotograf_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        fotograf_entry = Entry(bilde_vindu)
        fotograf_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #Legger til en knapp for å legge til nytt bilde
        legg_til_button = Button(bilde_vindu, text="Legg til bilde", command=legg_til_bilde)
        legg_til_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(bilde_vindu,text="Tilbake til bildemeny", command=bilde_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)
    
    def endre_beskrivelse_vindu():
        def endre_beskrivelse():
            #Henter verdiene
            bildeid = brukerid_entry.get()
            ny_beskrivelse = ny_beskrivelse_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-spørring for å oppdatere beskrivelsen til et bilde i Bilde-tabellen
            sql_kode="UPDATE Bilde SET beskrivelse = %s WHERE bildeid = %s"

            #Verdiene
            verdier=(ny_beskrivelse,bildeid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
            
            #Lukker vinduet etter oppdateringen av beskrivelse er utført
            beskrivelse_vindu.destroy()
        
        #Oppretter vindu
        beskrivelse_vindu = Toplevel()
        beskrivelse_vindu.title("Endre bildebeskrivelse")

        #Oppretter inndata og visningsfelt i GUI
        brukerid_label = Label(beskrivelse_vindu, text="BildeID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(beskrivelse_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        ny_beskrivelse_label = Label(beskrivelse_vindu, text="Ny beskrivelse:")
        ny_beskrivelse_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        ny_beskrivelse_entry = Entry(beskrivelse_vindu)
        ny_beskrivelse_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Oppretter knapp for å endre bildebeskrivelse
        endre_button = Button(beskrivelse_vindu,text="Endre bildebeskrivelse", command=endre_beskrivelse)
        endre_button.grid(row=2, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(beskrivelse_vindu,text="Tilbake til bildemeny", command=beskrivelse_vindu.destroy)
        avslutt_button.grid(row=3, column=2, padx=5, pady=5, sticky=E)
    
    def legg_til_emneknagg_vindu():
        def legg_til_emneknagg():
            #Henter verdier
            emneknaggid = emneknaggid_entry.get()
            emneknaggen = emneknaggen_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å legge til ny emnetag
            sql_kode = "INSERT INTO Emneknagg (EmneknaggID, Emneknaggen) VALUES(%s, %s)"

            #Verdier
            verdier = (emneknaggid, emneknaggen)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet etter å ha lagt til emneknagg
            emneknagg_vindu.destroy()

        #Oppretter vindu
        emneknagg_vindu = Toplevel()
        emneknagg_vindu.title("Legg til emneknagg")

        #Legger til etiketter og inndatafelt i GUI
        emneknaggid_label = Label(emneknagg_vindu, text="EmneknaggID:")
        emneknaggid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        emneknaggid_entry = Entry(emneknagg_vindu)
        emneknaggid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        emneknaggen_label = Label(emneknagg_vindu, text="Emneknaggen:")
        emneknaggen_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        emneknaggen_entry = Entry(emneknagg_vindu)
        emneknaggen_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Legger til knapp
        legg_til_button = Button(emneknagg_vindu, text="Legg til emneknagg", command=legg_til_emneknagg)
        legg_til_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)
        
        avslutt_button = Button(emneknagg_vindu,text="Tilbake til bildemeny", command=emneknagg_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def like_vindu():
        def like():
            #Henter verdier
            bildeid = bildeid_entry.get()
            brukerid = brukerid_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å legge til likes i Likes-tabellen
            sql_kode = "INSERT INTO Likes (BildeID, BrukerID) VALUES(%s, %s)"

            #Verdiene
            verdier = (bildeid, brukerid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet etter likes er lagt til
            like_vindu.destroy()

        #Oppretter vindu
        like_vindu = Toplevel()
        like_vindu.title("Like et bilde")

        #Legger til etiketter og inndatafelt
        brukerid_label = Label(like_vindu, text="Oppgi din brukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(like_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        bildeid_label = Label(like_vindu, text="Oppgi bildeID du vil like:")
        bildeid_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(like_vindu)
        bildeid_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Legger til knapp 
        legg_til_button = Button(like_vindu, text="Like bildet", command=like)
        legg_til_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)
        
        avslutt_button = Button(like_vindu,text="Tilbake til bildemeny", command=like_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def slett_like_vindu():
        def slett_like():
            #Henter verdiene
            bildeid = bildeid_entry.get()
            brukerid = brukerid_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å slette likes fra likes-tabellen
            sql_kode = "DELETE FROM Likes WHERE BildeID = %s AND BrukerID = %s"

            #Verdiene
            verdier = (bildeid, brukerid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet
            slett_like_vindu.destroy()

        #Oppretter vindu
        slett_like_vindu = Toplevel()
        slett_like_vindu.title("Slett bilde like")

        #Legger til etiketter og inndatafelt 
        brukerid_label = Label(slett_like_vindu, text="Oppgi din brukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(slett_like_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        bildeid_label = Label(slett_like_vindu, text="Oppgi bildeID du vil slette like på:")
        bildeid_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(slett_like_vindu)
        bildeid_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Legger til knapp
        legg_til_button = Button(slett_like_vindu, text="Slett like", command=slett_like)
        legg_til_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(slett_like_vindu,text="Tilbake til bildemeny", command=slett_like_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)
    
    def legg_til_kommentar_vindu():
        def legg_til_kommentar():
            #Henter verdiene
            bildeid = bildeid_entry.get()
            brukerid = brukerid_entry.get()
            kommentaren = kommentaren_entry.get()   

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å legge til kommentar i Kommentar-tabellen
            sql_kode = "INSERT INTO Kommentar (BildeID, BrukerID, Kommentaren) VALUES(%s, %s, %s)"

            #Verdiene
            verdier = (bildeid, brukerid, kommentaren,)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()

            #Lukker vinduet
            kommentar_vindu.destroy()

        def sok_bilde():
            #Henter verdiene
            bildeid = bildeid_entry.get()

            #Oppretter cursor
            cursor0 = db.cursor()

            #Henter beskrivelse fra Bilde-tabellen
            sql_kode0 = "SELECT Beskrivelse, Opplastetdato FROM Bilde WHERE BildeID = %s"

            #Verdier
            verdier=(bildeid,)

            #Utfører spørringen med verdiene
            cursor0.execute(sql_kode0,verdier)

            #Henter det første resultatet fra spørringen
            resultat = cursor0.fetchone()

            #Henter beskrivelsen fra det første resultatet
            beskrivelsen = resultat[0]

            #Henter datoen fra det første resultatet
            datoen = resultat[1]

            #Setter verdien for beskrivelse
            b.set(beskrivelsen)

            #Setter verdien for dato
            d.set(datoen)

            #Committer
            db.commit()

            #Lukker cursor
            cursor0.close()
        
        #Oppretter vindu
        kommentar_vindu = Toplevel()    
        kommentar_vindu.title("Legg til kommentar")

        #Legger til etiketter, visningsfelt og inndatafelt 
        bildeid_label = Label(kommentar_vindu, text="BildeID:")
        bildeid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(kommentar_vindu)
        bildeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Legger til søk-knapp
        søk_bilde_button = Button(kommentar_vindu, text="Søk på bildet", command=sok_bilde)
        søk_bilde_button.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=E)
        
        b = StringVar()
        vis_beskrivelse_label = Entry(kommentar_vindu, textvariable=b, state="readonly")
        vis_beskrivelse_label.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        beskrivelsen_label=Label(kommentar_vindu,text="Beskrivelsen:")
        beskrivelsen_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        d = StringVar()
        vis_opplastetdato_label=Entry(kommentar_vindu, textvariable=d, state="readonly")
        vis_opplastetdato_label.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        opplastetdato_label=Label(kommentar_vindu,text="Opplastetdato:")
        opplastetdato_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        brukerid_label = Label(kommentar_vindu, text="Din BrukerID:")
        brukerid_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(kommentar_vindu)
        brukerid_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        kommentaren_label = Label(kommentar_vindu, text="Kommentaren:")
        kommentaren_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        kommentaren_entry = Entry(kommentar_vindu)
        kommentaren_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        #Legger til legg til kommentar-knapp
        legg_til_button = Button(kommentar_vindu, text="Legg til kommentar", command=legg_til_kommentar)
        legg_til_button.grid(row=6, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(kommentar_vindu,text="Tilbake til bildemeny", command=kommentar_vindu.destroy)
        avslutt_button.grid(row=7, column=2, padx=5, pady=5, sticky=E)
    
    def slett_kommentar_vindu():
        def slett_kommentar():
            #Henter verdier
            bildeid = bildeid_entry.get()
            brukerid = brukerid_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å slette kommentar fra Kommentar-tabellen
            sql_kode = "DELETE FROM Kommentar WHERE BildeID = %s AND BrukerID = %s"

            #Verdiene
            verdier = (bildeid, brukerid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet
            slett_like_vindu.destroy()

        #Oppretter vindu
        slett_kommentar_vindu = Toplevel()
        slett_kommentar_vindu.title("Slett kommentar")

        #Legger til etiketter og inndatafelt i GUI
        brukerid_label = Label(slett_kommentar_vindu, text="Oppgi din brukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        brukerid_entry = Entry(slett_kommentar_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        bildeid_label = Label(slett_kommentar_vindu, text="Oppgi bildeID du vil slette kommentar på:")
        bildeid_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(slett_kommentar_vindu)
        bildeid_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #Legger til en knapp for å slette kommentar
        slett_button = Button(slett_kommentar_vindu, text="Slett kommentar", command=slett_kommentar)
        slett_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)
        
        avslutt_button = Button(slett_kommentar_vindu,text="Tilbake til bildemeny", command=slett_kommentar_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def legg_til_tag_vindu():
        def legg_til_tag():
            #Henter verdier
            brukerid = brukerid_entry.get()
            bildeid = bildeid_entry.get()
            emneknaggid = emneknaggid_entry.get()
            
            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å finne brukerid i Bruker-tabellen
            bruker_sql_kode = "SELECT * FROM Bruker WHERE BrukerID = %s"

            #Verdier
            verdier = (brukerid,)

            #Utfører spørringen med sql koden og verdiene
            cursor.execute(bruker_sql_kode, verdier)

            #Henter resultatet
            bruker = cursor.fetchone()

            #Hvis bruker finnes skal denne koden kjøres og tag kan legges til
            if bruker:
                #Oppretter cursor
                cursor = db.cursor()

                #SQL-kode for å legge til i TagForBilde-tabellen
                sql_kode = "INSERT INTO TagForBilde (BildeID, EmneknaggID) VALUES(%s, %s)"

                #Verdiene
                verdier = (bildeid, emneknaggid)

                #Utfører spørringen med verdiene
                cursor.execute(sql_kode, verdier)

                #Committer
                db.commit()

                #Lukker cursor
                cursor.close()
        
            #Lukker vinduet etter å ha lagt til Tag
            tag_vindu.destroy()

        #Oppretter vindu
        tag_vindu = Toplevel()
        tag_vindu.title("Tag et bilde")

        #Legger til etiketter og inndatafelt
        brukerid_label = Label(tag_vindu,text="Oppgi din BrukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        brukerid_entry = Entry(tag_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        emneknaggid_label = Label(tag_vindu, text="Oppgi EmneknaggID:")
        emneknaggid_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        emneknaggid_entry = Entry(tag_vindu)
        emneknaggid_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        bildeid_label = Label(tag_vindu, text="Oppgi bildeID:")
        bildeid_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(tag_vindu)
        bildeid_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #Knapp for å legge til bildetag
        legg_til_button = Button(tag_vindu, text="Legg til bildetag", command=legg_til_tag)
        legg_til_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(tag_vindu,text="Tilbake til bildemeny", command=tag_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)
    
    def slett_tag_vindu():
        def slett_tag():
            #Henter verdier
            bildeid = bildeid_entry.get()
            emneknaggid = emneknaggid_entry.get()

            #Oppretter vursor
            cursor = db.cursor()
            #SQL-kode for å slette Tag fra TagForBilde-tabellen
            sql_kode = "DELETE FROM TagForBilde WHERE BildeID = %s AND EmneknaggID = %s"

            #Verdier
            verdier = (bildeid, emneknaggid)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Committer
            db.commit()

            #Lukker cursor
            cursor.close()
        
            #Lukker vinduet etter å ha slettet tag
            slett_tag_vindu.destroy()

        #Oppretter vindu
        slett_tag_vindu = Toplevel()
        slett_tag_vindu.title("Slett tag fra bilde")

        #Legger til etiketter og inndatafelt
        bildeid_label = Label(slett_tag_vindu, text="Oppgi bildeID:")
        bildeid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(slett_tag_vindu)
        bildeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        emneknaggid_label = Label(slett_tag_vindu, text="Oppgi EmneknaggID:")
        emneknaggid_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        emneknaggid_entry = Entry(slett_tag_vindu)
        emneknaggid_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)


        #Legger til knapp for slette bildetag
        legg_til_button = Button(slett_tag_vindu, text="Slett bildetag", command=slett_tag)
        legg_til_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(slett_tag_vindu,text="Tilbake til bildemeny", command=slett_tag_vindu.destroy)
        avslutt_button.grid(row=5, column=2, padx=5, pady=5, sticky=E)

    def slett_bilde_vindu():
        def slett_bilde():
            #Henter verdien 
            bildeid = bildeid_entry.get()

            #Oppretter cursor 
            cursor = db.cursor()
            
            #SQL-kode for å slette like fra Like-tabellen hvor bildeID er den gitte verdien
            sql_kode_likes = "DELETE FROM Likes WHERE BildeID = %s"

            #Verdier
            verdier = (bildeid,)

            #Utfører spørringen med verdier
            cursor.execute(sql_kode_likes, verdier)
            
            #SQL-kode for å slette like fra Like-tabellen hvor bildeID er den gitte verdien
            sql_kode_tag = "DELETE FROM TagForBilde WHERE BildeID = %s"

            #Utfører spørringen med verdier
            cursor.execute(sql_kode_tag, verdier)

            #SQL-kode for å slette kommentar fra Kommentar-tabellen
            sql_kode_kommentar = "DELETE FROM Kommentar WHERE BildeID = %s" #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            #Utfører spørringen med verdier
            cursor.execute(sql_kode_kommentar,verdier)

            #SQL-kode for å slette bilde fra Bilde-tabellen
            sql_kode_bilde = "DELETE FROM Bilde WHERE BildeID = %s"

            #Utfører spørringen med verdier
            cursor.execute(sql_kode_bilde, verdier)
        
            #Gjennomførere endringene og lukker cursor
            db.commit()
            cursor.close()

            #Lukker vinduet etter det er slettet
            slett_bilde_vindu.destroy()

        #Oppretter vindu
        slett_bilde_vindu = Toplevel()
        slett_bilde_vindu.title("Slett bilde")

        #Legger til etiketter og inndatafelt
        bildeid_label = Label(slett_bilde_vindu, text="Oppgi bildeID på bildet du vil slette:")
        bildeid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        bildeid_entry = Entry(slett_bilde_vindu)
        bildeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Legger til knapp for å slette bildet
        legg_til_button = Button(slett_bilde_vindu, text="Slett bildet", command=slett_bilde)
        legg_til_button.grid(row=1, column=2, padx=5, pady=5, sticky=E)

        avslutt_button = Button(slett_bilde_vindu,text="Tilbake til bildemeny", command=slett_bilde_vindu.destroy)
        avslutt_button.grid(row=2, column=2, padx=5, pady=5, sticky=E)

    #Oppretter vindu
    bildehåndtering_vindu = Toplevel()
    bildehåndtering_vindu.title('Bildehåndtering')

    #Legg til knapper for bildehåndterings-menyen
    legg_til_bilde_button = Button(bildehåndtering_vindu, text="Legg til bilde", command=legg_til_bilde_vindu)
    legg_til_bilde_button.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    endre_beskrivelse_button = Button(bildehåndtering_vindu, text="Endre bildebeskrivelse", command=endre_beskrivelse_vindu)
    endre_beskrivelse_button.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    legg_til_emneknagg_button = Button(bildehåndtering_vindu, text="Legg til emneknagg",command=legg_til_emneknagg_vindu)
    legg_til_emneknagg_button.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    like_bilde_button = Button(bildehåndtering_vindu, text="Like et bilde",command=like_vindu)
    like_bilde_button.grid(row=3, column=0, padx=5, pady=5, sticky=W)

    slett_bilde_like_button = Button(bildehåndtering_vindu, text="Slett like på bilde",command=slett_like_vindu)
    slett_bilde_like_button.grid(row=4, column=0, padx=5, pady=5, sticky=W)

    legg_til_kommentar_button = Button(bildehåndtering_vindu, text="Legg til kommentar på bilde",command=legg_til_kommentar_vindu)
    legg_til_kommentar_button.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    
    slett_kommentar_button = Button(bildehåndtering_vindu, text="Slett kommentar på bilde",command=slett_kommentar_vindu)
    slett_kommentar_button.grid(row=6, column=0, padx=5, pady=5, sticky=W)

    legg_til_bildetag_button = Button(bildehåndtering_vindu, text="Legg til bildetag",command=legg_til_tag_vindu)
    legg_til_bildetag_button.grid(row=7, column=0, padx=5, pady=5, sticky=W)

    slett_bildetag_button = Button(bildehåndtering_vindu, text="Slett bildetag",command=slett_tag_vindu)
    slett_bildetag_button.grid(row=8, column=0, padx=5, pady=5, sticky=W)

    slett_bilde_button = Button(bildehåndtering_vindu, text="Slett bilde",command=slett_bilde_vindu)
    slett_bilde_button.grid(row=9, column=0, padx=5, pady=5, sticky=W)
    
    avslutt_button = Button(bildehåndtering_vindu, text="Tilbake til meny",command=bildehåndtering_vindu.destroy)
    avslutt_button.grid(row=11, column=4, padx= 25, pady=5, sticky=E)

def oversikt_vindu():
    def oversikt_bruker_vindu():
        def sok_bilder():
            #Henter brukerID fra inndatafeltet som tilsvarer Fotograf
            brukerid = brukerid_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-spørring. Velger beskrivelse basert på ID bruker skriver inn (brukerid = fotograf)
            sql_kode="SELECT Beskrivelse FROM Bilde WHERE Fotograf = %s"

            #Definerer verdiene som skal settes inn i spørringen
            verdier=(brukerid,)

            #Utfører SQL-spørringen
            cursor.execute(sql_kode,verdier)

            #Henter alle resultatene fra spørringen i variabelen 'bilder'
            bilder = cursor.fetchall()

            #Lukker cursor
            cursor.close()

            #Tømmer bildelisten før jeg legger til nye verdier
            bilde_liste.delete(0, END)
            
            #Intererer gjennom resultatene fra spørringen og legger til 'Beskrivelse' i liste
            for bilde in bilder:
                bilde_liste.insert(END, bilde[0])
        
        
        def hentden(valgt_beskrivelse_string):
            #Oppretter cursor
            cursor = db.cursor()

            #Henter bildeID fra bildetabellen
            sql_kode="SELECT BildeID FROM Bilde WHERE Beskrivelse = %s"

            #Verdier
            verdier = (valgt_beskrivelse_string,)

            #Utfører spørringen med verdiene
            cursor.execute(sql_kode, verdier)

            #Henter resultatene (bildeid)
            bildeid = cursor.fetchall()

            #Lukker cursor
            cursor.close()

            #Returnerer det første elementet (bildeid)
            return bildeid[0]


        def vis_kommentarer(event):
            # Hent det valgte bildet fra listen og får indeksene til de valgte bildene
            valgt_bilde = bilde_liste.curselection()

            #Hvis bruker trykker på et bilde (beskrivelse)
            if valgt_bilde:
                #Får verdien til det valgte bildet
                valgt_beskrivelse = bilde_liste.get(valgt_bilde)

                valgt_beskrivelse_string = str(valgt_beskrivelse)

                hentbildeid = hentden(valgt_beskrivelse_string)
                
                #Oppretter cursor
                cursor = db.cursor()

                #SQL-spørring for å hente kommentarer til det valgte bildet
                sql_kode="SELECT Kommentaren FROM Kommentar WHERE BildeID = %s"

                #Verdiene for spørringen
                verdier = (hentbildeid)

                #Utfører spørringen
                cursor.execute(sql_kode, verdier)

                #Henter alle kommentarer
                kommentarer = cursor.fetchall()

                #Lukker cursor
                cursor.close()
                
                #Tømmer kommentar listen for verdier før jeg legger til
                kommentar_liste.delete(0,END)

                #Legger til kommentarene i kommentarlisten 
                for kommentar in kommentarer:
                    kommentar_liste.insert(END, kommentar[0])

        #Oppretter et hovedvindu
        brukeroversikt_vindu = Toplevel()
        brukeroversikt_vindu.title("Bruker sine bilder")


        ####################################################################################

        #Oppretter liste for å vise bilder
        bilde_liste = Listbox(brukeroversikt_vindu)
        bilde_liste.grid(row=2, column=0,padx=5,pady=5, sticky=W)

        #Oppretter scrollbar og kobler denne til bilde_liste
        scrollbar1=Scrollbar(brukeroversikt_vindu, orient=VERTICAL, command=bilde_liste.yview)
        scrollbar1.grid(row=2, column=1, rowspan=5, padx=(0,100), sticky=NS)

        scrollbar1["command"]=bilde_liste.yview


        ####################################################################################

        #Oppretter liste for å vise kommentarer
        kommentar_liste = Listbox(brukeroversikt_vindu)
        kommentar_liste.grid(row=2, column=2, padx=5,pady=5, sticky=W)

        #Oppretter scrollbar og kobler denne til kommentar_liste
        scrollbar=Scrollbar(brukeroversikt_vindu, orient=VERTICAL, command=kommentar_liste.yview)
        scrollbar.grid(row=2, column=3, rowspan=5, padx=(0,100), sticky=NS)

        scrollbar["command"]=kommentar_liste.yview

        ####################################################################################

        bilde_beskrivelse = Label(brukeroversikt_vindu, text="Bildebeskrivelse:")
        bilde_beskrivelse.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        bilde_kommentar = Label(brukeroversikt_vindu, text="Kommentarer:")
        bilde_kommentar.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        #Legger til etiketter og inndatafelt
        brukerid_label = Label(brukeroversikt_vindu, text="BrukerID:")
        brukerid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        brukerid_entry = Entry(brukeroversikt_vindu)
        brukerid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Lager knapp for å søke etter bilder
        sok_button = Button(brukeroversikt_vindu, text="Søk på bruker", command=sok_bilder)
        sok_button.grid(row=0, column=2, padx=5, pady=5, sticky=E)

        #Lager knapp for å gå tilbake til menyen
        avslutt_button = Button(brukeroversikt_vindu, text="Tilbake til oversikt", command=brukeroversikt_vindu.destroy)
        avslutt_button.grid(row=3, column=3, padx=5, pady=5, sticky=E)

        #Listeboks
        bilde_liste.bind("<<ListboxSelect>>", vis_kommentarer)

    def søk_bilde_vindu ():
        def sok_bildeid():
            #Henter bildeid fra inndatafeltet
            bildeid = bildeid_entry.get()

            #Oppretter cursor
            cursor = db.cursor()

            #SQL-spørring. Velger kommentarene basert på BildeID bruker skriver inn
            sql_kode="SELECT Kommentaren FROM Kommentar WHERE BildeID = %s"

            #Definerer verdiene som skal settes inn i spørringen
            verdier=(bildeid,)

            #Utfører SQL-spørringen
            cursor.execute(sql_kode,verdier)

            #Henter alle resultatene fra spørringen i variabelen 'kommentarer'
            kommentarer = cursor.fetchall()

            #Lukker cursor
            cursor.close()

            #Tømmer kommentarlisten før jeg legger til nye verdier
            kommentar_liste.delete(0, END)
            
            #Intererer gjennom resultatene fra spørringen og legger til kommentar i liste
            for kommentar in kommentarer:
                kommentar_liste.insert(END, kommentar[0])
        
        def hentden(valgt_kommentar_string):
            #Oppretter cursor
            cursor = db.cursor()

            #SQL-kode for å hente BrukerID
            sql_kode="SELECT BrukerID From Kommentar WHERE Kommentaren =%s "

            #Verdier
            verdier = (valgt_kommentar_string,)

            #Utfører spørringen
            cursor.execute(sql_kode,verdier)

            #Henter resultat fra spørring (brukerid)
            brukerid = cursor.fetchall()

            #Lukker cursor
            cursor.close()

            #Returnerer første element fra resultat (brukerid)
            return brukerid[0]

        def vis_brukerinfo (event):
            trykk_kommentar = kommentar_liste.curselection()
            if trykk_kommentar:
                #Henter verdien til kommentar og lager den til en string og tar den med videre til en annen funksjon
                valgt_kommentar = kommentar_liste.get(trykk_kommentar)
                valgt_kommentar_string = str(valgt_kommentar)
                hentbrukerID = hentden(valgt_kommentar_string)

                #Oppretter cursor
                cursor = db.cursor()
                
                #SQL-spørring for å hente fornavn og etternavn til bruker
                sql_kode = "SELECT Fornavn, Etternavn FROM Bruker WHERE BrukerID = %s"

                #Verdiene for spørringen
                verdier = (hentbrukerID)

                #Utfører spørringen
                cursor.execute(sql_kode,verdier)

                #Henter all brukerinformasjon
                brukerinformasjon = cursor.fetchall()

                #Lukker cursor
                cursor.close()

                #Tømmer brukerlisten for verdier før jeg legger til
                bruker_liste.delete(0,END)
                
                #Legger til fornavn og etternavn i kommentarlisten
                for bruker in brukerinformasjon:
                    bruker_liste.insert(END, bruker[0] + " " + bruker[1])

        #Oppretter et hovedvindu
        bildeoversikt_vindu = Toplevel()
        bildeoversikt_vindu.title("Bildet sine kommentarer")
        
        ############################################################################################

        #Oppretter liste for å vise kommentarer
        kommentar_liste = Listbox(bildeoversikt_vindu)
        kommentar_liste.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        #Oppretter scrollbar og kobler denne til kommentar_liste
        scrollbar=Scrollbar(bildeoversikt_vindu, orient=VERTICAL, command=kommentar_liste.yview)
        scrollbar.grid(row=2, column=1, rowspan=5, padx=(0,100), pady=5, sticky=NS)

        scrollbar["command"]=kommentar_liste.yview

        ############################################################################################

        #Oppretter liste for å vise brukerinformasjon
        bruker_liste = Listbox(bildeoversikt_vindu)
        bruker_liste.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        #Oppretter scrollbar og kobler denne til bruker_liste
        scrollbar1=Scrollbar(bildeoversikt_vindu, orient=VERTICAL, command=bruker_liste.yview)
        scrollbar1.grid(row=2, column=3, rowspan=5, padx=(0,100), sticky=NS)

        scrollbar1["command"]=bruker_liste.yview

        ############################################################################################

        bilde_kommentar = Label(bildeoversikt_vindu, text="Kommentarer:")
        bilde_kommentar.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        bilde_bruker = Label(bildeoversikt_vindu, text="Brukerinformasjon:")
        bilde_bruker.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        #Legger til etiketter og inndatafelt
        bildeid_label = Label(bildeoversikt_vindu, text="BildeID:")
        bildeid_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        bildeid_entry = Entry(bildeoversikt_vindu)
        bildeid_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #Lager knapp for å søke etter bilder
        sok_button = Button(bildeoversikt_vindu, text="Søk på bilde", command=sok_bildeid)
        sok_button.grid(row=0, column=2, padx=5, pady=5, sticky=E)

        #Lager knapp for å gå tilbake til menyen
        avslutt_button = Button(bildeoversikt_vindu, text="Tilbake til oversikt", command=bildeoversikt_vindu.destroy)
        avslutt_button.grid(row=3, column=3, padx=5, pady=5, sticky=E)

        #Listeboks
        kommentar_liste.bind("<<ListboxSelect>>", vis_brukerinfo)

    #Knapp i oversiktvindu for å komme til rett funksjon
    oversikt_vindu = Tk()
    oversikt_vindu.title('Oversikt og søk')

    se_bruker_button=Button(oversikt_vindu,text='Søk på bruker',command=oversikt_bruker_vindu)
    se_bruker_button.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    søk_bilde_button=Button(oversikt_vindu,text="Søk på bilde",command=søk_bilde_vindu)
    søk_bilde_button.grid(row=1, column=0,padx=5,pady=5, sticky=W)

    avslutt_button = Button(oversikt_vindu, text="Tilbake til meny", command=oversikt_vindu.destroy)
    avslutt_button.grid(row=4, column=4, padx= 25, pady=5, sticky=W)

#Menysystemet kodes inn i main
def main():
    #Oppretter vindu
    window = Tk()
    window.title('Meny')
    
    #GUI
    brukerhåndtering_button = Button(window, text="Brukerhåndtering", command=brukerhåndtering_vindu)
    brukerhåndtering_button.grid(row=1, column=0, padx= 5, pady=5, sticky=W)

    bildehåndtering_button = Button(window, text="Bildehåndtering", command=bildehåndtering_vindu)
    bildehåndtering_button.grid(row=2, column=0, padx= 5, pady=5, sticky=W)

    søkoversikt_button = Button(window, text="Søk og oversikt", command=oversikt_vindu)
    søkoversikt_button.grid(row=4, column=0, padx= 5, pady=5, sticky=W)

    avslutt_button = Button(window, text="Avslutt program", command=window.destroy)
    avslutt_button.grid(row=6, column=1, padx= 25, pady=5, sticky=W)

    window.mainloop()

main()