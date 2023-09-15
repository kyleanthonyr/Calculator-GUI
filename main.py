from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime


# Create a class for the main window, with parent class QWidget
class AgeCalculator(QWidget):
    def __init__(self):
        # allows access to parent class attributes and methods
        super().__init__()

        # Set Window Title
        self.setWindowTitle("Age Calculator")

        # overwrites __init__ func with custome controls for widgets
        grid = QGridLayout()

        # Name label and line edit widgets
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        # Data label and line edit widgets
        date_birth_label = QLabel("Data of Birth (DD/MM/YYY): ")
        self.date_birth_line_edit = QLineEdit()

        # Calculate button
        calculate_btn = QPushButton("Calculate Age")
        calculate_btn.clicked.connect(self.calculate_age)

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_btn, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        # Add grid object to age_calculator instance using method from parent class
        self.setLayout(grid)

    def calculate_age(self):
        # Get current year
        curr_year = datetime.now().year

        # Extract user birthdate from input
        date_of_birth = self.date_birth_line_edit.text()

        year_of_birth = datetime.strptime(
            date_of_birth, '%m/%d/%Y').date().year

        # Calculate age
        age = curr_year - year_of_birth
        self.output_label.setText(
            f"{self.name_line_edit.text()} is {age} years old.")


if __name__ == "__main__":
    # Create App instance
    app = QApplication(sys.argv)

    # Create calculator instance
    age_calculator = AgeCalculator()

    # Show calculator window
    age_calculator.show()

    # Exit app
    sys.exit(app.exec())
