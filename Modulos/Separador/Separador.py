import clases

def Main(inputs, outputs, numoutputs, Parametros):

    for x in outputs:
        x.Temperatura = inputs[0].Temperatura
        x.Presion = inputs[0].Presion
        x.FraccionesMolares = inputs[0].FraccionesMolares
        x.FraccionesMasicas = inputs[0].FraccionesMasicas

    outputs[0].Flujo = inputs[0].Flujo * Parametros[0]
    outputs[1].Flujo = inputs[0].Flujo * (1 - Parametros[0])

    return outputs