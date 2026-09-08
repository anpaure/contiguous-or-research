# Audit of the capacity, calibration, hash, and orbit claims

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The edge-transitive fractional-capacity identity is exact.  The claimed
middle-versus-row calibration is also exact after correcting the rank
index and distinguishing exact coverage from floor-rounded coverage.  The
characteristic-two warning is correct, but replacing the second power sum
by the elementary symmetric function does not by itself prove the stated
collision bound: one must rule out an identically zero difference
polynomial.  Finally, a small vertex orbit can be the unique capacity
bottleneck, whereas a small edge orbit in a union of edge orbits need not
control the optimized fractional capacity.

## 1. Exact edge-transitive fractional matching number

Let a finite group act transitively on the labelled edges of a finite
multihypergraph `H`.  Let `O` range over its vertex orbits, and let

\[
 a_O=|e\cap O|
\]

for one, hence every, edge `e`.  Orbits with `a_O=0` are omitted.  Double
counting incidences gives the common degree on `O`:

\[
 d_O={|E|a_O\over|O|}.
\]

Thus

\[
 \Delta=\max_O d_O,
 \qquad
 {|E|\over\Delta}=\min_O{|O|\over a_O}.
 \tag{1.1}
\]

### Proposition 1.1

For the ordinary vertex-capacity-one fractional matching LP,

\[
 \boxed{
 \nu^*(H)={|E|\over\Delta}
          =\min_O{|O|\over a_O}.}
 \tag{1.2}
\]

#### Proof

The constant edge weight `1/Delta` is feasible because every vertex degree
is at most `Delta`, and has mass `|E|/Delta`.  Conversely, for every
fractional matching `x`, summing the capacity inequalities over `O` gives

\[
 a_O\sum_ex_e\le|O|.
\]

Minimize over `O`. \(\square\)

This remains true with labelled parallel edges.  If an edge contains a
resource with multiplicity, that resource must instead be represented by
labelled capacity copies or the multiplicity must be included in `a_O`;
ordinary simple-edge notation silently collapses it.

## 2. Exact middle/row calibration

Let the middle vertex orbit have size

\[
 W=\binom nm
\]

and suppose every interval-template edge contains exactly `a_m=n`
distinct middle targets.  Let a rank-`r` vertex orbit have size

\[
 N_r=\binom nr
\]

and let every template edge contain `a_r` distinct protected targets from
that orbit.  The orbit degrees are

\[
 d_m={|E|n\over W},\qquad
 d_r={|E|a_r\over N_r}.
\]

Therefore

\[
 \boxed{
 d_r\le d_m
 \quad\Longleftrightarrow\quad
 {a_r\over n}\le {N_r\over W}.}
 \tag{2.1}

Now suppose exactly

\[
 C_m={W\over n}
\]

template edges are selected and their protected rank-`r` targets cover
all `N_r` vertices.  Slot counting gives

\[
 C_ma_r\ge N_r,
\]

or

\[
 \boxed{{a_r\over n}\ge {N_r\over W}.}
 \tag{2.2}

Hence middle capacity and exact full row coverage are co-critical:
together they force equality in (2.1)--(2.2).

There are four qualifications.

1. If `n=2m`, the complement-paired notation `m-j,m+j` is correct and
   \[
   {\binom{2m}{m-j}\over\binom{2m}m}
   =\exp\left[-{j^2\over m}
      +O\left({j^3\over m^2}+{j\over m}\right)\right].
   \]
   But `C_m=W/n` need not be an integer, so "exactly `C_m` edges" must
   then be interpreted as a fractional-mass calculation or replaced by an
   integral rounded count.  In odd dimension `n=2m+1`, the
   complement-paired ranks are
   `m-j` and `m+1+j`, not `m-j` and `m+j`.  The former have the common
   cardinality
   \[
   N_j=\binom n{m-j}=\binom n{m+1+j}.
   \]
   If the intended upper row is actually `m+j`, its own binomial size
   must be used.
2. In that odd case, uniformly for `j=o(m^{2/3})`,
   \[
   {N_j\over W}
   =\exp\left[-{j(j+1)\over m}
        +O\left({j^3\over m^2}+{j\over m}\right)\right].
   \tag{2.3}
   \]
   The shorthand `exp(-j^2/m)` is valid on fixed Gaussian windows only
   up to a `1+o(1)` factor.
3. Coverage by `(1+epsilon)C_m` edges changes (2.2) to
   `a_r/n >= (N_r/W)/(1+epsilon)`.  Allowing holes or incidental
   unclaimed witnesses changes it again.
4. Exact equality need not be integral.  The capacity-safe choice
   \[
   a_r=\left\lfloor{nN_r\over W}\right\rfloor
   \tag{2.4}
   \]
   leaves fewer than `C_m=W/n` scalar slots at that row.  Across
   `Q=o(n)` rows this floor leave is `o(W)`.  Thus the audited
   construction correctly uses floor calibration rather than claiming
   literal equality at every row.

If targets are complement-paired atoms, the atom orbit size and the number
of atoms claimed per edge must be used consistently.  One cannot mix the
mask count on one side with the atom count on the other.

## 3. The characteristic-two correction

Let `h(x)` take values in a field of characteristic two and define power
sums

\[
 \chi_1(S)=\sum_{x\in S}h(x),\qquad
 \chi_2(S)=\sum_{x\in S}h(x)^2.
\]

Frobenius additivity gives

\[
 \boxed{\chi_2(S)=\chi_1(S)^2.}
 \tag{3.1}
\]

So `(chi_1,chi_2)` is only one invariant, not a two-moment hash.  A valid
second symmetric invariant is

\[
 e_2(S)=\sum_{\{x,y\}\subseteq S}h(x)h(y).
 \tag{3.2}
\]

However, a claimed Vandermonde or degree-two collision bound requires more
than replacing `chi_2` by `e_2`.  If two structured target traces give
coefficient vectors `c(S)` and `c(T)`, their collision equation is a
polynomial of degree at most two only after an exact trace calculation.
The bound "at most two phases" follows only when that difference
polynomial is nonzero.  Equivalently, the relevant coefficient map must be
injective on the compared trace types (or its zero fibres must be audited
separately).  In characteristic two, a nonzero quadratic still has at most
two roots; the danger is the identically zero polynomial, not the usual
root bound.

Also, a nonzero constant-step arithmetic progression in **any**
characteristic-two field has period two, because `2 alpha=0`.  Passing from
`F_2` to `F_{2^s}` does not repair that particular construction.  An
extension field can support a long polynomial-evaluation hash only if the
phases are assigned distinct field parameters by a different rule and the
trace is recomputed as a polynomial in that parameter.  If the proof needs
literal constant-step progressions, it must use odd characteristic (with
the characteristic at least the desired progression length), and the
physical label-class capacities must be rechecked.

## 4. Small orbits and invariant excision

A small **vertex** orbit can determine the entire capacity.  For example,
if every edge contains one tag from an orbit of size `T`, then (1.2) gives

\[
 \nu^*(H)\le T
\]

regardless of how large every other target orbit is.  What matters is the
ratio `|O|/a_O`, not the fraction of all vertices or all displayed claims
lying in `O`.

This is especially important for hashes.  A hash **part** is a partition
class of physical target vertices, not a consumable resource.  If the
`p` hash labels themselves are incorrectly inserted as capacity vertices
and a hash-rainbow edge contains all `p` labels, then (1.2) gives

\[
 \nu^*(H)\le {p\over p}=1.
\]

Even one auxiliary hash-label vertex per edge would cap the matching by
the number of labels.  Hashes may index or stratify physical resources;
they cannot be promoted to shared matching vertices unless that reuse
restriction is genuinely intended.

The corresponding statement for a small **edge** orbit is different.  In
a union of several edge orbits, the raw maximum degree of the unweighted
union may be caused by one small orbit, but the optimized fractional
matching may downweight or ignore it.  Formula (1.2) is a one-edge-orbit
theorem and cannot be applied to the union without solving the orbit-weight
LP.

Explicitly, if `E_j` are edge orbits and every edge of `E_j` contains
`a_{jO}` vertices from vertex orbit `O`, an orbit-constant fractional point
with per-edge weight `x_j` obeys

\[
 \sum_j x_j{|E_j|a_{jO}\over|O|}\le1
 \qquad\text{for every }O,
 \tag{4.1}
\]

and maximizes `sum_j x_j|E_j|`.  A low-total-mass edge orbit can still be
binding if its incidence is concentrated on a tiny required vertex orbit,
but this is decided by (4.1), not by the raw maximum degree of the
unweighted union.

Finally, a proper deterministic edge deletion inside one transitive edge
orbit cannot remain invariant under the full group: the only invariant
subsets are the empty set and the full orbit.  One may

* discard whole edge orbits from a union of orbits;
* pass to a subgroup and recompute its split vertex and edge orbits; or
* make a noninvariant pruning and abandon the exact transitive formulas.

"Invariant in distribution" is not enough for a realized residual.  Any
claim that pruning preserves (1.2), the exact degree calibration, or the
weighted translate lemma must specify which literal group still acts
transitively after the pruning.

## 5. Final verdict

The correct exact core is

\[
 \boxed{
 \nu^*(H)=\min_O{|O|\over a_O},\qquad
 {a_r\over n}\le{N_r\over W}
 \text{ for middle-controlled capacity}.}
\]

Exact `C_m`-edge coverage forces the reverse row inequality, so the two
requirements meet at equality before integer rounding.  The floor error is
small enough in aggregate, but it is real.  Characteristic-two power sums
need the `e_2` correction plus a nondegeneracy proof.  Orbit excision and
low-mass claims must be interpreted at the level of literal vertex and
edge orbits, not averaged informally.
