from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('frontPage', __name__)

@app.route('/')
def home():
        return render_template('FrontPage.html', title="Home", data=getTestName())

def getTestName():
        conn = None
        testData = None
        try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute('SELECT * FROM public.user_account WHERE id = 1')
                testData = cur.fetchone() # Fetches a single row from the database
                cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        finally:
                if conn is not None:
                        conn.close()
                return testData
