#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Integer, String
from sqlalchemy.sql import select, text, bindparam, exists, func, and_, or_, not_

engine = create_engine("postgresql://postgres:password@db:5433/term_data")
conn = engine.connect()
print(conn)
