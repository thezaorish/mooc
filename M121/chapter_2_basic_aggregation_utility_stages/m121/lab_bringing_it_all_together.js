var predicate = {
    "$match":
     {
         "languages": { $in: [ "English"] },
         "imdb.rating" : {$gte: 1},
         "imdb.rating" : {$gte: 1},
         "year": {"$gte": 1990}
     }
}

var calculate_scalled_vote = {
    "$addFields":
    {
      "scaled_votes": {
        $add: [
          1,
          {
            $multiply: [
              9,
              {
                $divide: [
                  { $subtract: ["$imdb.votes", 5] },
                  { $subtract: [1521105, 5] }
                ]
              }
            ]
          }
        ]
      }
    }
}

var project = {
    "$project":
    {
      "_id": 0,
      "title": 1,
      "imdb.rating": 1,
      "scaled_votes": 1,
      "normalized_rating": 1
    }
}

var calculate_normalized_rating = {
    "$addFields":
    {
      "normalized_rating": {
        $avg: [ "$scaled_votes", "$imdb.rating" ]
      }
    }
}

var sort = {
    "$sort": { "normalized_rating": 1 }
}

var limit = {
    "$limit": 1
}

var pipeline = [
    predicate,
    calculate_scalled_vote,
    calculate_normalized_rating,
    project,
    sort,
    limit
]

db.movies.aggregate(pipeline).pretty()
