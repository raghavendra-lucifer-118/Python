import os
count = 0
img_files = 0
pdf_files = 0
docx_files = 0
pptx_files = 0
mkv_files = 0

directory = os.listdir('C:/Users/Raghavendra/Downloads')
for f in directory:
    count += 1
    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
        img_files += 1
    elif f.endswith(".pdf"):
        pdf_files += 1
    elif f.endswith(".docx"):
        docx_files += 1
    elif f.endswith(".pptx"):
        pptx_files += 1
    else:
        mkv_files += 1


print("Scanning folder: /Users/raghavendra/Downloads")
print("No. Of Files Found: " , count)
print("Preview :")
print("Images    : " , img_files)
print("PDF Files : " , pdf_files)
print("DOCX Files: " , docx_files)
print("PPTX Files: " , pptx_files)
print("MKV Files: " , mkv_files)


print("Dry-run completed. No files were moved.")

