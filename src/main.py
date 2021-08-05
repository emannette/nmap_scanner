import argparse
import logging.config


def instantiate_logger() -> None:
    log_file = 'src/lib/configs/logging.conf'
    logging.config.fileConfig(log_file)
instantiate_logger()
logger = logging.getLogger('main')

def get_args() -> argparse.Namespace:
    logger.info("Gathering arguments.")
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='host_file', type=str,
                        help='The file containing the hosts to scan.')
    parser.add_argument('-s', '--servers', dest='server_list', type=str,
                        help='A string containing the hosts to scan.')
    nmap_args = parser.add_argument_group('NMAP')
    nmap_args.add_argument('-na', '--nmap-args', dest='nmap_args', type=str,
                           help='A comma separated string of arguments to pass to nmap.')
    nmap_args.add_argument('-p', '--ports', dest='scan_ports', type=str,
                           help='A comma separated list of ports to be scanned by nmap.')
    return parser.parse_args()

def create_scan_hosts():
    pass

if __name__ == '__main__':
    logger.info("Beginning execution.")
    cl_args = get_args()