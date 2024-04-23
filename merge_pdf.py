import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Open the first PDF file
    with open(pdf1_path, 'rb') as pdf1_file:
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        
        # Open the second PDF file
        with open(pdf2_path, 'rb') as pdf2_file:
            pdf2_reader = PyPDF2.PdfReader(pdf2_file)
            
            # Create a new PDF writer object
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add all pages from the first PDF file to the writer
            for page_num in range(len(pdf1_reader.pages)):
                page = pdf1_reader.pages[page_num]
                pdf_writer.add_page(page)
                
            # Add all pages from the second PDF file to the writer
            for page_num in range(len(pdf2_reader.pages)):
                page = pdf2_reader.pages[page_num]
                pdf_writer.add_page(page)
                
            # Write the merged PDF to the output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

if __name__ == "__main__":
  merge_pdfs("Resume_Ekaterina_Gorbunova_Full_Stack_Developer.pdf", "Wage_Subsidy_Letter_Ekaterina_Gorbunova.pdf", "merged_file.pdf")

# Usage example
# merge_pdfs("file1.pdf", "file2.pdf", "merged_file.pdf")