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

   \varepsilon_{i}^{\alpha_i}(f) = \left.\frac{\partial E_\text{Koopmans}}{\partial f_i}\right|_{f_i = f} = \left.\langle \varphi_i|\hat H_\text{DFT} + \alpha_i \hat v_i^\mathrm{Koopmans}|\varphi_i \rangle\right|_{f_i = f}

All of these quantities for calculating :math:`\alpha^{n+1}_i` are obtained from constrained Koopmans and DFT calculations. Specifically, a :math:`N`-electron Koopmans calculation yields :math:`E^\text{Koopmans}(N)` and :math:`\varepsilon^{\alpha_i^n}_i`, a constrained :math:`N \pm 1`-electron calculation yields :math:`E^\text{Koopmans}_i(N \pm 1)`, and a DFT calculation yields :math:`\varepsilon_i^0`.

Typically, very few iterations are required in order to reach self-consistency.

.. note::

   For a periodic system, this method for determining the screening parameters requires a supercell treatment. This is because the :math:`N \pm 1`-electron systems have a charged defect and a supercell is required in order to avoid spurious interactions between periodic images.

.. _theory_dfpt:

DFPT
^^^^
In this approach the energy is approximated as a quadratic function of the occupation number and the expression for the screening coefficients reduces to

.. math::  \alpha_i = \frac{d^2E_{\rm DFT}/df_i^2}{\partial^2 E_{\rm DFT}/\partial f_i^2} = \frac{\langle n_i | \epsilon^{-1} f_{\rm Hxc} | n_i \rangle}{\langle n_i | f_{\rm Hxc} | n_i \rangle} 

where :math:`\frac{d}{df_i}` and :math:`\frac{\partial}{\partial f_i}` represent variations done accounting for the orbitals relaxation or not, respectively. 
:math:`\epsilon(\mathbf{r},\mathbf{r}')` is the microscopic dielectric function of the material, 
:math:`f_{\rm Hxc}(\mathbf{r},\mathbf{r}') = \delta^2 E_{Hxc}/ \delta \rho(\mathbf{r})\delta \rho(\mathbf{r}')` is the Hartree-exchange and correlation kernel,
and :math:`n_i(\mathbf{r})=|\varphi_i(\mathbf{r})|^2` is the orbital density. The evaluation of the screening coefficient within this approach requires only 
quantity available from a :math:`N`-electrons system calculation and has been implemented :cite:`Colonna2018` using the machinery of Density Functional 
Perturbation Theory :cite:`Baroni2001`. Eq :eq:`alpha_LR` can be rewritten in term of the desity response :math:`\Delta^i \rho` to a perturbation given by the Hxc potential :math:`V^i_{\rm pert}` generated by the orbital density :math:`n_i`:

.. math:: \alpha_i = 1 + \frac{\langle V^{i}_{\rm pert} | \Delta^{i} \rho \rangle}{\langle n_{i} | V^{i}_{\rm pert} \rangle}
          :label: alpha_LR

The advantage of this approach compared to the ΔSCF is that there is no need for a supercell treatment, and in the 
case of peridoc solids a primitive cell implementaiton can be used :cite:`Colonna2021`. In particular in this latter 
case the Bloch symmetry can be explicitely exploited meaning that the linear response formula for the screening coeffcient 
:eq:`alpha_LR` can be decomposed into a set of independent problems, one for each :math:`q` point sampling the Brillouin 
zone of the primitive cell

.. math::  \alpha_{i} =  1 + \frac{\sum_{\mathbf{q}} \langle V^{i}_{{\rm pert},\mathbf{q}} | \Delta^{i}_{\mathbf{q}}\rho \rangle} {\sum_{\mathbf{q}} \langle \rho^{i}_{\mathbf{q}} | V^{i}_{{\rm pert}, \mathbf{q}} \rangle}

This means that the problem can be solved on separate computational resources, allowing for a straightforward parallelization, and more 
importantly, the computational cost is also greatly reduced (see below).

 The limitations of the DFPT approch are

1. the quadratic approximation, which however is in most of the case very accurate correctly capturing the leading Hartree contribution and leaving outside 
   orders higher than the second one in the xc contribution. 
2. it is only applicable to the KI functional, for KIPZ the implementation of the PZ kernel, i.e. the second derivative of the PZ enegy wrt the density would 
   be needed and this is not implemented in common electronic structure codes. 


Computational scaling
^^^^^^^^^^^^^^^^^^^^^
In the ΔSCF the screening coefficients are computed within a Supercell (SC) setup and with a finite difference approach by performing
additional total-energy calculations where the occupation of a Wannier function is constrained~\cite{nguyen_koopmans-compliant_2018}. 
This requires, for each orbital, multiple SCF calculations with a computational time :math:`T^{\rm SC}` that scales roughly as :math:`{N_{\rm el}^{\rm SC}}^3`,
where :math:`N_{\rm el}^{\rm SC}` is the number of electrons in the SC. The DFPT approach described above scales instead as 
:math:`T^{\rm PC} \propto N_{\mathbf{q}} N_{\mathbf{k}} {N_{\rm el}^{\rm PC}}^3`; this is the typical computational time for the SCF cycle 
(:math:`N_{\mathbf{k}} {N_{\rm el}^{\rm PC}}^3`), times the number of independent monochromatic perturbations (:math:`N_{\mathbf{q}}`). Using 
the relation :math:`N_{\rm el}^{\rm SC}=N_{\mathbf{k}}N_{\rm el}^{\rm PC}`, and the fact that :math:`N_{\mathbf{q}}=N_{\mathbf{k}}`, the ratio between the 
SC and PC computational times is :math:`T^{\rm SC}/T^{\rm PC} \propto N_{\mathbf{q}}`. Therefore as the supercell size (and, equivalently, 
the number of :math:`\mathbf{q}`-points in the PC) increases, the PC-DFPT approach becomes more and more computationally convenient.



The flavour: KI, pKIPZ, or KIPZ
-------------------------------
As we have seen Koopmans functionals are constructed starting from the exact or an approximate DFT energy functional :math:`E^{\rm DFT}` 
(the "base" functional) and replacing, orbital-by-orbital, the contribution to the total DFT energy that is not linear in the fractional
orbital occupation with one that is linear:

.. math:: 

    & E^{\rm Koopmans} =  E^{\rm DFT} + \sum_{i} \alpha_i \Pi^{\rm Koopmans}_i\;, \label{kc_gen} \\
    & \Pi_i^{\rm Koopmans} = -\int_0^{f_i} \langle \varphi_i | \hat{H}^{\rm DFT}(s) | \varphi_i \rangle ds + f_i \eta_i\;. \label{kc_gen1}

Here, :math:`\hat{H}^{\rm DFT}(s)` is the KS Hamiltonian of the underlying density functional (exact or approximated) calculated with a fractional 
occupation :math:`s` in orbital :math:`\varphi_i`, and :math:`\alpha_i` are screening coefficients introduced to ensure the linearity is 
preserved when taking into account the response and relaxation of all other orbitals :math:`\{\varphi_{j\neq i}\}`. 
The slope :math:`\eta_i` in the linear Koopmans' term can be chosen in a number of ways, leading to different Koopmans flavors. 
In KI the slope :math:`\eta_i` is chosen as the total energy difference of two adjacent electronic configurations with integer occupations:

.. math::
    \eta_i^{\rm KI} = & E^{\rm DFT}[f_i=1]-E^{\rm DFT}[f_i=0] \nonumber \\
                  = & \int_0^{1} \langle \varphi_i | \hat{H}^{\rm DFT}(s) | \varphi_i \rangle ds;
                  \label{eta_ki}

the explicit expression for the unscreened KI Koopmans' correction becomes thus

.. math::
 \Pi_i^{\rm KI} = -\int_0^{f_i} \langle \varphi_i | \hat{H}^{\rm DFT}(s) | \varphi_i \rangle ds + f_i \int_0^{1} \langle \varphi_i | \hat{H}^{\rm DFT}(s) | \varphi_i \rangle ds\;,


where it can be seen that at integer occupations :math:`\Pi^{\rm KI}_i=0`, and the KI functional becomes identical to its base functional, 
independently from the screening coefficients. The KI functional thus preserves exactly the potential energy surface of the base functional, 
including that of the exact DFT functional (if one had it); its values at fractional occupations are instead different 
(except when the highest occupied state is concerned), and so are the derivatives calculated at integer occupations - hence the effect on
spectral properties.

In KIPZ the slope :math:`\eta_i` is also chosen as the total energy difference of two adjacent electronic configurations with integer 
occupations, but this time using the Perdew-Zunger (PZ) self-interaction corrected (SIC) functional applied onto the  approximate DFT base
functional. We have

.. math::
    \eta_i^{\rm KIPZ} = & E^{\rm PZ}[f_i=1]-E^{\rm PZ}[f_i=0] \nonumber \\
                  = & \int_0^{1} \langle \varphi_i | \hat{H}_i^{\rm PZ}(s) | \varphi_i \rangle ds,
                  \label{eta_kipz}

providing the explicit expression for the unscreened :math:`\Pi_i^{\rm KIPZ}` correction

.. math::
 \Pi_i^{\rm KIPZ} = -\int_0^{f_i} \langle \varphi_i | \hat{H}^{\rm DFT}(s) | \varphi_i \rangle ds + f_i \int_0^{1} \langle \varphi_i | \hat{H}^{\rm PZ}_i(s) | \varphi_i \rangle ds\;.

where :math:`\hat{H}_i^{\rm PZ}(s) = \hat{H}^{\rm DFT}(s) - \hat{v}^{\rm DFT}_{\rm Hxc}[\:s\:|\varphi_i(\mathbf{r})|^2\:]`, 
with :math:`-\hat{v}^{\rm DFT}_{\rm Hxc}[\:s\:|\varphi_i(\mathbf{r})|^2\:]` the PZ self-interaction correction for the 
:math:`i^{\rm th}` orbital, that subtracts out the sum of the Hartree and exchange-correlation potentials for that orbital,
that has occupation :math:`s` and orbital density :math:`s\:|\varphi_i(\mathbf{r})|^2`.
Note that in the unscreened case (:math:`\alpha_i = 1`) the KIPZ functional can be thought of as the KI correction
applied to the PZ-SIC functional (this can be verified by replacing the base DFT functional and Hamiltonian with its PZ-SIC 
counterparts). However, in the general case of :math:`\alpha_i \ne 1` the KIPZ functional form implies also scaling each PZ 
self-interaction correction with its own screening coefficient. At integer occupations the KIPZ functional thus results into a
scaled PZ-SIC functional; this is a desirable property since the bare PZ self-interaction correction tends to overcorrect the base 
functional :cite:`vydrov2004,vydrov2005` and introducing a scaling parameter often improves the energetic and 
thermochemistry :cite:`Jonsson_JCP_2012,vydrov_scaling_down_PZ,jonsson_simulation_2011`. 
The KIPZ screening parameters thus plays a dual role; they ensure linearity when taking into account orbital relaxations and 
acts as physically motivated scaling parameters for the PZ corrections (we note that further refinements could use different screening 
parameters to impose PWL, and to impose correctly charge transfer or polarizability). 

In summary, these two approaches lead to two functionals that depend only on orbital densities with the following final expressions 
for the unscreened KI and KIPZ corrections :cite:`Borghi2014`:

.. math::
     \Pi^{\rm KI}_i &=  E_{\rm Hxc} [\rho-\rho_i] -E_{\rm Hxc}[\rho] \nonumber \\      
     &+f_i \Big[ E_{\rm Hxc}[\rho-\rho_i+n_i] -E_{\rm Hxc}[\rho-\rho_i] \Big]\label{Eq:KC_KI}, \\
    %
     \Pi^{\rm KIPZ}_i &= \Pi^{\rm KI}_i -f_i E_{\rm Hxc} [n_i]\label{Eq:KC_KIPZ},

having defined :math:`\rho_i(\mathbf{r}) = f_i\:|\varphi_i(\mathbf{r})|^2` and :math:`n_i(\mathbf{r}) = |\varphi_i(\mathbf{r})|^2`, 
and with :math:`E_{\rm Hxc}` denoting the Hartree and exchange-correlation energy corresponding to the underlying base functional.
As mentioned, the orbital-dependent screening coefficients :math:`\alpha_{i}` account for electronic screening and orbitals relaxation;
if these were all set to be equal to one, the Koopmans functionals would fulfill the Koopmans' condition at frozen orbitals, rather than at 
relaxed orbitals.

Once the screening coefficients are defined, from a computational point of view a complete KIPZ calculation requires the energy minimization 
of the orbital-density dependent functionals. The KI energy correction is instead identically zero at integer occupation numbers (i.e. for 
insulating systems), meaning that it preserves the ground state density and enegy of the underlying density functional and its unitary 
invariance under rotation of the occupied and empty electronic manifolds. To uniquely define the minimizing orbitals we add an infinitesimally 
small PZ-SIC contribution to the KI energy. This allow us to 1) unanbigously defined the manifolds, since the small PZ-SIC term breaks the 
unitary invariance, and 2) localize the orbitals without changing the ground-state energy. Overall this ammount to defining KI as the limit
of the KIPZ functional when the PZ-SIC correction is vanishingly small :cite:`Borghi2014`. The only additional cost beside the underlying DFT 
calculation is therefor the one needed to define the unitary transformation connecting the DFT canonical states to the PZ-SIC ones at fixed manifold.
To retain the computational cost of the KI calculation and the superior accuracy of the KIPZ functional, a perturbative KIPZ (pKIPZ) calculation 
can be defined where the KIPZ hamiltonian is computed on top of the KI variational orbitals and screening coefficients, 
thus neglecting self-consistency effects at the KIPZ level. This typically shows performance in between the KI and KIPZ functionals at a 
computational cost almost identical to that of a KI calculation :cite:`Colonna2019`. 
