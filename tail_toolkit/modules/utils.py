#!/usr/bin/env python

import os
import pkgutil
import logger


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def click_get_command_choice(command, conf):
        opts = ['']
        if command in conf.cli:
            for opt in conf.cli[command]['commands']:
                opts.append(opt)

        return opts

    @staticmethod
    def docstring_parameter(*sub):
        def dec(obj):
            obj.__doc__ = pkgutil.get_data("tail_toolkit", os.path.join(sub[0].sett['C_HELPS_FILES'], obj.func_name + ".txt"))
            return obj
        return dec

    @staticmethod
    def click_validate_required_options(ctx,conf):
        if ctx.info_name in conf.cli:
            if ctx.params['action'] in conf.cli[ctx.info_name]['commands']:
                for check in conf.cli[ctx.info_name]['commands'][ctx.params['action']]:
                    if isinstance(check, unicode):
                        c = check.replace("-", "_")
                        if ctx.params[c] is None:
                            logger.get_my_logger("Utils").critical("The option '--" + check + "' is required");
                    elif isinstance(check, list):
                        # At least one parameter in the list should be informed
                        find = False
                        for c in check:
                            c = c.replace("-", "_")
                            if c in ctx.params and ctx.params[c] is not None:
                                find = True
                                break
                        if find:
                            continue
                        logger.get_my_logger("Utils").critical("One of those parameters should be included: " + ', '.join(map(str, check)))
                    else:
                        logger.get_my_logger("Utils").critical("Invalid cli conf file in: " + check)

