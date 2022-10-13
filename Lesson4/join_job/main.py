import html_creater as hc
import xml_generator as xg
import data_provider as dp
import logger as log

# print(hc.create())
# print(xg.create())
data = dp.data_collection()
hc.new_create(xg.new_create(data))
log.data_collection(data)