"""
   Service Section
"""

__author__ = "Asiri Amal"
__copyright__ = 'Copyright 2020, Asiri Amal'
__credits__ = ['Asiri']
__license__ = 'Asiri Amal service'
__version__ = 'V.0.0.3'
__maintainer__ = 'Asiri Amal'
__email__ = 'asiri.15@cse.mrt.ac.lk'
__status__ = 'development'
__date__ = '10/11/2020'

service_dict = {
    "Web Design": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'paint-brush'],
    "Web Development": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'code'],
    "Responsive Design": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'cut'],
    "Edit Sections": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'object-ungroup'],
    "Data Bases": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'database'],
    "Android": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'android'],
}
service_topics = service_dict.keys()
service_desc = []
service_icon = []

for topic in service_topics:
    service_desc.append(service_dict[topic][0])
    service_icon.append(service_dict[topic][1])
