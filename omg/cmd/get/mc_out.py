from tabulate import tabulate

from omg.common.helper import age

def mc_out(t, ns, res, output, show_type):
    output_res=[]
    # header
    header = ['NAME','GENERATEDBYCONTROLLER','IGNITIONVERSION','AGE']
    # resources
    for r in res:
        mc = r['res']
        row = []
        # name
        if show_type:
            row.append(t + '/' + mc['metadata']['name'])
        else:
            row.append(mc['metadata']['name'])

        # generated by cont.
        try: 
            gen_by = mc['metadata']['annotations']['machineconfiguration.openshift.io/generated-by-controller-version']
        except:
            gen_by = ''
        row.append(gen_by)
        # ignition ver
        i_ver = mc['spec']['config']['ignition']['version']
        row.append(i_ver)
        # age
        try:
            ct = mc['metadata']['creationTimestamp']
            ts = r['gen_ts']
            row.append(age(ct,ts))
        except:
            row.append('Unknown')

        output_res.append(row)

    #print(tabulate(output_res,tablefmt="plain"))
    # sort by 1st column (name)
    sorted_output = sorted(output_res, key=lambda x: x[0])
    sorted_output.insert(0,header)

    print(tabulate(sorted_output,tablefmt="plain"))