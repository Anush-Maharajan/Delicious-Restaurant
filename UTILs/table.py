class Table:
    def __init__(self, data):
        # Initialize the table with the given data
        lines = data.strip().split('\n')
        self.headers = lines[0].split(',')  # First line as headers
        self.rows = [line.split(',') for line in lines[1:]]  # Remaining lines as rows
        self.data = [self.headers] + self.rows  # Store all data in a 2D list

    def display(self):
        # Determine the maximum width for each column
        column_widths = [max(len(str(item)) for item in column) for column in zip(*self.data)]

        # Display the table
        for row in self.data:
            formatted_row = " | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, column_widths))
            print(formatted_row)
        print("-" * (sum(column_widths) + 3 * (len(self.headers) - 1)))  # Print separator line

