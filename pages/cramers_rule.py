import streamlit as st
import numpy as np

def cramer_rule(A, b):
    n = len(A)
    x = np.zeros(n)

    # menghitung determinan matriks A
    det_A = np.linalg.det(A)

    for i in range(n):
        # mengganti kolom i dengan vektor b
        A_i = np.copy(A)
        A_i[:, i] = b

        # menghitung determinan matriks A_i
        det_A_i = np.linalg.det(A_i)

        # menghitung nilai variabel x_i
        x[i] = det_A_i / det_A

    return x

def main():
    st.title("Metode Cramer's Rule")

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

    # memberikan penyelesian sistem persamaan linier
    if st.button("Hitung"):
        A = np.array(A)
        b = np.array(b)
        try:
            x = cramer_rule(A, b)
            st.write("Solusi Ditemukan:")
            for i in range(n):
                st.write(f"x{i+1} = {x[i]}")
        except np.linalg.LinAlgError:
            st.write("Tidak Ada Solusi yang Ditemukan.")

if __name__ == "__main__":
    main()
