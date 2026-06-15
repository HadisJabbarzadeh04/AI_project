def print_result(result):

    print("\n" + "=" * 40)
    print("FINAL RESULT")
    print("=" * 40)

    if result is None:
        print("No solution found.")
        return

    if "path" in result:
        print("Path:", " -> ".join(result["path"]))

    if "cost" in result:
        print("Cost:", result["cost"])

    if "expanded_nodes" in result:
        print("Expanded Nodes:", result["expanded_nodes"])

    print("=" * 40)