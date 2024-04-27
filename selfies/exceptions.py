class SMILESParserError(ValueError):
    """Exception raised when a SMILES fails to be parsed.
    """

    def __init__(self, smiles, reason="N/A", idx=-1):
        self.smiles = smiles
        self.idx = idx
        self.reason = reason

    def __str__(self):
        pointer = " " * self.idx + "^"
        return (f"\n"
                f"\tSMILES: {self.smiles}\n"
                f"\t        {pointer}\n"
                f"\tIndex:  {self.idx}\n"
                f"\tReason: {self.reason}")


class EncoderError(Exception):
    """Exception raised by :func:`selfies.encoder`.
    """

    pass


class DecoderError(Exception):
    """Exception raised by :func:`selfies.decoder`.
    """

    pass
