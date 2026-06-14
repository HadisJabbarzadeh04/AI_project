from dls import DLS


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

            if result.success:
                return result

            depth += 1