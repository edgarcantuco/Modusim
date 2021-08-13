class Sustancia:
    def __init__(self, nombre, formula, PM, GE, Tm, Hm, Tb, Hv, Tc, Pc, w, Zc, Vc, AntoineA, AntoineB, AntoineC, CpGa, CpGb, CpGc, CpGd, CpLa, CpLb, CpLc, CpLd):
        self.nombre = nombre
        self.formula = formula
        self.PM = PM
        self.GE = GE
        self.Tm = Tm
        self.Hm = Hm
        self.Tb = Tb
        self.Hv = Hv
        self.Tc = Tc
        self.Pc = Pc
        self.w = w
        self.Zc = Zc
        self.Vc = Vc
        self.Antoine = self.Antoine(AntoineA, AntoineB, AntoineC)
        self.Gas = self.Estado(CpGa, CpGb, CpGc, CpGd)
        self.Liquido = self.Estado(CpLa, CpLb, CpLc, CpLd)
        
    class Estado:
        def __init__(self, CpA, CpB, CpC, CpD):
            self.Cp = self.cCp(CpA, CpB, CpC, CpD)

        class cCp:
            def __init__(self, A, B, C, D):
                self.A = A
                self.B = B
                self.C = C
                self.D = D

    class Antoine:
        def __init__(self, AntA, AntB, AntC):
            self.A = AntA
            self.B = AntB
            self.C = AntC

class CorrienteDeMateria:
    def __init__(self, nombre, Sustancias, Temperatura, Presion, Flujo, FraccionesMolares, FraccionesMasicas):
        self.nombre = nombre
        self.Sustancias = Sustancias
        self.Temperatura = Temperatura
        self.Presion = Presion
        self.Flujo = Flujo

        if isinstance(FraccionesMolares, list):
            suma = 0
            for x in FraccionesMolares:
                suma += x
            
            if not suma == 1:
                raise NameError('Las fracciones molares definidas no dan igual a 1 en la corriente ' + nombre)
            else:
                self.FraccionesMolares = FraccionesMolares

        else:
            raise NameError('Las fracciones molares tienen que ser definidas como lista. Error en la corriente ' + nombre)

        if isinstance(FraccionesMasicas, list):
            suma = 0
            for x in FraccionesMasicas:
                suma += x
            
            if not suma == 1:
                raise NameError('Las fracciones másicas definidas no dan igual a 1 en la corriente ' + nombre)
            else:
                self.FraccionesMasicas = FraccionesMasicas

        else:
            raise NameError('Las fracciones másicas tienen que ser definidas como lista. Error en la corriente ' + nombre)

class CorrienteDeEnergia:
    def __init__(self, Energia):
        self.Energia = Energia