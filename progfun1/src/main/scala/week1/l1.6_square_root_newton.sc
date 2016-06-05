object newton_improved {

  def abs(x: Double) =
    if (x < 0) -x else x

  def sqrt(x: Double) = {
    def srqtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else srqtIter(improve(guess))

    def isGoodEnough(guess: Double): Boolean =
      abs(guess * guess - x) / x < 0.001

    def improve(guess: Double): Double =
      (guess + x / guess) / 2

    srqtIter(1.0)

  }

  sqrt(2)
  sqrt(4)
  sqrt(1e-6)
  sqrt(1e60)

}