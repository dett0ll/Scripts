import webbrowser
with open("subdomain.txt") as f:
    for url in f:
        webbrowser.open_new_tab(url)
