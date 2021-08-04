.. _theory_ingredients:

The key ingredients in a Koopmans calculation
=============================================

.. _theory_vorbs_vs_corbs:

The variational orbitals
------------------------
The one important distinction that is worth making right away is that Koopmans functionals are not density functionals, but *orbital-density-dependent* (ODD) functionals. This is because in addition to being dependent on the total density :math:`\rho` they are also dependent on the individual occupancies. Indeed, each orbital will be subjected to a different potential, and when we solve a Koopmans functional we must minimise the total energy with respect to the entire set of orbitals as opposed to just the total density.

A further complication of ODDFTs is that we actually have *two* sets of orbitals that we must be careful to distinguish. The set of orbitals that minimise the total energy are the so-called *variational* orbitals. Because the leading term in an orbital's Koopmans potential is the negative of that orbital's self-Hartree energy, these variational orbitals tend to be very localised.

.. figure:: figures/fig_nguyen_variational_orbital.png
   :width: 400
   :align: center
   :alt: Two variational orbitals of polyethylene

   Two variational orbitals of polyethylene. Figure taken from :cite:`Nguyen2018`

If we have minimised the total Koopmans energy we can then construct the Hamiltonian. If we then diagonalise this Hamiltonian we would obtain the so-called *canonical* orbitals. In a DFT framework, diagonalising the Hamiltonian would yield exactly the same orbitals that minimise the total energy. However, in an ODDFT, this is not the case, because the total energy is not invariant with respect to unitary rotations of a given set of orbitals, and thus the variational and canonical orbitals are different. In contrast to the variational orbitals, the canonical orbitals are typically very delocalised and much more closely resemble the Kohn-Sham orbitals of DFT. 

.. figure:: figures/fig_nguyen_canonical_orbital.png
   :width: 400
   :align: center
   :alt: a canonical orbital of polyethylene

   A canonical orbital of polyethylene. Figure taken from :cite:`Nguyen2018`

Going from a DFT to and ODDFT may seem like a bothersome complication but actually it is a natural generalisation of DFT -- indeed, an ODDFT is in fact an energy-discretised spectral functional theory :cite:`Ferretti2014`.

.. _theory_screening:

The screening parameters
------------------------
In any Koopmans calculation, we must obtain the set of screening parameters :math:`\{\alpha_i\}`. As we discussed earlier, we would like the functional's total energy to be piecewise linear i.e. we would like quasiparticle energy to match the corresponding total energy differences. Specifically, we would like :math:`\varepsilon^\text{Koopmans}_i = \Delta E^\text{Koopmans}_i`, where

.. math::

   \Delta E^\text{Koopmans}_i =
   \begin{cases}
      E^\text{Koopmans}(N) - E^\text{Koopmans}_i(N-1)
      & \text{filled orbitals}\\
      E^\text{Koopmans}_i(N+1) - E^\text{Koopmans}(N)
      & \text{empty orbitals}
   \end{cases}

where :math:`E^\text{Koopmans}_i(N\pm1)` is the total energy of the system where we add/remove an electron from variational orbital :math:`i` and allow the rest of the system to relax.

We will use this condition to determine the screening parameters `ab initio`. In order to do so, there are two potential approaches: (a) via :ref:`ΔSCF calculations <theory_dscf>` or (b) via :ref:`DFPT <theory_dfpt>`.

.. _theory_dscf:

ΔSCF
^^^^

In this approach, we explicitly calculate all of the energy differences :math:`\Delta E_i^\text{Koopmans}` via a series of constrained Koopmans and DFT calculations. Specifically, given a starting guess :math:`\{\alpha^0_i\}` for the screening parameters, an improved guess for the screening parameters can be obtained via

.. math::

   \alpha^{n+1}_i =
   \alpha^n_i \frac{\Delta E_i - \varepsilon_{i}^0(1)}{\varepsilon_{i}^{\alpha^n_i}(1) - \varepsilon_{i}^0(1)}

for filled orbitals and

.. math::

   \alpha^{n+1}_i =
   \alpha^n_i \frac{\Delta E_i - \varepsilon_{i}^0(0)}{\varepsilon_{i}^{\alpha^n_i}(0) - \varepsilon_{i}^0(0)}

for empty orbitals, where

.. math::

   \varepsilon_{i}^{\alpha_i}(f) = \left.\frac{dE_\text{Koopmans}}{df_i}\right|_{f_i = f} = \left.\langle \varphi_i|\hat H_\text{DFT} + \alpha_i \hat v_i^\mathrm{Koopmans}|\varphi_i \rangle\right|_{f_i = f}

All of these quantities for calculating :math:`\alpha^{n+1}_i` are obtained from constrained Koopmans and DFT calculations. Specifically, a :math:`N`-electron Koopmans calculation yields :math:`E^\text{Koopmans}(N)` and :math:`\varepsilon^{\alpha_i^n}_i`, a constrained :math:`N \pm 1`-electron calculation yields :math:`E^\text{Koopmans}_i(N \pm 1)`, and a DFT calculation yields :math:`\varepsilon_i^0`.

Typically, very few iterations are required in order to reach self-consistency.

.. note::

   For a periodic system, this method for determining the screening parameters requires a supercell treatment. This is because the :math:`N \pm 1`-electron systems have a charged defect and a supercell is required in order to avoid spurious interactions between periodic images.

.. _theory_dfpt:

DFPT
^^^^

TODO

.. note::

   Comment on scaling comparing the two methods

.. note::

   Comment on what is and isn't possible with the current formulation

The flavour: KI, pKIPZ, or KIPZ
-------------------------------
KI vs KIPZ...