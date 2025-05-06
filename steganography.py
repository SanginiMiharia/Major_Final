import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import numpy as np
import cv2

class DCTSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DCT Steganography")
        self.root.geometry("400x200")
        self.label = tk.Label(
            root, text="DCT Steganography", font=("Arial", 16)
        )
        self.label.pack(pady=10)
        self.encode_button = tk.Button(
            root, text="Encode Message", command=self.encode_message
        )
        self.encode_button.pack(pady=5)
        self.decode_button = tk.Button(
            root, text="Decode Message", command=self.decode_message
        )
        self.decode_button.pack(pady=5)
        self.exit_button = tk.Button(
            root, text="Exit", command=root.quit
        )
        self.exit_button.pack(pady=5)
