from pathlib import Path

classics = ["/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/pride_and_prejudice.txt",
            "/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/room_with_a_view.txt",
            "/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/dracula.txt",
            "/Users/andrew/Developer/vscode/02_matthes_exercises/matthes_main/chapter_10/moby_dick.txt"]

for filename in classics:

    book = Path(filename)
    contents = book.read_text().lower()
    words = contents.split()

    target_word = words.count("ahab")
    # target_word2 = words.count("")
    # target_word3 = words.count("Dick-")
    # total_target = target_word + target_word2 +target_word3

    print(f"{filename} contains {target_word} dicks.")