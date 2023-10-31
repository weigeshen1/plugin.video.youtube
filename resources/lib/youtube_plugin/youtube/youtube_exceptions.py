# -*- coding: utf-8 -*-
"""

    Copyright (C) 2014-2016 bromix (plugin.video.youtube)
    Copyright (C) 2016-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

from ..kodion import KodionException


class LoginException(KodionException):
    pass


class YouTubeException(KodionException):
    pass


class InvalidGrant(KodionException):
    pass
