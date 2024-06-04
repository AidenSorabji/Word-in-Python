# WHAT TO ADD NEXT
#
# - Intro Screen (New File, Load File, Keep the other buttons) Then turn in to actual editor

# Modules
import customtkinter
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox

# Tag Stuff
def new_tag_config(self, tagName, **kwargs):
    return self._textbox.tag_config(tagName, **kwargs)

customtkinter.CTkTextbox.tag_config = new_tag_config

# Classifying Stuff
global is_bolded, is_underlined, is_striked
current_font_size = 17
current_font = "SF Display"
textbox = None
path_to_folder = None
main_window = None
cut_button = None
word_count = "Words: 0"
is_bolded = False
is_underlined = False
is_striked = False
windows_opened = 1

# Icons
checkmark_icon = customtkinter.CTkImage(dark_image=Image.open("checkmark.png"),
                                        size=(15, 15))
copy_icon = customtkinter.CTkImage(dark_image=Image.open("copy.png"),
                                size=(19, 19))
paste_icon = customtkinter.CTkImage(dark_image=Image.open("paste.png"),
                                    size=(19, 19))

# Definitions
def open_file():
    checkmark_icon = customtkinter.CTkImage(dark_image=Image.open("checkmark.png"),
                                            size=(15, 15))
    copy_icon = customtkinter.CTkImage(dark_image=Image.open("copy.png"),
                                       size=(19, 19))
    paste_icon = customtkinter.CTkImage(dark_image=Image.open("paste.png"),
                                        size=(19, 19))


def show_error():
    # Show some error message
    CTkMessagebox(
        title="Error", message="No Selection Chosen!", icon="cancel", option_1="Ok")


def cut_variable():
    global textbox, main_window, cut_button

    def cut_variable():
        text_selected = textbox.get(
            customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
        main_window.clipboard_append(text_selected)
        textbox.delete(customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
        main_window.update()
        return cut_button

    if cut_button:  # Check if cut_button exists
        cut_button.destroy()  # Destroy the button if it exists

    cut_button = customtkinter.CTkButton(main_window,
                                         fg_color='#4e4f52',
                                         corner_radius=8,
                                         text="Cut?",
                                         border_width=1,
                                         border_color="#4e5255",
                                         hover_color="#414245",
                                         bg_color="#2b2b2b",
                                         width=60,
                                         height=25,
                                         command=cut_variable)
    cut_button.place(x=4,
                     y=572)


def start_textbox():
    global main_window, textbox
    textbox_frame = customtkinter.CTkFrame(main_window,
                                           width=900,
                                           height=472,
                                           border_width=2,
                                           corner_radius=0)
    textbox_frame.place(x=0,
                        y=98)

    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    textbox = customtkinter.CTkTextbox(textbox_frame,
                                       width=900,
                                       height=470,
                                       font=customtkinter.CTkFont(current_font, size=current_font_size))
    textbox.grid(sticky="n")


def new_file_prompt():
    global path_to_folder, textbox, path
    file_window = customtkinter.CTk()
    file_window.title("Create New File")
    file_window.geometry("300x153")
    file_window.attributes('-topmost', True)

    # --------------------------- Labels and Stuff --------------------------- #

    label1 = customtkinter.CTkLabel(file_window,
                                    text="Filename",
                                    bg_color="#242424",
                                    font=customtkinter.CTkFont(size=15,
                                                               weight="bold"))
    label1.pack(padx=10,
                pady=3,
                side="top",
                anchor="nw")

    label2 = customtkinter.CTkLabel(file_window,
                                    text="Custom Path",
                                    bg_color="#242424",
                                    font=customtkinter.CTkFont(size=15,
                                                               weight="bold"))
    label2.pack(padx=10,
                pady=7,
                side="top",
                anchor="nw")

    label3 = customtkinter.CTkLabel(file_window,
                                    text="All changes will be saved",
                                    bg_color="#242424",
                                    font=customtkinter.CTkFont("italic", size=10))
    label3.place(x=10,
                 y=121)

    # -------------------------- Buttons and Stuff -------------------------- #

    file_extension = ".txt"

    filename = customtkinter.CTkEntry(file_window,
                                      font=customtkinter.CTkFont(size=13),
                                      height=9,
                                      width=100,
                                      placeholder_text="filename")
    filename.place(x=130,
                   y=5)

    filextension_var = customtkinter.StringVar(value=".txt")

    def file_extension_variable(choice):
        file_extension = str(choice)
        print(file_extension)
        return file_extension

    filextension = customtkinter.CTkOptionMenu(file_window,
                                               values=[".txt", ".doc"],
                                               variable=filextension_var,
                                               width=60,
                                               height=23,
                                               bg_color="#242323",
                                               command=file_extension_variable)
    filextension.place(x=235,
                       y=5)

    custompath = 0

    choice_var = customtkinter.IntVar()

    path_to_folder = None

    def variable_no():
        global custompath, path_to_folder
        if path_to_folder is not None:
            path_to_folder.destroy()
        custompath = 0
        return custompath

    no_button = customtkinter.CTkRadioButton(file_window,
                                             bg_color="#242323",
                                             width=7,
                                             height=3,
                                             text="No",
                                             font=customtkinter.CTkFont(
                                                 size=12),
                                             variable=choice_var,
                                             value=1,
                                             command=variable_no)
    no_button.place(x=245,
                    y=45)

    def variable_yes():
        global custompath, path_to_folder
        path_to_folder = customtkinter.CTkEntry(file_window,
                                                font=customtkinter.CTkFont(
                                                    size=13),
                                                height=9,
                                                width=110,
                                                placeholder_text="/path/to/folder")
        path_to_folder.place(x=184,
                             y=75)
        custompath = 1
        return path_to_folder, custompath

    yes_button = customtkinter.CTkRadioButton(file_window,
                                              bg_color="#242323",
                                              width=7,
                                              height=3,
                                              text="Yes",
                                              font=customtkinter.CTkFont(
                                                  size=12),
                                              variable=choice_var,
                                              value=2,
                                              command=variable_yes)
    yes_button.place(x=185,
                     y=45)

    def create_file(file_extension, content, custompath):
        global path, textbox
        if custompath == 1:
            global path_to_folder
            filename_and_extension = (filename.get()) + file_extension
            path = str(path_to_folder.get()) + "/" + \
                str(filename_and_extension)
            with open(path, 'w') as file_:
                file_.write(content)
                file_.close()
                file_window.destroy()
        elif custompath == 0:
            current_dir = os.getcwd()
            filename_and_extension = (filename.get()) + file_extension
            path1 = str(current_dir) + "/" + "Written_Works"

            if not os.path.exists(path1):
                os.makedirs(path1)
            if os.path.exists(path1):
                pass

            path = path1 + "/" + str(filename_and_extension)
            with open(path, 'w') as file_:
                file_.write(content)
                file_.close()
                file_window.destroy()

    # Inside save_textbox_prompt function

    def create_file_callback():
        global path_to_folder, textbox, path
        content = textbox.get("1.0", "end-1c")  # Get content from textbox
        create_file(file_extension, content, custompath)

    create_file_button = customtkinter.CTkButton(file_window,
                                                 bg_color="#242323",
                                                 width=90,
                                                 height=20,
                                                 text="Create File",
                                                 command=create_file_callback)
    create_file_button.place(x=205,
                             y=125)

    file_window.mainloop()


def save_file_callback():
    global path, textbox
    if path:  # Check if path is not None
        with open(path, 'w') as file_:
            content = textbox.get("1.0", "end-1c")  # Get content from textbox
            file_.write(content)
            file_.close()


def constant_update():
    global textbox, word_counter_label, main_window
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    # ---------------- Update Textbox and Word Counter Label ------------------- #
    text = textbox.get("1.0", "end-1c")
    word_count_before = len(text.split())
    word_count = "Words:", str(word_count_before)
    word_counter_label.configure(text=word_count)
    word_counter_label.update()

    # ------------------------- Check for Highlight ---------------------------- #
    if textbox.tag_ranges("sel"):
        # Create Buttons that will have different functions
        cut_variable()
        pass
    if not textbox.tag_ranges('sel'):
        if cut_button:  # Check if cut_button exists
            cut_button.destroy()  # Destroy the button if it exists
        pass
    # -------------------------- Update Everything ---------------------------- #
    main_window.after(300, constant_update)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- Main -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #
def main():
    global main_window, textbox, size_entry, change_size
    main_window = customtkinter.CTk()
    main_window.geometry("900x600")
    main_window.title("Word")
    main_window.resizable(False, False)
    main_window._apply_appearance_mode("dark")

    def quitting():
        print("ye")
        main_window.destory()
        pygame.quit()
        quit()

    main_window.bind('<Command-BackSpace>',
                     lambda event: textbox.delete("1.0", customtkinter.INSERT))
    main_window.bind('<Option-BackSpace>',
                     lambda event: textbox.delete("insert-1c wordstart", "insert"))
    main_window.bind('<Command-b>', 
                     lambda event: bold_function())
    main_window.bind('<Command-u>',
                     lambda event: underline_function())
    main_window.bind('<Command-i>',
                     lambda event: strikethrough_function())
    main_window.bind('<Command-Q>',
                     lambda event: quitting())
    # ------------------- Top Part ------------------- #
    top_frame = customtkinter.CTkFrame(main_window,
                                       width=900,
                                       height=99,
                                       border_width=2,
                                       corner_radius=1)
    top_frame.pack(padx=0,
                   pady=0,
                   side="top")
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    new_file_button = customtkinter.CTkButton(main_window,
                                              height=26,
                                              width=150,
                                              text="New File",
                                              corner_radius=4,
                                              border_width=1,
                                              fg_color="#242424",
                                              border_color="#333232",
                                              bg_color="#2b2b2b",
                                              font=customtkinter.CTkFont(size=14,
                                                                         weight="bold"),
                                              command=new_file_prompt)
    new_file_button.place(x=5,
                          y=6)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    load_file_button = customtkinter.CTkButton(main_window,
                                               height=26,
                                               width=150,
                                               text="Load File",
                                               corner_radius=4,
                                               border_width=1,
                                               fg_color="#242424",
                                               border_color="#333232",
                                               bg_color="#2b2b2b",
                                               font=customtkinter.CTkFont(size=14,
                                                                          weight="bold"))
    load_file_button.place(x=5,
                           y=36)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    save_file_button = customtkinter.CTkButton(main_window,
                                               height=26,
                                               width=150,
                                               text="Save File",
                                               corner_radius=4,
                                               border_width=1,
                                               fg_color="#242424",
                                               border_color="#333232",
                                               bg_color="#2b2b2b",
                                               font=customtkinter.CTkFont(size=14,
                                                                          weight="bold"),
                                               command=save_file_callback)
    save_file_button.place(x=5,
                           y=66)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    def clear_textbox():
        textbox.delete("1.0", "end")  # Clear the textbox

    clear_textbox_text = """Clear
Texbox"""

    clear_textbox_button = customtkinter.CTkButton(main_window,
                                                   width=75,
                                                   height=42,
                                                   text=clear_textbox_text,
                                                   corner_radius=4,
                                                   border_width=1,
                                                   fg_color="#242424",
                                                   border_color="#333232",
                                                   bg_color="#2b2b2b",
                                                   hover_color="#135970",
                                                   font=customtkinter.CTkFont(size=12,
                                                                              weight="bold"),
                                                   command=clear_textbox)
    clear_textbox_button.place(x=159,
                               y=6)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    options_button = customtkinter.CTkButton(main_window,
                                             width=75,
                                             height=40,
                                             text="Options",
                                             corner_radius=4,
                                             border_width=1,
                                             fg_color="#242424",
                                             border_color="#333232",
                                             bg_color="#2b2b2b",
                                             hover_color="#135970",
                                             font=customtkinter.CTkFont(size=12,
                                                                        weight="bold"))
    options_button.place(x=159,
                         y=52)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    size_entry = customtkinter.CTkEntry(main_window,
                                        height=23,
                                        width=80,
                                        placeholder_text=current_font_size,
                                        font=customtkinter.CTkFont(size=13),
                                        bg_color="#2b2b2b",
                                        border_color='#555b5e',
                                        placeholder_text_color="white",
                                        corner_radius=4,
                                        border_width=1)
    size_entry.place(x=240,
                     y=7)

    def change_size():
        current_font_size = int(size_entry.get())
        if current_font_size > 450:
            current_font_size = 450
        textbox.configure(state="normal")

        textbox.configure(font=(current_font, current_font_size))

    size_entry_confirm = customtkinter.CTkButton(main_window,
                                                 fg_color='#353638',
                                                 width=23,
                                                 height=23,
                                                 corner_radius=3,
                                                 image=checkmark_icon,
                                                 border_width=1,
                                                 border_color='#4e5255',
                                                 background_corner_colors=[
                                                     '#555b5e', '#353638', '#353638', '#555b5e'],
                                                 bg_color='#2b2b2b',
                                                 text="",
                                                 hover_color="#137022",
                                                 command=change_size)
    size_entry_confirm.place(x=298,
                             y=7)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    def bold_function():
        global is_bolded
        if is_bolded == False:
            textbox.tag_add("bold", customtkinter.SEL_FIRST,
                            customtkinter.SEL_LAST)
            textbox.tag_config("bold", font=customtkinter.CTkFont(current_font,
                                                                  weight="bold",
                                                                  size=(current_font_size + 0)))
            is_bolded = True
        elif is_bolded == True:
            sel_first = textbox.index(customtkinter.SEL_FIRST)
            sel_last = textbox.index(customtkinter.SEL_LAST)
            textbox.tag_remove("bold", sel_first, sel_last)
            is_bolded = False

    bold_button = customtkinter.CTkButton(main_window,
                                          fg_color='#353638',
                                          width=25,
                                          height=25,
                                          corner_radius=4,
                                          text="B",
                                          border_width=1,
                                          font=customtkinter.CTkFont(
                                              size=12, weight="bold"),
                                          border_color="#4e5255",
                                          hover_color="#136d70",
                                          bg_color="#2b2b2b",
                                          command=bold_function)
    bold_button.place(x=240,
                      y=34)

    def underline_function():
        global is_underlined
        if is_underlined == False:
            textbox.tag_add("underline", customtkinter.SEL_FIRST,
                            customtkinter.SEL_LAST)
            textbox.tag_config("underline", underline=True)
            is_underlined = True
        elif is_underlined == True:
            textbox.tag_remove(
                "underline", customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
            textbox.tag_config("underline", font=customtkinter.CTkFont(
                underline=False, size=current_font_size))
            is_underlined = False

    underline_button = customtkinter.CTkButton(main_window,
                                               fg_color='#353638',
                                               width=25,
                                               height=25,
                                               corner_radius=4,
                                               text="U",
                                               border_width=1,
                                               font=customtkinter.CTkFont(
                                                   size=12, underline=True),
                                               border_color="#4e5255",
                                               hover_color="#136d70",
                                               bg_color="#2b2b2b",
                                               command=underline_function)
    underline_button.place(x=269,
                           y=34)

    def strikethrough_function():
        global is_striked
        if is_striked == False:
            textbox.tag_add("strikethrough",
                            customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
            textbox.tag_config("strikethrough", overstrike=True)
            is_striked = True
        elif is_striked == True:
            textbox.tag_delete(
                "strikethrough", customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
            textbox.tag_config("strikethrough", font=customtkinter.CTkFont(
                overstrike=False, size=current_font_size))
            is_striked = False

    strikethrough_button = customtkinter.CTkButton(main_window,
                                                   fg_color='#353638',
                                                   width=25,
                                                   height=25,
                                                   corner_radius=4,
                                                   text="S",
                                                   border_width=1,
                                                   font=customtkinter.CTkFont(
                                                       size=12, overstrike=True),
                                                   border_color="#4e5255",
                                                   hover_color="#136d70",
                                                   bg_color="#2b2b2b",
                                                   command=strikethrough_function)
    strikethrough_button.place(x=298,
                               y=34)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    def copy_callback():
        if textbox.tag_ranges("sel"):
            text_selected = textbox.get(
                customtkinter.SEL_FIRST, customtkinter.SEL_LAST)
            main_window.clipboard_append(text_selected)
            main_window.update()
        if not textbox.tag_ranges('sel'):
            show_error()
            pass

    copy_button = customtkinter.CTkButton(main_window,
                                          fg_color='#353638',
                                          corner_radius=4,
                                          text="",
                                          border_width=1,
                                          border_color="#4e5255",
                                          hover_color="#136d70",
                                          bg_color="#2b2b2b",
                                          width=39,
                                          height=28,
                                          image=copy_icon,
                                          command=copy_callback)
    copy_button.place(x=240,
                      y=63)

    def paste_callback():
        user_clipboard = main_window.clipboard_get()
        curser_location = textbox.index(customtkinter.CURRENT)
        textbox.insert(curser_location, user_clipboard)

    paste_button = customtkinter.CTkButton(main_window,
                                           fg_color='#353638',
                                           corner_radius=4,
                                           text="",
                                           border_width=1,
                                           border_color="#4e5255",
                                           hover_color="#136d70",
                                           bg_color="#2b2b2b",
                                           width=39,
                                           height=28,
                                           image=paste_icon,
                                           command=paste_callback)
    paste_button.place(x=284,
                       y=63)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
    def font_callback(choice):
        global textbox, main_window, current_font_size
        if choice == "SF Display":
            current_font = choice
        elif choice == "Arial":
            current_font = choice
        elif choice == "Helvetica":
            current_font = choice
        elif choice == "Comic Sans MS":
            current_font = choice
        elif choice == "Times New Roman":
            current_font = choice
        elif choice == "Impact":
            current_font = choice

        textbox.configure(state="normal")
        textbox.configure(font=(current_font, current_font_size))
        font_menu.configure(font=(current_font, 12))
        return current_font

    font_menu = customtkinter.CTkOptionMenu(main_window,
                                            fg_color='#353638',
                                            height=23,
                                            width=140,
                                            dropdown_fg_color="#353638",
                                            button_color="#353638",
                                            font=customtkinter.CTkFont(
                                                size=12),
                                            bg_color="#2b2b2b",
                                            corner_radius=4,
                                            values=["SF Display",
                                                    "Arial",
                                                    "Helvetica",
                                                    "Comic Sans MS",
                                                    "Times New Roman",
                                                    "Impact"],
                                            button_hover_color="#302f2f",
                                            command=font_callback)
    font_menu.place(x=332,
                    y=8)
    # ------------------ Middle Part ----------------- #
    start_textbox()
    # ------------------- End Part ------------------- #
    bottom_frame = customtkinter.CTkFrame(main_window,
                                          width=900,
                                          height=33,
                                          border_width=1,
                                          corner_radius=4)
    bottom_frame.place(x=0,
                       y=569)

    global word_counter_label
    word_counter_label = customtkinter.CTkLabel(main_window,
                                                text=word_count,
                                                font=customtkinter.CTkFont(
                                                    size=14),
                                                bg_color="#2b2b2b",
                                                text_color="#d4d4d4",
                                                height=26)
    word_counter_label.place(x=810,
                             y=570)
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #

    # --------------- Constant Update --------------- #
    constant_update()

    main_window.mainloop()


main()
