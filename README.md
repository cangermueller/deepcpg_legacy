DeepCpG
=======

Abstract
--------
Technological advances have enabled assaying genome-wide DNA methylation in
single cells. Methods to model and predict methylation states are critical, both
for understanding the sources of methylation variability, and for addressing the
challenges of incomplete coverage to enable genome-wide analyses. We here report
DeepCpG, a method based on deep neural networks that predicts DNA methylation
states from DNA sequence and CpG context in single cells and populations. In
applications to mouse embryonic stem cells, we find that DeepCpG yields
substantially more accurate predictions of methylation states than previous
methods across genomic contexts. Additionally, the model allows to efficiently
quantify the effect of DNA nucleotide and methylation state changes, and
discovers previously known and new sequence motifs that affect DNA methylation.
Finally, we show that some of these motifs are primarily associated with changes
in methylation levels while others appear to control DNA methylation
heterogeneity between cells.

Content
-------
* `/deepcpg/`: DeepCpG package
* `/script/`: Scripts for data generation, model training, and imputation
* `/examples/`: Example files for model training and imputation
* `/data/`: Example data files

Contact
-------
* Christof Angermueller
* cangermueller@gmail.com
* https://cangermueller.com
