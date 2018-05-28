db.movies.aggregate([
  {"$match": { "imdb.rating": {"$gt": 0}, "metacritic": {"$gt": 0} }},
  {"$facet": {
    // get top 10 imdb rating descending
    top_imdbs: [
      {"$sort": {"imdb.rating": -1}},
      {"$project": {"_id": 1}},
      {"$limit": 10}
    ],
    // get movies with 100 metacritic score (yes, they are more than 10)
    top_metacritic: [
      {"$match": {"metacritic": {"$eq": 100}}},
      {"$project": {"_id": 1}}
    ]
  }},
  {
    "$project": {
      intersection: { "$setIntersection": [ "$top_imdbs", "$top_metacritic" ] }
    }
  }
]).pretty()


// or
db.movies.aggregate([
  {"$match": { "imdb.rating": {"$gt": 0}, "metacritic": {"$gt": 0} }},
  {"$facet": {
    // get top 10 imdb rating descending
    top_imdbs: [
      {"$sort": {"imdb.rating": -1}},
      {"$project": {"_id": 1}},
      {"$limit": 10}
    ],
    /// get top 10 metacritic descending
    top_metacritic: [
      {"$sort": {"metacritic": -1}},
      {"$project": {"_id": 1}},
      {"$limit": 10}
    ]
  }},
  {
    "$project": {
      intersection: { "$setIntersection": [ "$top_imdbs", "$top_metacritic" ] }
    }
  }
]).pretty()
