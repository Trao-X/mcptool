from mccolors import mcwrite
from loguru import logger

from ..managers.language_manager import LanguageManager as LM


class ValidateArgument:
    @logger.catch
    @staticmethod
    def validate_arguments_length(command_name: str, command_arguments: list, user_arguments: list) -> bool:
        """
        Method to validate the arguments length
        """

        logger.info(f'Validating arguments for command: {command_name} with arguments: {user_arguments}')

        for i in range(0, len(command_arguments)):
            try:
                user_arguments[i]

            except IndexError:
                error_message: str = LM().get(['commands', 'missingArguments'])
                arguments_message: str = ''

                for argument_valid in command_arguments[:i]:
                    arguments_message += f'&a{argument_valid} '

                for argument_invalid in command_arguments[i:]:
                    arguments_message += f'&c&n{argument_invalid}&r '

                # Add the name of the command
                error_message = error_message.replace('%command%', command_name)

                # Add th arguments
                error_message = error_message.replace('%arguments%', arguments_message)
                
                # Print the error message
                mcwrite(error_message)
                return False
        
        return True
    
    @logger.catch
    @staticmethod
    def is_domain(domain: str) -> bool:
        """
        Method to validate if a string is a domain
        """

        if domain.count('.') < 1:
            return False

        # Split the domain into parts
        domain_parts = domain.split('.')

        # Check if each part is alphanumeric
        for part in domain_parts:
            if not part.isalnum():
                return False

        return True
    
    @logger.catch 
    @staticmethod
    def is_ip_address(ip: str) -> bool:
        """
        Method to validate if a string is an IP address
        """

        logger.info(f'Validating if the string is an IP address: {ip}')
        ip_parts: list = ip.split('.')

        if len(ip_parts) != 4:
            return False

        for part in ip_parts:
            try:
                part: int = int(part)

                if part < 0 or part > 255:
                    return False
                
            except ValueError:
                return False

        return True
    
    @logger.catch
    @staticmethod
    def is_ip_and_port(ip: str) -> bool:
        """
        Method to validate if a string is an IP and port
        """

        logger.info(f'Validating if the string is an IP and port: {ip}')

        if ':' not in ip:
            return False

        ip_parts: list = ip.split(':')

        if len(ip_parts) != 2:
            return False

        ip_address: str = ip_parts[0]
        port: str = ip_parts[1]

        if not ip_address or not port:
            return False

        try:
            port: int = int(port)

            if port < 0 or port > 65535:
                return False
            
        except ValueError:
            return False

        ip_parts: list = ip_address.split('.')

        if len(ip_parts) != 4:
            return False

        for part in ip_parts:
            try:
                part: int = int(part)

                if part < 0 or part > 255:
                    return False
                
            except ValueError:
                return False

        return True
    
    @logger.catch
    @staticmethod
    def is_port_range_py_method(port_range: str) -> bool:
        """
        Method to validate if a string is a port range for the Python scanner
        """

        logger.info(f'Validating if the string is a port range for the Python scanner: {port_range}')

        if '-' not in port_range:
            if not port_range.isnumeric():
                return False
            
            if int(port_range) < 0 or int(port_range) > 65535:
                return False

            return True

        # Split the port range into start and end
        start, end = port_range.split('-')

        try:
            start: int = int(start)
            end: int = int(end)

            if start < 0 or start > 65535 or end < 0 or end > 65535:
                return False

            if start > end:
                return False
    
        except ValueError:
            return False

        return True

    @logger.catch
    @staticmethod
    def is_seeker_subcommand(subcommand: str) -> bool:
        """
        Method to validate if a string is a seeker subcommand
        """

        logger.info(f'Validating if the subcommand is a seeker subcommand: {subcommand}')

        if subcommand not in ['token', 'servers']:
            return False

        return True

    @logger.catch
    @staticmethod
    def is_scan_method(method: str) -> bool:
        """
        Method to validate if a string is a scan method
        """

        logger.info(f'Validating if the method is a scan method: {method}')

        if method not in ['nmap', 'qubo', 'masscan', 'py']:
            return False

        return True
    