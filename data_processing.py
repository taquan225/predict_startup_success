from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('MTMzYjVkOGU5ZDY4OWZhZThiOTU1ZTAyMzhmY2VmZGI6MWFlMDgzMDA0ZmIyOTczNTEwMjhiZTA2MzNkZjI3ZjM=')
intrinio.ApiClient().allow_retries(True)

ticker = ''
status = ''
start_date = ''
end_date = ''
offer_amount_greater_than = ''
offer_amount_less_than = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_company_ipos(ticker=ticker, status=status, start_date=start_date, end_date=end_date, offer_amount_greater_than=offer_amount_greater_than, offer_amount_less_than=offer_amount_less_than, page_size=page_size, next_page=next_page)
print(response)