def converterTemperatura(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def imprimirValor(valor):
    valorArredondado = round(valor, 2)
    print('Valor em Celsius: {0}°C'.format(valorArredondado))


f = float(input("Entre com a temperatura em farenheit: "))
valorConvertido = converterTemperatura(f)
imprimirValor(valorConvertido)
