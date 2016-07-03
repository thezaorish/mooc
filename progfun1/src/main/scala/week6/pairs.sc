object test {

  def isPrime(n: Int): Boolean = {
    (2 until n) forall(d => n % d != 0)
  }
  val n = 7

  (1 until n) flatMap (i =>
    (1 until i) map (j => (i, j))) filter (pair =>
      isPrime(pair._1 + pair._2)
    )

  for {
    i <- 1 to n
    j <- 1 to i
    if isPrime(i + j)
  } yield (i, j)

}