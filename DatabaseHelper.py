import sys
import sqlite3

class DatabaseHelper:
    conn = object()
    
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)

    def GetAllDimesions(self):
        cursor = self.conn.cursor()
        cursor.execute("Select Designation FROM Angles")
        anglesDesignation = cursor.fetchall()
        cursor.execute("Select Designation FROM Beams")
        beamsDesignation = cursor.fetchall()
        cursor.execute("Select Designation FROM Channels")
        channelsDesignation = list(cursor.fetchall())
        allDesignations = set().union(anglesDesignation).union(beamsDesignation).union(channelsDesignation)
        return list(allDesignations)

    def GetAnglesDataForADesignation(self, designation):
        cursor = self.conn.cursor()
        cursor.execute("Select * FROM Angles WHERE Designation = ?", (designation,))
        row = cursor.fetchall()
        return row

    def GetBeamsDataForADesignation(self, designation):
        cursor = self.conn.cursor()
        cursor.execute("Select * FROM Beams WHERE Designation = ?", (designation,))
        row = cursor.fetchall()
        return row

    def GetChannelsDataForADesignation(self, designation):
        cursor = self.conn.cursor()
        cursor.execute("Select * FROM Channels WHERE Designation = ?", (designation,))
        row = cursor.fetchall()
        return row

    
