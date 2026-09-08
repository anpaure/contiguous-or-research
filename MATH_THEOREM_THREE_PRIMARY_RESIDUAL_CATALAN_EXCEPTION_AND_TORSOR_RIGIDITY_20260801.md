# Three-primary residual symmetry requires a Catalan-scale braid

Date: 2026-08-01  
Lane: clean cyclic quotient / non-affine phase rules / recursive quotient lift  
Status: exact obstruction and exact smaller-necklace identification.  No
all-parameter quotient Latin forest is claimed.

## 0. Outcome

Let

\[
 n=2m-1,
 \qquad s=3^{v_3(n)},
 \qquad G\leq \mathbb Z_n,
 \qquad |G|=h=n/s,
\]

where `G` is the maximal three-free rotation subgroup used in the clean
quotient.  The existing reduction makes `G` free on the row, column,
symbol, and matched-value ranks, and leaves a residual cyclic action

\[
                    R=\mathbb Z_n/G\cong\mathbb Z_s.
\]

Two exact conclusions follow.

1. On free cyclic torsors, an equivariant phase map is only a translation.
   Thus a nonlinear complete mapping, orthomorphism, Skolem sequence, or
   Langford sequence cannot create additional *within-orbit* phase freedom
   while exact `G`-equivariance is retained.  Such objects can choose
   quotient atom types, or they can deliberately break symmetry, but they
   cannot repair the quotient forest by a hidden nonlinear phase rule.

2. If `3|n`, write

   \[
                         m=3r+2.
   \]

   The order-three subgroup of `R` fixes exactly

   \[
                         {s\over3}\operatorname {Cat}_r
   \]

   row vertices of the clean quotient, and fixes no column or symbol
   vertex.  Those fixed row vertices form exactly

   \[
                         \operatorname {Cat}_r
   \]

   residual `R`-orbits.  Every one of these orbits must be symmetry-broken
   by any row-saturating selector.

3. The forced exceptional rows nevertheless admit an exact all-parameter
   local solution.  For any fixed clean matching `mu`, choosing an arbitrary
   containing column for each fixed quotient row produces distinct columns,
   distinct symbols, and a directed matching (hence a forest).  The open
   issue is extending the nonexceptional bulk while avoiding this large
   reserved bank, not internal correlation among the exceptional rows.
   Moreover `mu` may be chosen fully rotation-equivariant, in which case
   literal cell development attains exactly one wrap seam per Catalan
   sector.

Consequently the hoped-for clean quotient plus `O(1)` exceptional
order-three orbits is impossible.  The required residual braid is
Catalan-scale:

\[
        \operatorname {Cat}_{(m-2)/3}
        =2^{(2/3+o(1))m}.
\]

There is nevertheless a canonical smaller target.  The forced exceptional
sectors are naturally indexed by the rotation necklaces of rank `r` on
`2r+1` points.  Thus a viable three-primary induction must expose at least
this smaller Catalan necklace layer; it cannot carry the three-primary
defect as a bounded sidecar.

## 1. Free-torsor rigidity

### Lemma 1.1

Let a group `G` act freely and transitively on finite sets `X` and `Y`.
After choosing origins and identifying both torsors with `G`, every
`G`-equivariant map `f:X->Y` has the form

\[
                              f(x)=x+c                 \tag{1.1}
\]

for one constant `c in G`.

#### Proof

Put `c=f(0)`.  Equivariance gives

\[
                         f(x)=f(x+0)=x+f(0)=x+c.
\]

Conversely every translation is equivariant.  \(\square\)

### Corollary 1.2 (orthomorphisms do not supply equivariant phases)

If `|G|>1`, no equivariant map between two free `G`-torsors is an
orthomorphism in the phase coordinate: for (1.1),

\[
                              f(x)-x=c
\]

is constant, not a permutation.

More generally, between disjoint unions of free torsors an equivariant map
consists only of:

* a map between the quotient orbit sets; and
* one constant voltage for every chosen source-target orbit pair.

All nonlinear freedom therefore lives at quotient-type level.  It is not
an additional phase degree of freedom inside a selected orbit.

This distinction is especially sharp for the rooted Latin forest.  On a
quotient tree all edge voltages are gauge and its lift is a disjoint union
of trees.  A quotient cycle, with zero or nonzero voltage, lifts to physical
cycles.  Hence nonlinear phase schedules cannot turn a cyclic quotient
selection into the required physical forest.

## 2. Exact order-three fixed-row census

Assume `3|n`.  Write

\[
                m=3r+2,
                \qquad n=6r+3=3q,
                \qquad q=2r+1.                       \tag{2.1}
\]

Let `K<=Z_n` be the unique subgroup of order three.  The `K`-orbits on
coordinates are the `q` triples

\[
                  \{u,u+q,u+2q\},\qquad u\in\mathbb Z_q. \tag{2.2}
\]

The rows and columns in the complement-Latin table are

\[
          \mathcal C=\binom{\mathbb Z_n}{m-2}
                    =\binom{\mathbb Z_n}{3r},
          \qquad
          \mathcal B=\binom{\mathbb Z_n}{m-1}
                    =\binom{\mathbb Z_n}{3r+1}.       \tag{2.3}
\]

### Lemma 2.1 (physical fixed sets)

The order-three subgroup fixes exactly

\[
                         \binom qr                         \tag{2.4}
\]

rows in `C`, and no columns in `B`.

#### Proof

A subset fixed by `K` is a union of the triples (2.2).  A row has size
`3r`, so choosing it is choosing `r` of the `q` triples.  This gives
(2.4).  A column has size `3r+1`, which is not divisible by three, and
hence cannot be a union of `K`-orbits.  \(\square\)

Every row counted in (2.4) has stabilizer exactly `K`.  Indeed, the order
of a translation stabilizer divides both the ambient cycle length and the
set size, while

\[
                         \gcd(6r+3,3r)=3.
\]

Likewise every column has trivial physical stabilizer because
`gcd(2m-1,m-1)=1`.

Write bars for `G`-orbits.  Let `Kbar<=R` be the order-three subgroup of
the residual group.

### Lemma 2.2 (fixed quotient vertices descend exactly)

The `Kbar`-fixed vertices of `C/G` are exactly the `G`-orbits of the
physical `K`-fixed rows.  No vertex of `B/G` is `Kbar`-fixed.

#### Proof

The forward containment for rows is immediate.  Conversely, suppose
`[C]` is fixed by `Kbar`.  For a generator `k` of `K`, there is `g in G`
such that

\[
                              k+C=g+C.
\]

Thus the translation `t=k-g` stabilizes `C`.  Its image in `Z_n/G` has
order three, so the order of `t` is divisible by three.  The cyclic group
generated by `t` therefore contains the unique subgroup `K`, and `C` is
`K`-fixed.

The identical argument for a column `B` would produce a stabilizing
translation of order divisible by three.  Every orbit of that translation
has length divisible by three, forcing

\[
                              3\mid |B|,
\]

contrary to `|B|=3r+1`.  \(\square\)

The clean subgroup acts freely on `C`, so every `G`-orbit in the fixed-row
family has size `h`.  Because

\[
 h={n\over s}={3q\over s},
 \qquad
 {1\over q}\binom qr=\operatorname {Cat}_r,          \tag{2.5}
\]

Lemmas 2.1--2.2 give the exact fixed-vertex count

\[
 \left|\operatorname {Fix}_{\mathcal C/G}(\bar K)\right|
  ={1\over h}\binom qr
  ={s\over3}\operatorname {Cat}_r.                   \tag{2.6}
\]

## 3. Exact Catalan number of forced exceptional sectors

### Theorem 3.1 (residual Catalan exception theorem)

The fixed row vertices in (2.6) form exactly `Cat_r` orbits under the full
residual group `R`.  Every `R`-equivariant row selector

\[
                      \sigma:\mathcal C/G\longrightarrow\mathcal B/G,
                      \qquad C\subset\sigma(C),       \tag{3.1}
\]

must therefore be undefined or symmetry-broken on at least `Cat_r`
residual row orbits.

#### Proof

Identify a physical `K`-fixed row with the corresponding `r`-subset of
the `q=2r+1` coordinate triples.  Rotation descends to ordinary cyclic
rotation on `Z_q`.

The action of `Z_q` on rank-`r` subsets is free: a nonidentity stabilizer
has orbit length `d>1` dividing `q`, and would force `d|r`, impossible
because `gcd(q,r)=gcd(2r+1,r)=1`.  Consequently its number of orbits is

\[
                         {1\over q}\binom qr
                         =\operatorname {Cat}_r.       \tag{3.2}
\]

These are precisely the residual `R`-orbits on the `Kbar`-fixed quotient
rows.  Equivalently, the exact stabilizer statement after Lemma 2.1 makes
every such orbit have size `s/3`, agreeing with (2.6).  Columns and symbols
are free `R`-sets after quotienting by `G`.

Now let `[C]` be `Kbar`-fixed at a point where (3.1) is equivariant.  Then
`sigma([C])` must also be `Kbar`-fixed.  Lemma 2.2 says no such column
vertex exists.  Hence every one of the `Cat_r` orbits in (3.2) must lie in
the exceptional set.  \(\square\)

### Proposition 3.2 (one monodromy seam per sector is sharp)

At the bare torsor level, every one of the `Cat_r` exceptional sectors
requires at least one failure of successor equivariance, and one failure is
enough.

#### Proof

Write the residual group as `R=Z_s` and its order-three subgroup as

\[
                  \bar K=\{0,s/3,2s/3\}.
\]

One fixed-row sector is the homogeneous space `R/Kbar`, of size `s/3`,
whereas every column orbit is a free `R`-torsor.  If a phase section

\[
                         f:R/\bar K\longrightarrow R
\]

commuted with the successor at every step, iterating the successor `s/3`
times would give

\[
                         f(x)=f(x)+s/3,
\]

which is impossible in `R`.  Hence at least one seam is necessary.

It is sufficient abstractly: index `R/Kbar` by
`0,1,...,s/3-1` and take `f(i)=i`.  Successor equivariance holds at every
nonwrap step and fails only at the wrap, by the nonzero monodromy `s/3`.
Thus the order-three obstruction is exactly one unavoidable phase seam per
Catalan sector before incidence, column/symbol injectivity, and forest
constraints are imposed.  \(\square\)

### Corollary 3.3

No construction on the maximal clean quotient can restore the residual
three-primary action using `O(1)` exceptional orbit types.  More precisely,
the exception count is at least

\[
       \operatorname {Cat}_{(m-2)/3}
       \sim {4^{(m-2)/3}\over
              \sqrt\pi\,((m-2)/3)^{3/2}}.             \tag{3.3}
\]

When `v_3(2m-1)=1`, the residual group itself has order three and the
`Cat_r` exceptional quotient rows are pointwise fixed.  For example:

\[
\begin{array}{c|c|c|c}
m&r&2m-1&\text{forced exceptional residual orbits}\\ \hline
5&1&9&1\\
8&2&15&2\\
11&3&21&5\\
14&4&27&14\\
17&5&33&42
\end{array}                                           \tag{3.4}
\]

## 4. The exceptional rows have an exact isolated-edge solution

Fix any `G`-equivariant perfect incidence matching

\[
                 \mu:\mathcal B\longrightarrow\mathcal D,
                 \qquad \mu(B)=B+\alpha(B),           \tag{4.1}
\]

whose existence is already supplied by regular bipartite quotient
matching.  For a `K`-fixed row `C`, choose any `b notin C` and put

\[
                 B_C=C+\{b\},
                 \qquad A_C=C+\{\alpha(B_C)\}.        \tag{4.2}
\]

This is a legal table cell because `alpha(B_C) notin B_C`.

### Theorem 4.1 (fixed-row isolated bank)

Choosing one cell (4.2) for every `Kbar`-fixed quotient row gives:

1. pairwise distinct quotient columns `[B_C]`;
2. pairwise distinct quotient symbols `[A_C]`; and
3. pairwise distinct matched-value orbits `[mu(B_C)]`; and
4. a quotient digraph consisting entirely of isolated directed edges
   `[B_C]->[A_C]`.

Thus all `(s/3)Cat_r` fixed quotient rows can be saturated simultaneously
without a column collision, symbol collision, loop, or cycle, for every
fixed clean matching `mu`.

#### Proof

For any set obtained from a `K`-fixed row `C` by adding one or two points,
the union of its fully occupied `K`-coordinate triples is exactly `C`:
fewer than three added points cannot fill a previously empty triple.  Call
this recoverable set its `K`-core.

Both `B_C` and `A_C` in (4.2) have `K`-core `C`.  If
`[B_C]=[B_(C')]`, translation by some `g in G` and taking `K`-cores gives
`[C]=[C']`.  Hence distinct quotient rows give distinct quotient columns.
The same proof gives distinct symbols.

The matched-value orbits are distinct because `mu` is an equivariant
bijection and the selected column orbits are distinct.

If a selected head orbit `[A_C]` equalled a selected tail orbit
`[B_(C')]`, the core argument would first give `[C]=[C']`.  After choosing
one representative cell per quotient-row index, this is the same selected
edge, so the alleged equality is a loop `[A_C]=[B_C]`.  It gives an element
`g in G` with `A_C+g=B_C`; taking cores gives `C+g=C`.  Freeness of the
clean action forces `g=0`, and then `A_C=B_C`, contrary to
`alpha(B_C) notin B_C`.  Thus no selected head is any selected tail, and
all directed edges are isolated.  Development under `G` preserves the same
argument physically.  \(\square\)

This theorem does not say that the remaining nonfixed rows can avoid the
reserved columns and symbols.  It says that the unavoidable
three-primary bank is internally exact; the surviving gate is a relative
Latin-forest completion around it.

### Theorem 4.2 (literal one-seam development)

The first matching `mu` may be chosen fully `Z_n`-equivariant.  Relative to
such a matching, every one of the `Cat_r` fixed-row sectors has a literal
Latin-cell development with exactly one covariance seam.  Therefore the
lower bound in Proposition 3.2 is attained simultaneously on the entire
fixed-row block.

#### Proof

Full rotation is free on both ranks `m-1` and `m`, because

\[
              \gcd(n,m-1)=\gcd(n,m)=1.
\]

Their quotient incidence graph is a balanced `m`-regular bipartite
multigraph, and hence has a perfect matching.  Developing it gives a fully
rotation-equivariant `mu`.

Choose one `K`-fixed representative row `C_0` in a fixed-row sector and one
point `b_0 notin C_0`.  Put `B_0=C_0+{b_0}` and, for

\[
                         0\le i<q=n/3,
\]

define

\[
 C_i=C_0+i,
 \qquad B_i=B_0+i,
 \qquad A_i=C_i+\{\alpha(B_i)\}.                    \tag{4.3}
\]

Equivariance of `mu` gives

\[
                         \alpha(B_i)=\alpha(B_0)+i,
\]

so (4.3) is the literal translate of one legal table cell at every nonwrap
step.  The core proof in Theorem 4.1 makes all these cells isolated and all
their resources distinct.

At the wrap,

\[
                         C_q=C_0,
 \qquad B_q=B_0+q\ne B_0.                            \tag{4.4}
\]

The row equality holds because translation by `q` generates `K`; the
column inequality holds because columns are rotation-free.  Thus the sole
failure of covariance is the wrap seam.  Doing this independently on all
`Cat_r` sectors gives exactly one seam per sector, meeting Proposition 3.2.
\(\square\)

Its absolute Catalan size should not be confused with positive density.
The fraction of quotient rows occupied by the exceptional bank is exactly

\[
 {\binom{2r+1}r\over\binom{6r+3}{3r}}
      =2^{-(4+o(1))r}=2^{-(4/3+o(1))m}.              \tag{4.5}
\]

Thus the residual bank is exponentially sparse inside the full quotient
table, even though it is far too large to be an `O(1)` sidecar.  This makes
a relative absorption theorem plausible, but does not prove one.

## 5. Exact relative free-bulk quotient left over

Let `F_0` be the fixed-row bank from Theorem 4.2.  Let `T_0` be the set of
full-rotation orbits containing its selected tails, and let `H_0` be the
corresponding set for its selected heads.  The core theorem gives

\[
                         |T_0|=|H_0|=\operatorname {Cat}_r.     \tag{5.1}
\]

Put

\[
                         c=|T_0\cap H_0|.             \tag{5.2}
\]

The clean `G`-orbit tails and heads used by `F_0` are disjoint, but their
full-rotation orbits need not be: a head may be an order-three translate of
its tail.  Thus `c` is a genuine extra bulk parameter.

For a fixed-row sector represented by `C`, define

\[
 \epsilon_C(b)=
 \mathbf1_{\{\alpha(C+\{b\})-b\in K\setminus\{0\}\}}
 \qquad(b\notin C).                                  \tag{5.3}
\]

The selected tail and head full-rotation orbits coincide exactly when
`epsilon_C(b)=1`.  Choices from different sectors cannot share a tail or
head orbit by the core argument, so the minimum possible overlap for fixed
`mu` is

\[
 c_{\min}(\mu)=
 \#\{[C]:\epsilon_C(b)=1\text{ for every }b\notin C\}. \tag{5.4}
\]

Call these the **triangularly trapped** smaller necklaces.  In a trapped
sector, on each empty `K`-triple the three maps
`b -> alpha(C+{b})` form one of the two oriented three-cycles.  Indeed all
images stay in that triple, while injectivity of `mu` forces the three
unordered matched pairs to be distinct.  Conversely those oriented
triangles make every phase overlapping.  Thus seam-phase choice achieves
`c=0` exactly when `mu` has no triangularly trapped smaller necklace.  The
existence of a fully cyclic `mu` with this property is not proved here.

There is an exact protected-matching form of that missing statement.  For
one smaller-necklace sector `C`, there are `r+1` full-rotation column orbits
`C+{b}`, according to the empty `K`-triple containing `b`.  For each column
orbit there are

\[
                              3r
\]

nonoverlapping incidence-edge orbits: choose `alpha(C+{b})` in one of the
other `r` empty triples and choose its relative `K`-phase.  Thus every
sector has exactly

\[
                              3r(r+1)                 \tag{5.5}
\]

good first-matching edge-orbits.  Edges chosen for different sectors have
distinct column and matched-value orbits, because their `K`-cores recover
different smaller necklaces.

Consequently a fully cyclic `mu` with `c_min(mu)=0` exists if and only if
one can choose one of the `3r(r+1)` good edge-orbits per smaller necklace
so that the resulting automatic matching extends to a perfect matching of
the full cyclic `B`--`D` quotient incidence graph.  Equivalently, after
deleting the chosen endpoints, the residual graph satisfies ordinary Hall.
This is the exact smaller-necklace protected-matching gate; raw candidate
supply is solved, but its residual Hall theorem is open.

Although `F_0` uses only one third of each such full orbit, any fully cyclic
bulk atom using the same orbit in the same role would collide with it.
Thus (5.1) is the exact role-wise quarantine cost.

### Theorem 5.1 (two-scale relative quotient)

Assume `m>=5`, equivalently `r>=1`.  After removing the `K`-fixed rows,
every remaining row has trivial full
rotation stabilizer.  The number of long row orbits is

\[
 L={1\over n}\left(\binom n{m-2}-{n\over3}\operatorname {Cat}_r\right).
                                                               \tag{5.6}
\]

The available full-rotation tail orbits and head orbits each number

\[
                         {1\over n}\binom n{m-1}
                         -\operatorname {Cat}_r.       \tag{5.7}
\]

Hence the exact scalar spare on either role is

\[
 S_{\rm role}
   ={\operatorname {Cat}_m\over n}
      -{2\over3}\operatorname {Cat}_r>0.             \tag{5.8}
\]

Every long row retains a legal atom in the relative catalogue.

Relative completion of `F_0` is exactly the following finite quotient
problem.

1. Take the full-rotation orbits of legal cells whose row is long, whose
   tail orbit is outside `T_0`, and whose head orbit is outside `H_0`.
2. Select one atom orbit per long row orbit, with every available tail and
   head orbit used at most once.
3. Develop the selection to the clean `G`-quotient, add `F_0`, and require
   the resulting voltage graph to be loopless and acyclic.

There are no further short-orbit or stabilizer cases hidden in this
instance.

#### Proof

A row stabilizer has order dividing

\[
                         \gcd(n,m-2)=3.
\]

The nontrivial rows are exactly the `K`-fixed rows already removed, so all
remaining rows are free.  Their count gives (5.6).  Columns and symbols are
free, and quarantining (5.1) gives (5.7).  Subtracting (5.6) from (5.7) and
using

\[
 \binom n{m-1}-\binom n{m-2}=\operatorname {Cat}_m
\]

gives (5.8).

For positivity, use

\[
 {\operatorname {Cat}_{j+1}\over\operatorname {Cat}_j}
       ={2(2j+1)\over j+2}\ge2.
\]

There are `2r+2` factors from `Cat_r` to `Cat_(3r+2)`, so

\[
 {\operatorname {Cat}_{3r+2}\over\operatorname {Cat}_r}
       \ge2^{2r+2}>4r+2={2n\over3},
\]

which is exactly `S_role>0`.

It remains to classify zero rows.  A quarantined rank-`3r+1`
set has occupancy type

\[
                         3^r1                         \tag{5.9}
\]

across the `K`-coordinate triples.  A nonfixed rank-`3r` row can lie below
such a set only if it has type

\[
                         3^{r-1}21.                   \tag{5.10}
\]

For a row of type (5.10), exactly one extension has type (5.9): add the
missing point to its unique two-point triple.  Call this extension `E`.
Every other long row has no extension of type (5.9).

If the full orbit of `E` lies in `T_0\setminus H_0`, no quarantined head
contains the row, so any tail other than `E` works.  If it lies in
`H_0\setminus T_0`, choose tail `B=E`; its symbol differs from `E` because
the table has no loop, and no second containing set can lie in `H_0`.  If
the orbit of `E` lies in neither bank, every role is available.

The only remaining case is

\[
                         [E]\in T_0\cap H_0.          \tag{5.11}
\]

Write the long row as

\[
                         R=E-\{t_0\},                 \tag{5.12}
\]

where `t_0` belongs to a full `K`-triple `T` of the fixed core of `E`.
Let `S={s_0,s_1,s_2}` be the singleton `K`-triple of `E`, with
`s_0 in E`, and put

\[
                         B_i=R+\{s_i\}\qquad(i=1,2). \tag{5.13}
\]

Both tails have type `3^(r-1)2^2`, so neither lies in `T_0`.  If both had
the unique possible quarantined head `E`, then

\[
                         \mu(B_i)=E+\{s_i\}\qquad(i=1,2). \tag{5.14}
\]

The two right sides of (5.14) are full-rotation equivalent: translation by
one of the two nonzero elements of `K` maps one to the other.  The two tails
`B_1,B_2` are not full-rotation equivalent.  To see this, any such rotation
would preserve or swap their two occupancy-two triples `T,S`.  A translation
cannot swap two distinct points of the odd cycle `Z_q`, since that would
give `2delta=0`.  It must therefore fix both triple labels and hence lie in
`K`.  Preserving the missing point `t_0` in `T` forces the identity, which
does not change the missing phase in `S`.

Thus two distinct tail orbits would be sent by the equivariant bijection
`mu` to one matched-value orbit, a contradiction.  At least one `B_i` has
head outside `H_0`, and is a legal relative atom.  Hence no zero row exists,
including in case (5.11).

Finally, a selected full-rotation atom orbit covers its free row orbit once
and has unit tail/head orbit loads.  The row, tail, and head conditions are
therefore exactly the three quotient matching rows.  The clean `G` action
is free on all physical endpoints, so the established voltage theorem says
that adding `F_0` gives a physical forest exactly when the developed
`G`-quotient is loopless and acyclic.  This proves the equivalence.  \(\square\)

If one instead quarantines the union `T_0 union H_0` from **both** endpoint
roles, the bulk becomes vertex-disjoint from `F_0`.  This removes
`2Cat_r-c` orbits per role and leaves scalar spare

\[
 S_{\rm vertex}
   ={\operatorname {Cat}_m\over n}
      -{5\over3}\operatorname {Cat}_r+c>0.           \tag{5.15}
\]

Indeed the same product bound gives
`Cat_(3r+2)/Cat_r>=2^(2r+2)>10r+5=5n/3`, which proves positivity.
This stronger quarantine
does not inherit the no-zero-row assertion above; it is a cleaner
sufficient subproblem, not an equivalent reduction.

## 6. The exact smaller-necklace seam bank

The obstruction is not an unstructured exponential family.  The proof
identifies it canonically as

\[
             \binom{\mathbb Z_{2r+1}}r\big/\mathbb Z_{2r+1}.   \tag{6.1}
\]

This set has `Cat_r` elements.  Theorems 4.1--4.2 solve its internal Latin
and forest rows exactly.  The remaining quotient-respecting construction
has the following relative form:

1. choose the fully equivariant first matching `mu`;
2. install the one-seam isolated bank indexed by (6.1);
3. complete every nonfixed row while avoiding the reserved columns and
   symbols and preserving the forest condition.

A complete mapping or Skolem/Langford starter may compress the description
of Step 2, but it cannot reduce its number of seams to a bounded sidecar.
Any literal starter containing only `t` quotient atom types develops to
only `t` row orbits, so a nonrecursive `O(m)` starter cannot saturate the
`Cat_r` forced sectors.

The tight pivot should therefore be imposed only after this bulk relative
selector is available.  Its `O(sqrt(m))` resource bank is negligible
relative to (3.3), but it cannot cure the residual fixed-row obstruction.

## 7. Revised frontier

The clean cyclic quotient remains useful: it removes the large free phase
and constructs the first matching `mu`.  The present result sharply limits
what can finish it.

* For `3`-free `2m-1`, the open problem is still the integral quotient
  Latin forest.
* For `3|2m-1`, an additional global braid is unavoidable.  Its minimum
  state space is the smaller Catalan necklace layer (6.1), not `O(1)`
  exceptional order-three orbits.  The exceptional rows themselves form an
  exact one-seam isolated-edge bank; relative completion of the bulk is
  open.
* Orthomorphisms and complete mappings can act on quotient atom types, but
  free-torsor rigidity prevents them from supplying hidden nonlinear phase
  freedom under exact equivariance.

This changes the status of the proposed non-affine shortcut: the bounded
exception route is disproved, the forced bank is explicitly solvable, and
the surviving target is a relative quotient Latin-forest completion around
a Catalan-indexed seam bank.
