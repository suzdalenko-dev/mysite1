from invoice.models.company import Company
from ..utils.json_suzdal import json_suzdal
from ..utils.time_suzdal import time_suzdal


def try_login(request):
    try:

        cif      = request.POST.get('cif').strip()
        email    = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        company = Company.objects.get(cif=cif, email=email)
        if company.password != password:
            return json_suzdal({'message': 'Company matching query does not exist 2', 'status': 'error'})
      
        company.lastvisit = time_suzdal()
        company.numvisit += 1
        company.save()

        rdata = {
            'id': company.id,
            'uid': company.uid,
            'status': 'ok',
        }

        res = json_suzdal(rdata)
        return res
    
    except Exception as e:
            return json_suzdal({'message': str(e),'status': 'error'})