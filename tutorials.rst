*********
Tutorials
*********
.. tip::
  Before beginning, download the `pseudopotentials <https://github.com/elinscott/python_KI/tree/master/pseudos>`_ and set the environment variable ``ESPRESSO_PSEUDO_DIR`` to wherever they're located on your machine

A simple KI calculation 
===================================
To write

Convergence testing
===============================
In this tutorial, we will make use of the ``convergence`` task to determine how large a cell size and energy cutoff is required to converge the PBE energy of the highest occupied molecular orbital (HOMO) of a water molecule. In order to do this, our ``workflow`` block needs a few particular keywords:

.. literalinclude:: _static/tutorials/pbe_convergence.json
  :lines: 1-11
  :linenos:
  :emphasize-lines: 5, 7-9

The important lines are highlighted. ``"task": "convergence"`` means that we will be performing a convergence test. The other three highlighted keywords specifying that we are going to converge the HOMO energy to within 0.01 eV, with respect to *both* the energy cutoff ``ecutwfc`` and the cell size. The full input file can be found `here <https://raw.githubusercontent.com/elinscott/koopmans_docs/main/_static/tutorials/pbe_convergence.json>`_.

When you run the calculation you should get something like this:

.. code-block:: text

  $ run_koopmans.py pbe_convergence.json
  ecutwfc = 20.0, cell_size = 1.0
  Running pbe... done
  
  ecutwfc = 20.0, cell_size = 1.1
  Running pbe... done
  
  ecutwfc = 20.0, cell_size = 1.2
  Running pbe... done
  
  ...
  
  ecutwfc = 60.0, cell_size = 1.4
  Running pbe... done
  
  Converged parameters are ecutwfc = 50.0, cell_size = 1.3

The code progressively tries higher and higher energy cutoffs, as well as larger and larger cells, until it arrives at the converged solution, with a ``ecutwfc`` of 50.0 Ha and a cell 1.3 times larger than that provided in the ``.json`` input file.

The individual calculations reside in nested subdirectories. If you plot the HOMO energies from each of these, this is what you will get:

.. image:: _static/tutorials/pbe_convergence_plot.png
  :width: 800
  :alt: Plot of HOMO energy with respect to ecutwfc and cell size
  :align: center

and we can see that indeed the calculation with ``ecutwfc = 50.0`` and ``cell_size = 1.3`` is the one where the energy of the HOMO goes within (and stays within) 0.01 eV of the most accurate calculation.

Calculating screening parameters
============================================
To write


A bulk system
=========================

Calculating electron affinities for small anions
================================================

.. literalinclude:: _static/tutorials/o2_environ_dscf.json
  :lines: 1-5
  :linenos:

The full input file can be downloaded `here <https://raw.githubusercontent.com/elinscott/koopmans_docs/main/_static/tutorials/o2_environ_dscf.json>`_

.. code-block:: text

  PBE ΔSCF WORKFLOW

  Performing neutral calculations...
  Running neutral/8/pbe... done
  Running neutral/6/pbe... done
  Running neutral/4/pbe... done
  Running neutral/3.5/pbe... done
  Running neutral/3/pbe... done
  Running neutral/2.5/pbe... done
  Running neutral/2/pbe... done
  Running neutral/1/pbe... done

  Performing charged calculations...
  Running charged/8/pbe... done
  Running charged/6/pbe... done
  Running charged/4/pbe... done
  Running charged/3.5/pbe... done
  Running charged/3/pbe... done
  Running charged/2.5/pbe... done
  Running charged/2/pbe... failed to converge

  WORKFLOW COMPLETE

.. image:: _static/tutorials/o2_dscf_ea_result.png
  :width: 800
  :alt: Quartic fit to embedded energies of O2 to calculate its vertical electron affinity 
  :align: center