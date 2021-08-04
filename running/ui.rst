The ui block
^^^^^^^^^^^^
This block controls the unfolding and interpolation procedure for generating band structures and densities of states from Γ-only supercell calculations

.. raw:: html

   <center>
   <input type="text" id="uiInput" onkeyup="lookupTable(uiInput, uiTable)" placeholder="Search for keywords...", style="width:50%">
   </center>
   <br>

.. raw:: html
   :file: ../_static/python_ki_keywords/ui_keywords.html

.. raw:: html

   <script>

   function lookupTable(input, tab) {
     // Declare variables
     var input, filter, tab, tr, a, i, txtValue;
     // input = document.getElementById(inputID);
     filter = input.value.toUpperCase();
     // tab = document.getElementById(tableID);
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

