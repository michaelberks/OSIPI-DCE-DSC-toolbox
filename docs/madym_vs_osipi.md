# Madym vs OSIPI

In designing a DCE/DSC library/toolkit for OSIPI, a natural starting place for @michaelberks is to convert the design of Madym (an open source C++ toolkit available [here](https://gitlab.com/manchester_qbi/manchester_qbi_public/madym_cxx)) into a python library. 

Whether this is a good idea or not depends on a few key questions:

+ How does the functionality in Madym match up to the pipeline specifications set out by [OSIPI taskforce 2.3](pipeline_specification)?

+ How well do the C++ design principals in Madym map to python?

+ Given this is a chance to start a library from fresh, are there 'old ways of thinking' embedded in Madym we're better off scrapping?

This docs adds some thoughts on these.

## Madym functionality vs OSIPI specification

The functionality expected of the OSIPI library is set out in the TF2.3 [pipeline specification document](pipeline_specification).

On the whole, Madym provides functionality that covers most of the pipeline specification (and adds some additional functionality). However there are also some important options missing from Madym.

### Key OSIPI specifications Madym meets

+ T1 mapping using variable flip-angles or inversion recovery, with design to make adding new mapping methods easy

+ AIF input using either a population AIF or a reference mask

+ A standard TK model voxel-wise fitting pipeline in which S(t) is converted to C(t), and PK parameters are optimised for a given tracer-kinetic model in a least-squares fit to C(t), with a design to make adding new TK models easy

### OSIPI specifications currently not available in Madym

+ Madym always fits models in C(t) space, and doesn't even implement C(t) to S(t), therefore it is not capable of: 
  + fitting models directly to S(t)
  + fitting to signal enhancement (ASE(t) or RSE(t))

+ Madym includes the bolus arrival time (BAT) as a free parameter in its TK models (thus BAT is fitted voxel-wise). It does not have methods implemented for estimating BAT as an independent step. Note however that if BAT is implemented as an independent step, Madym models can already make use of this via the parameter initialization/fixing options (see below). It may also be possible to treat BAT as a model-fit, depending on what method is used for BAT estimation

+ Madym can take image volumes as input for voxel-wise processing (either all or voxels or in a masked ROI) using the full `madym_DCE` pipeline or individual time-series as input using the `madym_DCE-lite` timeline. However it does not currently allow taking image volumes as input, computing an average over an ROI, and then fitting to the average time-series. This would however be trivial to add.

+ DSC: Madym has no DSC methods fitted (@michaelberks confession: I hadn't even heard of DSC before joining OSIPI)

### Additional options provided by Madym

Note some of these may be implicitly assumed in the OSIPI specs, even if they haven't been explicitly described

+ Dual-input models: Madym allows specifying a second vascular input function - thus far this has assumed to be the hepatic portal vein (due to developing Madym for liver processing) and thus labelled a PIF, but in theory this can be generalised to any secondary vascular input that mixes with the primary AIF using a single mixing proportion.

+ Parameter initialisation and fixing: Madym supports a rich set of options for configuring how parameters in TK models are initialised and optimised, including:
  + Specifying initial values for any parameters applied to all voxels
  + Specifying initial values for any parameters on a per-voxel basis (*eg* using previously output parameter maps as input)
  + Fixing any parameters to their initial values
  + Specifying relative bounds within which a parameter can be optimised (this is particularly useful with voxel-wise initialisation as it allows grid-search and then local refinement fitting)
  + Fitting to only a range of time-points within the DCE sequence (*eg* this can be used for BAT estimation to fit the delay time in the expected peak window, the output of which can be used as input to initialize delay time in subsequent fits)

+ Specifying AIFs using a simple input text format (as an additional option to using a population AIF or AIF mask) - this means any externally computed AIF can be used

+ Auto-detecting voxels from which to generate an AIF

+ Specifying an estimate of temporally varying (but spatially fixed) noise on the DCE time-series, allowing weighted least-squares model-fitting where noise is not constant across the time-series (in theory this means the fitted parameters remain maximum-likelihood estimators, which is not the case of a simple least-squares fit if noise - *ie* the variance of the error term - is not constant between samples)

## How well does Madym's C++ design translate to python?

Python is a object-oriented (OO) language, and while many OSIPI target users may not be used to writing their own classes, they will be used to class based methods from many of the common scientific toolboxes. Thus a good OO design should translate naturally to python while providing a simple to use interface.

Python should make some aspects of the design much simpler, *eg*:

+ Less worry about public/protected/private encapsulation (although it makes sense to use property decorators and leading underscores to have some notion of "private")

+ Multiple return values

+ Duck-typing for input types

+ Easy to import well established libraries for image IO

+ Simple element-wise processing of arrays

The latter point is the source of probably the biggest initial design decision: what to do about the Image3D class? In Madym, a 3D image object (which stores voxel data plus image data like acquisition parameters) is the basis of all volumetric processing. *eg* VFA T1 mapping is performed a set of 3D signal images; A DCE time-series is set of 3D images; Each parameter map is generated as a 3D image. However the image data in python will almost certainly be a numpy array (or some derivative of), in which case it makes sense to hold *eg* DCE time-series as a 4D array, so that a voxel time series is trivially extracted by slicing across the 4th dimension.

My suggestion would be to have a generic ImageND class with specification subclasses in 3 and 4D (similar to pytorch modules for 2 and 3D).

## Should we just start afresh for OSIPI?

+ Given this is a chance to start a library from fresh, are there 'old ways of thinking' embedded in Madym we're better off scrapping?

The 'pros' for starting with Madym as a design template are that:

+ It already solves a large part of the design specification

+ Most of what it doesn't solve will be trivial to add (especially in python)

+ It provides a concrete basis from which to get started

+ It provides a design specification for OSIPI contributors to critique and improve

The possible 'cons':

+ As the author of Madym, @michaelberks may be implicitly biased towards Madym's design, in a way that could be detrimental to OSIPI's final design

+ Other contributors may not feel comfortable critquing the design

+ This could hamper the overall OSIPI TF2.3 team effort 

+ [Design-to-the-lexicon](design_to_lexicon) provides an intriguing alternative, with modularity the overriding principal from the start of the design

The latter is possibly the biggest argument against starting with Madym as a design. However, the downside of the design-to-the-lexicon approach is knowing how to get started. 

@michaelberks: For this reason, I still feel the effort of translating Madym's structure to a python design (*ie* module files, class/method definitions and doc strings) is a worthwhile endeavour. From that starting point, we can consider to what extent a lexicon based design fits with the template, in a way I think will be more productive than trying to start with 'design-to-the-lexicon' from scratch.




