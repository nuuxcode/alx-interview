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
    setofkeys = []
    counter = 0
    total_boxes = len(boxes)
    for key in boxes[0]:
        if key < total_boxes and key not in setofkeys and key > 0:
            setofkeys.append(key)
            counter +=1
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        #print("setofkeys", setofkeys)
        #print("setofkeys length start:", len(setofkeys))
        #print("key number:", setkey)
        #print("opening box:", boxes[setkey])
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if key < total_boxes and key not in setofkeys and key > 0:
                setofkeys.append(key)
                counter +=1
        index += 1
        #print("setofkeys", setofkeys)
        #print("setofkeys length  end:", len(setofkeys))
        #print("++++++")
    print("total keys:", counter)
    if (counter == total_boxes-1):
        return True
    else:
        return False
