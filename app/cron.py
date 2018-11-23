from app.models import Domain
import whois

def execute_cron():
    #verify_domain()
    check_domain_validity()
    pass

def check_domain_validity():
    domain_to_verify = Domain.query()
    if application.config['WHOIS_ORG_RE'] != '':
        org_re = re.compile(application.config['WHOIS_ORG_RE']) 
        for d in domain_to_verify:
            w = whois.whois(d.domain)
            if not w['org']:
                print('We need to remove the domain')
                # remove the domain and send email
                pass 
            else:
                if not org.re.match(d.domain):
                    print('The domain no longer belong to us')
                    pass
         
