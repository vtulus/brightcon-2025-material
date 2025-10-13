
import bw2data as bd
import bw2io as bi

NAME_PROJECT='workshop-bw25'

#Open a brightway project associated with the project name chosen
bd.projects.set_current(NAME_PROJECT)

bi.import_ecoinvent_release(
        version="3.10.1",
        system_model="cutoff",
        use_mp=True
        #username="XX",
        #password="yy"
        )

# For those that have a valid ecoinvent license, you can simply restore a project with:

# bi.restore_project_directory("/srv/data/brightway2-project-workshop-bw25-backup13-October-2025-05-30PM.tar.gz", overwrite_existing=True)

