*********
Tutorials
*********
.. tip::
  Before beginning, download the `pseudopotentials <https://github.com/elinscott/python_KI/tree/master/pseudos>`_ and set the environment variable ``ESPRESSO_PSEUDO_DIR`` to wherever they're located on your machine

A simple KI calculation 
===================================

Convergence testing
===============================
In this tutorial, we will make use of the ``convergence`` task to determine how large a cell size and energy cutoff is required to converge the PBE total energy of a water molecule. In order to do this, our ``workflow`` block needs a few particular keywords:

.. literalinclude:: _static/tutorials/pbe_convergence.json
  :lines: 1-10
  :linenos:
  :emphasize-lines: 5, 7-9

The important lines are highlighted. ``"task": "convergence"`` means that we will be performing a convergence test. The other three highlighted keywords specifying that we are going to converge the total energy to within 0.1 eV, with respect to *both* the energy cutoff ``ecutwfc`` and the cell size. The full input file can be found `here <https://raw.githubusercontent.com/elinscott/koopmans_docs/main/_static/tutorials/pbe_convergence.json>`_.

When you run the calculation you should get something like this:

.. code-block:: bash

  $ run_koopmans.py pbe_convergence.json
  ecutwfc = 20.0, cell_size = 1.0
  Running pbe... done
  
  ecutwfc = 20.0, cell_size = 1.1
  Running pbe... done
  
  ecutwfc = 20.0, cell_size = 1.2
  Running pbe... done
  
  ...
  
  ecutwfc = 80.0, cell_size = 1.2
  Running pbe... done
  
  Converged parameters are ecutwfc = 70.0, cell_size = 1.0

Calculating screening parameters
============================================

A bulk system
=========================


