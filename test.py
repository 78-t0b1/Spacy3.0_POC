import spacy

nlp1 = spacy.load(R".\output\model-best") #load the best model
doc = nlp1("Did you see the F16 fly by just now?") # input sample text

spacy.displacy.render(doc, style="ent", jupyter=True) # display in Jupyter