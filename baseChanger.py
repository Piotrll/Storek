import tkinter as tk
from tkinter import ttk
import queryHandle as qh
import classLib as cl
"""def loadBase(event, ):
    selectedBase = event.widget.get()
    selectedBaseQ = "use " + selectedBase+";"
    qh.queryMPKDB(selectedBaseQ)
    baseData = cl.Base
    baseData.data = qh.queryMPKDB("select * from storage;")
    baseData.columns = qh.queryMPKDB("show fields from storage;")
    return baseData

def initBase():
    storageStatus = qh.queryMPKDB("select * from storage;")
    storageFields = qh.queryMPKDB("show fields from storage;")
    baseData = cl.Base()
    baseData.data = storageStatus
    baseData.columns = storageFields
    return baseData"""