import flet as ft

NODE_WIDTH = 45
NODE_HEIGHT = 28
NULL_WIDTH = 30
NULL_HEIGHT = 16
Y_STEP = 60  


class NODE:
    def __init__(self, key=None):
        self.key = key
        self.data = None
        self.color = "BLACK"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = NODE()
        self.NIL.color = "BLACK"
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL    
        self.history = []

    def log_state(self, msg,highlight_key=None):
        print(f"[RBT LOG]: {msg}")

        def clone_tree(node,parent_clone,nil_clone):
            if node == self.NIL:
                return nil_clone
            new_node = NODE(node.key)
            new_node.color = node.color
            new_node.parent = parent_clone
            new_node.left = clone_tree(node.left, new_node, nil_clone)
            new_node.right = clone_tree(node.right, new_node, nil_clone)
            return new_node

        nil_clone = NODE()
        nil_clone.color = "BLACK"
        nil_clone.left = nil_clone
        nil_clone.right = nil_clone
        root_clone = clone_tree(self.root, nil_clone, nil_clone)
        self.history.append((root_clone, msg, highlight_key))


    def left_rotate(self, x):
        y = x.right
        if y == self.NIL: return
        
        x.right = y.left
        if y.left != self.NIL: y.left.parent = x
            
        y.parent = x.parent
        if x.parent == self.NIL: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
            
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        if x == self.NIL: return
        
        y.left = x.right
        if x.right != self.NIL: x.right.parent = y
            
        x.parent = y.parent
        if y.parent == self.NIL: self.root = x
        elif y == y.parent.left: y.parent.left = x
        else: y.parent.right = x
            
        x.right = y
        y.parent = x

def rbt_view_practice(page: ft.Page, algorithm: str, mode: str, hints_enabled: bool):
    page.title = "Red Black Tree Practice"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 1200

    title_text = ft.Text(
        "Red Black Tree Practice",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE
    )

    subtitle_text = ft.Text(
        "Practice your Red Black Tree skills by performing insertions and deletions.",
        size=16,
        color=ft.Colors.WHITE
    )