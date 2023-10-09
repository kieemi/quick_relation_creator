from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class AttributesTableWidget(QWidget):
    def __init__(self, parent=None):
        super(AttributesTableWidget, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        # Create a layout for the widget
        layout = QVBoxLayout(self)

        # Create a table widget
        self.table_widget = QTableWidget()

        # Add the table widget to the layout
        layout.addWidget(self.table_widget)

        # Set the layout for the widget
        self.setLayout(layout)

    def set_table_data(self, attribute_data):
        # Clear existing data
        self.table_widget.clear()

        # Set the number of rows and columns in the table
        num_rows = len(attribute_data)
        num_cols = len(attribute_data[0])
        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_cols)

        # Add data to the table
        for i, row in enumerate(attribute_data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(i, j, item)