# Day 3 — Flask + PostgreSQL

## Goal

Connect a Flask application to PostgreSQL and build database-backed API endpoints.

---

## Architecture

```text
Client / Postman
       ↓
    Flask API
       ↓
   database.py
       ↓
     psycopg
       ↓
   PostgreSQL
       ↓
   student_db
       ↓
   students