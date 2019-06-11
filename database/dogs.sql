create table dogs as
    select "fillmore" as name, "curry" as fur union
    select "herman",           "long"         union
    select "beminham",         "short"        union
    select "jasonham",         "long"         union
    select "catkin",           "short"        union
    select "taitan",           "long"         union
    select "rathen",           "curry";

create table parents as
    select "fillmore" as parent, "jasonham" as child union
    select "herman",             "catkin"            union
    select "herman",             "taitan"            union
    select "beminham",           "herman"            union
    select "beminham",           "fillmore"          union
    select "rathen",             "beminham";

create table grandparents as
    select  a.parent as grandparent, b.child as grandchild
        from parents as a, parents as b
        where a.child = b.parent;

# get pairs of grandparent and grandchild whose fur are same.
select grandparent, grandchild
    from grandparents, dogs as c, dogs as d
    where c.name = grandparent and
          d.name = grandchild and
          c.fur = d.fur;
