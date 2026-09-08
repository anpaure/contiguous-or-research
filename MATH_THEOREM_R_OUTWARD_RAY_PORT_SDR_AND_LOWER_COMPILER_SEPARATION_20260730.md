# Outward-ray seam ports and exact separation from the lower compiler

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: unconditional interface theorem.  Upper repair is exactly an
owner-interval problem and cannot be purchased with scalar lower deadline
slack.  A protected seam-port condition plus the independent lower
port-capture Hall condition is sufficient.  No PBBS/Pascal construction is
claimed to satisfy those conditions for every `k`.

## 0. Outcome

Let `T=(T_0,...,T_(W-1))` be a rank-`r` owner path and let the nonzero source
word `A=(A_0,...,A_(W+d-1))` satisfy

\[
                 T_i=\bigcup_{p=i}^{i+d}A_p.          \tag{0.1}
\]

There is a label-preserving bijection

\[
 \{\hbox{source intervals of length at least }d+1\}
 \longleftrightarrow
 \{\hbox{owner intervals}\},
 \qquad [p,q]\longmapsto[p,q-d].                    \tag{0.2}
\]

Every source interval of length at most `d` has rank at most `r`.
Consequently a target of rank greater than `r` occurs in `A` **if and only
if** it occurs as an interval union in `T`.  Changing the lower compiler
inside the fixed fibre `D^d A=T` can neither create nor destroy an upper
occurrence.

For the outward-ray loss family of
`MATH_THEOREM_R_PROTECTED_WEDGE_RAYS_AND_PRODUCT_SPILL_20260730.md`, this
has three consequences.

1. After `(E1)` protects depth two, there are at most

   \[
                    \ell\le b\max\{k-r-2,0\}          \tag{0.3}
   \]

   possible old-upper casualties from `b` opened components.
2. They cost zero extra letters exactly when the final owner path rehosts
   every one of their explicit outward-ray masks.  Any rehost of a genuinely
   lost mask crosses a new seam.
3. The lower deadline slack

   \[
     \sigma=dW+{d+1\choose2}-\sum_{s=1}^{r-1}{k\choose s}             \tag{0.4}
   \]

   is not a bank of upper ports.  It counts aggregate duplicate/rank-`r`
   short-window mass.  Even `sigma` much larger than (0.3) gives no upper
   rehost and no lower Hall theorem.

The minimal strengthened protected-port condition is therefore:

> **(E1-port).**  The opened/rethreaded owner path preserves depth two, and
> every explicit geodesic outward-ray casualty at depth at least three is
> the union of a new seam-crossing owner interval.

This condition closes the upper repair.  The lower compiler remains the
separate common-`Q`/port-capture Hall problem stated in Theorem 5.1 below.

## 1. Exact upper occurrence equivalence

Write `A[I]=union_(p in I) A_p` and `T[J]=union_(i in J)T_i`.

### Theorem 1.1 (source/owner interval bijection)

Assume (0.1).

1. Every source interval of length at most `d` is contained in a derivative
   window and hence has union of rank at most `r`.
2. If `0<=p<=q<W+d` and `q-p+1>=d+1`, then

   \[
              A[[p,q]]=T[[p,q-d]].                   \tag{1.1}
   \]
3. Conversely, for every owner interval `[i,j]`,

   \[
              T[[i,j]]=A[[i,j+d]].                   \tag{1.2}
   \]

Thus (0.2) is a bijection preserving the union label.  In particular, for
every `Y` with `|Y|>r`,

\[
 Y\text{ occurs in }A
 \quad\Longleftrightarrow\quad
 Y\text{ occurs as an owner-interval union in }T.    \tag{1.3}
\]

#### Proof

Every interval `[p,q]` of at most `d` source positions is contained in some
`[i,i+d]` with `0<=i<W`; this remains true at both clipped ends of the source
line.  Hence its union is contained in `T_i` and has rank at most `r`.

If `q-p+1>=d+1`, then `p<=W-1` and `0<=q-d<=W-1`.  Using (0.1),

\[
 \bigcup_{i=p}^{q-d}T_i
 =\bigcup_{i=p}^{q-d}\bigcup_{u=i}^{i+d}A_u
 =\bigcup_{u=p}^{q}A_u,
\]

because the consecutive derivative windows cover exactly `[p,q]`.  This is
(1.1); the same calculation with `p=i,q=j+d` proves (1.2).  The two maps are
inverse.  The first part forces every witness of a rank-greater-than-`r`
target to use at least `d+1` source positions, so (1.3) follows.  QED.

### Corollary 1.2 (fixed-row compiler no-go)

Fix `T`.  Among all nonzero words `A` satisfying `D^dA=T`, the multiset of
upper interval labels, including multiplicities, is identical.  No change
of common `Q`, lower pins, or short-cell assignment within that fibre can
repair an upper hole.

This is stronger than a rank-count obstruction: it is an exact occurrence
bijection.

## 2. Exact outward-ray rehost condition

Start from a protected cycle factor.  Cut its components into pieces,
retain and possibly reverse their interiors, and join them into a final
owner path `T`.  Let `C` be the set of upper targets which lose every old
interior witness.  Assume all upper targets outside `C` retain an interior
or already certified new witness.

Let `J_new(T)` denote the owner intervals crossing at least one inserted
seam, and define

\[
 H_T(Y)=\{J\in J_{\rm new}(T):T[J]=Y\}.              \tag{2.1}
\]

### Theorem 2.1 (exact seam-host criterion)

Under the preceding retained-interior hypothesis, the final owner path is
upper-complete if and only if

\[
                         H_T(Y)\ne\varnothing
                         \qquad(Y\in C).              \tag{2.2}
\]

For distinct targets `Y`, the host families `H_T(Y)` are pairwise disjoint.
Hence choosing one actual interval per casualty is automatically an SDR;
there is no occurrence-capacity Hall obstruction after `T` is fixed.

#### Proof

Sufficiency is immediate from the retained witnesses and (2.2).  Conversely,
if a casualty is restored, its new witness cannot be wholly inside one
retained interior, since by definition every such old witness was lost.
It therefore crosses a new seam and belongs to (2.1).  An owner interval has
one union label, so it cannot belong to the host families of two distinct
targets.  QED.

### Corollary 2.2 (minimal protected-ray port condition)

Assume fixed-width all-depth support and `(E1)`.  Choose one legal wedge
flank in each of `b` components.  For each component `a`, form the explicit
ray list

\[
 {cal R}_a=\{Y_{a,q}:3\le q\le k-r,\ Y_{a,q}
                 \text{ is a geodesic rank-}(r+q)\text{ ray}\}.       \tag{2.3}
\]

Then the old-upper loss family is a subset of `union_a R_a` and has size at
most (0.3).  Condition `(E1-port)` is necessary and sufficient for restoring
all of these losses **inside the owner-interval architecture**.

The necessity scope matters.  It uses Theorem 1.1 and therefore applies to
every source word with the same final derivative row.  It does not say that
one cannot change the owner row again by a larger braid.

## 3. Configurable capacity-one ports and Hall

Before a final owner path is fixed, a macro construction may have a finite
set `P` of mutually exclusive seam/boundary sockets.  A socket can be set to
one of several modes, each mode rehosting one casualty.  Assume the following
**joint-installability** condition: every choice of modes at distinct
sockets is realized by one legal owner path and preserves all declared
interior witnesses.  This is an additional physical theorem, not a
consequence of marginal port lists.

Join `Y in C` to `p in P` when socket `p` has a legal mode rehosting `Y`.

### Theorem 3.1 (capacity-one ray-port Hall theorem)

Under joint installability, all casualties can be rehosted if and only if

\[
               |N_G(X)|\ge|X|\qquad(X\subseteq C).   \tag{3.1}
\]

If

\[
 \delta_U(G)=\max_{X\subseteq C}(|X|-|N_G(X)|),      \tag{3.2}
\]

then a maximum port assignment leaves exactly `delta_U(G)` casualties
unassigned in this capacity-one architecture.

#### Proof

This is Hall's theorem and its deficiency form.  Joint installability turns
the abstract matching into one physical owner path.  QED.

In particular, a bank of

\[
                         |P|\ge b(k-r-2)              \tag{3.3}

fully universal sockets suffices after `(E1)`.  Merely having that many
crossing intervals or boundary-grid labels does not suffice: their labels
may all be wrong or their controlling modes may be correlated.

### Theorem 3.2 (exact interval-list reduction)

Order the sockets as `1,...,m` and suppose every casualty has an interval
list

\[
                         N_G(Y)=[l_Y,u_Y].            \tag{3.4}

Then a full SDR exists if and only if, for every `1<=s<=t<=m`,

\[
 \#\{Y:s\le l_Y\le u_Y\le t\}\le t-s+1.            \tag{3.5}
\]

For prefix lists `[1,u_Y]`, this reduces to

\[
             \#\{Y:u_Y\le t\}\le t\qquad(1\le t\le m).            \tag{3.6}
\]

The matching is produced deterministically by the usual earliest-deadline
greedy assignment.

#### Proof

Necessity follows by applying Hall to the targets whose whole lists lie in
`[s,t]`.  Conversely, if Hall fails for a target set `X`, decompose the union
of its interval lists into disjoint interval components.  Every list, being
connected, lies in one component.  Some component `[s,t]` contains more
members of `X` than ports; all of their lists lie in `[s,t]`, contradicting
(3.5).  The prefix specialization is immediate.  Standard exchange moves
turn any matching of the first `j-1` deadline-ordered jobs into one using the
earliest available allowed ports, proving the greedy statement.  QED.

The same proof gives the laminar version: if the port lists form a laminar
family, it is enough to check

\[
       \#\{Y:N_G(Y)\subseteq Q\}\le|Q|              \tag{3.7}
\]

for each list `Q` in the laminar closure.

## 4. Why positive lower slack is not an upper resource

Let

\[
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 M_d=dW+{d+1\choose2}=\Lambda+\sigma                 \tag{4.1}
\]

be the number of strict lower targets and the number of short source
intervals.  For a hole-free compiler, the exact collision identity is

\[
                         C_<(A)+R_=(A)=\sigma.        \tag{4.2}
\]

Thus all `M_d` short intervals are already present; `sigma` counts duplicate
lower labels and rank-`r` labels.  It does not designate empty cells.  By
Theorem 1.1 none of these short intervals can carry an upper target.

There is also no lower Hall implication from the scalar inequality alone.
For every `Lambda>=2` and `sigma>=1`, consider an abstract occurrence table
with `Lambda+sigma` cells: target `S_1` has only cell `c_1`; every other
target has its own cell; and all `sigma` extra cells repeat `S_2`.  The table
has a complete target assignment and exactly `sigma` duplicate occurrences.
Deleting the single cell `c_1` leaves at least `Lambda` cells when
`sigma>=1`, but destroys the last provider of `S_1`.

This is an exact counterexample to every argument using only
`(Lambda,sigma,number of affected cells)`.  It is not asserted to be a PBBS
antecedent; its purpose is to identify the missing structural input: a
deletion-stable lower matching/common-`Q` theorem.

## 5. Lower seam damage and the independent Hall gate

Suppose a source word is transported in pieces, old and new seams are
separated by at least `d`, and every relevant piece has at least `d-1`
source positions on each side of a seam.  A seam is crossed by exactly

\[
                         {d\choose2}                 \tag{5.1}
\]

short intervals.  If `J_-` old seams are deleted and `J_+` new seams are
inserted, the set `Z` of short occurrences whose literal label is not
protected has

\[
                         |Z|\le(J_-+J_+){d\choose2}. \tag{5.2}
\]

For one cut in each of `b` old cyclic pieces and `b-1` new joins this gives
the conservative count

\[
                         |Z|\le(2b-1){d\choose2}.    \tag{5.3}
\]

Consequently

\[
                  \sigma\ge(2b-1){d\choose2}         \tag{5.4}

\]

guarantees only that at least `Lambda` protected short occurrences remain.
It is not sufficient for a lower compiler.

After conditioning every forced singleton/facet pin and performing exact
unit closure, form a bipartite graph `G_L` between residual lower targets
and protected short-cell ports.  Join a target to a port when there is a
physical candidate using that port.  Assume the **port-capture condition**:
every selector using distinct ports is common-`Q` compatible.  Equivalently,
no minimal negative-window conflict has an SDR from its candidate port
lists.

### Theorem 5.1 (lower port-capture Hall theorem)

Under port capture, the exact loss in the protected-port architecture is

\[
 \delta_L(G_L)=max_{X}(|X|-|N_{G_L}(X)|).            \tag{5.5}
\]

In particular, (5.4) plus

\[
                         |N_{G_L}(X)|\ge|X|           \tag{5.6}
\]

for every residual target set `X` gives a complete lower compiler.  If the
target port lists are intervals or laminar, Theorem 3.2 or (3.7) gives the
corresponding deterministic finite cut test.

#### Proof

The deficiency form of Hall gives a matching covering all but
`delta_L(G_L)` target parts.  Port capture makes every such rainbow selector
physically compatible, so it extends the forced unit-closed table.  No
larger matching exists.  QED.

Without port capture, ordinary Hall is not sufficient: several selected
negative windows can cover the last positive occurrence of one coordinate.
The exact common-`Q` positive-cover and empty-position cores remain the
correct test.

## 6. Combined shadow-port/compiler theorem

### Theorem 6.1 (deterministic separated repair)

Let the protected opening theorem leave a casualty set `C` with
`|C|<=b max(k-r-2,0)`.  Let `T` be one final rank-`r` owner path retaining
all other upper targets.  Put

\[
 u=\#\{Y\in C:H_T(Y)=\varnothing\}.                 \tag{6.1}
\]

Suppose the exact forced lower rows admit a port-capture graph with Hall
deficiency `delta_L`.  Then

\[
                    \boxed{\nu(k)\le B(k)+u+\delta_L.}             \tag{6.2}
\]

In particular, `(E1-port)` and lower Hall give `nu(k)=B(k)`; `(E1-port)` and
`delta_L=O(k)` give `B(k)+O(k)`.

#### Proof

Theorem 2.1 supplies every upper target except the `u` unhosted casualties.
Theorem 5.1 gives one source word `A` with `D^dA=T` covering every lower
target except `delta_L` unmatched targets.  By Theorem 1.1 this compiler
choice preserves exactly the upper interval labels of `T`.  Append the
`u+delta_L` missing masks literally.  QED.

The formula separates the two defects exactly:

* `u` is an owner-path/seam-label defect;
* `delta_L` is a short-window/common-`Q` compiler defect.

The deadline slack enters only in crude protected-cell capacity such as
(5.4).  It never subtracts from `u`, and it does not imply `delta_L=0`.

## 7. Proved and conditional boundary

Unconditional statements in this note are Theorems 1.1, 2.1, 3.1--3.2,
the seam count (5.2), and Theorems 5.1 and 6.1 under their explicitly stated
physical port-capture hypotheses.  The following remain unproved for a
general PBBS/Pascal recursion:

1. a jointly installable seam-socket bank satisfying `(E1-port)`;
2. interval or laminar lists for those configurable sockets;
3. deletion-stable lower port capture after the upper rethreading; and
4. the full lower Hall inequalities.

Thus the protected-ray `O(bk)` spill theorem is upgraded to an exact
zero-cost upper-repair criterion, but not to an unconditional all-`k`
construction.  No finite SAT, exhaustive search, remote computation, or web
input is used.
