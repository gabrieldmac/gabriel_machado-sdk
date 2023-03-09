# Guide

First, install your package and it's dependents:

pip install -i https://test.pypi.org/simple/ lotr-sdk-liblab-gdm
pip install requests
pip install python-dotenv

Second, import the package in your python file

from lotrsdk import lotrsdk

Third, use the APIs:

get_movies()

get_one_movie(movie_id)

get_quote_fom_movie(movie_id)

TIP: Find the movie id's using the get_movies function
