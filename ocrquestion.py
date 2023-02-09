import os
import PyPDF2

path = "."
pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
errors = []

for pdf_file in pdf_files:
    try:
        pdf = PyPDF2.PdfReader(pdf_file)
        has_text = False
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                has_text = True
                break
        
        if not has_text:
            os.rename(pdf_file, "ocr_pending_" + pdf_file)
    except Exception as e:
        errors.append(pdf_file + ": " + str(e))

if errors:
    with open("errors.txt", "w") as f:
        for error in errors:
            f.write(error + "\n")
    print("The following errors occurred:")
    for error in errors:
        print(error)
else:
    print("All PDF files processed successfully")
