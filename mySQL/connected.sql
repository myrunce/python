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
order by num_cities desc;