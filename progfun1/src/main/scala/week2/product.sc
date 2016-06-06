object week2 {

  /**
    * Write a function product that computes the product of the values of
    * functions at points over a given range
    */
  def product(f: Int => Int)(a: Int, b: Int): Int = {
    if (a > b) 1
    else f(a) * product(f)(a + 1, b)
  }
  product(x => x * x)(1, 2)

  /**
    * Write factorial in terms of product
    * */
  def fact(n: Int) = product(x => x)(1, n)
  fact(5)

  /**
    * Write an even more general function which generalizes both sum and product?
    */
  def mapReduce(f: Int => Int, combine : (Int, Int) => Int, zero: Int)(a: Int, b: Int): Int = {
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a + 1, b))
  }
  def product2(f: Int => Int)(a: Int, b: Int): Int = mapReduce(f, (x, y) => (x * y), 1)(a, b)

  def fact2(n: Int) = product2(x => x)(1, n)
  fact2(5)

}