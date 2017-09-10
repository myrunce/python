select countries.name , languages.language, languages.percentage
from countries
join languages
on countries.id = languages.country_id
where languages.language = 'Slovene'
order by countries.name desc;

select countries.name, count(cities.id) as num_cities
from countries
join cities
on countries.id = cities.country_id
group by countries.id
order by num_cities desc;

select cities.name, cities.population
from countries 
join cities 
on countries.id = cities.country_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage
from countries
join languages 
on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;

select countries.name, countries.surface_area, countries.population
from countries
where countries.surface_area < 501 and countries.population > 100000;

select countries.name, countries.government_form, countries.life_expectancy, countries.capital
from countries
where countries.government_form = 'Consitutional Monarchy' and countries.capital > 200 and countries.life_expectancy > 75;

select countries.name, cities.name, cities.district, cities.population
from countries
join cities on countries.id = cities.country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;

select countries.region, count(countries.id) as num_countries
from countries
group by countries.region
order by num_countries desc;
