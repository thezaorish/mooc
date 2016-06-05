object newton {

  def srqtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else srqtIter(improve(guess, x), x)

  def abs(x: Double) =
    if (x < 0) -x else x

  def isGoodEnough(guess: Double, x: Double): Boolean =
    abs(guess * guess - x) / x < 0.001

  def improve(guess: Double, x: Double): Double =
    (guess + x / guess) / 2

  def sqrt(x: Double) = srqtIter(1.0, x)

  sqrt(2)
  sqrt(4)
  sqrt(1e-6)
  sqrt(1e60)

}