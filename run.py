#!/usr/bin/env python

import webtim

app_config = {
    'db_url': 'sqlite:////tmp/webtim.sqlite',
    'monitor_path': '/tmp/foo'
}
app = webtim.make_app(app_config)
app.run()
