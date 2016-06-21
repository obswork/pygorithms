"""
Implementation of a priority queue (PQ) in python using underling unsorted list

PQ:
    a collection of prioritized elements allowing arbitrary insertion but removal of the element with
    'first' priority - as determined by an a < b type comparison on the keys

    hint: think stocks or situations in which a queue's FIFO policy is insufficient for the
          application at hand (e.g. plane landings)


    PQ ADT formally supports:
        pq.add(k, v)
            insert item w/ key k, value v into the PQ

        pq.min():
            return the key, value of the item w/ minimum key w/out removing it;
            return an error if the PQ is empty

        pq.remove_min():
            remove the min
"""
