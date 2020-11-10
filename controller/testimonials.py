"""
   testimonial Section
"""

__author__ = "Asiri Amal"
__copyright__ = 'Copyright 2020, Asiri Amal'
__credits__ = ['Asiri']
__license__ = 'Asiri Amal testimonial'
__version__ = 'V.0.0.3'
__maintainer__ = 'Asiri Amal'
__email__ = 'asiri.15@cse.mrt.ac.lk'
__status__ = 'development'
__date__ = '10/11/2020'

testimonial_dict = {
    "Lisa Redfern": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'lisa_redfern.jpg',
        "5"],
    "Cassi": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'cassi.jpg',
        "5"],
    "Md Nahidul": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
        'md_nahidul.jpg',
        "4"],
    "Alex": [
        "Easy communication and back-and-forth conversations on requirements and getting the project started. Great follow ups and no problem revisions on the initial design as well to get to exactly what I had in mind.",
        'alex.jpg',
        "4"],
}

client_names = testimonial_dict.keys()
client_feedback = []
client_image = []
client_rating = []

for name in client_names:
    client_feedback.append(testimonial_dict[name][0])
    client_image.append(testimonial_dict[name][1])
    client_rating.append(testimonial_dict[name][2])
