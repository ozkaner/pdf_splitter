import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdfs_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]
    
    for file in files:
        file_path = os.path.join(input_directory, file)
        
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            num_pages = pdf_reader.getNumPages()
            
            for page_num in range(num_pages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(page_num))
                
                output_filename = f"{os.path.splitext(file)[0]}_page_{page_num + 1}.pdf"
                output_path = os.path.join(output_directory, output_filename)
                
                with open(output_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
                
                print(f"Created: {output_filename}")
