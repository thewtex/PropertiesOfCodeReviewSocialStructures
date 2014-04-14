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

Another model that can be considered is the `hierarchical structure
<http://en.wikipedia.org/wiki/Hierarchy>`_, shown in Figure 2. Familiar from
militaries and industrial era corporations, generals delegate to lieutenants,
who delegate to majors, etc.  The detail and scope of reviews decrease and
increase, respectively, as they travel up the hierarchy. An example is the
Linux kernel where Linus Torvalds delegates to lieutenants for the various
sub-systems of the kernel.

The third model we'll consider is the `community structure
<http://en.wikipedia.org/wiki/Community_structure>`_, Figure 3. These
self-organizing networks emerge when members contribute reviews as their
interest and time permit.  This type of network is encouraged by tools like
`Gerrit <https://code.google.com/p/gerrit/>`_ or when anyone is encouraged to
perform a review that shows up on a label rating board. An example is the code
review structure of a project I have participated in, the `Insight Toolkit
<http://itk.org>`_, Figure 4.  Interestingly , the number of reviews performed by
community members follow a `power law
<http://en.wikipedia.org/wiki/BA_model>`_, just like the `distribution of code
submitted <http://www.whust.com/staff/yutao%20ma_files/SEKE2013.pdf>`_, Figure
6.
