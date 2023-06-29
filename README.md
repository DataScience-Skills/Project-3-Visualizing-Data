# Project-3-Visualizing-Data
Bootcamp: UTA-VIRT-DATA-PT-02-2023-U-LOLC-MWTH(B) Project 3

## The Great Freeze - Texas Energy Prices Across Sectors:
- There are defining moments in time, and the State of Texas had an extreme weather outlier During February, 2021. This inspired JARDO Analytics, Inc. to determine how such extreme weather conditions impact energy consumption and prices in Texas.
- We used the [Energy Information Administration](<https://www.eia.gov/opendata/>){:target="_blank" rel="noopener"} API to request Texas energy data between January 2020 and January 2023. The EIA “collects, analyzes, and disseminates independent and impartial energy information to promote sound policymaking, efficient markets, and public understanding of energy and its interaction with the economy and the environment.” <https://www.eia.gov/opendata/>
![image](https://github.com/DataScience-Skills/Project-3-Visualizing-Data/assets/61632673/84ace6e4-a2f9-481d-9252-8b7db2c653dc)
- Our process:
  1. Make Initial calls to the EIA API
  2.Analyze, transform, and export JSON results
  3. Create charts using cleaned data
  4. Create a PSQL database to store the data
  5. Develop a Flask API to connect to the database and power the interactive webpage
  6. Design interactive webpage
 
- Two of the notable conclusions we made are:
  - The City Gate Price was greater during the freeze than the Residential Consumers Price, which is an anomaly since the City Fate Price is a component for calculating the Residential Consumers Price. The extreme weather conditions caused the transportation of fuel to be significantly more expensive , even if the fuel was not transferred to the residents.
  - The Petroleum sector showed spikes in petroleum consumption during the last two freezes in Texas, skipping over Winter 2021, in which there was no extreme freeze.

<https://github.com/DataScience-Skills/Project-3-Visualizing-Data/edit/main/Images/ng_prices.png>
<https://github.com/DataScience-Skills/Project-3-Visualizing-Data/edit/main/Images/petroleum_consumption.png>

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

