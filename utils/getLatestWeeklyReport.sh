#!/usr/bin/env bash
month=`date -v -1d '+%b'`
day=`date -v -1d '+%-d'`
year=`date -v -1d '+%Y'`

fulldate="${month}-${day}-${year}"
reportName="$fulldate-weekly-report.xlsx"

echo $fulldate
fullURL="https://www.mass.gov/doc/weekly-covid-19-public-health-report-february-4-2021/download"
fullPath="./reports/${fulldate}"

echo $fullURL
wget -P './reports/' ${fullURL}
mv './reports/download' ./reports/$reportName

