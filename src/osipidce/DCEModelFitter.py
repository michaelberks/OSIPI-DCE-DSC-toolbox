'''
 mdm_DCEModelFitter.h
 Class that holds DCE time-series data and an asssociated tracer kinetic model
 More info...
 @author @michaelberks
'''

import numpy as np

class mdm_DCEModelFitter:
	''' 
	Holds DCE time-series data and an asssociated tracer kinetic model

	Attributes:
		BAD_FIT_SSD constant returned when fitting goes bad
	'''
	
	BAD_FIT_SSD = 1e6

	def __init__(
		self,
		model:DCEModelBase,
		timepoint0:int,
		timepointN:int,
		noiseVar:np.array,
		maxIterations:int = 0):
		''' 
		Constructor
		\param model tracer-kinetic model applied to voxel
		\param timepoint0 first timepoint used in model fit 
		\param timepointN last timepoint used in model fit 
		\param noiseVar temporal-varying noise (if empty,ant noise=1 used)
		\param maxIterations number of iterations to use in fit (if 0, fit to convergence)
		'''
		pass

	def  initialiseModelFit(self, CtData:TimeSeries):
		''' 
		Compute modelled C(t) at initial model parameters
		\param CtData contrast-agent concentration time-series
		'''
		pass

	
	def fitModel(self, status:DCEVoxelStatus):
		''' 
		Optimise tracer-kinetic model fit to concentration time-series
		\param status validity staus of voxel to fit
		'''
		pass

	@property
	def timepoint0(self)->int:
		''' 
		Return first timepoint used in computing model fit
		\return first timepoint used in computing model fit
		'''
		pass

	@property
	def timepointN(self)->int:
		''' 
		Return first timepoint used in computing model fit
		\return first timepoint used in computing model fit
		'''
		pass
  
	@property
	def CtModel(self)->TimeSeries:
		''' Return signal-derived contrast-agent concentration time-series
		\return model-estimated contrast-agent concentration time-series
		'''
		pass
	
	
	def modelFitError()->float:
		''' Return model fit error (sum of squared residuals)
		\return fit error
		\see BAD_FIT_SSD
		'''
		pass


	#double CtSSD(const std::vector<double> &parameter_array):

  #double computeSSD(const std::vector<double> &CtModel):

	#static void CtSSDalglib(const alglib::real_1d_array &x, alglib::real_1d_array &func, void *context) {
	#	std::vector<double> params(x.getcontent(), x.getcontent() + x.length()):
	#	func[0] = static_cast<mdm_DCEModelFitter*>(context)->CtSSD(params):
	#}

	#void optimiseModel():

	#VARIABLES
  #mdm_DCEModelBase &model_:

  #size_t timepoint0_:
  #size_t timepointN_:
  #std::vector<double> noiseVar_:			//DCE time series vector of estimated noise variance for each temporal volume

	#double modelFitError_: //SSD error between catData (actual concentrations) and catModel (fitted concentrations)

  #std::vector<double>* CtData_:

	#Upper an lower bounds to use with optimiser
	#alglib::real_1d_array lowerBoundsOpt_:
	#alglib::real_1d_array upperBoundsOpt_:

	#Maximum number of iterations applied
	#int maxIterations_:

  #double  '''< Value returned for SSD for failed model fits
