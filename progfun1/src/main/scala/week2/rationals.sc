object rationals {
  val x = new Rational(1, 3)
  x.numer
  x.denom

  val y = new Rational(5, 7)
  val z = new Rational(3, 2)

  x.add(y)
  x.sub(y).sub(z)

  val x3 = new RationalRelaxedIdentifiers(1, 2)
  val y3 = new RationalRelaxedIdentifiers(3, 4)

  x3 + y3
  x3 - y3
}

class Rational(x: Int, y: Int) {

  require(y > 0, "denominator must be positive") // predefined function

  def this(x: Int) = this(x, 1) // second constructor

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

  val numer = x / gcd(x, y)
  val denom = y / gcd(x, y)

  def add(that: Rational) = new Rational(numer * that.denom + denom * that.numer, denom * that.denom)

  def sub(that: Rational) = add(that.neg)

  def neg: Rational = new Rational(-numer, denom)

  def less(that: Rational) = numer * that.denom < that.numer * denom

  def max(that: Rational) = if (this.less(that)) that else this

  override def toString = numer + "/" + denom

}

class RationalUnSimplified(x: Int, y: Int) {

  require(y > 0, "denominator must be positive") // predefined function

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

  val numer = x
  val denom = y

  def add(that: Rational) = new Rational(numer * that.denom + denom * that.numer, denom * that.denom)

  def sub(that: Rational) = add(that.neg)

  def neg: Rational = new Rational(-numer, denom)

  def less(that: Rational) = numer * that.denom < that.numer * denom

  def max(that: Rational) = if (this.less(that)) that else this

  override def toString = {
    val g = gcd(x, y)
    numer / g + "/" + denom / g
  }

}

class RationalRelaxedIdentifiers(x: Int, y: Int) {

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
  private val g = gcd(x, y)

  def numer = x / g
  def denom = y / g

  def + (r: RationalRelaxedIdentifiers) = new RationalRelaxedIdentifiers(numer * r.denom + r.numer * denom, denom * r.denom)

  def - (r: RationalRelaxedIdentifiers) = new RationalRelaxedIdentifiers(numer * r.denom + denom * r.numer, denom * r.denom)

  override def toString = numer + "/" + denom

}