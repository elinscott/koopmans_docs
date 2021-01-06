from glob import glob
from koopmans import io
import matplotlib.pyplot as plt
import aesthetics

if __name__ == '__main__':

    calcs = []
    for fname in glob('*/*/*.cpo'):
        fname = fname.replace('.cpo', '')
        calc = io.load_calculator(fname)
        calc.cell_size = calc.calc.atoms.cell[0, 0] 
        calcs.append(calc)

    ecutwfcs = sorted(list(set([c.ecutwfc for c in calcs])))
    cell_sizes = sorted(list(set([c.cell_size for c in calcs])))

    fig, ax = plt.subplots()

    [reference_calc] = [c for c in calcs if c.ecutwfc == max(ecutwfcs) and c.cell_size == max(cell_sizes)]
    ref_homo = reference_calc.results['homo_energy']

    for cell_size in cell_sizes:
        selected_calcs = sorted([c for c in calcs if c.calc.atoms.cell[0, 0] == cell_size], key=lambda x: x.ecutwfc)
        assert [c.ecutwfc for c in selected_calcs] == ecutwfcs
        x = ecutwfcs
        y = [abs(c.results['homo_energy'] - ref_homo) for c in selected_calcs]
        if cell_size == max(cell_sizes):
            x = x[:-1]
            y = y[:-1]
        cell_size /= min(cell_sizes)
        plt.semilogy(x, y, 'o-', label=f'{cell_size:.1f}')

    ax.set_ylabel(r'$|\Delta\varepsilon_{HOMO}|$ (eV)')
    ax.set_xlabel('energy cutoff (Ha)')

    ax.legend(title='cell size', ncol=2)
    plt.tight_layout()
    plt.savefig('pbe_convergence_plot.png', facecolor=(1,1,1,0))
