import dns.exception
import requests
from concurrent.futures import ThreadPoolExecutor
import dns.resolver

#Definimos la funcion que tome los parametros subdomain y domain

def check_subdomain(subdomain, domain):
    url = f"http://{subdomain}.{domain}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            
            print(f"[-] subdominio encontrado con exito: {url}")
            
        else:
            
            print(f"[-] Subdominio no encontrado: {url} (Código de estado: {response.status_code})")
            
    except requests.ConnectionError:
        print(f"[-] Error de conexion: {url}")
        
#Funcion para enumerar los subdominios

def enumerate_subdomains(domain):
    
    subdomains = ['www', 'mail', 'ftp', 'test', 'dev', 'staging', 'blog', 'shop', 'api', 'admin']
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        
        for subdomain in subdomains:
            
            executor.submit(check_subdomain, subdomain, domain)

#Funcion para consultar DNS

def dns_enumeration(domain):
    
    try:
        
        answers = dns.resolver.resolve(domain, 'A')
        
        for rdata in answers:
            
            print(f"[+] Direccion IP encontrada: {rdata}")
    
    except dns.resolver.NoAnswer:
        print(f"[-] No se encontraron registros A A para {domain}")
        
    except dns.resolver.NXDOMAIN:
        print(f"[-] El dominio {domain} no existe")
    
    except dns.resolver.Timeout:
        print(f"[!] La consulta DNS para {domain} ha expirado")
    
    except dns.exception.DNSException as e:
        print(f"[!] Error en la consulta DNS: {e}")

domain = input("Ingrese el sitio que desee enumerar: ")
        
#Llamadas a las funciones

dns_enumeration(domain)
enumerate_subdomains(domain)
       
    
        
        
    
        
