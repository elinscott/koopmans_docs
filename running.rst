Running
=======
To run a calculation, all that is required is 

.. code-block:: bash

  $ koopmans <seed>.json


Input file
----------
The JSON input file contains the calculation parameters, divided into the following blocks: :ref:`workflow`, :ref:`setup`, :ref:`kcp`, :ref:`pw`, :ref:`w90`, and :ref:`pw2wannier`. These are explained below.

workflow
^^^^^^^^
The ``workflow`` block contains variables that define the details of the workflow that we are going to run. Valid keywords are as follows: 

.. raw:: html

   <center>
   <input type="text" id="myInput" onkeyup="lookupTable()" placeholder="Search for keywords...", style="width:50%">
   </center>
   <br>

.. raw:: html
   :file: _static/python_ki_keywords/keywords.html

.. raw:: html 

   <script>
   function lookupTable() {
     // Declare variables
     var input, filter, tab, tr, a, i, txtValue;
     input = document.getElementById('myInput');
     filter = input.value.toUpperCase();
     tab = document.getElementById("keywordTable");
     tr = tab.getElementsByTagName('tr');
     // Loop through all list items, and hide those who don't match the search query
     for (i = 1; i < tr.length; i++) {
       a = tr[i].getElementsByTagName("td")[0].getElementsByTagName("code")[0];
       txtValue = a.textContent || a.innerText;
       if (txtValue.toUpperCase().indexOf(filter) > -1) {
         tr[i].style.display = "";
       } else {
         tr[i].style.display = "none";
       }
     }
   }
   </script>

setup
^^^^^

The ``setup`` block contains variables common to all of the quantum espresso calculations e.g.

.. literalinclude:: _static/tutorials/pbe_convergence.json
  :lines: 12-36

It uses the same keywords and cards as ``kcp.x`` input files, with namelists and cards are provided as subdictionairies. The one exception to this rule is the ``k_points`` block, which is not a ``cp.x`` card but can still be provided here e.g.

.. literalinclude:: _static/tutorials/si.json
  :lines: 47-60

where ``kind`` can be either ``automatic`` or ``gamma``. ``kpath`` specifies the path for band structures plotted during post-processing.

kcp
^^^
This block contains keywords specific to ``kcp.x``, a modified version of ``cp.x`` for performing Koopmans calculations. Any keywords specified both here in the ``setup`` block will use the value provided in this block.

In addition to `the keywords associated with cp.x <https://www.quantum-espresso.org/Doc/INPUT_CP.html>`_ there are several new keywords associated with the Koopmans implementation in ``kcp.x``. These are...

pw
^^
This block contains keywords specific to ``pw.x`` (see the `list of pw.x keywords <https://www.quantum-espresso.org/Doc/INPUT_PW.html>`_)

w90
^^^
This block contains keywords specific to ``wannier90.x``. Because the occupied and empty manifolds are wannierised separately, you may want to use slightly different wannierization protocols for each. You can do this by placing keywords within the ``occ`` and ``emp`` sub-dictionaries e.g.

.. literalinclude:: _static/tutorials/si.json
  :lines: 75-93

In this case both the occupied and empty manifolds will use ``sp3`` projections, but only the empty manifold will use the provided ``dis_froz_max`` etc.

pw2wannier
^^^^^^^^^^
This block contains ``pw2wannier.x`` keywords, in a single dictionary with no subdictionairies.
