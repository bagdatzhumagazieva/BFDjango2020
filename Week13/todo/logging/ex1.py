import logging

logging .basicConfig(
    level=logging.DEBUG,
    filename='example1.log',
    filemode='a',
    format=''
)


test_message = 'Someone'

logging.debug(f'debug message show: {test_message}')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')