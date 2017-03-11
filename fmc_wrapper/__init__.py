"""
Firepower Management Center API wrapper for managing Firepower Threat Defense and legacy Firepower devices through a Firepower Management Center

http://www.cisco.com/c/en/us/td/docs/security/firepower/610/api/REST/Firepower_REST_API_Quick_Start_Guide/Objects_in_the_REST_API.html

Currently tested against FMC v6.2.0
"""

__all__ = []

def export(defn):
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn
from . import SecurityZone
from . import NetworkObject
