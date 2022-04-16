import json
import logging
from django.http import JsonResponse, HttpResponse
import datetime
import psycopg2
from config import database, database_password, database_username, port_name, hostname
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

client_error = 400
conn = psycopg2.connect(database=database, user=database_username, host=hostname, password=database_password,
                        port=port_name)
logger = logging.getLogger(__name__)


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


@csrf_exempt
def register(request) -> JsonResponse:

    """
    Documentation for API call to Register a User.
    Requirements:
        1. POST Request is required.
        2. Content Type of Request should be Application/JSON.
        3. Attach the Data in Body Section of JSON request and not in Parameter Section.
            i.e. URL/api/../?test=value will not work.
        4. Please follow naming conventions with the cases (small case, words divided using underscores).

        NOTICE: Both Students and Alumni contain personal_details. Key 'academic' should be sent only with
            registration request of Student and not with Alumni. This should be followed for Alumni Specific
            fields too.

        * The body section for the request for registration of a Student should follow the template given below.

        {
            "personal_details": {
                "name": "Sarvesh Joshi",
                "gender": "Male",
                "password":"abracadabra",
                "account": "Student",
                "email": "valid@moderncoe.edu.in",
                "contact_number": "9988776655",
                "about": "anysing"
            },
            "academic": {
                "branch": "1",
                "year": "2",
                "skills": ["2", "3", "5", "6", "8"]
            },
            "social": {
                "linkedin": null,
                "twitter": "https://www.twitter.com/_SarveshJoshi",
                "github": "https://www.github.com/SarveshJoshi25",
                "portfolio": null
            }
        }
    """
    if request.method != "POST":
        print("A Post Request was expected.")
        return JsonResponse({'error': "A POST Request was expected."}, status=client_error)
    if not request.content_type == "application/json":
        print("JSON Data was expected.")
        return JsonResponse({'error': "JSON Data was expected."}, status=client_error)
    try:
        received_data = json.loads(request.body.decode("utf-8"))

        if received_data["personal_details"]["account"] == "Student":
            print(received_data["personal_details"]["email"])
        else:
            print("Alumni Account")

        return JsonResponse({"message": "working"})
    except KeyError:
        print("Key Error is generated.")
        return JsonResponse({"error": "Key/Keys not found."}, status=client_error)
    except json.decoder.JSONDecodeError:
        print("JSON Decoder has raised an error.")
        return JsonResponse({"error": "Inaccurate JSON Data."}, status=client_error)
    except:
        print("Some Error has occurred. ")
        return JsonResponse({"error": "Some Error has occurred. Please try again."}, status=client_error)


def login(request) -> JsonResponse:
    return JsonResponse({'message': "working"})
