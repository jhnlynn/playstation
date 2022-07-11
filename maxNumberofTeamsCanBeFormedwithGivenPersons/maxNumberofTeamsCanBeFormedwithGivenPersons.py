class MaxCanForm:
    def max_can_form(self, n, m):
        def canFormTeam(n, m):
            # 1 person of Type1 and 2 persons of Type2
            # can be chosen
            if n >= 1 and m >= 2:
                return True

            # 1 person of Type2 and 2 persons of Type1
            # can be chosen
            if m >= 1 and n >= 2:
                return True

            # Cannot from a team
            return False

        # To store the required count of teams formed
        count = 0

        while canFormTeam(n, m):
            if n > m:
                # Choose 2 persons of Type1
                n -= 2

                # And 1 person of Type2
                m -= 1

            else:
                # Choose 2 persons of Type2
                m -= 2

                # And 1 person of Type1
                n -= 1

                # Another team has been formed
            count += 1

        return count


if __name__ == '__main__':
    mcf = MaxCanForm()
    assert mcf.max_can_form(4, 5) == 3
