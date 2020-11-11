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

from flask import Markup

portfolio_dict = {
    Markup("AI for Car Insurance <br>-Django-"): [
        "Unique and specialized quote for you. According to your input data and AI will analyse your input with trained models and return one of the most accurate insurance quotes",
        'ai_car.png',
        "https://aifocarinsurance.herokuapp.com/"],
    Markup("Covid-19 Interactive Dashboard <br>-Flask-"): [
        "Expert AI-driven forecasts across 4716 time series including economics, equities markets, technology trends, elections, and public health. An integrated and fully connected knowledge graph powers the engine to forecast better than seen anywhere before.",
        'covid_dashboard.png',
        "https://dashflaskgraph.herokuapp.com/"],
    "OpenCV Object detection Image Processing with OCR": [
        "Detect comic speech bubble boxes accurately and draw a box around that. Computer Vision (OpenCV), Python3 algorithms with image processing. Three versions have been created with py tesseract, OCR-Space and, image segmentation",
        'ocr.png',
        "https://github.com/AsiriAmalk/Comic_Speech_Bubble_Identifier_Using_OcrSpace"],
    "Scrappers": [
        "Yahoo finance scrapper with automatic with cookies. This scrape specific sections in the Yahoo finance site with rotating proxies to avoid getting banned. The dashboard is built from Django and, a notification will send to the discord webhook.",
        'scrapper.png',
        "https://github.com/AsiriAmalk/full_stock"],
    "Artificial Intelligence": [
        "Deep reinforcement learning Ongoing Research and Development (R&D) to reduce the time spent on optimizing the circuit locations in Printed Circuit Boards(PCB). This is a private repo.",
        'pcb.png',
        "https://github.com/AsiriAmalk"],
    "Machine Learning & Data Science": [
        "Predict the delay for each flight with past data with 55k+ records. This is a regression problem. Data Correlation analysis, Data Visualization, Test Train split. Clear documentation and coding.",
        'flight.png',
        "https://github.com/AsiriAmalk/Flight_Departure_Delay_Machine_Learning"],
}
portfolio_topics = portfolio_dict.keys()
portfolio_desc = []
portfolio_image = []
portfolio_link = []

for topic in portfolio_topics:
    portfolio_desc.append(portfolio_dict[topic][0])
    portfolio_image.append(portfolio_dict[topic][1])
    portfolio_link.append(portfolio_dict[topic][2])
