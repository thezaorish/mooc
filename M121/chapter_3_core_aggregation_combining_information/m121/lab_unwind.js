predicate = {
    "$match":
     {
         "cast": { "$elemMatch": { "$exists": 'true' } },
         "languages": { "$in": [ "English" ] }
     }
}

unwinding = {
    "$unwind": "$cast"
}

grouping = {
    "$group":
         {
            "_id": "$cast",
            "count": {"$sum": 1},
            "average": {"$avg": "$imdb.rating"}
        }
}

sorting = {
    "$sort":
        {
            "count": -1
        }
}

limiting = {
    "$limit": 1
}

pipeline = [
    predicate,
    unwinding,
    grouping,
    sorting,
    limiting
]

db.movies.aggregate(pipeline).pretty()
