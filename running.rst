python KI
=========
To run a calculation, all that is required is 

.. code-block:: bash

  $ run_koopmans.sh <seed>.json


Input file
----------
The JSON input file contains the calculation parameters, divided into the following blocks: :ref:`workflow`, :ref:`setup`, :ref:`cp`, :ref:`pw`, :ref:`w90`, and :ref:`pw2wannier`. These are explained below.

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

It uses the same keywords and cards as ``cp.x`` input files, with namelists and cards are provided as subdictionairies. The one exception to this rule is the ``k_points`` block, which is not a ``cp.x`` card but can still be provided here e.g.

.. literalinclude:: _static/tutorials/bulk_si.json
  :lines: 27-32

where ``kind`` can be either ``automatic`` or ``gamma``.

cp
^^
This block contains keywords specific to ``cp.x`` (see the `list of cp.x keywords <https://www.quantum-espresso.org/Doc/INPUT_CP.html>`_). Any keywords specified both here in the ``setup`` block will use the value provided in this block.

There are several new keywords associated with the Koopmans implementation in ``cp.x``. These are...

pw
^^
This block contains keywords specific to ``pw.x`` (see the `list of pw.x keywords <https://www.quantum-espresso.org/Doc/INPUT_PW.html>`_)

w90
^^^
This block contains keywords specific to ``wannier90.x``, contained in two subdictionairies, ``occ`` and ``emp``, specifying the wannierization protocol for the occupied and empty manifolds e.g.

.. literalinclude:: _static/tutorials/bulk_si.json
  :lines: 50-69

pw2wannier
^^^^^^^^^^
This block contains ``pw2wannier.x`` keywords, in a single dictionary with no subdictionairies.
