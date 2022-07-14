def send_queries(queries=[], connection=None):
    # No queries have been passed
    if len(queries) == 0:
        return []
    
    results = []
    print(f"Total queries: {len(queries)}")
    for i in range(len(queries)):
        cursor = connection.cursor()
        print(f"> - Sending query {i+1}...")
        try:
            # Execute the query
            cursor.execute(queries[i])
            # Add the result into the results list
            results.append(cursor.fetchall())
            print(f"> - Success!")
        except:
            print("> - Failure! Something went wrong.")
        cursor.close()

    return results

if __name__ == "__main__":
    print("Running send_queries module of RXNormVisualize package.")
    results = send_queries([])
