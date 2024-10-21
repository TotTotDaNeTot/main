import traceback
from crypt import methods
from inspect import trace
from keyword import kwlist
from typing import Optional

from pydantic import  BaseModel, EmailStr, ValidationError
from flask import Flask
from flask_restful import Api, Resource, reqparse
import pymysql, pymysql.cursors
from db import host, user, password, db_name

app = Flask(__name__)
api = Api()



connection = pymysql.connect(
        host=host,
        port=8889,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )



cinema = {

}

par = reqparse.RequestParser()
par.add_argument('movie', type=str, location='form')
par.add_argument('description', type=str, location='form')
par.add_argument('rating', type=float, location='form')
# cinema[] = par.parse_args()
# print(cinema)


class Main(Resource):


    def get(self, cor_id):
        # if cor_id == 0:
        #     return courses
        # else:
        #     return courses[cor_id]

        try:
            with connection.cursor() as cursor:
                if cor_id == 0:
                    rt = "SELECT * FROM cinema"
                    cursor.execute(rt)
                    r = cursor.fetchall()
                    return r
                else:
                    rt = ("SELECT * FROM cinema "
                          "WHERE id = {}").format(cor_id)
                    cursor.execute(rt)
                    r = cursor.fetchall()
                    return r

        finally:
            cursor.close()


    def delete(self, cor_id):
        # del courses[cor_id]
        # return courses

        try:
            with connection.cursor() as cursor:
                rt = "DELETE FROM cinema WHERE id = {}".format(cor_id)
                cursor.execute(rt)
                #r = cursor.fetchall()
                connection.commit()
                #return r
        except:
            traceback.print_exc()
            connection.rollback()

        finally:
            cursor.close()


    def post(self, cor_id):

        cinema[cor_id] = par.parse_args()
        # a = cinema[cor_id]['movie']
        # b = cinema[cor_id]['description']
        # c = cinema[cor_id]['rating']

        try:
            with connection.cursor() as cursor:

                # rt = ("INSERT INTO cinema(id, movie, description, rating) "
                #       "VALUES ({}, {}, {}, {})".format(cor_id, par, par, par))
                # rt = ("INSERT INTO cinema(id, movie, description, rating) "
                #       "VALUES (%s, %s, %s, %s)", (cor_id, 'qwe', 'dfv', 3.4))
                cursor.execute("INSERT INTO "
                      "cinema(id, movie, description, rating) "
                      "VALUES (%s, %s, %s, %s)",
                               (cor_id, cinema[cor_id]['movie'],
                                    cinema[cor_id]['description'],
                                    cinema[cor_id]['rating']))
                connection.commit()
                #app.id = cursor.lastrowid
                #return rt
        except:

            traceback.print_exc()
            connection.rollback()

        finally:
            cursor.close()

    def put(self, cor_id):
        cinema[cor_id] = par.parse_args()

        try:
            with connection.cursor() as cursor:
                # rt = ("UPDATE cinema SET movie = %s, "
                #       "description = %s,"
                #       " rating = %s WHERE id = %s", (cor_id,
                #                     cinema[cor_id]['movie'],
                #                     cinema[cor_id]['description'],
                #                     cinema[cor_id]['rating']))
                cursor.execute("UPDATE cinema SET movie = %s, "
                      "description = %s,"
                      " rating = %s WHERE id = %s", (
                                    cinema[cor_id]['movie'],
                                    cinema[cor_id]['description'],
                                    cinema[cor_id]['rating'], cor_id))
                connection.commit()
        finally:
            cursor.close()


# api.add_resource(Main, "/Applications/MAMP/htdocs/cinema/<int:cor_id>")
api.add_resource(Main, "/Applications/MAMP/htdocs/cinema/<int:cor_id>")
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8888, host='localhost')