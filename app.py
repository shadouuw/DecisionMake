from flask import Flask, render_template, request, url_for, redirect
import rdflib
import pandas as pd
from owlready2 import get_ontology
from rdflib import URIRef, Namespace, RDF, Literal, XSD

owlready_ontology = get_ontology("aaa.owl").load()
app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def hello_world():  # put application's code here
    rdfClass = None
    rdfClass2 = None
    rdfClass3 = None

    for classe in owlready_ontology.classes():
        if "aaa.PROJECT_COST_MANAGEMENT" == str(classe):
            rdfClass = classe
        if "aaa.PROJECT_SCHEDULE_MANAGEMENT" == str(classe):
            rdfClass2 = classe
        if "aaa.PROJECT_SCOPE_MANAGEMENT" == str(classe):
            rdfClass3 = classe

    L = []
    stri = ""
    for i in owlready_ontology.get_children_of(rdfClass):
        try:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_COST_MANAGEMENT" + ";" + str(
                owlready_ontology[str(i).replace("aaa.", "")].isDefinedBy[0])
        except:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_COST_MANAGEMENT"

        L.append(stri)
    for i in owlready_ontology.get_children_of(rdfClass2):
        try:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_SCHEDULE_MANAGEMENT" + ";" + str(
                owlready_ontology[str(i).replace("aaa.", "")].isDefinedBy[0])
        except:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_SCHEDULE_MANAGEMENT"

        L.append(stri)
        print(owlready_ontology[str(i).replace("aaa.", "")].isDefinedBy)
    for i in owlready_ontology.get_children_of(rdfClass3):
        try:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_SCOPE_MANAGEMENT" + ";" + str(
                owlready_ontology[str(i).replace("aaa.", "")].isDefinedBy[0])
        except:
            stri = str(i).replace("aaa.", "") + ";" + "PROJECT_SCOPE_MANAGEMENT"

        L.append(stri)

    return render_template("final.html", table=L)


if __name__ == '__main__':
    app.run()
