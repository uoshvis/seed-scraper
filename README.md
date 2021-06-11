# seed-scraper
Securities Enforcement Empirical Database (SEED) scraper. The use of SEED data is for academic research purposes only.

To run scraper:
```
scrapy crawl enforcements -o output.csv -t csv
```

Output file: *output.csv*

**Collected data example:**


|legal_case_name                                                                                                                                                                                                                                                         |defendant_name                   |defendant_type|first_doc_date|first_resolution_date|allegation_type                |initial_filling_format|case_number|federal_district_court                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|--------------|--------------|---------------------|-------------------------------|----------------------|-----------|---------------------------------------|
|SEC v. Adelphia Communications Corporation, John J. Rigas, Tmothy J. Rigas, Michael J. Rigas, James P. Rigas, James R. Brown, and Michael C. Mulcahey                                                                                                                   |Adelphia Communications Corp.    |Public Company|24-Jul-2002   |30-Oct-2008          |Issuer Reporting and Disclosure|Civil Proceeding      |02-cv-05776|New York, Southern District of New York|
|SEC v. Frank J. Custable, Jr., Sara Wetzel, Suburban Capital Corporation, Francis Scott Widen, Wasatch Pharmaceutical Inc., David Giles, Gary Heesch, Pacel Corporation, David Calkins, Gateway Distributors, Ltd., Richard Bailey, and Thermoelastic Technologies, Inc.|ThermoElastic Technologies, Inc. |Other         |01-Apr-2003   |23-Feb-2010          |Issuer Reporting and Disclosure|Civil Proceeding      |03-cv-02182|Illinois, Northern District of Illinois|


**More datapoints are available**