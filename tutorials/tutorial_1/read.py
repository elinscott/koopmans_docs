from koopmans.io.jsonio import read_json
  
# Load the workflow object
with open('ozone.kwf', 'r') as fd:
    wf = read_json(fd)

# Access the results from the very last calculation
results = wf.all_calcs[-1].results

# Calculate the IP and EA
ip = -results['homo_energy']
ea = -results['lumo_energy']

# Print
print(f' IP = {ip:.2f} eV')
print(f' EA = {ea:.2f} eV')
