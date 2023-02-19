from src.services.timer import timer


class ListSearch():

    @timer
    def lineal_search(items, field, value):
        for item in items:
            if item.__dict__[field] == value:
                return item
        return


    @timer
    def binary_search(items, field, value):
        low = 0
        high = len(items) - 1
        mid = high - low // 2
        while items[mid].__dict__[field] != value and low <= high:
            if value > items[mid].__dict__[field]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return items[mid] if low <= high else None


    @timer
    def fibbonachi_search(items, field, value):

        fibs = [0, 1, 1]
        while True:
            fib = fibs[-1] + fibs[-2]
            if fib > len(items):
                break
            fibs.append(fibs[-1] + fibs[-2])
        M = fib - len(items) - 1
        i = fibs[-1] - M
        p = fibs[-2]
        q = fibs[-3]

        while True:
            if i < 0:
                if q == 0:
                    return
                i = i - q
                p, q = q, p - q
            elif i >= len(items):
                if p == 1:
                    return
                i = i + p
                p = p - q
                q = q - p
            elif items[i].__dict__[field] == value:
                return items[i]
            elif value < items[i].__dict__[field]:
                if q == 0:
                    return
                i = i - q
                p, q = q, p - q
            elif value > items[i].__dict__[field]:
                if p == 1:
                    return
                i = i + p
                p = p - q
                q = q - p


class TreeSearch:

    @timer
    def recursive_tree_search(root, value):
        result = None
        if root:
            if root.value == value:
                return root
            result = TreeSearch.recursive_tree_search(root.left, value)
            result = TreeSearch.recursive_tree_search(root.right, value)
        return result

    @timer
    def bintree_linear_search(root, value):
        if value < root.value:
            return TreeSearch.bintree_linear_search(root.left, value)
        elif value > root.value:
            return TreeSearch.bintree_linear_search(root.right, value)
        elif value == root.value:
            return root
