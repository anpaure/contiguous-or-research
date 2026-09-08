# PBBS rethreading: residence stability, exact seam flags, and the owner gate

Date: 2026-07-28

Status: theorem-level synthesis and new local-surgery lemmas.  Every
unconditional assertion below is proved.  No PBBS Hamiltonization and no
coefficient-one theorem are claimed.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac{W}{n}=\operatorname {Cat}_m.
\]

The canonical PBBS odd-graph factor already carries the complete descending
flag tower at every depth.  Opening its at most `B` projected cycles and using
the dominance-staircase collars costs `O(HB)`, hence `o(W)` when
`H=O(sqrt(m))`.  Thus component topology is not the coefficient-one gate.

The useful new invariant is the following uniform surgery law.  If a
rethreading deletes `d` projected Johnson transitions, then, for every `H`,

\[
 \boxed{|\nu_H(P')-\nu_H(P)|\le d,\qquad
        |\tau_H(P')-\tau_H(P)|\le d,\qquad
        |J_H(P')-J_H(P)|\le d.}
 \tag{0.1}
\]

Consequently any `O(B)` local connector tree changes the critical PBBS
packing `nu_H` by only `O(B)`.  At `H=Theta(sqrt(m))` this is negligible on
the unresolved `B sqrt(m)` scale.  A Catalan-edit Hamiltonization can neither
prove nor refute the short-residence theorem unless that theorem is already
settled for the original PBBS factor.

There is a complementary positive statement.  Arbitrary `d=O(B)` seams need
not preserve the PBBS flag histogram: all destroyed canonical flags can be
restored by the existing one-cut charts at additional cost `O(Hd)=o(W)`.
Thus flag-neutral connectors are also unnecessary asymptotically.

For the exact finite formula, that extra word length is unavailable.  The
true connector conditions are then simultaneous:

1. a return transversal and safe residence collars;
2. literal paired-factor legality;
3. the exact all-depth coloured flag-load inequalities;
4. one common owner/Hall extension;
5. Hamilton monodromy, only if a Hamilton factor is desired.

The new hypersimplex completion theorem removes every *rankwise marginal*
version of item 3 whenever its sharp coordinate bounds
`0<=gamma_(q,x)<=e_q` hold; in particular they hold for the frozen `k=15`
depth-two and depth-three rows.  What remains there is precisely the
simultaneous chronological lift together with item 4.

## 1. Authoritative PBBS input

Let `f` be the canonical PBBS permutation of the `m`-sets and let `g=f^2`.
Along a directed `g`-cycle write `B_0,B_1,...`.  The all-depth corridor
theorem says that, for every `1<=q<=m` and every

\[
 S\in\binom{[n]}{m-q},
\]

there is a directed `q`-edge PBBS path with

\[
 \bigcap_{t=0}^q B_t=S,
\]

and its correct-rank load lies between `1` and
`binom(2q+1,q)`.  This is Theorem 21.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, independently audited in
`MATH_AUDIT_PBBS_ALLQ_CORRIDOR_AND_FIXED_BAND_WORDS_20260726.md`.

The complement-antipodal reduction identifies these occurrences with the
odd-graph flags

\[
 F_i^{(q)}=\bigcap_{h=0}^{q-1}B_{i+h}
 =B_i\setminus
   \{z_{2i+1},z_{2i+3},\ldots,z_{2i+2q-3}\}.
 \tag{1.1}
\]

Hence upper universality is exactly the surjectivity of all rows of this one
descending flag tower, not a separate turn-colour problem.

There is a small strengthening of the corridor construction which is useful
for surgery.

### Lemma 1.1 (the canonical witness has no internal positive return)

For the canonical depth-`q` witness in Theorem 21.2, no coordinate inserted
at one of its transitions is deleted at a later transition of the same
`q`-edge path.

#### Proof

At transition `t`, the corridor proof deletes `C_(q-t-1)` and inserts
`A_t`.  A positive return inside the path would give

\[
 A_h=C_{q-t-1}\qquad\text{for some }0\le h<t\le q-1.
\]

Writing `j=q-t-1`, this gives `j+h<=q-2`.  Equation (21.12) in the PBBS
proof excludes `C_j=A_h` whenever `j+h<=q-1`.  The proposed return is
therefore impossible.  \(\square\)

This lemma does **not** say that all `2q` transition labels are distinct: a
deletion may reappear later as an insertion.  It says exactly what residence
requires, namely that an insertion is not deleted again inside the witness.

## 2. Residence intervals and rethreading

Let `P` be an oriented Johnson cycle factor on rank-`(m+1)` owners.  A
positive run of a coordinate is a maximal consecutive block of owners which
contain it.  Its residence length is the number of owners in the block.  As
in the PBBS reduction, attach to the run the transition interval consisting
of its insertion edge, all internal edges, and its removal edge.  Let
`I_H(P)` be the family of these intervals whose residence length is at most
`H`.  In the exceptional case that a coordinate occupies a whole factor
cycle, its interval support is defined to be the whole edge set of that
cycle.  (Canonical PBBS runs are proper, but this convention makes the
general surgery statement closed.)

Write

\[
 \nu_H(P)=\nu(\mathcal I_H(P)),\qquad
 \tau_H(P)=\tau(\mathcal I_H(P)),
\]

for its edge-disjoint packing and transition-edge transversal numbers.
Let `J_H(P)` be the minimum number of cuts which both opens every cycle and
meets every interval in `I_H(P)`.

Suppose `P'` is obtained from `P` by cutting transition edges and rejoining
the resulting oriented path pieces.  Put

\[
 D_-=E(P)\setminus E(P'),\qquad
 D_+=E(P')\setminus E(P),\qquad
 |D_-|=|D_+|=d.
 \tag{2.1}
\]

Here `E(P)` means the **undirected projected Johnson-edge support**.  A
residence interval is decorated by its coordinate and is compared through
its undirected edge support; reversing it gives the same decorated interval.
The path pieces may be retained with either orientation, since coordinate
membership, run length, and this underlying transition interval are
unchanged by reversal.

If a surgery is presented as `J` old **projected** cuts followed by `J`
reconnections,
some nominal cuts may cancel because an old transition is reinserted.  In
that notation `d<=J`.  The intrinsic parameter in (2.1) is therefore at
most the physical seam count requested in a connector construction.

### Theorem 2.1 (exact common/boundary decomposition)

There is a common internal family `I_H^0` such that

\[
 \mathcal I_H(P)=\mathcal I_H^0\mathbin{\dot\cup}\mathcal B_-,
 \qquad
 \mathcal I_H(P')=\mathcal I_H^0\mathbin{\dot\cup}\mathcal B_+,
 \tag{2.2}
\]

where every member of `B_-` meets `D_-` and every member of `B_+` meets
`D_+`.

#### Proof

Delete the changed transitions.  The common retained graph is a disjoint
union of paths and unchanged cycles.  A proper residence interval of `P`
which avoids `D_-` contains its insertion and removal edges and hence lies
wholly inside one retained component.  The same coordinate block, with the
same two boundary edges and the same length, occurs in `P'`; if the component
was reversed, only its orientation changes.  A whole-cycle interval which
avoids `D_-` lies on an unchanged common cycle and is likewise unchanged.
The converse is symmetric.  Thus the intervals avoiding the changed
transitions are exactly the common family, and every remaining interval
meets the appropriate changed set.
\(\square\)

### Theorem 2.2 (uniform edit-Lipschitz laws)

For every `H>=1`, equation (0.1) holds.

#### Proof

An edge-disjoint packing contains at most `d` members of `B_-`: assign to
each such member one edge of `D_-` which it contains.  Disjoint intervals
receive distinct edges.  Therefore

\[
 \nu(\mathcal I_H^0)
 \le \nu_H(P)
 \le \nu(\mathcal I_H^0)+d,
\]

and the same inequalities hold for `P'`.  This proves the packing bound.

For transversals, retain the common edges of a minimum transversal for `P`
and add all of `D_+`.  The retained edges hit `I_H^0`, while `D_+` hits every
member of `B_+`.  Hence

\[
 \tau_H(P')\le\tau_H(P)+d.
\]

Interchanging `P,P'` gives the reverse inequality.

For `J_H`, start with an optimal old cut set, retain its common edges, and
add `D_+`.  Every changed new cycle contains an inserted transition, while
an unchanged cycle retains an old cut.  The resulting paths have no short
internal positive run.  Thus `J_H(P')<=J_H(P)+d`, and symmetry finishes the
proof.  \(\square\)

No separation assumption occurs in this proof.  An interval may cross two
or more seams; it still belongs to `B_-` or `B_+` and contains at least one
changed edge.  In a disjoint packing, two such intervals cannot be charged
to the same changed edge.  Likewise, reversal of a retained segment changes
only the order of a common coordinate block: its two absent/present boundary
edges and its edge set remain the same.  Thus for a `J`-seam surgery the
sharp form requested here is

\[
 \boxed{|\nu_H(P')-\nu_H(P)|\le d\le J,}
 \tag{2.2a}
\]

uniformly in `H`, with no hidden factor two or factor `H`.  If instead `J`
counts cuts of the underlying odd-graph `f`-factor, one such edge can border
two step-two projected transitions, and only the converted bound `d<=2J` is
automatic.  The paired matching `C_6/C_8` switches below are already counted
in projected slots.

### Corollary 2.3 (local connector ceiling)

A legal paired alternating circuit with `r` changed matching slots deletes
at most `r` projected Johnson transitions.  Hence a deck with `s_6`
hexagons and `s_8` octagons satisfies

\[
 d\le3s_6+4s_8.
 \tag{2.3}
\]

If the rethreaded factor has no residence interval of length at most `H`,
then necessarily

\[
 3s_6+4s_8\ge d\ge\tau_H(P)\ge\nu_H(P).
 \tag{2.4}
\]

#### Proof

Changing one matching slot changes at most the one projected successor
transition incident with that slot.  If `P'` is `H`-resident, every old
short interval must meet `D_-` by Theorem 2.1, so `D_-` is a transversal.
This proves (2.4).  \(\square\)

The topology-minimal loose `C_6` forest which joins `c` components uses at
most `(c-1)/2` hexagons, with at most one four-slot parity bridge.  Since
`c<=B`, it supplies at most

\[
 \frac{3}{2}B+4
 \tag{2.5}
\]

deleted transitions.  Therefore such a merge architecture cannot make the
factor `H`-resident unless the unresolved return transversal is already
Catalan-scale.

### Corollary 2.4 (critical packing is invariant under Catalan edits)

Let `H=ceil(A sqrt(m))`, with `A` fixed, and let `d=O_A(B)`.  Then

\[
 \frac{\nu_H(P')-\nu_H(P)}{B\sqrt m}=o_A(1).
 \tag{2.6}
\]

In particular both properties

\[
 \nu_H=O_A(B),\qquad
 \nu_H=o_A(B\sqrt m)
 \tag{2.7}
\]

are invariant under such rethreadings.

This is the rigorous obstruction to using a GMN-style `O(B)` merge tree as
a residence proof.  Connectivity can change completely while the normalized
critical return packing changes by `o(1)`.

## 3. Arbitrary Catalan seams are asymptotically repairable

The preceding obstruction does not mean that connectors damage the
coefficient-one construction.  Their flag damage is cheap in the literal
word model.

### Theorem 3.1 (canonical-support repair after arbitrary rethreading)

Let `P=P_m` be the complement-projected PBBS factor and let `P'` be any
`d`-transition rethreading of its path pieces.  For `2H<=m+1`, there is a
literal nonzero word covering every intended lower and upper target through
depth `H`, of length at most

\[
 \boxed{
 L_H(P')\le W+(5H-1)\bigl(J_H(P)+d\bigr).}
 \tag{3.1}
\]

No residence or flag-neutrality condition is imposed on the inserted
seams.

#### Proof

Before surgery, fix one correct-rank corridor witness from Theorem 21.2 for
each lower target, together with the corresponding complementary upper
witness.  This selection is necessary: Theorem 21.2 asserts the existence
of a correct witness, not that every PBBS window is floor-correct.

Let `C` be an optimal old cut set of size `J_H(P)`.  Cut `P'` at

\[
 (C\cap E(P'))\cup D_+.
\]

Equivalently, up to independent reversal, the retained pieces are the old
PBBS paths obtained by cutting `P` at \(C\cup D_-\).  There are at most
`J_H(P)+d` pieces.  They have no short internal positive run, since `C` met
every old short interval.  Reversal does not change an intersection or union
of the vertices of an internal window.

Endpoint-capped erosion costs one letter per retained owner plus `H` letters
per path.  It exposes every selected witness lying wholly inside a piece.
Every destroyed selected witness crosses a member of \(C\cup D_-\); assign
it to any such old cut.  The linear dominance-staircase theorem supplies, at
each old cut, all floor-correct crossing lower intersections and all
crossing upper unions through depth `H` in exactly `4H-1` letters.  The
selected lower witnesses are correct-rank, so these charts restore every
destroyed selected target.  Charts are needed at the distinct old cuts in
\(C\cup D_-\), at most `J_H(P)+d`; no chart is needed at `D_+`, since those
new seams are themselves cut away.
Adding the erosion and chart charges gives

\[
 W+H(J_H(P)+d)+(4H-1)(J_H(P)+d),
\]

which is (3.1).  Nonemptiness follows from `2H<=m+1`, exactly as in the
dominance-staircase theorem.  \(\square\)

### Corollary 3.2 (flag neutrality is not an asymptotic gate)

If `d<=K_A B` and `H=ceil(A sqrt(m))`, the extra cost caused by the
rethreading is

\[
 (5H-1)d=O_A(HB)=O_A(W/\sqrt m)=o_A(W).
 \tag{3.2}
\]

Thus, conditional on the canonical short-residence estimate needed in
equation (24.7), arbitrary Catalan-many connectors preserve coefficient
one.  Conversely, Theorem 2.2 shows that they cannot establish that estimate
if it fails at critical order.

This separates the two notions which were previously conflated:

* opening or merging components is topologically and asymptotically cheap;
* improving the return packing is a different problem and is edit-Lipschitz.

## 4. Exact flag debt of a cut set

For an exact finite construction, the repair in Section 3 consumes palette
length and cannot simply be appended.  The precise occurrence debt is still
elementary.

In this section retain the orientation of every path piece; alternatively,
identify occurrences only by their unoriented intersection/union window.
Reversal preserves target sets but not a based directed provenance cell.
Index transition slots cyclically on each old component.  For a deleted set
`D` define

\[
 \partial_qD
 =\{i:\{i,i+1,\ldots,i+q-1\}\cap D\ne\varnothing\}.
 \tag{4.1}
\]

Thus \(\partial_qD\) is the set of starts of old `q`-edge windows destroyed by
the surgery.

### Lemma 4.1 (all-depth flag-occurrence debt)

The number of destroyed old depth-`q` occurrences is exactly
\(\lvert\partial_qD\rvert\).  If `D` consists of `d` transition edges in `b` nonempty
cyclic blocks, and every gap between blocks contains at least `H` undeleted
edges, then, for every `1<=q<=H`,

\[
 |\partial_qD|=d+b(q-1).
 \tag{4.2}
\]

Consequently

\[
 \boxed{
 \Phi_H(D):=\sum_{q=1}^H|\partial_qD|
 =Hd+\frac{bH(H-1)}2.}
 \tag{4.3}
\]

#### Proof

A `q`-edge window survives precisely when none of its `q` transition slots
is deleted, proving the first assertion.  Expanding one deleted block
backwards by `q-1` start positions adds exactly `q-1` positions.  The gap
hypothesis prevents the expansions of distinct blocks from meeting for
`q<=H`.  Hence each of the `b` blocks contributes its own `q-1` boundary
positions, proving (4.2).  Summation gives (4.3).  \(\square\)

The distinction between occurrences and targets is essential.  A target
with another unaffected PBBS occurrence is not lost, and an unused destroyed
occurrence creates no owner debt.  Formula (4.3) is exactly the **raw
destroyed-occurrence count**, not by itself a lower bound on missing targets
or Hall deficiency.  It becomes labelled provenance debt only after one
fixes selected occurrence cells.  It also shows that clustering cuts, rather
than merely reducing the component count, is the geometry which reduces the
raw boundary count.

Combining Theorems 2.2 and 4.1 gives a sharp local trade-off at the raw
occurrence level: one deleted transition can reduce the packed-return number
by at most one, while it destroys `H` old occurrences across the first `H`
depths even before the block-boundary term is charged.  Whether those losses
become actual target or owner debt depends on multiplicity and the selected
owner matching.  Any architecture using them as selected unique
provenances must recycle them collectively.

## 5. Literal paired-factor rethreading

The exact local connector can be written without any appeal to the lexical
Hamiltonization.

Let

\[
 \mathcal X=\binom{[n]}m,\qquad U_Z=Z^c.
\]

The canonical PBBS paired matchings are

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z).
 \tag{5.1}
\]

Fix a finite support \(S\subset\mathcal X\) and a permutation `pi` of `S`
with no fixed point.  Extend `pi` by the identity on
\(\mathcal X\setminus S\).  Send donor `Z` to receiver `pi Z` by defining

\[
 M_1'(U_{\pi Z})=f(Z),\qquad M_0'=M_0,
 \tag{5.2}
\]

and leave all other matching edges unchanged.

### Lemma 5.1 (exact legality and monodromy)

The rethreading (5.2) is a literal pair of edge-disjoint perfect incidence
matchings if and only if, for every `Z in S`,

\[
 f(Z)\cap\pi Z=\varnothing,
 \qquad \pi Z\ne f^2(Z).
 \tag{5.3}
\]

Since `pi` has no fixed point, this is the usual PBBS exchange condition
`pi Z notin {Z,f^2Z}`.  If

\[
 \sigma=M_1^{-1}M_0,
\]

then the new monodromy is

\[
 \boxed{\sigma'=\pi\sigma.}
 \tag{5.4}
\]

In particular the rethreaded paired factor is Hamiltonian exactly when
`pi sigma` is one cycle.

#### Proof

The new matching edge at receiver `X=pi Z` is incident precisely when
`f(Z) subset X^c`, which is the first condition in (5.3).  It coincides
with the fixed edge `M_0(U_X)=f^{-1}(X)` precisely when
`f(Z)=f^{-1}(X)`, equivalently `X=f^2(Z)`.  Because `pi` is bijective, every
donor and receiver is used once, so these local conditions are also
sufficient for two perfect edge-disjoint matchings.

On upper vertices, (5.2) says `M_1'=M_1 pi^{-1}`.  Therefore

\[
 (M_1')^{-1}M_0=\pi M_1^{-1}M_0=\pi\sigma.
\]

Alternating components are exactly monodromy cycles, proving the last
assertion.  \(\square\)

The new crossing Johnson edge is literally

\[
 f(Z)\longrightarrow f^{-1}(X),\qquad X=\pi Z.
 \tag{5.5}
\]

The legality conditions ensure that these are distinct `m`-subsets of
`X^c`.

## 6. Exact all-depth seam ledger

Assume now that the old cut edges indexed by `S` are `H`-separated: every
old window of at most `H` projected transitions meets at most one of them.
For `1<=q<=H` and `0<=u<q`, define

\[
\begin{aligned}
 \Lambda^-_{q,u}(Z,X)
  &=\bigcap\bigl(
       f^{2u+1}Z,f^{2u-1}Z,\ldots,fZ,
       f^{-1}X,f^{-3}X,\ldots,f^{-(2(q-u)-1)}X
     \bigr),\\
 \Lambda^+_{q,u}(Z,X)
  &=\bigcup\bigl(
       f^{2u+1}Z,f^{2u-1}Z,\ldots,fZ,
       f^{-1}X,f^{-3}X,\ldots,f^{-(2(q-u)-1)}X
     \bigr).
\end{aligned}
 \tag{6.1}
\]

Each list has exactly `q+1` projected Johnson vertices.  The case `X=Z`
is the old canonical crossing window; `X=pi Z` is the new one.

All load vectors in this section are histograms on the full power set
\(2^{[n]}\), not only on the intended rank.  This is necessary because a
new seam can produce an intersection or union of the wrong cardinality.
For a set `T`, let `e_T` denote its unit load vector.  Define

\[
 R_{q,S}^{\pm}
   =\sum_{Z\in S}\sum_{u=0}^{q-1}
       e_{\Lambda^{\pm}_{q,u}(Z,Z)},
 \qquad
 A_{q,\pi}^{\pm}
   =\sum_{Z\in S}\sum_{u=0}^{q-1}
       e_{\Lambda^{\pm}_{q,u}(Z,\pi Z)}.
 \tag{6.2}
\]

### Theorem 6.1 (exact coloured flag derivative)

For every `q<=H`, the lower-intersection and upper-union load vectors obey

\[
 \boxed{
 \mu_q^{\prime\,\pm}
 =\mu_q^{\pm}-R_{q,S}^{\pm}+A_{q,\pi}^{\pm}.}
 \tag{6.3}
\]

In particular exactly `q|S|` old occurrences are removed and exactly
`q|S|` new occurrences are inserted at depth `q`, with multiplicity, in the
full power-set histogram.  Some inserted occurrences may have the wrong
rank.

#### Proof

Every window avoiding the cut support lies in a retained PBBS path piece
and is unchanged.  By `H`-separation, a window of depth at most `H` crosses
at most one seam.  For a window having `u` old transitions before that seam,
its vertex list is exactly the list in (6.1), first with `X=Z` and then with
`X=pi Z`.  There are `q` choices of `u` at each seam.  Summing their deleted
and inserted unit loads gives (6.3).  \(\square\)

At depth one the upper ledger cancels automatically:

\[
 \Lambda^+_{1,0}(Z,X)=f(Z)\cup f^{-1}(X)=X^c.
 \tag{6.4}
\]

As `X=pi Z` permutes the receivers, `A^+_{1,pi}=R^+_{1,S}`.  This is the
exact upper-rainbow invariant of paired matching switches.  There is no
corresponding automatic cancellation at higher depth.

Because PBBS starts with complete all-depth support, exact support after the
rethreading is equivalent to the coloured inequalities, restricted to every
target `T` of the intended rank,

\[
 \boxed{
 \mu_q^{\pm}(T)-R_{q,S}^{\pm}(T)+A_{q,\pi}^{\pm}(T)\ge1}
 \tag{6.5}
\]

for every intended target `T` and every `q<=H`.  Ordinary matching Hall
conditions do not imply (6.5).

## 7. Exact residence collars and the decorated seam graph

Write an oriented Johnson chronology near one new seam as

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\},
\]

where the inserted seam is transition `i=0`, negative indices lie in the
retained left piece, and positive indices lie in the retained right piece.
Assume each retained piece has no internally bounded positive run of length
at most `H` and that between any two successive new seams there are at least
`H` retained transitions (equivalently their seam-transition distance is at
least `H+1`).  This stronger separation is what makes each short-run test a
single-seam predicate.

### Lemma 7.1 (complete all-`H` seam test)

The new chronology has no short positive run crossing this seam if and only
if all applicable inequalities

\[
\begin{aligned}
 b_{-u}&\ne a_0 &&(1\le u\le H),\\
 b_0&\ne a_v &&(1\le v\le H),\\
 b_{-u}&\ne a_v &&(u,v\ge1,\ u+v\le H)
\end{aligned}
 \tag{7.1}
\]

hold.

#### Proof

Depth-`H` residence for a transition word is exactly

\[
 b_i\ne a_{i+t}\qquad(1\le t\le H).
 \tag{7.2}
\]

A forbidden pair crossing the seam has one of three forms: its deletion is
the seam (`i=-u,t=u`), its insertion is the seam (`i=0,t=v`), or its
insertion is on the left and deletion on the right
(`i=-u,t=u+v`).  These are exactly the three lines of (7.1).  All other
pairs lie in one retained piece and are safe by hypothesis.  \(\square\)

### Theorem 7.2 (exact separated residence rethreading criterion)

Let `D_-` be a PBBS cut set satisfying the `H`-retained-transition
separation above and let `pi` be a legal donor to receiver permutation.  The
rethreaded factor is `H`-resident if and only if

1. `D_-` meets every member of `I_H(P_m)`; and
2. every new seam passes (7.1).

#### Proof

If an old short interval avoids `D_-`, Theorem 2.1 says that it survives,
so condition 1 is necessary.  Condition 2 is necessary by Lemma 7.1.

Conversely, condition 1 makes every retained path piece internally
`H`-resident.  Separation ensures that a new run of length at most `H` can
cross at most one new seam, and Lemma 7.1 excludes all such runs.  \(\square\)

For a fixed cut support `S`, form a bipartite graph with a donor copy and a
receiver copy of `S`.  Join donor `Z` to receiver `X` when the literal
conditions (5.3), the nontriviality condition `X!=Z`, and the seam
inequalities (7.1) hold.  The following distinction is exact.

### Corollary 7.3 (three independent completion tests)

A residence-safe exact middle-factor rethreading on `S` exists if and only
if the decorated donor/receiver graph has a perfect matching, equivalently

\[
 |N(Y)|\ge|Y|\qquad(Y\subseteq S),
 \tag{7.3}
\]

provided `S` is already a transversal and has the stronger separation in
Theorem 7.2.  For a selected perfect matching `pi`:

* Hamiltonicity is the additional condition that `pi sigma` is one cycle;
* all-depth target preservation is the additional family (6.5).

Neither additional condition follows from (7.3).

This is the exact local connector interface.  A `C_6/C_8` library imposes
the further restriction that the matching permutation decompose into
cycles of lengths three and four; ordinary Hall does not imply that either.

## 8. The actual owner-Hall condition

The Hall condition in Corollary 7.3 completes the *middle paired factor*.
It must not be confused with the stronger owner assignment in the literal
compiler.

Fix a compiler matching `M` which saturates a specified target domain
`T_0`.  (For a full compiler, `T_0` is the whole target set.)  For a surgery
with deleted set `D`, let \(A_D\subseteq T_0\) be the targets whose selected cell
is no longer present or legal after surgery.  For occurrence/provenance-
labelled cells in an orientation-preserving surgery, these are exactly the
selected starts lying in \(\partial_qD\); for coarser owner cells they are
only a subset, because a crossing target can be recreated at the same owner.
Freeze the assignments of all targets in \(T_0\setminus A_D\), and let `R_0` be
the owner cells occupied by those frozen assignments.  Let `G'` be the
post-surgery target-to-cell incidence graph.

### Lemma 8.1 (frozen-outside owner extension)

The matching of the same domain `T_0` is restored after the surgery while
fixing every unaffected assignment if and only if

\[
 \boxed{
 |N_{G'}(Y)\setminus R_0|\ge|Y|
 \qquad\text{for every }Y\subseteq A_D.}
 \tag{8.1}
\]

#### Proof

After deleting the already occupied cells `R_0`, the only unmatched left
vertices are exactly `A_D`.  A matching saturating them exists if and only
if Hall's inequalities (8.1) hold.  Adjoining it to the frozen matching is
the desired extension.  \(\square\)

This criterion is conditional on a selected old owner assignment and on
freezing its unaffected part.  It does not assert that PBBS already has the
exact finite compiler, and it is not necessary for an unrestricted new
matching which is allowed to reroute formerly unaffected targets.  If a
partial matching is to be enlarged to new targets, those new demands must
also be included on the left side of (8.1).  The lemma isolates a useful
composable extension test; it is not an absolute owner-existence theorem.

## 9. A composable local score

Let `U_1,...,U_s` be pairwise edge-disjoint collars which are `H`-closed for
both the old and new factors: every `H`-short interval meeting `U_j` is
wholly contained in `U_j`.  Suppose a surgery changes the factor only inside
their union.  Put

\[
 \gamma_H(U_j)=
 \nu(\mathcal I_H(P)|_{U_j})-
 \nu(\mathcal I_H(P')|_{U_j}).
 \tag{9.1}
\]

### Lemma 9.1 (additivity on `H`-closed collars)

Under these hypotheses,

\[
 \boxed{
 \nu_H(P)-\nu_H(P')=\sum_{j=1}^s\gamma_H(U_j).}
 \tag{9.2}
\]

#### Proof

The short-interval hypergraph is the disjoint union of the unchanged
outside hypergraph and the restrictions to the edge-disjoint closed
collars.  Matching number is additive on a disjoint union.  Subtract the
two decompositions.  \(\square\)

Thus a useful local connector must have positive `gamma_H`, pass the seam
test (7.1), satisfy the coloured flag inequalities or admit the repair of
Section 3, and pass the relevant owner Hall test.  A component-merging score
alone has no bearing on (9.2).  The `H`-closed hypothesis is strong: no old
or new short interval may cross a collar boundary, and no existing atlas is
asserted here to supply such collars.

## 10. Reconciliation with hypersimplex completion

`MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md`
proves that whenever

\[
 0\le\gamma_{q,x}\le e_q,
\]

the forced depth-`q` excess-degree vector is a sum of `e_q` uniform blocks.
One copy of every target plus those blocks is therefore a hole-free multiset
with exactly the actual trace point degrees, and symmetric two-block
exchanges connect all such rankwise realizations.

For the frozen `k=15` Hall-29 carrier, the depth-two coordinates lie in

\[
 [568,574]\subset[0,1428],
\]

and the depth-three coordinates lie in

\[
 [1138,1147]\subset[0,3429].
\]

Therefore no scalar capacity, point-degree vector, or rankwise exchange
lattice can obstruct hole-free depth-two or depth-three rows.  Equations
(6.3)--(6.5) must be read as a *simultaneous chronological lift* problem:
one donor permutation/deletion word must realize compatible exchanges at all
depths, preserve residence, and admit one joint owner matching.  In the
special frozen-outside situation this last condition is (8.1).  Proving
another independent rankwise balancing lemma would not advance this gate.

## 11. Sharp proved/conditional boundary

The following statements are unconditional.

1. PBBS supplies every all-depth target with load at most
   `binom(2q+1,q)`.
2. Its at most `B` components cost only `O(HB)` to open and collar.
3. The return packing, transversal, and rotor cut number are all
   `1`-Lipschitz per deleted projected transition.
4. Any `O(B)` local Hamiltonization changes the normalized critical
   residence packing by `o(1)`.
5. The incremental literal repair cost of any `O(B)` seam set is
   asymptotically negligible; the unresolved baseline `J_H(P_m)` term
   remains.
6. For separated paired-factor rethreadings, legality, residence, all-depth
   loads, and monodromy are exactly the independent tests (5.3),
   (7.1)--(7.3), (6.5), and (5.4).  Equation (8.1) is exact for the stated
   frozen-outside owner-extension problem.
7. Whenever `0<=gamma_(q,x)<=e_q`, rankwise marginal completion is solved by
   the hypersimplex theorem; these bounds are verified for the frozen
   `k=15` depth-two and depth-three rows.

What is not proved is equally sharp.

* No existing PBBS `C_6/C_8` atlas is known to hit a critical short-return
  transversal while passing the decorated seam graph.
* No known atlas satisfies the simultaneous coloured constraints (6.5) and
  an unrestricted joint owner Hall condition.  Equation (8.1) applies only
  to a frozen-outside extension of an existing assignment.
* Published GMN/MNW Hamiltonization starts from the lexical factor, not the
  PBBS factor, and supplies none of these missing verifications.

For asymptotic coefficient one, the surviving theorem remains

\[
 \boxed{
 \nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(B\sqrt m)
 \quad\text{for every fixed }A>0,}
 \tag{11.1}
\]

or an alternative nonlocal surgery which deletes more than Catalan-many
projected transitions while keeping its actual target/owner repair cost
below `o(W)`.  The raw occurrence count (4.3) is a warning, not by itself a
lower bound on that repair cost.
Theorem 2.2 rules out obtaining that vanishing factor from a Catalan-edit
merge tree.

For the exact finite formula, the remaining theorem is a simultaneous
hypersimplex lift: construct one legal deletion/insertion chronology whose
all-depth loads satisfy (6.5), whose residence collars satisfy (7.1), and
which admits one joint owner matching.  Equation (8.1) is a sufficient and
necessary formulation only when an old assignment is being preserved
outside the affected set; a Hall-29 construction with no old full assignment
must solve the unrestricted joint Hall problem instead.  Hamiltonicity is
useful only when achieved inside that stronger construction; by itself it is
not the gate.
