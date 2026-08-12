# Even-\(m\) \(BA\)-orbit owner parity obstruction

Date: 2026-07-26

Method: exact coordinate-permutation and incidence-vector audit; no
computation or external input.

## 0. Statement

Put

\[
 n=2m+1,\qquad C=BA,\qquad L=m(m+1),
\]

with

\[
 A(x_1,\ldots,x_n)=(x_2,\ldots,x_{n-1},x_1,x_n)
\]

and

\[
 C(x_1,\ldots,x_n)
 =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\]

Identify an injective de Bruijn arc with its associated permutation
state, and write

\[
 \kappa(x_1,\ldots,x_n)=\{x_1,\ldots,x_m\}
\]

for its middle owner. If \(S\) is the source set of an alternating atom
circulation, its selected owner occurrences are

\[
 \{\kappa(e):e\in S\}\mathbin{\dot\cup}
 \{\kappa(Ae):e\in S\},
\tag{0.1}
\]

where the disjoint union records occurrences, not necessarily distinct
owner labels. Exact de Bruijn balance is \(S=C(S)\).

### Theorem 0.1 (orbitwise doubling for even \(m\))

Assume \(m\) is even. For every \(C\)-orbit \(\mathcal O\), the source
and successor owner multisets agree exactly:

\[
 \boxed{
 \bigl\{\!\bigl\{\kappa(e):e\in\mathcal O\bigr\}\!\bigr\}
 =
 \bigl\{\!\bigl\{\kappa(Ae):e\in\mathcal O\bigr\}\!\bigr\}.}
\tag{0.2}
\]

More precisely, for every \(e\in\mathcal O\) and every integer \(t\),

\[
 \boxed{\kappa(AC^t e)=\kappa(C^{t+m+1}e).}
\tag{0.3}
\]

Consequently, if \(S=C(S)\), its owner-incidence vector is twice a
nonnegative integral vector:

\[
 \boxed{
 \sum_{e\in S}
  \bigl({\bf e}_{\kappa(e)}+{\bf e}_{\kappa(Ae)}\bigr)
 =2\sum_{e\in S}{\bf e}_{\kappa(e)}.}
\tag{0.4}
\]

In particular, no nonempty union of \(BA\)-orbits can satisfy owner
capacity one, even if arbitrary owner rows are allowed to be left
empty. Hence the canonical matching--circulation intersection from
MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md
has no nonzero integral solution when \(m\) is even.

This is an obstruction to that alternating nested-star ansatz, not an
obstruction to general rotor circulations or to the constant-one
conjecture.

## 1. Coordinate footprints and the exact CRT phase

Let

\[
 P=\{1,\ldots,m\},\qquad Q=\{2,\ldots,m+1\}.
\tag{1.1}
\]

Thus \(\kappa(\pi)\) reads the labels in footprint \(P\), while
\(\kappa(A\pi)\) reads the labels in footprint \(Q\).

The pullback permutation \(c\) of coordinate positions for \(C\) is
defined by

\[
 (C\pi)_j=\pi_{c(j)}.
\]

The displayed formula for \(C\) gives

\[
 c=(1,3,5,\ldots,2m-1)
   (2,4,6,\ldots,2m,2m+1).
\tag{1.2}
\]

The cycles have lengths \(m\) and \(m+1\), respectively. This also
checks that every state orbit has length

\[
 \operatorname{lcm}(m,m+1)=m(m+1),
\tag{1.3}
\]

because a state has pairwise distinct coordinate labels.

Write \(m=2k\). On the odd-position cycle,

\[
 P\cap\{1,3,\ldots,2m-1\}
   =\{1,3,\ldots,2k-1\},
\]

whereas

\[
 Q\cap\{1,3,\ldots,2m-1\}
   =\{3,5,\ldots,2k+1\}.
\]

Thus the required phase displacement is one step modulo \(m\). On the
second position cycle,

\[
 P\cap\{2,4,\ldots,2m,2m+1\}
 =Q\cap\{2,4,\ldots,2m,2m+1\}
 =\{2,4,\ldots,2k\},
\]

so the displacement is zero modulo \(m+1\). The exact simultaneous
congruences are therefore

\[
 s\equiv1\pmod m,\qquad s\equiv0\pmod{m+1}.
\tag{1.4}
\]

Their unique solution modulo \(L=m(m+1)\) is

\[
 \boxed{s=m+1.}
\tag{1.5}
\]

Indeed, \(m+1\equiv1\pmod m\) and is zero modulo \(m+1\). Hence

\[
                       c^{m+1}P=Q.
\tag{1.6}
\]

This exponent uses the pullback action in (1.2). There is therefore no
hidden sign reversal in the phase: the convention is fixed directly by
\((C\pi)_j=\pi_{c(j)}\).

## 2. Proof of orbitwise doubling

For a state \(\pi=(x_1,\ldots,x_n)\) and a position set \(D\), write
\(x_D=\{x_i:i\in D\}\). By the pullback convention,

\[
 \kappa(C^t\pi)=x_{c^tP}.
\tag{2.1}
\]

Applying \(A\) after \(C^t\) makes its first \(m\) output positions read
positions \(Q\) of \(C^t\pi\), and therefore

\[
 \kappa(AC^t\pi)=x_{c^tQ}.
\tag{2.2}
\]

Using (1.6),

\[
 x_{c^tQ}=x_{c^tc^{m+1}P}
          =x_{c^{t+m+1}P}
          =\kappa(C^{t+m+1}\pi),
\]

which proves (0.3). Translation \(t\mapsto t+m+1\) is a permutation
of the \(L\) phases of a \(C\)-orbit, so (0.2) follows with
multiplicities.

The two occurrences paired in (0.3) are genuinely different selected
arc states. If \(AC^t\pi=C^{t+m+1}\pi\), distinctness of all labels
would imply the equality of coordinate permutations \(A=C^{m+1}\).
But \(C^{m+1}\) fixes the second position (it is the identity on the
length-\(m+1\) coordinate cycle), whereas \(A\) sends output position
\(2\) to input position \(3\). Thus \(A\ne C^{m+1}\).

Now let \(S=C(S)\). Since \(C\) is a permutation, \(S\) is a disjoint
union of full \(C\)-orbits. Summing (0.2) over those orbits yields

\[
 \sum_{e\in S}{\bf e}_{\kappa(Ae)}
 =\sum_{e\in S}{\bf e}_{\kappa(e)},
\]

and hence (0.4).

No grouping of the states into canonical atom triples affects this
identity: it depends only on \(S=C(S)\). Nor can two different orbits
cancel it. Owner incidences are nonnegative, and every orbit already
has an even incidence vector. A sum of such vectors remains
coordinatewise even. Therefore a capacity vector in
\(\{0,1\}^{\binom{[n]}m}\) can be realized only by the zero selection.
\(\square\)

## 3. Exact and approximate consequences

Let

\[
 \lambda_X=\#\{e\in S:\kappa(e)=X\},
 \qquad
 \ell_X=\#\{e\in S:\kappa(e)=X\}
          +\#\{e\in S:\kappa(Ae)=X\}.
\]

For even \(m\), (0.4) says

\[
                         \ell_X=2\lambda_X.
\tag{3.1}
\]

Three sharp consequences follow.

1. **Partial capacity-one packing is zero.** If
   \(0\le\ell_X\le1\) for every owner \(X\), then every
   \(\lambda_X=0\), hence \(S=\varnothing\). Thus allowing a leave does
   not help: the leave is exactly

   \[
                         \boxed{W=\binom{2m+1}m.}
   \tag{3.2}
   \]

   The conclusion is unchanged after adding any auxiliary literal
   reservoir. If \(a_X\in\mathbb Z_{\ge0}\) is its owner load and
   \(\ell_X+a_X\le1\) for every \(X\), then already
   \(\ell_X\le1\), so \(S=\varnothing\). Positive owner occurrences
   cannot cancel the orbitwise doubling.

2. **Linear mismatch is unavoidable without the capacity constraint.**
   For every \(BA\)-invariant \(S\), including \(S=\varnothing\),

   \[
    \boxed{
    \sum_{X\in\binom{[n]}m}|\ell_X-1|\ge W.}
   \tag{3.3}
   \]

   Indeed \(\ell_X\) is an even nonnegative integer, so its distance
   from \(1\) is at least \(1\) in every coordinate. Equivalently, if
   \(H_0=\#\{X:\ell_X=0\}\) and
   \(O=\sum_X(\ell_X-1)_+\), then

   \[
                         H_0+O\ge W.
   \tag{3.4}
   \]

3. **At least half the occurrences must be edited orbitwise.** The
   phase bijection in (0.3) pairs the \(2L\) source/successor
   occurrences of one activated orbit into \(L\) equal-owner pairs.
   Any occurrence-level repair imposing capacity one must delete at
   least one member of every pair, hence at least \(L\) occurrences per
   activated orbit. This lower bound ignores the additional flow damage
   caused by breaking a full orbit, so it is valid a fortiori for an
   exact circulation repair.

Thus the even-\(m\) subsequence has an integral parity gap of order
\(W\), not a small divisibility residue. Fractional orbit weights can
hide the obstruction---for example, a factor \(1/2\) changes an even
orbit incidence vector into an integral candidate---but Boolean
activation cannot. Any surviving construction must break at least one
of the following hypotheses on a linear owner scale: full \(BA\)-orbit
activation, strict alternation of the source and \(A\)-successor shores,
or use of only nonnegative canonical owner incidences.
