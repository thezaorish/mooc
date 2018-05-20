var predicate = {
    "$match":
     {
         "cast": { "$elemMatch": { "$exists": 'true' } },
         "countries": { "$in": [ "USA" ] },
         "tomatoes.viewer.rating": {"$gte": 3}
     }
}

var projection = {
    "$project":
    {
        "tomatoes.viewer.rating": 1,
        "title": 1,
        "num_favs": { "$size": {"$setIntersection": [ [
                                          "Sandra Bullock",
                                          "Tom Hanks",
                                          "Julia Roberts",
                                          "Kevin Spacey",
                                          "George Clooney"
                                        ], "$cast" ]}},
        "_id": 1
    }
}

var sorting = {
    "$sort": {
        "num_favs": -1,
        "tomatoes.viewer.rating": -1,
        "title": -1
    }
}

var skipping = {
    "$skip": 24
}

var limiting = {
    "$limit": 1
}

var pipeline = [
    predicate,
    projection,
    sorting,
    skipping,
    limiting
]

db.movies.aggregate(pipeline)
