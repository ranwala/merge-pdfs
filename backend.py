from PyPDF2 import PdfMerger
from io import BytesIO

from PyPDF2.errors import PdfReadError

def merge_pdfs(pdf_files: list[str]):
    """ Merge multiple PDF files """

    # Create instance for pdf merger
    merger = PdfMerger()

    # Purpose of this variable is to save merged pdf as bytes for download purpose
    merge_pdf_bytes = BytesIO()

    try:
        for pdf_file in pdf_files:
            merger.append(pdf_file)

        merger.write(merge_pdf_bytes)

        merge_pdf_bytes.seek(0)
        return merge_pdf_bytes

    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except PdfReadError as e:
        print(f'Pdf read error: {e}')
    except Exception as e:
        print(f'Unknown error: {e}')
    finally:
        merger.close()

    return None


# For testing
if __name__ == '__main__':
    merge_pdfs(['test', 'test1'])