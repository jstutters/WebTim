#!/usr/bin/env python

import scanbox

app_config = {
    'db_url': 'sqlite:////tmp/scanbox.sqlite',
    'monitor_path': '/tmp/foo'
}
app = scanbox.make_app(app_config)
app.run()
