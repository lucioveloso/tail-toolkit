#!/usr/bin/env python

import logger
import boto3

class Utils:

    def __init__(self):
        pass


    @staticmethod
    def docstring_parameter(*sub):
        def dec(obj):
            obj.__doc__ = sub[0].cli[obj.func_name]['default_help']
            return obj
        return dec

    @staticmethod
    def click_list_runtime():
        return ['python2.7', 'python3.6', 'nodejs6.10', 'nodejs4.3', 'nodejs4.3-edge']

    @staticmethod
    def click_get_command_choice(command, conf):
        opts = ['']
        if command in conf.cli:
            for opt in conf.cli[command]['commands']:
                opts.append(opt)

        return opts

    @staticmethod
    def click_validate_required_options(ctx,conf):
        if ctx.info_name in conf.cli:
            if ctx.params['action'] in conf.cli[ctx.info_name]['commands']:
                for check in conf.cli[ctx.info_name]['commands'][ctx.params['action']]:
                    if ctx.params[check] is None or ctx.params[check] is False:
                        print("The option '--" + check + "' is required");
                        exit(1)

