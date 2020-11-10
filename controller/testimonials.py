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
portfolio_topics = portfolio_dict.keys()
portfolio_desc = []
portfolio_icon = []

for topic in portfolio_topics:
    portfolio_desc.append(portfolio_dict[topic][0])
    portfolio_icon.append(portfolio_dict[topic][1])
