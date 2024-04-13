import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot

import anthropic

####### MANDATORY WRITE YOUR ANTHROPIC.COM API KEY HERE -- https://console.anthropic.com/settings/keys
client = anthropic.Anthropic(api_key="sk-ant-...")


class NovelBuilder(QWidget):
    # Define a signal that carries text as its argument
    newTextReceived = pyqtSignal(str, QTextEdit)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        # General Data column
        general_data_layout = QVBoxLayout()
        general_data_layout.addWidget(QLabel("General Data"))
        self.races_factions = QTextEdit()
        self.geography = QTextEdit()
        self.history = QTextEdit()
        self.geopolitics = QTextEdit()
        self.ckRaces = QCheckBox()
        self.ckRaces.setChecked(True)
        self.ckGeog = QCheckBox()
        self.ckGeog.setChecked(True)
        self.ckHist = QCheckBox()
        self.ckHist.setChecked(True)
        self.ckGeop = QCheckBox()
        self.ckGeop.setChecked(True)
        general_data_layout.addWidget(self.ckRaces)
        general_data_layout.addWidget(QLabel("Available races or factions:"))
        general_data_layout.addWidget(self.races_factions)
        general_data_layout.addWidget(self.ckGeog)
        general_data_layout.addWidget(QLabel("Geography:"))
        general_data_layout.addWidget(self.geography)
        general_data_layout.addWidget(self.ckHist)
        general_data_layout.addWidget(QLabel("History:"))
        general_data_layout.addWidget(self.history)
        general_data_layout.addWidget(self.ckGeop)
        general_data_layout.addWidget(QLabel("Geopolitics:"))
        general_data_layout.addWidget(self.geopolitics)
        layout.addLayout(general_data_layout)

        # Characters column
        characters_layout = QVBoxLayout()
        characters_layout.addWidget(QLabel("Characters"))
        self.main_char = QTextEdit()
        self.killer = QTextEdit()
        self.wisdom_counselor = QTextEdit()
        self.absolute_enemy = QTextEdit()
        self.nuanced_enemy = QTextEdit()
        self.goal = QTextEdit()
        self.minor_npcs = QTextEdit()

        self.ckMainChar = QCheckBox()
        self.ckMainChar.setChecked(True)
        self.ckKiller = QCheckBox()
        self.ckKiller.setChecked(True)
        self.ckWisdom = QCheckBox()
        self.ckWisdom.setChecked(True)
        self.ckAbsEnemy = QCheckBox()
        self.ckAbsEnemy.setChecked(True)
        self.ckNuancedEnemy = QCheckBox()
        self.ckNuancedEnemy.setChecked(True)
        self.ckGoal = QCheckBox()
        self.ckGoal.setChecked(True)
        self.ckMinorNPCs = QCheckBox()
        self.ckMinorNPCs.setChecked(True)

        characters_layout.addWidget(self.ckMainChar)
        characters_layout.addWidget(QLabel("Main character:"))
        characters_layout.addWidget(self.main_char)
        characters_layout.addWidget(self.ckKiller)
        characters_layout.addWidget(QLabel("The killer (ally or enemy sociopath):"))
        characters_layout.addWidget(self.killer)
        characters_layout.addWidget(self.ckWisdom)
        characters_layout.addWidget(QLabel("Absolute wisdom counselor:"))
        characters_layout.addWidget(self.wisdom_counselor)
        characters_layout.addWidget(self.ckAbsEnemy)
        characters_layout.addWidget(QLabel("Absolute enemy cruel:"))
        characters_layout.addWidget(self.absolute_enemy)
        characters_layout.addWidget(self.ckNuancedEnemy)
        characters_layout.addWidget(QLabel("Nuanced enemy:"))
        characters_layout.addWidget(self.nuanced_enemy)
        characters_layout.addWidget(self.ckGoal)
        characters_layout.addWidget(QLabel("The goal to physically pursue or flee:"))
        characters_layout.addWidget(self.goal)
        characters_layout.addWidget(self.ckMinorNPCs)
        characters_layout.addWidget(QLabel("The 3x3 matrix minor NPCs (intention vs intensity):"))
        characters_layout.addWidget(self.minor_npcs)
        layout.addLayout(characters_layout)

        # Scenes column
        scenes_layout = QVBoxLayout()
        scenes_layout.addWidget(QLabel("Scenes"))
        self.tropes_selector = QTextEdit()
        self.story = QTextEdit()
        self.ckTropes = QCheckBox()
        self.ckTropes.setChecked(True)
        self.ckStory = QCheckBox()
        self.ckStory.setChecked(True)

        scenes_layout.addWidget(self.ckTropes)
        scenes_layout.addWidget(QLabel("Tropes selector:"))
        scenes_layout.addWidget(self.tropes_selector)
        scenes_layout.addWidget(self.ckStory)
        scenes_layout.addWidget(QLabel("The Story with twists and spoilers, in one page:"))
        scenes_layout.addWidget(self.story)
        layout.addLayout(scenes_layout)

        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_data)
        layout.addWidget(submit_button)

        # Connect the signal to the slot
        self.newTextReceived.connect(self.updateText)

        # Load Data
        self.loadText()

        self.setLayout(layout)
        self.setWindowTitle("Novel Builder")
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowState(Qt.WindowMaximized)
        self.show()

    def loadText(self):
        try:
            with open("saved_factions.txt", "r") as file:
                self.races_factions.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_geography.txt", "r") as file:
                self.geography.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_history.txt", "r") as file:
                self.history.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_geopolitics.txt", "r") as file:
                self.geopolitics.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_mainchar.txt", "r") as file:
                self.main_char.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_thekiller.txt", "r") as file:
                self.killer.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_wisdom_counselor.txt", "r") as file:
                self.wisdom_counselor.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_absolute_enemy.txt", "r") as file:
                self.absolute_enemy.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_nuanced_enemy.txt", "r") as file:
                self.nuanced_enemy.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_goal.txt", "r") as file:
                self.goal.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_minor_npcs.txt", "r") as file:
                self.minor_npcs.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_tropes.txt", "r") as file:
                self.tropes_selector.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)
        try:
            with open("saved_story.txt", "r") as file:
                self.story.setPlainText(file.read())
        except Exception as e:
            print("Failed to load the text:", e)

    @pyqtSlot(str, QTextEdit)
    def updateText(self, text, qtx):
        # This method will run in the main thread
        qtx.setPlainText(qtx.toPlainText() + text)

    def submit_data(self):
        # Retrieve the data from the input fields
        races_factions = self.races_factions.toPlainText()
        geography = self.geography.toPlainText()
        history = self.history.toPlainText()
        geopolitics = self.geopolitics.toPlainText()
        main_char = self.main_char.toPlainText()
        killer = self.killer.toPlainText()
        wisdom_counselor = self.wisdom_counselor.toPlainText()
        absolute_enemy = self.absolute_enemy.toPlainText()
        nuanced_enemy = self.nuanced_enemy.toPlainText()
        goal = self.goal.toPlainText()
        minor_npcs = self.minor_npcs.toPlainText()
        tropes_selector = self.tropes_selector.toPlainText()
        story = self.story.toPlainText()

        # Process the data or perform any desired actions
        print("Submitted data:")
        print("Races/Factions:", races_factions)
        print("Geography:", geography)
        print("History:", history)
        print("Geopolitics:", geopolitics)
        print("Main Character:", main_char)
        print("Killer:", killer)
        print("Wisdom Counselor:", wisdom_counselor)
        print("Absolute Enemy:", absolute_enemy)
        print("Nuanced Enemy:", nuanced_enemy)
        print("Goal:", goal)
        print("Minor NPCs:", minor_npcs)
        print("Tropes Selector:", tropes_selector)
        print("Story:", story)


        if self.ckRaces.isChecked() is True:
            print("\n\nGENERATING FACTIONS")
            self.races_factions.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small number of factions or races, either sci-fi or fantasy, but not both. Build a beautiful universe with diverse races or factions."}],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.newTextReceived.emit(text, self.races_factions)
                #self.races_factions.setPlainText(self.races_factions.toPlainText() + text)

        if self.ckGeog.isChecked() is True:
            print("\n\nGENERATING GEOGRAPHY")
            self.geography.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph of geography which fits these races/factions nicely: " + self.races_factions.toPlainText()}],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.geography.setPlainText(self.geography.toPlainText() + text)

        if self.ckHist.isChecked() is True:
            print("\n\nGENERATING HISTORY")
            self.history.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph of history which fits these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText()}],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.history.setPlainText(self.history.toPlainText() + text)

        if self.ckGeop.isChecked() is True:
            print("\n\nGENERATING GEOPOLITICS")
            self.geopolitics.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph of geopolitics which fits these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.geopolitics.setPlainText(self.geopolitics.toPlainText() + text)

        if self.ckMainChar.isChecked() is True:
            print("\n\nGENERATING Main Character")
            self.main_char.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about the main character (give an elegant and original name and surname (not Zephyr)) which fits one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.main_char.setPlainText(self.main_char.toPlainText() + text)

        if self.ckKiller.isChecked() is True:
            print("\n\nGENERATING KILLER")
            self.killer.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about 'the killer' archetype character who is a sociopath assassin (either ally or enemy) which complements the main character nicely, and with an original name (not Zephyr), main character description being: '" + self.main_char.toPlainText() + "'. /// He should also fit one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.killer.setPlainText(self.killer.toPlainText() + text)

        if self.ckWisdom.isChecked() is True:
            print("\n\nGENERATING ABSOLUTE WISDOM COUNSELOR")
            self.wisdom_counselor.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about 'the absolute wisdom counselor' archetype character who is mysterious and guiding the main character on its path; it has an original name (not Zephyr); and it complements the main character nicely, main character description being: '" + self.main_char.toPlainText() + "'. /// He or She should also fit one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.wisdom_counselor.setPlainText(self.wisdom_counselor.toPlainText() + text)

        if self.ckAbsEnemy.isChecked() is True:
            print("\n\nGENERATING ABSOLUTE ENEMY")
            self.absolute_enemy.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about 'the absolute enemy' archetype character who is pure evil enemy; which complements the main character nicely, with an original name (not Zephyr) and main character description being: '" + self.main_char.toPlainText() + "'. /// He or She should also fit one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.absolute_enemy.setPlainText(self.absolute_enemy.toPlainText() + text)

        if self.ckNuancedEnemy.isChecked() is True:
            print("\n\nGENERATING NUANCED ENEMY")
            self.nuanced_enemy.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about 'the nuanced enemy' archetype charismatic character who is unlawful but with a code of honor, or torn apart between his actions and his desire to change to do good later in the story. He has a good name (not Zephyr). He or She complements the main character nicely, main character description being: '" + self.main_char.toPlainText() + "'. /// He or She should also fit one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.nuanced_enemy.setPlainText(self.nuanced_enemy.toPlainText() + text)

        if self.ckGoal.isChecked() is True:
            print("\n\nGENERATING GOAL")
            self.goal.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate a small paragraph about 'the goal to pursue or flee physically' Very Important story element which the main characters are drawn to or escaping it. Make it interesting and with a lot of weight. It complements the main character nicely, main character description being: '" + self.main_char.toPlainText() + "'. /// It should also fit the main enemy being:'" + self.absolute_enemy.toPlainText() + "'. ///It should also fit one of these races/factions nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.goal.setPlainText(self.goal.toPlainText() + text)

        if self.ckMinorNPCs.isChecked() is True:
            print("\n\nGENERATING 3x3")
            self.minor_npcs.setPlainText("")

            with client.messages.stream(
                max_tokens=1024,
                messages=[{"role": "user", "content": "Generate 3 lines about 9 characters being the combinations of intention (helpful, neutral, harmful) with the intensity of it (very conflictual, neutral, slightly). That is nine combinations. Give them a name and write them in one or 2 lines for each character. Make it interesting and with a lot of weight. These characters complements the main character or enemy nicely along the story, main character description being: '" + self.main_char.toPlainText() + "'. /// It should also fit the main enemy being:'" + self.absolute_enemy.toPlainText() + "'. ///It should also fit one of these races/factions diversely and nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.minor_npcs.setPlainText(self.minor_npcs.toPlainText() + text)

        if self.ckTropes.isChecked() is True:
            print("\n\nGENERATING TROPES")
            self.tropes_selector.setPlainText("")

            with client.messages.stream(
                max_tokens=2048,
                messages=[{"role": "user", "content": "Generate 20 diverse tropes for the story and sidestories. Give them a name and write them in one or 2 lines for each trope. Make it interesting and with a lot of depth. It should be harmonious withh the main character description being: '" + self.main_char.toPlainText() + "'. /// It should make use of the 9 minor characters: " + self.minor_npcs.toPlainText() +  "./// It should also fit the main enemy being:'" + self.absolute_enemy.toPlainText() + "'. ///It should also fit one of these races/factions diversely and nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.tropes_selector.setPlainText(self.tropes_selector.toPlainText() + text)

        if self.ckStory.isChecked() is True:
            print("\n\nGENERATING STORY")
            self.story.setPlainText("")

            with client.messages.stream(
                max_tokens=4096,
                messages=[{"role": "user", "content": "Generate a full story using our characters and tropes. Make it lengthily and complex, using all the information. It should be harmonious withh the main character description being: '" + self.main_char.toPlainText() + "'. /// It should involve the 'killer' sociopath: "  + self.killer.toPlainText()  + ". /// It should make use of the 9 minor characters: " + self.minor_npcs.toPlainText() +  "./// It should also fit the main enemy being:'" + self.absolute_enemy.toPlainText() + "'. /// It should use the wise councelor: " + self.wisdom_counselor.toPlainText() + ". /// It should also use the nuanced enemy: " + self.nuanced_enemy.toPlainText() + "It should also fit one of these races/factions diversely and nicely: " + self.races_factions.toPlainText() + ". /// It should also fit this geography: " + self.geography.toPlainText() + ". /// It should also fit this History: " + self.history.toPlainText() + ". /// It should also fit this geopolitics: " + self.geopolitics.toPlainText() + ". /// We make heavy usage of the 'goal object' or person, which we are pursuing or fleeing from intensely; this is its description: " + self.goal.toPlainText() + ". /// Finally, use cleverly a sample or all of the tropes we have provided here: " + self.tropes_selector.toPlainText()}
                          ],
                model="claude-3-opus-20240229",
            ) as stream:
              for text in stream.text_stream:
                print(text, end="", flush=True)
                self.story.setPlainText(self.story.toPlainText() + text)

        try:
            with open("saved_factions.txt", "w") as file:
                file.write(self.races_factions.toPlainText())
            with open("saved_geography.txt", "w") as file:
                file.write(self.geography.toPlainText())
            with open("saved_history.txt", "w") as file:
                file.write(self.history.toPlainText())
            with open("saved_geopolitics.txt", "w") as file:
                file.write(self.geopolitics.toPlainText())
            with open("saved_mainchar.txt", "w") as file:
                file.write(self.main_char.toPlainText())
            with open("saved_thekiller.txt", "w") as file:
                file.write(self.killer.toPlainText())
            with open("saved_wisdom_counselor.txt", "w") as file:
                file.write(self.wisdom_counselor.toPlainText())
            with open("saved_absolute_enemy.txt", "w") as file:
                file.write(self.absolute_enemy.toPlainText())
            with open("saved_nuanced_enemy.txt", "w") as file:
                file.write(self.nuanced_enemy.toPlainText())
            with open("saved_goal.txt", "w") as file:
                file.write(self.goal.toPlainText())
            with open("saved_minor_npcs.txt", "w") as file:
                file.write(self.minor_npcs.toPlainText())
            with open("saved_tropes.txt", "w") as file:
                file.write(self.tropes_selector.toPlainText())
            with open("saved_story.txt", "w") as file:
                file.write(self.story.toPlainText())
        except Exception as e:
            print("Failed to save the text:", e)
                

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    novel_builder = NovelBuilder()
    sys.exit(app.exec_())