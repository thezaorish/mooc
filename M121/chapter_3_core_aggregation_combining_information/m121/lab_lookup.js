predicate = {
  "$match": {
      "airplane": {"$regex": "747|380"}
  }
}

lookup = {
    "$lookup":
            {
                "from": "air_alliances",
                "localField": "airline.name",
                "foreignField": "airlines",
                "as": "airline_all"
            }
}

unwinding = {
    "$unwind": "$airline_all"
}

grouping = {
    "$group":
             {
                "_id": "$airline_all.name",
                "count": {"$sum": 1}
            }
}

sorting = {
    "$sort":
            {
                "count": -1
            }
}

pipeline = [
    predicate,
    lookup,
    unwinding,
    grouping,
    sorting
]

db.routes.aggregate(pipeline).pretty()
