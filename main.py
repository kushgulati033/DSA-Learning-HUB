import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
from collections import deque
import threading
import random


class Node:
    """Node class for linked list and tree structures"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None


class LinkedList:
    """Implementation of a singly linked list"""

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev


class Stack:
    """Implementation of a stack using list"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return str(self.items) if self.items else "Empty"


class Queue:
    """Implementation of a queue using deque"""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return str(list(self.items)) if self.items else "Empty"


class BinarySearchTree:
    """Implementation of a Binary Search Tree"""

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node is not None

        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


class SortingAlgorithms:
    """Collection of sorting algorithms"""

    @staticmethod
    def bubble_sort(arr, callback=None):
        n = len(arr)
        arr_copy = arr.copy()
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                if callback:
                    callback(arr_copy.copy())
        return arr_copy

    @staticmethod
    def selection_sort(arr, callback=None):
        n = len(arr)
        arr_copy = arr.copy()
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            if callback:
                callback(arr_copy.copy())
        return arr_copy

    @staticmethod
    def insertion_sort(arr, callback=None):
        arr_copy = arr.copy()
        for i in range(1, len(arr_copy)):
            key = arr_copy[i]
            j = i - 1
            while j >= 0 and key < arr_copy[j]:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            arr_copy[j + 1] = key
            if callback:
                callback(arr_copy.copy())
        return arr_copy


class DSAGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Learning Hub - Interactive GUI")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')

        # Data structures
        self.linked_list = LinkedList()
        self.stack = Stack()
        self.queue = Queue()
        self.bst = BinarySearchTree()

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.setup_gui()

    def configure_styles(self):
        """Configure custom styles for the GUI"""
        self.style.configure('Title.TLabel',
                             font=('Arial', 24, 'bold'),
                             foreground='#ecf0f1',
                             background='#2c3e50')

        self.style.configure('Heading.TLabel',
                             font=('Arial', 14, 'bold'),
                             foreground='#3498db',
                             background='#34495e')

        self.style.configure('Custom.TButton',
                             font=('Arial', 10, 'bold'),
                             padding=10)

        self.style.configure('Success.TLabel',
                             font=('Arial', 12),
                             foreground='#27ae60',
                             background='#34495e')

        self.style.configure('Error.TLabel',
                             font=('Arial', 12),
                             foreground='#e74c3c',
                             background='#34495e')

    def setup_gui(self):
        """Setup the main GUI layout"""
        # Main title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x', padx=20, pady=10)
        title_frame.pack_propagate(False)

        title_label = ttk.Label(title_frame, text="🚀 DSA Learning Hub", style='Title.TLabel')
        title_label.pack(expand=True)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)

        # Create tabs
        self.create_linked_list_tab()
        self.create_stack_tab()
        self.create_queue_tab()
        self.create_bst_tab()
        self.create_sorting_tab()
        self.create_search_tab()

    def create_linked_list_tab(self):
        """Create the linked list tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='📋 Linked List')

        # Title
        title = ttk.Label(frame, text="Linked List Operations", style='Heading.TLabel')
        title.pack(pady=10)

        # Display area
        self.ll_display = tk.Text(frame, height=4, width=80, bg='#ecf0f1', fg='#2c3e50',
                                  font=('Consolas', 12), state='disabled')
        self.ll_display.pack(pady=10)

        # Input frame
        input_frame = tk.Frame(frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Value:", bg='#34495e', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        self.ll_entry = tk.Entry(input_frame, font=('Arial', 10), width=20)
        self.ll_entry.pack(side='left', padx=5)

        # Buttons frame
        button_frame = tk.Frame(frame, bg='#34495e')
        button_frame.pack(pady=20)

        buttons = [
            ("Append", self.ll_append, '#27ae60'),
            ("Prepend", self.ll_prepend, '#3498db'),
            ("Delete", self.ll_delete, '#e74c3c'),
            ("Reverse", self.ll_reverse, '#f39c12'),
            ("Clear", self.ll_clear, '#95a5a6')
        ]

        for text, command, color in buttons:
            btn = tk.Button(button_frame, text=text, command=command,
                            bg=color, fg='white', font=('Arial', 10, 'bold'),
                            width=10, relief='flat', cursor='hand2')
            btn.pack(side='left', padx=5)

        # Status label
        self.ll_status = ttk.Label(frame, text="Ready", style='Success.TLabel')
        self.ll_status.pack(pady=10)

        self.update_ll_display()

    def create_stack_tab(self):
        """Create the stack tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='📚 Stack')

        title = ttk.Label(frame, text="Stack Operations (LIFO)", style='Heading.TLabel')
        title.pack(pady=10)

        # Visual stack display
        self.stack_canvas = tk.Canvas(frame, width=200, height=300, bg='#ecf0f1')
        self.stack_canvas.pack(side='left', padx=20, pady=20)

        # Right side controls
        controls_frame = tk.Frame(frame, bg='#34495e')
        controls_frame.pack(side='right', fill='both', expand=True, padx=20)

        # Display area
        self.stack_display = tk.Text(controls_frame, height=6, width=40, bg='#ecf0f1', fg='#2c3e50',
                                     font=('Consolas', 12), state='disabled')
        self.stack_display.pack(pady=10)

        # Input
        input_frame = tk.Frame(controls_frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Value:", bg='#34495e', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        self.stack_entry = tk.Entry(input_frame, font=('Arial', 10), width=15)
        self.stack_entry.pack(side='left', padx=5)

        # Buttons
        button_frame = tk.Frame(controls_frame, bg='#34495e')
        button_frame.pack(pady=20)

        buttons = [
            ("Push", self.stack_push, '#27ae60'),
            ("Pop", self.stack_pop, '#e74c3c'),
            ("Peek", self.stack_peek, '#3498db'),
            ("Clear", self.stack_clear, '#95a5a6')
        ]

        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(button_frame, text=text, command=command,
                            bg=color, fg='white', font=('Arial', 10, 'bold'),
                            width=8, relief='flat')
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

        self.stack_status = ttk.Label(controls_frame, text="Ready", style='Success.TLabel')
        self.stack_status.pack(pady=10)

        self.update_stack_display()

    def create_queue_tab(self):
        """Create the queue tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='🔄 Queue')

        title = ttk.Label(frame, text="Queue Operations (FIFO)", style='Heading.TLabel')
        title.pack(pady=10)

        # Display area
        self.queue_display = tk.Text(frame, height=4, width=80, bg='#ecf0f1', fg='#2c3e50',
                                     font=('Consolas', 12), state='disabled')
        self.queue_display.pack(pady=10)

        # Input
        input_frame = tk.Frame(frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Value:", bg='#34495e', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        self.queue_entry = tk.Entry(input_frame, font=('Arial', 10), width=20)
        self.queue_entry.pack(side='left', padx=5)

        # Buttons
        button_frame = tk.Frame(frame, bg='#34495e')
        button_frame.pack(pady=20)

        buttons = [
            ("Enqueue", self.queue_enqueue, '#27ae60'),
            ("Dequeue", self.queue_dequeue, '#e74c3c'),
            ("Front", self.queue_front, '#3498db'),
            ("Clear", self.queue_clear, '#95a5a6')
        ]

        for text, command, color in buttons:
            btn = tk.Button(button_frame, text=text, command=command,
                            bg=color, fg='white', font=('Arial', 10, 'bold'),
                            width=10, relief='flat')
            btn.pack(side='left', padx=5)

        self.queue_status = ttk.Label(frame, text="Ready", style='Success.TLabel')
        self.queue_status.pack(pady=10)

        self.update_queue_display()

    def create_bst_tab(self):
        """Create the BST tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='🌳 BST')

        title = ttk.Label(frame, text="Binary Search Tree", style='Heading.TLabel')
        title.pack(pady=10)

        # Display area
        self.bst_display = tk.Text(frame, height=6, width=80, bg='#ecf0f1', fg='#2c3e50',
                                   font=('Consolas', 12), state='disabled')
        self.bst_display.pack(pady=10)

        # Input
        input_frame = tk.Frame(frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Value (integer):", bg='#34495e', fg='white', font=('Arial', 10)).pack(side='left',
                                                                                                          padx=5)
        self.bst_entry = tk.Entry(input_frame, font=('Arial', 10), width=20)
        self.bst_entry.pack(side='left', padx=5)

        # Buttons
        button_frame = tk.Frame(frame, bg='#34495e')
        button_frame.pack(pady=20)

        buttons = [
            ("Insert", self.bst_insert, '#27ae60'),
            ("Search", self.bst_search, '#3498db'),
            ("Random Fill", self.bst_random, '#f39c12'),
            ("Clear", self.bst_clear, '#95a5a6')
        ]

        for text, command, color in buttons:
            btn = tk.Button(button_frame, text=text, command=command,
                            bg=color, fg='white', font=('Arial', 10, 'bold'),
                            width=12, relief='flat')
            btn.pack(side='left', padx=5)

        self.bst_status = ttk.Label(frame, text="Ready", style='Success.TLabel')
        self.bst_status.pack(pady=10)

        self.update_bst_display()

    def create_sorting_tab(self):
        """Create the sorting algorithms tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='🔄 Sorting')

        title = ttk.Label(frame, text="Sorting Algorithms", style='Heading.TLabel')
        title.pack(pady=10)

        # Input area
        input_frame = tk.Frame(frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Numbers (space-separated):", bg='#34495e', fg='white', font=('Arial', 10)).pack()
        self.sort_entry = tk.Entry(input_frame, font=('Arial', 10), width=50)
        self.sort_entry.pack(pady=5)
        self.sort_entry.insert(0, "64 34 25 12 22 11 90")

        tk.Button(input_frame, text="Generate Random", command=self.generate_random_array,
                  bg='#9b59b6', fg='white', font=('Arial', 10, 'bold'), relief='flat').pack(pady=5)

        # Algorithm buttons
        algo_frame = tk.Frame(frame, bg='#34495e')
        algo_frame.pack(pady=10)

        algorithms = [
            ("Bubble Sort", lambda: self.run_sort("bubble"), '#e74c3c'),
            ("Selection Sort", lambda: self.run_sort("selection"), '#27ae60'),
            ("Insertion Sort", lambda: self.run_sort("insertion"), '#3498db')
        ]

        for text, command, color in algorithms:
            btn = tk.Button(algo_frame, text=text, command=command,
                            bg=color, fg='white', font=('Arial', 10, 'bold'),
                            width=15, relief='flat')
            btn.pack(side='left', padx=5)

        # Results area
        results_frame = tk.Frame(frame, bg='#34495e')
        results_frame.pack(fill='both', expand=True, pady=10)

        tk.Label(results_frame, text="Results:", bg='#34495e', fg='white', font=('Arial', 12, 'bold')).pack(anchor='w')

        self.sort_results = scrolledtext.ScrolledText(results_frame, height=15, width=100,
                                                      bg='#ecf0f1', fg='#2c3e50', font=('Consolas', 10))
        self.sort_results.pack(fill='both', expand=True, pady=5)

        self.sort_status = ttk.Label(frame, text="Ready", style='Success.TLabel')
        self.sort_status.pack(pady=5)

    def create_search_tab(self):
        """Create the search algorithms tab"""
        frame = tk.Frame(self.notebook, bg='#34495e')
        self.notebook.add(frame, text='🔍 Search')

        title = ttk.Label(frame, text="Search Algorithms", style='Heading.TLabel')
        title.pack(pady=10)

        # Input area
        input_frame = tk.Frame(frame, bg='#34495e')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Array (space-separated):", bg='#34495e', fg='white', font=('Arial', 10)).pack()
        self.search_array_entry = tk.Entry(input_frame, font=('Arial', 10), width=50)
        self.search_array_entry.pack(pady=5)
        self.search_array_entry.insert(0, "1 5 8 12 15 20 25 30 35 40")

        tk.Label(input_frame, text="Target:", bg='#34495e', fg='white', font=('Arial', 10)).pack()
        self.search_target_entry = tk.Entry(input_frame, font=('Arial', 10), width=20)
        self.search_target_entry.pack(pady=5)
        self.search_target_entry.insert(0, "25")

        # Algorithm buttons
        algo_frame = tk.Frame(frame, bg='#34495e')
        algo_frame.pack(pady=20)

        tk.Button(algo_frame, text="Linear Search", command=lambda: self.run_search("linear"),
                  bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), width=15, relief='flat').pack(side='left',
                                                                                                      padx=10)

        tk.Button(algo_frame, text="Binary Search", command=lambda: self.run_search("binary"),
                  bg='#27ae60', fg='white', font=('Arial', 10, 'bold'), width=15, relief='flat').pack(side='left',
                                                                                                      padx=10)

        # Results area
        self.search_results = scrolledtext.ScrolledText(frame, height=20, width=100,
                                                        bg='#ecf0f1', fg='#2c3e50', font=('Consolas', 10))
        self.search_results.pack(fill='both', expand=True, pady=10)

        self.search_status = ttk.Label(frame, text="Ready", style='Success.TLabel')
        self.search_status.pack(pady=5)

    # Linked List Methods
    def ll_append(self):
        value = self.ll_entry.get().strip()
        if value:
            self.linked_list.append(value)
            self.ll_entry.delete(0, tk.END)
            self.update_ll_display()
            self.ll_status.config(text=f"Appended '{value}'", style='Success.TLabel')
        else:
            self.ll_status.config(text="Please enter a value", style='Error.TLabel')

    def ll_prepend(self):
        value = self.ll_entry.get().strip()
        if value:
            self.linked_list.prepend(value)
            self.ll_entry.delete(0, tk.END)
            self.update_ll_display()
            self.ll_status.config(text=f"Prepended '{value}'", style='Success.TLabel')
        else:
            self.ll_status.config(text="Please enter a value", style='Error.TLabel')

    def ll_delete(self):
        value = self.ll_entry.get().strip()
        if value:
            if self.linked_list.delete(value):
                self.update_ll_display()
                self.ll_status.config(text=f"Deleted '{value}'", style='Success.TLabel')
            else:
                self.ll_status.config(text=f"'{value}' not found", style='Error.TLabel')
            self.ll_entry.delete(0, tk.END)
        else:
            self.ll_status.config(text="Please enter a value", style='Error.TLabel')

    def ll_reverse(self):
        self.linked_list.reverse()
        self.update_ll_display()
        self.ll_status.config(text="List reversed", style='Success.TLabel')

    def ll_clear(self):
        self.linked_list = LinkedList()
        self.update_ll_display()
        self.ll_status.config(text="List cleared", style='Success.TLabel')

    def update_ll_display(self):
        self.ll_display.config(state='normal')
        self.ll_display.delete(1.0, tk.END)
        display_text = f"Linked List: {self.linked_list.display()}\n"
        display_text += f"Operations: append, prepend, delete, reverse\n"
        display_text += "Visual: HEAD -> " + self.linked_list.display().replace(" -> ", " -> ") + " -> NULL"
        self.ll_display.insert(1.0, display_text)
        self.ll_display.config(state='disabled')

    # Stack Methods
    def stack_push(self):
        value = self.stack_entry.get().strip()
        if value:
            self.stack.push(value)
            self.stack_entry.delete(0, tk.END)
            self.update_stack_display()
            self.stack_status.config(text=f"Pushed '{value}'", style='Success.TLabel')
        else:
            self.stack_status.config(text="Please enter a value", style='Error.TLabel')

    def stack_pop(self):
        popped = self.stack.pop()
        if popped is not None:
            self.update_stack_display()
            self.stack_status.config(text=f"Popped '{popped}'", style='Success.TLabel')
        else:
            self.stack_status.config(text="Stack is empty", style='Error.TLabel')

    def stack_peek(self):
        top = self.stack.peek()
        if top is not None:
            self.stack_status.config(text=f"Top element: '{top}'", style='Success.TLabel')
        else:
            self.stack_status.config(text="Stack is empty", style='Error.TLabel')

    def stack_clear(self):
        self.stack = Stack()
        self.update_stack_display()
        self.stack_status.config(text="Stack cleared", style='Success.TLabel')

    def update_stack_display(self):
        # Update text display
        self.stack_display.config(state='normal')
        self.stack_display.delete(1.0, tk.END)
        display_text = f"Stack (LIFO): {self.stack.display()}\n"
        display_text += f"Size: {self.stack.size()}\n"
        display_text += f"Top: {self.stack.peek() if not self.stack.is_empty() else 'None'}\n"
        display_text += "Operations: push (add to top), pop (remove from top)"
        self.stack_display.insert(1.0, display_text)
        self.stack_display.config(state='disabled')

        # Update visual display
        self.stack_canvas.delete("all")
        items = self.stack.items
        box_height = 30
        box_width = 120
        start_y = 280

        for i, item in enumerate(reversed(items)):
            y = start_y - i * (box_height + 5)
            # Draw box
            self.stack_canvas.create_rectangle(40, y, 40 + box_width, y + box_height,
                                               fill='#3498db', outline='#2980b9', width=2)
            # Draw text
            self.stack_canvas.create_text(40 + box_width // 2, y + box_height // 2,
                                          text=str(item), font=('Arial', 10, 'bold'), fill='white')

        if items:
            # Draw "TOP" arrow
            self.stack_canvas.create_text(180, start_y - (len(items) - 1) * (box_height + 5) + box_height // 2,
                                          text="← TOP", font=('Arial', 10, 'bold'), fill='#e74c3c')

    # Queue Methods
    def queue_enqueue(self):
        value = self.queue_entry.get().strip()
        if value:
            self.queue.enqueue(value)
            self.queue_entry.delete(0, tk.END)
            self.update_queue_display()
            self.queue_status.config(text=f"Enqueued '{value}'", style='Success.TLabel')
        else:
            self.queue_status.config(text="Please enter a value", style='Error.TLabel')

    def queue_dequeue(self):
        dequeued = self.queue.dequeue()
        if dequeued is not None:
            self.update_queue_display()
            self.queue_status.config(text=f"Dequeued '{dequeued}'", style='Success.TLabel')
        else:
            self.queue_status.config(text="Queue is empty", style='Error.TLabel')

    def queue_front(self):
        front = self.queue.front()
        if front is not None:
            self.queue_status.config(text=f"Front element: '{front}'", style='Success.TLabel')
        else:
            self.queue_status.config(text="Queue is empty", style='Error.TLabel')

    def queue_clear(self):
        self.queue = Queue()
        self.update_queue_display()
        self.queue_status.config(text="Queue cleared", style='Success.TLabel')

    def update_queue_display(self):
        self.queue_display.config(state='normal')
        self.queue_display.delete(1.0, tk.END)
        display_text = f"Queue (FIFO): {self.queue.display()}\n"
        display_text += f"Size: {self.queue.size()}\n"
        display_text += f"Front: {self.queue.front() if not self.queue.is_empty() else 'None'}\n"
        display_text += "Operations: enqueue (add to rear), dequeue (remove from front)"
        self.queue_display.insert(1.0, display_text)
        self.queue_display.config(state='disabled')

    # BST Methods
    def bst_insert(self):
        try:
            value = int(self.bst_entry.get().strip())
            self.bst.insert(value)
            self.bst_entry.delete(0, tk.END)
            self.update_bst_display()
            self.bst_status.config(text=f"Inserted {value}", style='Success.TLabel')
        except ValueError:
            self.bst_status.config(text="Please enter a valid integer", style='Error.TLabel')

    def bst_search(self):
        try:
            value = int(self.bst_entry.get().strip())
            found = self.bst.search(value)
            self.bst_status.config(text=f"{value} {'found' if found else 'not found'}",
                                   style='Success.TLabel' if found else 'Error.TLabel')
        except ValueError:
            self.bst_status.config(text="Please enter a valid integer", style='Error.TLabel')

    def bst_random(self):
        self.bst = BinarySearchTree()
        values = random.sample(range(1, 100), 10)
        for value in values:
            self.bst.insert(value)
        self.update_bst_display()
        self.bst_status.config(text=f"Inserted random values: {values}", style='Success.TLabel')

    def bst_clear(self):
        self.bst = BinarySearchTree()
        self.update_bst_display()
        self.bst_status.config(text="BST cleared", style='Success.TLabel')

    def update_bst_display(self):
        self.bst_display.config(state='normal')
        self.bst_display.delete(1.0, tk.END)
        traversal = self.bst.inorder_traversal()
        display_text = f"Binary Search Tree\n"
        display_text += f"Inorder Traversal: {traversal}\n"
        display_text += f"Size: {len(traversal)}\n"
        display_text += "Properties: Left child < Parent < Right child\n"
        display_text += "Operations: insert, search (O(log n) average case)\n"
        display_text += f"Tree structure (inorder): {' -> '.join(map(str, traversal)) if traversal else 'Empty'}"
        self.bst_display.insert(1.0, display_text)
        self.bst_display.config(state='disabled')

    # Sorting Methods
    def generate_random_array(self):
        arr = [random.randint(1, 99) for _ in range(random.randint(5, 15))]
        self.sort_entry.delete(0, tk.END)
        self.sort_entry.insert(0, ' '.join(map(str, arr)))

    def run_sort(self, algorithm):
        try:
            arr_text = self.sort_entry.get().strip()
            if not arr_text:
                self.sort_status.config(text="Please enter an array", style='Error.TLabel')
                return

            arr = list(map(int, arr_text.split()))
            original_arr = arr.copy()

            self.sort_results.delete(1.0, tk.END)
            self.sort_results.insert(tk.END, f"=== {algorithm.upper()} SORT ===\n")
            self.sort_results.insert(tk.END, f"Original array: {original_arr}\n")
            self.sort_results.insert(tk.END, f"Array size: {len(arr)} elements\n\n")

            steps = []

            def step_callback(current_arr):
                steps.append(current_arr.copy())
                if len(steps) <= 20:  # Limit steps shown
                    self.sort_results.insert(tk.END, f"Step {len(steps)}: {current_arr}\n")
                self.root.update()
                time.sleep(0.1)  # Small delay for visualization

            start_time = time.time()

            if algorithm == "bubble":
                sorted_arr = SortingAlgorithms.bubble_sort(arr, step_callback)
            elif algorithm == "selection":
                sorted_arr = SortingAlgorithms.selection_sort(arr, step_callback)
            elif algorithm == "insertion":
                sorted_arr = SortingAlgorithms.insertion_sort(arr, step_callback)

            end_time = time.time()

            if len(steps) > 20:
                self.sort_results.insert(tk.END, f"... (showing first 20 of {len(steps)} steps)\n")

            self.sort_results.insert(tk.END, f"\nFinal sorted array: {sorted_arr}\n")
            self.sort_results.insert(tk.END, f"Total steps: {len(steps)}\n")
            self.sort_results.insert(tk.END, f"Time taken: {end_time - start_time:.4f} seconds\n")
            self.sort_results.insert(tk.END, f"Time complexity: O(n²) average case\n\n")

            self.sort_status.config(text=f"{algorithm.title()} sort completed in {end_time - start_time:.4f}s",
                                    style='Success.TLabel')

        except ValueError:
            self.sort_status.config(text="Please enter valid integers separated by spaces", style='Error.TLabel')
        except Exception as e:
            self.sort_status.config(text=f"Error: {str(e)}", style='Error.TLabel')

    # Search Methods
    def run_search(self, algorithm):
        try:
            arr_text = self.search_array_entry.get().strip()
            target_text = self.search_target_entry.get().strip()

            if not arr_text or not target_text:
                self.search_status.config(text="Please enter array and target", style='Error.TLabel')
                return

            arr = list(map(int, arr_text.split()))
            target = int(target_text)

            self.search_results.delete(1.0, tk.END)
            self.search_results.insert(tk.END, f"=== {algorithm.upper()} SEARCH ===\n")
            self.search_results.insert(tk.END, f"Array: {arr}\n")
            self.search_results.insert(tk.END, f"Target: {target}\n")
            self.search_results.insert(tk.END, f"Array size: {len(arr)} elements\n\n")

            start_time = time.time()

            if algorithm == "linear":
                self.search_results.insert(tk.END, "Linear Search Process:\n")
                result = -1
                for i, val in enumerate(arr):
                    self.search_results.insert(tk.END, f"Step {i + 1}: Checking index {i}, value = {val}")
                    if val == target:
                        result = i
                        self.search_results.insert(tk.END, f" ✓ FOUND!\n")
                        break
                    else:
                        self.search_results.insert(tk.END, f" ✗\n")
                    self.root.update()
                    time.sleep(0.2)

            elif algorithm == "binary":
                # Sort array first for binary search
                sorted_arr = sorted(arr)
                self.search_results.insert(tk.END, f"Sorted array: {sorted_arr}\n")
                self.search_results.insert(tk.END, "Binary Search Process:\n")

                left, right = 0, len(sorted_arr) - 1
                result = -1
                step = 1

                while left <= right:
                    mid = (left + right) // 2
                    mid_val = sorted_arr[mid]

                    self.search_results.insert(tk.END, f"Step {step}: left={left}, right={right}, mid={mid}\n")
                    self.search_results.insert(tk.END, f"         Checking middle value: {mid_val}\n")

                    if mid_val == target:
                        result = mid
                        self.search_results.insert(tk.END, f"         ✓ FOUND at index {mid}!\n")
                        break
                    elif mid_val < target:
                        left = mid + 1
                        self.search_results.insert(tk.END, f"         Target is larger, search right half\n")
                    else:
                        right = mid - 1
                        self.search_results.insert(tk.END, f"         Target is smaller, search left half\n")

                    step += 1
                    self.root.update()
                    time.sleep(0.3)

            end_time = time.time()

            self.search_results.insert(tk.END, f"\nResult: ")
            if result != -1:
                self.search_results.insert(tk.END, f"Target {target} found at index {result}\n")
                self.search_status.config(text=f"Found at index {result}", style='Success.TLabel')
            else:
                self.search_results.insert(tk.END, f"Target {target} not found\n")
                self.search_status.config(text="Target not found", style='Error.TLabel')

            self.search_results.insert(tk.END, f"Time taken: {end_time - start_time:.4f} seconds\n")

            if algorithm == "linear":
                self.search_results.insert(tk.END, f"Time complexity: O(n)\n")
            else:
                self.search_results.insert(tk.END, f"Time complexity: O(log n)\n")

        except ValueError:
            self.search_status.config(text="Please enter valid integers", style='Error.TLabel')
        except Exception as e:
            self.search_status.config(text=f"Error: {str(e)}", style='Error.TLabel')

    def run(self):
        """Start the GUI application"""
        self.root.mainloop()


def main():
    """Main function to run the GUI DSA project"""
    app = DSAGui()
    app.run()


if __name__ == "__main__":
    main()