from bmtk.analyzer.spike_trains import to_dataframe
print(to_dataframe(config_file='simulation_config.json'))

from bmtk.analyzer.cell_vars import plot_report

plot_report(config_file='simulation_config.json')
