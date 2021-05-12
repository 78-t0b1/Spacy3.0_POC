from spacy.matcher import DependencyMatcher
from spacy.matcher import Matcher
import spacy

nlp = spacy.blank("en")
matcher = DependencyMatcher(nlp.vocab)
# matcher = Matcher(nlp.vocab)

pattern = [{"RIGHT_ID": "founded_id",
            "RIGHT_ATTRS": {"ORTH": "founded"}}]
matcher.add("FOUNDED", [pattern])
doc = nlp("Bill Gates founded Microsoft.")
matches = matcher(doc)
print(doc[matches[0][1][0]])
