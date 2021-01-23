# importing the Kaggle API
# pip install kaggle
import pandas as pd
import numpy as np

file = "country_vaccinations.csv"
vaccinesdf = pd.read_csv(file)
#print(vaccinesdf.info())
#print(vaccinesdf.shape)
#print(vaccinesdf)

#
file2 = "population_by_country_2020.csv"
popdf = pd.read_csv(file2)
print(popdf)

# sort country by ppl_fully_vacs. replace missing values w/ 0
vaccinesdf[["people_fully_vaccinated"]] = vaccinesdf[["people_fully_vaccinated"]].fillna(0)
#print(vaccinesdf[["people_fully_vaccinated"]])

# set d type of column "date" as initially "object"
vaccinesdf[["date"]] = vaccinesdf[["date"]].apply(pd.to_datetime)
# print(vaccinesdf.dtypes)

# group by&loc
total_vac_per_country = vaccinesdf.loc[vaccinesdf.groupby('country').date.idxmax()]

# sort largest to smallest value
total_vac_per_country = total_vac_per_country.sort_values(by='people_fully_vaccinated', ascending=False)
#print(total_vac_per_country[["country", "people_fully_vaccinated"]])

# filter for countries where number of vaccinations is more than 200000
vaccine_gt_200k = total_vac_per_country[total_vac_per_country.people_fully_vaccinated > 200000][
    ["country", "people_fully_vaccinated"]]

# iterate over rows with iterrows()
for index, row in vaccine_gt_200k.iterrows():
    print(str(row[1]) + " people have been fully vaccinated in " + row[0])



# daily vacs per 1mil country pop
#vaccinesdf["daily_vaccinations_per_million"] = 1000000 * vaccinesdf[["people_fully_vaccinated"]"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
#high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
#high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
#result = high_homelessness_srt[["state", "indiv_per_10k"]]
#print(result)
