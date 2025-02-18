import struct

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def write_record(self, record):
        """Writes a record to the database file."""
        with open(self.filename, "ab") as f:
            f.write(struct.pack("50s", record.encode()))

    def read_records(self):
        """Reads all records from the database file."""
        records = []
        with open(self.filename, "rb") as f:
            while chunk := f.read(50):
                records.append(chunk.decode().strip("\x00"))
        return records
