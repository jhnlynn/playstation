class WaysToSum:
    def ways_to_sum(self, N, K) -> int:
        """

        :param N:
        :param K:
        :return:
        """
        # Initialize a list
        dp = [0] * (N + 1)

        # Update dp[0] to 1
        dp[0] = 1

        # Iterate over the range [1, K + 1]
        for row in range(1, K + 1):

            # Iterate over the range [1, N + 1]
            for col in range(1, N + 1):

                # If col is greater
                # than or equal to row
                if col >= row:
                    # Update current
                    # dp[col] state
                    dp[col] = dp[col] + dp[col - row]

        # Return the total number of ways
        return dp[N]


if __name__ == '__main__':
    wts = WaysToSum()
    assert wts.ways_to_sum(8, 2) == 5
