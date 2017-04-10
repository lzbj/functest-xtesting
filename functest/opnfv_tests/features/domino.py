#!/usr/bin/python
#
# Copyright (c) 2015 All rights reserved
# This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# 0.1: This script boots the VM1 and allocates IP address from Nova
# Later, the VM2 boots then execute cloud-init to ping VM1.
# After successful ping, both the VMs are deleted.
# 0.2: measure test duration and publish results under json format
# 0.3: add report flag to push results when needed
# 0.4: refactoring to match Test abstraction class

import functest.core.feature as base
from functest.utils.constants import CONST


class Domino(base.BashFeature):
    def __init__(self, **kwargs):
        repo = CONST.__getattribute__('dir_repo_domino')
        kwargs["cmd"] = 'cd %s && ./tests/run_multinode.sh' % repo
        super(Domino, self).__init__(**kwargs)
