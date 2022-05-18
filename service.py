import sqlite3
from netaddr import *


def get_connect():

    conn = sqlite3.connect('test.db')
    return conn

# search the provider with the id
def search_provider_by_id(provider_id):

    conn = get_connect()
    print(provider_id)
    cur = conn.cursor()
    cur.execute("SELECT * FROM providers WHERE id = ?", (str(provider_id),))
    usuario = cur.fetchone()
    print(usuario)
    conn.close()
    return ("provider: " + usuario[5])

# search the provider with a given ip 
def search_provider_by_ip(ip):

    conn = get_connect()
    ip_number = verify_ip(ip)
    print(ip_number)
    iterator = conn.cursor()
    iterator.execute("select * from providers")

    if(ip_number != "other"):

        for provider in iterator.fetchall():

                ip_start = IPNetwork(provider[1])
                ip_end = IPNetwork(provider[2])
              
                if(ip_number[0] >= ip_start.value and ip_number[0] <= ip_end.value):
                    
                    print(provider[5])
                    
                    break
        conn.close()
        return ("provider: " + provider[5])
    else:
        conn.close() 
        return "You are entry a not valid IP address"
    
    
# verify what kinf of ip the user entry
def verify_ip(ip):

    response = []
    ipv4 = "ipv4"
    ipv6 = "ipv6"
    other = "other"
    ip_str = ip.split('.')

    if(len(ip_str) > 1):

        print(IPNetwork(ip).value)
        ip_str_number = IPNetwork(ip)
        response.append(ip_str_number.value)
        response.append(ipv4)
        return response

    else:
        
        ip_str = ip.split(':')
        if (len(ip_str) > 1):
            ip_str_number = IPNetwork(ip)
            response.append(ip_str_number.value)
            response.append(ipv6)
            return response
        else:
            return other
