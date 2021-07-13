'''
Class that holds DCE time-series data and an asssociated tracer kinetic model
More info...
@author @michaelberks
'''

#Standard imports
from __future__ import annotations
from enum import Enum

#OSIPI imports
import DCEModelBase
from ErrorTracker import ErrorType

TimeSeries = list[float]



class DCEVoxel:
  ''' 
  Holds DCE time-series data and an asssociated tracer kinetic model

  Attributes:
  Some limits and error values when computing dynamic T1 and hence concentrations
  '''
  Ca_BAD1 = 1e6
  Ca_BAD2 = 1e6
  T1_TOLERANCE = 1e6
  DYN_T1_MAX = 1e6
  DYN_T1_INVALID = 1e6

  class DCEVoxelStatus(Enum):
    ''' Enum of current voxel error status
  
    '''
    OK = 0 #DCEVoxelStatus
    DYN_T1_BAD = 1 # Dynamic T1 invalid at one or more timepoints
    CA_NAN = 2 # NaNs found in signal-derived concentration
    T10_BAD = 3 # Baseline T1 is invalid
    M0_BAD = 4 # Baseline M0 is invalid
    NON_ENHANCING = 5 # No CA uptake
  
  def __init__(self,
    dynSignals:TimeSeries,
    dynConc:TimeSeries,
    injectionImg:int,
    dynamicTimings:TimeSeries,
    IAUCTimes:'list[float]',
    IAUCAtPeak:bool):
    ''' Constructor
    
    \param dynSignals time-series of dynamic signals (if empty, requires dynConc)
    \param dynConc time-series of signal-derived concentration (if empty, computed from dynSignals)
    \param injectionImg timepoint bolus injected
    \param dynamicTimings time in minutes of each series timepoint
    \param IAUCTimes times at which compute IAUC
    \param IAUCAtPeak flag to compute IAUC at peak signal
    '''
    pass

  
  def computeCtFromSignal(self,
    T1:float, FA:float, TR:float, r1Const:float,
    M0:float, B1:float = 1.0, timepoint0:int = 0):
    ''' 
    Convert signal time-series to contrast agent concentration
    
    \param T1 baseline T1 
    \param FA flip-angle in degrees
    \param TR repetition in ms
    \param r1Const relaxivity constant of contrast-agent
    \param M0 baseline magnetisation constant
    \param timepoint0 first time-point to use in pre-bolus noise estimation (default 0)
    \param B1 B1 correction factor
    '''
    pass

  
  def computeIAUC(self):
    ''' 
    Compute IAUC values at selected times
    '''
    pass

  @property
  def status(self)->DCEVoxelStatus:
    ''' Return the current error status
    '''
    pass

  @property
  def StData()->TimeSeries:
    ''' Return signal time-series
    '''
    pass

  @property
  def CtData()->TimeSeries:
    ''' Return signal-derived contrast-agent concentration time-series
    '''
    pass
  
  @property
  def IAUC_values()->'list[float]':
    ''' Return IAUC values
    '''
    pass

  @property
  def IAUC_times()->'list[float]':
    ''' Return IAUC times
    '''
    pass
  
  @property
  def enhancing()->bool:
    ''' Return enhancing status, true if voxel is enhancing OR testEnhancement is set false
    \see testEnhancing()
    '''
    pass

  def testEnhancing():
    ''' Test to see if voxel is enhancing, sets internal enhancing flag
    '''


#METHODS

  def _computeT1DynPBM(st:float, s_pbm:float, 
    T1:float, cosFA:float, sinFA:float, TR:float)->tuple[float,ErrorType]:
    pass

  def _computeT1DynM0(st:float, M0:float, 
    cosFA:float, sinFA:float, TR:float)->tuple[float,ErrorType]:
    pass

  def _computeIAUC(times:list[float], computePeak:bool)->list[float]:
    pass

  #VARIABLES

  #mdm_DCEVoxelStatus _status;

  #std::vector<double> _StData;		//DCE time series vector of signals
  #std::vector<double> _CtData;				//DCE time series vector of signal-derived concentrations
  
  
  #size_t _injectionImg;    //Time point of injection
  #std::vector<double> _IAUCTimes; //Vector of times (in secs) at which to caclucate IAUC values
  #std::vector<double> _IAUCVals; 
  #bool _IAUCAtPeak;
  
  #bool _enhancing; //Flag if the voxel enhanced

  #Reference to dynamic times, set at initialization from global volume analysis
  #const std::vector<double> _dynamicTimings;
