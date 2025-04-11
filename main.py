from avl_tree import AVLTree
from bst_tree import BSTree
from data_generator import generate_sorted_data
from utils import measure_time
from tree_visualizer import export_tree_to_graphviz

def print_menu():
    print("1. Wczytaj dane z klawiatury (n ≤ 10)")
    print("2. Wygeneruj dane (losowe, posortowane)")
    print("3. Utwórz drzewo AVL")
    print("4. Utwórz drzewo BST")
    print("5. Wypisz ścieżkę do min/max (AVL i BST)")
    print("6. Wypisz in-order i pre-order (AVL i BST)")
    print("7. Usuń wszystkie elementy post-order (AVL i BST)")
    print("8. Równoważ BST (algorytm DSW)")
    print("10. Wizualizacja")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def main():
    avl = AVLTree()
    bst = BSTree()
    avl_root = None
    bst_root = None
    data = []

    while True:
        print_menu()
        choice = input("Wybierz opcję: ")

        if choice == '1':
            try:
                data = list(map(int, input("Podaj liczby oddzielone spacją: ").split()))
                if len(data) > 10:
                    print("\033[91mPodano zbyt wiele liczb.\033[0m")
                    data = []
            except:
                print("\033[91mSprawdź poprawność wprowadzonych danych\033[0m")
        elif choice == '2':
            try:
                n = int(input("Ile liczb wygenerować? "))
                data = generate_sorted_data(n)
                print_green(f"Wygenerowano: {data}")
            except:
                print("\033[91mNieprawidłowe n.\033[0m")
        elif choice == '3':
            avl_root, t = measure_time(avl.insert_balanced, data)
            print_green(f"AVL utworzone, wysokość: {avl.max_depth(avl_root)}, czas: {t:.6f}s")
        elif choice == '4':
            import time
            bst_root = None
            start = time.perf_counter()
            for d in data:
                bst_root = bst.insert(bst_root, d)
            t = time.perf_counter() - start
            print_green(f"BST utworzone, wysokość: {bst.max_depth(bst_root)}, czas: {t:.6f}s")
        elif choice == '5':
            print_green(f"AVL min path: {avl.find_min_path(avl_root)}")
            print_green(f"AVL max path: {avl.find_max_path(avl_root)}")
            print_green(f"BST min path: {bst.find_min_path(bst_root)}")
            print_green(f"BST max path: {bst.find_max_path(bst_root)}")
        elif choice == '6':
            print_green(f"AVL in-order: {avl.in_order(avl_root)}")
            print_green(f"AVL pre-order: {avl.pre_order(avl_root)}")
            print_green(f"BST in-order: {bst.in_order(bst_root)}")
            print_green(f"BST pre-order: {bst.pre_order(bst_root)}")
        elif choice == '7':
            print_green(f"AVL usunięto: {avl.post_order_delete(avl_root)}")
            print_green(f"BST usunięto: {bst.post_order_delete(bst_root)}")
            avl_root = None
            bst_root = None
        elif choice == '8':
            bst_root = bst.dsw_balance(bst_root)
            print_green("BST zrównoważone.")
        elif choice == '10':
            if avl_root:
                dot = export_tree_to_graphviz(avl_root, tree_type="AVL")
                dot.render('AVL_Tree', view=True)
            if bst_root:
                dot = export_tree_to_graphviz(bst_root, tree_type="BST")
                dot.render('BST_Tree', view=True)
        elif choice == '11':
            print_green("Zamykanie programu.")
            break
        else:
            print("\033[91mNieznana opcja.\033[0m")

if __name__ == "__main__":
    main()