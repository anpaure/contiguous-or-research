# PBBS two-boundary flags: the exact `2q` halo theorem, rankwise Hall, and the common-compiler gate

Date: 2026-07-29

Status: unconditional boundary-capacity and Hall-reduction theorems, and a
conditional laminar-package compiler theorem.  PBBS supplies the demand
flags and their cut ledger; it does not supply the Hall expansion or the
common compiler required by the conditional theorem.

## 0. Verdict

Let `T` be a linearly depth-`d` resident rank-`r` Johnson path of length
`W`, and let `A` have length

\[
                         L=W+d,
 \qquad D^dA=T.                                          \tag{0.1}
\]

At lower depth `q`, a rank-`(r-q)` target which is not realized in its
natural internal row has only two kinds of alternative source:

1. an interior cell in one of the preceding `q-1` short rows; or
2. one of `q` fixed-start chains in the left halo or `q` fixed-end chains
   in the right halo.

Each boundary chain is nested and hence supplies at most one distinct
rank-`(r-q)` target.  The boundary contribution is therefore exactly

\[
                              2q.                        \tag{0.2}
\]

For `q=1` there is no preceding row, so the capacity is exactly two.  In a
two-cycle q1-rainbow opening these are the two global boundary chains, and
the two deleted q1 colours are individually admissible there.  For
`q>=2`, the number `2q` is only the boundary term: unused or duplicate
cells in the preceding rows are a separate shared bank.  In particular,
the scalar necessary inequality is

\[
                       h_q\le S_{q-1}+2q,                \tag{0.3}
\]

not `h_q<=2q` for the full compiler.

PBBS gives a canonical correct-rank occurrence of every lower target.
After one cut in each of two cycles, at most `q` selected depth-`q`
occurrences cross either cut.  Thus the selected seam-hole family obeys

\[
                         |H_q|\le2q.                     \tag{0.4}
\]

Moreover the crossing occurrences split into fixed-offset nested flag
chains, so PBBS gives an explicit target-to-boundary-chain graph.  Hall's
inequalities in that graph are necessary, and ordinary max flow makes them
integral rank by rank.

This does **not** prove a common depth-`d` compiler.  Distinct matched pins
can delete the last two occurrences of one coordinate in the same central
window, although each pin is individually admissible.  A valid sufficient
theorem must add the exact common-pin conditions.  One useful checkable
version is: choose the Hall assignments so that the exceptional halo
intervals form an inclusion-monotone laminar forest and satisfy the atom,
controller port/gap, native-trace-survival, and point-core tests.  The
coordinatewise maximal word then realizes all pins integrally.

There is no dimension-uniform theorem saying that the bounds (0.4) alone
make this laminar condition automatic.  One boundary can contain
`q` distinct holes at every depth, a total of `d(d+1)/2`; a laminar family
of distinct nonempty intervals on its `d` source positions has at most
`2d-1` members.  The scalar implication already fails for `d>=3`.

## 1. The exact fixed-pin kernel

For a resident path `T`, put

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<L.                                      \tag{1.1}
\]

Residence gives `D^dP=T`.  A pin is a pair `(I,S)`, where `I` is a
nonempty source interval and the requested equality is

\[
                         \bigcup_{p\in I}A_p=S.          \tag{1.2}
\]

For a pin family `Pi`, define

\[
 K_p(\Pi)=P_p\cap
          \bigcap_{(I,S)\in\Pi:\,p\in I}S.             \tag{1.3}
\]

### Lemma 1.1 (maximal-core criterion)

There is a nonzero word satisfying `D^dA=T` and all pins in `Pi` if and
only if

\[
 K_p(\Pi)\ne\varnothing\qquad(0\le p<L),               \tag{1.4}
\]

\[
 [i,i+d]\cap\{p:x\in K_p(\Pi)\}\ne\varnothing
 \qquad(x\in T_i),                                      \tag{1.5}
\]

and

\[
 I\cap\{p:x\in K_p(\Pi)\}\ne\varnothing
 \qquad((I,S)\in\Pi,\ x\in S).                        \tag{1.6}
\]

When these conditions hold, the coordinatewise maximal solution is

\[
                         A_p=K_p(\Pi).                  \tag{1.7}
\]

#### Proof

Every central equality forces `A_p subseteq P_p`; every extra pin containing
`p` forces `A_p subseteq S`.  Hence every solution is contained in (1.3),
which proves necessity of (1.4)--(1.6).  Conversely, (1.3) excludes every
forbidden coordinate.  Equations (1.5) and (1.6) supply every positive
coordinate of the central and extra pins, and (1.4) makes every source
letter nonempty.  Thus (1.7) realizes all equalities.  `square`

For a background family `Pi`, call a candidate pin `(I,S)` **individually
admissible** if `Pi union {(I,S)}` passes Lemma 1.1.  This is an exact,
finite, coordinatewise test; no LP rounding is involved.

## 2. The boundary-cell trichotomy

Assume that every consecutive intersection of `s+1<=d+1` middle states has
the fresh rank

\[
 \left|\bigcap_{i=u}^{u+s}T_i\right|=r-s.               \tag{2.1}
\]

This follows from strong depth-`d` residence along a Johnson path.

For a source cell `I=[a,b]`, `b-a<d`, the central windows containing `I`
have indices

\[
 J(a,b)=
 [\max(0,b-d),\min(a,W-1)].                             \tag{2.2}
\]

Every realization satisfies

\[
 \bigcup_{p=a}^{b}A_p
 \subseteq \bigcap_{i\in J(a,b)}T_i.                   \tag{2.3}
\]

Define the fixed-start and fixed-end boundary chains

\[
 \mathcal L_j={[j,j+t]:0\le t\le d-1-j\},             \tag{2.4}
\]

\[
 \mathcal R_j=
 \{[L-1-j-t,L-1-j]:0\le t\le d-1-j\},                 \tag{2.5}
\]

for `0<=j<d`.

### Theorem 2.1 (exact boundary-chain classification)

Let `S` have rank `r-q`, `1<=q<=d`, and suppose `S` is realized on a
source interval `I=[a,b]` of at most `d` letters.  Exactly one of the
following applies.

1. `I` is an interior interval of `d-q+1` letters.  Then `S` equals the
   natural intersection of `q+1` consecutive middle states.
2. `I` is an interior interval in one of the preceding `q-1` rows; that
   is, it has at least `d-q+2` letters.
3. `I` belongs to `L_j` or `R_j` for some `0<=j<q`.

Consequently, after the preceding-row bank is frozen, the two boundary
halos can realize at most `2q` distinct non-natural rank-`(r-q)` targets.

#### Proof

Put `n=|J(a,b)|`.  By (2.1), the right side of (2.3) has rank `r-n+1`.
Since it contains the rank-`(r-q)` set `S`, one has

\[
                              n\le q+1.                 \tag{2.6}
\]

If neither end of (2.2) is clipped, then

\[
 n=d-(b-a)+1.                                           \tag{2.7}
\]

Equality `n=q+1` forces equality in (2.3), giving item 1.  If `n<=q`,
then `b-a>=d-q+1`, so the interval lies in one of the preceding `q-1`
rows, giving item 2.

If the left end is clipped, then `b<d` and `J(a,b)=[0,a]`.  Hence
`n=a+1<=q+1`.  If `a=q`, equality of ranks again gives the natural prefix
intersection.  Otherwise `a=j<q`, and `I in L_j`.

If the right end is clipped, then `a>W-1` and
`J(a,b)=[b-d,W-1]`.  Writing `j=L-1-b` gives `n=j+1`.  The equality case
`j=q` is the natural suffix intersection; otherwise `j<q` and
`I in R_j`.  These cases exhaust (2.2).

For fixed `j`, the intervals in (2.4), and separately those in (2.5), are
nested.  Their OR values are therefore nested.  Two distinct nested sets
cannot have the same rank, so each chain supplies at most one distinct
rank-`(r-q)` value.  There are `q` chains at either end.  `square`

### Corollary 2.2 (q1 is qualitatively different)

At `q=1` there is no preceding-row bank.  Every missing rank-`(r-1)`
target must use `L_0` or `R_0`, so the capacity is exactly two.  At larger
depth the boundary term is `2q`, but it competes with the common surplus in
the preceding rows.  In the notation of the shadow-prefix ledger this is

\[
                         h_q\le S_{q-1}+2q.             \tag{2.8}
\]

For odd `k`, reserving one natural occurrence of every q1 colour sharpens
the depth-two instance to

\[
                         h_2\le c_1+4=h_1+3.            \tag{2.9}
\]

The number four in (2.9), rather than the q1 number two, is the first
genuine nested-boundary capacity.

## 3. What the two PBBS cuts supply

On an oriented cyclic middle component, write

\[
 F_{q,s}=\bigcap_{i=-s}^{q-s}T_i,
 \qquad 1\le s\le q,                                   \tag{3.1}
\]

for the `q` depth-`q` windows crossing the cut between `T_{-1}` and
`T_0`.  A short component only decreases this count.

### Lemma 3.1 (cut ledger and fixed-offset chains)

Choose one canonical PBBS occurrence of every rank-`(r-q)` target.  After
one cut in each of two components, let `H_q` be the targets whose selected
occurrence is destroyed and which have no credited surviving or seam-created
occurrence.  Then

\[
                         |H_q|\le2q.                    \tag{3.2}
\]

For a fixed offset `j=q-s`, the crossing values

\[
 F_{q,q-j},\qquad q=j+1,j+2,\ldots,d,                  \tag{3.3}
\]

form a decreasing nested flag and satisfy

\[
 F_{q,q-j}\subseteq\bigcap_{i=0}^{j}T_i.               \tag{3.4}
\]

Thus the crossing occurrences at one cut canonically map to the `q`
chains `L_0,...,L_(q-1)` at depth `q`; reversal gives the right-hand map.

#### Proof

A fixed cut edge belongs to exactly `q` cyclic windows of `q+1` owners, or
at most `q` when the component is shorter.  Two cuts therefore destroy at
most `2q` selected occurrences, proving (3.2).  Holding `j=q-s` fixed and
increasing `q` adds owner states only on the negative side of (3.1), so the
intersections decrease.  Every such window contains `T_0,...,T_j`, which
gives (3.4).  `square`

The PBBS all-depth theorem supplies the canonical occurrences used here,
with correct-rank load between `1` and `binom(2q+1,q)`.  The lower bound
being one is important: it gives no uniform reserve against a cut.  The
upper bound is not a Hall expansion theorem.

Before compiler admissibility is imposed, the occurrence-to-chain map is
already injective after duplicate target values are collapsed: distinct
values can be represented by distinct crossing occurrences.  The Hall
problem appears only after chains whose corresponding source pins fail the
maximal-core test are deleted.  Thus PBBS supplies the unpruned incidence,
not expansion of the admissible graph (4.1).

At `q=1`, if the factor has a squarefree complete q1 colour deck, the holes
are exactly the two cut colours not restored by the seam.  Each cut colour
is individually admissible at the outer boundary of its own opened
component: the cut facet and the retained incident facet are distinct
facets of the same `r`-set, and their union is that `r`-set.  Hence setting
the extreme source letter to the cut facet preserves the central window.
This proves the two q1 edges of the boundary graph, but no deeper edge.

## 4. The PBBS-checkable rankwise Hall graph

Fix a background pin family `Pi`, containing all lower targets already
credited to surviving native cells and any protected compiler pins.  For
`S in H_q`, define

\[
 \begin{split}
 N_q(S)=\{&L_j:0\le j<q,\ \exists I\in\mathcal L_j
                 \text{ with }(I,S)\text{ individually admissible}\}\\
 \cup\{&R_j:0\le j<q,\ \exists I\in\mathcal R_j
                 \text{ with }(I,S)\text{ individually admissible}\}.
                                                               \tag{4.1}
 \end{split}
\]

All sets in (4.1) are obtained from the endpoint `d`-collars, the PBBS flag
labels, and Lemma 1.1.  Thus the graph has at most `|H_q|<=2q` left
vertices and exactly `2q` right vertices.

### Theorem 4.1 (rankwise boundary Hall)

If a common compiler realizes every member of `H_q` on the boundary halos,
while realizing `Pi`, then

\[
 |X|\le |N_q(X)|\qquad(X\subseteq H_q).                \tag{4.2}
\]

Conversely, (4.2) gives an integral injection of `H_q` into the boundary
chains.  If concrete witnessing intervals for the matched edges can be
chosen so that their union with `Pi` passes Lemma 1.1, then all members of
`H_q` are installed simultaneously.

#### Proof

Choose one boundary witness cell for each target in an existing compiler.
Theorem 2.1 assigns it to `L_j` or `R_j` with `j<q`.  Two distinct
rank-`(r-q)` values cannot use the same chain, so these choices form an
injection into (4.1).  Hall's inequalities follow.

Conversely Hall's theorem, equivalently integral max flow in the usual
source--target--chain--sink network, gives the injection.  The last clause
is Lemma 1.1 applied to all selected pins together.  `square`

The final clause cannot be deleted.  Suppose a coordinate `x` has exactly
two allowed occurrences `p_1,p_2` in one required central window.  A pin
omitting `x` on `p_1` is individually admissible, as is a different pin
omitting `x` on `p_2`.  They may occupy distinct Hall resources, but
together they delete both occurrences and violate the central equality.
This is the minimal common-coordinate obstruction to turning (4.2) into a
full compiler theorem.

There is a compact form of (4.2) when the **neighbourhoods**, rather than
merely the PBBS target labels, are laminar.

### Theorem 4.2 (laminar-neighbourhood Hall reduction)

Let `D` be unit demands and let the boundary-chain resources `B` have
integral capacities `b(c)`.  Suppose the distinct nonempty neighbourhoods

\[
                         \{N(u):u\in D\}                \tag{4.3}
\]

are laminar.  A capacitated matching saturating `D` exists if and only if,
for every neighbourhood node `C` in (4.3),

\[
 \boxed{
 |\{u\in D:N(u)\subseteq C\}|
       \le\sum_{c\in C}b(c).}                           \tag{4.4}
\]

#### Proof

Necessity is immediate.  For sufficiency, take an arbitrary `X subseteq D`.
The inclusion-maximal neighbourhoods among `N(u)`, `u in X`, are pairwise
disjoint.  Partition `X` according to these maximal nodes.  Applying (4.4)
to every part and summing gives

\[
                         |X|\le\sum_{c\in N(X)}b(c),    \tag{4.5}
\]

which is the capacitated Hall inequality.  Integral max flow gives the
matching.  `square`

If every depth-`q` hole sees the complete `2q` bank, (4.4) collapses to the
scalar capacity inequality.  With proper subbanks, every laminar-node cut
is required.  Laminarity of the set labels in the PBBS flags does not imply
laminarity of the target-to-chain neighbourhoods (4.1); the latter must be
checked from the actual endpoint collars.

## 5. A genuine laminar sufficient theorem

The preceding obstruction disappears under an exact laminar pin audit.
Call a pin native when its label equals the union of the maximal controller
`P` on its interval.  Native pins introduce no negative deletion.  Let the
remaining exceptional pin intervals form a laminar forest, and require

\[
 J\subset I\quad\Longrightarrow\quad S_J\subseteq S_I. \tag{5.1}
\]

For an exceptional node `I`, let `ch(I)` be its maximal proper children and

\[
                         At(I)=I\setminus\bigcup_{J\in ch(I)}J.          \tag{5.2}
\]

At a position `p`, let `delta(p)` be the smallest exceptional interval
containing `p`, using label `[k]` if none exists, and put

\[
                         A_p=P_p\cap S_{\delta(p)}.       \tag{5.3}
\]

### Theorem 5.1 (laminar two-halo compiler)

The word (5.3) realizes the central row, every native pin, and every
exceptional boundary pin, and is nonzero, provided:

1. **atom condition:**
   \[
   S_I\setminus\bigcup_{J\in ch(I)}S_J
      \subseteq\bigcup_{p\in At(I)}P_p;                 \tag{5.4}
   \]
2. **controller port/gap condition:** in each maximal controller run of
   every coordinate, every forced internal endpoint survives and every
   connected deleted block has at most `d` positions;
3. **native trace survival:** every coordinate of every native pin has a
   surviving controller occurrence in that pin interval; and
4. **point core:** `P_p cap S_(delta(p))` is nonempty for every `p`.

#### Proof

Nested labels make (5.3) the maximal word compatible with all exceptional
negative requirements.  Induct upward in the laminar forest.  A coordinate
of `S_I` which lies in a child label is supplied by that child; otherwise
(5.4) supplies it on `At(I)`.  Thus every exceptional equality holds.

Native pins are negative-inert, and condition 3 preserves their positive
coordinates.  In a controller run, deleting a block of `s` consecutive
positions creates a gap of `s+1` between surviving occurrences.  The
central `d`-window equalities hold exactly when forced internal run endpoints
survive and all such gaps are at most `d+1`, which is condition 2.  Condition
4 gives nonzero letters.  `square`

This theorem turns Theorem 4.1 into a usable sufficient criterion: find the
rankwise Hall injections, choose their concrete halo cells so that the
selected exceptional intervals form a laminar, inclusion-monotone forest,
and check (5.4) plus the three coordinate tests.  All data live in the two
endpoint `d`-collars and the selected PBBS flag labels.  For `O(d^2)` seam
holes, the literal audit is polynomial in `k` and the selected atlas size.

There is also a standard package-flow formulation.  Precompute a family of
laminar flag packages and pairwise disjoint guarded halo slots.  Join a
package to a slot when its transplanted pins pass conditions 1--4 locally.
If

\[
                         |N(\mathcal G')|\ge|\mathcal G'|
                         \qquad(\mathcal G'\subseteq\mathcal G),         \tag{5.5}
\]

then integral max flow assigns distinct slots to all packages.  Disjoint
guards prevent deleted controller blocks from coalescing, so the union of
the local certificates satisfies Theorem 5.1.  This is a genuine Hall
theorem for a common compiler; its right vertices are physical slots, not
separate copies of the same halo.

## 6. Why the strongest automatic laminar theorem is false

### Proposition 6.1 (triangular laminar obstruction)

The statements

\[
 |H_q|\le2q\quad(1\le q\le d)
 \tag{6.1}
\]

and fixed-offset nesting do not imply that all seam holes have a laminar
realization in the two `d`-position halos.

#### Proof

One cut may lose `q` distinct targets at every depth `q`, for a total of

\[
                         1+2+\cdots+d=\frac{d(d+1)}2.    \tag{6.2}
\]

Distinct targets require distinct witness intervals.  A laminar family of
distinct nonempty intervals on a line of `d` points has at most `2d-1`
members: represent it as a rooted laminar forest; after adjoining singleton
leaves if necessary, every internal node has at least two children, so the
number of all nodes is at most twice the number of leaves minus one.
For `d>=3`,

\[
                         \frac{d(d+1)}2>2d-1.            \tag{6.3}
\]

Hence the maximal crossing triangle cannot be encoded by a laminar interval
family in one halo.  Fixed-offset target flags are nested separately, but
the union of the offset chains need not be laminar in physical source
intervals.  `square`

Thus Theorem 5.1 is a useful sufficient route when the actual hole family
is sparse or packageable; it is not a consequence of the PBBS count.
An unrestricted successful compiler may use crossing exceptional intervals,
as `COMP_d(T)` permits.

## 7. Exact PBBS boundary

PBBS supplies:

1. an occurrence-level, correct-rank lower flag for every target at every
   depth, with load between `1` and `binom(2q+1,q)`;
2. the explicit cyclic chronology, hence the two-cut crossing lists
   (3.1), their fixed-offset nesting, and the hole bound (3.2);
3. after a protected modification has been found, the endpoint collars on
   which (4.1) and the maximal-core tests can be evaluated; and
4. in the complement-projected fixed-matching factor used at `k=15`, a
   q1-rainbow deck.  This is an extra factor property, not a theorem about
   every raw PBBS `f^2` factor.

PBBS does not currently supply, uniformly in odd `k`:

1. an at-most-two-component factor which retains the all-depth tower and is
   `d(k)`-resident after opening;
2. an arbitrary-width upper-safe seam;
3. Hall expansion (4.2) of the **labelled** boundary neighborhoods;
4. a cross-depth choice passing the common maximal-core or laminar tests;
5. allocation of the preceding-row slack bank; or
6. the global compiler for the deep ideal `|S|<r-d`, whose targets are not
   made native merely by a PBBS occurrence at depth greater than `d`.

Therefore the strongest valid dimension-uniform statement is conditional:

> A protected two-boundary PBBS opening proves `nu(k)=B(k)` if it is
> linearly `d(k)`-resident and upper-complete, its seam holes admit the
> rankwise boundary Hall assignments together with one common maximal-core
> (or laminar-package) certificate, and the remaining preceding-row and
> deep-ideal targets admit the same `COMP_d(T)` solution.

The exact `k=15` certificate verifies this common solution literally.  It
does not turn any of the six missing uniform assertions into a PBBS theorem.
