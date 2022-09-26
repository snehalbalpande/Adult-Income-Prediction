from flask import Flask
import sys
from income_prediction.logger import logging
from income_prediction.exception import IncomeException

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        income_prediction = IncomeException(e,sys)
        logging.info(income_prediction.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)