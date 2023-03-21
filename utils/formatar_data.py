class FormatarData:
    def data_cnab(data):
        try:
            data_formatada = ""
            
            if str(data)[:8].isnumeric():
                ano = str(data)[:4]
                mes = str(data)[4:6]
                dia = str(data)[6:8]
                ano = int(ano)
                if ano >= 2100 or ano <= 1900:
                    raise ValueError("Ano invalido: " + str(ano))
                    
                if mes > "12":
                    raise ValueError("Mes Maior que o permitido: " + str(mes))
                    
                if dia > "31":
                    raise ValueError("Dia Maior o permitido: " + str(dia))
                data_formatada = dia + '/' + mes + '/' + str(ano)

        except Exception as e:
            print('Erro ao formatar numero em hora', e)

        return data_formatada
