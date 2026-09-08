# Every later good pair cell crosses the first good sector

**Date:** 2026-08-13  
**Status:** unconditional structural obstruction to first-hit whole-cell absorption.

## 1. Pair structures

Let \(\mathcal S\) and \(\mathcal S'\) be two sentinel-plus-perfect-matching pair
structures on the same odd ground set.  For an owner \(T\), write
\(m_{\mathcal S}(T)\) for its number of singleton matching pairs in
\(\mathcal S\).

A dimension-\(m\) cell \(C\) of \(\mathcal S'\) has \(m\) variable pairs.  Outside
their \(2m\) endpoints, membership is fixed; on each variable pair, an owner in
\(C\) chooses exactly one endpoint.

## 2. Cross-structure maximum lemma

### Lemma 2.1

Every dimension-\(m\) cell \(C\) of \(\mathcal S'\) contains an owner \(T\) with

\[
                         m_{\mathcal S}(T)\ge m.           \tag{2.1}
\]

#### Proof

Let \(J\) be the matching of the \(m\) variable pairs of \(C\).  Superimpose on
their endpoints the matching edges of \(\mathcal S\).  If an endpoint is the
sentinel of \(\mathcal S\), it has no such edge.  If its \(\mathcal S\)-partner lies
outside the variable set, attach that fixed partner as a boundary vertex.  Ignore
\(\mathcal S\)-edges with both endpoints fixed, since their singleton status is a
nonnegative constant independent of the choice in \(C\).

The resulting graph is a disjoint union of alternating cycles and alternating paths.
Assign zero/one memberships to the variable endpoints subject to the mandatory rule
that every \(J\)-edge has opposite endpoint values.

* On an alternating cycle, proper two-colouring makes every \(\mathcal S\)-edge
  singleton.  The numbers of \(J\)- and \(\mathcal S\)-edges are equal.
* On a path with two fixed boundary endpoints, there is one more
  \(\mathcal S\)-edge than \(J\)-edge.  If the two prescribed boundary values are
  parity-compatible, cut every \(\mathcal S\)-edge.  Otherwise violate one
  \(\mathcal S\)-edge.  In either case at least as many \(\mathcal S\)-edges as
  \(J\)-edges are singleton.
* On a path ending at the \(\mathcal S\)-sentinel, there is only one prescribed
  boundary value and the two-colouring phase can be chosen to cut every
  \(\mathcal S\)-edge.  Again their number is at least the number of \(J\)-edges.

Choose these phases independently on the components.  Summing, at least the total
number \(m\) of \(J\)-edges become singleton \(\mathcal S\)-pairs.  The resulting
membership vector is an owner of \(C\), because it makes exactly one choice on every
variable pair and leaves all fixed coordinates unchanged.  This proves (2.1).
\(\square\)

## 3. First-hit obstruction

Fix the long-run threshold

\[
                         M=q+\lceil3\log_2p\rceil.
\]

### Theorem 3.1

Every good cell of \(\mathcal S'\), meaning every cell of dimension at least \(M\),
intersects the good-owner sector of \(\mathcal S\).

#### Proof

If \(C\) has dimension \(m\ge M\), Lemma 2.1 supplies
\(T\in C\) with \(m_{\mathcal S}(T)\ge m\ge M\).  Thus \(T\) is good for
\(\mathcal S\).  \(\square\)

### Corollary 3.2

Select all whole good cells of one pair structure and let its bad sector be the
uncovered residual.  No whole good cell of any later pair structure is contained in
that residual.  Consequently a “first good structure” assignment can use later
structures only by cutting their cells.

This remains true even when a constant family of pair structures covers every owner
by at least one good cell.  The later structures solve support coverage but cannot be
installed intact after the first partition.  A switchable overlap theorem, a
cross-cell cycle selector, or a non-cube absorber is therefore logically necessary.
