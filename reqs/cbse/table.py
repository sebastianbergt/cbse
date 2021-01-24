class Table:
    def __init__(self):
        self.header = list()
        self.rows = list()

    def set_header(self, header: list = []):
        self.header = header

    def add_row(self, row: list = []):
        if row:
            self.rows.append(row)

    def to_html(self) -> str:
        html = "<table>\n"
        html += "  <tr>\n"
        for elem in self.header:
            html += "    <td><b>" + str(elem) + "</b></td>\n"
        html += "  <tr>\n"
        for row in self.rows:
            html += "  <tr>\n"
            for elem in row:
                html += "    <td>" + str(elem) + "</td>\n"
            html += "  <tr>\n"
        html += "</table>\n"
        return html