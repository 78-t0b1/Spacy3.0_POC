import spacy
from spacy import displacy
import PyPDF2

nlp = spacy.load('en_core_web_trf')
pdfFileObj = open(
    'C:\\Users\\tanma\\Downloads\\TataComm_all_files\\TataComm_all_files\\msa_format_1\\msa_format_1_epdf\\test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)


doc = nlp(pageObj.extractText())

displacy.render(doc, style='ent')
pdfFileObj.close()
