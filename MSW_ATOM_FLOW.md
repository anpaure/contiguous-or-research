# The MSW wreath factor and the exact vertical atom-flow obstruction

This note replaces the formerly conjectural middle-wreath packing step by an
exact theorem, and then isolates the remaining vertical problem on that fixed
skeleton.  The main point is that the vertical integrality problem is a tower
of ordinary bipartite perfect matchings.  Its shallow levels are, however,
asymptotically degree one, so a generic fractional or expansion argument has
essentially no room to round.

Throughout,

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 N_q=\binom{n}{m-q}=\binom{n}{m+1+q}.
\tag{0.1}
\]

## 1. The middle wreath factor is already exact

Mütze, Standke and Wiechert prove that the odd graph

\[
 O_{m+1}=KG(2m+1,m)
\]

has a factor into cycles of length `2m+1`; see Theorem 4 of *A
minimum-change version of the Chung--Feller theorem for Dyck paths*.
There are exactly

\[
 \frac{W}{2m+1}=\operatorname {Cat}_m
\tag{1.1}
\]

cycles.

Every such minimum odd cycle is a literal wreath.  If its vertices in odd
graph order are `A_0,...,A_(n-1)` and

\[
 z_i=[n]\setminus(A_i\cup A_{i+1}),
\tag{1.2}
\]

then equality in the odd-girth argument gives

\[
 A_i=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\}.
\tag{1.3}
\]

The labels `z_i` are all distinct.  Reading them in step-two order therefore
turns the vertices into all cyclic intervals of length `m` in one cyclic
coordinate order.  Thus the MSW factor is an exact partition of the entire
middle layer into `Cat_m` wreaths.  No asymptotic hypergraph packing theorem
is needed for the middle layer.

For reference, in the MSW construction a Dyck path `x` of length `2m`
generates a column

\[
 x_0=x,\ x_1=f(x),\ldots,x_m=f^m(x)=\overline x.
\tag{1.4}
\]

Writing `y_e=g(x_e)`, their odd cycle is

\[
 x_0,\ \overline{y_0}\cup\{z\},\ x_1,
 \ \overline{y_1}\cup\{z\},\ldots,
 \overline{y_{m-1}}\cup\{z\},\ x_m.
\tag{1.5}
\]

The omitted labels in (1.2) are the arrival and departure coordinates of
the successive minimum-change swaps, followed by `z`.  Lemma 12 of the MSW
paper says that these are a permutation of the `2m+1` coordinates, which is
also a direct proof of (1.3) for their factor.

## 2. Vertical interval chains on a fixed factor

Let `Omega` be the set of all pointed starts in the wreath factor.  Thus
`|Omega|=W`.  For a start `v=(pi,j)` define

\[
 L_q(v)=I_\pi(j,m-q),\qquad
 U_q(v)=I_\pi(j,m+1+q).
\tag{2.1}
\]

The sets

\[
 L_d(v)\subset\cdots\subset L_0(v)
 \subset U_0(v)\subset\cdots\subset U_d(v)
\tag{2.2}
\]

form a saturated symmetric chain of radius `d`.

For every `q`, form the bipartite multigraph `G_q`.  Its left side is rank
`m-q`, its right side is rank `m+1+q`, and every start `v in Omega` supplies
the edge

\[
                         L_q(v)U_q(v).
\tag{2.3}
\]

In particular `G_q` has `W` labelled edges and `N_q` vertices on each side.

### Theorem 1 (nested-matching normal form)

A radius assignment

\[
                         d:\Omega\longrightarrow\{0,\ldots,H\}
\]

makes the interval chains (2.2) partition every rank in the central band if
and only if the nested edge sets

\[
 A_q=\{v:d(v)\ge q\},\qquad
 \Omega=A_0\supseteq A_1\supseteq\cdots\supseteq A_H,
\tag{2.4}
\]

satisfy

\[
 \boxed{\ G_q[A_q]\text{ is a perfect matching for every }q.\ }
\tag{2.5}

Here `G_q[A]` means that only the labelled edges corresponding to starts in
`A` are retained.

#### Proof

At lower rank `m-q`, the radius-assigned chains contain precisely the sets
`L_q(v)` with `v in A_q`.  They partition that rank exactly when the map
`v -> L_q(v)` is bijective.  The identical statement on the upper side is
that `v -> U_q(v)` is bijective.  Both statements together say precisely
that the labelled edges `A_q` form a perfect matching in `G_q`.  Nesting is
equivalent to the fact that a chain reaching depth `q+1` also reaches depth
`q`.  QED.

The radius counts are automatic:

\[
 |A_q|=N_q,\qquad
 |\{v:d(v)=q\}|=N_q-N_{q+1}.
\tag{2.6}
\]

Thus (2.6) is exactly the symmetric-chain radius law, now integrally rather
than fractionally.

### Corollary 2 (sequential Hall criterion)

Suppose `A_(q-1)` has already been chosen.  It extends through depth `q` if
and only if the restricted graph

\[
                         G_q[A_{q-1}]
\tag{2.7}
\]

has a perfect matching.  Any such perfect matching may be taken as `A_q`.

Consequently vertical resolution on a fixed exact wreath factor is a tower
of ordinary bipartite matching/flow problems.  There is no growing-uniformity
hypergraph in this formulation.  The difficulty is that the choice at one
level changes the edge reservoir at every later level.

## 3. The shallow matching graphs are forced to be almost bijections

The sequential formulation exposes a rigidity hidden by the fractional
radius law.

### Theorem 3 (degree-one rigidity)

Assume `A_(q-1)` extends through depth `q`.  Then on either side of
`G_q[A_(q-1)]`, at least

\[
 N_q-(N_{q-1}-N_q)
\tag{3.1}
\]

vertices have degree exactly one.  Equivalently, the proportion of vertices
which can have degree at least two is at most

\[
 \frac{N_{q-1}-N_q}{N_q}
   =\frac{2q}{m-q+1}.
\tag{3.2}
\]

#### Proof

The restricted graph has exactly `|A_(q-1)|=N_(q-1)` edges.  A perfect
matching implies that no vertex is isolated.  On either side,

\[
 \sum_x(\deg x-1)=N_{q-1}-N_q.
\]

Every vertex of degree at least two contributes at least one to this sum,
which proves (3.1).  The binomial ratio

\[
 \frac{N_{q-1}}{N_q}
   =\frac{m+q+1}{m-q+1}
\]

gives (3.2).  QED.

For every `q=o(m)`, almost every target therefore has a **unique** eligible
occurrence before the depth-`q` matching is chosen.  A random or Poisson
reservoir of mean about one is qualitatively wrong: it leaves a constant
fraction of isolated targets.  The required object must already be a
near-rainbow bijection at every shallow depth.  The exact size-bias identity
in `MIXED_PAIR_ROUNDING.md` balances first moments but does not supply this
degree-one organization.

This is the precise atom-first obstruction.  Ordinary flow solves each
level once its nearly bijective incidence graph is present; producing those
graphs coherently for `H=sqrt(m) omega(1)` is the remaining theorem.

## 4. The particular MSW factor is not vertically complete

The existence of the exact middle factor must not be confused with vertical
coverage.  The MSW factor itself already misses interval shadows.

On the even core, the adjacent unions of the column paths (1.4) are

\[
                         x_e\cup x_{e+1}=y_e=g(x_e).
\tag{4.1}
\]

The map `g` is a bijection from all balanced paths except the last flaw
class to the rank-`m+1` paths.  Hence these adjacent unions enumerate rank
`m+1` exactly.  The adjacent intersections do not enjoy the dual statement.
Already for `m=3` they cover only 13 of the 15 rank-two subsets.

For the literal odd wreath factor, exhaustive reconstruction from (1.5) gives
the following numbers of distinct rank-`m-1` intervals:

\[
\begin{array}{c|rrrrrr}
m&4&5&6&7&8&9\\ \hline
\text{covered}&80&298&1111&4168&15739&59771\\
N_1&84&330&1287&5005&19448&75582
\end{array}
\tag{4.2}
\]

For `m=4`, the four absent triples are

\[
 \{1,4,7\},\quad\{2,5,8\},\quad
 \{2,5,9\},\quad\{4,7,9\}.
\tag{4.3}
\]

The program `msw_shadow_test.cpp` reconstructs `f`, the odd cycles, their
omitted-label cyclic orders, and checks every interval independently.  The
table is computational evidence, not an asserted asymptotic formula.  The
single finite counterexample (4.3) is enough to disprove the claim that the
published factor itself is automatically a cyclic-interval SCD resolution.

## 5. Local cycle switches cannot repair a macroscopic shadow defect

There is a simple stability bound which should govern any attempt to repair
the factor by the switches used in odd-graph Hamiltonicity proofs.

### Lemma 4 (window-switch bound)

Change `s` transitions in a collection of directed middle paths/cycles.  At
depth `q`, at most `qs` old starting windows and at most `qs` new starting
windows contain a changed transition.  Consequently the number of newly
covered lower targets, or newly covered upper targets, is at most `qs`.

#### Proof

A fixed changed transition lies in exactly `q` windows of `q` transitions,
counting cyclically and with multiplicity.  A union bound over the changed
transitions proves the assertion.  QED.

If a starting factor misses `D_q` targets of one sign at depth `q`, every
repair using fewer than `D_q/q` changed transitions still misses at least one
of them.  In particular, should the numerical trend (4.2) be proved to be a
positive-density deficit, it would rule out every `o(W/H)`-switch repair at
all fixed `q<=H`.  One would need a genuinely global re-factorization, not
the `O(W/n)` switches used merely to join the MSW cycles.

## 6. Exact successor theorem

After the MSW theorem, the central-band problem can be stated without any
generic block-packing conjecture.

> **Nested-rainbow factor theorem.**  Modify or replace the exact MSW wreath
> factor so that its graphs `G_q`, for
> `1<=q<=H=sqrt(m) omega(1)`, admit nested perfect matchings as in
> (2.4)--(2.5), with total unmatched rank vertices `o(W)` in the approximate
> version.

Combined with `TRUNCATED_IDEAL_PRODUCT.md`, the approximate version already
implies a universal OR word of length `W+o(W)`.  The new formulation separates
the tasks cleanly:

* the middle factor is solved exactly by MSW;
* the radius ledger is solved exactly by (2.6);
* each integral extension step is an ordinary bipartite matching;
* the unsolved content is coherent near-bijectivity of all the shallow
  interval-shadow maps.

This is strictly sharper than asking for a black-box rounding of the large
typed hypergraph.  It also says what a successful construction must look
like: not merely expanding, but almost one-to-one at every central depth.

## 7. For the OR problem, a low-collision factor is enough

The nested tower is the exact atom-first formulation for an SCD, but it is
still stronger than the original OR problem.  Erosion does not consume a
shadow after using it once.  Every start may supply a window at every depth,
and repeated values are harmless except insofar as they force other values to
be absent.

For a wreath factor `F`, let

\[
 \mu_q^-(S)=|\{v:L_q(v)=S\}|,
 \qquad
 \mu_q^+(S)=|\{v:U_q(v)=S\}|,
\tag{7.1}
\]

and put

\[
 M_q^\pm=N_q-|\{S:\mu_q^\pm(S)>0\}|.
\tag{7.2}
\]

Thus `M_q^pm` is the actual number of missing interval shadows.  The weakest
sufficient vertical statement is simply

\[
 \boxed{
   \sum_{q=0}^{H}(M_q^-+M_q^+)=o(W).
 }
\tag{7.3}
\]

Indeed, for each wreath order write its intervals of length `m-H` and repeat
the first `2H+1` entries.  Consecutive ORs give every fixed-start interval in
the band.  The total word length is

\[
 W+(2H+1)\frac{W}{2m+1}.
\tag{7.4}
\]

Append the masks missing in (7.3), and then append the two-tail word from
`TRUNCATED_IDEAL_PRODUCT.md`.  That note is stated on the even core `2m`.
To obtain an odd-dimensional tail word, apply the usual one-bit lift to the
even tail word: if `B` is the even word and `z` is the new coordinate, use

\[
 B\ \Vert\ [\{z\}]\ \Vert\
 [\{z\}\cup B_i:1\le i<|B|].
\tag{7.5}
\]

The standard suffix argument works for this partial target family exactly as
it does for a universal word.  Every odd target outside the displayed central
band has an even part in one of the two even tails.  The lifted tail still has
length `o(W)`.  For

\[
 H=\sqrt{m\,\omega(m)},\qquad \omega(m)\longrightarrow\infty
\quad\hbox{and}\quad H=o(m),
\tag{7.6}
\]

both the seam term in (7.4) and the tail word are `o(W)`.  Condition (7.3)
therefore proves

\[
                         \nu(2m+1)=W+o(W).
\tag{7.7}
\]

There is an exact collision statistic for (7.3).  Define

\[
 C_q^\pm=\sum_S\binom{\mu_q^\pm(S)}2.
\tag{7.8}
\]

Because there are `W` occurrences distributed among `N_q` possible targets,

\[
 \boxed{
 C_q^\pm-(W-N_q)
   =M_q^\pm+
     \sum_{S:\mu_q^\pm(S)\ge3}
       \binom{\mu_q^\pm(S)-1}{2}.
 }
\tag{7.9}

To prove (7.9), subtract from each nonzero multiplicity `d` its unavoidable
duplicate excess `d-1`; the residue is
`binom(d,2)-(d-1)=binom(d-1,2)`, while the `M_q^pm` absent targets account
for the difference between `W-N_q` and total duplicate excess.

Identity (7.9) is useful only in the shallow range.  The previously proposed
all-depth condition

\[
 \sum_{q=0}^{H}\sum_{\epsilon\in\{-,+\}}
   \bigl(C_q^\epsilon-(W-N_q)\bigr)=o(W)               \tag{7.10}
\]

is **impossible** when `H^2/m->infinity`.  Indeed, write
`W=aN_q+b`, where `a=floor(W/N_q)` and `0<=b<N_q`.  Convexity gives

\[
 C_q\ge N_q\binom a2+ab,
\]

and therefore

\[
 C_q-(W-N_q)
 \ge N_q\frac{(a-1)(a-2)}2+b(a-1).                    \tag{7.11}
\]

As soon as `W/N_q->infinity`, the right side is
`(1/2+o(1))W^2/N_q`, much larger than `W`.  Quadratic collision energy
over-penalizes the triple and higher multiplicities which are unavoidable in
deep ranks.

The correct exact energy is the **linear duplicate excess**

\[
 D_q^\pm:=\sum_S(\mu_q^\pm(S)-1)_+.
\tag{7.12}
\]

Since there are `W` slots,

\[
 \boxed{D_q^\pm-(W-N_q)=M_q^\pm.}                     \tag{7.13}
\]

Thus (7.3) itself, or equivalently the sum of the excesses in (7.13), is the
weakest sufficient vertical statement.

This correction creates a genuine multiscale split.  At `q=1`, and more
generally for `q=o(sqrt m)`, `W/N_q=1+o(1)`; a Poisson-like factor misses a
constant fraction and a deliberately correlated two-sided near-rainbow design
is necessary.  At depths

\[
 q^2/m=\log\log m-\log2+o(1)
\]

and beyond, a Poisson-like **miss probability** is useful even though its
quadratic energy is necessarily large.  The exact benchmark, concentration,
conditioning obstruction, and sufficient switching ratios are proved in
`RANDOM_VERTICAL_FACTOR.md`.

The sharp strategy is therefore:

* use the nested/rainbow construction for the shallow depths;
* measure it by missing colours or the linear energy (7.13), not by (7.10);
* use exact-factor switching only in the outer central band, where its
  exponential miss bound leaves `o(W)` repairs;
* let Lemma 4 control the locality of proposed trades.
