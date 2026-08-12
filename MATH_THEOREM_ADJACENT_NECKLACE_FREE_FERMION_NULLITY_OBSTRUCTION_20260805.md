# Adjacent necklaces: a free-fermion nullity obstruction

**Date:** 2026-08-05  
**Method:** exterior algebra, Fourier diagonalization, and Koszul rotation
signs; no computation  
**Status:** unconditional no-go theorem for the quadratic/free-fermion
route.  It does **not** disprove a near-perfect matching in the adjacent
necklace graph.  It proves that the natural rotation-compatible quadratic
Tutte specialization cannot certify one, except in the trivial one-particle
or one-hole cases.

## 1. The labelled token cycle and its necklace quotient

Let

\[
             N=q+b,
\]

where `q` is odd.  Let \(V=\mathbb C^N\), with cyclically indexed basis
\(e_0,\ldots,e_{N-1}\), and put

\[
             \mathcal F_b=\bigwedge^b V.
\]

The standard monomial basis of \(\mathcal F_b\) is indexed by binary
strings of length \(N\) and weight \(b\).  A one-particle hop across a
cycle edge changes an adjacent `10` to `01`, or conversely.  Thus the
support graph in this basis is the labelled \(b\)-token graph of \(C_N\).
Quotienting by cyclic rotation gives the simple adjacent-necklace graph.

Let \(R e_i=e_{i+1}\).  We use the same letter for the induced exterior
action \(\bigwedge^b R\) when no confusion is possible.  The signs in this
action are the genuine Koszul signs; they must not be discarded before
passing to necklaces.

### Lemma 1.1 (odd stabilizers remove the Koszul obstruction)

If `q` is odd, the invariant space \(\mathcal F_b^R\) has one basis vector
for every ordinary binary necklace of length \(N\) and weight \(b\).

#### Proof

Suppose a binary string has rotational orbit length \(p\), and put
\(h=N/p\).  The string consists of \(h\) repeats, so \(h\mid b\) and
\(h\mid N\).  Therefore

\[
                    h\mid (N-b)=q.
\]

In particular, \(h\) is odd.  Rotation by \(p\) permutes the occupied
basis vectors as \(b/h\) disjoint cycles of length \(h\).  Its exterior
sign is

\[
                 (-1)^{(h-1)b/h}=1.
\]

Hence the signed orbit sum is nonzero.  Distinct necklace orbits have
disjoint monomial supports, so the normalized signed orbit sums form a
basis of \(\mathcal F_b^R\). \(\square\)

This is exactly where oddness of `q` enters the fermionic quotient.

## 2. Classification of the free nearest-neighbour operator

Let \(a_i^\dagger,a_i\) denote the usual exterior creation and contraction
operators.  A number-preserving quadratic operator supported on adjacent
token moves has the form \(d\Gamma(A)\), where the one-particle matrix
\(A\) is supported on the edges of \(C_N\).  If the many-particle matrix is
skew-symmetric in the monomial basis, then \(A^T=-A\).

Put

\[
 A_0=R-R^{-1},\qquad
 K_0=d\Gamma(A_0)ig|_{\mathcal F_b^R}.
                                                        \tag{2.1}
\]

### Lemma 2.1 (unique periodic free current)

Assume \(N\ge5\).  Every rotation-equivariant skew-symmetric
number-preserving quadratic operator supported on adjacent token moves is
a scalar multiple of \(d\Gamma(R-R^{-1})\).

More generally, if an arbitrary skew quadratic adjacent-hop operator is
only compressed to \(\mathcal F_b^R\), its compression equals the
compression of such a scalar multiple.

#### Proof

On the one-particle space, rotation acts transitively on the oriented
cycle edges.  Commutation with rotation therefore makes all clockwise
coefficients equal.  Skew symmetry makes every anticlockwise coefficient
the negative of the corresponding clockwise coefficient.  This gives
\(A=a(R-R^{-1})\).

For the second statement, average the arbitrary operator over cyclic
conjugation.  If \(P\) is the orthogonal projection onto
\(\mathcal F_b^R\), then for invariant \(x,y\),

\[
 \langle y,R^j K R^{-j}x\rangle=\langle y,Kx\rangle.
\]

Consequently \(PKP\) is unchanged by averaging.  The average is again a
skew quadratic adjacent-hop operator and is rotation-equivariant, so the
first part applies. \(\square\)

Thus varying physical edge weights before projecting does not create
additional free parameters on the necklace space.

## 3. Exact Fourier zero-mode bank

Let \(\omega=e^{2\pi i/N}\), and choose a Fourier basis
\(f_j\), \(j\in\mathbb Z_N\), satisfying

\[
 Rf_j=\omega^j f_j,
 \qquad
 A_0f_j=(\omega^j-\omega^{-j})f_j.
                                                        \tag{3.1}
\]

For a \(b\)-subset \(J\subseteq\mathbb Z_N\), put

\[
 f_J=\bigwedge_{j\in J}f_j.
\]

Then

\[
 Rf_J=\omega^{\sum_{j\in J}j}f_J,
 \qquad
 d\Gamma(A_0)f_J=
 \left(\sum_{j\in J}(\omega^j-\omega^{-j})\right)f_J.
                                                        \tag{3.2}
\]

### Theorem 3.1 (invariant free-fermion nullity)

Let `q` be odd.  For the periodic free current (2.1),

\[
 \dim\ker K_0\ \ge\
 \begin{cases}
 \displaystyle {\binom{(N-1)/2}{b/2}},&b\text{ even},\\[3mm]
 \displaystyle {\binom{(N-2)/2}{(b-1)/2}},&b\text{ odd}.
 \end{cases}                                           \tag{3.3}
\]

In particular, if \(q\ge3\) and \(b\ge2\), then

\[
                         \dim\ker K_0>1.                \tag{3.4}
\]

#### Proof

First suppose \(b=2s\).  Then \(N=q+b\) is odd.  Apart from momentum
zero, the momenta split into \((N-1)/2\) inverse pairs

\[
                         \{j,-j\}.
\]

Choose any \(s\) of these pairs and let \(J\) be their union.  The total
momentum is zero, so \(f_J\in\mathcal F_b^R\).  Each inverse pair makes
zero contribution to the second sum in (3.2), so \(f_J\in\ker K_0\).
The resulting vectors are distinct Fourier monomials and hence linearly
independent.  This proves the first line of (3.3).

Now suppose \(b=2s+1\).  Then \(N\) is even.  Choose momentum zero and any
\(s\) inverse pairs among the \((N-2)/2\) non-self-inverse pairs.  Again
the product has total momentum zero and current eigenvalue zero.  This
proves the second line.

If \(q\ge3\) and \(b\ge2\), the lower entry of either binomial coefficient
is positive and the complementary entry is at least \((q-1)/2\ge1\).
Thus the binomial coefficient is greater than one. \(\square\)

The zero modes are not an accidental degeneracy at a few parameters.
They are the entire bank of inverse-momentum-pair states forced by the
one-particle skew spectrum.

## 4. The antiperiodic spin structure does not help

There is one other real orthogonal spin structure.  Let \(R_-\) be the
signed cyclic shift with

\[
 R_-e_i=e_{i+1}\quad(i<N-1),
 \qquad
 R_-e_{N-1}=-e_0.
                                                        \tag{4.1}
\]

Then \(R_-^N=-I\).  It defines a genuine cyclic action on
\(\mathcal F_b\) only when \(b\) is even.  In that case `q` odd implies
\(N\) odd.

### Proposition 4.1 (the twisted nullity is the same)

For even \(b\), the signed invariant space
\(\mathcal F_b^{R_-}\) again has one basis vector per ordinary necklace,
and

\[
 \dim\ker\left(
 d\Gamma(R_--R_-^{-1})ig|_{\mathcal F_b^{R_-}}
 \right)
 \ge {\binom{(N-1)/2}{b/2}}.                           \tag{4.2}
\]

#### Proof

For a necklace stabilizer of odd order \(h\), the signed stabilizer acts
by a real scalar \(\lambda\in\{\pm1\}\).  Its \(h\)-th power is
\((R_-^N)^{\wedge b}=1\).  Since \(h\) is odd, \(\lambda=1\), proving the
orbit-basis assertion.

The one-particle eigenvalues of \(R_-\) are the \(N\) roots of
\(z^N=-1\).  Since \(N\) is odd, they consist of the self-inverse root
\(-1\) and \((N-1)/2\) inverse pairs.  Choosing \(b/2\) inverse pairs
gives product one and zero eigenvalue for
\(d\Gamma(R_--R_-^{-1})\), exactly as in Theorem 3.1. \(\square\)

Thus changing the real spin structure cannot remove the paired zero
modes.  A generic complex magnetic flux would destroy transpose-skew
symmetry (or the ordinary necklace action), so it is not a Pfaffian
operator on the required quotient.

## 5. Failure of exact quotient support

The obstruction is even stronger than excess nullity.  Distinct labelled
token edges can project to the same simple necklace edge with opposite
fermionic current signs, and therefore cancel.

### Example 5.1 (the smallest nontrivial graph)

Take \((q,b)=(3,2)\), so \(N=5\).  There are exactly two weight-two
necklaces:

\[
                   [11000],\qquad [10100].
\]

They are adjacent, so the simple necklace graph is \(K_2\) and has a
perfect matching.  But (3.3) gives

\[
                \dim\ker K_0\ge {\binom 21}=2.
\]

The invariant space itself has dimension two, so \(K_0=0\).  Concretely,
the clockwise and anticlockwise labelled hops between the two orbit classes
cancel after orbit summation.

Therefore the natural current is supported on labelled token edges but
need not be nonzero on every edge of the simple necklace quotient.

## 6. Consequence for Pfaffian matching arguments

A skew matrix on a graph certifies a perfect or near-perfect matching only
when its nullity is at most zero or one, respectively.  Theorem 3.1 proves
that every nontrivial periodic quadratic/free-fermion specialization has
nullity greater than one on the necklace orbit space.  Example 5.1 shows
that this can happen even when the graph itself has an obvious perfect
matching.

Hence the following route is closed:

\[
 \boxed{
 \text{translation-compatible quadratic hopping}
 \;\Longrightarrow\;
 \text{Fourier nonsingularity}
 \;\Longrightarrow\;
 \text{necklace matching}.}
\]

To obtain a Pfaffian proof one must leave the free theory.  One may assign
configuration-dependent, orbit-dependent variables to necklace edges,
equivalently use interacting terms such as

\[
 n_{i_1}\cdots n_{i_t},a_{i+1}^\dagger a_i-	ext{transpose}.
\]

With algebraically independent variables this becomes the ordinary Tutte
matrix.  Its full rank is equivalent to the desired matching and is no
longer Fourier-diagonalizable; it does not by itself prove the theorem.

Thus the viable algebraic continuation is an interacting discrete-Morse
or Schur-complement construction in which most vertices are paired first
and the induced operator on the explicit critical necklaces is analyzed.
The terminal-fracture and path-product reductions in the current record
have exactly that form.

## 7. Scope

Proved:

1. odd `q` makes the genuine Koszul invariant basis coincide with ordinary
   binary necklaces;
2. the periodic nearest-neighbour skew free current is unique up to scale;
3. its invariant kernel has the explicit lower bound (3.3);
4. the antiperiodic real spin structure has the same obstruction;
5. quotient-edge cancellation occurs already for \((q,b)=(3,2)\); and
6. no quadratic Fourier/Pfaffian specialization can certify the desired
   nontrivial near-perfect matching.

Not proved or disproved:

1. existence of a perfect or near-perfect matching in the simple adjacent
   necklace graph;
2. an interacting Tutte specialization of nullity at most one;
3. collision-free matching of the shifted-quiet critical necklaces; or
4. any universal-word upper bound.

