'''
Class that records error codes for each voxel through the DCE modelling process
More info...
@author @michaelberks
'''

#Standard imports
from __future__ import annotations
from enum import Enum

#OSIPI imports
import Image3D

class mdm_ErrorTracker:
  '''
  Records error codes for each voxel through the DCE modelling process
  '''

  class ErrorCode(Enum):
    ''' Enum of defined error codes in T1 mapping and tracer-kinetic model fitting
  
    Each code uses a bit in a 32-bit integer, so that codes maybe added (bit-wise) and indiviudal
    codes recovered from the final aggergate code
    '''
    OK = 0										# No error condition                      - Binary no bits set
    VFA_THRESH_FAIL = 1			  # SigInt(FA = 2deg) < UserSetThreshold    - Binary bit 1 set  
    T1_INIT_FAIL = 2					# Initialisation of T1 fitting failed     - Binary bit 2 set  
    T1_FIT_FAIL = 4					  # Error in main T1 calculation routine    - Binary bit 3 set  
    T1_MAX_ITER = 8					  # Hit max iterations in T1 calculation    - Binary bit 4 set  
    T1_MAD_VALUE = 16				  # (T1 < 0.0) || (T1 > 6000.0)             - Binary bit 5 set  
    M0_NEGATIVE = 32					# Earlier error condition caused M0 = 0.0 - Binary bit 6 set 
    NON_ENH_IAUC = 64				  # Voxel non-enhancing by IAUC60 < 0.0     - Binary bit 7 set  
    CA_IS_NAN = 128					  # [CA](t) == NaN                          - Binary bit 8 set 
    DYNT1_NEGATIVE = 256			# T1(t) < 0.0                             - Binary bit 9 set 
    DCE_INVALID_INPUT = 512	  # Input value NaN or -ve                  - Binary bit 10 set 
    DCE_FIT_FAIL = 1024			  # Error in model fitting optimisation     - Binary bit 11 set
    DCE_INVALID_PARAM = 2048	# Error in model fitting optimisation     - Binary bit 12 set
    B1_INVALID = 4096	        # B1 map correction value <= 0            - Binary bit 13 set
  
  def __init__(self):
    ''' Default constructor
  
    '''
    pass

  
  @property
  def errorImage(self)->Image3D:
    '''    
    Return the error image
    '''
    pass

  @errorImage.setter
  def errorImage(self, imgWithDims:Image3D):
    '''    Set error image
    
    Input image must be non-empty and of type mdm_Image3D#imageType#TYPE_ERRORMAP, otherwise
    the error image will not be set, and the function will return false.
    \param    imgWithDims   mdm_Image3D object, must have type mdm_Image3D#imageType#TYPE_ERRORMAP
    \see mdm_Image3D#imageType
    '''
    pass

  def initErrorImage(img:Image3D):
    '''    
    Initialise error image, copying dimensions from existing image
    \param    img   mdm_Image3D object with voxel and matrix dimensions to copy
    '''
    pass

  def resetErrorImage():
    '''    
    Reset error image to empty image
    '''
    pass

  def updateVoxel(voxelIndex:int, errCode:ErrorCode):
    '''    
    Update a voxel in the error image with the specified error code
    \param    voxelIndex  Integer image voxel index (from x, y, z co-ordinates), must be >=0 and 
    < errorImage_.numVoxels()
    \param    errCode     Integer error code
    \see ErrorCode
    '''
    pass

  def  maskSingleErrorCode(errCode:int)->Image3D:
    ''' 
    Return mask image where all voxels matching the given error code are set to 1
    \param errCode error code to match
    \return masked image as mdm_Image3D object
    '''
    pass

  
  def checkOrSetDimension(img:Image3D, msg:str):
    '''Check the image dimensions match, with option to set if no current reference dimensions
    /* If no other images set yet, this will
    - initialise the error tracker
    - in doing so, set the dimension for all subsequent images to be checked against
    Throws mdm_mismatched_image() exception if dimensions don't match
    \param img input image to check
    '''
    pass

  
  def checkDimension(img:Image3D, msg:str):
    '''Check the image dimensions match, with option to set if no current reference dimensions
    /*
    Throws mdm_mismatched_image() exception if dimensions don't match
    \param img input image to check
    '''
    pass

  
  def setVoxelSizeWarnOnly(flag:bool):
    ''' Set voxelSizeWarnOnly flag
    
    \param flag if true, loaded images with mismatched voxel sizes only generate a warning
    '''
    pass

  #Map to log images, also sets expected dimensions for all image input
  #Image3D errorImage_;

  #Only log warning instead of breaking error if voxel sizes don't match
  #bool voxelSizeWarnOnly_;