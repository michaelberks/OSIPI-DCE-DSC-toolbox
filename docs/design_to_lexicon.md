# Design-to-lexicon

[OSIPI task-force 4.2](https://osipi.org/task-force-4-2/) is tasked with developing guidelines for reporting of DCE/DSC image acquisition and analysis. In doing so, they have developing a comprehensive lexicon that describes all aspects of DCE/DSC analysis in modular components, with functional relationships between components generating analysis pipelines.

Thus one way of implementing a harmonized DCE/DSC library would be to start with the lexicon, and produce code that directly implements each modular component.

+ The lexicon components are grouped at a high-level - each component class would translate to an abstract base class

+ All/most/some? lexicon components translate naturally to sub-classes of their group

+ Functional relationships between components could either be defined as class methods, or standalone imperitaive functions

Implementing the DCE/DSC library in this way would surely provide a guaranteed level of modularity and extensibility.

+ We could either start from scratch with a design-to-lexicon approach

+ We could start with an initial design template, and then see how well this fits the lexicon, updating the design as necessary (*eg* see [thoughts on using Madym as a design template for OSIPI](madym_vs_osipi))