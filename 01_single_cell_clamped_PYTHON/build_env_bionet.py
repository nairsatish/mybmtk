from bmtk.utils.sim_setup import build_env_bionet
build_env_bionet(network_dir='network', tstop=2000.0, dt=0.1,
                 reports={'membrane_report': {
                         "module": "membrane_report",
                         'cells': 'all',
                         'variable_name': ['cai', 'v'],
                         "file_name": "cell_vars.h5",
                         "sections": "soma",
                     }})
					 
"""this creates standard SONATA configuration files for BioNet, using the built network files 
in ./network and having a simulation run-time of 2 seconds. The membrane_report-vars and 
membrane_report-sections sets it so that we are recording membrane potential (v) and calcium 
concentration (cai) at the soma.:
NOW FROM BASH copy the following json files:
%%bash
cp sources/bionet_files/components/biophysical/electrophysiology/472363762_fit.json biophys_components/biophysical_neuron_templates/
cp sources/bionet_files/components/biophysical/morphology/Scnn1a_473845048_m.swc biophys_components/morphologies/
"""