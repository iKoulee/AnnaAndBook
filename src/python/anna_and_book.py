#!/usr/bin/env python

from math import log10

from sympy import source

coins = [1, 2, 5, 10, 20, 50]

class CoinResult(dict):
    def __init__(self, source: dict):
        super().__init__(source)

    def __hash__(self):
        my_hash = 0
        for key in self:
            hash_part = key*self[key]
            if hash_part == 0:
                my_hash = my_hash * 10
            else:
                shift = int(log10(hash_part)) + 1
                my_hash = (my_hash * 10**shift) + hash_part            
        return my_hash

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear       = _immutable
    update      = _immutable
    setdefault  = _immutable
    pop         = _immutable
    popitem     = _immutable


result_set = set()

def collect_money(participants, target=780, coins=coins, depth=0, result={i: 0 for i in coins}):
    """
    Get all possible combinations how to collect target value from participants,
    using coins only with equal share.
    """
    for coin in coins:
        collected = coin * participants
        if collected > target:
            continue
        updated_result = result.copy()
        updated_result[coin] += 1
        if collected == target:
            final_result = CoinResult(updated_result)
            result_set.add(final_result)
            #print(f"Found result: {final_result}")
            continue
        collect_money(participants=participants, target=target-collected, coins=coins, depth=depth+1, result=updated_result)
        


if __name__ == "__main__":

    collect_money(2, target=780)
    print(f"Result set: {result_set}")