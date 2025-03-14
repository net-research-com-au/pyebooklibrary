import pymupdf
import re

## Settings
PAGES_TO_READ = 10
# isbn_pattern = r"((978[-– ])?[0-9][0-9-– ]{10}[-– ][0-9xX])|((978)?[0-9]{9}[0-9Xx])"
# isbn_pattern = r'\b(?:\d{3}[- ]?)?\d{1,5}[- ]?\d{1,7}[- ]?\d{1,7}[- ]?\d{1,7}|\d{10}|\d{13}\b'
isbn_pattern = r'ISBN.* (.*)'


pdfsrcfile = "goodmath.pdf"
# pdfsrcfile = "datascienceessentialsinpython.pdf"
# pdfsrcfile = "practicalcybersecurityarchitecture.pdf"

def pdfreadext(PAGES_TO_READ, isbn_pattern, pdfsrcfile):
    doc = pymupdf.open(pdfsrcfile) #open document
    metadata = doc.metadata
    pagecount = doc.page_count

    # add pagecount to meta data
    metadata['extratedpagecount'] = pagecount

    if pagecount > PAGES_TO_READ:
        for i,page in enumerate(doc.pages(0,PAGES_TO_READ,1)):
            print(f"{i}. Searching...")
        # text = page.search_for("ISBN")
            text = page.get_text()
            print(text)

        ## Find all ISBN numbers in the text
        # isbn_numbers = re.findall(isbn_pattern, text)
            gotisbn = re.search(isbn_pattern, text)
    
        ## Clean the ISBN numbers by removing hyphens or spaces
        # cleaned_isbns = [isbn.replace('-', '').replace(' ', '') for isbn in isbn_numbers]

        #print(isbn_numbers)
            if gotisbn is not None:
                print(gotisbn.groups())
                isbn_num = gotisbn.groups()[0]
                break
            else:
                isbn_num = None
    # add ISBN to metadata

    metadata['isbn'] = isbn_num
    return metadata


if __name__ == '__main__':
    metadata = pdfreadext(PAGES_TO_READ, isbn_pattern, pdfsrcfile)

    print(f"Metadata of file {pdfsrcfile} is \n")
    [print(f"{item}: {metadata[item]} ") for item in metadata]

# print(f"Page count {pagecount}")

# if pagecount > PAGES_TO_READ:
#     for i,page in enumerate(doc.pages(0,PAGES_TO_READ,1)):
#         print(f"{i}. Searching...")
#         # text = page.search_for("ISBN")
#         text = page.get_text()

#         # Find all ISBN numbers in the text
#         isbn_numbers = re.findall(isbn_pattern, text)
#         gotisbn = re.search(isbn_pattern, text)
    
#         # Clean the ISBN numbers by removing hyphens or spaces
#         cleaned_isbns = [isbn.replace('-', '').replace(' ', '') for isbn in isbn_numbers]

#         print(isbn_numbers)
#         if gotisbn is not None:
#             print(gotisbn.groups()[0])
