Il codice all' esecuzione chiederà 3 informazioni:
1)Se desideriamo applicare un min-conflicts senza inizializzazione dei colori o usare il metodo di Brelaz per assegnare un colore ad ogni nodo: nel primo caso digitare 0, altrimenti 1;
2)Quanti nodi desideriamo che la mappa abbia: inserire numero intero maggiore o uguale a 6. I test da me svolti sono stati fatti su mappe con numero nodi n=30,60,90,120,150,180;
3)Se desideriamo un grafo scarsamente connesso (con un numero di archi uguale a 2 volte il numero di nodi) o un grafo densamente connesso (numero archi m=n*(n-1)/4, dove n è il numero di nodi): 
      digitare 0 per il primo caso ed 1 per il secondo.

Se la scelta sarà ricaduta su un min-conflicts senza Brelaz, i risultati ottenuti si baseranno su 1000 esecuzioni del min-conflicts sulla stessa mappa.
Se scegliamo di applicare Brelaz, l'esecuzioni saranno 100 nel caso del grafo scarsamente connesso e 10 nel caso densamente connesso.

Ogni esecuzione del programma equivale all'instanziazione di un grafo, quindi dove nella relazione si parla di 3 istanze (grafo scarsamente connesso), vuol dire che ho eseguito 3 volte il programma per ogni n desiderato, 
      mentre dove si parla di 8 istanze (grafi densamente connessi) ho eseguito il programma 8 volte per ogni n desiderato.

