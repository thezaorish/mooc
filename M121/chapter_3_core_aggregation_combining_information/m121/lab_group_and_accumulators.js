pipeline = [
    matching,
    grouping
]

db.movies.aggregate(pipeline).pretty()

var matching = {
    "$match": {
        "awards": { "$regex": "Won \\d{1,2} Oscars?"}
    }
}

var grouping = {
    "$group": {
        "_id": "null",
        "max_imdb": {"$max": "$imdb.rating"},
        "min_imdb": {"$min": "$imdb.rating"},
        "avg_imdb": {"$avg": "$imdb.rating"},
        "stdDev_imdb": {"$stdDevSamp": "$imdb.rating"}
    }
}
