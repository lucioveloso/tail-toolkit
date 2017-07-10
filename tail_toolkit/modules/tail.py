#!/usr/bin/env python

import boto3
import time
import logger


class Tail:

    def __init__(self, conf, kwargs):
        self.log = logger.get_my_logger(self.__class__.__name__)
        self.conf = conf
        self.loggroupname = kwargs['loggroupname']

    def cloudwatch_tail(self):
        client = boto3.client('logs')
        current_time = int(time.time() * 1000) - int(self.conf.sett['C_CONFIG_TAIL_TIME_PREVIOUS_LOG'])

        print ("Collecting logs in real time, starting from "
               + str(int(self.conf.sett['C_CONFIG_TAIL_TIME_PREVIOUS_LOG']) / 1000 / 60)
               + " minutes ago")

        while True:
            try:
                paginator = client.get_paginator('describe_log_streams')
                for page in paginator.paginate(logGroupName=self.loggroupname):
                    for stream in page.get('logStreams', []):
                        response = client.get_log_events(logGroupName=self.loggroupname,
                                                         logStreamName=stream['logStreamName'],
                                                         startTime=current_time)
                        new_current_time = int(time.time() * 1000)
                        if len(response['events']) > 0:
                            if str(response['events'][len(response['events']) - 1]['message']).startswith('REPORT RequestId:'):
                                for event in response['events']:
                                    print event['message'].rstrip()

                                print("*************")

                                current_time = new_current_time
            except Exception as e:
                self.log.debug(e)
                self.log.critical("Failed to load the logGroupName '" + self.loggroupname + "'.")

            time.sleep(int(self.conf.sett['C_CONFIG_TAIL_TIME_TO_SLEEP']))
