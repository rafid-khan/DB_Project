class Schema:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        """Creates a table schema."""
        self.tables[table_name] = columns

    def get_table(self, table_name):
        """Retrieves schema details for a table."""
        return self.tables.get(table_name)
