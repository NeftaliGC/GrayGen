import matplotlib.pyplot as plt
from matrixGenerator import MatrixGenerator
import seaborn as sns
import numpy as np

if __name__ == '__main__':
    mxGen = MatrixGenerator(rows=400, columns=400)

    mxGen.generateMatrix()

    matrix = mxGen.getMatrix()

    values = matrix.ravel()
    hist_values, bin_edges = np.histogram(values, bins=256, range=(0, 256), density=True)
    y_min = hist_values.min()
    y_max = hist_values.max()

    # Mostrar la imagen en escala de grises
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(matrix, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.title("Matriz en escala de grises")

    # Graficar la curva de densidad (histograma suavizado)
    plt.subplot(1, 2, 2)
    sns.kdeplot(values, color='black', fill=True, bw_adjust=0.3)
    plt.xlim(0, 255)
    plt.ylim(bottom=y_min)
    plt.title("Densidad de Intensidad")
    plt.xlabel("Intensidad")
    plt.ylabel("Densidad")

    plt.tight_layout()

    # Guardar la figura en formato JPG
    plt.savefig("grafico.jpg", format="jpg", dpi=300)

    plt.show()