def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


cobro_con_envio = calcular_cobro(80000)
cobro_envio_gratis = calcular_cobro(80000, envio=0)

print("Con envío predeterminado:", cobro_con_envio)
print("Con envío gratuito:", cobro_envio_gratis)
