# urban-contours

# data sources & notes
## wind data
### `JRA55`: Japanese 55-year Reanalysis, Daily 3-Hourly and 6-Hourly Data
- access: register at [Data for Climate & Weather Research](https://rda.ucar.edu/datasets/ds628.0/#!access)
- we want "JRA-55 6-Hourly 1.25 Degree Surface Analysis Fields"; grab u- and v- components 

## emissions data 
### `CEDS_GBD-MAPS`: Global Anthropogenic Emission Inventory of NOx, SO2, CO, NH3, NMVOCs, BC, and OC from 1970-2017
- access: available on [Zenodo](https://zenodo.org/record/3754964#.YAGkwud7nb0)
- we want `gridded_emissions_by_sector_fuel_YYYY.zip` files
- references: 
  - [The generation of gridded emissions data for CMIP6](https://gmd.copernicus.org/articles/13/461/2020/)
  - [JGCRI / CEDS](https://github.com/JGCRI/CEDS)
  - [EDGARv4.2 Emission Maps](https://data.jrc.ec.europa.eu/dataset/jrc-edgar-emissionmapsv42)
  - [Historical (1750–2014) anthropogenic emissions of reactive gases and aerosols from the Community Emissions Data System (CEDS)](https://gmd.copernicus.org/articles/11/369/2018/)

(all thanks to [Tatyana Deryugina](https://github.com/tatyanaderyugina)!
