__all__ = [
    'dose_achieving'
]

import numpy as np
import re
import io
import math
import itertools as it
import pandas as pd
from scipy.stats import norm, kstest
import abm
from matplotlib import colors


def dose_achieving(df, output_name, target_output_value, dose_col='dose_mpk', value_col = 'value', get_data = False):
    """returns dose achieiving some metric e.g. RO90
    
    Parameters
    ----------
    df : pandas.DataFrame
        Table containing results of dose sweep. Must be in 'tall' format. Column containing output names must be titled 'output'
    output_name : str
        Name of output to threshold  
    target_output_value : float or int
        Desired threshold to calculate achieving dose for.
    dose_col: str, optional
        Column name in which dose values are listed. Default = 'dose_mpk'
    value_col: str, optional
        Column name in which output values are listed. Default = 'value'
        
    Returns
    -------
    list
        List of doses at which target_output_value of output_name is reached
    """
    df_select = df.query('output == @output_name')
    # make sure table is sorted by dose
    df_select = df_select.sort_values(by=dose_col)
    solns = []
    # loop over pairs of rows
    for ind in range(len(df_select)-1):
        row_0 = df_select.iloc[ind]
        row_1 = df_select.iloc[ind+1]
        # catch any solutions 
        if (row_0[value_col] <= target_output_value <= row_1[value_col]) or (row_0[value_col] >= target_output_value >= row_1[value_col]):
            soln = np.interp(target_output_value,[row_0[value_col], row_1[value_col]],[row_0[dose_col], row_1[dose_col]])
            solns.append(soln)
    return solns   

def color_scheme(scheme_name = 'bright', Num = None, test = False):
    '''Scheme Name Options: ["bright", "high_contrast", "muted", "vibrant", "medium_contrast", "light", "div_sunset", "div_nightfall", "div_BuRd", "div_PRGn", "seq_YlOrBr", "seq_Iridescent", "seq_Incandescent", "disc_rainbow", "smooth_rainbow"]

 Sequential, divergent, and rainbow color schemes are meant to be linearly interpolated. These should include a value for optional parameter Num

 Optional Parameter: Num is a parameter that counts the number of colors desired for the plot - this should be the number of discrete data sets you are using

 Optional Parameter: test: This parameter is used if you want to preview your scheme. Setting test = True does not allow you to use the color schemeas an input in your plot, but running color_scheme(scheme_name, Num, test = True) will output a color bar that shows an example of all the colorsthat will be used in the plot once test is set to False.'''
    scheme_dict = {
                'bright':['#4477AA', '#66CCEE','#228833', '#CCBB44', '#EE6677', '#AA3377', '#BBBBBB'],
                'high_contrast':['#DDAA33', '#BB5566', '#004488', '#000000'],
                'muted':['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#CC6677', '#882255', '#AA4499', '#DDDDDD'],
                'vibrant':['#0077BB','#33BBEE', '#009988', '#EE7733','#CC3311', '#EE3377', '#BBBBBB'],
                'medium_contrast':['#EECC66', '#EE99AA', '#6699CC', '#997700', '#994455', '#004488', '#000000'],
                'light': ['#77AADD', '#99DDFF', '#44BB99', '#BBCC33', '#AAAA00', '#EEDD88', '#EE8866', '#FFAABB', '#DDDDDD'],
                'div_sunset':['#364B9A', '#4A7BB7', '#6EA6CD', '#98CAE1', '#C2E4EF', '#EAECCC', '#FEDA8B', '#FDB366', '#F67E4B', '#DD3D2D', '#A50026'],
                'div_nightfall':[ '#125A56', '#00767B', '#238F9D', '#42A7C6', '#60BCE9', '#9DCCEF', '#C6DBED', '#DEE6E7', '#ECEADA', '#F0E6B2', '#F9D576', '#FFB954', '#FD9A44', '#F57634', '#E94C1F', '#D11807', '#A01813'],
                'div_BuRd':['#2166AC', '#4393C3', '#92C5DE', '#D1E5F0', '#F7F7F7', '#FDDBC7', '#F4A582', '#D6604D', '#B2182B'],
                'div_PRGn':['#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#F7F7F7', '#D9F0D3', '#ACD39E', '#5AAE61', '#1B7837'],
                'seq_YlOrBr':[ '#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FB9A29', '#EC7014', '#CC4C02', '#993404', '#662506'],
                'seq_Iridescent': ['#FEFBE9', '#FCF7D5', '#F5F3C1', '#EAF0B5', '#DDECBF', '#D0E7CA', '#C2E3D2', '#B5DDD8', '#A8D8DC', '#9BD2E1', '#8DCBE4', '#81C4E7', '#7BBCE7', '#7EB2E4', '#88A5DD', '#9398D2', '#9B8AC4', '#9D7DB2', '#9A709E', '#906388', '#805770', '#684957', '#46353A'],
                'seq_Incandescent':['#CEFFFF', '#C6F7D6', '#A2F49B', '#BBE453', '#D5CE04', '#E7B503', '#F19903', '#F6790B', '#F94902', '#E40515', '#A80003'],
                'disc_rainbow':['#D9CCE3', '#D1BBD7', '#CAACCB', '#BA8DB4', '#AE76A3', '#AA6F9E', '#994F88', '#882E72', '#1965B0', '#437DBF', '#5289C7', '#6195CF', '#7BAFDE', '#4EB265', '#90C987', '#CAE0AB', '#F7F056', '#F7CB45', '#F6C141', '#F4A736', '#F1932D', '#EE8026', '#E8601C', '#E65518', '#DC050C', '#A5170E', '#72190E', '#42150A'],
                'smooth_rainbow':['#D1C1E1', '#C3A8D1', '#B58FC2', '#A778B4', '#9B62A7', '#8C4E99', '#6F4C9B', '#6059A9', '#5568B8', '#4E79C5', '#4D8AC6', '#4E96BC', '#549EB3', '#59A5A9', '#60AB9E', '#69B190', '#77B77D', '#8CBC68', '#A6BE54', '#BEBC48', '#D1B541', '#DDAA3C', '#E49C39', '#E78C35', '#E67932', '#E4632D', '#DF4828', '#DA2222', '#B8221E', '#95211B', '#721E17', '#521A13']
}
    if test == False:
        if Num == None:
            return scheme_dict[scheme_name]
        else:
            x =  colors.LinearSegmentedColormap.from_list(scheme_name,scheme_dict[scheme_name], Num)
            return [ colors.to_hex(x(i)) for i in range(x.N)]
    else:
        if Num == None:
            return colors.LinearSegmentedColormap.from_list(scheme_name,scheme_dict[scheme_name], len(scheme_dict[scheme_name]))
        else:
            return colors.LinearSegmentedColormap.from_list(scheme_name,scheme_dict[scheme_name], Num)