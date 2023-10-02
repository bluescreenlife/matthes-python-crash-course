from pathlib import Path

filenames = ["/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/cats.txt",
             "/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        read_file = path.read_text()
        print(read_file)
    except FileNotFoundError:
        # print(f"File missing: {filename}")
        pass