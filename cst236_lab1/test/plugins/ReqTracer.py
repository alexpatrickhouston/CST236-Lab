from nose2.events import Plugin
import logging

log = logging.getLogger('nose2.plugins.ReqTracer')


class ReqTracer(Plugin):
    configSection = 'req-tracer'

    def startTestRun(self, event):
        log.info('Hello pluginized world!')

    def afterSummaryReport(self, event):
        print("Req_Tracer_Running")
        with open("Project_Traces.txt", "w") as f:  # open and write to Project_Traces.txt
            for key, item in Requirements:  # iterate through the keys
                f.write(key + ' ' + item.func_name)


class RequirementTrace(object):
    req_text = ""

    def __init__(self, text):
        self.req_text = text
        self.func_name = []


Requirements = {}


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


with open('Project_Requirements.txt') as f:
    for line in f.readlines():
        # print("Req_Tracer_Running")
        if '#00' in line:  # if the line starts with #00 then
            req_id, desc = line.split(' ', 1)  # split the line by the space between and set variables
            Requirements[req_id] = RequirementTrace(desc)  # set the key value to be the req_id and
