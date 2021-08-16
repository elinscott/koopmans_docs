from koopmans.io import read_json

for grid_size in [2, 4, 8]:

    print('\n {0}x{0}x{0} grid'.format(grid_size))

    wf = read_json('si.json', override={'setup': {'k_points': {'kpts': [grid_size for _ in range(3)]}}})
    wf.run()
