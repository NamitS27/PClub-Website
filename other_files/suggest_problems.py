import requests
import random

def get_id():
    response = requests.get('https://codeforces.com/api/contest.list')
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    ids = []
    for contest in response: ids.append(contest["id"])
    ids.sort()
    return ids


# function to get ID of all the problems which are correctly solved by the user
def get_user_handle_ids(handles):
    ids = []
    response = requests.get('https://codeforces.com/api/user.status', params={"handle": handles})
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]

    for problem in response:
        try:
            if problem["verdict"]=='OK':
                ids.append(problem["contestId"])
        except:
            continue
    unique_ids = set(ids)
    return unique_ids


# To eleminate all the solved problem id (by user) and to get problems from the problem id's and generate url
def get_problems(min_rating,max_rating,handle_id,tags=''):

    id1 = get_id()
    id2 = get_user_handle_ids(handle_id)
    ids = set(id1) - set(id2)

    response = requests.get('https://codeforces.com/api/problemset.problems', params={"tags": tags})
    response.raise_for_status()
    response = response.json()
    if response["status"] != "OK":
        print("Invalid response")
        exit()
    response = response["result"]
    problems_response = response["problems"]
    give_problem = set([])
    problems = []

    for problem in problems_response:
        try:
            if problem["contestId"] in ids and (problem["rating"]>=min_rating and problem["rating"]<=max_rating):
                url = 'https://www.codeforces.com/problemset/problem/' + \
                    str(problem["contestId"]) + '/' + problem["index"]
                problems.append(url)
        except:
            continue
    
    while len(give_problem)!=min(2,len(problems)):
        i = random.randint(0, len(problems)-1)
        give_problem.add(problems[i])
    return list(give_problem)