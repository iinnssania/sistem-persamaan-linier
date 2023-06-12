import streamlit as st
import numpy as np

def gauss_jordan_elimination(A, b):
    n = len(A)

    # membentuk matriks augmented [A | b]
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        # memproses baris i
        pivot = augmented_matrix[i, i]

        # membagi baris i dengan pivot
        augmented_matrix[i, :] /= pivot

        # mengeliminasi elemen-elemen di bawah pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

        # mengeliminasi elemen-elemen di atas pivot
        for j in range(i):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # memberikan solusi
    x = augmented_matrix[:, -1]
    return x

def main():
    st.title("Metode Eliminasi Gauss-Jordan")

    # memasukkan jumlah variabel
    n = st.number_input("Jumlah Variabel", min_value=2, value=2, step=1)

    # memasukkan nilai koefisien dan batasan
    A = []
    b = []
    for i in range(n):
        st.write(f"Variabel x{i+1}")
        coefficients = []
        for j in range(n):
            coefficients.append(st.number_input(f"Koefisien a{i+1}{j+1}"))
        A.append(coefficients)
        b.append(st.number_input(f"Batasan b{i+1}"))

    # memberikan penyelesaian sistem persamaan linier
    if st.button("Hitung"):
        A = np.array(A)
        b = np.array(b)
        try:
            x = gauss_jordan_elimination(A, b)
            st.write("Solusi Ditemukan:")
            for i in range(n):
                st.write(f"x{i+1} = {x[i]}")
        except np.linalg.LinAlgError:
            st.write("Tidak Ada Solusi yang Ditemukan.")

if __name__ == "__main__":
    main()
