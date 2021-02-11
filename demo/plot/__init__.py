from demo.plot import elements
from demo.plot import utils

from myterial import grey_darker, grey_dark
from  matplotlib import rc

# set latex
# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Times-Roman']})
# rc('text', usetex = True)

# set axes style
rc('text', color=grey_dark)
rc('axes', edgecolor=grey_dark, linewidth=2, labelcolor=grey_darker, 
    labelweight='bold', labelsize='larger', labelpad=8,
    titlesize=12, axisbelow=True, ymargin=0.01,
    )
rc('xtick', color=grey_dark, labelsize='large', )
rc('xtick.major', size=8, width=2)
rc('figure', titleweight='bold', titlesize=16)
