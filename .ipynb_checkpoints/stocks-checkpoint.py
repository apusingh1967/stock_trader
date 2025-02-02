import quandl;
import numpy as np;
import matplotlib.pyplot as plt;


amzn = quandl.get("WIKI/AMZN", start_date="2017-01-01", end_date="2018-01-01");
amzn.head();


