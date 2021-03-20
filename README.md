# gender_gap

This repo contains scripts for calculating the gender gap in [Statistics Sweden's party preference survey (PSU)](https://www.scb.se/hitta-statistik/statistik-efter-amne/demokrati/partisympatier/partisympatiundersokningen-psu/).

Input files must be formatted exactly as the files in the data directory (otherwise calculate_gender_gap.py has to be modified).

Two measures of the gender gap are calculated, both expressed in percentage points:
* gender_gap1: sum of all differences between women's and men's party preferences
* gender_gap2: sum of all significant (at 95% level) differences