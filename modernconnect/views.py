from django.http import JsonResponse
import psycopg2
from config import database, database_password, database_username, port_name, hostname

# Create your views here.

client_error = 400
conn = psycopg2.connect(database=database, user=database_username, host=hostname, password=database_password,
                        port=port_name)


def index(request) -> JsonResponse:
    return JsonResponse({"message": "Congratulations, This is working!"})


def skills(request) -> JsonResponse:
    # {
    #     "skills": [
    #         {
    #             "skill_id" : "4552", "skill_title" : "Python"
    #         },
    #         {
    #             "skill_id" : "4522", "skill_title" : "JS"
    #         }
    #               ]
    # }
    cur = conn.cursor()
    cur.execute("select skill_id, title from skills;")
    skillList = cur.fetchall()
    message = []
    for each in skillList:
        message.append({"skill_id": each[0], "skill_title": each[1]})
    return JsonResponse({"skills": message})


def register(request) -> JsonResponse:
    if not request.POST:
        print("A Post Request was expected.")
        return JsonResponse({'error': "A POST Request was expected."}, status=client_error)
    print(request.name)
    return JsonResponse({"message": "working"})


def login(request) -> JsonResponse:
    return JsonResponse({'message': "working"})
