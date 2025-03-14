import pytest
from pdfextractmeta import pdfreadext

# Define constants
PAGES_TO_READ = 10
isbn_pattern = r'ISBN.* (.*)'
pdfsrcfile = "goodmath.pdf"  # Ensure this file exists in the test environment

def test_pdf_page_count():
    """Test to check if the extracted page count matches the actual page count."""
    metadata = pdfreadext(PAGES_TO_READ, isbn_pattern, pdfsrcfile)
    assert "extratedpagecount" in metadata, "Page count metadata is missing."
    
    expected_page_count = 270  # Replace with the actual number of pages in goodmath.pdf
    actual_page_count = metadata["extratedpagecount"]
    
    assert actual_page_count == expected_page_count, f"Expected {expected_page_count}, but got {actual_page_count}."
