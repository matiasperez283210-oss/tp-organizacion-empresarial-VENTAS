import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulación del Dataset de Ventas (Estructura sugerida en la consigna)
data = {
    'id': [1, 2, 3, 4, 5],
    'sales_date': ['2026-01-15', '2026-01-18', '2026-02-10', '2026-02-22', '2026-03-05'],
    'product': ['Teclado Mecánico', 'Mouse Gamer', 'Teclado Mecánico', 'Monitor 24"', 'Mouse Gamer'],
    'quantity': [2, 5, 1, 1, 3],
    'sales_amount': [12000, 3500, 6000, 45000, 2100]
}

df = pd.DataFrame(data)

# Asegurar que los datos se guarden localmente usando rutas relativas
os.makedirs('datos', exist_ok=True)
df.to_csv('datos/dataset_ventas.csv', index=False)
print("-> Dataset guardado con éxito en /datos.")

# 2. Cálculos e Indicadores Comerciales
ventas_totales = (df['quantity'] * df['sales_amount']).sum()
producto_mas_vendido = df.groupby('product')['quantity'].sum().idxmax()

# Convertir fecha para agrupar por mes
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['mes'] = df['sales_date'].dt.strftime('%Y-%m')
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

# Imprimir métricas en consola con comentarios explicativos
print(f"MÉTRICAS COMERCIALES:")
print(f" - Ventas Totales Históricas: ${ventas_totales}")
print(f" - Producto con mayor demanda: {producto_mas_vendido}")
print(f" - Facturación mensual:\n{ventas_por_mes}\n")

# 3. Generación del Gráfico Evolutivo
plt.figure(figsize=(8, 4))
plt.plot(ventas_por_mes.index, ventas_por_mes.values, marker='o', color='darkblue', linestyle='--')
plt.title('Evolución Mensual de Ventas Comerciales', fontsize=12, fontweight='bold')
plt.xlabel('Meses analizados', fontsize=10)
plt.ylabel('Monto Total Facturado ($)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)

# Guardar el gráfico en la carpeta de resultados mediante ruta relativa
os.makedirs('resultados', exist_ok=True)
plt.savefig('resultados/grafico_ventas.png', dpi=300)
plt.close()
print("-> Gráfico evolutivo exportado con éxito a /resultados.")
