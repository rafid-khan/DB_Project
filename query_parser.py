import re

class QueryParser:
    def parse(self, query):
        """Parses a SQL-like query and returns tokens."""
        query = query.strip().lower()
        if query.startswith("create table"):
            match = re.match(r"create table (\w+) \((.+)\)", query)
            if match:
                table, columns = match.groups()
                return {"action": "create_table", "table": table, "columns": columns}
        elif query.startswith("insert into"):
            match = re.match(r"insert into (\w+) values \((.+)\)", query)
            if match:
                table, values = match.groups()
                return {"action": "insert", "table": table, "values": values}
        elif query.startswith("select * from"):
            match = re.match(r"select \* from (\w+)", query)
            if match:
                return {"action": "select", "table": match.group(1)}
        return {"error": "Invalid query"}
