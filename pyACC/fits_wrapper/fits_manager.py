import numpy as np
from astropy.io import fits
from ..helpers.logger import Logger


class FitsManager:
    """
    class to manage fits files
    """
    def __init__(self, file_path):
        " constructor of the class"
        self.file_path = file_path
        self.hdulist = fits.open(file_path)
        self.logger = Logger('FitsManager')
        self.logger("FITS file opened successfully")


    def get_hdu_count(self):
        """
        return the number of HDUs in the .fits file
        """

        return len(self.hdulist)
    

    def get_header(self, hdu_index):
        """
        Get header of a given HDU
        """

        if hdu_index < 0 or hdu_index >= self.get_hdu_count():
            self.logger.error("Invalid HDU index")


        return self.hdulist[hdu_index].header
    
    def get_data(self, hdu_index):
        """
        Get data of a given HDU
        """

        if hdu_index < 0 or hdu_index >= self.get_hdu_count():
            self.logger.error("Invalid HDU index")
        
        return self.hdulist[hdu_index].data