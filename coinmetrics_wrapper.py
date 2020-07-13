#!/bin/python
#
# A Python wrapper for https://community-api.coinmetrics.io/v2/
#
#

import time
import yaml
import logging
import requests
import datetime
import pandas as pd

api_queries = 'coinmetrics_api_data.yaml'

with open(api_queries, 'r') as f:
    try:
        query_yaml = yaml.load(f)
        print(query_yaml)
    except yaml.YAMLError as e:
        logging.error(e)

API_ENDPOINT = query_yaml['api_endpoint']

def format_parameter(parameter):
    """ Format parameters for the query """
    if isinstance(parameter, list):
        return ','.join(parameter)
    else:
        return parameter


def get_url(query_name, **kwargs):
    """
    Get formatted url for a required query
    Pass the arguments to the query as keyword arguments
    """
    query_data = query_yaml[query_name]
    query_url = API_ENDPOINT + query_data['url']
    query_arguments = []
    # Check if all the required arguments are provided
    """
    if 'required' in query_data['parameters'].keys() and query_data['parameters']['required'] is not None and any(argument not in kwargs for argument in query_data['parameters']['required']):
        logging.info("Not all required arguments provided for {query}. "
                     "Required arguments are {args}.".format(query=query_name, args=query_data['parameters']['required']))
        return None
    else:
        possible_query_arguments = list(query_data.get('parameters', {}).get('required', {}).keys()) + list(query_data.get('parameters', {}).get('additional', {}).keys())
        for argument, value in kwargs.items():
            if argument in possible_query_arguments:
                query_arguments.append("{argument}={value}".format(argument=argument, value=format_parameter(value)))
    """
    #query = query_url + '?' + '&'.join(query_arguments)
    #print(query)
    return query_url


def query_coinmetrics(url):
    """ Query CryptoCoinmetrics API """
    try:
        response = requests.get(url).json()
        #print(response)
    except Exception as e:
        logging.error("Failure while querying {query}. \n{err}".format(query=url, err=e))
        return None

    if not response or 'Response' not in response.keys():
        return response

    if response['Response'] is 'Error':
        logging.error("Failed to query {url}".format(url=url))
        return None
    return response


def convert_timestamp(timestamp):
    """ Convert timestamp into readable datetime """
    try:
        #return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d-%m-%Y %H:%M')
        return timestamp
    except Exception as e:
        logging.debug(e)
        return None


def get_data(response):
    """ Separate query data from response """
    header = {key: (value if key != 'Data' else len(value)) for key, value in response.items()}
    data = response['Data']
    return header, data


def get_readable_df(response):
    """ Extract data from given response and return a dataframe """
    header, data = get_data(response)
    if data is None:
        return None
    try:
        df_data = pd.DataFrame(data)
        #print(df_data.columns)
        df_data = df_data.rename(columns={'time': 'unix_timestamp'})
        #df_data['time'] = df_data.timestamp.apply(convert_timestamp)
        if 'unix_timestamp' in df_data:
            df_data = df_data.set_index('unix_timestamp')
        else:
            return None
    except AttributeError as e:
        logging.debug(e)
        return None
    return df_data


def get_coin_list():
    """ Get asset list """
    data = query_coinmetrics(get_url('assets'))
    return data

# coins = get_coin_list()
# COIN_DB = pd.DataFrame.from_dict(coins, orient='index')
# print(COIN_DB.head())


def get_exchanges_list():
    """ Get a list of all exchanges on coinmetrics """
    data = query_coinmetrics(get_url('exchanges'))
    return data

# exchanges = get_exchanges_list()
# EXCHANGE_DB = pd.DataFrame.from_dict(e, orient='index')
# print(EXCHANGE_DB.head())

def get_markets_list():
    """ Get a list of all markets on coinmetrics """
    data = query_coinmetrics(get_url('markets'))
    return data

def get_metrics_list():
    """ Get a list of all metrics on coinmetrics """
    data = query_coinmetrics(get_url('metrics'))
    return data

def get_metrics_info_list():
    """ Get information of all metrics on coinmetrics """
    data = query_coinmetrics(get_url('metric_info'))
    return data
