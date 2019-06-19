create table nouns as
  select "dog" as phrase union
  select "cat"           union
  select "bird";

# Using || to combine two strings together.
select subject.phrase || " chased " || object.phrase
  from nouns as subject, nouns as object
  where subject.phrase <> object.phrase;
