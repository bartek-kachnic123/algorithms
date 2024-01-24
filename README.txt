========================================================================
Autor: Bartłomiej Kachnic,                           Krakow, 24.01.2024
========================================================================

* Zawartosc:
============

Katalog bst zawiera:
--------------------------------------------------------------------

I.     Implementacja algorytmu DSW w klasie BinarySearchTree.

            1) bst.py - zawiera klasy BinarySearchTree i Node
            2) main.py - program z przykłądem użycia DSW
            3) tests.py - zawiera testy metod z klasy BinarySearchTree



* Klasa BinarySearchTree
=========================

-> BinarySearchTree(root=None) - (konstruktor domyślny) - tworzy nowe drzewo o korzeniu głównym
  wartości domyślnej None.

-> is_empty(): (sprawdzenie czy drzewo nie zawiera elementów) - zwraca true, jeśli root
  jest równy None, w przeciwnym wypadku
  zwraca false.

-> search(data): (wyszukanie elementu zawierającego data) - zwraca Node, jeśli znajdzie w
   drzewie node z szukanym elementem data, w przeciwnym wypadku
  zwraca None.

-> clear(): (wyszyszczenie drzewa) - ustawia  root na None.

-> insert(data) (dodaje Node o elemencie data do drzewa) - dodaje element po odpowiedniej
    stronie drzewa i zwraca dodany obiekt Node.

-> remove(data) (usuwanie Node o elemencie Node) - usuwa i zwraca Node z drzewa, jeśli
 został odnaleziony, w przeciwnym wypadku zwraca None

-> travelUp(node, level=1): (szukanie poprzedników) - zwraca poprzednika, który był o określoną
    liczbę level w górę (domyślnie 1 zwraca rodzica) aż do samego roota.

-> height() - zwraca aktualną wysokośc drzewa

-> inorder() - generator zwracający node z kolejnością inorder

-> printPreorder() - wypisuje node.data z kolejnością preorder

-> printInorder() - wypisuje node.data z kolejnością inorder

-> balanceBST() - wykorzystuje algorytm DSW:
    -* Najpierw tworzy pusty Node o nazwie pseudo_root z wkazaniem right na root
    -* Następnie bstToVine - zmienia strukturę drzewa na vine (sorted linked list) za pomocą prawych rotacji
    -* Wykonuje compress(pseudo_root, count - m) - wykonuje tyle lewych rotacji ile jest liści
    -* Kolejno compress - przywraca strukturę drzewa za pomocą lewych rotacji
    -* Zapisuje root jako pseudo_root.right i usuwa stworzonego pustego Node pseudo_root