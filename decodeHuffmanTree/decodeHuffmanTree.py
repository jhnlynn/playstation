class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


class DecodeHuff:
    """
    class Node:
        def __init__(self, freq,data):
            self.freq= freq
            self.data=data
            self.left = None
            self.right = None
    """

    def decodeHuff(self, root, S):
        def decode(root, S):
            if not S:
                return 0
            if not root.left and not root.right:
                res.append(root.data)
                return 0

            x = S[0]
            if not S[1:]:
                if x == '1':
                    res.append(root.right.data)
                else:
                    res.append(root.left.data)

            if x == '1':
                return 1 + decode(root.right, S[1:])
            else:
                return 1 + decode(root.left, S[1:])

        res = []
        while S:
            Len = decode(root, S)
            S = S[Len:]

        print(''.join(res))
