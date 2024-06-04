# Imports
import time

# File Types
file_docx = ["Docx", "docx", "1"]
file_txt = ["TxT", "Txt", "txt", "2"]
file_doc = ["Doc", "DOC", "doC", "doc", "3"]
file_rtf = ["RTF", "Rtf", "rtf"]
file_wpd = ["WPD", "Wpd", "wpd"]

# Way to exit
leave = ["exit", "exit()", "Exit", "Exit()"]

yo = "yo"

# Intro
print("""
Word for
 Python
  v1.0.2
""")

time.sleep(1.3)


# File type Program
file_type = input("""Please choose a file type:\n 1 docx\n 2 txt\n 3 doc\n 4 rtf\n 5 wpd\n

>>> """)

    # Opening files in their respective formats
if file_type in file_docx:
    f = open("Untitled.docx", "w")
elif file_type in file_txt:
    f = open("Untitled.txt", "w")
elif file_type in file_doc:
    f = open("Untitled.doc", "w")
elif file_type in file_rtf:
    f = open("Untitled.rtf", "w")
elif file_type in file_wpd:
    f = open("Untitled.wpd", "w")
else:
    print("""Using .txt ...
""")
    time.sleep(1)
    f = open("use_the_correct_file_format_next_time_lmao.txt", "w")


print('Remember, press enter and then type "exit()" to exit.')
time.sleep(1)

enter = input("""Press enter to continue...
""")


# typing Part
print("""Start Typing: """)
while True:
    write = input(""" \n """)
    if write in leave:
        # Saving File
        print("""
Saving File... """)
        f.close()
        
        time.sleep(1.2)

        # Exiting out of Python
        print("""
Closing Python...""")
        time.sleep(0.7)
        exit()
    else:
        f.write(write)
