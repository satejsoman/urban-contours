using NetCDF
using GRIB 

# use 2014 data 
# path = string(homedir(), "/Documents/workspace/research/slum-mapping/Atmospheric data/anl_surf125.051_spfh.2014030100_2014033118")
path = string(homedir(), "/Documents/workspace/research/slum-mapping/Atmospheric data/anl_surf125.013_pot.2004010100_2004123118")

GribFile(path) do f
    i = 0
    for message in f 
        print(i, message["name"], "\n")
        i += 1
    end 
end



destroy(f)