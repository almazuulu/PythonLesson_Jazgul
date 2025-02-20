# help() - показывает документацию какой-то функции

print(help(print))
print(help(input))
print(help(sorted))

# Однострочная документация
def say_hello(name):
    """Function that helps printout the name it accepts"""
    print(f"Hello {name}")

print(help(say_hello))


# Многострочная документация
def calc_avg(nums: int) -> float:
    """ 
    Function that helps to find avg number out of the list
    
    Args:
        nums (list[int]): List of integer numbers that can be used to find average number
        
    Returns:
        avg_num(float): Float average number that's found after calculation was made
        
    Raises:
        ValueError: If list is empty
    """
    if not nums:
        raise ValueError("List cannot be empty!")
    
    avg_num = sum(nums) / len(nums)
    return avg_num

print(help(calc_avg))


# Docstring styles

# Google docstring styles
def fetch_data(url: str, timeout: int=30) -> dict[str, str]:
    """ 
    Accepts data from requested url
    
    Args:
        url: String of url address that can be used to fetch the data
        timeout: Timeout in secs, by default is 30
    
    Returns:
        dict: Returns data in JSON Format
        
    Raises:
        ConnectionError: In case of Network Error
        TimeoutError: In case of timeout exceeds the limit
    """
    pass


# NumPy/ SciPy Style

def calculate_statistics(data):
    """ 
    Calculates basic static data
    
    
    Parameters
    ----------
    data: array_like
        Array with integer nums
    
    Returns
    -------
    mean: float
        Average value
    std: float
        Standard deviation
    
    See also
    --------
    numpy.mean, numpy.std
    
    Examples
    -------
    >>> stats = calculate_statistics([1, 2, 3, 4, 5])
    >>> print(stats)
    (3.0, 1.41)
    """

# reST Style - restructurec text

def process_image(image_path, size=[100,100]):
    """ 
    Function that process images
    
    :param image_path: path to the image from the source
    :type image_path: str
    :param size: size of the image
    :type size: tuple
    :returns: processed images
    :rtype: PIL.Image
    :raises: IOError: if file not found
    
    .. note:: Functions supports images in JPG and PNG Formats 
    """
    pass




