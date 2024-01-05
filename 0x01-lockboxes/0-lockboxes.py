#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
            go to box0
                get all keys and add them setofkeys
            start opening boxes from setofkeys
                go to each box of each key
                    and take the keys from it and add them to set of keys
                keep loping through all setof keys
            ignore keys that dont have box
            track opening of boxes by a counter, if at end it equal to lentgh of boxes it mean all boxes unlock
    """
    print("boxes:", boxes)
    print("total boxes", len(boxes))
    setofkeys = set()
    total_boxes = len(boxes)
    for key in boxes[0]:
        if key < total_boxes:
            setofkeys.add(key)
    print("setofkeys", setofkeys)
    index = 0
    while index < len(setofkeys):
        print("key number", setofkeys[index])
        index+=1
    print("-----")

