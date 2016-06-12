package funsets

/**
 * 2. Purely Functional Sets.
 */
object FunSets {

  /**
   * We represent a set by its characteristic function, i.e. its `contains` predicate.
   */
  type Set = Int => Boolean

  /**
   * Indicates whether a set contains a given element.
   */
  def contains(s: Set, elem: Int): Boolean = s(elem)

  /**
   * Returns the set of the one given element.
   */
  def singletonSet(elem: Int): Set = {
    def setElement(x: Int): Boolean = x == elem
    setElement
  }


  /**
   * Returns the union of the two given sets, the sets of all elements that are in either `s` or `t`.
   */
  def union(s: Set, t: Set): Set = {
    def union_set(elem: Int) = s(elem) || t(elem)
    union_set
  }
  
  /**
   * Returns the intersection of the two given sets, the set of all elements that are both in `s` and `t`.
   */
  def intersect(s: Set, t: Set): Set = {
    def intersect_set(elem: Int) = s(elem) && t(elem)
    intersect_set
  }
  
  /**
   * Returns the difference of the two given sets, the set of all elements of `s` that are not in `t`.
   */
  def diff(s: Set, t: Set): Set = {
    def diff_set(elem: Int) = s(elem) && !t(elem)
    diff_set
  }
  
  /**
   * Returns the subset of `s` for which `p` holds.
   */
  def filter(s: Set, p: Int => Boolean): Set = {
    def filter_set(elem: Int) = s(elem) && p(elem)
    filter_set
  }
  

  /**
   * The bounds for `forall` and `exists` are +/- 1000.
   */
  val bound = 1000

  /**
   * Returns whether all bounded integers within `s` satisfy `p`.
   */
  def forall(s: Set, p: Int => Boolean): Boolean = {
    def inforall(a: Int): Boolean = {
      if (s(a) && !p(a)) false
      else if (a == bound) true
      else inforall(a + 1)
    }
    inforall(-bound)
  }

  def sum(f: Int => Int): (Int, Int) => Int = {
    def sumF(a: Int, b: Int): Int =
      if (a > b) 0
      else f(a) + sumF(a + 1, b)
    sumF
  }
  
  /**
   * Returns whether there exists a bounded integer within `s` that satisfies `p`.
   */
  def exists(s: Set, p: Int => Boolean): Boolean = {
    !forall(s, (x: Int) => !p(x))
  }
  
  /**
   * Returns a set transformed by applying `f` to each element of `s`.
   */
  def map(s: Set, f: Int => Int): Set = ???
  
  /**
   * Displays the contents of a set
   */
  def toString(s: Set): String = {
    val xs = for (i <- -bound to bound if contains(s, i)) yield i
    xs.mkString("{", ",", "}")
  }

  /**
   * Prints the contents of a set on the console.
   */
  def printSet(s: Set) {
    println(toString(s))
  }

}
