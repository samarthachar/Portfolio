from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageTk


def download_image():
    # Gets File Path
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
        title="Save baseed Image"
    )
    # Saves the file path is the given route
    if file_path:
        watermark.save(file_path)  # Save the image to the selected path
        messagebox.showinfo("Success", "Image saved successfully!")

def add_base(base_fp, file_fp):
    # Checks if both file paths exists
    if not base_fp and not file_fp:
        messagebox.showinfo("ERROR", "Please submit both the base and the watermark image first")
        return

    global watermark
    # Open base
    base = Image.open(base_fp).convert('RGBA')
    #Makes base transparent

    alpha_enhancer = ImageEnhance.Brightness(base.split()[3])
    new_alpha = alpha_enhancer.enhance(0.4)
    r, g, b, _ = base.split()
    base = Image.merge('RGBA', (r, g, b, new_alpha))


    #Open watermark image
    watermark = Image.open(file_fp).convert('RGBA')

    #Resizes the watermark proportionally to the base
    scale = 0.8
    target_width = int(watermark.width * scale)
    wm_ratio = base.height / base.width
    target_height = int(target_width * wm_ratio)
    base = base.resize((target_width, target_height), Image.LANCZOS)

    # Find center of base and watermark
    base_center = (base.width//2, base.height//2)
    watermark_center = (watermark.width//2, watermark.height//2)

    #Finds perfect position to overlay
    overlay_position = (watermark_center[0] - base_center[0],watermark_center[1] - base_center[1])

    #OVerlays the two images
    watermark.paste(base, overlay_position, base)


    # Makes a copy, then shows it in the gui
    preview = watermark.copy()
    preview.thumbnail((400, 400), Image.LANCZOS)  # Shrinks while keeping aspect ratio
    watermarked_image = ImageTk.PhotoImage(preview)

    watermarked_image_label = Label(window, image=watermarked_image)
    watermarked_image_label.destroy()
    watermarked_image_label = Label(window, image=watermarked_image)
    watermarked_image_label.grid(column=1, row=7)
    watermarked_image_label.image = watermarked_image
    download_button = Button(window, text="Download Image Here", command=download_image)
    download_button.grid(column=1, row=8, pady=10)

def choose_base():
    # Opens dialogue to open dialogue box
    global base_path
    base_path = filedialog.askopenfilename(
        title="Select the base",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if base_path:
        global tk_base

        img = Image.open(base_path)
        img.thumbnail((100, 100), Image.LANCZOS)
        tk_base = ImageTk.PhotoImage(img)
        base_img = Label(window, image=tk_base)
        base_img.grid(column=0, row=3)


def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select the image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if file_path:
        global tk_file

        img = Image.open(file_path)
        img.thumbnail((100, 100), Image.LANCZOS)
        tk_file = ImageTk.PhotoImage(img)
        base_img = Label(window, image=tk_file)
        base_img.grid(column=2, row=3)

# -- Main Code --
base_path = None
file_path = None
tk_base = None
tk_file = None
watermark = None

window = Tk()
window.title("Watermarker™ ")
window.config(padx=50, pady=50)

title = Label(text="Watermarker™ ", font=("Helvetica", 30, "bold"))
title.grid(column=1, row=0 , rowspan=3)

submit_base = Button(text="Upload base image", width=10, command=choose_base)
submit_base.grid(column=0, row=2)

submit_file = Button(text="Upload watermark", width=10, command=choose_file)
submit_file.grid(column=2, row=2)

make_base_button = Button(text="Submit Images", width=55, command=lambda: add_base(file_path, base_path))
make_base_button.grid(column=0, row=5, columnspan=3)

window.mainloop()