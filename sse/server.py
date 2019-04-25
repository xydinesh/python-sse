from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response
)

import time
from datetime import datetime

bp = Blueprint('sse', __name__)
subscriptions = []

# SSE "protocol" is described here: http://mzl.la/UPFyxY
class ServerSentEvent(object):
    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data : "data",
            self.event : "event",
            self.id : "id"
        }

    def encode(self):
        if not self.data:
            return ""
        lines = ["%s: %s" % (v, k) 
                 for k, v in self.desc_map.items() if k]
        return "%s\n\n" % "\n".join(lines)

@bp.route('/datetime')
def sse_datetime():
    sleep_time = int(request.args.get('sleep', '10'))
    def gen(n):
        while True:
            ev = ServerSentEvent(datetime.utcnow().isoformat())
            yield ev.encode()
            time.sleep(n)
    return Response(gen(sleep_time), mimetype="text/event-stream")
