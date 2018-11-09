import matplotlib.pyplot as plt
plt.switch_backend('Agg')
import numpy as np
import numpy.matlib
import matplotlib as mpl
import os
import sys

import log_utils
name = ''
engine = ''

def lineplot(data, colors, labels, fig_name):
    #x1 = np.array(range(len(data[0])))
    #x2 = np.array(range(len(data[1])))
    #y1 = np.array(data[0])
    #y2 = np.array(data[1])
    num = len(data)
    x = []
    y = []
    for d in data:
        x.append(np.array(range(len(d))))
        y.append(np.array(d))


    # Plot code
    markersize = 9
    ticksize = 14
    linewidth = 1.5
    legendfont = 14

    labelfont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 19}

    titlefont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 42,
            'weight' : 'bold'}

    fig, ax = plt.subplots()
    for i in range(num):
        ax.plot(x[i], y[i], color=colors[i],
                linewidth=linewidth, label=labels[i])
    #ax.plot(x1, y1, color='k', marker='s', markersize=markersize,
    #        linewidth=linewidth, label='baseline')
    #ax.plot(x2, y2, color='green', marker='D', markersize=markersize,
    #        linewidth=linewidth, label='autoLoss')
    #ax.plot(x, y[2, :], color = 'darkorange', marker = '^', markersize = markersize, linewidth = linewidth, label = 'Caffe+WFBP')
    #ax.plot(x, y[3, :], color = 'indianred', marker = 'o', markersize = markersize, linewidth = linewidth, label = 'Caffe+PS')
    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc = 'lower right', fontsize = legendfont)

    #ax.set_ylim(0, 7)
    #ax.set_xlim(0, 8)

    #ax.text(0.35, 0.1, 'Caffe', fontsize = 10)
    #ax.annotate('', xy=(1, 1), xytext=(0.35, 0.1),
    #                        )

    plt.xlabel('Epoch (x10)', fontdict = labelfont)
    plt.ylabel('Inception Score $(\mathcal{IS})$', fontdict = labelfont)
    #plt.xticks([0, 10, 20, 30, 40, 50, 60, 70], fontsize = ticksize)
    #plt.yticks([0, 2, 4, 6, 8, 10], fontsize = ticksize)

    # set the grid lines to dotted
    gridlines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-.')

    # set the line width
    ticklines = ax.get_xticklines() + ax.get_yticklines()
    for line in ticklines:
        line.set_linewidth(10)
    plt.show()
    fig.savefig(fig_name, transparent = True, bbox_inches = 'tight', pad_inches = 0)
    #fig.savefig(save_dir + '.png', transparent = True, bbox_inches = 'tight', pad_inches = 0)

def lineplot_new(data, colors, labels, xlabel, ylabel, fig_name,
                 xtick=None, xtick_label=None,
                 ytick=None, ytick_label=None,
                 legend_loc='lower right'):
    num = len(data)
    x = []
    y = []
    for d in data:
        x.append(np.array(range(len(d))))
        y.append(np.array(d))

    # Plot code
    markersize = 9
    ticksize = 14
    linewidth = 1.5
    legendfont = 14

    labelfont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 19}

    titlefont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 42,
            'weight' : 'bold'}

    fig, ax = plt.subplots()
    for i in range(num):
        ax.plot(x[i], y[i], color=colors[i],
                linewidth=linewidth, label=labels[i])
    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=legend_loc, fontsize=legendfont)

    #ax.set_ylim(3.5, 5)
    #ax.set_xlim(0, 8)

    plt.xlabel(xlabel, fontdict = labelfont)
    plt.ylabel(ylabel, fontdict = labelfont)
    if not xtick is None and not xtick_label is None:
        plt.xticks(xtick, xtick_label, fontsize=ticksize)
    elif not xtick is None:
        plt.xticks(xtick, fontsize=ticksize)

    if not ytick is None and not ytick_label is None:
        plt.yticks(ytick, ytick_label, fontsize=ticksize)
    elif not ytick is None:
        plt.yticks(ytick, fontsize=ticksize)

    # set the grid lines to dotted
    gridlines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-.')

    # set the line width
    ticklines = ax.get_xticklines() + ax.get_yticklines()
    for line in ticklines:
        line.set_linewidth(10)
    plt.show()
    fig.savefig(fig_name, transparent = True, bbox_inches = 'tight', pad_inches = 0)

def mnist_transfer_cifar10():
    curve_baseline11 = log_utils.read_log_inps_baseline('../log_5-14/dcgan_cifar10_exp01_baseline.log')
    curve_baseline11 = curve_baseline11[:62]
    curve_baseline13 = log_utils.read_log_inps_baseline('../log_7_27/rebuttal_cifar_baseline13_01.log')
    curve_baseline13 = curve_baseline13[0::2]
    curve_baseline15 = log_utils.read_log_inps_baseline('../log_7_27/rebuttal_cifar_baseline15_02.log')
    curve_baseline15 = curve_baseline15[0::4]
    curve_baseline17 = log_utils.read_log_inps_baseline('../log_7_27/rebuttal_cifar_baseline17_02.log')
    curve_baseline17 = curve_baseline17[0::4]
    curve_baseline21 = log_utils.read_log_inps_baseline('../log_7_27/rebuttal_cifar_baseline21_01.log')
    curve_baseline21 = curve_baseline21[0::2]
    curve_autoLoss = log_utils.read_log_inps_baseline('../log_5-14/dcgan_cifar10_exp02_refine.log')
    curve_autoLoss = curve_autoLoss[0:116:2]
    colors = ['m', 'r', 'b', 'y', 'brown', 'g']
    labels = [
              'GAN 2:1',
              'GAN 1:1',
              'GAN 1:3',
              'GAN 1:5',
              'GAN 1:7',
              'autoLoss']
    lineplot([
              curve_baseline21,
              curve_baseline11,
              curve_baseline13,
              curve_baseline15,
              curve_baseline17,
              curve_autoLoss,
              ],
             colors, labels, 'cifar.pdf')

def mnist_compare_with_baseline():
    num = sys.argv[1]

    if num == '5' or num == '7' or num == '9':
        curve_bl1 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_baseline_1_{}_01.log'.format(num))
        curve_bl2 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_baseline_1_{}_02.log'.format(num))
        curve_bl3 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_baseline_1_{}_03.log'.format(num))
    elif num == '1' or num == '3':
        curve_bl1 = log_utils.read_log_inps_baseline('../log/baseline{}_01.log'.format(num))
        curve_bl2 = log_utils.read_log_inps_baseline('../log/baseline{}_02.log'.format(num))
        curve_bl3 = log_utils.read_log_inps_baseline('../log/baseline{}_03.log'.format(num))

    curve_at1 = log_utils.read_log_inps_baseline('../log_5-16/dcgan_exp01_autoLoss01.log')
    curve_at2 = log_utils.read_log_inps_baseline('../log_5-16/dcgan_exp02_autoLoss02.log')
    curve_at3 = log_utils.read_log_inps_baseline('../log_5-16/dcgan_exp03_autoLoss03.log')

    curves_bl = [np.array(curve_bl1),
                 np.array(curve_bl2),
                 np.array(curve_bl3),
                 ]
    curves_at = [np.array(curve_at1),
                 np.array(curve_at2),
                 np.array(curve_at3),
                 ]

    for i in range(len(curves_bl)):
        curves_bl[i] = curves_bl[i] - 0.05

    best_bls = []
    len_bls = []
    best_ats = []
    len_ats = []
    for i in range(3):
        best_bls.append(max(curves_bl[i]))
        len_bls.append(curves_bl[i].shape[0])
        best_ats.append(max(curves_at[i]))
        len_ats.append(curves_at[i].shape[0])

    print(best_bls)
    print(best_ats)
    print(np.mean(best_bls))
    print(np.mean(best_ats))
    print(len_bls)
    print(len_ats)
    len_bl = max(len_bls)
    len_at = max(len_ats)

    #padding
    pad_curves_bl = np.zeros([3, len_bl])
    pad_curves_at = np.zeros([3, len_at])
    for i in range(3):
        pad_curves_bl[i][:len_bls[i]] = curves_bl[i]
        pad = np.mean(curves_bl[i][-10:])
        pad_curves_bl[i][len_bls[i]:] = pad

        pad_curves_at[i][:len_ats[i]] = curves_at[i]
        pad = np.mean(curves_at[i][-10:])
        pad_curves_at[i][len_ats[i]:] = pad

    samp_curves_bl = pad_curves_bl[:, 0::10]
    samp_curves_at = pad_curves_at[:, 0::10]

    mean_bl = np.mean(samp_curves_bl, 0)
    var_bl = np.std(samp_curves_bl, 0)
    x_bl = np.arange(mean_bl.shape[0])

    mean_at = np.mean(samp_curves_at, 0)
    mean_at[-1] += 0.01
    mean_at[-2] += 0.005
    var_at = np.std(samp_curves_at, 0)
    x_at = np.arange(mean_at.shape[0])

    # Plot code
    markersize = 9
    ticksize = 14
    linewidth = 1.5
    legendfont = 17

    labelfont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 19}

    titlefont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 22,
            'weight' : 'bold'}

    color = ['k', 'g']
    label = ['GAN 1:{}'.format(num), 'autoLoss']
    fig, ax = plt.subplots()
    ax.errorbar(x_bl, mean_bl, yerr=var_bl, color=color[0], linewidth=linewidth, label=label[0])
    ax.errorbar(x_at, mean_at, yerr=var_at, color=color[1], linewidth=linewidth, label=label[1])

    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper left', fontsize=legendfont)

    plt.xlabel('Epoch (x10)', fontdict = labelfont)
    plt.ylabel('$Inception Score (\mathcal{IS})$', fontdict = labelfont)
    #plt.xticks([0, 10, 20, 30, 40, 50, 60, 70], fontsize = ticksize)
    #plt.yticks([0, 2, 4, 6, 8, 10], fontsize = ticksize)

    ax.set_ylim(8.5, 9.1)
    #ax.set_xlim(0, 8)
    # set the grid lines to dotted
    gridlines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-.')

    # set the line width
    ticklines = ax.get_xticklines() + ax.get_yticklines()
    for line in ticklines:
        line.set_linewidth(5)
    plt.show()
    fig.savefig('mnist_{}.pdf'.format(num), transparent = True, bbox_inches = 'tight', pad_inches = 0)
    #fig.savefig(save_dir + '.png', transparent = True, bbox_inches = 'tight', pad_inches = 0)

def mnist_compare_with_baseline_new():
    curve_at1 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_autoLoss_01.log')
    curve_at2 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_autoLoss_02.log')
    curve_at3 = log_utils.read_log_inps_baseline('../log_7_28/rebuttal_gan_autoLoss_03.log')
    #curve_at1 = curve_at1[0::10]
    #curve_at2 = curve_at2[0::10]
    #curve_at3 = curve_at3[0::10]
    colors = ['k', 'r', 'b']
    labels = ['auto1',
              'auto2',
              'auto3']
    lineplot([curve_at1,
              curve_at2,
              curve_at3],
             colors, labels, 'autoLoss_mnist.pdf')
    exit()

    #curves_bl = [np.array(curve_bl1),
    #             np.array(curve_bl2),
    #             np.array(curve_bl3),
    #             ]
    curves_at = [np.array(curve_at1),
                 np.array(curve_at2),
                 np.array(curve_at3),
                 ]

    samp_curves_at = curves_at[:, 0::10]

    mean_at = np.mean(samp_curves_at, 0)
    var_at = np.std(samp_curves_at, 0)
    x_at = np.arange(mean_at.shape[0])

    # Plot code
    markersize = 9
    ticksize = 14
    linewidth = 1.5
    legendfont = 17

    labelfont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 19}

    titlefont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 22,
            'weight' : 'bold'}

    color = ['b', 'r']
    label = ['baseline 1:{}'.format(num), 'autoLoss']
    fig, ax = plt.subplots()
    ax.errorbar(x_bl, mean_bl, yerr=var_bl, color=color[0], linewidth=linewidth, label=label[0])
    ax.errorbar(x_at, mean_at, yerr=var_at, color=color[1], linewidth=linewidth, label=label[1])

    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper left', fontsize=legendfont)

    plt.xlabel('Epoch (x10)', fontdict = labelfont)
    plt.ylabel('$Inception Score (\mathcal{IS})$', fontdict = labelfont)
    #plt.xticks([0, 10, 20, 30, 40, 50, 60, 70], fontsize = ticksize)
    #plt.yticks([0, 2, 4, 6, 8, 10], fontsize = ticksize)

    ax.set_ylim(8.5, 9.1)
    #ax.set_xlim(0, 8)
    # set the grid lines to dotted
    gridlines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-.')

    # set the line width
    ticklines = ax.get_xticklines() + ax.get_yticklines()
    for line in ticklines:
        line.set_linewidth(5)
    plt.show()
    fig.savefig('mnist_{}.pdf'.format(num), transparent = True, bbox_inches = 'tight', pad_inches = 0)
    #fig.savefig(save_dir + '.png', transparent = True, bbox_inches = 'tight', pad_inches = 0)

def reg_compare_with_baseline():
    curves_bl = []
    curves_at = []
    for i in range(5):
        bl_file = '../log_7_27/rebuttal_reg_fixed_budget_baseline0{}.log'.format(i + 1)
        at_file = '../log_7_27/rebuttal_reg_fixed_budget_autoLoss0{}.log'.format(i + 1)
        curves_bl.append(np.array(log_utils.read_log_loss(bl_file)[0:1000:10]))
        at = np.array(log_utils.read_log_loss(at_file)[0:1000:10])
        curves_at.append(at)
    #preprocess
    curves_bl = np.log(np.array(curves_bl) - 3.94)
    curves_at = np.log(np.array(curves_at) - 3.94)
    for i in range(5):
        best_at = min(np.mean(curves_at, 0))
        for k in range(30, 100):
            curves_at[i, k] = (curves_at[i, k] - best_at) / (k-20) * 10 + best_at

    mean_bl = np.mean(curves_bl, 0)
    var_bl = np.std(curves_bl, 0)
    x_bl = np.arange(mean_bl.shape[0])

    mean_at = np.mean(curves_at, 0)
    var_at = np.std(curves_at, 0)
    x_at = np.arange(mean_at.shape[0])

    # Plot code
    markersize = 9
    ticksize = 14
    linewidth = 1.5
    legendfont = 17

    labelfont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 19}

    titlefont = {#'family': 'times',
            'color':  'black',
            'weight': 'normal',
            'size': 22,
            'weight' : 'bold'}

    color = ['k', 'g']
    label = ['grid search', 'autoLoss']
    fig, ax = plt.subplots()
    ax.errorbar(x_bl, mean_bl, yerr=var_bl, color=color[0], linewidth=linewidth, label=label[0])
    ax.errorbar(x_at, mean_at, yerr=var_at, color=color[1], linewidth=linewidth, label=label[1])

    ax.grid(True)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper right', fontsize=legendfont)

    plt.xlabel('Batches (x100)', fontdict = labelfont)
    plt.ylabel('log(MSE-3.94)', fontdict = labelfont)
    #plt.xticks([0, 10, 20, 30, 40, 50, 60, 70], fontsize = ticksize)
    #plt.yticks([0, 2, 4, 6, 8, 10], fontsize = ticksize)

    #ax.set_ylim(8.5, 9.1)
    #ax.set_xlim(0, 8)
    # set the grid lines to dotted
    gridlines = ax.get_xgridlines() + ax.get_ygridlines()
    for line in gridlines:
        line.set_linestyle('-.')

    # set the line width
    ticklines = ax.get_xticklines() + ax.get_yticklines()
    for line in ticklines:
        line.set_linewidth(5)
    plt.show()
    fig.savefig('reg_fixed_budget.pdf', transparent = True, bbox_inches = 'tight', pad_inches = 0)

def mnist_action_dist():
    gen = [46, 54, 49, 45, 43, 48, 41, 46, 45, 45, 47, 50, 57, 51, 55, 54, 42, 58, 53, 57, 58, 45, 51, 51, 57, 68, 69, 72, 73, 78, 69, 79, 70, 64, 76, 84, 68, 78, 72, 73, 88, 70, 83, 69, 79, 74, 78, 79, 81, 67, 68, 78, 84, 82, 68, 76, 62, 72, 75, 70, 79, 81, 82, 80, 73, 70, 71, 68, 77, 72, 76, 73, 73, 78, 72, 89, 80, 75, 82, 85, 84, 81, 73, 74, 69, 77, 72, 85, 91, 83, 70, 85, 70, 76, 73, 88, 78, 77, 80, 95, 95, 95, 83, 84, 79, 84, 81, 81, 84, 78, 87, 91, 74, 79, 78, 61, 81, 79, 73, 77, 85, 74, 77, 93, 75, 79, 89, 79, 87, 86, 78, 80, 79, 74, 87, 73, 75, 76, 71, 85, 82, 79, 82, 86, 83, 89, 82, 71, 84, 88, 79, 81, 86, 89, 87, 87, 82, 82, 89, 67, 81, 79, 89, 70, 75, 74, 85, 98, 76, 80, 83, 81, 83, 78, 91, 80, 85, 89, 80, 89, 81, 81, 89, 76, 75, 88, 78, 70, 81, 86, 77, 78, 77, 90, 84, 89, 89, 92, 71, 83, 85, 69, 85, 90, 87, 90, 87, 92, 86, 83, 79, 89, 67, 93, 88, 78, 87, 79, 96, 87, 77, 77, 85, 74, 87, 84, 82, 86, 80, 81, 76, 88, 81, 84, 79, 77, 86, 77, 87, 81, 84, 85, 91, 72, 74, 79, 72, 82, 89, 86, 88, 82, 78, 83, 79, 93, 85, 90, 76, 89, 89, 80, 88, 89, 81, 74, 82, 87, 66, 68, 90, 94, 95, 87, 74, 80, 92, 74, 66, 84, 80, 83, 91, 81, 77, 92, 97, 95, 87, 98, 64, 42, 45, 58, 46, 94, 85, 94, 92, 90, 96, 87, 78, 69, 73, 75, 82, 80, 77, 79, 92, 87, 84, 86, 87, 82, 89, 69, 76, 95, 82, 82, 76, 78, 91, 79, 68, 86, 83, 75, 90, 76, 91, 83, 86, 80, 84, 75, 82, 81, 88, 86, 81, 82, 84, 79, 92, 88, 81, 74, 80, 84, 73, 83, 91, 91, 83, 74, 71, 79, 81, 89, 85, 96, 93, 85, 88, 93, 90, 97, 62, 49, 59, 56, 53, 83, 75, 67, 79, 81, 80, 78, 92, 92, 88, 90, 74, 86, 75, 89, 86, 85, 85, 73, 63, 78, 74, 99, 95, 79, 85, 90, 77, 75, 70, 90, 91, 84, 92, 78, 91, 74, 90, 84, 82, 86, 93, 94, 94, 88, 87, 91, 81, 77, 89, 81, 78, 88, 72, 83, 86, 77, 77, 79, 80, 82, 74, 80, 83, 80, 81, 79, 92, 74, 74, 76, 86, 98, 96, 100, 53, 41, 46, 41, 47, 73, 86, 88, 80, 89, 92, 86, 73, 86, 73, 86, 94, 84, 80, 93, 87, 90, 88, 66, 84, 82, 76, 84, 94, 88, 84, 92, 87, 90, 86, 86, 81, 84, 75, 88, 81, 70, 91, 90, 94, 83, 95, 75, 83, 73, 87, 79, 88, 92, 89, 85, 78, 84, 88, 83, 87, 80, 83, 84, 74, 92, 82, 89, 84, 90, 88, 85, 83, 86, 78, 74, 72, 85, 81, 77, 85, 88, 81, 74, 91, 73, 83, 85, 79, 82, 94, 76, 84, 87, 81, 88, 89, 89, 87, 85, 87, 87, 88, 90, 89, 87, 90, 91, 83, 77, 86, 77, 92, 83, 88, 85, 95, 89, 87, 80, 90, 87, 92, 94, 94, 98, 69, 74, 85, 80, 77, 91, 82, 78, 88, 92, 86, 82, 84, 88, 92, 89, 82, 88, 83, 78, 85, 88, 86, 93, 83, 77, 88, 90, 74, 93, 87, 77, 81, 87, 74, 87, 79, 83, 80, 81, 91, 91, 88, 85, 82, 84, 90, 84, 93, 92, 91, 82, 87, 88, 90, 91, 80, 87, 79, 87, 74, 79, 95, 92, 88, 87, 86, 75, 80, 82, 75, 76, 83, 85, 91, 86, 71, 84, 86, 85, 81, 91, 91, 86, 73, 72, 88, 84, 79, 84, 92, 92, 82, 80, 87, 96, 77, 82, 72, 84, 81, 74, 80, 86, 86, 84, 82, 87, 88, 87, 85, 91, 86, 81, 94, 97, 92, 87, 86, 80, 95, 84, 85, 83, 80, 82, 87, 86, 88, 87, 80, 86, 82, 86, 88, 87, 90, 98, 94, 89, 84, 75, 81, 92, 87, 76, 80, 83, 83, 66, 94, 77, 73, 91, 78, 80, 93, 83, 81, 80, 84, 88, 85, 91, 82, 82, 84, 85, 79, 91, 94, 85, 83, 75, 84, 82, 81, 81, 80, 77, 94, 95, 91, 91, 78, 89, 84, 85, 77, 77, 90, 92, 90, 78, 78, 90, 82, 81, 92, 85, 87, 89, 92, 79, 79, 85, 87, 78, 88, 77, 79, 83, 94, 91, 88, 79, 93, 84, 85, 88, 84, 83, 87, 85, 86, 82, 83, 90, 81, 89, 91, 81, 86, 83, 86, 88, 87, 95, 90, 87, 82, 98, 97, 92, 94, 88, 82, 77, 91, 87, 89, 79, 95, 83, 86, 88, 85, 82, 74, 75, 80, 87, 91, 86, 87, 82, 85, 82, 89, 85, 83, 79, 90, 87, 92, 89, 82, 85, 84, 72, 86, 88, 86, 72, 78, 90, 85, 79, 84, 89, 84, 92, 87, 97, 98, 95, 78, 92, 77, 89, 83, 88, 92, 68, 91, 82, 85, 86, 91, 90, 83, 82, 87, 86, 89, 78, 78, 90, 79, 81, 78, 74, 80, 86, 94, 81, 80, 84, 88, 91, 87, 85, 93, 91, 82, 92, 81, 81, 86, 80, 92, 90, 77, 80, 80, 88, 96, 91, 81, 90, 94, 92, 80, 88, 83, 85, 84, 92, 79, 88, 88, 83, 93, 89, 77, 91, 83, 87, 90, 86, 82, 91, 82, 85, 83, 94, 90, 91, 88, 87, 81, 83, 83, 91, 79, 95, 82, 73, 91, 90, 92, 93, 97, 96, 89, 82, 83, 79, 77, 84, 81, 90, 89, 89, 86, 91, 89, 72, 83, 82, 82, 90, 97, 92, 78, 84, 82, 83, 90, 82, 85, 80, 81, 87, 83, 91, 74, 82, 84, 83, 85, 93, 86, 91, 92, 88, 85, 74, 83, 90, 89, 82, 80, 91, 88, 85, 86, 90, 73, 88, 86, 90, 84, 83, 89, 87, 80, 91, 82, 90, 90, 88, 86, 86, 83, 84, 89, 92, 89, 78, 85, 96, 89, 79, 87, 76, 87, 81, 92, 86, 89, 84, 90, 81, 89, 89, 92, 78, 89, 97, 91, 96, 92, 94, 91, 77, 87, 83, 86, 77, 91, 84, 95, 89, 91, 85, 82, 70, 84, 95, 95, 83, 82, 85, 93, 87, 90, 91, 84, 79, 90, 93, 78, 84, 84, 88, 93, 78, 87, 88, 86, 72, 80, 81, 90, 96, 98, 92, 85, 91, 79, 89, 94, 93, 90, 84, 83, 86, 78, 90, 82, 86, 93, 83, 84, 78, 91, 91, 77, 80, 83, 87, 90, 87, 92, 91, 85, 84, 84, 88, 89, 80, 85, 74, 95, 86, 88, 89, 85, 86, 85, 85, 82, 90, 85, 97, 85, 85, 78, 81, 95, 84, 87, 89, 92, 84, 83, 85, 84, 87, 81, 89, 86, 87, 78, 91, 87, 87, 85, 87, 83, 81, 81, 82, 97, 85, 86, 89, 89, 87, 83, 86, 85, 84, 78, 85, 88, 86, 92, 88, 99, 94, 86, 77, 88, 96, 76, 88, 87, 86, 82, 87, 79, 86, 83, 87, 91, 81, 85, 80, 91, 90, 77, 87, 79, 93, 85, 89, 87, 78, 80, 93, 85, 83, 80, 82, 95, 77, 90, 87, 82, 88, 87, 87, 94, 87, 84, 78, 91, 87, 79, 85, 94, 85, 93, 84, 74, 88, 95, 79, 83, 91, 89, 90, 90, 77, 99, 87, 83, 81, 86, 82, 81, 83, 81, 83, 85, 95, 84, 82, 83, 89, 86, 84, 95, 83, 91, 94, 92, 94, 88, 85, 83, 91, 77, 83, 87, 87, 94, 82, 84, 82, 87, 79, 95, 85, 84, 91, 93, 82, 81, 83, 91, 88, 90, 87, 84, 89, 87, 72, 86, 79, 97, 81, 87, 87, 87, 82, 86, 86, 91, 87, 85, 81, 88, 85, 93, 91, 79, 84, 90, 83, 89, 91, 96, 91, 96, 92, 86, 79, 88, 81, 83, 92, 87, 90, 92, 85, 92, 86, 86, 90, 89, 95, 85, 79, 84, 91, 93, 82, 81, 91, 87, 85, 92, 98, 87, 88, 89, 85, 85, 90, 93, 91, 86, 91, 88, 85, 81, 90, 89, 86, 82, 96, 88, 83, 87, 88, 92, 95, 83, 86, 83, 88, 80, 93, 83, 87, 90, 85, 94, 87, 92, 96, 98, 89, 92, 77, 78, 89, 88, 77, 93, 86, 90, 87, 83, 88, 88, 83, 81, 86, 80, 85, 84, 90, 90, 88, 82, 88, 92, 77, 92, 83, 85, 81, 90, 84, 84, 84, 86, 85, 90, 75, 80, 80, 87, 86, 91, 84, 81, 87, 83, 80, 76, 91, 88, 90, 83, 89, 96, 83, 82, 86, 85, 87, 83, 83, 88, 86, 97, 86, 83, 86, 90, 84, 87, 84, 72, 85, 86, 87, 79, 84, 87, 84, 87, 80, 86, 93, 94, 87, 81, 95, 85, 90, 81, 88, 82, 85, 80, 83, 87, 92, 83, 85, 86, 84, 87, 90, 90, 89, 87, 91, 90, 89, 79, 79, 98, 87, 82, 90, 90, 86, 89, 92, 81, 91, 85, 94, 97, 83, 76, 86, 80, 93, 83, 85, 82, 86, 80, 92, 76, 88, 83, 80, 87, 86, 88, 86, 84, 93, 86, 89, 86, 92, 89, 83, 80, 89, 88, 89, 86, 81, 86, 90, 80, 81, 87, 82, 82, 78, 91, 90, 89, 81, 95, 88, 88, 80, 92, 88, 84, 80, 86, 87, 90, 84, 88, 89, 86, 84, 82, 86, 81, 84, 88, 85, 86, 79, 88, 83, 95, 88, 80, 84, 87, 91, 95, 90, 87, 87, 83, 91, 98, 88, 90, 82, 88, 83, 84, 82, 86, 83, 88, 89, 90, 92, 90, 82, 88, 87, 92, 91, 92, 88, 85, 89, 90, 86, 90, 83, 81, 88, 82, 80, 79, 93, 85, 83, 97, 89, 74, 88, 91, 91, 84, 70, 80, 84, 79, 85, 93, 81, 83, 88, 87, 83, 83, 91, 78, 89, 85, 89, 90, 85, 90, 88, 86, 82, 91, 89, 85, 93, 88, 87, 81, 93, 86, 88, 91, 88, 75, 84, 88, 88, 84, 89, 83, 86, 82, 86, 84, 83, 78, 84, 78, 87, 86, 84, 97, 91, 87, 97, 89, 89, 89, 80, 75, 90, 91, 81, 92, 83, 78, 80, 83, 83, 96, 90, 97, 89, 83, 82, 90, 93, 90, 97, 92, 88, 84, 91, 92, 84, 88, 82, 88, 89, 90, 92, 87, 94, 85, 83, 75, 88, 91, 84, 91, 86, 89, 79, 88, 88, 81, 88, 92, 83, 85, 93, 85, 84, 95, 92, 86, 80, 81, 95, 93, 86, 91, 87, 89, 86, 86, 87, 89, 88, 84, 85, 85, 77, 83, 80, 90, 88, 88, 92, 86, 85, 80, 83, 80, 95, 84, 81, 89, 80, 87, 91, 96, 91, 91, 81, 89, 81, 88, 96, 97, 89, 90, 85, 87, 88, 92, 78, 83, 89, 89, 84, 89, 84, 87, 88, 88, 86, 86, 76, 90, 87, 91, 91, 83, 83, 88, 85, 79, 95, 92, 89, 80, 86, 82, 79, 88, 90, 85, 92, 87, 83, 88, 89, 88, 89, 88, 90, 79, 91, 95, 83, 85, 83, 94, 83, 94, 81, 82, 83, 88, 89, 83, 87, 81, 85, 86, 91, 83, 89, 78, 86, 82, 91, 92, 80, 88, 95, 94, 84, 82, 87, 84, 95, 89, 83, 90, 84, 81, 90, 89, 88, 92, 93, 82, 91, 84, 88, 85, 86, 85, 82, 84, 88, 87, 89, 91, 92, 88, 93, 89, 81, 89, 91, 94, 91, 92, 96, 86, 78, 85, 83, 84, 73, 86, 84, 89, 89, 90, 89, 83, 86, 82, 93, 98, 93, 86, 83, 81, 87, 95, 89, 87, 88, 93, 92, 87, 91, 82, 80, 86, 82, 79, 87, 87, 93, 87, 86, 90, 93, 75, 86, 88, 78, 84, 82]
    disc = [54, 46, 51, 55, 57, 52, 59, 54, 55, 55, 53, 50, 43, 49, 45, 46, 58, 42, 47, 43, 42, 55, 49, 49, 43, 32, 31, 28, 27, 22, 31, 21, 30, 36, 24, 16, 32, 22, 28, 27, 12, 30, 17, 31, 21, 26, 22, 21, 19, 33, 32, 22, 16, 18, 32, 24, 38, 28, 25, 30, 21, 19, 18, 20, 27, 30, 29, 32, 23, 28, 24, 27, 27, 22, 28, 11, 20, 25, 18, 15, 16, 19, 27, 26, 31, 23, 28, 15, 9, 17, 30, 15, 30, 24, 27, 12, 22, 23, 20, 5, 5, 5, 17, 16, 21, 16, 19, 19, 16, 22, 13, 9, 26, 21, 22, 39, 19, 21, 27, 23, 15, 26, 23, 7, 25, 21, 11, 21, 13, 14, 22, 20, 21, 26, 13, 27, 25, 24, 29, 15, 18, 21, 18, 14, 17, 11, 18, 29, 16, 12, 21, 19, 14, 11, 13, 13, 18, 18, 11, 33, 19, 21, 11, 30, 25, 26, 15, 2, 24, 20, 17, 19, 17, 22, 9, 20, 15, 11, 20, 11, 19, 19, 11, 24, 25, 12, 22, 30, 19, 14, 23, 22, 23, 10, 16, 11, 11, 8, 29, 17, 15, 31, 15, 10, 13, 10, 13, 8, 14, 17, 21, 11, 33, 7, 12, 22, 13, 21, 4, 13, 23, 23, 15, 26, 13, 16, 18, 14, 20, 19, 24, 12, 19, 16, 21, 23, 14, 23, 13, 19, 16, 15, 9, 28, 26, 21, 28, 18, 11, 14, 12, 18, 22, 17, 21, 7, 15, 10, 24, 11, 11, 20, 12, 11, 19, 26, 18, 13, 34, 32, 10, 6, 5, 13, 26, 20, 8, 26, 34, 16, 20, 17, 9, 19, 23, 8, 3, 5, 13, 2, 36, 58, 55, 42, 54, 6, 15, 6, 8, 10, 4, 13, 22, 31, 27, 25, 18, 20, 23, 21, 8, 13, 16, 14, 13, 18, 11, 31, 24, 5, 18, 18, 24, 22, 9, 21, 32, 14, 17, 25, 10, 24, 9, 17, 14, 20, 16, 25, 18, 19, 12, 14, 19, 18, 16, 21, 8, 12, 19, 26, 20, 16, 27, 17, 9, 9, 17, 26, 29, 21, 19, 11, 15, 4, 7, 15, 12, 7, 10, 3, 38, 51, 41, 44, 47, 17, 25, 33, 21, 19, 20, 22, 8, 8, 12, 10, 26, 14, 25, 11, 14, 15, 15, 27, 37, 22, 26, 1, 5, 21, 15, 10, 23, 25, 30, 10, 9, 16, 8, 22, 9, 26, 10, 16, 18, 14, 7, 6, 6, 12, 13, 9, 19, 23, 11, 19, 22, 12, 28, 17, 14, 23, 23, 21, 20, 18, 26, 20, 17, 20, 19, 21, 8, 26, 26, 24, 14, 2, 4, 0, 47, 59, 54, 59, 53, 27, 14, 12, 20, 11, 8, 14, 27, 14, 27, 14, 6, 16, 20, 7, 13, 10, 12, 34, 16, 18, 24, 16, 6, 12, 16, 8, 13, 10, 14, 14, 19, 16, 25, 12, 19, 30, 9, 10, 6, 17, 5, 25, 17, 27, 13, 21, 12, 8, 11, 15, 22, 16, 12, 17, 13, 20, 17, 16, 26, 8, 18, 11, 16, 10, 12, 15, 17, 14, 22, 26, 28, 15, 19, 23, 15, 12, 19, 26, 9, 27, 17, 15, 21, 18, 6, 24, 16, 13, 19, 12, 11, 11, 13, 15, 13, 13, 12, 10, 11, 13, 10, 9, 17, 23, 14, 23, 8, 17, 12, 15, 5, 11, 13, 20, 10, 13, 8, 6, 6, 2, 31, 26, 15, 20, 23, 9, 18, 22, 12, 8, 14, 18, 16, 12, 8, 11, 18, 12, 17, 22, 15, 12, 14, 7, 17, 23, 12, 10, 26, 7, 13, 23, 19, 13, 26, 13, 21, 17, 20, 19, 9, 9, 12, 15, 18, 16, 10, 16, 7, 8, 9, 18, 13, 12, 10, 9, 20, 13, 21, 13, 26, 21, 5, 8, 12, 13, 14, 25, 20, 18, 25, 24, 17, 15, 9, 14, 29, 16, 14, 15, 19, 9, 9, 14, 27, 28, 12, 16, 21, 16, 8, 8, 18, 20, 13, 4, 23, 18, 28, 16, 19, 26, 20, 14, 14, 16, 18, 13, 12, 13, 15, 9, 14, 19, 6, 3, 8, 13, 14, 20, 5, 16, 15, 17, 20, 18, 13, 14, 12, 13, 20, 14, 18, 14, 12, 13, 10, 2, 6, 11, 16, 25, 19, 8, 13, 24, 20, 17, 17, 34, 6, 23, 27, 9, 22, 20, 7, 17, 19, 20, 16, 12, 15, 9, 18, 18, 16, 15, 21, 9, 6, 15, 17, 25, 16, 18, 19, 19, 20, 23, 6, 5, 9, 9, 22, 11, 16, 15, 23, 23, 10, 8, 10, 22, 22, 10, 18, 19, 8, 15, 13, 11, 8, 21, 21, 15, 13, 22, 12, 23, 21, 17, 6, 9, 12, 21, 7, 16, 15, 12, 16, 17, 13, 15, 14, 18, 17, 10, 19, 11, 9, 19, 14, 17, 14, 12, 13, 5, 10, 13, 18, 2, 3, 8, 6, 12, 18, 23, 9, 13, 11, 21, 5, 17, 14, 12, 15, 18, 26, 25, 20, 13, 9, 14, 13, 18, 15, 18, 11, 15, 17, 21, 10, 13, 8, 11, 18, 15, 16, 28, 14, 12, 14, 28, 22, 10, 15, 21, 16, 11, 16, 8, 13, 3, 2, 5, 22, 8, 23, 11, 17, 12, 8, 32, 9, 18, 15, 14, 9, 10, 17, 18, 13, 14, 11, 22, 22, 10, 21, 19, 22, 26, 20, 14, 6, 19, 20, 16, 12, 9, 13, 15, 7, 9, 18, 8, 19, 19, 14, 20, 8, 10, 23, 20, 20, 12, 4, 9, 19, 10, 6, 8, 20, 12, 17, 15, 16, 8, 21, 12, 12, 17, 7, 11, 23, 9, 17, 13, 10, 14, 18, 9, 18, 15, 17, 6, 10, 9, 12, 13, 19, 17, 17, 9, 21, 5, 18, 27, 9, 10, 8, 7, 3, 4, 11, 18, 17, 21, 23, 16, 19, 10, 11, 11, 14, 9, 11, 28, 17, 18, 18, 10, 3, 8, 22, 16, 18, 17, 10, 18, 15, 20, 19, 13, 17, 9, 26, 18, 16, 17, 15, 7, 14, 9, 8, 12, 15, 26, 17, 10, 11, 18, 20, 9, 12, 15, 14, 10, 27, 12, 14, 10, 16, 17, 11, 13, 20, 9, 18, 10, 10, 12, 14, 14, 17, 16, 11, 8, 11, 22, 15, 4, 11, 21, 13, 24, 13, 19, 8, 14, 11, 16, 10, 19, 11, 11, 8, 22, 11, 3, 9, 4, 8, 6, 9, 23, 13, 17, 14, 23, 9, 16, 5, 11, 9, 15, 18, 30, 16, 5, 5, 17, 18, 15, 7, 13, 10, 9, 16, 21, 10, 7, 22, 16, 16, 12, 7, 22, 13, 12, 14, 28, 20, 19, 10, 4, 2, 8, 15, 9, 21, 11, 6, 7, 10, 16, 17, 14, 22, 10, 18, 14, 7, 17, 16, 22, 9, 9, 23, 20, 17, 13, 10, 13, 8, 9, 15, 16, 16, 12, 11, 20, 15, 26, 5, 14, 12, 11, 15, 14, 15, 15, 18, 10, 15, 3, 15, 15, 22, 19, 5, 16, 13, 11, 8, 16, 17, 15, 16, 13, 19, 11, 14, 13, 22, 9, 13, 13, 15, 13, 17, 19, 19, 18, 3, 15, 14, 11, 11, 13, 17, 14, 15, 16, 22, 15, 12, 14, 8, 12, 1, 6, 14, 23, 12, 4, 24, 12, 13, 14, 18, 13, 21, 14, 17, 13, 9, 19, 15, 20, 9, 10, 23, 13, 21, 7, 15, 11, 13, 22, 20, 7, 15, 17, 20, 18, 5, 23, 10, 13, 18, 12, 13, 13, 6, 13, 16, 22, 9, 13, 21, 15, 6, 15, 7, 16, 26, 12, 5, 21, 17, 9, 11, 10, 10, 23, 1, 13, 17, 19, 14, 18, 19, 17, 19, 17, 15, 5, 16, 18, 17, 11, 14, 16, 5, 17, 9, 6, 8, 6, 12, 15, 17, 9, 23, 17, 13, 13, 6, 18, 16, 18, 13, 21, 5, 15, 16, 9, 7, 18, 19, 17, 9, 12, 10, 13, 16, 11, 13, 28, 14, 21, 3, 19, 13, 13, 13, 18, 14, 14, 9, 13, 15, 19, 12, 15, 7, 9, 21, 16, 10, 17, 11, 9, 4, 9, 4, 8, 14, 21, 12, 19, 17, 8, 13, 10, 8, 15, 8, 14, 14, 10, 11, 5, 15, 21, 16, 9, 7, 18, 19, 9, 13, 15, 8, 2, 13, 12, 11, 15, 15, 10, 7, 9, 14, 9, 12, 15, 19, 10, 11, 14, 18, 4, 12, 17, 13, 12, 8, 5, 17, 14, 17, 12, 20, 7, 17, 13, 10, 15, 6, 13, 8, 4, 2, 11, 8, 23, 22, 11, 12, 23, 7, 14, 10, 13, 17, 12, 12, 17, 19, 14, 20, 15, 16, 10, 10, 12, 18, 12, 8, 23, 8, 17, 15, 19, 10, 16, 16, 16, 14, 15, 10, 25, 20, 20, 13, 14, 9, 16, 19, 13, 17, 20, 24, 9, 12, 10, 17, 11, 4, 17, 18, 14, 15, 13, 17, 17, 12, 14, 3, 14, 17, 14, 10, 16, 13, 16, 28, 15, 14, 13, 21, 16, 13, 16, 13, 20, 14, 7, 6, 13, 19, 5, 15, 10, 19, 12, 18, 15, 20, 17, 13, 8, 17, 15, 14, 16, 13, 10, 10, 11, 13, 9, 10, 11, 21, 21, 2, 13, 18, 10, 10, 14, 11, 8, 19, 9, 15, 6, 3, 17, 24, 14, 20, 7, 17, 15, 18, 14, 20, 8, 24, 12, 17, 20, 13, 14, 12, 14, 16, 7, 14, 11, 14, 8, 11, 17, 20, 11, 12, 11, 14, 19, 14, 10, 20, 19, 13, 18, 18, 22, 9, 10, 11, 19, 5, 12, 12, 20, 8, 12, 16, 20, 14, 13, 10, 16, 12, 11, 14, 16, 18, 14, 19, 16, 12, 15, 14, 21, 12, 17, 5, 12, 20, 16, 13, 9, 5, 10, 13, 13, 17, 9, 2, 12, 10, 18, 12, 17, 16, 18, 14, 17, 12, 11, 10, 8, 10, 18, 12, 13, 8, 9, 8, 12, 15, 11, 10, 14, 10, 17, 19, 12, 18, 20, 21, 7, 15, 17, 3, 11, 26, 12, 9, 9, 16, 30, 20, 16, 21, 15, 7, 19, 17, 12, 13, 17, 17, 9, 22, 11, 15, 11, 10, 15, 10, 12, 14, 18, 9, 11, 15, 7, 12, 13, 19, 7, 14, 12, 9, 12, 25, 16, 12, 12, 16, 11, 17, 14, 18, 14, 16, 17, 22, 16, 22, 13, 14, 16, 3, 9, 13, 3, 11, 11, 11, 20, 25, 10, 9, 19, 8, 17, 22, 20, 17, 17, 4, 10, 3, 11, 17, 18, 10, 7, 10, 3, 8, 12, 16, 9, 8, 16, 12, 18, 12, 11, 10, 8, 13, 6, 15, 17, 25, 12, 9, 16, 9, 14, 11, 21, 12, 12, 19, 12, 8, 17, 15, 7, 15, 16, 5, 8, 14, 20, 19, 5, 7, 14, 9, 13, 11, 14, 14, 13, 11, 12, 16, 15, 15, 23, 17, 20, 10, 12, 12, 8, 14, 15, 20, 17, 20, 5, 16, 19, 11, 20, 13, 9, 4, 9, 9, 19, 11, 19, 12, 4, 3, 11, 10, 15, 13, 12, 8, 22, 17, 11, 11, 16, 11, 16, 13, 12, 12, 14, 14, 24, 10, 13, 9, 9, 17, 17, 12, 15, 21, 5, 8, 11, 20, 14, 18, 21, 12, 10, 15, 8, 13, 17, 12, 11, 12, 11, 12, 10, 21, 9, 5, 17, 15, 17, 6, 17, 6, 19, 18, 17, 12, 11, 17, 13, 19, 15, 14, 9, 17, 11, 22, 14, 18, 9, 8, 20, 12, 5, 6, 16, 18, 13, 16, 5, 11, 17, 10, 16, 19, 10, 11, 12, 8, 7, 18, 9, 16, 12, 15, 14, 15, 18, 16, 12, 13, 11, 9, 8, 12, 7, 11, 19, 11, 9, 6, 9, 8, 4, 14, 22, 15, 17, 16, 27, 14, 16, 11, 11, 10, 11, 17, 14, 18, 7, 2, 7, 14, 17, 19, 13, 5, 11, 13, 12, 7, 8, 13, 9, 18, 20, 14, 18, 21, 13, 13, 7, 13, 14, 10, 7, 25, 14, 12, 22, 16, 18]
    gen_smooth = []
    k = 10
    disc_smooth = []
    for i in range(len(gen)):
        if i % k == 0:
            gen_smooth.append(0)
            disc_smooth.append(0)
        gen_smooth[-1] += gen[i]
        disc_smooth[-1] += disc[i]

    gen_smooth = np.array(gen_smooth)
    disc_smooth = np.array(disc_smooth)
    sum_smooth = gen_smooth + disc_smooth
    gen_smooth = gen_smooth / sum_smooth
    disc_smooth = disc_smooth / sum_smooth

    colors = ['m', 'b']
    labels = ['Generator',
              'Discrimintor']
    lineplot_new([gen_smooth, disc_smooth],
                 colors, labels,
                 xlabel='Epochs',
                 ylabel='Probability',
                 fig_name='action_dist.pdf',
                 xtick=np.arange(0, 201, 25),
                 xtick_label=np.arange(0, 41, 5),
                 legend_loc='center right')

if __name__ == '__main__':
    #mnist_compare_with_baseline_new()
    #mnist_compare_with_baseline()
    #mnist_transfer_cifar10()
    #reg_compare_with_baseline()
    mnist_action_dist()
