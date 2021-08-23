from koopmans import io

# Load the workflow object
wf = io.read('si.kwf')

# Access the band structure from the very last calculation
results = wf.all_calcs[-1].results
bs = results['band structure']

# Print the band strucutre to file
bs.plot(filename='ki_bandstructure.png')

# Extract the band gap
n_occ = wf.master_calcs['w90_occ'].num_wann
gap = bs.energies[:, :, n_occ:].min() - bs.energies[:, :, :n_occ].max()
print(f'KI band gap = {gap:.2f} eV')
