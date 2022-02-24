# Hardware-efficient-MUA-compression
Code, study results and hardware designs for the hardware efficient compression of threshold-crossing neural MUA signals via Machine-Learning selected static Huffman encoders.

Article located at:

Results and data (neural data .mat files) located at:


## Code to recreate results:

### BR results:
Run “Compressing data/get_BR_approx_sort.py”  to produce the approx. sort BR results

Run “Compressing data/get_BR_no_sort.py” to produce the no sort BR results.

### BDP results:
Run “Behavioral decoding/HPC code/Flint_HPC_BDP_S_test.pbs”, “…Flint_HPC_BDP_S_train.pbs”, “…Sabes_HPC_BDP_S_test.pbs”, “…Sabes_HPC_BDP_S_train.pbs” (designed as HPC .pbs BASH scripts that call the Python functions [in .py files of the same name as .pbs files] as array jobs)

Download the results (.pkl files) to Results directory, in e.g. “Results\BDP_results\results_Flint_train” directory. 

Run "analyse_BDP_S_pkl.py" to analyze the (hyper-)parameter optimization results and to save the optimized BDP vs. S and BP results in .pkl files for easy access.

### Hardware power consumption and resources results:
See "FPGA implementation" directory README file.


## Code to analyze complete results:
After BR, BDP and hardware results have been re-produced, one can integrate the results to further analyse them.

### To integrate results into the same excel spreadsheet:
Run “integrate_BR_and_BDP_results_into_excel.py” to add the BR and BDP results to the excel template.

One has to manually add the hardware processing power and resource consumption results into the excel.


### Plots:
To plot 3d, colored scatter plots (BDP vs. Dynamic Power vs. Resources vs. BP/BDTP), run “Analyse results/plot_3d_color_scatter_plot_BDP_BP_resources_power.py”.

To do the permutation p-value test for the number of channels that can fit on an implant, run “Analyse results/max_nb_channels_p_value_power_budget.py”

