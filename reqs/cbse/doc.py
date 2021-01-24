from cbse.req import Req, ReqType, Path

class Doc:
    def __init__(self, title: str):
        self.reqs = list()
        self.title = title

    def req(self, id, text: str, req_type: ReqType, trace_filepath: Path = None, trace_function: str = None, function_hash: str = None):
        r = Req(id, text, req_type, trace_filepath, trace_function, function_hash)
        self.reqs.append(r)

    def export(self, file_path:Path=None, title: str = None):
        if not file_path:
            return

        # Create table from requirements
        from cbse.table import Table
        table = Table()
        if len(self.reqs) > 0:
            table.set_header(self.reqs[0].create_header())
        for req in self.reqs:
            table.add_row(req.create_row())

        template_vars = {"title" : self.title, "content": table.to_html()}

        # create html document
        from jinja2 import Environment, FileSystemLoader
        env = Environment(loader=FileSystemLoader('.'))
        template_path = Path('reqs')/ 'cbse' / 'templates' / 'report.html'
        template = env.get_template( template_path.as_posix() )
        html_out = template.render(template_vars)

        # create pdf document
        from weasyprint import HTML
        HTML(string=html_out).write_pdf(file_path.as_posix())