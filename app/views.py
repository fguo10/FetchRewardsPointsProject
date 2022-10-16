from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from app.models import Transaction

# ViewSets define the view behavior.
from rest_framework.views import APIView

from app.models import Transaction
from app.utils import balance, spend, statistics_points


# all the views about Transaction(get, post)
class TransactionDetailsView(APIView):
    def get(self, request):
        trans = Transaction.objects.order_by('timestamp')
        results = []
        for tran in trans:
            results.append({
                'payer': tran.payer,
                'points': tran.points,
                'unused_points': tran.unused_points,
                'timestamp': tran.timestamp,
                'is_credit': tran.is_credit
            })
        return JsonResponse(results, safe=False)

    def post(self, request):
        """
        Suppose you call your add transaction route with the following sequence of calls:
        ● { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
        ● { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" }
        ● { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" }
        ● { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" }
        ● { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" }
        """
        # parse post data
        data = request.data
        payer = data.get('payer').upper()
        points = data.get('points')
        timestamp = data.get('timestamp')

        # validate payer's points to go negative.
        record = statistics_points()
        print(record, payer)
        payer_points = record.get(payer, 0)

        if payer_points + points <= 0:
            return JsonResponse({"msg": "no payer's points to go negative."})

        # save new transaction to db
        transaction = Transaction(
            payer=payer,
            points=points,
            unused_points=points,
            timestamp=timestamp,
            is_credit=(points > 0))
        transaction.save()

        return JsonResponse({'code': 200, 'msg': 'add transaction successfully'})


class PointsView(APIView):
    def get(self, request):
        """
        A subsequent call to the points balance route, after the spend, should returns the following results:
        {
            "DANNON": 1000,
            ”UNILEVER” : 0, ,
            "MILLER COORS": 5300
        }
        """
        record = statistics_points()
        return JsonResponse(record)


class SpendView(APIView):
    def post(self, request):
        """
        Then you call your spend points route with the following request:
        { "points": 5000 }
        The expected response from the spend call would be:
        [
            { "payer": "DANNON", "points": -100 },
            { "payer": "UNILEVER", "points": -200 },
            { "payer": "MILLER COORS", "points": -4,700 }
        ]
        """
        spend_points = request.data['points']
        balance()
        record_json = spend(spend_points)
        return JsonResponse(record_json)
