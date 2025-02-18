from src.storage import Storage
from src.schema import Schema
from src.query_parser import QueryParser

class Database:
    def __init__(self):
        self.schema = Schema()
        self.storage = Storage("database.db")
        self.parser = QueryParser()

    def execute(self, query):
        """Parses and executes a given SQL-like query."""
        command = self.parser.parse(query)

        if command["action"] == "create_table":
            self.schema.create_table(command["table"], command["columns"])
            print(f"Table {command['table']} created.")

        elif command["action"] == "insert":
            self.storage.write_record(command["values"])
            print(f"Inserted record into {command['table']}.")

        elif command["action"] == "select":
            records = self.storage.read_records()
            print(f"Records from {command['table']}: {records}")

        else:
            print("Invalid command.")
