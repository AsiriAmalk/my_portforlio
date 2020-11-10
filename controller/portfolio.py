"""
   Portfolio Section
"""

__author__ = "Asiri Amal"
__copyright__ = 'Copyright 2020, Asiri Amal'
__credits__ = ['Asiri']
__license__ = 'Asiri Amal Portfolio'
__version__ = 'V.0.0.3'
__maintainer__ = 'Asiri Amal'
__email__ = 'asiri.15@cse.mrt.ac.lk'
__status__ = 'development'
__date__ = '10/11/2020'

portfolio_dict = {
    "Threads": [
        "illustration",
        '01-thumbnail.jpg',
        "https://github.com/asiriamalk"],
    "Explore": [
        "Graphic Design",
        '02-thumbnail.jpg',
        "https://github.com/asiriamalk"],
    "Finish": [
        "illustration",
        '03-thumbnail.jpg',
        "https://github.com/asiriamalk"],
    "Lines": [
        "illustration",
        '04-thumbnail.jpg',
        "https://github.com/asiriamalk"],
    "Southwest": [
        "illustration",
        '05-thumbnail.jpg',
        "https://github.com/asiriamalk"],
    "Window": [
        "illustration",
        '06-thumbnail.jpg',
        "https://github.com/asiriamalk"],
}
portfolio_topics = portfolio_dict.keys()
portfolio_desc = []
portfolio_image = []
portfolio_link = []

for topic in portfolio_topics:
    portfolio_desc.append(portfolio_dict[topic][0])
    portfolio_image.append(portfolio_dict[topic][1])
    portfolio_link.append(portfolio_dict[topic][2])
