# The exact certificates as an iterated Johnson flag tower

Date: 2026-07-28

Status: theorem-level synthesis from the raw exact words through `k=14` and
the current `k=15` Hall-29 carrier.  No `k=15` solution is claimed.

## 0. Main conclusion

The recurring non-forced structure in the odd exact answers is not best
described as three separately good lower shadows.  A depth-`d` resident
middle chronology produces one **iterated Johnson flag tower**:

\[
 L_i^{(q)}=\bigcap_{j=0}^{q}T_{i+j},\qquad
 L_i^{(q+1)}=L_i^{(q)}\cap L_{i+1}^{(q)}.
\]

Every row of this tower is itself a Johnson path.  Thus the depth-`q+1`
coverage problem is literally the intersection-edge-colour problem on the
depth-`q` path.  The depths are maximally correlated; they are not separate
occupancy experiments.

For odd `k`, the first row

\[
                         X_i=T_i\cap T_{i+1}
\]

contains essentially the whole construction.  It determines every interior
middle vertex by

\[
                         T_i=X_{i-1}\cup X_i,
\]

and it determines every deeper lower row by consecutive intersections.
Within the resident one-path normal form, optimal length forces `X` into one
of only two first-shadow types:

1. no repeated `(r-1)`-set and exactly one omitted set; or
2. one repeated occurrence and exactly two omitted sets.

The exact odd solutions have

\[
\begin{array}{c|c|c|c}
k&d&(h_1,c_1)&(h_1,\ldots,h_d)\\ \hline
7&2&(2,1)&(2,0)\\
9&2&(1,0)&(1,1)\\
11&3&(1,0)&(1,1,0)\\
13&3&(1,0)&(1,0,0),
\end{array}
\]

where `h_q` is the number of omitted depth-`q` lower colours and `c_1` is
first-shadow repeat excess.  The current `k=15` carrier instead has

\[
                 (h_1,c_1)=(4,3),\qquad(h_1,h_2,h_3)=(4,21,4).
\]

It is therefore exactly two first-shadow units outside the only admissible
optimal classes, before one asks the deeper Hall question.

A second theorem explains another conspicuous feature of the raw answers.
The `k=11` solution is obtained by opening one cyclic-equivariant component;
the `k=13` solution by opening and joining two.  Opening `c` cycles of a
shadow-perfect invariant factor destroys at most `cq` old depth-`q` windows,
and the resulting path retains at least `W-2c` edges in common with every
translate.  The measured overlaps are exactly

\[
            460=462-2\quad(k=11),\qquad
            1712=1716-4\quad(k=13).
\]

So the huge cyclic overlap is not decorative symmetry or a search accident.
It is the exact signature of a bounded-surgery construction.

Together these facts suggest a sharper mathematical target than “repair
Hall 29”: construct the first-shadow path `X` directly, in one of the two
admissible first-shadow classes, with its iterated intersection tower and
union lift simultaneously rainbow.  This is stated precisely in Section 7.

## 1. Scope and notation

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad T_i\in\binom{[k]}r,
\]

be a Johnson path: consecutive sets differ by one deletion and one
insertion.  Write

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\]

The path is **depth-`d` resident** when every internal coordinate run in
`T` has length at least `d+1`.  Equivalently, no coordinate inserted at one
transition is deleted during the next `d` transitions.  Boundary runs need
the corresponding one-sided condition; all statements below that mention
only internal indices avoid that bookkeeping.

For `0<=q<=d`, define

\[
 L_i^{(q)}=\bigcap_{j=0}^{q}T_{i+j}
 \quad(0\le i<W-q).
 \tag{1.1}
\]

Thus `L^(0)=T`, and `L^(q)` is the internal depth-`q` lower-shadow word.
Let

\[
 N_q=\binom{k}{r-q},
\]

let `h_q` be the number of members of that layer omitted by `L^(q)`, and
let

\[
 c_q=\sum_R(\mu_q(R)-1)^+
\]

be its repeat excess.

The lower-bound theorem by itself forces none of the Johnson, residence,
cyclic, or low-owner-dimension hypotheses when scalar slack is positive.
The theorems in this note are conditional structural theorems about the
normal form actually used by every stable exact construction from `k=6`
onward.  The empirical statements are labelled as such.

## 2. The iterated Johnson flag-tower theorem

### Theorem 2.1 (deleted-symbol formula)

For every `q<=d`,

\[
 \boxed{
 L_i^{(q)}=T_i\setminus\{a_i,a_{i+1},\ldots,a_{i+q-1}\}.}
 \tag{2.1}
\]

In particular `|L_i^(q)|=r-q`.

#### Proof

During the displayed `q` transitions, residence prevents an inserted
coordinate from being deleted again.  Hence the `q` deleted coordinates are
distinct coordinates of `T_i`, and no insertion belongs to all `q+1`
middle sets.  Removing exactly those deleted coordinates from `T_i` gives
their intersection.  \(\square\)

### Theorem 2.2 (flag-tower recurrence)

For `q<d`,

\[
 \boxed{L_i^{(q+1)}=L_i^{(q)}\cap L_{i+1}^{(q)}.}
 \tag{2.2}
\]

Moreover consecutive terms of `L^(q)` are Johnson adjacent.

#### Proof

The recurrence is the set identity

\[
 \left(\bigcap_{j=0}^{q}T_{i+j}\right)\cap
 \left(\bigcap_{j=1}^{q+1}T_{i+j}\right)
 =\bigcap_{j=0}^{q+1}T_{i+j}.
\]

For adjacency, (2.1) gives a common `(r-q-1)`-set

\[
 T_i\setminus\{a_i,\ldots,a_{i+q}\}.
\]

The first term adds `a_(i+q)` and the second adds `b_i`.  The former was
already present in `T_i`: if it had been inserted after time `i`, it would
be deleted within at most `q<=d` transitions, contradicting residence.  The
latter has not yet been deleted, again by residence.  They are distinct, so
the two terms are Johnson adjacent.  \(\square\)

### Corollary 2.3 (iterated rainbow interpretation)

The depth-`q+1` lower word is exactly the intersection-edge-colour word of
the depth-`q` Johnson path.  Consequently simultaneous lower coverage to
depth `d` is one recursively coloured path problem, not `d` independent
covering problems.

This is the deterministic mechanism behind the strong cross-depth
correlation seen both in PBBS-type carriers and in the exact words.

## 3. Compression to the first shadow

Put

\[
                         X_i=L_i^{(1)}=T_i\cap T_{i+1}.
\]

Assume `d>=2`.

### Theorem 3.1 (first-shadow reconstruction)

The sequence `X` is a Johnson path in `J(k,r-1)`, and every interior middle
vertex is recovered by

\[
 \boxed{T_i=X_{i-1}\cup X_i\qquad(1\le i\le W-2).}
 \tag{3.1}
\]

Furthermore,

\[
 \boxed{L_i^{(q)}=\bigcap_{j=0}^{q-1}X_{i+j}}
 \qquad(1\le q\le d).
 \tag{3.2}
\]

Away from the two ends, the upper shadows are also functions of `X`:

\[
 \bigcup_{j=0}^{q}T_{i+j}
   =\bigcup_{j=-1}^{q}X_{i+j}.
 \tag{3.3}
\]

#### Proof

The Johnson assertion is Theorem 2.2 at `q=1`.  Both `X_(i-1)` and `X_i`
are `(r-1)`-subsets of `T_i`.  They are distinct because the element
inserted at transition `i-1` cannot be deleted at transition `i`.  Their
union therefore has size `r` and equals `T_i`.  Formula (3.2) follows by
intersecting the defining adjacent pairs; every `T_i,...,T_(i+q)` occurs.
Formula (3.3) follows from (3.1).  \(\square\)

### Theorem 3.2 (residence drops by one)

A maximal internal run of a coordinate in `T` of length `ell` corresponds
to a maximal internal run in `X` of length `ell-1`.  Hence internal
depth-`d` residence of `T` is equivalent to every internal coordinate run
of `X` having length at least `d`.

#### Proof

The coordinate belongs to `X_i` exactly when it belongs to both `T_i` and
`T_(i+1)`.  Intersecting consecutive positions removes precisely the last
position of every internal run and changes no internal gap.  \(\square\)

### Theorem 3.3 (bi-rainbow reconstruction)

Let

\[
 X_0,\ldots,X_{W-2}\in\binom{[k]}{r-1}
\]

be a Johnson walk.  For `1<=i<=W-2`, colour its `i`th edge by

\[
                         Y_i=X_{i-1}\cup X_i.
 \tag{3.4}
\]

Suppose these `W-2` union colours are distinct.  Let `Y_-` and `Y_+` be the
two unused rank-`r` sets.  If they can be assigned to the two ends so that

\[
 Y_-\cap Y_1=X_0,\qquad
 Y_{W-2}\cap Y_+=X_{W-2},                              \tag{3.5}
\]

then

\[
 T=(Y_-,Y_1,\ldots,Y_{W-2},Y_+)
 \tag{3.6}
\]

is a Hamilton path of `J(k,r)` and its intersection-edge word is exactly
`X`.  Conversely every Hamilton middle path whose first shadow is `X`
arises this way.

#### Proof

Every consecutive pair in (3.6) shares the indicated `(r-1)`-set `X_i`;
the endpoint equations are exactly what is needed at the two ends.  All
terms have rank `r` and are distinct, and there are `W` of them, so they
enumerate the middle layer.  Conversely Theorem 3.1 gives every interior
term as the union colour (3.4), and the first and last middle sets are the
two omitted colours satisfying (3.5).  \(\square\)

Thus, in the extremal odd first-shadow class, the middle construction is a
literal **bi-rainbow path problem** one rank lower:

* its vertices cover all but one or two `(r-1)`-sets;
* its union edge colours cover all but two `r`-sets; and
* its intersection edge colours recursively form the next lower path.

The endpoint choice is only a two-by-two attachment test.  The hard object
is the bi-rainbow lower path, not a separately chosen rank-`r` chronology.

### Corollary 3.4 (the Middle Levels theorem supplies the first layer)

Let `k=2r-1`.  Take any Hamilton cycle in the middle levels incidence graph
on ranks `r-1` and `r`, and cut it at one rank-`(r-1)` vertex `X_*`.
Reading the remaining alternating path gives

\[
 T_0,X_0,T_1,X_1,\ldots,X_{W-2},T_{W-1}.
\]

Then the `T_i` enumerate every rank-`r` set, the `X_i` enumerate every
rank-`(r-1)` set except `X_*`, and

\[
 X_i=T_i\cap T_{i+1}.
\]

Thus the unconditional Middle Levels theorem supplies a Type-I
first-shadow carrier (`h_1=1,c_1=0`) for every odd `k`.  Moreover the one
omitted colour lies in **both** endpoints, because those were its two
neighbours before the cut.

This sharply locates the open content.  The first bi-rainbow layer is not an
existence problem.  One must choose such a cycle (or a bounded-component
variant) so that its upper projection is also depth-`d` resident, its
iterated intersection rows cover the deeper lower layers, and its higher
unions and owner system are compatible.  The exact `k=11` omission `155`
being contained in both endpoints is the literal signature of this
Middle-Levels cut mechanism.

There is a complementary unconditional half.  A tight enumeration of the
two levels `r-2,r-1` projects to a Hamilton cycle of `J(k,r-1)` whose
intersection edge colours cover every rank-`(r-2)` set.  Therefore the two
classical inputs say:

\[
\begin{array}{c|c|c}
\text{source}&\text{vertex/union property of }X&
                 \text{intersection property of }X\\ \hline
\text{Middle Levels Hamilton cycle}&\text{perfect}&\text{uncontrolled}\\
\text{two-level tight enumeration}&\text{perfect vertices; unions uncontrolled}&\text{perfect}.
\end{array}
\]

They generally give different `X` cycles.  Their conjunction is exactly the
first nontrivial piece of the present problem: one nearly Hamilton path in
`J(k,r-1)` whose union colours are all distinct and whose intersection
colours cover the next layer.  The flag-tower theorem then asks to iterate
the intersection property and add residence.  This explains why both
classical theorems look tantalizingly close while neither alone compiles an
optimal OR word.

### Exact reduction 3.5

Within the resident flat-middle normal form, one may therefore search on
`X`, not on `T`.  Choose a Johnson path of `(r-1)`-sets and two endpoint
`r`-supersets.  Define the interior middle sets by (3.1).  Then impose:

1. the resulting `W` middle sets are distinct and cover `binom([k],r)`;
2. the endpoint intersections are the prescribed first and last `X` terms;
3. every internal coordinate run of `X` has length at least `d`;
4. the consecutive intersections in (3.2) and unions in (3.3), with their
   endpoint versions, have the required coverage; and
5. the resulting intersection tableau has a realizable injective lower
   owner assignment.

These conditions are necessary and sufficient for the normal form: the
forward direction is Theorems 2.1--3.2, and the reverse direction reconstructs
`T`, then its maximal erosion, and finally the source word from the owner
assignment.

This removes one whole layer of chronology variables.  More importantly,
it exposes what the first-shadow defect means structurally: it is a defect
in a nearly spanning path of `J(k,r-1)`, not merely a scalar score attached
to a rank-`r` path.

## 4. The all-depth palette conservation law

The familiar immediate-shadow identity has an exact all-depth extension.

### Theorem 4.1 (path-cover palette law)

Suppose the middle layer is partitioned into path components of sizes
`n_1,...,n_p`.  At depth `q`, the number of internal windows is

\[
 S_q=\sum_{j=1}^{p}\max(n_j-q,0).
 \tag{4.1}
\]

Then

\[
 \boxed{h_q-c_q=N_q-S_q.}
 \tag{4.2}
\]

If every component has more than `q` vertices, this becomes

\[
 \boxed{h_q-c_q=N_q-W+pq.}
 \tag{4.3}
\]

#### Proof

The number of distinct depth-`q` colours is both `N_q-h_q` and
`S_q-c_q`.  Equating them proves (4.2); substituting `S_q=W-pq` proves
(4.3).  \(\square\)

Thus, after subtracting the arithmetic collision floor, excess collisions
and holes are the same quantity.  In particular, for odd `k=2r-1`, one has
`N_1=W`, so a one-path carrier satisfies

\[
                         h_1=c_1+1.
 \tag{4.4}
\]

### Lemma 4.2 (two boundary chains)

In a flat depth-`d` resident construction, an internally missing
rank-`(r-1)` target can be realized below the middle row only on one of two
nested boundary chains.  Each chain can realize at most one distinct
rank-`(r-1)` target.  Consequently

\[
                              h_1\le2.
 \tag{4.4a}
\]

#### Proof

Consider a physical cell of depth `h<d`.  Its maximal erosion envelope is a
consecutive intersection `T_a cap ... cap T_b`, hence has rank
`r-(b-a)`.  If the cell realizes a rank-`(r-1)` target, its envelope must
have rank at least `r-1`, so `b-a<=1`.

If `b-a=1`, the envelope itself is one of the internal first-shadow colours.
A rank-`(r-1)` subset of that envelope equals the envelope, so it cannot be
an internally missing colour.  The remaining case is `a=b`.  Boundary
clipping then forces the envelope to be `T_0` or `T_(W-1)`.  The relevant
physical cells are respectively prefixes of the source word at the left end
and suffixes at the right end.  Their ORs are nested by inclusion.  Two
nested sets of the same rank `r-1` are equal, so each end supplies at most
one distinct missing target.  \(\square\)

The lemma also explains why the `k=13` normalized compiler may place one
rank-six owner in each of two shallower boundary rows without contradicting
the bound: the shallower rows do exist, but their same-end outputs are a
nested chain, not independent capacity.

### Corollary 4.3 (endpoint-containment test)

Every internally missing first-shadow target that is realizable on the fixed
carrier is contained in `T_0` or in `T_(W-1)`.  In particular, a missing
rank-`(r-1)` set contained in neither endpoint is a literal fixed-carrier
Hall obstruction.

The raw odd exact answers saturate this test in the cleanest possible way:

\[
\begin{array}{c|c|c}
k&\text{missing first-shadow masks}&\text{endpoint containment}\\ \hline
7&13,70&13\subset T_0,\ 70\subset T_{W-1}\\
9&170&170\subset T_{W-1}\\
11&155&155\subset T_0\cap T_{W-1}\\
13&2135&2135\subset T_{W-1}.
\end{array}
\]

This is a genuinely non-forced alignment between the omitted colour and the
two endpoint flags.

### Corollary 4.4 (the odd first-shadow dichotomy)

In an optimal resident one-path compiler, Lemma 4.2 and (4.4) give
`c_1<=1`.
Equivalently the first-shadow word `X` has exactly one of the following two
types:

* it is simple and omits one `(r-1)`-set;
* it has one repeat-excess unit and omits two `(r-1)`-sets.

The current Hall-29 carrier has `(h_1,c_1)=(4,3)`.  Its missing masks are

\[
                         5801,\ 7267,\ 8877,\ 13620.
\]

Exactly two are endpoint-compatible:

\[
              8877\subset T_0,\qquad7267\subset T_{W-1},
\]

with literal endpoint masks `T_0=9901` and `T_(W-1)=7779`.

whereas `5801` and `13620` are contained in neither endpoint.  Corollary 4.3
therefore gives a direct fixed-carrier deficiency of at least two, with no
DM computation.  These are exactly the two raw rank-seven holes that remain
as holes in the peeled Hall-29 kernel; its other six rank-seven survivors are
collision partners.  The deeper Hall witness strengthens this elementary
two-unit obstruction to 29.

### Theorem 4.5 (coordinatewise run law)

Let `b_x` be the number of maximal runs of coordinate `x` in the linear
middle word `T`, and let `mu_1(R)` be first-shadow multiplicity.  Then

\[
 \boxed{
 b_x=\binom{k-1}{r-1}-
          \sum_{R\ni x}\mu_1(R).}
 \tag{4.5}
\]

For odd `k=2r-1`, this is

\[
 \boxed{
 b_x=C_{r-1}
   +\#\{R\in H_1:x\in R\}
   -\sum_{R\ni x}(\mu_1(R)-1)^+,}
 \tag{4.6}
\]

where `C_(r-1)` is the Catalan number.

#### Proof

In a binary word, the number of one-runs equals the number of ones minus the
number of adjacent `11` pairs.  Coordinate `x` lies in exactly
`binom(k-1,r-1)` middle sets.  An adjacent pair has `11` in coordinate `x`
exactly when its intersection colour contains `x`, which proves (4.5).
Adding and subtracting the complete rank-`(r-1)` layer gives

\[
 \binom{2r-2}{r-1}-\binom{2r-2}{r-2}=C_{r-1},
\]

and separates omitted from repeated colours, proving (4.6).  \(\square\)

For a Type-I first shadow with unique omission `R_*`, this specializes to

\[
 b_x=C_{r-1}+\mathbf1_{x\in R_*}.
 \tag{4.7}
\]

The exact run-count vectors at `k=9,11,13` therefore contain no additional
search information: their `+1` coordinates are exactly the coordinates of
the unique omitted first-shadow mask.  What remains genuinely free is the
**distribution of run lengths**, which controls residence.  This separates
two statistics that had repeatedly been conflated: the q1 palette fixes the
number of runs, but not whether any run is too short.

### Corollary 4.6 (the whole ballot block hierarchy)

For a fixed `t`-set `Q`, let `b_Q` be the number of maximal blocks of middle
positions whose sets contain `Q`.  Then, for odd `k=2r-1`,

\[
 b_Q=
 \frac{t}{r}\binom{2r-1-t}{r-t}
 +\#\{R\in H_1:Q\subseteq R\}
 -\sum_{R\supseteq Q}(\mu_1(R)-1)^+.
 \tag{4.8}
\]

In the Type-I case with unique omission `R_*`,

\[
 \boxed{
 b_Q=\frac{t}{r}\binom{2r-1-t}{r-t}
      +\mathbf1_{Q\subseteq R_*}.}
 \tag{4.9}
\]

#### Proof

Apply “number of one-blocks = number of ones minus adjacent `11` pairs” to
the indicator of `Q subseteq T_i`.  There are `binom(k-t,r-t)` middle sets
containing `Q`, while adjacent `11` pairs are counted by first-shadow
occurrences `R superset Q`.  The complete-layer difference is

\[
 \binom{2r-1-t}{r-t}-\binom{2r-1-t}{r-1-t}
 =\frac{t}{r}\binom{2r-1-t}{r-t}.
\]

Separating omissions and repeat excess gives (4.8), and Type I gives
(4.9).  \(\square\)

Thus the Catalan count (`t=1`) and every higher ballot block count observed
in the exact certificates are consequences of the first-shadow palette.
They should be used as consistency checks, not optimized as independent
features.

## 5. What is genuinely non-forced in the exact words

The following census is computed directly from the normalized raw answers,
with the Hall-29 carrier appended as the comparison row.

\[
\begin{array}{c|c|c|c|c}
k&d&(h_1,c_1)&(h_1,\ldots,h_d)&\text{minimum internal run in }T\\ \hline
7&2&(2,1)&(2,0)&3\\
9&2&(1,0)&(1,1)&3\\
10&2&(0,41)&(0,0)&3\\
11&3&(1,0)&(1,1,0)&4\\
12&2&(0,131)&(0,0)&3\\
13&3&(1,0)&(1,0,0)&4\\
14&2&(0,428)&(0,0)&3\\
15\text{ H29}&3&(4,3)&(4,21,4)&4.
\end{array}
\]

For even `k`, `N_1<W`, so the large displayed `c_1` contains the forced
arithmetic surplus and is not a defect.  For odd `k`, the first-shadow column
is directly comparable.  The exact `k=8` word is omitted from this table
because its chosen middle chronology has two non-Johnson transitions and is
therefore outside the hypotheses of the flag-tower theorem; this is another
useful reminder that the normal form is constructed, not forced by the
scalar lower bound.

Three patterns are genuinely informative rather than scalar consequences of
the lower bound.

1. **Exact residence.** Every displayed chronology meets the minimum
   run threshold exactly; residence is built into the path rather than
   repaired by the compiler.
2. **Near-Hamilton first shadow.** The `k=9,11,13` first-shadow paths are
   simple and omit exactly one vertex.  This is the extremal type in
   Corollary 4.4, but the lower bound with positive slack does not force the
   construction to use this normal form.
3. **Simultaneous flatness.** Their deeper lower rows are perfect or miss a
   single boundary-compatible colour.  By Theorem 2.2 this is one iterated
   rainbow phenomenon, not a coincidence repeated at each rank.

The actual missing masks sharpen the last point.  At `k=9` they form the
nested endpoint flag `42 subset 170` through the two required depths (and
the next, nonrequired missing mask is `10 subset 42`); at `k=11` they form
`154 subset 155`; at `k=13` only the top member `2135` is missing.  Nestedness
is not forced by the palette law.  It is how one boundary choice pays several
depth conditions at once.

The normalized owner maps add a fourth non-forced pattern:

\[
 \max_p\kappa_p\le1\quad(6\le k\le13),\qquad
 \#\{p:\kappa_p=2\}=5\quad(k=14),
\]

where `kappa_p` is the owner meet dimension.  Hence the chronology is global,
but the final pointwise negative compiler remains of width one or two.

## 6. Why the `k=11` and `k=13` symmetry is mathematical

Let a group `Gamma` act on `J(k,r)`.  Let `F` be a `Gamma`-invariant
2-factor on all `W` middle vertices, with `c` cycle components.  Choose one
edge from every cycle, delete the resulting cut set `C`, and add `c-1` seam
edges to obtain one spanning path `P`.

### Theorem 6.1 (cyclic upper-excess design)

First suppose `k=2r-1` and `F` has perfect cyclic first lower shadow and
covers every rank-`(r+1)` upper union.  If `mu(U)` is the upper-union load,
let the excess multidesign `D` contain `mu(U)-1` copies of every target `U`.
Then

\[
 \boxed{|D|=C_r,\qquad d_D(x)=2C_{r-1}\quad(x\in[k]).}
 \tag{6.1}
\]

#### Proof

There are `W` cyclic upper-union occurrences and
`binom(2r-1,r+1)` targets.  Their difference is

\[
 W-\binom{2r-1}{r+1}
 =\frac{2W}{r+1}=C_r.
\]

For a coordinate `x`, the cyclic middle word has
`binom(2r-2,r-1)=rC_(r-1)` ones.  Perfect cyclic first lower shadow gives
exactly `C_(r-1)` one-runs by Theorem 4.5 with no omissions or repeats.
Therefore `x` belongs to `(r+1)C_(r-1)` adjacent unions.  The complete
rank-`(r+1)` layer contains `x` in
`binom(2r-2,r)=(r-1)C_(r-1)` targets.  Subtraction gives excess degree
`2C_(r-1)`.  \(\square\)

This exposes a composite-only feature at the first open case.  Under cyclic
translation, the `k=11` and `k=13` excess designs can be unions of free
orbits: `C_6=132=12*11` and `C_7=429=33*13`.  At `k=15`, however,

\[
                         |D|=C_8=1430\equiv5\pmod {15}.
\]

A rank-nine set has cyclic orbit size `15` or `5`: a short orbit is exactly
a union of three cycles of the translation by five.  Hence every
`Z_15`-invariant upper-excess multidesign necessarily contains a short
five-orbit, with the number of such orbit copies congruent to one modulo
three.  If the upper profile is simple (`mu<=2`), it must contain exactly one
of the two available short five-orbits and 95 free orbits.

This is not an obstruction, but it is a forced exceptional block absent from
the prime `k=11,13` constructions.  Any invariant `k=15` proof or search that
silently assumes all upper-excess orbits are free is infeasible.

### Theorem 6.2 (bounded-surgery shadow theorem)

Fix `q` smaller than every component length.

1. Opening the cycles removes exactly `cq` cyclic depth-`q` windows.
2. Adding the seams creates exactly `(c-1)q` new depth-`q` windows.
3. If `F` has `h_q(F)` missing lower (or upper) depth-`q` colours, then

\[
                       h_q(P)\le h_q(F)+cq.
 \tag{6.2}
\]

4. More exactly, before the seams are added, a target disappears if and
   only if every one of its cyclic occurrences crosses a chosen cut.
5. If `F` is depth-`d` resident, every new residence failure in `P` lies in
   the `d`-transition collar of a seam.

#### Proof

At one cut of a cycle, precisely the `q` cyclic windows whose transition
interval crosses that cut cease to exist.  Summing over the `c` cycles gives
the first assertion.  A seam between two paths participates in exactly `q`
new windows, proving the second.  Deletion can destroy at most one distinct
target per deleted occurrence, while adding windows cannot create a hole,
which proves (6.1).  The exact criterion in part 4 is simply the definition
of losing all occurrences.  Every unchanged internal window has the same
coordinate word as in `F`, so a new short run must cross a seam.  \(\square\)

### Theorem 6.3 (translate-overlap signature)

For every `g in Gamma`,

\[
 \boxed{|E(P)\cap gE(P)|\ge W-2c.}
 \tag{6.3}
\]

#### Proof

Since `F` is invariant, both `P` and `gP` contain every edge of

\[
                         F\setminus(C\cup gC).
\]

The cut union has size at most `2c`.  \(\square\)

For the exact `k=11` carrier, `c=1` and every nontrivial cyclic shift has
directed overlap `460=W-2`.  For `k=13`, `c=2` and every nontrivial cyclic
shift has directed overlap `1712=W-4`.  Equality in (6.2) is observed in
both cases.

This proves that the enormous shift overlap is the fingerprint of the
bounded-surgery construction.  It also explains the successful division of
labour:

* an invariant factor pays for all bulk shadow constraints at once;
* only `O(cd)` collars must be checked for residence and lost shadows;
* the compiler spends its boundary/slack budget on those collars.

At depth `q`, an optimal word has `2q` noninternal physical cells in the
corresponding nominal row.  Hence `c=2` is the exact numerical threshold at
which the crude loss bound `cq` still fits the boundary-cell count `2q` at
every depth.  This is only a capacity statement, not a Hall theorem, but it
explains why one component at `k=11` and two at `k=13` are qualitatively
special.

## 7. The revised mathematical target for `k=15`

The Hall-29 path is already resident and upper-complete.  Its failure is
that its first-shadow path `X` lies outside the two admissible optimal types,
and the defect propagates through its iterated intersection tower.  Local
carrier moves can improve one displayed neighbourhood while transporting
the same flag defect elsewhere.

Theorem 3.3 makes the diagnosis sharper.  Because H29 already is a Hamilton
middle path, the union edge colours of its `X`-walk are automatically all
distinct: that half of the bi-rainbow condition is solved exactly.  What
fails is the vertex palette of `X` (four omissions and three repeats), and
then the intersection edge palette one level lower (21 omissions).  The
mathematical move required at `k=15` is therefore a reorganization of a
union-rainbow walk into a nearly vertex-Hamilton, recursively
intersection-rainbow walk.

The certificate evidence therefore supports the following target.

### Boundary-absorbing bi-rainbow flag path

For odd `k=2r-1`, construct a Johnson path

\[
 X_0,\ldots,X_{W-2}\in\binom{[k]}{r-1}
\]

and two endpoint `r`-supersets such that:

1. `X` is simple with one omitted vertex, or has one repeat and two omitted
   vertices;
2. the unions `X_(i-1) union X_i`, together with the endpoints, enumerate
   `binom([k],r)` exactly;
3. every internal coordinate run in `X` has length at least `d`;
4. the iterated intersections of consecutive `X` terms cover the required
   lower layers, with all omissions routable into the two boundary triangles;
5. the corresponding consecutive unions cover every upper layer; and
6. the resulting lower tableau has an injective owner assignment of
   pointwise meet dimension at most two.

By Exact Reduction 3.5 and the nested-owner realization theorem, such an
object yields a word of length `W+d=B(k)`; the monotone-deadline lower bound
then proves equality.

There is a particularly concrete invariant subtarget for `k=15`: find a
`Z_15`-invariant resident, shadow-complete middle 2-factor with at most two
components, then choose cuts and seams whose lost occurrences are restored
or absorbed at the boundary.  Theorem 6.2 makes every remaining audit
bounded-size.  Failure of the two-component invariant subtarget would not
refute the general flag-path target, but success would reproduce exactly the
mechanism already certified at `k=11` and `k=13`.

## 8. Practical consequence

The mathematically nonredundant search coordinate is now the first-shadow
path `X` and its flag tower.  Searching only on the rank-`r` chronology hides
three exact facts:

* middle vertices are mostly unions of consecutive `X` terms;
* residence is a minimum-run constraint one unit shorter on `X`; and
* every lower depth is obtained by applying the same intersection-edge
  operator again.

For `k=15`, a candidate with `(h_1,c_1)` outside `{(1,0),(2,1)}` cannot be a
terminal optimal flat resident carrier, regardless of how good its upper
score is.  A candidate inside those two classes should be evaluated by the whole
iterated flag tower and owner compatibility, not by three unrelated hole
counts.  This is the cleanest theorem-level reconciliation of the solved
certificates with Hall 29.

## 9. Audited finite inputs

The empirical rows and endpoint-containment checks in this note use:

```text
answers/k07.word
answers/k09.word
answers/k10.word
answers/k11.word
answers/k12.word
answers/k13.word
answers/k14.word
scratch/raw_optimal_words_k01_k14.json
scratch/raw_optimal_k06_k14_compiler_normal_form_audit.json
scratch/k15_doubletrans_05_213_hall29.json
scratch/k15_h29_one_owner_cia_audit.json
```

All theorem statements before substitution of these finite values are
independent of the searches that produced the files.
