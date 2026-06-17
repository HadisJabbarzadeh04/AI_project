from algorithms.uninformed_search.dls import DLS


class IDS:

    def search(self, problem):

        dls = DLS()
        depth = 0

        while True:

            print( "=" * 50)
            print(f"ITERATION WITH DEPTH = {depth}")
            print("=" * 50)

            result = dls.search(
                problem,
                limit=depth
            )

            if result["status"] == "success":
                return result

            if result["status"] == "failure":
                return None

            depth += 1