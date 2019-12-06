#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:12:03 2019

@author: ep9k
"""

import psycopg2


try:
    connection = psycopg2.connect(user = "postgres",                
    #psycopg2.connect() creates connection to PostgreSQL database instance
                              password = "battlebot",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "BRE_2019")

    cursor = connection.cursor()                                #creates a cursor object which allows us to execute PostgreSQL commands through python source

    cursor.execute('SELECT * FROM "AllKeeperAddresses_2019" ;')           #Executes a database operation or query. Execute method takes SQL query as a parameter. Returns list of result
    record = cursor.fetchall()

    print(record)


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL: ", error)
