## Fetch Rewards Points Project

Coding challenge for Fetch Rewards Backend Software Engineering

To execute this code:

```bash
# Installing the project's dependency packages
pip install -r requirements.txt
# Run the project and start the Django service
python manage.py runserver
```
Starting development server at `http://127.0.0.1:8000/`



## API
Example input/output from [https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf](https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf):

Accepts the following HTTP requests:


| Method | API                        | Desc                                          | request                                                                    | response                                                                                                                     |
|--------|----------------------------|-----------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| POST   | localhost:8000/api/trans/  | add transaction route                         | { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" } | {'code': 200, 'msg': 'add transaction successfully'}                                                                         | 
| GET    | localhost:8000/api/trans/  | get transactions route                        | null                                                                       | [[{"payer": "DANNON","points": 300,"unused_points": 0,"timestamp": "2020-10-31T10:00:00Z","is_credit": true}]                                                                                                                           | 
| POST   | localhost:8000/api/spend/  | spend points route                            | { "points": 5000 }                                                         | [{ "payer": "DANNON", "points": -100 },{ "payer": "UNILEVER", "points": -200 },{ "payer": "MILLER COORS", "points": -4,700}] |
| POST   | localhost:8000/api/points/ | A subsequent call to the points balance route | null                                                                       | {"DANNON": 1000,”UNILEVER” : 0, ,"MILLER COORS": 5300}                                                                       |                                                                                                                            |




## Comments on the challenge
This was a really enjoyable experience!The hardest part was trying to understand the requirements and very important two rules .
 - We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received)
 - We want no payer's points to go negative.

key files:
```bash
- app
  - utils.py
  - views.py
- testCase
```

Thank you again for the opportunity to showcase what I can do and i'm looking forward to discussing the challenge with the engineering team!

