# -*- coding: utf-8 -*-
class ApiErrorCodeException(Exception):
    """Exception returning code and explanation given in api description for errorCode (like unknown or wrong ean code)"""
    def __init__(self, code, message):
        self.code = code
        self.message  = message
    
    def __str__(self):
        #TODO fix encoding for example put in wrong ean format
        return self.code + ":  " + self.message

class UnknownApiStatusCode(Exception):
    """Api returned status code not recognized by library"""
    def __str__(self):
        return "OpenEAN Api returned an error code that's not recognized"

class RequestStatus:
    def __init__(self):
        self.statuscodes = {
            0: ["OK", "Operation war erfolgreich"],
            1: ["not found", "die EAN konnte nicht gefunden werden"],
            2: ["checksum", "die EAN war fehlerhaft (Checksummenfehler)"],
            3: ["EAN-format", "die EAN war fehlerhaft (ungültiges Format / fehlerhafte Ziffernanzahl)"],
            4: ["not a global, unique EAN", "es wurde eine für interne Anwendungen reservierte EAN eingegeben (In-Store, Coupon etc.)"],
            5: ["access limit exceeded", "Zugriffslimit auf die Datenbank wurde überschritten"],
            6: ["no product name", "es wurde kein Produktname angegeben"],
            7: ["product name too long", "der Produktname ist zu lang (max. 20 Zeichen)"],
            8: ["no or wrong main category id", "die Nummer für die Hauptkategorie fehlt oder liegt außerhalb des erlaubten Bereiches"],
            9: ["no or wrong sub category id", "die Nummer für die zugehörige Unterkategorie fehlt oder liegt außerhalb des erlaubten Bereiches"],
            10: ["illegal data in vendor field", "unerlaubte Daten im Herstellerfeld"],
            11: ["illegal data in description field", "unerlaubte Daten im Beschreibungsfeld"],
            12: ["data already submitted", "Daten wurden bereits übertragen"],
            13: ["queryid missing or wrong", "die UserID/queryid fehlt in der Abfrage oder ist für diese Funktion nicht freigeschaltet"],
            14: ["unknown command", "es wurde mit dem Parameter 'cmd' ein unbekanntes Kommando übergeben"]
        }

    def checkStatus(self, code):
        if code != 0:
            result = self.statuscodes.get(code)
            if result == None:
                raise UnknownApiStatusCode()
            else:
                raise ApiErrorCodeException(result[0], result[1]) 

