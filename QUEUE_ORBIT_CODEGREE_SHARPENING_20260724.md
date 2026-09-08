# Sharp weighted codegrees for the monotone queue orbit

This note isolates what can and cannot be gained by reweighting the
monotone-profile queue atom.  It gives a substantially sharper codegree
estimate than the union bound used in the quantitative growing-depth proof.
It does **not** prove the missing integral rounding theorem.

Throughout

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \mu_q={W\over N_q}.
\]

An atom has starts `0 <= t < H`.  Its real slot of signed depth `s` is

\[
 B_{t,s}=\{z_{t-s},z_{t-s+1},\ldots,z_{t+m-1}\},
 \qquad -d\le s\le d,
\tag{1}
\]

whenever that slot is active.  We use the symmetric fractional matching from
the dummy-completed construction: choose the coordinate permutation
uniformly, choose any profile law independently of the permutation, and put

\[
 x_e={W\over H}\Pr(E=e).
\tag{2}
\]

The usual monotone quota law is one instance.  The upper bound below only
uses that a slot is either present or absent, so it also applies to arbitrary
random quota profiles independent of the coordinate permutation.

## 1. Interval-pair lemma

Assume

\[
 H+3d\le m.
\tag{3}
\]

This holds with enormous room in every proposed tail-threshold application,
where `H,d=m^{1/2+o(1)}`.

For fixed signed depths `s,r`, put

\[
 P_{t,s}=[t-s,t+m-1].
\]

### Lemma 1

Fix integers `a,b >= 0` with `a+b>0`.  For each fixed `t`, at most two
values of `u` satisfy

\[
 |P_{t,s}\setminus P_{u,r}|=a,\qquad
 |P_{u,r}\setminus P_{t,s}|=b.
\tag{4}
\]

#### Proof

Condition (3) implies that any two active intervals overlap: their left
endpoints differ by at most `H-1+2d`, while either interval has length at
least `m-d`.

Write `c=|P_{t,s}\cap P_{u,r}|`.  Then `c=m+s-a=m+r-b` is fixed.  Two
overlapping intervals of fixed lengths and fixed intersection length can be
placed relative to one another in at most two ways: the second interval
extends to the left of the first, or to its right.  Thus there are at most
two possible relative shifts `u-t`.  QED

## 2. The symmetric orbit has codegree independent of `H`

For two distinct augmented vertices `A,B`, write

\[
 c_x(A,B)=\sum_{e\supseteq\{A,B\}}x_e,
 \qquad \alpha(x)=\max_{A\ne B}c_x(A,B).
\]

### Theorem 2 (real--real upper bound)

Under (3), for two distinct real central-band masks,

\[
 \boxed{c_x(A,B)\le {2\mu_d\over m-d}.}
\tag{5}
\]

In particular this bound is independent of the number `H` of starts.

#### Proof

The cardinalities of `A` and `B` uniquely determine their signed rows, say
`m+s` and `m+r`.  For a proposed ordered slot pair `(t,s),(u,r)`, let

\[
 a=|P_{t,s}\setminus P_{u,r}|,
 \qquad b=|P_{u,r}\setminus P_{t,s}|.
\]

Conditioned on `z(P_{t,s})=A`, compatibility is necessary, and when it
holds

\[
 \Pr(z(P_{u,r})=B\mid z(P_{t,s})=A)
 =\left[
 \binom{m+s}{|A\cap B|}
 \binom{m-s}{|B\setminus A|}
 \right]^{-1}.
\tag{6}
\]

Equivalently the two lower entries are `a` and `b`.  The case `a=b=0`
would make the two position intervals equal; then compatibility would force
`A=B`, which is excluded.  At least one binomial coefficient in (6) is
therefore nontrivial.  Both top parameters are at least `m-d`, so (6) is at
most `1/(m-d)`.

For each `t`, Lemma 1 leaves at most two possible values of `u`.  There are
at most `2H` compatible ordered slot pairs altogether.  Slot activity can
only decrease their probability, while

\[
 \Pr(z(P_{t,s})=A)=1/N_{|s|}.
\]

Consequently

\[
 \Pr(A,B\in E)\le {2H\over N_{|s|}(m-d)}.
\]

Multiplying by `W/H` as in (2), and using
`W/N_{|s|}<=mu_d`, proves (5).  QED

### Dummy pairs

For the standard dummy classes, `R_q=W-N_q >= R_1=W/(m+1)`.  The same
conditioning as in the quantitative proof gives

\[
 c_x(A,y)
 \le {HW\over N_dR_1}
 =O\!\left({H\mu_d m\over W}\right)
\tag{7}
\]

for a real vertex and a dummy vertex, and

\[
 c_x(y,y')=O\!\left({Hm^2\over W}\right)
\tag{8}
\]

for two distinct dummies.  In the same dummy class the exact conditional
probability is `b_q(b_q-1)/(R_q(R_q-1))`; using sampling without replacement
only improves (8).

Thus, whenever `H,mu_d=m^{o(1)}`,

\[
 \boxed{\alpha(x)\le {2\mu_d\over m-d}+e^{-\Omega(m)}.}
\tag{9}
\]

This replaces the earlier crude `H/(m-d)` estimate.

## 3. No exact fractional reweighting can beat the `1/m` scale

The preceding upper bound is close to the best possible order at shallow
depth, and this fact does not depend on symmetry.

### Theorem 3 (universal first-row lower bound)

Consider any nonnegative fractional weighting of augmented queue atoms that
has fractional degree one at every middle mask and every rank-`m-1` real
mask.  Assume that every active first-lower-row occurrence is retained
together with its same-start middle mask.  Then

\[
 \boxed{\max_{A,F} \sum_{e\supseteq\{A,F\}}x_e
 \ge {1\over m+1},}
\tag{10}
\]

where the maximum may be restricted to nested pairs
`F subset A`, `|F|=m-1`, `|A|=m`.

#### Proof

Every active first-lower slot contributes one same-start nested pair.  Since
the fractional degree of every rank-`m-1` real vertex is one, the total
weight of these pair occurrences is

\[
 N_1=\binom{2m}{m-1}.
\]

The number of nested pairs is

\[
 N_1(m+1)=Wm.
\]

The average same-start pair weight is therefore exactly `1/(m+1)`.  The
full edge codegree is at least its same-start contribution, proving (10).
QED

The symmetric orbit hence satisfies, in the regime (3),

\[
 {1\over m+1}\le \alpha(x)
 \le {2\mu_d\over m-d}+e^{-\Omega(m)}.
\tag{11}
\]

At

\[
 d=(1+o(1))\sqrt{m\log\log m},
\]

the binomial ratio gives `mu_d=(log m)^{1+o(1)}`.  Thus

\[
 m^{-1+o(1)}\le\alpha(x)\le m^{-1+o(1)}.
\tag{12}
\]

In exponent scale the symmetric weighting is already optimal; a different
fractional weighting can save at most a subpolynomial factor.

## 4. Consequence for the missing rounding theorem

Take the natural tail-threshold parameters

\[
 d=(1+o(1))\sqrt{m\log\log m},\qquad
 H=\sqrt m\,f(m),\qquad
 \sqrt{\log\log m}\ll f(m)\ll\sqrt m.
\]

Then the independently initialized literal reset ratio is `d/H=o(1)`, and
the real incidence size is

\[
 K_{\rm real}=(\sqrt\pi+o(1))mf(m).
\tag{13}
\]

Theorem 2 improves the available weighted-codegree estimate from
`O(f(m)/sqrt(m))` to

\[
 \alpha(x)=O(\log m/m).
\tag{14}
\]

This is a real structural gain: long queue paths do not themselves create
large pair-codegrees.  The obstruction in the one-shot ABKV proof is
therefore the huge all-row edge uniformity, not the path length.

It still does not make that black box sufficient.  Any displayed residual
of the form

\[
 \operatorname{poly}(K)\,\alpha^{c/K}
\]

is `1-o(1)` when `K=Theta(mf(m))` and
`log(1/alpha)=Theta(log m)`.  Meanwhile the queue ledger needs an uncovered
fraction `o(m^{-1/2})` of its `Theta(sqrt(m)W)` real vertices.  Theorem 3
also shows that fractional reweighting alone cannot turn `alpha` into
`exp(-Omega(K))`.

Accordingly, a successful next theorem must use more than a smaller maximum
pair-codegree.  It must round the rows hierarchically under common middle
ownership, use an absorber/switching system, or share resets in a way that
removes the `K=Omega(m)` one-shot edge.

## 5. A sharp black-box counterexample

There is a stronger reason not to expect a theorem based only on edge size,
exact fractional degrees, and weighted pair-codegree.  Those three parameters
can match the queue scale while the integral matching number is one.

Let `Pi` be a projective plane of prime-power order `q`.  It has

\[
 n_0=q^2+q+1
\]

points and the same number of lines; every line has

\[
 k_0=q+1
\]

points, every point lies on `k_0` lines, and two lines meet.

Take `f` disjoint copies of the point set.  A hyperedge is a tuple of one
line from each copy, regarded as their union.  Thus

\[
 K=fk_0.
\tag{15}
\]

Give every such edge the weight

\[
 w={1\over k_0n_0^{f-1}}.
\tag{16}
\]

### Proposition 4

This hypergraph has an exact fractional perfect matching, maximum weighted
pair-codegree

\[
 \alpha={k_0\over n_0}
 ={1+O(1/q)\over k_0},
\tag{17}
\]

and its ordinary matching number is one.

#### Proof

A point is contained in `k_0 n_0^{f-1}` edge tuples, so its fractional
degree under (16) is one.

Two distinct points in the same copy determine a unique line.  They are
therefore together in `n_0^{f-1}` edge tuples, of total weight `1/k_0`.
Two points in different copies are together in
`k_0^2 n_0^{f-2}` edge tuples, of total weight `k_0/n_0`.  Since
`k_0^2>n_0`, this is the maximum (and is only a `1+O(1/q)` factor above
`1/k_0`).
This proves (17).

Finally, any two edge tuples contain two lines in each projective-plane
copy, and those two lines intersect.  In particular any two hyperedges
intersect, so the matching number is one.  QED

Taking `k_0=Theta(m)` and allowing `f=f(m)` gives simultaneously

\[
 K=Theta(mf),\qquad \alpha=Theta(1/m),
\tag{18}
\]

which is precisely the exponent scale of the proposed tail-threshold queue
orbit.  Nevertheless the fractional-to-integral gap is maximal.

This is **not** a counterexample to queue rounding: projective-plane products
do not have queue interval geometry.  It is a counterexample to any claimed
rounding principle whose hypotheses remember only `K`, fractional vertex
degrees, and weighted pair-codegrees.  A valid positive theorem must name
and use additional structure, such as switchable interval endpoints,
successive-row conditional expansion, or an explicit absorber.

## Status

* Proved: the interval-pair lemma; the `O(mu_d/m)` symmetric weighted
  codegree; the universal `1/(m+1)` lower bound; the projective-plane
  black-box counterexample.
* Not proved: an integral matching or cover at the tail threshold.
* Scope: (10) is an obstruction to improving the fractional pair-codegree
  scale by reweighting.  It is not a nonexistence theorem for structured
  integral queue packings.
