import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
from matplotlib import pyplot as plt
import numpy as np

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('idea.ui', self)

        self.apple = self.findChild(QPushButton, 'apple')
        if self.apple:
            self.apple.setIcon(QIcon(QPixmap("apple.png").scaled(120, 120)))

        self.google = self.findChild(QPushButton, 'google')
        if self.google:
            self.google.setIcon(QIcon(QPixmap("google.png").scaled(120, 120)))

        self.linedit = self.findChild(QLineEdit, 'lineEdit')

        self.sign_button = self.findChild(QPushButton, 'sign')
        self.sign_button.clicked.connect(self.open_main_window)

        self.main_window = None
        self.user_name = None  # Initialize user_name attribute

        self.show()

    def open_main_window(self):
        self.user_name = self.linedit.text().strip()
        
        if not self.main_window:
            self.main_window = MainWindow(self.user_name)  # Pass username to MainWindow
            self.close()

        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.user_name = user_name  # Store username in MainWindow instance

        self.temp_image = self.findChild(QLabel, 'temp')
        self.fallit = self.findChild(QLabel, 'fall')

        self.label_hi = self.findChild(QLabel, 'label_13')
        self.label_hi.setText(f'Hi, {user_name}!')

        self.stats_button = self.findChild(QPushButton, "stat")
        self.stats_button.clicked.connect(self.open_stats)

        self.profile_button = self.findChild(QPushButton, "profile")
        self.profile_button.clicked.connect(self.show_profile)

        self.aout = self.findChild(QPushButton, "aboutus")
        self.aout.clicked.connect(self.show_about)

        self.show()

    def open_stats(self):
        # Generate random data for demonstration
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        drink_amounts = np.random.randint(200, 800, 7)

        # Creating the figure and axis objects
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plotting the bar chart
        ax.bar(days, drink_amounts, color='skyblue')

        # Setting the background color for the entire figure
        fig.patch.set_facecolor((20/255, 62/255, 94/255))
        plt.gca().set_facecolor((20/255, 62/255, 94/255))

        # Adding labels and title
        ax.set_xlabel('Days of the Week', color='white')
        ax.set_ylabel('Drink Amount (ml)', color='white')
        ax.set_title('Drink Amounts per Week', color='white')

        # Adjusting tick color
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # Display the plot
        plt.show()
 
    def show_profile(self):
        self.my_profile = Profile(self.user_name)  # Pass username to Profile
        self.my_profile.show()

    def show_about(self):
        self.about_us = AboutUs()
        self.about_us.show()


class Profile(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        uic.loadUi('profile.ui', self)

        self.text_profile = self.findChild(QLabel, 'label')
        self.text_profile.setText(user_name)  # Set text with username

        self.show()

class AboutUs(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('about.ui', self)

        self.show()


def login():
    app = QApplication(sys.argv)
    main_window = LoginWindow()
    sys.exit(app.exec_())

# Execute login window
login()
