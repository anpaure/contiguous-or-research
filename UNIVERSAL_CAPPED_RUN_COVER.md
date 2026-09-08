# Universal peak meshes and the surviving capped-run problem

## 1. Outcome

Work in the middle hexagon

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                    \ |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1.
\]

Throughout, `a` is a positive integer and all orders are linear (not
cyclic) orders of the distinct points of `H_a`.

Let

\[
                         T_1,T_2,\ldots,T_{M_a}
\]

be an arbitrary ordering of its points.  For a coordinate `c` and an
integer threshold `t`, a maximal interval on which `c(T_j)>=t` is an
**internal threshold run** if it meets neither end of the ordering.
As in the heterogeneous run-cover lemma, an index may be assigned such a
run only when the run does not contain that index.

This note attacks Conjecture D from `FABLE_GENERAL_CASE_WORK.md`.  It does
not settle that conjecture for an arbitrary ordering.  It proves three
things which sharply reduce it.

1. **Congestion is automatic.**  Every interval of `4a+2` consecutive
   middle points contains an internal threshold run.  More strongly, the
   run may be chosen to be a constant-coordinate peak plateau and hence has
   at most `2a+1` vertices.  Consequently every ordering has a run
   assignment on all but `O(a)` indices with charge congestion at most
   `4a+3` and total clipped cost

   \[
                    (6+o(1))a^3.                       \tag{1.1}
   \]

   Thus the `O(a)`-congestion requirement in Conjecture D is never the
   difficult part.  Only the constant in the run-length budget remains.

2. **The entire surviving intact-side-block regime is cheap.**  Suppose
   the order is obtained by permuting and independently reversing the
   `6a` half-open side blocks `B_{k,s}` from
   `THREE_BOX_PHASE_SEPARATION_RESEARCH.md`, keeping every block intact,
   and inserting the center anywhere.  There may be `Theta(a)` genuine
   side switches; no batching hypothesis is made.  Then the same assignment
   has

   \[
           \sum_i\min(\lambda_i,3a-1)
                    \le (3+o(1))a^3,                  \tag{1.2}
   \]

   leaves only `O(a)` indices unassigned, and has congestion `O(a)`.
   Hence Conjecture D is true, with a full unit of leading-constant room,
   for every intact forced-side-block schedule.  In particular, merely
   making the number of side switches linear cannot escape the fan-capped
   obstruction.

3. **Any arbitrary-order survivor has a rigid long-line corridor.**  If the
   elementary peak assignment cannot achieve `(4-o(1))a^3`, then for every
   fixed `0<delta<4/3`, a positive proportion of all length-`(4a+2)` forward
   windows contain no peak run whose cost `lambda=|run|-1` is at most

   \[
                         (4/3-\delta)a.                \tag{1.3}
   \]

   Such windows force `Omega_delta(a)` almost-disjoint directed
   coordinate-line subsequences, each longer than `(4/3-delta)a`, whose fixed
   coordinate lies in the central strip

   \[
                         |c|<(2/3+\delta)a+O(1).       \tag{1.4}
   \]

   On each subsequence either of the other coordinates is strictly monotone;
   consecutive terms need not be neighbouring lattice points.
   This is the precise remaining failure mode.  It is substantially more
   rigid than an arbitrary `Theta(a)`-switch schedule, but it is not yet a
   contradiction: a rotating triangular packing of line segments is the
   unresolved extremal configuration.

The proofs use only elementary order and geometry.  No computation or
fixed-row assumption is involved.

## 2. Peak runs

For a scalar word

\[
                         u_1,u_2,\ldots,u_n,
\]

call a maximal constant interval `[p,q]` an **internal peak plateau** when

\[
                         u_{p-1}<u_p=u_{p+1}=\cdots=u_q>u_{q+1}. \tag{2.1}
\]

It is exactly an internal threshold run for the threshold `t=u_p`.
Its run cost in the convention of the heterogeneous run-cover lemma is

\[
                         \lambda=q-p.                  \tag{2.2}
\]

The following elementary characterization is the source of the universal
mesh.

### Lemma 1 (peak-free scalar words are valleys)

A finite scalar word has no internal peak plateau if and only if it is
weakly valley-shaped: for some index `m`,

\[
 u_1\ge u_2\ge\cdots\ge u_m
       \le u_{m+1}\le\cdots\le u_n.                  \tag{2.3}
\]

#### Proof

Compress every maximal constant interval to one symbol.  Adjacent symbols
in the compressed word are unequal.  An internal peak plateau in the
original word is exactly an internal strict local maximum in the compressed
word.  If the compressed word has no such maximum, its successive
comparison signs cannot change from `+` to `-`.  They therefore consist of
some `-` signs followed by some `+` signs, which is (2.3).  The converse is
immediate.  \(\square\)

### Lemma 2 (monotone middle paths have length at most `2a+1`)

Let `P_1,\ldots,P_n` be distinct points of `H_a`.  Suppose that, for each
of the three coordinates, the corresponding scalar sequence is weakly
monotone on this interval.  Then

\[
                              n\le2a+1.                \tag{2.4}
\]

#### Proof

The coordinates which are nondecreasing form a nonempty proper subset `S`
unless the sequence has only one point.  Put

\[
                         \Phi(P)=\sum_{c\in S}c(P).
\]

At every step between distinct points, `Phi` increases by at least one:
all coordinates in `S` are nondecreasing, all complementary coordinates
are nonincreasing, and the total coordinate sum remains zero.  If `S` has
one coordinate, `Phi` is that coordinate; if it has two, `Phi` is the
negative of the remaining coordinate.  In either case its range is at most
`2a`.  Hence there are at most `2a+1` points.  \(\square\)

## 3. The universal peak-mesh theorem

### Theorem 3 (every `4a+2` window contains a peak)

Every interval of `4a+2` consecutive terms in an ordering of distinct
points of `H_a` contains an internal peak plateau of one of the three
coordinate words.  The plateau is an internal threshold run in the full
ordering and has at most `2a+1` vertices.

#### Proof

Suppose a window `W` contains no internal peak plateau for any coordinate.
By Lemma 1, each of its three coordinate words is valley-shaped.  Choose one
valley index for each coordinate and sort the three indices:

\[
                              p_1\le p_2\le p_3.
\]

Split `W` at these indices into four overlapping intervals.  Before `p_1`
all three coordinates are nonincreasing.  Since their sum is zero, no two
distinct consecutive points can occur there, so this first interval has
length at most one.  The same argument shows that the interval after `p_3`
has length at most one.

On each of the two middle intervals, every coordinate is weakly monotone,
with at least one nondecreasing and at least one nonincreasing coordinate.
Lemma 2 bounds each middle interval by `2a+1` points.  The three cut points
are counted twice in the sum of the four interval lengths.  Therefore, if
`|W|=n`,

\[
 n+3\le1+(2a+1)+(2a+1)+1=4a+4,
\]

and hence `n<=4a+1`, a contradiction.

The resulting peak plateau is bounded on both sides by smaller coordinate
values inside `W`.  Thus its maximal threshold component cannot extend
outside `W`, and it is also an internal run in the full ordering.
The strict smaller neighbour also implies that its level is greater than
`-a`, so this is a genuine coordinate-increment threshold of the product
of chains, not a vacuous all-one threshold.

Finally, a plateau on the level `c=t` uses distinct points of

\[
                         H_a\cap\{c=t\}.

\]

That level has exactly

\[
                         2a+1-|t|\le2a+1              \tag{3.1}

\]

points.  \(\square\)

### Corollary 4 (a universal `6a^3` capped cover)

Put `L=4a+2`.  For every `1<=i<=M_a-L`, apply Theorem 3 to the forward
window

\[
                         W_i=[i+1,i+L]

\]

and assign `i` one peak run contained in that window.  Leave the final `L`
indices unassigned.  Then

\[
 \begin{aligned}
  M_a-|J|&=4a+2=O(a),\\
  C_\alpha&\le4a+3,\qquad C_\beta=0,\\
  \sum_{i\in J}\min(\lambda_i,3a-1)
      &\le 2a(M_a-L)=(6+o(1))a^3.                    \tag{3.2}
 \end{aligned}

#### Proof

The assigned run lies strictly after `i`, so it does not contain `i`.  Its
last position `v_i` satisfies `v_i+1-i<=L+1`.  A fixed adjacent increment
of the monotone offset sequence `alpha` can therefore be charged only by
one of the preceding `L+1` indices.  This gives the congestion bound.  The
cost bound follows from Theorem 3, because a run of at most `2a+1` vertices
has `lambda<=2a`.  \(\square\)

This corollary is weaker than Conjecture D only in the leading run-cost
constant.  It shows that no arbitrary ordering can evade the run method by
forcing superlinear charge congestion alone.

## 4. A plateau-parameter reduction

For an ordering `T`, let `mu(T)` be the largest number of consecutive terms
having one fixed coordinate value.  The proof above immediately gives the
following useful criterion.

### Corollary 5

Every ordering admits an assignment on all but `4a+2` indices with

\[
 \sum_{i\in J}\min(\lambda_i,3a-1)
       \le(\mu(T)-1)(M_a-4a-2),                       \tag{4.1}
\]

and `C_alpha<=4a+3`, `C_beta=0`.

Consequently, if for some fixed `delta>0`,

\[
                         \mu(T)\le(4/3-\delta)a,       \tag{4.2}

\]

then

\[
 \sum_{i\in J}\min(\lambda_i,3a-1)
       \le(4-3\delta+o(1))a^3.                        \tag{4.3}

Thus Conjecture D is already proved for every family of orders satisfying
(4.2).  An arbitrary-order proof only needs to handle long
constant-coordinate corridors.

## 5. Arbitrary intact side-block schedules

Recall the half-open blocks, with `0<=t<s`,

\[
\begin{array}{c|c}
k&B_{k,s}(t)\\ \hline
0&(s,-s+t,-t)\\
1&(s-t,t,-s)\\
2&(-t,s,-s+t)\\
3&(-s,s-t,t)\\
4&(-s+t,-t,s)\\
5&(t,-s,s-t).
\end{array}                                                   \tag{5.1}
\]

The `6a` blocks, together with the center, partition `H_a`.  Consider any
order formed by permuting these blocks, reversing any of them, and placing
the center arbitrarily.  Blocks are required only to stay intact.  There is
no restriction on the number or pattern of side switches.

### Lemma 6 (plateaux in a side-block order are short)

For `a>=3`, every constant-coordinate plateau in such an order has at most

\[
                              a+2                     \tag{5.2}

\]

vertices.

#### Proof

Inside a block of length at least two, one coordinate is constant and the
other two are strictly monotone.  Hence a plateau which contains two terms
of such a block must use its constant coordinate and, by maximality, contains
the whole block.  For any fixed nonzero coordinate value `c`, there is only
one non-unit block whose designated constant coordinate equals `c`; its
length is `|c|<=a`.

A neighboring nonconstant block can contribute at most one endpoint to the
same plateau.  It cannot be crossed, because its next term has a different
coordinate value.  Thus a plateau containing a non-unit constant block has
at most `|c|+2<=a+2` terms.

It remains to account for plateaux made only from unit blocks, the center,
and endpoints of non-unit blocks.  For a fixed coordinate, exactly two of
the six radius-one points have value `1`, two have value `-1`, and two have
value `0`; the center contributes one additional zero.  Therefore such a
plateau has at most two endpoint terms plus three unit/center terms, namely
at most five.  Since `a>=3`, this is again at most `a+2`.  \(\square\)

### Theorem 7 (the `Theta(a)`-switch regime is fan-capped)

For `a>=3`, every intact side-block schedule has a heterogeneous internal-run assignment
with

\[
 \begin{aligned}
 M_a-|J|&=O(a),\\
 C_\alpha+C_\beta&=O(a),\\
 \sum_{i\in J}\min(\lambda_i,3a-1)
                  &\le(3+o(1))a^3.                  \tag{5.3}
 \end{aligned}

#### Proof

Use the forward-window assignment of Corollary 4.  Lemma 6 improves every
assigned peak from `lambda<=2a` to `lambda<=a+1`.  Hence

\[
 \sum_{i\in J}\min(\lambda_i,3a-1)
       \le(a+1)(M_a-4a-2)=3a^3+O(a^2).               \tag{5.4}

The omitted-index and congestion bounds are unchanged.  \(\square\)

Combining this theorem with the fan-capped avoidance theorem gives
`D=Omega(a^2)` for every such central witness order.  This includes the
previously unresolved case of `Theta(a)` maximal side-homogeneous batches.
The only way a forced-ring-arc construction can remain outside the theorem
is to break a linear proportion of its side blocks into genuinely
interleaved fragments (or to use a selected middle order unrelated to the
obvious forced-side occurrences).

## 6. Necessary long-line structure of an arbitrary survivor

The universal mesh also gives a quantitative normal form for any possible
counterexample to Conjecture D.

For `1<=i<=M_a-L`, define

\[
 q_i=\min\{\lambda(P):P\text{ is an internal peak plateau contained in }
                         [i+1,i+L]\},                 \tag{6.1}

\]

where `L=4a+2`.  Theorem 3 says this minimum always exists, and (3.1) gives
`q_i<=2a`.

### Proposition 8 (many long-peak windows are necessary)

Suppose

\[
                         \sum_i q_i\ge(4-o(1))a^3.    \tag{6.2}

\]

Fix `0<delta<4/3`, and put `q_0=(4/3-delta)a`.  Then the number `F_delta` of
indices `i` for which `q_i>q_0` satisfies

\[
 F_\delta\ge
 \left({3\delta\over 2/3+\delta}-o(1)\right)a^2.    \tag{6.3}

Consequently the order contains `Omega_delta(a)` distinct peak plateaux of
more than `(4/3-delta)a` vertices.

#### Proof

Outside those `F_delta` windows, `q_i<=q_0`; everywhere, `q_i<=2a`.
Therefore

\[
 \sum_iq_i
 \le q_0(M_a-L)+(2a-q_0)F_\delta.                   \tag{6.4}

Substitute `M_a=3a^2+O(a)` and compare with (6.2) to obtain (6.3).

A fixed plateau `P` can be contained in at most `L-|P|+1<=L` of the
forward windows.  Dividing (6.3) by `L=O(a)` gives the final assertion.
\(\square\)

An actual counterexample to Conjecture D must in particular make this
specific `O(a)`-congestion assignment too expensive, so (6.2) is a necessary
condition for any asymptotic counterexample whose optimal cost is
`(4-o(1))a^3` or larger.

### Lemma 9 (long peaks are directed central-line subsequences)

Let `P` be a peak plateau of a coordinate `c` contained in a window counted
by `F_delta`.  Then

\[
 |P|>(4/3-\delta)a,
 \qquad
 |c|<(2/3+\delta)a+1.                                \tag{6.5}

Moreover either of the two other coordinates is strictly monotone along
`P` (one increases exactly when the other decreases).

#### Proof

The first inequality is the definition of `F_delta`, with the harmless
one-unit conversion between `|P|` and `lambda(P)`.  Since the full level
`c=t` has `2a+1-|t|` points,

\[
                         |P|\le2a+1-|c|,

\]

which gives the second inequality.

On `P`, fixing `c` makes the other two coordinates sum to `-c`, and distinct
middle points therefore have distinct values in each of those two
coordinates.  If their order were not strictly monotone, some interior term
would be a strict local maximum or a strict local minimum.  In the first
case it is a singleton peak of that coordinate; in the second case it is a
singleton peak of the remaining coordinate.  Either singleton lies in the
same forward window and contradicts `q_i>q_0`.  \(\square\)

Here "directed" means strictly monotone in either cross-coordinate; the
points need not be consecutive lattice neighbours on their coordinate
line.  Peak plateaux belonging to the same coordinate are disjoint.  Peak
plateaux of two different coordinates intersect in at most one position,
because two fixed coordinates determine the third.  Hence the
`Omega_delta(a)` long objects forced by Proposition 8 are an almost-disjoint
packing of directed lines.  Their total mass is `Omega_delta(a^2)`.

There is an exact one-dimensional form of this packing observation which is
useful for the next attack.

### Lemma 10 (peak edge budgets are disjoint)

For a peak plateau `P=[u,v]`, let

\[
                         E(P)=\{(j,j+1):u\le j<v\}.
\]

The sets `E(P)`, over **all** peak plateaux of all three coordinates, are
pairwise disjoint.  Consequently

\[
                         \sum_P\lambda(P)\le M_a-1.   \tag{6.6}
\]

#### Proof

Two different maximal constant plateaux of one coordinate are disjoint.
If plateaux of two different coordinates shared an index edge `(j,j+1)`,
then both of those coordinates would be equal at `T_j` and `T_(j+1)`.
Their sum is fixed, so the third coordinate would also be equal, contrary
to the distinctness of the middle points.  Thus no edge is used twice, and
(6.6) follows.  \(\square\)

In particular, the number of peaks with
`lambda>(4/3-delta)a` is at most

\[
                 {M_a-1\over(4/3-\delta)a}=O(a).      \tag{6.7}
\]

Together with Proposition 8 this pins the survivor to `Theta_delta(a)`
long corridors: neither a sublinear exceptional family nor a superlinear
cloud of unrelated peaks can account for it.  Notice, however, that (6.6)
does not by itself control reuse.  One long peak may be assigned to
`Theta(a)` nearby indices, so the weighted assignment cost can still be
`Theta(a^3)`.

This is the surviving arbitrary-order regime:

> a positive-density portion of the middle order must be organized into a
> linear number of directed, central coordinate-line corridors, each of
> length close to or above `4a/3`, with the three coordinate directions
> rotating so that no short peak is created at a join.

The natural extremal picture is a nested triangular or three-directional
line braid.  The existing phase-separated and complete-ring orders do not
realize it: their intact side plateaux have length at most `a+O(1)` and are
covered by Theorem 7.

## 7. Exact remaining lemma and explicit failure modes

The arbitrary-order Conjecture D would follow from either of the following
strictly stronger, now sharply localized statements.

### Short-peak average lemma

For every ordering of `H_a`, with `q_i` as in (6.1),

\[
                         \sum_iq_i\le(4-\varepsilon)a^3 \tag{7.1}

\]

for some absolute `epsilon>0`.

This statement already includes an explicit assignment and the congestion
bound `4a+3`; no further scheduling theorem would be needed.

### Long-line transition lemma

No ordering of `H_a` can contain a positive-density, `O(a)`-mesh packing of
directed peak plateaux satisfying (6.5) without also creating a positive
density of internal threshold runs whose cost `lambda=|run|-1` is at most
`(4/3-epsilon)a` near the joins.

The second formulation isolates the only missing geometry.  A proof must
use more than the following facts, which are all compatible with a linear
number of long corridors:

* there are only `2a+1-|c|` points on a coordinate level;
* long peak intervals of different directions overlap in at most one point;
* each long peak can service only `O(a)` forward windows; and
* there are only `O(a)` eligible central coordinate levels.

Those estimates permit `Theta(a)` long corridors with total mass
`Theta(a^2)`.  The unresolved issue is their **ordered transition
geometry**, not their raw count.

Three concrete failure modes must be excluded in a future proof.

1. **Rotating triangular braid.**  Long `x`-, `y`-, and `z`-constant
   directed segments alternate cyclically.  The increasing coordinate of
   one segment becomes the long constant peak of the next, preventing a
   singleton at the join.
2. **Boundary-fed corridor.**  Some long superlevel components touch an end
   of the selected-middle order and are not internal.  The universal
   forward assignment discards only `O(a)` terminal indices, but a transition
   proof must still distinguish these boundary components from internal
   peaks.
3. **Non-peak threshold escape.**  Even when every local peak plateau is
   long, a lower threshold can produce a shorter nonconstant component
   across parts of two neighboring corridors.  This helps Conjecture D, but
   it is not detected by the peak-only normal form; a final proof should
   exploit, rather than accidentally ignore, these components.

## 8. Status

Proved here:

* the `4a+2` universal peak mesh;
* a universal run assignment with `O(a)` omitted indices and `O(a)` charge
  congestion;
* the `(6+o(1))a^3` arbitrary-order clipped-cost bound;
* the `(3+o(1))a^3` bound for every permutation/reversal of intact forced
  side blocks, with no restriction on side switches; and
* the long directed-line-subsequence normal form necessary for a
  peak-method survivor.

Not proved here:

* the `(4-epsilon)a^3` bound for an arbitrary ordering;
* impossibility of the rotating triangular braid; or
* a lower bound showing that such a braid genuinely defeats every
  heterogeneous run assignment.

Accordingly Conjecture D remains open in full generality.  Its previously
named `Theta(a)`-switch side-block regime is closed; what remains requires
fragmenting those blocks into long central-line corridors and controlling
the transitions between the three line directions.

### Exact relation to subcritical product aggregation

The direction of implication is worth making explicit.  If Conjecture D
were proved with a fixed `epsilon>0`, then applying the fan-capped bound
with the full lower family, of height `h=3a-1`, would give

\[
 4a^3+O(a^2)
 \le (4-\varepsilon)a^3+O(aD)+O(a^2),
\]

and hence `D=Omega(a^2)` for every three-box word on
`[0,2a]^3`.  This would rule out the uniform local estimate

\[
 g_3(\boldsymbol\ell)
 \le w(\boldsymbol\ell)+O((1+\ell_1+\ell_2+\ell_3)^c),
 \qquad c<2,
\]

required by the three-factor case of the subcritical product-chain
aggregation theorem (the cubic subfamily alone would contradict it).

The results proved in this note do **not** yield that conclusion: the
universal peak assignment has leading cost `6a^3`, and Theorem 7 gives
leading cost `3a^3` only for intact side-block schedules.  Conversely, an
order escaping the proposed cheap cover would only be a candidate geometry
for a local construction; escape by itself would not prove any
subquadratic upper bound.
