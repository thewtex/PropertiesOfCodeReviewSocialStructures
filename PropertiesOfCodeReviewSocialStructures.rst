Robustness and Information Transmission Properties of Code Review Social Structures
====================================================================================

Introduction
------------

Code review is a practice that facilitates the rapid collaboration, sharing of
knowledge, and supreme quality typical in open source projects. The code
review social structure is a defining characteristic of a project.  What is
the best social structure for an open source project? In this article, we
examine this question by analyzing three common models, the benevolent dictor
for life (BFDL), hierarchy, and community models with two graph theory metrics
that quantify their robustness and information transmission capabilities.

Code Review Social Structures
-----------------------------

Long before the likes of Facebook and LinkedIn became popular, open source
projects developed social structures through mailing lists. In that history, a
few organizational structures governing the review and integration of code
have emerged.

.. raw:: html

  <iframe src="figures/bdfl_graph.html" name="bdfl_graph" scrolling="no"
  seamless="seamless" width="500" height="400"></iframe>

*Figure 1: Graph model of the Benevolent Dictator for Life code review
social structure.*

The term `Benevolent Dictator for Life
<https://en.wikipedia.org/wiki/Benevolent_Dictator_For_Life>`_ refers to a
single individual that controls a project's direction, such as Guido van
Rossum of the `Python <http://python.org>`_ programming language. For larger
projects this only applies to issues where there are arguments
or disputes, but the model taken to totalitarian extremes is represented by Figure
1. In this model, one person reviews and controls all patches before they are
committed. This structure is encouraged by tools like
`GitHub <https://github.com>`_ when patches are reviewed after `forking
<https://help.github.com/articles/fork-a-repo>`_ and
creating a `pull request
<https://help.github.com/articles/using-pull-requests>`_ for a single-owner
repository.

.. raw:: html

  <iframe src="figures/hierarchy_graph.html" name="hierarchy_graph" scrolling="no"
  seamless="seamless" width="500" height="400"></iframe>

*Figure 2: Graph model of a hierarchical code review social structure.*

Another model that can be considered is the `hierarchical structure
<http://en.wikipedia.org/wiki/Hierarchy>`_, shown in Figure 2. Familiar from
militaries and industrial era corporations, generals delegate to lieutenants,
who delegate to majors, etc.  The detail and scope of reviews decrease and
increase, respectively, as they travel up the hierarchy. An example is the
Linux kernel where Linus Torvalds delegates to lieutenants for the various
sub-systems of the kernel.

.. raw:: html

  <iframe src="figures/community_graph.html" name="community_graph" scrolling="no"
  seamless="seamless" width="500" height="400"></iframe>

*Figure 3: Graph model of a community code review social structure.*


The third model we'll consider is the `community structure
<http://en.wikipedia.org/wiki/Community_structure>`_, Figure 3. These
self-organizing networks emerge when members contribute reviews as their
interest and time permit.  This type of network is encouraged by tools like
`Gerrit <https://code.google.com/p/gerrit/>`_ or when anyone is encouraged to
perform a review that shows up on a label rating board.

Quantifying their Properties
----------------------------

We can assess models in Figures 1-3 with metrics defined in social network
theory. In these models, each node represents a person and each edge
represents a code review.

The size of nodes in the graph visualizations are scaled by a measure of
information transmission, `closeness centrality
<http://networkx.lanl.gov/reference/generated/networkx.algorithms.centrality.closeness_centrality.html>`_. The closeness centrality is a normalized measure, with
values that range from zero to one, that quantifies the inverse of the average
distance to all other people in the code review network. When closeness
centrality is high, knowledge is communicated well. High closeness means that
experiences and knowledge of many peers are transmitted so that individual
contributions are strengthened by the size of the network.

The color of nodes in the graph visualization are mapped according to how
critical they are to maintaining communication within the network.  Blue nodes
have a low `betweenness centrality
<http://networkx.lanl.gov/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html>`_, red nodes a high betweenness centrality, and purple hued nodes
are somewhere in the middle. Betweenness centrality is a normalized measure of
the number of shortest paths that pass through a reviewer.  When there are
nodes with high betweenness centrality it reflects poorly on the robustness of
that network -- if the node would fail, communication in the network will
fall apart.

How the Models Perform
----------------------

The BDFL model, Figure 1, performs very well in information transmission
(closeness centrality), but lacks robustness.  Since the central BFDL node is
involved in all the reviews, they impart their knowledge and pass on
information from every other participant in the network. However, the central
BFDL node is also a single point of failure.  Should the central node switch
jobs, go on vacation, discover a new programming language, get hit by a bus,
be abducted by aliens, etc., the network will collapse.  The *degree* of the
central node, how many code reviews that are performed, is also very high.
This is likely to cause burnout and makes it difficult for the network to
scale.

While the hierarchical structure in Figure 2 can scale without requiring any
single node to have a high degree, it fails in both and robustness and information
transmission properties.  The network is vulnerable to losses at the top of the
hierarchy.  And the information transmission, visualized as the size of the
nodes, is poor throughout the entire network.

While the community code review structure in Figure 3 lacks the regularity
found in Figure 1 or Figure 2, it both has high information transmission
capabilities and is very robust. While there is not an express BFDL or top of
the hierarchy, leaders still emerge in this structure. This leading roles are
determined by actions, e.g. the amount of reviews performed, instead of
their position in the network. But there are additional requirements in this
free form organization. Higher amounts of communication are necessary --
there are more edges than the other models. Also, this situation requires
tools and objective criteria to make effective decisions; whether to merge a
patch can depend on whether it passes all
`unit tests <http://en.wikipedia.org/wiki/Unit_testing>`_, has reached the standard
testing `code coverage <http://en.wikipedia.org/wiki/Code_coverage>`_, passes
automated style checks, etc. as opposed to "whether Lieutenant Dan says so."

Conclusions
-----------



An example is the code
review structure of a project I have participated in, the `Insight Toolkit
<http://itk.org>`_, Figure 4.  Interestingly , the number of reviews performed by
community members follow a `power law
<http://en.wikipedia.org/wiki/BA_model>`_, just like the `distribution of code
submitted <http://www.whust.com/staff/yutao%20ma_files/SEKE2013.pdf>`_, Figure
6.
