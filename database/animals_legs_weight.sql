create table animals as
  select "dog" as name, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;

select "Compute the minimum legs and maximum weight in animals.";
select min(legs), max(weight) from animals
  where name <> "t-rex";

select "Sum the weight of animals whose legs is 4.";
select sum(weight) from animals
  where legs = 4;

select "Get the average weight of these animals";
select avg(weight) from animals;

select "Count how many animals whose weight is 10.";
select count(*) from animals
  where weight = 10;

select "Count distinct legs in animals.";
select count(distinct legs) from animals;

select "Get the maximum weight animal.";
select name, max(weight) from animals;

select "Count how many animals having same legs.";
select legs, count(*) from animals group by legs;

select "Get the top 5 times that the weight shows up"
select name, count(*) as count from animals group by weight order by count desc limit 5;

select "Get the maximum weight animal grouping by legs.";
select legs, max(weight) from animals group by legs;

select "Get all the distinct combination of legs and weight.";
select legs, weight from animals group by legs, weight;

select "Get distinct ratio weight/legs which the count is great than 1";
select max(name), weight/legs
    from animals
    group by weight/legs
    having count(*)>1;
