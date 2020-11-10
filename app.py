__author__ = "Asiri Amal"
__copyright__ = 'Copyright 2020, Asiri Amal'
__credits__ = ['Asiri']
__license__ = 'Asiri Amal service'
__version__ = 'V.0.0.3'
__maintainer__ = 'Asiri Amal'
__email__ = 'asiri.15@cse.mrt.ac.lk'
__status__ = 'development'
__date__ = '10/11/2020'

# Imports

from flask import Flask
from flask import  render_template
from flask import request
from controller.service import service_topics, service_desc, service_icon
from controller.portfolio import portfolio_topics, portfolio_image, portfolio_desc, portfolio_link

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html',
                           service_topics=service_topics,
                           service_desc=service_desc,
                           service_icon=service_icon,

                           portfolio_topics=portfolio_topics,
                           portfolio_image=portfolio_image,
                           portfolio_desc=portfolio_desc,
                           portfolio_link=portfolio_link)


@app.route('/test')
def test():
    return render_template('/test/test.html')


if __name__ == '__main__':
    app.run(debug=True)
