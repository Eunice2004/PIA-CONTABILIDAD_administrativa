import pandas as pd
def separador():
    print(" ")
    print("*"*60)
    print(" ")

#Variables
NombresProductos = ["Producto D","ProductoDI","Producto Z"]
#------------------1---------------------
PrimerSemUnidades = [12000,8000,7000]
PrimerSemPrecio = [250,300,200]

SegundoSemUnidades = [6000,3000,6000]
SegundoSemPrecio = [270,150,180]

PrimerSemVentasEsperadasPesos = []
SegundoSemVentasEsperadasPesos = []

TotalProducto = []
#-------------------2--------------------
SaldoClientes = 50000
SaldoClientesProximoAno_1 = 0
EntradasEfectivo = 0

Cobranza = 50000
CobranzaProximoAno = 0
ProcentajeVentasPeriodo = 80.0

TotalEntradas = 0
SaldoClientesProximoAno_2 = 0
#--------------------3-------------------
PrimerSemUnidadesVender = [12000,8000,7000]
PrimerSemInventarioFinal = [11000,4500,5100]
PrimerSemInventarioInicial = [11000,4500,5100]
PrimerSemTotalUnidades = []
PrimerSemUnidadesProducir = []

SegundoSemUnidadesVender = [6000,3000,6000]
SegundoSemInventarioFinal = [8000,4000,2100]
SegundoSemInventarioInicial = PrimerSemInventarioInicial
SegundoSemTotalUnidades = []
SegundoSemUnidadesProducir = []
#--------------------4-------------------
GramosMaterialA = [10,15,20]
GramosMaterialB = [8,9,8]
GramosMaterialC = [7,5,3]

PrimerSemTotalMaterialA = []
PrimerSemTotalMaterialB = []
PrimerSemTotalMaterialC = []

SegundoSemTotalMaterialA = []
SegundoSemTotalMaterialB = []
SegundoSemTotalMaterialC = []
#--------------------5-------------------

PrimerSemInventarioFinalMaterialA = 11000
PrimerSemInventarioFinalMaterialB = 20000
PrimerSemInventarioFinalMaterialC = 5500

SegundoSemInventarioFinalMaterialA = 9000
SegundoSemInventarioFinalMaterialB = 3000
SegundoSemInventarioFinalMaterialC = 4000

PrimerSemInventarioInicialMaterialA = 11000
PrimerSemInventarioInicialMaterialB = 20000
PrimerSemInventarioInicialMaterialC = 5500

SegundoSemInventarioInicialMaterialA = PrimerSemInventarioInicialMaterialA
SegundoSemInventarioInicialMaterialB = PrimerSemInventarioInicialMaterialB
SegundoSemInventarioInicialMaterialC = PrimerSemInventarioInicialMaterialC

PrimerSemRequerimientoMaterialesA = 0
PrimerSemRequerimientoMaterialesB = 0
PrimerSemRequerimientoMaterialesC = 0

SegundoSemRequerimientoMaterialesA = 0
SegundoSemRequerimientoMaterialesB = 0
SegundoSemRequerimientoMaterialesC = 0

PrimerSemTotalMaterialesA = 0
PrimerSemTotalMaterialesB = 0
PrimerSemTotalMaterialesC = 0

SegundoSemTotalMaterialesA = 0
SegundoSemTotalMaterialesB = 0
SegundoSemTotalMaterialesC = 0

PrimerSemMaterialComprarMaterialA = 0
PrimerSemMaterialComprarMaterialB = 0
PrimerSemMaterialComprarMaterialC = 0

SegundoSemMaterialComprarMaterialA = 0
SegundoSemMaterialComprarMaterialB = 0
SegundoSemMaterialComprarMaterialC = 0

PrimerSemPrecioMaterialA = 3.00
PrimerSemPrecioMaterialB = 3.70
PrimerSemPrecioMaterialC = 5.00

SegundoSemPrecioMaterialA = 3.10
SegundoSemPrecioMaterialB = 4.00
SegundoSemPrecioMaterialC = 5.40

PrimerSemMaterialAPesos = 0.0
PrimerSemMaterialBPesos = 0.0
PrimerSemMaterialCPesos = 0.0

SegundoSemMaterialAPesos = 0.0
SegundoSemMaterialBPesos = 0.0
SegundoSemMaterialCPesos = 0.0

TotalMateriaA = 0.0
TotalMateriaB = 0.0
TotalMateriaC = 0.0

TotalTodoMaterial = 0.0
#--------------------6-------------------
SaldoProveedores = 50000
TotalComprasProximoAno = 0.0
SaldoProveedoresProximoAno = 0.0

PagoProveedores = 50000
PagoProveedoresProximoAno = 0.0
PorcentajeValoresMaterialesComprados = 50.0
TotalPagosProximoAno = 0.0
#--------------------7-------------------
PrimerSemUnidadesManoObra = [12000,8000,7000]
PrimerSemHrsMO = [4,2,1]
PrimerSemTotalHrs = []
PrimerSemPrecioXHora = [12,12,12]
PrimerSemCostoManoObra = []

SegundoSemUnidadesManoObra = [3000,2500,3000]
SegundoSemHrsMO = [4,2,1]
SegundoSemTotalHrs = []
SegundoSemPrecioXHora = [14,14,14]
SegundoSemCostoManoObra = []

TotalHoras = 0
TotalManoObra = 0.0



#1
for producto in range(0,3):
    PrimerSemVentasEsperadasPesos.append(PrimerSemUnidades[producto] * PrimerSemPrecio[producto])

    SegundoSemVentasEsperadasPesos.append(SegundoSemUnidades[producto] * SegundoSemPrecio[producto])

    TotalProducto.append(PrimerSemVentasEsperadasPesos[producto] + SegundoSemVentasEsperadasPesos[producto])
print("-"*94)
print(f'|  {"1.- Propuesta de Venta":^90}|')
for producto in range(0,3):
    print("-"*94)
    print(f'|{NombresProductos[producto]:^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
    print("-"*94)
    print(f'|{"Unidades":^30}|{PrimerSemUnidades[producto]:^30}|{SegundoSemUnidades[producto]:^30}|')
    print("-"*94)
    print(f'|{"Precio":^30}|{PrimerSemPrecio[producto]:^30}|{SegundoSemPrecio[producto]:^30}|')
    print("-"*94)
    print(f'|{"Ventas esperadas en pesos":^30}|{PrimerSemVentasEsperadasPesos[producto]:^30}|{SegundoSemVentasEsperadasPesos[producto]:^30}|')
    print("-"*94)
    print(f'{" ":^30}{" ":^30}  |{"Total = $"+str(TotalProducto[producto]):^30}|')
    print("-"*94)
    print()
    print()

#2
SaldoClientesProximoAno_1 = sum(TotalProducto)
EntradasEfectivo = SaldoClientes + SaldoClientesProximoAno_1
CobranzaProximoAno = SaldoClientesProximoAno_1 * (ProcentajeVentasPeriodo/100)
TotalEntradas = Cobranza + CobranzaProximoAno
SaldoClientesProximoAno_2 = SaldoClientesProximoAno_1 - TotalEntradas

print("-"*94)
print(f'|  {"2.- Determinacion de saldo de clientes y flujo de entradas":^90}|')
print("-"*94)
print(f'| {"Saldo de clientes en 2008":^60}|{SaldoClientes:^30}|')
print("-"*94)
print(f'| {"Saldo de clientes en 2009":^60}|{SaldoClientesProximoAno_1:^30}|')
print("-"*94)
print(f'| {"Entradas de efectivo":^60}|{EntradasEfectivo:^30}|')
print("-"*94)
print(f'| {"Cobranza 2008":^60}|{Cobranza:^30}|')
print("-"*94)
print(f'| {"Cobranza 2009":^60}|{CobranzaProximoAno:^30}|')
print("-"*94)
print(f'| {"Total de entradas 2009":^60}|{TotalEntradas:^30}|')
print("-"*94)
print(f'| {"Saldo de clientes 2009":^60}|{SaldoClientesProximoAno_2:^30}|')
print("-"*94)
#3
for producto in range(0,3):
    PrimerSemTotalUnidades.append(PrimerSemUnidadesVender[producto] + PrimerSemInventarioFinal[producto])
    SegundoSemTotalUnidades.append(SegundoSemUnidadesVender[producto] + SegundoSemInventarioFinal[producto])

    PrimerSemUnidadesProducir.append(PrimerSemTotalUnidades[producto] - PrimerSemInventarioInicial[producto])
    SegundoSemUnidadesProducir.append(SegundoSemTotalUnidades[producto] - SegundoSemInventarioInicial[producto])

print("-"*94)
print(f'|  {"3.- Propuesto de produccion":^90}|')
for producto in range(0,3):
    print("-"*94)
    print(f'|{NombresProductos[producto]:^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
    print("-"*94)
    print(f'|{"Unidades a vender":^30}|{PrimerSemUnidadesVender[producto]:^30}|{SegundoSemUnidadesVender[producto]:^30}|')
    print("-"*94)
    print(f'|{"+ inventario final":^30}|{PrimerSemInventarioFinal[producto]:^30}|{SegundoSemInventarioFinal[producto]:^30}|')
    print("-"*94)
    print(f'|{"= Total de unidades":^30}|{PrimerSemTotalUnidades[producto]:^30}|{SegundoSemTotalUnidades[producto]:^30}|')
    print("-"*94)
    print(f'|{"- inventario final":^30}|{PrimerSemInventarioInicial[producto]:^30}|{SegundoSemInventarioInicial[producto]:^30}|')
    print("-"*94)
    print(f'|{"= Unidades a producir":^30}|{PrimerSemUnidadesProducir[producto]:^30}|{SegundoSemUnidadesProducir[producto]:^30}|')
    print("-"*94)
    print()
    print()
    

#4
for producto in range(0,3):
    PrimerSemTotalMaterialA.append(GramosMaterialA[producto] * PrimerSemUnidadesProducir[producto])
    PrimerSemTotalMaterialB.append(GramosMaterialB[producto] * PrimerSemUnidadesProducir[producto])
    PrimerSemTotalMaterialC.append(GramosMaterialC[producto] * PrimerSemUnidadesProducir[producto])

    SegundoSemTotalMaterialA.append(GramosMaterialA[producto] * SegundoSemUnidadesProducir[producto])
    SegundoSemTotalMaterialB.append(GramosMaterialB[producto] * SegundoSemUnidadesProducir[producto])
    SegundoSemTotalMaterialC.append(GramosMaterialC[producto] * SegundoSemUnidadesProducir[producto])
    
print("-"*94)
print(f'|  {"4.- Presupuesto de requerimiento de materias":^90}|')
for producto in range(0,3):
    print("-"*94)
    print(f'|{NombresProductos[producto]:^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
    print("-"*94)
    print(f'|{"Unidades a producir":^30}|{PrimerSemUnidadesProducir[producto]:^30}|{SegundoSemUnidadesProducir[producto]:^30}|')
    print("-"*94)
    print(f'|{"Material A":^30}|{GramosMaterialA[producto]:^30}|{GramosMaterialA[producto]:^30}|')
    print("-"*94)
    print(f'|{"Material B":^30}|{GramosMaterialB[producto]:^30}|{GramosMaterialB[producto]:^30}|')
    print("-"*94)
    print(f'|{"Material C":^30}|{GramosMaterialC[producto]:^30}|{GramosMaterialC[producto]:^30}|')
    print("-"*94)
    print(f'|{"Total requerido Material A":^30}|{PrimerSemTotalMaterialA[producto]:^30}|{SegundoSemTotalMaterialA[producto]:^30}|')
    print("-"*94)
    print(f'|{"Total requerido Material B":^30}|{PrimerSemTotalMaterialB[producto]:^30}|{SegundoSemTotalMaterialB[producto]:^30}|')
    print("-"*94)
    print(f'|{"Total requerido Material C":^30}|{PrimerSemTotalMaterialC[producto]:^30}|{SegundoSemTotalMaterialC[producto]:^30}|')
    print("-"*94)
    print()
    print()
    
    
    
    

#5
PrimerSemRequerimientoMaterialesA = sum(PrimerSemTotalMaterialA)
PrimerSemRequerimientoMaterialesB = sum(PrimerSemTotalMaterialB)
PrimerSemRequerimientoMaterialesC = sum(PrimerSemTotalMaterialC)

SegundoSemRequerimientoMaterialesA = sum(SegundoSemTotalMaterialA)
SegundoSemRequerimientoMaterialesB = sum(SegundoSemTotalMaterialB)
SegundoSemRequerimientoMaterialesC = sum(SegundoSemTotalMaterialC)

PrimerSemTotalMaterialesA = PrimerSemRequerimientoMaterialesA + PrimerSemInventarioFinalMaterialA
PrimerSemTotalMaterialesB = PrimerSemRequerimientoMaterialesB + PrimerSemInventarioFinalMaterialB
PrimerSemTotalMaterialesC = PrimerSemRequerimientoMaterialesC + PrimerSemInventarioFinalMaterialC

SegundoSemTotalMaterialesA = SegundoSemRequerimientoMaterialesA + SegundoSemInventarioFinalMaterialA
SegundoSemTotalMaterialesB = SegundoSemRequerimientoMaterialesB + SegundoSemInventarioFinalMaterialB
SegundoSemTotalMaterialesC = SegundoSemRequerimientoMaterialesC + SegundoSemInventarioFinalMaterialC

PrimerSemMaterialComprarMaterialA = PrimerSemTotalMaterialesA - PrimerSemInventarioInicialMaterialA
PrimerSemMaterialComprarMaterialB = PrimerSemTotalMaterialesB - PrimerSemInventarioInicialMaterialB
PrimerSemMaterialComprarMaterialC = PrimerSemTotalMaterialesC - PrimerSemInventarioInicialMaterialC

SegundoSemMaterialComprarMaterialA = SegundoSemTotalMaterialesA - SegundoSemInventarioInicialMaterialA
SegundoSemMaterialComprarMaterialB = SegundoSemTotalMaterialesB - SegundoSemInventarioInicialMaterialB
SegundoSemMaterialComprarMaterialC = SegundoSemTotalMaterialesC - SegundoSemInventarioInicialMaterialC

PrimerSemMaterialAPesos = PrimerSemPrecioMaterialA * PrimerSemMaterialComprarMaterialA
PrimerSemMaterialBPesos = PrimerSemPrecioMaterialB * PrimerSemMaterialComprarMaterialB
PrimerSemMaterialCPesos = PrimerSemPrecioMaterialC * PrimerSemMaterialComprarMaterialC

SegundoSemMaterialAPesos = SegundoSemPrecioMaterialA * SegundoSemMaterialComprarMaterialA
SegundoSemMaterialBPesos = SegundoSemPrecioMaterialB * SegundoSemMaterialComprarMaterialB
SegundoSemMaterialCPesos = SegundoSemPrecioMaterialC * SegundoSemMaterialComprarMaterialC

TotalMateriaA = PrimerSemMaterialAPesos + SegundoSemMaterialAPesos
TotalMateriaB = PrimerSemMaterialBPesos + SegundoSemMaterialBPesos
TotalMateriaC = PrimerSemMaterialCPesos + SegundoSemMaterialCPesos

TotalTodoMaterial = TotalMateriaA + TotalMateriaB + TotalMateriaC

print("-"*94)
print(f'|  {"5.- Presupuesto compra de materia":^90}|')
print("-"*94)
print(f'|{"Material A":^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
print("-"*94)
print(f'|{"Requerimiento de materiales":^30}|{PrimerSemRequerimientoMaterialesA:^30}|{SegundoSemRequerimientoMaterialesA:^30}|')
print("-"*94)
print(f'|{"+ inventario final":^30}|{PrimerSemInventarioFinalMaterialA:^30}|{SegundoSemInventarioFinalMaterialA:^30}|')
print("-"*94)
print(f'|{"= Total de materiales":^30}|{PrimerSemTotalMaterialesA:^30}|{SegundoSemTotalMaterialesA:^30}|')
print("-"*94)
print(f'|{"- inventario inicial":^30}|{PrimerSemInventarioInicialMaterialA:^30}|{SegundoSemInventarioInicialMaterialA:^30}|')
print("-"*94)
print(f'|{"= Material a comprar":^30}|{PrimerSemMaterialComprarMaterialA:^30}|{SegundoSemMaterialComprarMaterialA:^30}|')
print("-"*94)
print(f'|{"x precio de compra":^30}|{PrimerSemPrecioMaterialA:^30}|{SegundoSemPrecioMaterialA:^30}|')
print("-"*94)
print(f'|{"= Material A en pesos":^30}|{PrimerSemMaterialAPesos:^30}|{SegundoSemMaterialAPesos:^30}|')
print("-"*94)
print()
print()
print("-"*94)
print(f'|{"Material B":^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
print("-"*94)
print(f'|{"Requerimiento de materiales":^30}|{PrimerSemRequerimientoMaterialesB:^30}|{SegundoSemRequerimientoMaterialesB:^30}|')
print("-"*94)
print(f'|{"+ inventario final":^30}|{PrimerSemInventarioFinalMaterialB:^30}|{SegundoSemInventarioFinalMaterialB:^30}|')
print("-"*94)
print(f'|{"= Total de materiales":^30}|{PrimerSemTotalMaterialesB:^30}|{SegundoSemTotalMaterialesB:^30}|')
print("-"*94)
print(f'|{"- inventario inicial":^30}|{PrimerSemInventarioInicialMaterialB:^30}|{SegundoSemInventarioInicialMaterialB:^30}|')
print("-"*94)
print(f'|{"= Material a comprar":^30}|{PrimerSemMaterialComprarMaterialB:^30}|{SegundoSemMaterialComprarMaterialB:^30}|')
print("-"*94)
print(f'|{"x precio de compra":^30}|{PrimerSemPrecioMaterialB:^30}|{SegundoSemPrecioMaterialB:^30}|')
print("-"*94)
print(f'|{"= Material A en pesos":^30}|{PrimerSemMaterialBPesos:^30}|{SegundoSemMaterialBPesos:^30}|')
print("-"*94)
print()
print()
print("-"*94)
print(f'|{"Material C":^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
print("-"*94)
print(f'|{"Requerimiento de materiales":^30}|{PrimerSemRequerimientoMaterialesC:^30}|{SegundoSemRequerimientoMaterialesC:^30}|')
print("-"*94)
print(f'|{"+ inventario final":^30}|{PrimerSemInventarioFinalMaterialC:^30}|{SegundoSemInventarioFinalMaterialC:^30}|')
print("-"*94)
print(f'|{"= Total de materiales":^30}|{PrimerSemTotalMaterialesC:^30}|{SegundoSemTotalMaterialesC:^30}|')
print("-"*94)
print(f'|{"- inventario inicial":^30}|{PrimerSemInventarioInicialMaterialC:^30}|{SegundoSemInventarioInicialMaterialC:^30}|')
print("-"*94)
print(f'|{"= Material a comprar":^30}|{PrimerSemMaterialComprarMaterialC:^30}|{SegundoSemMaterialComprarMaterialC:^30}|')
print("-"*94)
print(f'|{"x precio de compra":^30}|{PrimerSemPrecioMaterialC:^30}|{SegundoSemPrecioMaterialC:^30}|')
print("-"*94)
print(f'|{"= Material A en pesos":^30}|{PrimerSemMaterialCPesos:^30}|{SegundoSemMaterialCPesos:^30}|')
print("-"*94)
print()
print()
print("-"*94)
print(f'|{"Material A":^30}|{"Material B":^30}|{"Material C":^30}|')
print("-"*94)
print(f'|{TotalMateriaA:^30}|{TotalMateriaB:^30}|{TotalMateriaC:^30}|')
print("-"*94)
print(f'|{" ":^30}|{"Total":^30}|{TotalTodoMaterial:^30}|')
print("-"*94)
print()
print()

#6

TotalComprasProximoAno = TotalTodoMaterial
SaldoClientesProximoAno = SaldoProveedores + TotalComprasProximoAno

PagoProveedoresProximoAno = TotalComprasProximoAno * (PorcentajeValoresMaterialesComprados/100)
TotalPagosProximoAno = PagoProveedores + PagoProveedoresProximoAno

SaldoProveedoresProximoAno =  SaldoClientesProximoAno - TotalPagosProximoAno

print("-"*94)
print(f'|  {"6.- Determinacion de saldo de provedores y flujo de salidas":^90}|')
print("-"*94)
print(f'| {"Saldo de proveedores 2008":^60}|{SaldoProveedores:^30}|')
print("-"*94)
print(f'| {" + compras 2009":^60}|{TotalComprasProximoAno:^30}|')
print("-"*94)
print(f'| {"Saldo de Proveedores 2009":^60}|{SaldoClientesProximoAno:^30}|')
print("-"*94)
print(f'| {"Saldo de efectivo":^60}|{" ":^30}|')
print("-"*94)
print(f'| {"Pago de proveedores 2008":^60}|{PagoProveedores:^30}|')
print("-"*94)
print(f'| {"Pago de proveedores 2009":^60}|{PagoProveedoresProximoAno:^30}|')
print("-"*94)
print(f'| {"Total pagos 2009":^60}|{TotalPagosProximoAno:^30}|')
print("-"*94)
print(f'| {"Saldo de proveedores 2009":^60}|{SaldoProveedoresProximoAno:^30}|')
print("-"*94)

#7
for producto in range(0,3):
    PrimerSemTotalHrs.append(PrimerSemUnidadesManoObra[producto] * PrimerSemHrsMO[producto])

    SegundoSemTotalHrs.append(SegundoSemUnidadesManoObra[producto] * SegundoSemHrsMO[producto])

    PrimerSemCostoManoObra.append(PrimerSemTotalHrs[producto] * PrimerSemPrecioXHora[producto])

    SegundoSemCostoManoObra.append(SegundoSemTotalHrs[producto] * SegundoSemPrecioXHora[producto])

TotalHoras = sum(PrimerSemTotalHrs) + sum(SegundoSemTotalHrs)
TotalManoObra = sum(PrimerSemCostoManoObra) + sum(SegundoSemCostoManoObra)

print("-"*94)
print(f'|  {"7.- Presupuesto de mano de Obra":^90}|')
for producto in range(0,3):
    print("-"*94)
    print(f'|{NombresProductos[producto]:^30}|{"1er Semestre":^30}|{"2do Semestre":^30}|')
    print("-"*94)
    print(f'|{"Unidades a producir":^30}|{PrimerSemUnidadesManoObra[producto]:^30}|{SegundoSemUnidadesManoObra[producto]:^30}|')
    print("-"*94)
    print(f'|{"x Hrs de M.O.":^30}|{PrimerSemHrsMO[producto]:^30}|{SegundoSemHrsMO[producto]:^30}|')
    print("-"*94)
    print(f'|{"= Total de horas":^30}|{PrimerSemTotalHrs[producto]:^30}|{SegundoSemTotalHrs[producto]:^30}|')
    print("-"*94)
    print(f'|{"x Precio por hora":^30}|{PrimerSemPrecioXHora[producto]:^30}|{SegundoSemPrecioXHora[producto]:^30}|')
    print("-"*94)
    print(f'|{"= Costo de Mano O.":^30}|{PrimerSemCostoManoObra[producto]:^30}|{SegundoSemCostoManoObra[producto]:^30}|')
    print("-"*94)
    print()
    print()

print("-"*94)
print(f'| {"Total de hrs":^60}|{TotalHoras:^30}|')
print("-"*94)
print(f'| {"Total de Mano de Obra":^60}|{TotalManoObra:^30}|')
print("-"*94)



#8
separador()
print(f"\n8. Presupuesto de gastos de fabricacion")

depreciacionP8 = 60000
seguros =3500
MantenimientoSem1 =40000
MantenimientoSem2 =45000
EnergeticosSem1 =30000
EnergeticosSem2 = 42000
Varios = 12000


reporte={
" ":[" ","Depreciacion","seguros","Mantenimiento","Energeticos","Varios"],
"  " : ["Semestre 1",depreciacionP8,seguros,MantenimientoSem1,EnergeticosSem1,Varios],
"   " : ["semestre 2",depreciacionP8,seguros,MantenimientoSem2,EnergeticosSem2,Varios]
}

reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)

separador()

TotalGIFSem1 = MantenimientoSem1 + EnergeticosSem1 + (depreciacionP8 ) + seguros  + Varios
TotalGIFSem2 = MantenimientoSem2 + EnergeticosSem2 + depreciacionP8 + seguros  + Varios
TotalGIFAño = TotalGIFSem1+TotalGIFSem2
CostoDeHoraGIF = TotalGIFAño /TotalHoras

reporte={
" ":["Total de GIF","Total de horas","Tasa de gif por unidad"],
"  " : [TotalGIFAño,TotalHoras, CostoDeHoraGIF]
}

reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()
#9


depreciacionP9=10000
saldos_salarios_sem1_eje9=150000
saldos_salarios_sem2_eje9=15000
comisiones_sem1_eje9=272000
comisiones_sem2_eje9=126000
varios_Sem1_eje9=5000
varios_Sem2_eje9=6000
interese_sem1_eje9=20000
interese_sem2_eje9=20000
totalsem1=sum([depreciacionP9,saldos_salarios_sem1_eje9,comisiones_sem1_eje9,varios_Sem1_eje9,interese_sem1_eje9])
totalsem2=sum([depreciacionP9,saldos_salarios_sem2_eje9,comisiones_sem2_eje9,varios_Sem2_eje9,interese_sem2_eje9])
total_eje9=totalsem1+totalsem2

reporte={
" ":[" ","Depreciacion","saldos y salarios","comisiones","varios","intereses por obligacion"," "],
"  " : ["Semestre 1",depreciacionP9,saldos_salarios_sem1_eje9,comisiones_sem1_eje9,
                                varios_Sem1_eje9,interese_sem1_eje9,totalsem1],
"   " : ["semestre 2",depreciacionP9,saldos_salarios_sem2_eje9,comisiones_sem2_eje9,
                                varios_Sem2_eje9,interese_sem2_eje9,totalsem2],
"    ":[" "," "," "," "," "," ",total_eje9]
}


reporte_df=pd.DataFrame(reporte).set_index(" ")


print(f"\n9. Presupuesto de gastos de administracion y ventas")
print(reporte_df)
separador()

#10


COST_MA_PD=3.1
COST_MB_PD=4
COST_MC_PD=5.4
CANT_A_PD=10
CANT_B_PD=8
CANT_C_PD=7
COST_POR_U_MA_PD=COST_MA_PD*CANT_A_PD
COST_POR_U_MB_PD=COST_MB_PD*CANT_B_PD
COST_POR_U_MC_PD=COST_MC_PD*CANT_C_PD
MO_=14
CANT_MO=4
GIF=3.38
CANT_GIF=4
C_POR_U_MO=MO_*CANT_MO
C_POR_U_GIF=GIF*CANT_GIF
TOTALCOSTO=sum([COST_POR_U_MA_PD,COST_POR_U_MB_PD,COST_POR_U_MC_PD,C_POR_U_MO,C_POR_U_GIF])


reporte={
" ":["Producto D","MATERIAL A","MATERIAL B", "MATERIAL C","M O", "GIF"," "],
"  ":["COSTO",COST_MA_PD,COST_MB_PD,COST_MC_PD,MO_,GIF," "],
"   ":["CANTIDAD",CANT_A_PD,CANT_B_PD,CANT_C_PD,CANT_MO,CANT_GIF," "],
"    ":["COSTO POR UNIDAD",COST_POR_U_MA_PD,COST_POR_U_MB_PD,COST_POR_U_MC_PD,C_POR_U_MO,C_POR_U_GIF,TOTALCOSTO]
}

reporte_df=pd.DataFrame(reporte).set_index(" ")

print(f"\n10.  Determinacion de costo unitario de productos terminados")
print(reporte_df)
separador()

COST_MA_PDI=3.1
COST_MB_PDI=4
COST_MC_PDI=5.4
CANT_A_PDI=15
CANT_B_PDI=9
CANT_C_PDI=5
COST_POR_U_MA_PDI=COST_MA_PDI*CANT_A_PDI
COST_POR_U_MB_PDI=COST_MB_PDI*CANT_B_PDI
COST_POR_U_MC_PDI=COST_MC_PDI*CANT_C_PDI
MO_=14
CANT_MO=2
GIF=3.38
CANT_GIF=2
C_POR_U_MO=MO_*CANT_MO
C_POR_U_GIF=GIF*CANT_GIF
TOTALCOSTO=sum([COST_POR_U_MA_PDI,COST_POR_U_MB_PDI,COST_POR_U_MC_PDI,C_POR_U_MO,C_POR_U_GIF])


reporte={
" ":["Producto DI","MATERIAL A","MATERIAL B", "MATERIAL C","M O", "GIF"," "],
"  ":["COSTO",COST_MA_PDI,COST_MB_PDI,COST_MC_PDI,MO_,GIF," "],
"   ":["CANTIDAD",CANT_A_PDI,CANT_B_PDI,CANT_C_PDI,CANT_MO,CANT_GIF," "],
"    ":["COSTO POR UNIDAD",COST_POR_U_MA_PDI,COST_POR_U_MB_PDI,COST_POR_U_MC_PDI,C_POR_U_MO,C_POR_U_GIF,TOTALCOSTO]
}

reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()


COST_MA_PZ=3.1
COST_MB_PZ=4
COST_MC_PZ=5.4
CANT_A_PZ=20
CANT_B_PZ=8
CANT_C_PZ=3
COST_POR_U_MA_PZ=COST_MA_PZ*CANT_A_PZ
COST_POR_U_MB_PZ=COST_MB_PZ*CANT_B_PZ
COST_POR_U_MC_PZ=COST_MC_PZ*CANT_C_PZ
MO_=14
CANT_MO=1
GIF=3.38
CANT_GIF=1
C_POR_U_MO=MO_*CANT_MO
C_POR_U_GIF=GIF*CANT_GIF
TOTALCOSTO=sum([COST_POR_U_MA_PZ,COST_POR_U_MB_PZ,COST_POR_U_MC_PZ,C_POR_U_MO,C_POR_U_GIF])




reporte={
" ":["Producto Z","MATERIAL A","MATERIAL B", "MATERIAL C","M O", "GIF"," "],
"  ":["COSTO",COST_MA_PZ,COST_MB_PZ,COST_MC_PZ,MO_,GIF," "],
"   ":["CANTIDAD",CANT_A_PZ,CANT_B_PZ,CANT_C_PZ,CANT_MO,CANT_GIF," "],
"    ":["COSTO POR UNIDAD",COST_POR_U_MA_PZ,COST_POR_U_MB_PZ,COST_POR_U_MC_PZ,C_POR_U_MO,C_POR_U_GIF,TOTALCOSTO]
}

reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()



#11


print(f"\n11.   valuacion  de inventarios finales")

print(" ")


COST_MA=3.1
COST_MB=4
COST_MC=5.4
CANT_A=9000
CANT_B=3000
CANT_C=4000
COST_POR_U_MA=COST_MA*CANT_A
COST_POR_U_MB=COST_MB*CANT_B
COST_POR_U_MC=COST_MC*CANT_C
TOTALCOSTO=sum([COST_POR_U_MA,COST_POR_U_MB,COST_POR_U_MC])


reporte={
" ":[" ","MATERIAL A","MATERIAL B","MATERIAL C"," "],
"  ":["COSTO",COST_MA,COST_MB,COST_MC," "],
"   ":["CANTIDAD",CANT_A,CANT_B,CANT_C," "],
"    ":["COSTO POR UNIDAD",COST_POR_U_MA,COST_POR_U_MB,COST_POR_U_MC,TOTALCOSTO]
}
print("\t inventario final de materiales")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()



COST_PD=170.32
COST_PDI=144.26
COST_PZ=127.58
CANT_PD=8000
CANT_PDI=4000
CANT_PZ=2100
COST_POR_U_PD=COST_PD*CANT_PD
COST_POR_U_PDI=COST_PDI*CANT_PDI
COST_POR_U_PZ=COST_PZ*CANT_PZ
TOTALCOSTO=sum([COST_POR_U_PD,COST_POR_U_PDI,COST_POR_U_PZ])


reporte={
" ":[" ","PRODUCTO D","PRODUCTO DI","PRODUCTO Z"," "],
"  ":["COSTO",COST_PD,COST_PDI,COST_PZ," "],
"   ":["CANTIDAD",CANT_PD,CANT_PDI,CANT_PZ," "],
"    ":["COSTO POR UNIDAD",COST_POR_U_PD,COST_POR_U_PDI,COST_POR_U_PZ,TOTALCOSTO]
}
print("\t inventario de productos terminados")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()

#Estados de costos de Produccion y ventas

SALDO_INI_M=80005
COMPRA_M=3518250
M_DISP=SALDO_INI_M+COMPRA_M
INV_FIN_M=61500
M_UTILIZADOS=M_DISP-INV_FIN_M
MANO_OBRA=1148000
GIF=307500
COSTO_PROD=sum([M_UTILIZADOS,MANO_OBRA,GIF])
INV_INI_PT=150000
SUM_COSTO_INV_INI=COSTO_PROD+INV_INI_PT
INV_FIN_PT=TOTALCOSTO
COSTO_DE_VENTAS=SUM_COSTO_INV_INI-INV_FIN_PT-SALDO_INI_M


reporte={
" ": ["Saldo inical de materiales","Compra de materiales","Materiales diponibles","Inventario final de materiales","Materiales utilizados",
        "Mano de Obra","GIF","Costo de Produccion","Inventario inical Productos Terminados","Total de produccion disponible",
        "invenario de prod terminados","Costo de verntas"],
"  ":[SALDO_INI_M,COMPRA_M,M_DISP,INV_FIN_M,M_UTILIZADOS,MANO_OBRA,GIF,COSTO_PROD,INV_INI_PT,SUM_COSTO_INV_INI,
        INV_FIN_PT,COSTO_DE_VENTAS]
}

print("\t Estado de costo de produccion y de venta")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()



#ESTADO DE RESULTADOS

VENTAS=9950000
COSTOS_VENTAS=2934774.01
UTILIDAD_BRUTA=VENTAS-COSTO_DE_VENTAS
GASTOS_OPERACION=634000
UTILIDAD_OP=UTILIDAD_BRUTA-GASTOS_OPERACION
ISR=UTILIDAD_OP*0.35
PRECIO_T_UNI=UTILIDAD_OP*0.11
UTILIDAD_NETA=UTILIDAD_OP-ISR-PRECIO_T_UNI

reporte={
" ":["Ventas","Costos de ventas","Utildiad bruta","Gaastos de operacion","Utildiad operativa",
        "ISR","Precio total unitario","Utilidad Neta"],
"  ":[VENTAS,COSTO_DE_VENTAS,UTILIDAD_BRUTA,GASTOS_OPERACION,UTILIDAD_OP,ISR,
        PRECIO_T_UNI,UTILIDAD_NETA]
}


print("\t Estado de Resultados")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()



#FLUJO DE EFECTIVO

SALOO_INICIAL=50000
COBRA_2008=50000
COBRA_2009=7960000
T_COBRA_2009=COBRA_2008+COBRA_2009

PAGO_PROV_08=50000
PAGO_PROV_09=1759125
MANO_OBRA_=1148000
GIF_=187500
GAST_OPE=614000
COMPRA_MAQ=50000
ISR_08=50000
ISR_09=2233492.10
TOTALSALIDAS=6092054.10
FLUJO_EFECTIVO=T_COBRA_2009-TOTALSALIDAS-SALOO_INICIAL



reporte={
" ":["saldo inicial","Cobranza 2008","Cobranza 2009","Total cobranza 2009","Salidas","Pagos Proveedores 2008",
        "Pagos proveedores 2009","Mano de obra","Gastos IF","Gastos de Operacion","Compra de Maquinaria","Pago ISR 2008",
        "Pago ISR 2009","Total de salidas","Flujo de efectivo"],
"  ":[SALOO_INICIAL,COBRA_2008,COBRA_2009,T_COBRA_2009," ",PAGO_PROV_08,PAGO_PROV_09,MANO_OBRA_,GIF_,
        GAST_OPE,COMPRA_MAQ,ISR_08,ISR_09,TOTALSALIDAS,FLUJO_EFECTIVO]
}

print("\t Flujo de efectivo")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)
separador()


#BALANCE GENERAL

#ACTIVOS CIRCULANTES
EFECTIVO=1867945.9
CLIENTES=9950000
INV_MAT=61500
INV_ART_T=2207480.99
T_CIRCULANTES=sum([EFECTIVO,CLIENTES,INV_MAT,INV_ART_T])
#ACTIVOS NO CIRCULANTES
TERRENO=550000
PLANTA_EQUIPO=1050000
DEPRE_ACUM=160000
T_NO_CIRCULANTE=(TERRENO+PLANTA_EQUIPO)-DEPRE_ACUM
ACTIVO_TOTAL=T_CIRCULANTES+T_NO_CIRCULANTE

#PASIVOS CORTO PLAZO
PROVEEDORES=1759125
DOC_PAGAR=100000
PTU=701934.9
IMP_RENTA_PAGAR=sum([PROVEEDORES,DOC_PAGAR,PTU])
#PASIVOS LARGO PLAZO
OBL_PAGAR=150000
TOTAL_PASIVO=IMP_RENTA_PAGAR+OBL_PAGAR

#CAPITAL CONTABLE

CAP_APORTADO=1399380
CAP_GANADO=80625
UTIL_NETA=3445862.03
CAP_CONTABLE=sum([CAP_APORTADO,CAP_GANADO,UTIL_NETA])
PASIVO_CAP_CONTABLE=TOTAL_PASIVO+CAP_CONTABLE


reporte={
" ":["ACTIVO","CIRCULANTES","EFECTIVO","CLIENTES","INVENTARIO MATERIALES","INVENTARIO ART TERMINADOS","TOTAL CIRCULANTE",
        " ","NO CIRCULANTES","TERRENO","PLANTA Y EQUIPO","DEPRECIACION ACUMULADA","TOTAL NO CIRCULANTE","ACTIVO TOTAL"],
"  ":[" "," ",EFECTIVO,CLIENTES,INV_MAT,INV_ART_T,T_CIRCULANTES," "," ",TERRENO,PLANTA_EQUIPO,DEPRE_ACUM,T_NO_CIRCULANTE,
        ACTIVO_TOTAL]
}


print("\t BALANCE GENERAL")
reporte_df=pd.DataFrame(reporte).set_index(" ")

print(reporte_df)

print("\n")

reporte={
"    ":["PASIVOS","A corto plazo","Proveedores ","Documentos por pagar ","PTU","Impuesto, sobre la renta por pagar",
        " "," ","A largo plazo","Obligaciones por pagar","Total pasivo"," ","Capital contable","Capital aportado","Capital ganado",
        "Utilidad Neta","Capital contable","Total pasivo + cap. Contable"],
"     ":[" "," ",PROVEEDORES,DOC_PAGAR,PTU,IMP_RENTA_PAGAR," "," "," ",OBL_PAGAR,TOTAL_PASIVO," "," ",CAP_APORTADO,
            CAP_GANADO,UTIL_NETA,CAP_CONTABLE,PASIVO_CAP_CONTABLE]
}

reporte_df=pd.DataFrame(reporte).set_index("    ")

print(reporte_df)


separador()
