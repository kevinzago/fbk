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
- Database Service (SQLite) connettore SQL Alchemy : app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

## Descrizione 

E' stato sviluppato un servizio di database utilizzando il db SQLite che permette agli utenti di accedervi tramite un'API REST utilizzando metodi HTTP come POST, PUT e GET. 


## Token Web JSON 

Il token Web JSON, noto anche come JWT , è il modo sicuro di trasferire token casuali tra due parti o entità. JWT è uno standard Open per creare chiavi (token) di accesso tra un server e un client.
JSON è generalmente composto da tre parti come segue: 

- Payload
- Header
- Signature

E' stato utilizzato JWT per creare un server web Flask con autorizzazione JWT. JWT diventa uno standard di autorizzazione e comunicazione tra SPA e web server.Viene utilizzato per gestire l'autenticazione in Flask con l'utilizzo della libreria flask-jwt-extended. flask-jwt-extended è un’estensione di flask per gestire l’autenticazione usando JWT.

flask-jwt-extended:  https://flask-jwt-extended.readthedocs.io/en/stable/

## REST APIs with Flask and Python

L'API (interfaccia di programmazione dell'applicazione) consente la comunicazione tra due applicazioni per recuperare o inviare i dati. 

Librerie utilizzate per la creazione REST APIs: 





Struttura della nostra API REST

-app.py: inizializzazioe e configurazione la nostra applicazione Flask e le nostre risorse API.Questo file è il punto di 
         accesso alla nostra API REST;
- 









• Con l’utente admin e relativa password (che non sono presenti nel database) si possa inserire attraverso il webservice (all’endpoint: /adduser ) un nuovo utente con i campi user, password e info (nel database mariadb/mysql)
• Autenticazione dei normali utenti (non admin) verso il webservice (all’endpoint: /auth ) con utente e password (che devono risiedere nel database mariadb/mysql) che deve restituire un token di autenticazione in caso di successo
• effettuare una richiesta verso il webservice (endpoint: /info ) usando il token preventivamente ricevuto per avere le informazioni sull’utente (che si trovano nel database mariadb/mysql)
• La password di admin deve poter essere passata come parametro all’avvio del programma










