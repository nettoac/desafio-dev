from datetime import datetime, time
import pytz
import unittest

class ConverterHoras:
    def horas(numero_horas):
        try:
            hora_cnab_final = ""
            if str(numero_horas)[:6].isnumeric():
                numero_horas = str(numero_horas)[:2] + ':' + str(
                    numero_horas)[2:4] + ':' + str(numero_horas)[4:6]

            # TODO ajuste no timezone conforme enunciado
            hora_cnab = datetime.strptime(numero_horas, "%H:%M:%S").time()
            # Criando um objeto datetime a partir do objeto time (usando a data de hoje)
            agora = datetime.now()
            hora_cnab_timezone = datetime.combine(agora, hora_cnab)
            # Definindo a timezone atual (UTC padrao -3 conforme enunciado)
            tz = pytz.UTC
            # Definindo a timezone desejada conforme o modelo de entrada
            saida_tz = pytz.timezone("America/Sao_Paulo")

            # Converter para a timezone desejada
            
            hora_cnab_final = tz.localize(hora_cnab_timezone).astimezone(saida_tz)
            hora_cnab_final = hora_cnab_final.time()

            if numero_horas > '23:59:59':
                numero_horas = '-'

        except Exception as e:
            print('Erro ao formatar numero em hora', e)
        return hora_cnab_final
'''
class TestHoras(unittest.TestCase):
    def test_horas_normal(self):
        self.assertEqual(horas('123456'), time(hour=12, minute=34, second=56))
        self.assertEqual(horas('090101'), time(hour=9, minute=1, second=1))
        self.assertEqual(horas('010101'), time(hour=1, minute=1, second=1))
        self.assertEqual(horas('235959'), time(hour=23, minute=59, second=59))
        
    def test_horas_com_ponto(self):
        self.assertEqual(horas('12.34.56'), time(hour=12, minute=34, second=56))
        self.assertEqual(horas('23.59.59'), time(hour=23, minute=59, second=59))
        
    def test_horas_invalidas(self):
        self.assertRaises(ValueError, horas, '24:00:00')
        self.assertRaises(ValueError, horas, '25:00:00')
        self.assertRaises(ValueError, horas, '123')
        
    def test_horas_timezone(self):
        # Hora em UTC-3
        hora_utc3 = time(hour=12, minute=0, second=0)
        agora_utc3 = datetime.now(pytz.timezone("America/Sao_Paulo"))
        hora_utc3_timezone = datetime.combine(agora_utc3, hora_utc3)
        self.assertEqual(hora_utc3_timezone, time(hora_utc3))
        
        # Hora em UTC-5
        hora_utc5 = time(hour=10, minute=0, second=0)
        agora_utc5 = datetime.now(pytz.timezone("America/New_York"))
        hora_utc5_timezone = datetime.combine(agora_utc5, hora_utc5)
        self.assertEqual(hora_utc5_timezone, time(hora_utc5))
        
        # Converter hora UTC-3 para UTC-5
        hora_utc5_convertida = horas(hora_utc3.strftime("%H%M%S"))
        self.assertEqual(hora_utc5_convertida, hora_utc5)
        
if __name__ == '__main__':
    unittest.main()'''