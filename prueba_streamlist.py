import streamlit as st
from fpdf import FPDF
import openpyxl
import io

st.title("Analizador de Idealista")
url = st.text_input("Pega la URL del anuncio de Idealista")

if url:
    # Datos de prueba fijos
    datos = {
        "URL": url,
        "Precio": "250.000 €",
        "m² construidos": "90 m²",
        "Habitaciones": "3",
        "Baños": "2",
        "Planta": "3ª",
        "Año construcción": "1995",
    }

    # --- Generar PDF ---
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Ficha del inmueble", ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", size=12)
    for clave, valor in datos.items():
        pdf.cell(0, 10, f"{clave}: {valor}", ln=True)

    pdf_bytes = bytes(pdf.output())

    # --- Generar Excel ---
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inmueble"
    ws.append(list(datos.keys()))
    ws.append(list(datos.values()))
    excel_buffer = io.BytesIO()
    wb.save(excel_buffer)
    excel_buffer.seek(0)

    st.success("✅ Archivos generados correctamente")

    col1, col2 = st.columns(2)
    with col1:
        st.download_button("📄 Descargar PDF", data=pdf_bytes,
                           file_name="inmueble.pdf", mime="application/pdf")
    with col2:
        st.download_button("📊 Descargar Excel", data=excel_buffer,
                           file_name="inmueble.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")