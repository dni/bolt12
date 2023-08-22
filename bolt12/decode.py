""" Bolt12 decoder """


class Bolt12:
    def __init__(self, invoice: str):
        self.invoice = invoice


def decode(invoice: str) -> Bolt12:
    return Bolt12(invoice)
