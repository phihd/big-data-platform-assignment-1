# Part 1 - Design

### 1. Explain your choice of types of data to be supported and technologies for **mysimbdp-coredms**.

The chosen data is [COVID-19 cases worldwide](https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data/resource/260bbbde-2316-40eb-aec3-7cd7bfc2f590), 
which contains the cummulative number for 14 days of COVID-19 cases per 100000 people. The data structure is as follow:

- *dateRep*: the date of record.
- *day, month, year*: the time detail of record.
- *cases*: the total number of cases.
- *deaths*: the total number deaths.
- *countriesAndTerritories*: the country name.
- *geoId*: 2-digit abbreviation of the country name.
- *countryterritoryCode*: 3-digit abbreviation of the country name.
- *popData2019*: the total population in 2019.
- *continentExp*: the continent that the country belongs to.
- *Cumulative_number_for_14_days_of_COVID-19_cases_per_100000*: the cummulative number for 14 days of COVID-19 cases per 100000 people.

The data can be aggregated by continent or country to analyse and compare statistics. Furthermore, time series data can be retrieved to
predict number of cases in the future with machine learning models. I chose MongoDB to represent **mysimbdp-coredms** due to its ability
to fully scale both vertically or horizontally. MongoDB also stored records as documents compressed in JSON files, which is suitable for
complex structured or unstructured data. Finally, it is easy to deploy with great user experience for developers.

### 2. Design and explain interactions between main components in the architecture of **mysimbdp**.

<p align="center">
<img src="Figures/architecture.png">
<p>

The diagram above illustrates the architecture of **mysimbdp**.
