import tkinter as tk

#inicializa el nodo 
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
    # Inserta un nuevo nodo al arbol
    def insert(self, key):
        self.root = self._insert(self.root, key)
    # Insersion de manera recursiva
    def _insert(self, root, key):
        # Si no hay nodo raiz entonces convierte el nodo insertado en el nodo padre
        if not root:
            return AVLNode(key)
        # Si el nodo insertado es menor a la raiz lo inserta a la izquierda
        elif key < root.key:
            root.left = self._insert(root.left, key)
        # Si no entonces entonces lo inserta a la derecha     
        else:
            root.right = self._insert(root.right, key)
        # Actualiza la altura del nodo y verifica que se encuentre balanceado
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)
      
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    # Obtiene el peso del nodo actual
    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)
    # Hace una rotacion a la derecha,"z" ahora sera el hijo derecho del nodo "y" y ahora el 
    # subarbol derecho del nodo "y" sera el subarbol derecho del nodo "z", despues actualiza
    # la altura de los nodos "y" y "z"
    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y
    # Hace una rotacion a la izquierda, el nodo "y" ahora es hijo izquierdo del nodo "z" y ahora 
    # el subarbol izquierdo del nodo "z" sera el subarbol izquiedo del nodo "y", a continuacion 
    # se actualiza la altura de los nodos "z" y "" y
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2
          
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

#Crea la interfaz grafica para insertar nodos y visualizarlo
class AVLApp:
    def __init__(self):
        self.avl_tree = AVLTree()
        self.window = tk.Tk()
        self.window.title("Balanceo de arboles AVL")
       
        self.input_frame = tk.Frame(self.window)
        self.input_frame.pack(pady=10)
        # Coloca la etiqueta a la izquierda del input
        self.input_label = tk.Label(self.input_frame, text="Valor del nodo:")
        self.input_label.pack(side=tk.LEFT)
        
        self.input_entry = tk.Entry(self.input_frame, width=10)
        self.input_entry.pack(side=tk.LEFT)

        self.insert_button = tk.Button(self.window, text="Introducir", command=self.insert_value)
        self.insert_button.pack(pady=10)
        # Define el alto y el ancho en frame.
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        self.draw_tree()
    #Se encarga de dibujar el arbol
    def draw_tree(self):
        self.canvas.delete("all")
        if self.avl_tree.root:
            self._draw_node(self.avl_tree.root, 400, 30, 400)
    #Se encarga de dibujar cada nodo
    def _draw_node(self, node, x, y, x_offset):
        # Define si ira a la derecha o a la izquierda
        if node.left:
            x_left = x - x_offset // 2
            y_left = y + 60
            self.canvas.create_line(x, y, x_left, y_left)
            self._draw_node(node.left, x_left, y_left, x_offset // 2)
        # Define si ira a la derecha
        if node.right:
            x_right = x + x_offset // 2
            y_right = y + 60
            self.canvas.create_line(x, y, x_right, y_right)
            self._draw_node(node.right, x_right, y_right, x_offset // 2)

        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="gray")
        self.canvas.create_text(x, y, text=str(node.key))
    # Recibe un valor que se pasa como argumento a la funcion insertar nodo
    # A continuacion dibuja el arbol de nuevo.
    def insert_value(self):
        value = int(self.input_entry.get())
        self.avl_tree.insert(value)
        self.draw_tree()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    # Inicia la interfaz grafica
    app = AVLApp()
    # Inicia el bucle para dibujar el arbol y sus respectivos nodos
    app.run()

