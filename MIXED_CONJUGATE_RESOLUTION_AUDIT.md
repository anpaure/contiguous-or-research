# Audit of the mixed-conjugate resolution scheme

## 1. Accepted statements

This audit accepts the following as proved in
`MIXED_CONJUGATE_RESOLUTION.md`:

* the exponential large-cell tail for the last-`DU` partition;
* the simultaneous one-point degree law under full coordinate conjugation;
* the diagonal-orbit codegree identity and its stated parameter bounds;
* exact fractional completion by repair singletons;
* rigidity of exact trades between two partitions.

It does **not** accept an integral resolution.  The Mixed-Conjugate
Resolution Conjecture remains precisely the missing step.

## 2. Large-cell tail

For one critical word of length `a`, last-one position gives

\[
 P(\delta=t)=2^{-t}\ (t<a),\qquad P(\delta=a)=2^{1-a}.
\]

Thus a fixed exponential moment below `log 2` is bounded independently of
`a`.  Critical words use disjoint orientation bits, so their deficits are
independent within an orbit.  With at most `d/2` words, Chernoff gives
`exp(-Omega(m))` probability of a linear deficit whenever
`d<=m^(2/3)`.  The separately proved radius and `DU` tails are respectively
`W exp(-Omega(m^(1/3)))` and `exp((log4-c)m)`.  Therefore the combined
exception is indeed `W exp(-Omega(m^(1/3)))`, which is `o(W/H)` at every
polynomial `H`.

No Markov-only estimate is used in the mixed scheme.

## 3. Radius transport

A permutation `pi` generally changes the original RSK shape of `X`.
The scheme does not assert otherwise.  It transports the label `d(B)` with
the complete block `B`.  Since the base counts of transported labels are
`a_d`, uniform conjugation gives `a_d/W` fractional mass of label `d` at
every middle vertex.  These are exactly the SCD chain-radius quotas.

Thus “radius-resolved” means constant transported block type plus correct
global quotas, not invariance of fixed-order RSK under `S_(2m)`.

## 4. Degree-law double count

For a transitive finite group acting on a class `Omega`, the average over
all conjugates of a base multiset `A` has degree `|A|/|Omega|` at every
point.  Apply this once to the `W-E` good middle occurrences and once to the
`G_q` lower or upper depth-`q` occurrences.  This gives exactly

\[
 (W-E)/W,\qquad G_q/N_q.
\]

Restricting the middle count to radius `d` gives `g_d/W`.  If `E=0`, the
telescoping identity `sum_(d>=q)a_d=N_q` makes every typed degree one.

This calculation uses all ordered matching frames.  A uniform bare perfect
matching, with no order or within-pair orientation, is not enough to justify
the RSK-radius count.

## 5. All depths are genuinely coupled

One real hyperedge contains:

* all `R` middle starts of one physical cyclic block;
* all `R` lower shadows and all `R` upper shadows at every depth certified
  by that block's one radius label.

Consequently an integral hypergraph matching can never select a depth-one
choice independently of its depth-two choice.  The formulation avoids the
invalid stitching step by construction.

## 6. Codegree audit

For a diagonal pair orbit `O`, orbit--stabilizer gives

\[
 \codeg_x(u,v)=|O|^{-1}\sum_B c_O(B).
\]

For middle distance `r`, `|O|=W binom(m,r)^2` and the base blocks contain at
most `W(R-1)` ordered pairs, proving `(R-1)/binom(m,r)^2`.

For a middle--depth-`q` pair, the continuation orbit of a fixed middle set
has at least `binom(m,q)` members and the base numerator is at most `WR`,
giving `R/binom(m,q)`.

There is a potential false shortcut for target--target pairs: arbitrary
opposite near-middle ranks possess complementary orbits with only one
continuation.  Those orbits cannot occur inside a base block, because all
typed vertices of that block share a fixed included core of size
`m-ell`.  For nonzero numerator orbits, the closest distinct/nested case has
at least `Theta(m)` continuations.  This validates the conservative bound

\[
 O(R e^{H^2/m+o(1)}/m).
\]

The condition `R e^(H^2/m)=o(m)` is therefore a real parameter restriction,
not an automatic consequence of `R=o(m)`.

## 7. Fractional repair accounting

Adding singleton mass equal to each degree deficit saturates every typed
vertex.  The total mass is

\[
 E+2\sum_{q<=H}\sum_{d>=q}e_d\le(2H+1)E=o(W).
\]

This proves a low-cost fractional perfect matching.  It does not prove that
an integral perfect matching uses comparably few singletons; that assertion
is exactly an integrality-gap/absorption conjecture.

## 8. Birkhoff and trade scope

For two partitions, exact coverage equations are `x_P+y_Q=1` on every edge
of their overlap graph.  They force one left/right choice per connected
component.  Thus averaging two partitions does not manufacture local
whole-cell trades.

At the decorated level, an individual conjugate block partition is usually
not a typed matching because shadows repeat across blocks.  Therefore the
uniform fractional vector is not a convex combination of integral typed
matchings, and Birkhoff--von Neumann is inapplicable.

## 9. Remaining risk

The real edges have growing size `R(1+2H)`, and the typed universe has
`Theta(W sqrt m)` vertices.  Ordinary small-codegree near-matching results
typically control a relative error in that larger universe; even an
`o(W sqrt m)` leftover is insufficient.  The desired theorem needs repair
cost `o(W)` and must preserve complete decorated blocks.

Accordingly the document supplies a rigorous all-dimensional fractional
scheme and an exact integral target, not a proof of asymptotic optimality.
