The setup block
^^^^^^^^^^^^^^^

The ``setup`` block contains variables common to all of the quantum espresso calculations e.g.

.. literalinclude:: ../../tutorials/tutorial_3/pbe_convergence.json
  :lines: 12-36

It uses the same keywords and cards as ``kcp.x`` input files, with namelists and cards are provided as subdictionairies. The one exception to this rule is the ``k_points`` block, which is not a ``cp.x`` card but can still be provided here e.g.

.. literalinclude:: ../../tutorials/tutorial_2/si.json
  :lines: 47-60

where ``kind`` can be either ``automatic`` or ``gamma``. ``kpath`` specifies the path for band structures plotted during post-processing.

