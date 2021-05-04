from itertools import product


def get_prob(unknow, wanted):
    if((unknow == 0) and (wanted == 0)):
        return 1.00
    elif((unknow == 0) and (wanted != 0)):
        return 0.00
    elif((unknow < abs(wanted))):
        return 0.00
    else:
        total = 0.0
        p = 0.0
        for roll in product(['+', '-'], repeat=unknow):
            total = total + 1
            spaces = roll.count("+") - roll.count("-")
            if(spaces == wanted):
                p = p+1
        return float(p/total)


if __name__ == '__main__':
    send = input()
    recived = input()

    positive_send = send.count("+")
    negative_send = send.count("-")
    end_position = positive_send - negative_send

    positive_recived = recived.count("+")
    negative_recived = recived.count("-")
    pre_end_position = positive_recived - negative_recived
    dougth_recived = recived.count("?")
    print(get_prob(dougth_recived, (end_position-pre_end_position)))
