// Import excel data

import excel "C:\Users\maria\OneDrive\Escritorio\EC226 Project\Raw Excel Files\Alldata.xlsx", sheet("Sheet1") firstrow

// rename variables

rename observation_date Date
label variable AirFares "Air Fares (non-inflation adjusted)"
label variable WTI "West Texas Intermediate oil price (non-inflation adjusted)"
label variable CPI "CPI, 1982-1984 = 100"

//Generate inflation-adjusted airfare and WTI data

generate real_AirFares = ( AirFares / CPI ) * 100
generate real_WTI = ( WTI / CPI ) * 100

//Add descriptions to that data

label variable real_AirFares "Air Fares (Inflation adjusted)"
label variable real_WTI "WTI oil price (Inflation adjusted)"