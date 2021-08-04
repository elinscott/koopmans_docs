.. _theory_ingredients:

The key ingredients in a Koopmans calculation
=============================================

.. _theory_vorbs_vs_corbs:

The variational orbitals
------------------------
.. image:: figures/fig_nguyen_variational_orbital.png
.. image:: figures/fig_nguyen_canonical_orbital.png

-  ODD functional means that we know :math:`\hat H \ket{\varphi_i}` for
   variational orbitals :math:`\{\ket{\varphi_i}\}` but we don’t know
   :math:`\hat H` in general

.. _theory_screening:

The screening parameters
------------------------
.. math::

   \frac{d E}{d f_i}
               \approx
               \alpha_i \frac{\partial E}{\partial f_i}
               \onslide<6->{
                  \Longrightarrow \varepsilon_i^\mathsf{Koopmans} = \frac{\partial E_\mathsf{Koopmans}}{\partial f_i}  \approx E_i(N-1) - E(N)}

Screening coefficients :math:`\{\alpha_i\}` must be determined first,
either (a) via :math:`\Delta`\ SCF calculations (using a supercell) or
(b) via DFPT (using a primitive cell)


.. _theory_dscf:

ΔSCF
^^^^

.. _theory_dfpt:

DFPT
^^^^

