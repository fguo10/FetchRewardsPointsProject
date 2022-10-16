from app.models import Transaction


def balance():
    trans = Transaction.objects.exclude(unused_points=0).order_by('timestamp')
    for tran in trans:
        print(tran)
        if tran.unused_points < 0:
            previous_trans = trans.filter(payer=tran.payer, timestamp__lt=tran.timestamp
                                          ).order_by('timestamp')
            print(previous_trans)
            cur_points = tran.unused_points
            print(cur_points)
            for prev_tran in previous_trans:
                cur_points += prev_tran.unused_points
                tran.unused_points = 0
                tran.save()
                print('====', prev_tran, cur_points)
                if cur_points == 0:
                    prev_tran.unused_points = 0
                    prev_tran.save()
                    break
                elif cur_points > 0:
                    prev_tran.unused_points = cur_points
                    prev_tran.save()
                    break


def spend(points=5000):
    trans = Transaction.objects.filter(
        is_credit=True).exclude(
        unused_points=0).order_by('timestamp')
    record = {}
    for tran in trans:
        print(tran, tran.unused_points, points)
        points -= tran.unused_points
        print(points)
        if points == 0:
            record[tran.payer] = -tran.unused_points
            tran.unused_points = 0
            tran.save()
            break

        elif points > 0:
            record[tran.payer] = -tran.unused_points
            tran.unused_points = 0
            tran.save()

        else:
            record[tran.payer] = -(points + tran.unused_points)
            tran.unused_points = abs(points)
            tran.save()
            break

        print(record)
    return record


def statistics_points():
    record = {}
    trans = Transaction.objects.order_by('timestamp')
    for tran in trans:
        record[tran.payer] = record.get(tran.payer, 0) + tran.unused_points
    return record
