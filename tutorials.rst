*********
Tutorials
*********
.. tip::
  Before beginning, download the `pseudopotentials <https://github.com/elinscott/python_KI/tree/master/pseudos>`_ and set the environment variable ``ESPRESSO_PSEUDO_DIR`` to wherever they're located on your machine

A simple KI calculation on a molecule
=====================================
In this tutorial, we will calculate the ionisation potential and electron affinity of ozone.

.. literalinclude:: _static/tutorials/ozone.json
  :linenos:

A simple KI calculation on a solid
==================================
In this tutorial, we will calculate the KI bandstructure of bulk silicon.

.. literalinclude:: _static/tutorials/si.json
  :linenos:

Convergence testing
===================
In this tutorial, we will make use of the ``convergence`` task to determine how large a cell size and energy cutoff is required to converge the PBE energy of the highest occupied molecular orbital (HOMO) of a water molecule. In order to do this, our ``workflow`` block needs a few particular keywords:

.. literalinclude:: _static/tutorials/pbe_convergence.json
  :lines: 1-11
  :linenos:
  :emphasize-lines: 5, 7-9

The important lines are highlighted. ``"task": "convergence"`` means that we will be performing a convergence test. The other three highlighted keywords specifying that we are going to converge the HOMO energy to within 0.01 eV, with respect to *both* the energy cutoff ``ecutwfc`` and the cell size. The full input file can be found `here <https://raw.githubusercontent.com/elinscott/koopmans_docs/main/_static/tutorials/pbe_convergence.json>`_.

When you run the calculation you should get something like this:

.. code-block:: text

  $ koopmans pbe_convergence.json
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

..
  Calculating screening parameters
  ============================================
  To write


  A bulk system
  =========================

Calculating electron affinities for small anions
================================================
.. tip:: To run this tutorial, you will need a version of ``pw.x`` with the `environ <https://environ.readthedocs.io/en/latest/>`_ patch installed.

The ``koopmans`` package can also calculate the PBE electron affinities of small molecules using the method of Nattino *et al.*. These anions are typically unbound (wrongly) by PBE, which means we cannot perform a standard ΔSCF calculation. Instead, the molecule is embedded within a cavity and finite difference calculations are performed with increasingly small values of :math:`\varepsilon_\infty`. See :cite:`Nattino2019` for a more detailed description.

Running these calculations is enabled with the ``environ_dscf`` task, and ``eps_cavity`` is a list of the trial values of :math:`\varepsilon_\infty` to use e.g.

.. literalinclude:: _static/tutorials/o2_environ_dscf.json
  :lines: 2-5
  :linenos:

The full input file can be downloaded `here <https://raw.githubusercontent.com/elinscott/koopmans_docs/main/_static/tutorials/o2_environ_dscf.json>`_. When you run this calculation, the output will be as follows:

.. code-block:: text

  $ koopmans o2_environ_dscf.json
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

so we can see that for :math:`\varepsilon_\infty = 2` the anion became unstable, as expected. If we perform a quartic fit to the energies (following the example of Nattino *et al.*) we can extrapolate back to :math:`\varepsilon_\infty = 1` to obtain the electron affinity of 1.30 eV.

.. image:: _static/tutorials/o2_dscf_ea_result.png
  :width: 800
  :alt: Quartic fit to embedded energies of O2 to calculate its vertical electron affinity 
  :align: center

.. warning::
  The `koopmans` implementation of this workflow differs from Nattino *et al.* in one major aspect: we use the same atomic positions for the anion as the neutral molecule. This means that we obtain *vertical* rather than *adiabatic* electron affinities. The reason for this choice is to be consistent with Koopmans spectral functionals, whose LUMO energies correspond to vertical electron affinities.
