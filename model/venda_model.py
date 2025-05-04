from datetime import date


class VendaModel:
    def __init__(self, codigo_funcionario: str, data: date):
        self.data = data
        self.codigo_funcionario = codigo_funcionario
