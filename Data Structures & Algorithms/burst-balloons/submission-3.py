from typing import List

#Not mine at all wth is going on
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        polygon = [1] + [x for x in nums if x > 0] + [1]
        n = len(polygon)

        if n < 3:
            return 0

        # Rotate the cyclic polygon so a maximum vertex comes first.
        start = max(range(n), key=polygon.__getitem__)
        polygon = polygon[start:] + polygon[:start]
        w = [0] + polygon + [polygon[0]]

        prefix = [0] * (n + 2)
        for i in range(1, n + 2):
            prefix[i] = prefix[i - 1] + w[i - 1] * w[i]

        # Arc data; index 0 represents null.
        u = [0]
        v = [0]
        high = [0]
        base = [0]
        chord = [0]
        num = [0]
        den = [0]

        # Leftist-heap data.
        left = [0]
        right = [0]
        heap_rank = [0]

        children = [[]]

        def new_arc(x: int, y: int) -> int:
            arc = len(u)

            u.append(x)
            v.append(y)
            high.append(x if w[x] >= w[y] else y)

            chord.append(w[x] * w[y])
            base.append(prefix[y] - prefix[x] - chord[arc])

            num.append(0)
            den.append(0)
            left.append(0)
            right.append(0)
            heap_rank.append(1)
            children.append([])

            return arc

        def contains(outer: int, inner: int) -> bool:
            return (
                u[outer] <= u[inner]
                and v[inner] <= v[outer]
            )

        # Enumerate all potential bridge arcs in O(n).
        stack = []
        candidates = []

        for i in range(1, n + 1):
            # Strict comparison is intentional: it handles duplicate values.
            while len(stack) >= 2 and w[stack[-1]] < w[i]:
                candidates.append((stack[-2], i))
                stack.pop()

            stack.append(i)

        while len(stack) >= 4:
            candidates.append((1, stack[-2]))
            stack.pop()

        # Build the laminar containment tree of bridge arcs.
        root = new_arc(1, n + 1)
        arc_stack = []

        for x, y in candidates:
            if x == 1 or y == 1:
                continue

            arc = new_arc(x, y)

            while arc_stack and contains(arc, arc_stack[-1]):
                children[arc].append(arc_stack.pop())

            arc_stack.append(arc)

        while arc_stack:
            children[root].append(arc_stack.pop())

        incident = [[] for _ in range(n + 2)]

        # Oriented Hu-Shing support comparison. Using division or normalizing
        # denominator signs here would make the comparison incorrect.
        def support_less(a: int, b: int) -> bool:
            lhs = num[a] * den[b]
            rhs = num[b] * den[a]

            return lhs < rhs or (lhs == rhs and a < b)

        # Meldable leftist heap.
        def meld(a: int, b: int) -> int:
            if not a:
                return b
            if not b:
                return a

            if support_less(b, a):
                a, b = b, a

            right[a] = meld(right[a], b)

            if heap_rank[left[a]] < heap_rank[right[a]]:
                left[a], right[a] = right[a], left[a]

            heap_rank[a] = heap_rank[right[a]] + 1
            return a

        def heap_push(heap: int, arc: int) -> int:
            left[arc] = right[arc] = 0
            heap_rank[arc] = 1

            incident[u[arc]].append(arc)
            incident[v[arc]].append(arc)

            return meld(heap, arc)

        def heap_pop(heap: int) -> int:
            incident[u[heap]].pop()
            incident[v[heap]].pop()

            return meld(left[heap], right[heap])

        def neighboring_product(arc: int) -> int:
            if arc == root:
                return w[1] * w[2] + w[1] * w[n]

            endpoint = high[arc]

            if endpoint == u[arc]:
                if (
                    not incident[endpoint]
                    or not contains(arc, incident[endpoint][-1])
                ):
                    return w[endpoint] * w[endpoint + 1]
            else:
                if (
                    not incident[endpoint]
                    or not contains(arc, incident[endpoint][-1])
                ):
                    return w[endpoint] * w[endpoint - 1]

            return chord[incident[endpoint][-1]]

        def solve_arc(arc: int) -> int:
            den[arc] = base[arc]
            heap = 0

            if not children[arc]:
                num[arc] = w[high[arc]] * (
                    den[arc]
                    + chord[arc]
                    - neighboring_product(arc)
                )
                return heap_push(0, arc)

            for child in children[arc]:
                heap = meld(heap, solve_arc(child))
                den[arc] -= base[child]

            num[arc] = w[high[arc]] * (
                den[arc]
                + chord[arc]
                - neighboring_product(arc)
            )

            while (
                heap
                and num[heap] < w[high[arc]] * den[heap]
            ):
                den[arc] += den[heap]
                heap = heap_pop(heap)

                num[arc] = w[high[arc]] * (
                    den[arc]
                    + chord[arc]
                    - neighboring_product(arc)
                )

            while (
                heap
                and num[heap] * den[arc]
                <= num[arc] * den[heap]
            ):
                den[arc] += den[heap]
                num[arc] += num[heap]
                heap = heap_pop(heap)

            return heap_push(heap, arc)

        heap = solve_arc(root)
        answer = 0

        while heap:
            answer += num[heap]
            heap = meld(left[heap], right[heap])

        return answer