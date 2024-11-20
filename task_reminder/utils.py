import spacy

nlp = spacy.load("en_core_web_sm")

def categorize_task(task):
    doc = nlp(task)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            return "Work"
    return "Personal"

def extract_due_time(task):
    if 'PM' in task or 'AM' in task:
        return 'time_found'
    return 'no_time_found'
