
import bw2data as bd
import bw2io as bi

NAME_PROJECT='workshop-bw25'

#Open a brightway project associated with the project name chosen
bd.projects.set_current(NAME_PROJECT)

bi.import_ecoinvent_release(
        version="3.10.1",
        system_model="cutoff",
        use_mp=True)