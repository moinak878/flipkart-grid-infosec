import vt
from apiKey import apiKey

# use the session here

client = vt.Client(apiKey)

# analysis = client.scan_url_async('').to_dict()
analysis = client.scan_url('51.83.254.3', wait_for_completion=True)
result =  analysis.to_dict()
print(result['attributes']['stats'])

client.close()

# urls_to_scan = ['https://www.google.com/', 'https://www.virustotal.com/', 'https://github.com/']
# futures = [client.scan_url_async(u) for u in urls_to_scan]
# # do some other work here
# for f in futures:
#   result = await f
#   print(result.to_dict())



# import vt
# import os
# import asyncio
# import nest_asyncio
# nest_asyncio.apply()

# async def hello(user_input):
#     client = vt.Client(os.environ.get('VIRUS_TOTAL_API_KEY'))
#     analysis = client.scan_url(user_input, wait_for_completion=True)
#     result =  analysis.to_dict()
#     client.close()
#     return result['attributes']['results']

# async def main():
#     print("Started ...")
#     json_data = await asyncio.create_task(hello('https://www.indiatoday.in/coronavirus-outbreak/story/chinese-president-xi-jinping-offers-help-to-india-in-fight-against-covid-19-1796738-2021-04-30'))
#     print(json_data)
#     print("Finished ...")

# asyncio.run(main())