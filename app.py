# # Imports:
# import tkinter as tk
# import numpy as np
# from PIL import Image, ImageOps

# #
from models import predict




# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Guessing Number")
        
#         # Wymiary płótna
#         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
#         self.pixel_size = 10    # 10x10 pikseli na każdy blok
#         self.eraser_mode = False  # Tryb gumki

#         # Tworzenie płótna
#         self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
#         self.canvas.pack()
        
#         # Tablica do przechowywania obrazu 28x28
#         self.image_array = np.zeros((28, 28), dtype=np.uint8)
        
#         # Łączenie zdarzeń z funkcjami
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)
        
#         # Dodaj przycisk do przewidzenia numeru
#         self.save_button = tk.Button(root, text="Predict Number", command=self.save_image)
#         self.save_button.pack()

#         # Dodaj przycisk do przełączania trybu gumki
#         self.eraser_button = tk.Button(root, text="Toggle Eraser", command=self.toggle_eraser)
#         self.eraser_button.pack()

#         # Dodaj przycisk do czyszczenia płótna
#         self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
#         self.clear_button.pack()

#     def paint(self, event):
#         # Przelicz współrzędne na odpowiedni piksel
#         x, y = event.x // self.pixel_size, event.y // self.pixel_size

#         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)

#         if 0 <= x < 28 and 0 <= y < 28:
#             # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
#             self.image_array[y, x] = color
            
#             # Narysuj kwadrat na płótnie
#             display_color = 'black' if color == 255 else 'white'
#             self.canvas.create_rectangle(
#                 x * self.pixel_size, y * self.pixel_size,
#                 (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
#                 fill=display_color, outline=display_color
#             )
    
    
#     def toggle_eraser(self):
#         # Przełącz tryb gumki
#         self.eraser_mode = not self.eraser_mode
#         if self.eraser_mode:
#             self.eraser_button.config(text="Toggle Brush")
#         else:
#             self.eraser_button.config(text="Toggle Eraser")

#     def clear_canvas(self):
#         # Wyczyść tablicę i płótno
#         self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
#         self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
    
#     def save_image(self):
#         # Zapisz obraz w tablicy NumPy jako plik PNG
#         image = Image.fromarray(self.image_array)
#         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
#         image.save("drawing.png")
#         predict()


# # Uruchomienie aplikacji
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()



# import tkinter as tk
# import numpy as np
# from PIL import Image, ImageOps

# # from models import predict


# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Guessing Number")
        
#         # Wymiary płótna
#         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
#         self.pixel_size = 10    # 10x10 pikseli na każdy blok
#         self.eraser_mode = False  # Tryb gumki

#         # Tworzenie głównej ramki
#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack()

#         # Tworzenie płótna
#         self.canvas = tk.Canvas(self.main_frame, width=self.canvas_size, height=self.canvas_size, bg='white')
#         self.canvas.grid(row=0, column=0, rowspan=12)  # Ustaw płótno w lewej części interfejsu

#         # Tablica do przechowywania obrazu 28x28
#         self.image_array = np.zeros((28, 28), dtype=np.uint8)
        
#         # Łączenie zdarzeń z funkcjami
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)
        
#         # Dodaj przycisk do przewidzenia numeru
#         self.save_button = tk.Button(self.main_frame, text="Predict Number", command=self.save_image)
#         self.save_button.grid(row=0, column=1)

#         # Dodaj przycisk do przełączania trybu gumki
#         self.eraser_button = tk.Button(self.main_frame, text="Toggle Eraser", command=self.toggle_eraser)
#         self.eraser_button.grid(row=1, column=1)

#         # Dodaj przycisk do czyszczenia płótna
#         self.clear_button = tk.Button(self.main_frame, text="Clear Canvas", command=self.clear_canvas)
#         self.clear_button.grid(row=2, column=1)

#         # Dodaj przyciski od 0 do 9
#         self.number_buttons = []
#         for i in range(10):
#             button = tk.Button(self.main_frame, text=str(i), command=lambda i=i: self.number_button_pressed(i))
#             button.grid(row=i+3, column=1)
#             self.number_buttons.append(button)

#         # Dodaj przycisk "Dobrze"
#         self.done_button = tk.Button(self.main_frame, text="Dobrze", command=self.done_button_pressed)
#         self.done_button.grid(row=13, column=1)

#     def paint(self, event):
#         # Przelicz współrzędne na odpowiedni piksel
#         x, y = event.x // self.pixel_size, event.y // self.pixel_size

#         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)

#         if 0 <= x < 28 and 0 <= y < 28:
#             # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
#             self.image_array[y, x] = color
            
#             # Narysuj kwadrat na płótnie
#             display_color = 'black' if color == 255 else 'white'
#             self.canvas.create_rectangle(
#                 x * self.pixel_size, y * self.pixel_size,
#                 (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
#                 fill=display_color, outline=display_color
#             )
    
#     def toggle_eraser(self):
#         # Przełącz tryb gumki
#         self.eraser_mode = not self.eraser_mode
#         if self.eraser_mode:
#             self.eraser_button.config(text="Toggle Brush")
#         else:
#             self.eraser_button.config(text="Toggle Eraser")

#     def clear_canvas(self):
#         # Wyczyść tablicę i płótno
#         self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
#         self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
    
#     def save_image(self):
#         # Zapisz obraz w tablicy NumPy jako plik PNG
#         image = Image.fromarray(self.image_array)
#         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
#         image.save("drawing.png")
#         predict()  # Uncomment when predict function is available
    
#     def number_button_pressed(self, number):
#         # Pusta funkcja do obsługi wciśnięcia przycisków 0-9
#         print(f"Button {number} pressed")

#     def done_button_pressed(self):
#         # Pusta funkcja do obsługi wciśnięcia przycisku "Dobrze"
#         print("Button 'Dobrze' pressed")


# # Uruchomienie aplikacji
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()








# import tkinter as tk
# import numpy as np
# from PIL import Image, ImageOps

# # from models import predict


# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Guessing Number")
        
#         # Wymiary płótna
#         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
#         self.pixel_size = 10    # 10x10 pikseli na każdy blok
#         self.eraser_mode = False  # Tryb gumki

#         # Tworzenie głównej ramki
#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack()

#         # Tablica do przechowywania obrazu 28x28
#         self.image_array = np.zeros((28, 28), dtype=np.uint8)

#         # Tworzenie płótna
#         self.canvas = tk.Canvas(self.main_frame, width=self.canvas_size, height=self.canvas_size, bg='white')
#         self.canvas.grid(row=0, column=0, rowspan=1, columnspan=3)  # Płótno zajmuje pierwszą kolumnę i wiersz
        

#         # Łączenie zdarzeń z funkcjami
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)

#         # Tworzenie ramki na przyciski pod płótnem
#         self.button_frame = tk.Frame(self.main_frame)
#         self.button_frame.grid(row=1, column=0, columnspan=3)

#         # Dodaj przycisk do przewidzenia numeru
#         self.save_button = tk.Button(self.button_frame, text="Predict Number", command=self.save_image)
#         self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Dodaj przycisk do przełączania trybu gumki
#         self.eraser_button = tk.Button(self.button_frame, text="Toggle Eraser", command=self.toggle_eraser)
#         self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Dodaj przycisk do czyszczenia płótna
#         self.clear_button = tk.Button(self.button_frame, text="Clear Canvas", command=self.clear_canvas)
#         self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Dodaj przyciski od 0 do 9 po prawej stronie płótna
#         self.number_buttons = []
#         for i in range(10):
#             button = tk.Button(self.main_frame, text=str(i), command=lambda i=i: self.number_button_pressed(i))
#             button.grid(row=i, column=3, padx=5, pady=5)
#             self.number_buttons.append(button)

#         # Dodaj przycisk "Dobrze"
#         self.done_button = tk.Button(self.main_frame, text="Dobrze", command=self.done_button_pressed)
#         self.done_button.grid(row=10, column=3, padx=5, pady=5)

#     def paint(self, event):
#         # Przelicz współrzędne na odpowiedni piksel
#         x, y = event.x // self.pixel_size, event.y // self.pixel_size

#         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)

#         if 0 <= x < 28 and 0 <= y < 28:
#             # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
#             self.image_array[y, x] = color
            
#             # Narysuj kwadrat na płótnie
#             display_color = 'black' if color == 255 else 'white'
#             self.canvas.create_rectangle(
#                 x * self.pixel_size, y * self.pixel_size,
#                 (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
#                 fill=display_color, outline=display_color
#             )
    
#     def toggle_eraser(self):
#         # Przełącz tryb gumki
#         self.eraser_mode = not self.eraser_mode
#         if self.eraser_mode:
#             self.eraser_button.config(text="Toggle Brush")
#         else:
#             self.eraser_button.config(text="Toggle Eraser")

#     def clear_canvas(self):
#         # Wyczyść tablicę i płótno
#         self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
#         self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
    
#     def save_image(self):
#         # Zapisz obraz w tablicy NumPy jako plik PNG
#         image = Image.fromarray(self.image_array)
#         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
#         image.save("drawing.png")
#         predict()  # Uncomment when predict function is available
    
#     def number_button_pressed(self, number):
#         # Pusta funkcja do obsługi wciśnięcia przycisków 0-9
#         print(f"Button {number} pressed")

#     def done_button_pressed(self):
#         # Pusta funkcja do obsługi wciśnięcia przycisku "Dobrze"
#         print("Button 'Dobrze' pressed")


# # Uruchomienie aplikacji
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()










# import tkinter as tk
# import numpy as np
# from PIL import Image, ImageOps

# # from models import predict


# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Guessing Number")
        
#         # Wymiary płótna
#         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
#         self.pixel_size = 10    # 10x10 pikseli na każdy blok
#         self.eraser_mode = False  # Tryb gumki

#         # Tworzenie głównej ramki
#         self.main_frame = tk.Frame(root)
#         self.main_frame.pack()

#         # Tablica do przechowywania obrazu 28x28
#         self.image_array = np.zeros((28, 28), dtype=np.uint8)

#         # Tworzenie płótna
#         self.canvas = tk.Canvas(self.main_frame, width=self.canvas_size, height=self.canvas_size, bg='white')
#         self.canvas.grid(row=0, column=0, rowspan=1, columnspan=3)  # Płótno zajmuje pierwszą kolumnę i wiersz
        
        
#         # Łączenie zdarzeń z funkcjami
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)



#         # Tworzenie ramki na przyciski pod płótnem
#         self.button_frame = tk.Frame(self.main_frame)
#         self.button_frame.grid(row=1, column=0, columnspan=3)

#         # Dodaj przycisk do przewidzenia numeru
#         self.save_button = tk.Button(self.button_frame, text="Predict Number", command=self.save_image)
#         self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Dodaj przycisk do przełączania trybu gumki
#         self.eraser_button = tk.Button(self.button_frame, text="Toggle Eraser", command=self.toggle_eraser)
#         self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Dodaj przycisk do czyszczenia płótna
#         self.clear_button = tk.Button(self.button_frame, text="Clear Canvas", command=self.clear_canvas)
#         self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

#         # Tworzenie ramki na przyciski numeryczne i przycisk "Dobrze" z prawej strony płótna
#         self.number_frame = tk.Frame(self.main_frame)
#         self.number_frame.grid(row=0, column=3, padx=10, pady=10)

#         # Dodaj przyciski od 0 do 9 w dwóch rzędach
#         self.number_buttons = []
#         for i in range(10):
#             button = tk.Button(self.number_frame, text=str(i), command=lambda i=i: self.number_button_pressed(i), width=5, height=2)
#             row, col = divmod(i, 5)
#             button.grid(row=row, column=col, padx=5, pady=5)
#             self.number_buttons.append(button)

#         # Dodaj przycisk "Dobrze" poniżej przycisków numerycznych
#         self.done_button = tk.Button(self.number_frame, text="Dobrze", command=self.done_button_pressed, width=13, height=2)
#         self.done_button.grid(row=2, column=0, columnspan=5, pady=10)

#     def paint(self, event):
#         # Przelicz współrzędne na odpowiedni piksel
#         x, y = event.x // self.pixel_size, event.y // self.pixel_size

#         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)

#         if 0 <= x < 28 and 0 <= y < 28:
#             # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
#             self.image_array[y, x] = color
            
#             # Narysuj kwadrat na płótnie
#             display_color = 'black' if color == 255 else 'white'
#             self.canvas.create_rectangle(
#                 x * self.pixel_size, y * self.pixel_size,
#                 (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
#                 fill=display_color, outline=display_color
#             )
    
#     def toggle_eraser(self):
#         # Przełącz tryb gumki
#         self.eraser_mode = not self.eraser_mode
#         if self.eraser_mode:
#             self.eraser_button.config(text="Toggle Brush")
#         else:
#             self.eraser_button.config(text="Toggle Eraser")

#     def clear_canvas(self):
#         # Wyczyść tablicę i płótno
#         self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
#         self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
    
#     def save_image(self):
#         # Zapisz obraz w tablicy NumPy jako plik PNG
#         image = Image.fromarray(self.image_array)
#         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
#         image.save("drawing.png")
#         predict()  # Uncomment when predict function is available
    
#     def number_button_pressed(self, number):
#         # Pusta funkcja do obsługi wciśnięcia przycisków 0-9
#         print(f"Button {number} pressed")

#     def done_button_pressed(self):
#         # Pusta funkcja do obsługi wciśnięcia przycisku "Dobrze"
#         print("Button 'Dobrze' pressed")


# # Uruchomienie aplikacji
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()







import tkinter as tk
import numpy as np
from PIL import Image, ImageOps

# from models import predict


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Number")
        
        # Wymiary płótna
        self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
        self.pixel_size = 10    # 10x10 pikseli na każdy blok
        self.eraser_mode = False  # Tryb gumki

        # Tworzenie głównej ramki
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        # Tworzenie płótna
        self.canvas = tk.Canvas(self.main_frame, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.grid(row=0, column=0, rowspan=1, columnspan=3)  # Płótno zajmuje pierwszą kolumnę i wiersz
        

        # Tablica do przechowywania obrazu 28x28
        self.image_array = np.zeros((28, 28), dtype=np.uint8)

        # statystyka::::
        self.number_of_tries = 0
        self.correct = 0

        # Łączenie zdarzeń z funkcjami
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)


        # Tworzenie ramki na przyciski pod płótnem
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0, columnspan=3)

        # Dodaj przycisk do przewidzenia numeru
        self.save_button = tk.Button(self.button_frame, text="Predict Number", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Dodaj przycisk do przełączania trybu gumki
        self.eraser_button = tk.Button(self.button_frame, text="Toggle Eraser", command=self.toggle_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Dodaj przycisk do czyszczenia płótna
        self.clear_button = tk.Button(self.button_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Tworzenie ramki na przyciski numeryczne i przycisk "Dobrze" z prawej strony płótna
        self.number_frame = tk.Frame(self.main_frame)
        self.number_frame.grid(row=0, column=3, padx=10, pady=10)

        # Dodaj przyciski od 0 do 9 w dwóch rzędach
        self.number_buttons = []
        for i in range(10):
            button = tk.Button(self.number_frame, text=str(i), command=lambda i=i: self.number_button_pressed(i), width=5, height=2)
            row, col = divmod(i, 5)
            button.grid(row=row, column=col, padx=5, pady=5)
            self.number_buttons.append(button)

        # Dodaj przycisk "Dobrze" poniżej przycisków numerycznych
        self.done_button = tk.Button(self.number_frame, text="Dobrze", command=self.done_button_pressed, width=13, height=2)
        self.done_button.grid(row=2, column=0, columnspan=5, pady=10)

        # Dodanie etykiety do wyświetlania informacji
        self.info_label = tk.Label(self.main_frame, text="", fg="black", font=("Arial", 12))
        self.info_label.grid(row=2, column=0, columnspan=4, pady=10)

        # Dodanie etykiety do statystyki
        self.statistic_label = tk.Label(self.main_frame, text="", fg="black", font=("Arial", 12))
        self.statistic_label.grid(row=3, column=0, columnspan=4, pady=10)

    def paint(self, event):
        # Przelicz współrzędne na odpowiedni piksel
        x, y = event.x // self.pixel_size, event.y // self.pixel_size

        color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)

        if 0 <= x < 28 and 0 <= y < 28:
            # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
            self.image_array[y, x] = color
            
            # Narysuj kwadrat na płótnie
            display_color = 'black' if color == 255 else 'white'
            self.canvas.create_rectangle(
                x * self.pixel_size, y * self.pixel_size,
                (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
                fill=display_color, outline=display_color
            )
    
    def toggle_eraser(self):
        # Przełącz tryb gumki
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(text="Toggle Brush")
        else:
            self.eraser_button.config(text="Toggle Eraser")

    def clear_canvas(self):
        # Wyczyść tablicę i płótno
        self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
        self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
        self.info_label.config(text="")  # Wyczyść również etykietę informacji
    
    def save_image(self):
        # Zapisz obraz w tablicy NumPy jako plik PNG
        image = Image.fromarray(self.image_array)
        image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
        image.save("drawing.png")
        predicted_number, procent = predict()  # Uncomment when predict function is available
        self.info_label.config(text=f"Predicted number {predicted_number}, with probability {(procent*100):.2f}%")  # Aktualizacja etykiety informacji
    
    def number_button_pressed(self, number):
        # Pusta funkcja do obsługi wciśnięcia przycisków 0-9
        self.number_of_tries += 1
        self.statistic_label.config(text=f"Correct guesses: {((self.correct / self.number_of_tries) * 100):.2f} %")  # Aktualizacja etykiety informacji
        print(f"Button {number} pressed")

    def done_button_pressed(self):
        # Pusta funkcja do obsługi wciśnięcia przycisku "Dobrze"
        self.number_of_tries += 1
        self.correct += 1
        self.statistic_label.config(text=f"Correct guesses: {((self.correct / self.number_of_tries) * 100):.2f} %")  # Aktualizacja etykiety informacji
        print("Button 'Dobrze' pressed")


# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
