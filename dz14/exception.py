class ValFormatError(Exception):
    def __str__(self):
        return f"Матрицы разных размеров!"