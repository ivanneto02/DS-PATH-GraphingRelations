def get_queries(CUIS=[]):
    queries = []
    base_query = 'SELECT CUI1, RELA, CUI2 FROM MRREL WHERE SAB = "RXNORM" AND CUI1 = "[REPLACE]"'
    for cui in CUIS:
        queries.append( base_query.replace("[REPLACE]", cui) )
    return queries

if __name__ == "__main__":
    print("Running get_queries module of RXNormVisualize package.")
    queries = get_queries(["C0000000", "C0000001", "C0000002"])
    print("Default Queries:\n")
    print(queries)