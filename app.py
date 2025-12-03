import streamlit as st

from backend import merge_pdfs

st.markdown(
    "<h1 style='text-align: center;'>Merge PDFs</h1>",
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=['pdf'],
    accept_multiple_files=True)

if uploaded_files:
    merged_pdf = merge_pdfs(uploaded_files)

    if merged_pdf:

        st.success('PDFs merged successfully 😍')

        st.pdf(merged_pdf, height=300)

        output_pdf_name = st.text_input('Enter output file name to download')

        if output_pdf_name:
            st.download_button(
                label="Download PDF",
                data=merged_pdf.getvalue(),
                file_name=output_pdf_name.strip(),
                mime="application/pdf",
            )

    else:
        st.error('Please upload a merged PDF 😉')

