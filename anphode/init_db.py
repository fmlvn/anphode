#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import create_app
from db import db


app = create_app()
app.app_context().push()
db.create_all(app=app)
