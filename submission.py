from hepdata_lib import Submission
from hepdata_lib import RootFileReader
from hepdata_lib import Table
from hepdata_lib import Variable, Uncertainty
import pickle
import numpy as np

def fig2a():

    #2a
    table                           = Table("Figure 2a")
    table.description               = "The MJY distribution for the number of observed events (black markers) compared with the estimated backgrounds (filled histograms) in the signal region 1. The distributions expected from the signal under three MX and MY hypotheses and assuming a cross section of 1 fb are also shown."
    table.location                  = "Data from Figure 2 (left)"
    table.keywords["observables"]   = ["MJY"]
    table.add_image("inputs/Figures/TT_MJY.pdf")

    reader                  = RootFileReader("test_TT.root")

    TotalBackground         = reader.read_hist_1d("totalbkg_projx")
    TT                      = reader.read_hist_1d("ttbar_projx")
    QCD                     = reader.read_hist_1d("qcd_projx")
    Data                    = reader.read_hist_1d("data_projx")
    Sig1                    = reader.read_hist_1d("MX1600_MY150_TT_projx")
    Sig2                    = reader.read_hist_1d("MX2000_MY300_TT_projx")
    Sig3                    = reader.read_hist_1d("MX3000_MY400_TT_projx")

    # x-axis: Y mass
    mjy                     = Variable("$M_{J}^{Y}$", is_independent=True, is_binned=False, units="GeV")
    mjy.values              = Data["x"]
    # y-axis: N events
    totalbackground         = Variable("Number of background events", is_independent=False, is_binned=False, units="")
    totalbackground.values  = TotalBackground["y"]

    tt                  = Variable("Number of ttbar events", is_independent=False, is_binned=False, units="")
    qcd                 = Variable("Number of qcd events", is_independent=False, is_binned=False, units="")
    data                = Variable("Number of data events", is_independent=False, is_binned=False, units="")
    sig1                = Variable("Number of MX1600_MY150 signal events", is_independent=False, is_binned=False, units="")
    sig2                = Variable("Number of MX2000_MY300 signal events", is_independent=False, is_binned=False, units="")
    sig3                = Variable("Number of MX3000_MY400 signal events", is_independent=False, is_binned=False, units="")
    tt.values           = TT["y"]
    qcd.values          = QCD["y"]
    data.values         = Data["y"]
    sig1.values         = Sig1["y"]
    sig2.values         = Sig2["y"]
    sig3.values         = Sig3["y"]

    unc_totalbackground = Uncertainty("total uncertainty", is_symmetric=True)
    unc_data            = Uncertainty("Poisson errors", is_symmetric=False)
    unc_totalbackground.values = TotalBackground["dy"]
    unc_data.values     = Data["dy"]

    totalbackground.add_uncertainty(unc_totalbackground)
    data.add_uncertainty(unc_data)

    table.add_variable(mjy)
    table.add_variable(totalbackground)
    table.add_variable(tt)
    table.add_variable(qcd)
    table.add_variable(data)
    table.add_variable(sig1)
    table.add_variable(sig2)
    table.add_variable(sig3)
    return table

def fig2b():
    #2b
    table                           = Table("Figure 2b")
    table.description               = "The MJJ distribution for the number of observed events (black markers) compared with the estimated backgrounds (filled histograms) in the signal region 1. The distributions expected from the signal under three MX and MY hypotheses and assuming a cross section of 1 fb are also shown."
    table.location                  = "Data from Figure 2 (right)"
    table.keywords["observables"]   = ["MJJ"]
    table.add_image("inputs/Figures/TT_MJJ.pdf")

    reader                  = RootFileReader("test_TT.root")

    TotalBackground         = reader.read_hist_1d("totalbkg_projy")
    TT                      = reader.read_hist_1d("ttbar_projy")
    QCD                     = reader.read_hist_1d("qcd_projy")
    Data                    = reader.read_hist_1d("data_projy")
    Sig1                    = reader.read_hist_1d("MX1600_MY150_TT_projy")
    Sig2                    = reader.read_hist_1d("MX2000_MY300_TT_projy")
    Sig3                    = reader.read_hist_1d("MX3000_MY400_TT_projy")

    # x-axis: Y mass
    mjj                     = Variable("$M_{JJ}$", is_independent=True, is_binned=False, units="GeV")
    mjj.values              = Data["x"]
    # y-axis: N events
    totalbackground         = Variable("Number of background events", is_independent=False, is_binned=False, units="")
    totalbackground.values  = TotalBackground["y"]

    tt                  = Variable("Number of ttbar events", is_independent=False, is_binned=False, units="")
    qcd                 = Variable("Number of qcd events", is_independent=False, is_binned=False, units="")
    data                = Variable("Number of data events", is_independent=False, is_binned=False, units="")
    sig1                = Variable("Number of MX1600_MY150 signal events", is_independent=False, is_binned=False, units="")
    sig2                = Variable("Number of MX2000_MY300 signal events", is_independent=False, is_binned=False, units="")
    sig3                = Variable("Number of MX3000_MY400 signal events", is_independent=False, is_binned=False, units="")
    tt.values           = TT["y"]
    qcd.values          = QCD["y"]
    data.values         = Data["y"]
    sig1.values         = Sig1["y"]
    sig2.values         = Sig2["y"]
    sig3.values         = Sig3["y"]

    unc_totalbackground = Uncertainty("total uncertainty", is_symmetric=True)
    unc_data            = Uncertainty("Poisson errors", is_symmetric=False)
    unc_totalbackground.values = TotalBackground["dy"]
    unc_data.values     = Data["dy"]

    totalbackground.add_uncertainty(unc_totalbackground)
    data.add_uncertainty(unc_data)

    table.add_variable(mjj)
    table.add_variable(totalbackground)
    table.add_variable(tt)
    table.add_variable(qcd)
    table.add_variable(data)
    table.add_variable(sig1)
    table.add_variable(sig2)
    table.add_variable(sig3)
    return table

def fig3():
    table                           = Table("Figure 3")
    table.description               = "The 95% confidence level expected and observed upper limits on signal cross-section for different values of MX and MY. Logarithmic interpolation is used between the tabulated values to plot the limits on a finer grid."
    table.location                  = "Data from Figure 3"
    table.keywords["observables"]   = ["MX","MY"]
    table.add_image("inputs/Figures/2d_obs_limits.pdf")
    table.add_image("inputs/Figures/2d_exp_limits.pdf")

    with open('forHepData.pkl', 'rb') as handle:
        myData = pickle.load(handle)
        limits = myData["limits"]
        limits = np.array(limits)

        # x-axis: MX
        mx              = Variable("$M_{X}$", is_independent=True, is_binned=False, units="GeV")
        my              = Variable("$M_{Y}$", is_independent=True, is_binned=False, units="GeV")
        exp             = Variable("Expected exclusion limit", is_independent=False, is_binned=False, units="fb")
        obs             = Variable("Observed exclusion limit", is_independent=False, is_binned=False, units="fb")

        mx.values       = limits[:,0]
        my.values       = limits[:,1]
        exp.values      = limits[:,4]
        obs.values      = limits[:,7]

        exp1s           = limits[:,[3,5]]
        exp2s           = limits[:,[2,6]]

        # +/- 1 sigma
        unc_1s = Uncertainty("1$\sigma$", is_symmetric=False)
        unc_1s.set_values_from_intervals((exp1s), nominal=exp.values)
        exp.add_uncertainty(unc_1s)

        # +/- 2 sigma
        unc_2s = Uncertainty("2$\sigma$", is_symmetric=False)
        unc_2s.set_values_from_intervals((exp2s), nominal=exp.values)
        exp.add_uncertainty(unc_2s)

        table.add_variable(mx)
        table.add_variable(my)
        table.add_variable(obs)
        table.add_variable(exp)

        return table


submission = Submission()

table2a = fig2a()
table2b = fig2b()
table3    = fig3()

submission.add_table(table2a)
submission.add_table(table2b)
submission.add_table(table3)
submission.create_files("example_output",remove_old=True)

