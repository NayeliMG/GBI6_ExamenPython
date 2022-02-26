import Bio
from Bio.Seq import Seq
# cargar biopython a sus módulos, funciones
from Bio import Entrez
import re
# Always tell NCBI who are (edit the e-mail below!)
Entrez.email = "nayeli.mamallacta@est.ikiam.edu.ec"
handle = Entrez.esearch(db = "pubmed",
                        term = "Ecuador genomics[Title/Abstract]",
                        usehistory = "y")
record = Entrez.read(handle)
# generate a Python list with all Pubmed IDs of articles about Dengue Network
id_list = record["IdList"]
print(record["Count"])
webenv = record["WebEnv"]
query_key = record["QueryKey"]
handle = Entrez.efetch(db = "pubmed",
                      rettype = "medline",
                      retmode = "text",
                      retstart = 0,
retmax = 51410, webenv = webenv, query_key = query_key)

handle.read()