"""
Avery Lee
CSE 163 AB
This program implements the functions for HW Mapping.
File: census GeoDataFrame file and food access csv file
that contains information about food deserts in WA state.
Performs analyses through GeoDataFrame visualizations,
such as plotting populations in each tract, populations
in each county, food access and food deserts
by tract and county.
"""


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def load_in_data(census_fn, food_access_fn):
    """
    parameters: filename (str) census dataset,
    filename (str) food_access dataset
    returns a merged GeoDataFrame of the two datasets with
    dimensions: (1318, 30)
    """
    census = gpd.read_file(census_fn)
    food_access = pd.read_csv(food_access_fn)
    merged = census.merge(food_access, left_on='CTIDFP00',
                          right_on='CensusTract', how='left')
    merged = gpd.GeoDataFrame(merged, geometry='geometry')
    return merged


def percentage_food_data(merged):
    """
    parameter: merged GeoDataFrame
    returns the percentage (float 0-100) of census tracts
    in WA for which we have food access data
    """
    census_tract = merged.loc[:, ['CensusTract']]  # just CensusTract column
    # percent WITHOUT data
    percentage = float(census_tract.isna().sum()) / len(census_tract)
    return (1 - percentage) * 100


def plot_map(merged):
    """
    parameter: merged GeoDataFrame
    creates and saves plot map.png that shows the entire WA state
    """
    fig, ax = plt.subplots(1)
    merged.plot(ax=ax)
    plt.title('Washington State')
    plt.savefig('map.png')


def plot_population_map(merged):
    """
    parameter: merged GeoDataFrame
    creates and saves plot population_map.png where
    each tract in WA is colored by population
    """
    fig, ax = plt.subplots(1)
    merged.plot(ax=ax, color='#EEEEEE')  # grey background
    merged.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington Census Tract Populations')
    plt.savefig('population_map.png')


def plot_population_county_map(merged):
    """
    parameter: merged GeoDataFrame
    creates and saves plot county_population_map.png where
    each county in WA is colord by population
    """
    fig, ax = plt.subplots(1)
    merged.plot(ax=ax, color='#EEEEEE')  # grey background
    # aggregate population by County
    population_by_county = merged.dissolve(by='County', aggfunc='sum')
    population_by_county.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington County Populations')
    plt.savefig('county_population_map.png')


def plot_food_access_by_county(merged):
    """
    parameter: merged GeoDataFrame
    creates and saves plot county_food_access.png containing 4 subplots that
    illustrate lapophalf ratio (low access in half mile radius / total),
    lalow10 ratio (low access in 10 mile radius / total),
    lalowihalf ratio (low access and low income in half mile radius / total),
    lalowi10 ratio (low access and low income in 10 mile radius / total)
    """
    # slice dataframe
    merged = merged.loc[:, ['County', 'geometry', 'POP2010',
                            'lapophalf', 'lapop10', 'lalowihalf', 'lalowi10']]
    county = merged.dissolve(by='County', aggfunc='sum')
    # adding more ratio columns
    county['lapophalf_ratio'] = county['lapophalf'] / county['POP2010']
    county['lapop10_ratio'] = county['lapop10'] / county['POP2010']
    county['lalowihalf_ratio'] = county['lalowihalf'] / county['POP2010']
    county['lalowi10_ratio'] = county['lalowi10'] / county['POP2010']
    # plots
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    # ax1
    merged.plot(ax=ax1, color='#EEEEEE')
    county.plot(ax=ax1, column='lapophalf_ratio', legend=True, vmin=0, vmax=1)
    ax1.set_title('Low Access: Half')
    # ax2
    merged.plot(ax=ax2, color='#EEEEEE')
    county.plot(ax=ax2, column='lalowihalf_ratio', legend=True, vmin=0, vmax=1)
    ax2.set_title('Low Access + Low Income: Half')
    # ax3
    merged.plot(ax=ax3, color='#EEEEEE')
    county.plot(ax=ax3, column='lapop10_ratio', legend=True, vmin=0, vmax=1)
    ax3.set_title('Low Access: 10')
    # ax4
    merged.plot(ax=ax4, color='#EEEEEE')
    county.plot(ax=ax4, column='lalowi10_ratio', legend=True, vmin=0, vmax=1)
    ax4.set_title('Low Access + Low Income: 10')

    plt.savefig('county_food_access.png')


def plot_low_access_tracts(merged):
    """
    parameter: merged GeoDataFrame
    creates and saves plot low_access.png that displays low access areas
    based on urban and rural definitions.
    definitions:
    urban: pophalf >= 500 or pophalf >= 33% * total
    rural: pop10 >= 500 or pop10 >= 33% * total
    """
    # filter low access
    # (urban) AND ((pophalf >= 500) OR (pophalf >= totalpop * 33%))
    # (rural) AND ((pop10 >= 500) OR (pop10 >= totalpop * 33%))
    low = merged[((merged['Urban'] == 1) &
                 ((merged['lapophalf'] >= 500) |
                  (merged['lapophalf'] >= (33/100) * merged['POP2010']))) |
                 ((merged['Rural'] == 1) &
                 ((merged['lapop10'] >= 500) |
                  (merged['lapop10'] >= (33/100) * merged['POP2010'])))]
    # plot
    fig, ax = plt.subplots(1)
    # background WA
    merged.plot(ax=ax, color='#EEEEEE')
    # available data
    available = merged[merged['CensusTract'].notna()]
    available.plot(ax=ax, color='#AAAAAA')
    # low access
    low.plot(ax=ax)

    plt.title('Low Access Census Tracts')
    plt.savefig('low_access.png')


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
