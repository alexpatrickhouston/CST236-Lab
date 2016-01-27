from nose2.events import Plugin
import logging


class ReqTracer(Plugin):
    configSection = 'req-tracer'

    def afterSummaryReport(self, event):
        print("Req_Tracer_Running")
        with open("Requirements_Traces.txt", "w") as f:  # open and write to Project_Traces.txt
            for key, item in Requirements.items():  # iterate through the keys
                f.write(key + ' ' + str(item.func_name) + '\n')
        print("Job_Story_Tracer_Running")
        with open("Job_Story_Traces.txt", "w") as f:
            for story in Stories:
                f.write(story.job_story_text + ' ' + str(story.func_name) + '\n')


Requirements = {}
Stories = []


class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


class JobStoryTrace(object):
    job_story_text = ""

    def __init__(self, text):
        self.job_story_text = text
        self.func_name = []


def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper


def story(js):
    def wrapper(func):
        def add_story_and_call(*args, **kwargs):
            for job_story in Stories:
                if job_story.job_story_text.lower()==js.lower():
                    job_story.func_name.append(func.__name__)
                    break
            else:
                raise Exception('Story [0] not defined'.format(js))

            return func(*args, **kwargs)

        return add_story_and_call

    return wrapper


with open('Project_Requirements.txt') as f:
    for line in f.readlines():
        # print("Req_Tracer_Running")
        if '#00' in line:  # if the line starts with #00 then
            req_id, desc = line.split(' ', 1)  # split the line by the space between and set variables
            Requirements[req_id] = RequirementTrace(desc)  # set the key value to be the req_id and
        if '*' in line:
            job_story = line.split(' ', 1)[1]
            Stories.append(JobStoryTrace(job_story.strip()))
