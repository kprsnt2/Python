notes = {}

def create_note(title, content):
    notes[title] = content

def list_notes():
    print("Notes:")
    for title in notes.keys():
        print(f"- {title}")

def retrieve_note(title):
    if title in notes:
        print(notes[title])
    else:
        print(f"Error: No note with title '{title}' found.")

while True:
    command = input("Enter command (create, list, retrieve, or exit): ")
    if command == "create":
        title = input("Enter title: ")
        content = input("Enter content: ")
        create_note(title, content)
    elif command == "list":
        list_notes()
    elif command == "retrieve":
        title = input("Enter title: ")
        retrieve_note(title)
    elif command == "exit":
        break
    else:
        print("Error: Unknown command.")

import tkinter as tk

notes = {}

def create_note():
    title = title_entry.get()
    content = content_entry.get("1.0", "end")
    notes[title] = content
    title_entry.delete(0, tk.END)
    content_entry.delete("1.0", tk.END)

def list_notes():
    notes_list.delete(0, tk.END)
    for title in notes.keys():
        notes_list.insert(tk.END, title)

def retrieve_note():
    title = notes_list.get(notes_list.curselection())
    content = notes[title]
    content_entry.insert("1.0", content)

root = tk.Tk()
root.title("Notes App")

title_label = tk.Label(root, text="Title")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

content_label = tk.Label(root, text="Content")
content_label.grid(row=1, column=0)
content_entry = tk.Text(root, height=10, width=30)
content_entry.grid(row=1, column=1)

create_button = tk.Button(root, text="Create", command=create_note)
create_button.grid(row=2, column=0)

notes_list = tk.Listbox(root)
notes_list.grid(row=0, column=2, rowspan=3)
notes_list.bind("<<ListboxSelect>>", retrieve_note)

root.mainloop()


