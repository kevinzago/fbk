# FBK - Docker + Flask + RESTful + SQLite

L’applicazione descritta in seguito deve essere resa disponibile attraverso un repository git pubblico che comprenda tutti i file necessari al progetto (programma python, dockerfile, docker-compose e continuous integration) ed un file README che descriva nel dettaglio il lavoro svolto in tutti i passaggi, gli strumenti utilizzati, le procedure da seguire per eseguire l’applicazione e le istruzioni per testarne il funzionamento.
Verranno valutati tutti gli aspetti della consegna: dall’implementazione alla documentazione e all’uso di tutti gli strumenti scelti, con particolare attenzione alla sicurezza nell’implementazione di tutti i passaggi e componenti.

## Principali componenti 

Flask è un framework basato su Python. È un micro-framework utilizzato dagli sviluppatori Python per creare API. Si chiama micro framework perché consente agli sviluppatori, ad esempio, di aggiungere autenticazione personalizzata e qualsiasi altro sistema di back-end in base alle preferenze.

I principali componeneti utilizzati sono:

- Flask (1.1.2)
- Docker (alpine:latest) 
- Python 3.7.3
- Insomnia (API Testing Tools) 
- Database Service (SQLite) connettore SQL Alchemy (app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db')

## Descrizione 

E' stato sviluppato un servizio di database utilizzando il db SQLite che permette agli utenti di accedervi tramite un'API REST utilizzando metodi HTTP come POST, PUT e GET. 


## Token Web JSON 

Il token Web JSON, noto anche come JWT , è il modo sicuro di trasferire token casuali tra due parti o entità. JWT è uno standard Open per creare chiavi (token) di accesso tra un server e un client.
JSON è generalmente composto da tre parti come segue: 

- Payload
- Header
- Signature

E' stato utilizzato JWT per creare un server web Flask con autorizzazione JWT. JWT diventa uno standard di autorizzazione e comunicazione tra SPA e web server.Viene utilizzato per gestire l'autenticazione in Flask con l'utilizzo della libreria flask-jwt-extended. flask-jwt-extended è un’estensione di flask per gestire l’autenticazione usando JWT.

Un JWT è un token Web JSON, è un insieme di dati codificati in una lunga stringa. I dati codificati contengono elementi come:

Un isscampo, che viene generalmente utilizzato per identificare in modo univoco l'utente che ha generato questo JWT;
Un jticampo, che è un identificatore univoco per questo JWT (non per l'utente!);
Un algcampo, che definisce quale algoritmo è stato utilizzato per codificare questo JWT;
Un expcampo, che contiene un timestamp della data di scadenza di questo JWT;
Dati arbitrari che vogliamo includere in esso (chiamati "reclami").

flask-jwt-extended:  https://flask-jwt-extended.readthedocs.io/en/stable/

-> user.py

from flask_jwt_extended import

    1. create_access_token,            
    2. create_refresh_token,           
    3. jwt_refresh_token_required,     
    4. get_jwt_identity,               
    5. jwt_required,
    6. get_raw_jwt,
    7. get_jwt_claims


1. CREAZIONE ACCESS TOKEN;
2. CREAZIONE REFRESH TOKEN;
3. DECORATORE PER PROTEGERRE UN ENDPOINT  (si assicurerà che il richiedente abbia un token di aggiornamento valido prima di 
   consentire la chiamata dell'endpoint);
4. RESTITUISCE L'IDENTITA' DEL JWT che accede a questo endpoint. Se non è presente alcun JWT, viene invece restituito 
   "None";
5. TOKEN ACCESSO VALIDO REQUISITO  Se si decora un endpoint con questo, si assicurerà che il richiedente abbia 
   un token di accesso valido prima di consentire la chiamata dell'endpoint. Ciò non controlla la validità del token di 
   accesso;
6. CREAZIONE ENDPOINT PROTETTO questo restituirà il dizionario Python che ha tutte le rivendicazioni del JWT che accede 
   all'endpoint. Se non è presente alcun JWT, viene invece restituito un dict vuoto;
7. CLAIMS RESTITUISCE IL DIZIONARIO delle attestazioni personalizzate nel JWT che accede all'endpoint
   Se non sono presenti richieste personalizzate dell'utente, viene invece restituito un dict vuoto.

## REST APIs with Flask and Python

L'API (interfaccia di programmazione dell'applicazione) consente la comunicazione tra due applicazioni per recuperare o inviare i dati. Flask-RESTful è un'estensione per Flask che aggiunge il supporto per la creazione rapida di API REST. È un'astrazione leggera che funziona con i tuoi ORM / librerie esistenti.

Librerie utilizzate per la creazione REST APIs: 

     1.from flask_restful import Api
     2.from flask_restful import Resource, reqparse 
     3.from werkzeug.security import safe_str_cmp
     4.from blacklist import BLACKLIST
     
     


## Struttura della nostra API REST

     STRUTTURA FILE PROGETTO






app.py:
In app.pyinizializzeremo e configureremo la nostra applicazione Flask. Configureremo anche le nostre risorse API.
Questo file è il punto di accesso alla nostra API REST;
_______
db.py:
In questo file creeremo il nostro oggetto database Python;

_________________________
cartella models/user.py:
UserModel è la definizione dei dati finale nella nostra API. 
Contengono: id; user; password; info;

____________________________
cartella resources/user.py: 
Queste risorse sono abbastanza diverse dalle altre due perché non si occupano solo della creazione e dell'aggiornamento dei dati nella nostra applicazione, ma si occupano anche delle specifiche migliorative di vari flussi di utenti come autenticazione, aggiornamento token, disconnessione e altro ancora.
- In caso di login/password errati deve restituire un errore
- In caso di token sbagliato deve restituire errore
- Il token deve avere una validità temporale limitata (esempio 10 minuti)
- In alternativa alla scadenza temporale del token un endpoint: /logout per chiudere la sessione
  ed annullare il token dell’utente

  
## Approfondimento: risorse dell'utente

Le risorse (API) utente implementate sono:

      1. Create Admin con l’utente admin e relativa password (Token) - (POST) - /admin
      2. Inserire attraverso il webservice (all’endpoint: /adduser ) un nuovo utente con i campi user, password e   
         info (nel database) - (POST) - /adduser
      3. Effettuare una richiesta verso il webservice (endpoint: /info ) usando il token preventivamente ricevuto                      per avere le informazioni sull’utente - GET - /info
      4. Autenticazione dei normali utenti (non admin) verso il webservice (all’endpoint: /auth ) -(POST) - /auth
      5. Token refresh - (POST) - /refresh
      6. Logout per chiudere la sessione ed annullare il token dell’utente. - (POST) - /logout

La maggior parte di queste risorse risponde alle POST richieste in quanto è il metodo utilizzato per rispondere a dati arbitrari e non necessariamente per creare modelli e salvarli nel nostro server. 

          Indirizzo URL è http://localhost:8080/
          
          
Ogni risorsa è una classe che definisce alcuni metodi. Ogni metodo corrisponde a un verbo HTTP (GET e POST utilizzati).

Il codice di stato HTTP più comune non è 404, come molti pensano! Sono infatti 200, che significa "OK".

Alcuni altri sono:

200 OK
201 CREATED
301 PERMANENT REDIRECT
400 BAD REQUEST
401 UNAUTHORIZED
404 NOT FOUND
500 INTERNAL SERVER ERROR


API: 

    1. Create Admin con l’utente admin e relativa password (Token)

    api.add_resource(TokenAdmin, '/admin')

 
 L'utente Admin con la relativa password (token) viene creato facendo una richiesta POST. 
 
 POST ->  http://localhost:8080/admin
 
 ![](immagini/1.png)


 






    2.Inserire attraverso il webservice (all’endpoint: /adduser ) un nuovo utente con i campi user, password e info (nel  
    database)
    
    api.add_resource(UserRegister, '/adduser')

L'Admin attraverso la richesta POST -> http://localhost:8080/adduser crea un nuovo utente inviando un JSON con i seguenti campi (user, password e info) per la creazione di un nuovo utente nel db. 
Un messaggio di errore avverte l'utente ADMIN della revoca del token (password admin) "The token has expired."

![](immagini/2.png)







L'Admin per creare un nuovo utente deve possedere la password (token) valida di tipo Bearer e inserila nel campo TOKEN: 
Un messaggio 201 avverte che il nuovo utente è stato creato. "message": "User created successfully."


![](immagini/3.png)









Questa risorsa esamina i dati passati dalla richiesta e crea un nuovo UserModel a meno che non esista già un utente con quel nome.

![](immagini/13.png)





La crittografia è un must quando si tratta di dati sensibili o password. E' stata utilizzata libreria di crittografia chiamata passlib, per crittografare le password prima di salvarle nel database.

     from passlib.context import CryptContext

     pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
     )



    3.Effettuare una richiesta verso il webservice (endpoint: /info ) usando il token preventivamente ricevuto per avere le         informazioni sull’utente
    
    api.add_resource(User, '/info/<int:user_id>')

Effettuando una richiesta all'endpoint /info http://localhost:8080/info/1 e inserendo dopo /info/n (n=1) si ha il primo utente e con (n=2) si ha il secondo utente (n=3) si ha il terzo ... E' necessario inserire il token valido nel campo TOKEN di tipo Bearer, se l'utente non inserisce il token un messaggio di errore: error": "invalid_token", "message": "Signature verification failed." 401 avvisa l'utente. Una volta inserto un token valido è possibile visualizzare le informazioni sull'utente (200).

![](immagini/4.png)


![](immagini/5.png)





Questa risorsa viene utilizzata per recuperare gli utenti esistenti.

![](immagini/14.png)







    4. Autenticazione dei normali utenti (non admin) verso il webservice (all’endpoint: /auth ) 

    api.add_resource(UserLogin, '/auth')

L'utente effettuando una richiesta POST http://localhost:8080/auth è possibile autenticarsi.
 
Questa risorsa utilizza Flask-JWT-Extended per generare un JWT (noto anche come token di accesso) e un token di aggiornamento per un determinato utente.

I JWT contengono payload codificati (idcampo dell'utente ) che possiamo quindi utilizzare per recuperare a quale utente è destinato il JWT quando ritorna in un'altra richiesta.

Questa risorsa controlla la combinazione nome user / password / info per assicurarsi che sia corretta.

Si noti che il token di accesso restituito da questo metodo viene creato con la create_access_token funzione, con il fresh=True parametro. Poiché questo endpoint risponde direttamente al login (auth) dell'utente, il token di accesso restituito sarà sempre aggiornato.

Viene restituito:

     {
        "access_token":      
                     "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODY5NDUwNDYsIm5iZiI6MTU4Njk0NTA0NiwianRpIjoiYmRiNjk3NmItMjZmMy00ODM3LTkzNWMtM2U1N2JiOTA0YWFiIiwiZXhwIjoxNTg2OTQ1OTQ2LCJpZGVudGl0eSI6MSwiZnJlc2giOnRydWUsInR5cGUiOiJhY2Nlc3MiLCJ1c2VyX2NsYWltcyI6eyJpc19hZG1pbiI6dHJ1ZX19.6GRG8uE3R8DXkP7MSEbRvMCvQuwXigDsZHq0Ec-GdOw",
  
        "refresh_token":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODY5NDUwNDYsIm5iZiI6MTU4Njk0NTA0NiwianRpIjoiMDJjNGRkMDAtYmY2Yy00MTEzLTkyMWQtMTUwNzc3MTUyNzAwIiwiZXhwIjoxNTg5NTM3MDQ2LCJpZGVudGl0eSI6MSwidHlwZSI6InJlZnJlc2gifQ.-je1eJntW2ctrcIrEK3uKAPyMnGTBjDPoKHRNa05Plk",
       
        "user_id": 1
      }

![](immagini/6.png)
 

![](immagini/7.png)


![](immagini/8.png)
 
      
    5.Token refresh

    api.add_resource(TokenRefresh, '/refresh')

Questa risorsa accetta un token di aggiornamento e ci fornisce un token di accesso non aggiornato.

I token di accesso in genere scadono dopo circa 10 minuti dalla loro generazione (alcuni durano più a lungo, a volte fino a qualche giorno). L'aggiornamento token consente alle applicazioni che utilizzano l'API di continuare a richiedere nuovi token di accesso senza che l'utente debba continuare ad accedere più volte.

Tuttavia, questo ci dà token non-fresh tokens. . Se abbiamo un'operazione altamente sensibile e vogliamo ricontrollare che l'utente sia effettivamente loro, abbiamo bisogno che accedano di nuovo. In tal caso, possiamo contrassegnare qualsiasi endpoint che richiede un nuovo token di accesso (fresh access token).

L'utente inserendo nel campo TOKEN (Bearer) il prprio refresh_token ricevuto durante l'operazione di login (auth), è possibile effettuare una chiamata POST http://localhost:8080/refresh per ottenere il nuovo token valido "access_token".

![](immagini/9.png)

![](immagini/10.png)







    6.Logout per chiudere la sessione ed annullare il token dell’utente

    api.add_resource(UserLogout, '/logout')

La risorsa UserLogout utilizza la lista nera (BLACKLIST). Quando un utente invia una richiesta a questa risorsa, salviamo l'identificatore univoco del suo token di accesso (che è diverso dal suo utente id!) Nella lista nera (BLACKLIST), in modo che quel token di accesso specifico non possa essere riutilizzato.

liberia utilizzata: 
from blacklist import BLACKLIST

Se vogliono accedere di nuovo, possono —> verrà generato un nuovo token di accesso.


![](immagini/11.png)




Questo utilizza la get_raw_jwt()funzione di Flask-JWT-Extended. Ci dà un dizionario delle varie proprietà memorizzate all'interno del JWT decodificato.

Se l'utente non inserisce nel campo TOKEN (Bearer) un token valido o effettua una richiesta con un token non valido, un messaggio di errore 401 avvisa l'utente che: 

1."error": "invalid_token", "message": "Signature verification failed."

2."description": "The token has been revoked.", "error": "token_revoked"




![](immagini/12.png)

## DB SQLite creazione e configurazione dell'app

Il UserModel è molto simile a quello ItemModel, perché in realtà non fa nulla da sola.

È solo un contenitore di dati (db), con alcuni metodi di supporto che ci semplificano la vita.

Impostiamo alcuni parametri di configurazione. In questa app stiamo impostando:

SQLALCHEMY_DATABASE_URI: quale database vogliamo usare. Stiamo usando SQLite.

SQLALCHEMY_TRACK_MODIFICATIONS: una configurazione per Flask-SQLAlchemy che tiene traccia delle modifiche ai modelli SQLAlchemy. 

PROPAGATE_EXCEPTIONS: un parametro di configurazione quasi completamente non documentato di Flask, è necessario che le eccezioni Flask-RESTful vengano visualizzate nella nostra app come errori invece di arrestare in modo anomalo il nostro server con un generico "Internal Server Error").

JWT_BLACKLIST_ENABLED: se abilitare o meno la lista nera in Flask-JWT-Extended. È necessario per consentire agli utenti di disconnettersi.

JWT_BLACKLIST_TOKEN_CHECKS: quali token per confrontare con la lista nera. Esistono due: access tokens e refresh tokens.

## CREAZIONE TABELLA NEL DB

La tabella users viene creata nel db SQLite format 3 utlizzando il connettore SQLALCHEMY. Un file data.db viene creato
per salvare gli utenti con le seguenti valori:

    # file data.db
    id INTEGER NOT NULL, 
	user VARCHAR(80), 
	password VARCHAR(80), 
	info VARCHAR(80), 
	PRIMARY KEY (id)

    # app.py
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    @app.before_first_request
    def create_tables():
       db.create_all()


    class UserModel(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80))
    password = db.Column(db.String(80))
    info = db.Column(db.String(80))


    def __init__(self, user, password, info):
        self.user = user
        self.password = password
        self.info = info
            
    def encrypt_password(self):
        return pwd_context.encrypt(self.password)


    def check_encrypted_password(self, hashed):
        return pwd_context.verify(self.password, hashed)   
    

    def json(self):
        return {
            'id': self.id,
            'user': self.user,
            'password': self.password,
            'info': self.info,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user):
        return cls.query.filter_by(user=user).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()




