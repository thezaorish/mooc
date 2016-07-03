object test {

  val xs: Array[Int] = Array(1, 2, 3)
  xs map (x => 2 * x)

  val ys: String = "Hello World!"
  ys filter (_.isUpper)

  val r: Range = 1 until 5
  val s: Range = 1 to 5
  1 to 10 by 3
  6 to 1 by -2

  ys exists {ys => ys.isUpper}
  ys forall {ys => ys.isUpper}

  val pairs = List(1, 2, 3) zip ys
  pairs.unzip

  ys
  ys flatMap(c => List('+', c))

}