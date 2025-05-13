class InvalidCNPJ(ValueError):
    def __init__(self, cnpj):
        self.cnpj = cnpj
        super().__init__(f"CNPJ '{cnpj}' is invalid.")


class CNPJNotFound(ValueError):
    def __init__(self, cnpj):
        self.cnpj = cnpj
        super().__init__(f"CNPJ '{cnpj}' not found.")
