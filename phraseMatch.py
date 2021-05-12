import spacy
from spacy.matcher import PhraseMatcher
import PyPDF2

pdfFileObj = open(
    'C:\\Users\\tanma\\Downloads\\TataComm_all_files\\TataComm_all_files\\msa_format_1\\msa_format_1_epdf\\test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
terms = ["MASTER SERVICES AGREEMENT"]
# Only run nlp.make_doc to speed things up
patterns = [nlp.make_doc(text) for text in terms]
matcher.add("TerminologyList", patterns)

doc = nlp(pageObj.extractText())
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    print(span.text)

pdfFileObj.close()
