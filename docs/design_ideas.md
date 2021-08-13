# OSIPI-DCE-DSC-Toolbox design

## General design ideas

The overall toolbox will be designed with the following elements:

1. The low-level library

2. Methods: these will be standalone python functions that utilise the low-level library to provide standard DCE functionality.

### Low-level library

This will be OO python, with lexicon concepts mapped to classes, and functionality mapped to class methods. General users do not need to know about the details of the library (though it will of course be well documented!), but contributors will need to understand the structure and conventions we've used.

OO inheritence will be used to provide standard interfaces for abstract concepts. 

Example 1: We will probably have an abstract DCE-MRI tracer-kinetic model class (*eg* `DCE_TK_Model`) that prescribes methods for setting model parameters (and their bounds), computing modelled C(t), checking fitted parameter validity *etc*. Specific sub-classes of `DCE_TK_Model` then implement (*ie* define) their own instance of these methods. So we may have a class `DCE_TK_Model_ETM` that implements the extended-Tofts model.

Example 2: We probably want a DCE_TimeSeries (or DCE_Voxel?) class that holds a signal time-series (S(t)) and has a method for converting between signal and contrast-agent concentration (C(t)). In most DCE-MRI applications we will use a concrete sub-class DCE_TimeSeries_SPGR (indeed this may be all we implement), but this leaves open the possibility for defining other more complex signal protocols. 

### OSIPI methods

The methods provide a mid-level between the low-level library and full data analysis pipelines. They allow you to do *eg*

> from osipi.dce.methods import fit_T1

They can be used by
+ OSIPI developers in the pipelines we provide (see below)
+ OSIPI users to write their own pipelines
+ OSIPI users for experimental/interactive analysis (eg Monte-Carlo simulations)

The main data inputs should duck-type standard numpy array inputs as well as our library classes, so that OSIPI users don't necessarily need detailed knowledge of the library to run the methods.

Flexibility/modularity is provided by using the inheritence structure of the underlying library and the [template method](https://en.wikipedia.org/wiki/Template_method_pattern) together with user options specifying what "flavour" they want to run.

Sensible candidates for methods might be:

+ Fitting baseline T1

+ Converting between contrast-agent concentration and signal time-series

+ Estimating bolus arrival time

+ Fitting a tracer-kinetic model to signal/concentration time-series

Example: Consider a method for converting signal to concentration. This might have a definition like:

> def signal_to_concentration(S_t, T_1, M_0, method='SPGR', **kwargs)

Here the signal time-series S_t can be input as a generic (N_samples x N_timepoints) numpy array, or as an object of our DCE_Voxel class (or sub-classes).

With the default method set to 'SPGR', a basic usage might be (using kwargs)

> signal_to_concentration(S_t, T_1, M_0, FA=FA, TR=TR, r1=r1)

In which case we use the input to construct a structure of DCE_TimeSeries_SPGR objects, on which we call their signal to concentration method, and then return C(t) from the main method.

But this is very easily extendable to other acquisition protocols. Imagine we have a factory, that takes as input the method string (default 'SPGR') and returns the correct subclass of DCE_TimeSeries.
So out signal-concentration method
1. Call the Time-Series factory to return us the correct sub-class of DCE_TimeSeries objects, initialised with the user supplied inputs
2. Call the objects own signal-to-concentration method

Then nothing needs to change in the main signal_to_concentration method when we add a new TimeSeries class - all we need to do is update our factory (note any additional parameters it needs are covered by **kwargs).

The same principal applies to *eg*, different methods of fitting baseline T1 (VFA, IR *etc*), or fitting different tracer-kinetic models.

### OSIPI pipelines

Pipelines fit together methods into complete analyses, and also manage data I/O to read in input images and output parameter maps, summary statistics etc.

In this way they differ from methods, that work with data structures already existing in python memory.

They are managed by 


### OSIPI tools

