French Flash Cards

An interactive French-English flashcard application built with Python and Tkinter to help practice and memorize French vocabulary.

The application displays a French word, automatically flips the card to reveal its English meaning after a few seconds, and allows the user to mark words they already know.

✨ Features
🃏 Interactive flashcard interface
🇫🇷 Displays French vocabulary
🇬🇧 Automatically reveals the English translation
⏱️ Automatically flips cards after 3 seconds
🔀 Randomly selects vocabulary cards
✅ Remove words that have been learned
💾 Saves remaining words to a CSV file
📂 Automatically creates the learning list from the original vocabulary dataset
🖥️ Graphical user interface built with Tkinter
🛠️ Technologies Used
Python
Tkinter – GUI development
Pandas – CSV data handling
Random – Random vocabulary selection
OS – File and directory handling
📂 Project Structure
French-Flash-Cards/
│
├── main.py
│
├── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
└── README.md
🎮 How It Works
1. Load Vocabulary

The application reads the original French vocabulary from:

data/french_words.csv

If a words_to_learn.csv file already exists, the application loads the remaining vocabulary from that file instead.

2. Display a French Word

A random vocabulary card is selected and displayed on the front of the flashcard.

Example:

French

chien
3. Flip the Card

After approximately 3 seconds, the card automatically flips and displays the English translation.

English

dog
4. Mark a Word as Known

If the user already knows the word, clicking the ✅ button removes it from the learning list.

The remaining words are saved to:

data/words_to_learn.csv

This allows the application to remember the user's progress between sessions.

5. Continue Learning

A new random card is displayed automatically, allowing the user to continue practicing.

📊 CSV Data Format

The vocabulary data uses a simple CSV structure:

French,English
chien,dog
chat,cat
maison,house
livre,book

The application converts the CSV data into Python dictionaries for easier access.

💾 Progress Tracking

One of the useful features of this project is that learned words are removed from the active learning list.

For example:

Original vocabulary
        ↓
French words
        ↓
User knows a word
        ↓
Remove from learning list
        ↓
Save remaining words
        ↓
words_to_learn.csv

When the application is opened again, it continues using the remaining words.

🚀 How to Run
1. Clone the repository
git clone <your-repository-url>
2. Install Pandas
pip install pandas

Tkinter is included with most standard Python installations.

3. Run the application
python main.py

Make sure the data and images folders are located in the same project directory as main.py.

🎯 Learning Outcomes

This project helped me practice:

Building GUI applications with Tkinter
Working with buttons, canvas elements and images
Using after() for timed events
Reading and writing CSV files
Using Pandas DataFrames
Converting DataFrames into dictionaries
Working with lists and dictionaries
Random selection using Python's random module
File and directory management using os
Persisting application data between sessions
Debugging and structuring a multi-function Python application
🔮 Future Improvements

Possible improvements for future versions:

Add more languages besides French
Add pronunciation/audio for vocabulary
Add difficulty levels
Track learning statistics
Add a score or progress indicator
Implement a proper spaced-repetition algorithm
Allow users to add their own vocabulary
Add a search and vocabulary management feature
📸 Project Preview

The application provides a simple flashcard-style interface where users can view French vocabulary, reveal translations, and mark words they have learned.

👩‍💻 Author

Nandhitha

Built as part of my Python learning journey and hands-on automation/application projects.