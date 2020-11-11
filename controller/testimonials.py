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

from flask import Markup

testimonial_dict = {
    Markup(
        "Dr. Endre Palatinus<br> Machine Learning Engineer at Stats Perform<br>Graz, Styria, Austria"): [
        "Asiri is a great Django developer. He is able to quickly pick up new technology, and understand complex data engineering topics. I would recommend him for working in a team as well, as he understands how to work in a team using github on the same project pretty well.",
        "endre_palantinus.jpg",
        "5"
    ],
    Markup(
        "Dvir (大卫) Kenig<br>Co-Founder&CTO at ITC<br>B.Sc Electric&Computer engineering<br>Technical Chinese expert"): [
        "We are highly impressed from Mr.Asiri professionalism. Deliver the work perfectly within the scope of the allocated time. the output of his work is accurately according to the expectation. a pleasure to work with you Mr.Asiri, happy that you are part of our team.",
        "dvir_kenig.jpg",
        "5"
    ],
    "Alex": [
        "Easy communication and back-and-forth conversations on requirements and getting the project started. Great follow ups and no problem revisions on the initial design as well to get to exactly what I had in mind.",
        'alex.jpg',
        "4"],
    # "Shwanjaff":
    #     ["Great work great in time and good with price",
    #      "shwanjaff.png",
    #      "5"],
    # "Qiuziguo":
    #     ["Very good job, fast and effective.",
    #      "shwanjaff.png",
    #      "5"],
    "oroefe":
        [
            "Asiri was very helpful and was happy to amend the project based on further requirements. He goes above and beyond when further help is required. I’d recommend him to anyone that requires projects in data mining!",
            "no_image.png",
            "5"],
    "manish0521":
        [
            "He is so fast and accommodating. He delivered with in an hour. Great knowledge. Will definitely come back to him.",
            "no_image.png",
            "5"],
    # "sunjaynair":
    #     ["Great work",
    #      "no_image.png",
    #      "5"],
    "lwaribo":
        ["He is very knowledgeable, I will recommend for anyone who needs help with python related task.",
         "no_image.png",
         "5"],
    "abdulmelik226":
        [
            "I'm very satisfied. He was very helpful and always answered in a very short time. In addition, he takes much less time than I specified for the task. Gladly again",
            "no_image.png",
            "5"],
    # "casberns":
    #     ["Good work,",
    #      "no_image.png",
    #      "4.3"],
    "mlhshn":
        [
            "A professional developer who delivers quality in the shortest possible time. I am glad to have met you here and hope for further cooperation.",
            "no_image.png",
            "5"],
    "trislav":
        [
            "Somehow my expectations are exactly as he coded. Very concise codes, well thought out. This is my second order. Will definitely order more",
            "no_image.png",
            "5"],
    "dynas7y2":
        ["Second order. Again, complex project, good communication, delivered as expected.",
         "no_image.png",
         "5"],
    # "wuyongfeng":
    #     ["fast and excellent",
    #      "no_image.png",
    #      "5"],
    "rdonning":
        ["Excellent job, everything I needed and quicker than I thought. Would definitely use again",
         "no_image.png",
         "5"],
    # "saravanansmkkb":
    #     ["Great work by the seller. Easy to communicate with.",
    #      "no_image.png",
    #      "5"],
    "sehun94":
        [
            "He is very intuitive and did the job that I asked him to do perfectly. I would order again from him for sure. Thanks.",
            "no_image.png",
            "4.7"],
    # "rahuldwivedi853":
    #     ["Talented and professional!",
    #      "rahuldwivedi853.jpg",
    #      "5"],
    "kpalmab":
        [
            "Great results, exceeded my expectations and delivered before expected, good communicator, I would hire again!",
            "no_image.png",
            "5"],
    "tsv1979dk":
        ["Seller is easy to communicate with, perfect job done. Not last time i buy from this seller.",
         "no_image.png",
         "5"],
    "oshanaiddi":
        ["Got the best service. Highly recommended and he gives his best to achieve the targets.",
         "oshanaiddi.jpg",
         "5"],
    # "aharmsen":
    #     [
    #         "Easy communication and back-and-forth conversations on requirements and getting the project started. Great follow ups and no problem revisions on the initial design as well to get to exactly what I had in mind.",
    #         "aharmsen.jpg",
    #         "5"],

}

client_names = testimonial_dict.keys()
client_feedback = []
client_image = []
client_rating = []

for name in client_names:
    client_feedback.append(testimonial_dict[name][0])
    client_image.append(testimonial_dict[name][1])
    client_rating.append(testimonial_dict[name][2])
