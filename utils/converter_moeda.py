class Moeda:
    def converterparamoeda(num_cnab) -> float:
        try:
            num_formatted = 0
            if num_cnab.isnumeric():
                num_float = float(num_cnab[:-2] + "." + num_cnab[-2:])
                num_formatted = float(num_formatted) / 100
                num_formatted = "{:.2f}".format(num_float)
        except Exception as e:
            print('Numero inválido', e)
        return num_formatted