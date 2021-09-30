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
        "Attractive UI and UX designs with conceptualizing, create, develop, and maintain visually appealing, user-friendly websites and interactive applications for any kind of business you have. (AdobeXD, PSD to HTML)",
        'paint-brush'],
    "Front End Development": [
        "Build, service, and maintain visually appealing and user-friendly websites. Not only work across a broad range of projects and technical disciplines but also liaise closely with clients to find out their exact needs, this in turn allows them to build a site that meets a customer's exact requirements. (HTML, CSS, JS, ReactJS, VueJS)",
        'object-group'],
    "Back End Development": [
        "Responsible for creating and maintaining technology at the back end of a website (the server, database, and application). Python3 Flask and Django Frameworks with a Version control system with GIT and knowledge of SOAP and REST web services",
        'code'],
    "Machine Learning and AI": [
        "Create machine learning models and retraining systems for AI applications. Expertise in statistics, programming, data science, and software engineering. (Deep Learning, Neural Networks, Modeling, Tensorflow, OpenCV)",
        'brain'],
    "Data Bases": [
        "Write new database programs and maintain existing programs to ensure they can handle the flow of traffic and the amount of data being stored in the database. With both SQL and NoSQL databases (PostgreSQL, MySQL, Redis, MongoDB)",
        'database'],
    "Web Scraping": [
        "Web scraping and data mining through given website. It will be an anonimous scraping using multiple proxies. No longer user needs to do the same task again and again with the scraper. (BeatifulSoup, Selenium, Scrapy)",
        'scroll'],
}
service_topics = service_dict.keys()
service_desc = []
service_icon = []

for topic in service_topics:
    service_desc.append(service_dict[topic][0])
    service_icon.append(service_dict[topic][1])
