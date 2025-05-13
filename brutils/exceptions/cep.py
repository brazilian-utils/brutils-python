class InvalidCEP(ValueError):
    def __init__(self, cep):
        self.cep = cep
        super().__init__(f"CEP '{cep}' is invalid.")


class CEPNotFound(ValueError):
    def __init__(self, cep):
        self.cep = cep
        super().__init__(f"CEP '{cep}' not found.")
