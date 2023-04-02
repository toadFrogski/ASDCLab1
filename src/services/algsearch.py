import math
from functools import reduce
from src.services.timer import timer

class ListSearch():
    """
    'ListSearch' class contains the list search methods needed for the lab work

    Methods
    -------
        * lineal_search
        * binary_search
        * fibbonachi_search
        * interpolar_search
    """

    @timer
    def lineal_search(items, field, value):
        """
        The function implements a linear search algorithm 

        Parameters
        ----------
        items: Student[]
            List that contains student objects 
        field: String
            Name of attribute we want to find
        value: Any
            Value of attribute we want to find


        Return
        ------
        Student | None
        """
        for item in items:
            if getattr(item, field) == value:
                return item
        return

    @timer
    def binary_search(items, field, value):
        """
        The function implements a binary search algorithm 

        Parameters
        ----------
        items: Student[]
            List that contains student objects 
        field: String
            Name of attribute we want to find
        value: Any
            Value of attribute we want to find

        Return
        ------
        Student | None
        """
        low = 0
        high = len(items) - 1
        mid = high - low // 2
        while getattr(items[mid], field) != value and low <= high:
            if value > getattr(items[mid], field):
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return items[mid] if low <= high else None

    @timer
    def fibbonachi_search(items, field, value):
        """
        The function implements a fibbonachi search algorithm 

        Parameters
        ----------
        items: Student[]
            List that contains student objects 
        field: String
            Name of attribute we want to find
        value: Any
            Value of attribute we want to find

        Return
        ------
        Student | None
        """
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
            elif getattr(items[i], field) == value:
                return items[i]
            elif value < getattr(items[i], field):
                if q == 0:
                    return
                i = i - q
                p, q = q, p - q
            elif value > getattr(items[i], field):
                if p == 1:
                    return
                i = i + p
                p = p - q
                q = q - p

    @timer
    def interpolar_search(items, field, value):
        """
        The function implements a interpolar search algorithm 

        Parameters
        ----------
        items: Student[]
            List that contains student objects 
        field: String
            Name of attribute we want to find
        value: Any
            Value of attribute we want to find

        Return
        ------
        Student | None
        """

        def num_interpolar(items, field, value):
            low, high = 0, len(items) - 1
            ilow = getattr(items[low], field)
            ihigh = getattr(items[high], field)
            while ilow < value and ihigh > value:
                if ihigh == ilow:
                    break
                mid = math.floor(
                    low + ((value - ilow) * (high - low)) / (ihigh - ilow))
                imid = getattr(items[mid], field)
                if imid < value:
                    low = mid + 1
                    ilow = getattr(items[low], field)
                elif imid > value:
                    high = mid - 1
                    ihigh = getattr(items[high], field)
                else:
                    return mid

            if ilow == value:
                return items[low]
            if ihigh == value:
                return items[high]

        def str_to_int(string):
            return reduce(lambda x, y: x + y, [ord(char) for char in string])

        def str_interpolar(items, field, value):
            low, high = 0, len(items) - 1
            ilow = str_to_int(getattr(items[low], field))
            ihigh = str_to_int(getattr(items[high], field))
            value = str_to_int(value)
            while ilow < value and ihigh > value:
                if ihigh == ilow:
                    break
                mid = math.floor(
                    low + ((value - ilow) * (high - low)) / (ihigh - ilow))
                imid = str_to_int(getattr(items[mid], field))
                if imid < value:
                    low = mid + 1
                    ilow = str_to_int(getattr(items[low], field))
                elif imid > value:
                    high = mid - 1
                    ihigh = str_to_int(getattr(items[high], field))
                else:
                    return items[mid]

            if ilow == value:
                return items[low]
            if ihigh == value:
                return items[high]

        if isinstance(getattr(items[0], field), str):
            return str_interpolar(items, field, value)
        else:
            return num_interpolar(items, field, value)


class TreeSearch:
    """
    'TreeSearch' class contains the binary tree search methods needed for the lab work

    Methods
    -------
        * recursive_tree_search
        * binary_tree_search
    """
    @timer
    def recursive_tree_search(root, value):
        """
        The function implements a recursive tree search algorithm 

        Parameters
        ----------
        root: Tree
            'Tree' object 
        value: Any
            Value of attribute we want to find

        Return
        ------
        Any | None
        """

        def find(root, value):
            if root:
                if root.value == value:
                    result.append(root)
                find(root.left, value)
                find(root.right, value)

        result = []
        find(root, value)
        return result[0] if len(result) else None

    @timer
    def binary_tree_search(root, value):
        """
        The function implements a binary tree search algorithm 

        Parameters
        ----------
        root: Tree
            'Tree' object 
        value: Any
            Value of attribute we want to find

        Return
        ------
        Any | None
        """

        def find(root, value):
            if value < root.value:
                find(root.left, value)
            elif value > root.value:
                find(root.right, value)
            elif value == root.value:
                return root
        return find(root, value)
