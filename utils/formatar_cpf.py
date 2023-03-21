class FormatarCPF:
    def formata_cpf(cpf):
        try:
            cpf = str(cpf)[:3]+'.'+str(cpf)[3:6]+'.'+str(cpf)[6:9]+'-'+str(cpf)[9:12]
        except Exception as e:
            print('Erro ao formatar o cpf', e)
        return cpf