#traccia 2
#web server multithread

import signal, sys
import http.server
import socketserver

host = 'localhost'

#prende come porta un valore passato in input da terminale, o mette come default la porta 8080.
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

# server che consente la connessione di più utenti tramite la gestione di thread. Quando un  
# nuovo utente si collega al server è il metodo SimpleHTTPRequestHandler che si occupa di gestire 
# il multithreading e consegna la pagina richiesta al client.
serverHTTP = socketserver.ThreadingTCPServer((host,port), http.server.SimpleHTTPRequestHandler)

def CloseSignal_Handler(signal, frame):
    try:
      if( serverHTTP ):
        serverHTTP.server_close()
    finally:
      sys.exit(0)
    
def main():
    #inizializzo il thread per le connessioni multiple
    serverHTTP.daemon_threads = True 
    #permetto il riusco delle connessioni
    serverHTTP.allow_reuse_address = True
    #interrompe se, da terminale o da tastiera, viene interrotta l'esecuzione. Normalmente effettuata con Ctrl+C
    signal.signal(signal.SIGINT, CloseSignal_Handler)
    
    try:
        while True:
            #sys.stdout.flush()
            serverHTTP.serve_forever()
    except KeyboardInterrupt:
        pass

    serverHTTP.server_close()
    
    
if __name__ == "__main__":
    main()