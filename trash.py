# # import numpy as np
# # a = np.array([[1,2,3,4], 
# #               [5,6,7,8]])

# # other = 1 - a
# # print(other)
# # print(np.concatenate([a, other], axis=0))


# import numpy as np
# from PIL import Image

# # Załaduj obrazek i przekonwertuj na skalę szarości (opcjonalnie)
# image = Image.open('numer.png').convert('L')

# # Przekształć obrazek na tablicę NumPy
# image_array = np.array(image)

# # Spłaszcz tablicę 28x28 na 1x784
# flattened_array = image_array.flatten()

# # Jeśli potrzebujesz tablicy 1x784, dodaj dodatkowy wymiar
# flattened_array = flattened_array.reshape(1, -1)

# print(flattened_array.shape)  # Wynik powinien być (1, 784)





# import tkinter as tk
# import numpy as np
# from PIL import Image, ImageOps, ImageDraw

# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("28x28 Pixel Drawing App")
        
#         # Wymiary płótna
#         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
#         self.pixel_size = 10    # 10x10 pikseli na każdy blok
#         self.brush_size = 2     # Grubość pędzla/gumki w pikselach
#         self.eraser_mode = False  # Tryb gumki
        
#         # Tworzenie płótna
#         self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
#         self.canvas.pack()
        
#         # Tablica do przechowywania obrazu 28x28
#         self.image_array = np.zeros((28, 28), dtype=np.uint8)

#         # Łączenie zdarzeń z funkcjami
#         self.canvas.bind("<B1-Motion>", self.paint)
#         self.canvas.bind("<Button-1>", self.paint)
        
#         # Dodaj przycisk do zapisania obrazu
#         self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
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
        
#         # Dodaj gradient wokół pędzla (ciemniejsze w środku, jaśniejsze na zewnątrz)
#         for i in range(-self.brush_size, self.brush_size + 1):
#             for j in range(-self.brush_size, self.brush_size + 1):
#                 distance = np.sqrt(i**2 + j**2)
#                 if distance <= self.brush_size:
#                     intensity = min(255, int(255 * (distance / self.brush_size)))
#                     xi, yj = x + i, y + j
#                     if 0 <= xi < 28 and 0 <= yj < 28:
#                         # Ustawiamy wartość pikseli w tablicy
#                         if not self.eraser_mode:
#                             self.image_array[yj, xi] = max(self.image_array[yj, xi], intensity)
#                         else:
#                             self.image_array[yj, xi] = min(self.image_array[yj, xi], 255 - intensity)
                        
#                         # Narysuj kwadrat na płótnie
#                         display_color = f'#{int(self.image_array[yj, xi]):02x}{int(self.image_array[yj, xi]):02x}{int(self.image_array[yj, xi]):02x}'
#                         self.canvas.create_rectangle(
#                             xi * self.pixel_size, yj * self.pixel_size,
#                             (xi + 1) * self.pixel_size, (yj + 1) * self.pixel_size,
#                             fill=display_color, outline=display_color
#                         )

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
#         print("Image saved as drawing.png")

# # Uruchomienie aplikacji
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DrawingApp(root)
#     root.mainloop()









# # import tkinter as tk
# # import numpy as np
# # from PIL import Image, ImageOps


# # class DrawingApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("28x28 Pixel Drawing App")
        
# #         # Wymiary płótna
# #         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
# #         self.pixel_size = 10    # 10x10 pikseli na każdy blok
# #         self.brush_size = 1    # Grubość pędzla w pikselach
        
# #         # Tworzenie płótna
# #         self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
# #         self.canvas.pack()
        
# #         # Tablica do przechowywania obrazu 28x28
# #         self.image_array = np.zeros((28, 28), dtype=np.uint8)
        
# #         # Łączenie zdarzeń z funkcjami
# #         self.canvas.bind("<B1-Motion>", self.paint)
# #         self.canvas.bind("<Button-1>", self.paint)
        
# #         # Dodaj przycisk do zapisania obrazu
# #         self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
# #         self.save_button.pack()

# #     def paint(self, event):
# #         # Przelicz współrzędne na odpowiedni piksel
# #         x, y = event.x // self.pixel_size, event.y // self.pixel_size
        
# #         for i in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #             for j in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #                 xi = x + i
# #                 yj = y + j
# #                 if 0 <= xi < 28 and 0 <= yj < 28:
# #                     # Ustawiamy wartość pikseli w tablicy na 255 (biały piksel na czarnym tle)
# #                     self.image_array[yj, xi] = 255
                    
# #                     # Narysuj kwadrat na płótnie
# #                     self.canvas.create_rectangle(
# #                         xi * self.pixel_size, yj * self.pixel_size,
# #                         (xi + 1) * self.pixel_size, (yj + 1) * self.pixel_size,
# #                         fill='black', outline='black'
# #                     )
    
# #     def save_image(self):
# #         # Zapisz obraz w tablicy NumPy jako plik PNG
# #         image = Image.fromarray(self.image_array)
# #         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
# #         image.save("drawing.png")
# #         predict()
# #         print("Image saved as drawing.png")

# # # Uruchomienie aplikacji
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = DrawingApp(root)
# #     root.mainloop()

# # import tkinter as tk
# # import numpy as np
# # from PIL import Image, ImageOps

# # class DrawingApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("28x28 Pixel Drawing App")
        
# #         # Wymiary płótna
# #         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
# #         self.pixel_size = 10    # 10x10 pikseli na każdy blok
# #         self.brush_size = 1    # Grubość pędzla/gumki w pikselach
# #         self.eraser_mode = False  # Tryb gumki
        
# #         # Tworzenie płótna
# #         self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
# #         self.canvas.pack()
        
# #         # Tablica do przechowywania obrazu 28x28
# #         self.image_array = np.zeros((28, 28), dtype=np.uint8)
        
# #         # Łączenie zdarzeń z funkcjami
# #         self.canvas.bind("<B1-Motion>", self.paint)
# #         self.canvas.bind("<Button-1>", self.paint)
        
# #         # Dodaj przycisk do zapisania obrazu
# #         self.save_button = tk.Button(root, text="Predict Number", command=self.save_image)
# #         self.save_button.pack()

# #         # Dodaj przycisk do przełączania trybu gumki
# #         self.eraser_button = tk.Button(root, text="Toggle Eraser", command=self.toggle_eraser)
# #         self.eraser_button.pack()

# #     def paint(self, event):
# #         # Przelicz współrzędne na odpowiedni piksel
# #         x, y = event.x // self.pixel_size, event.y // self.pixel_size
        
# #         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)
        
# #         for i in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #             for j in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #                 xi = x + i
# #                 yj = y + j
# #                 if 0 <= xi < 28 and 0 <= yj < 28:
# #                     # Ustawiamy wartość pikseli w tablicy na odpowiedni kolor
# #                     self.image_array[yj, xi] = color
                    
# #                     # Narysuj kwadrat na płótnie
# #                     display_color = 'black' if color == 255 else 'white'
# #                     self.canvas.create_rectangle(
# #                         xi * self.pixel_size, yj * self.pixel_size,
# #                         (xi + 1) * self.pixel_size, (yj + 1) * self.pixel_size,
# #                         fill=display_color, outline=display_color
# #                     )

# #     def toggle_eraser(self):
# #         # Przełącz tryb gumki
# #         self.eraser_mode = not self.eraser_mode
# #         if self.eraser_mode:
# #             self.eraser_button.config(text="Toggle Brush")
# #         else:
# #             self.eraser_button.config(text="Toggle Eraser")

# #     def save_image(self):
# #         # Zapisz obraz w tablicy NumPy jako plik PNG
# #         image = Image.fromarray(self.image_array)
# #         image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
# #         image.save("drawing.png")
# #         predict()
# #         # print("Image saved as drawing.png")

# # # Uruchomienie aplikacji
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = DrawingApp(root)
# #     root.mainloop()










# # import tkinter as tk
# # import numpy as np
# # from PIL import Image, ImageOps

# # class DrawingApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("28x28 Pixel Drawing App")
        
# #         # Wymiary płótna
# #         self.canvas_size = 280  # 280x280 pikseli (10x powiększenie)
# #         self.pixel_size = 10    # 10x10 pikseli na każdy blok
# #         self.brush_size = 1     # Grubość pędzla/gumki w pikselach
# #         self.eraser_mode = False  # Tryb gumki
        
# #         # Tworzenie płótna
# #         self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
# #         self.canvas.pack()
        
# #         # Tablica do przechowywania obrazu 28x28
# #         self.image_array = np.zeros((28, 28), dtype=np.uint8)
        
# #         # Łączenie zdarzeń z funkcjami
# #         self.canvas.bind("<B1-Motion>", self.paint)
# #         self.canvas.bind("<Button-1>", self.paint)
        
#         # Dodaj przycisk do zapisania obrazu
#         # self.save_button = tk.Button(root, text="Predict Number", command=self.save_image)
#         # self.save_button.pack()

#         # # Dodaj przycisk do przełączania trybu gumki
#         # self.eraser_button = tk.Button(root, text="Toggle Eraser", command=self.toggle_eraser)
#         # self.eraser_button.pack()

#         # # Dodaj przycisk do czyszczenia płótna
#         # self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
#         # self.clear_button.pack()

# #     def paint(self, event):
# #         # Przelicz współrzędne na odpowiedni piksel
# #         x, y = event.x // self.pixel_size, event.y // self.pixel_size
        
# #         color = 255 if not self.eraser_mode else 0  # Kolor pędzla (czarny) lub gumki (biały)
        
# #         for i in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #             for j in range(-self.brush_size // 2, self.brush_size // 2 + 1):
# #                 xi = x + i
# #                 yj = y + j
# #                 if 0 <= xi < 28 and 0 <= yj < 28:
# #                     # Ustawiamy wartość pikseli w tablicy na odpowiedni kolor
# #                     self.image_array[yj, xi] = color
                    
# #                     # Narysuj kwadrat na płótnie
# #                     display_color = 'black' if color == 255 else 'white'
# #                     self.canvas.create_rectangle(
# #                         xi * self.pixel_size, yj * self.pixel_size,
# #                         (xi + 1) * self.pixel_size, (yj + 1) * self.pixel_size,
# #                         fill=display_color, outline=display_color
# #                     )

#     # def toggle_eraser(self):
#     #     # Przełącz tryb gumki
#     #     self.eraser_mode = not self.eraser_mode
#     #     if self.eraser_mode:
#     #         self.eraser_button.config(text="Toggle Brush")
#     #     else:
#     #         self.eraser_button.config(text="Toggle Eraser")

#     # def clear_canvas(self):
#     #     # Wyczyść tablicę i płótno
#     #     self.image_array.fill(0)  # Ustaw wszystkie piksele na 0 (czarne tło)
#     #     self.canvas.delete("all")  # Usuń wszystkie elementy z płótna
    
#     # def save_image(self):
#     #     # Zapisz obraz w tablicy NumPy jako plik PNG
#     #     image = Image.fromarray(self.image_array)
#     #     image = ImageOps.invert(image)  # Opcjonalnie: Invertuj, aby liczba była czarna na białym tle
#     #     image.save("drawing.png")
#     #     predict()

# # # Uruchomienie aplikacji
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = DrawingApp(root)
# #     root.mainloop()



