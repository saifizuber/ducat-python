import tkinter as tk

import webbrowser

# Sample documents


def search_documents():
    query = query_entry.get().lower()
    matching_documents = []

    for i, document in enumerate(documents):
        if query in document.lower():
            matching_documents.append(documents[i])

    results_text.delete(1.0, tk.END)  # Clear previous results
    if matching_documents:
        results_text.insert(tk.END, "Matching Documents:\n")
        for doc in matching_documents:
            results_text.insert(tk.END, "- " + doc + "\n")
    else:
        results_text.insert(tk.END, "No matching documents found.")

def search_web():
    query = query_entry.get()
    url = f'https://www.google.com/search?q={query}'
    webbrowser.open(url)

root = tk.Tk()
root.title("Search Engine")

query_entry = tk.Entry(root)
query_entry.pack()



web_search_button = tk.Button(root, text="Web Search", command=search_web)
web_search_button.pack()


root.mainloop()