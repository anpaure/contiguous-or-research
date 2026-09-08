# All odd `k`: PBBS--Markov reduction, exact safe-opening atlas, and the full boundary compiler

Date: 2026-07-29

Status: unconditional reduction theorem, exact compiler theorem, and audited
calibration at `k=11,13,15`.  The architecture-free flat-middle gate is stated
separately from the stronger PBBS/protected wrapper.  The resulting all-odd
existence lemma is not proved uniformly.  No all-odd equality claim is made.

## 1. Parameters and the target

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r},
\]

and put

\[
 \Lambda=\sum_{j=1}^{r-1}\binom{k}{j},\qquad
 d=d(k)=\min\left\{e\ge0:eW+\binom{e+1}{2}\ge\Lambda\right\}.
\]

The proved monotone-deadline theorem gives

\[
 \nu(k)\ge B(k):=W+d.                                    \tag{1.1}
\]

We treat the nontrivial range `k>=3`; `k=1` is immediate.  Here
\(1\le d\le m=r-1\).  Indeed \(\Lambda=2^{2m}-1\), and
\(mW\ge\Lambda\): this is direct for `m=1`, while
\(m\binom{2m+1}{m}/4^m>1\) at `m=2` and its successive ratio is
\((m+1)(2m+3)/(2m(m+2))>1\).

Thus an all-odd upper theorem only has to construct a word of length `W+d`.
The purpose of this note is to state exactly what the PBBS/Markov route must
produce in order to do so.

Throughout, `D` denotes adjacent union:

\[
 (DA)_i=A_i\cup A_{i+1}.
\]

Hence

\[
 (D^dA)_i=\bigcup_{p=i}^{i+d}A_p.                        \tag{1.2}
\]

## 2. The q1 factor fibre and its complete Markov basis

Let `Gamma_k` be the bipartite inclusion graph with shores

\[
 \mathcal L=\binom{[k]}{r-1},\qquad
 \mathcal U=\binom{[k]}r,
\]

and an edge `X--T` when \(X\subset T\).  The shores both have size `W`,
and `Gamma_k` is `r`-regular.

A spanning 2-factor `H` of `Gamma_k` contracts to a Johnson 2-factor on
\(\mathcal U\): a lower vertex `X` and its two incident upper neighbours become
one Johnson edge coloured `X`.  Conversely, every Johnson 2-factor using
each rank-`r-1` colour exactly once expands uniquely to such a bipartite
2-factor.  We call these **q1-exact factors**.

### Theorem 2.1 (alternating circuits are an algebraically complete Markov basis)

If `H` and `H'` are q1-exact factors, then \(H\triangle H'\) decomposes into
edge-disjoint even circuits whose edges alternate between \(H\setminus H'\)
and \(H'\setminus H\).  Toggling all these circuits changes `H` exactly into `H'` and
preserves degree two on both shores after every circuit toggle.

#### Proof

At every vertex,

\[
 \deg_{H\setminus H'}(v)=\deg_{H'\setminus H}(v),
\]

because both factors have degree two.  At each vertex, pair its old-only
incident edges bijectively with its new-only incident edges.  Start with an
unused old-only edge; at its next endpoint follow the paired new-only edge,
then at the next endpoint follow its paired old-only edge, and continue.
Finiteness and the local pairing close an alternating even trail.  Repeating
partitions the symmetric difference into edge-disjoint alternating closed
trails; a repeated vertex can be split at two equal-parity visits into
alternating circuits.  Every circuit uses equally many old and new incidences
at each visited vertex, so toggling it preserves degree two.  The union of
all toggles is the symmetric difference.  QED.

The Middle Levels Hamilton-cycle theorem supplies a connected spanning
2-factor of `Gamma_k`.  Thus connectivity is not an obstruction **inside the
unprotected q1-factor subproblem**: the q1 factor fibre contains a connected
factor, and the particular q1-exact PBBS two-matching factor audited in
Section 3 is algebraically connected to it by alternating circuits.  This
says nothing about whether the resulting middle ordering is upper-complete
or admits `COMP_d(T)`, and it is not a necessity statement for arbitrary
optimal words.  In particular, neither the target factor nor the
intermediate toggles are thereby known to preserve PBBS all-depth flags or
residence.

### Theorem 2.2 (transversal alternating-cycle merge)

Let `H` be a q1-exact factor and let `Z` be an `H`-alternating cycle of
length `2t`.  If the `t` selected edges of `Z` lie in `t` distinct components
of `H`, then toggling `Z` replaces those `t` components by one component and
leaves every other component unchanged.  Hence the component count drops by
exactly `t-1`.

#### Proof

Deleting one selected edge from each of the `t` factor cycles turns each of
them into one path.  The `t` unselected edges of `Z`, in their cyclic order,
join the terminal endpoint of each path to the initial endpoint of the next.
Their union is therefore one cycle through all `t` paths.  Nothing outside
those components changes.  QED.

There is no `t=2` instance.  Indeed, `Gamma_k` has no 4-cycle: if two
distinct rank-`r-1` sets `X,Y` were both contained in two rank-`r` sets, then
\(|X\cup Y|=r\) and the only possible common upper neighbour would be
\(X\cup Y\).  Thus a transversal alternating `C_6` is the first possible
automatic merge, and it merges three components at once.

This gives one sufficient protected-reduction target inside the PBBS wrapper:

> while a protected factor has at least three components, find a transversal
> alternating circuit whose toggled endpoint remains protected.

If such circuits remain available, iteration reaches one or two components.
Two components are a convenient stopping point: the automatic two-edge
merge is intrinsically absent, while Section 6 handles their at most two
deleted q1 cut colours.  Neither reduction to two components nor this q1
capacity is necessary or sufficient for `FMCC(m)`.

In a fixed-matching chart there is also an exact nontransversal criterion.
Write the old factor permutation as \(\sigma=M_0^{-1}P\), replace `P` by
\(P\pi\), and let \(\rho\) send each marked row to the next marked row on
its old `sigma`-cycle.  The cut--join identity is

\[
 c(\sigma\pi)=c(\sigma)-c(\rho)+c(\pi\rho).                \tag{2.1}
\]

Thus a protected switch is component-improving exactly when

\[
 c(\pi\rho)<c(\rho).                                      \tag{2.2}
\]

The proof cuts each touched old cycle at its marked rows; `rho` records the
old fragment successor and `pi rho` records the new one.  This criterion,
proved and independently replayed in
`MATH_THEOREM_L_PBBS_COMPONENT_REDUCTION_AND_BOUNDARY_CAPACITY_20260729.md`,
also covers circuits which visit one old component several times.  Theorem
2.2 is its clean transversal special case.

## 3. The protected PBBS face

We first discharge an external assumption which must not be hidden inside
the phrase “PBBS all-depth factor.”  Put

\[
 \mathcal X=\binom{[2m+1]}m,
 \qquad \mathcal U=\binom{[2m+1]}{m+1},
\]

and let `f` be the canonical PBBS permutation of \(\mathcal X\).  The source
used here is the **antipodal two-matching lift**

\[
 M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c.              \tag{3.1}
\]

It is not merely the assertion that some PBBS windows cover every shadow.

### Proposition 3.1 (the chosen PBBS source is q1-exact)

For every `m>=1`, the two maps in (3.1) are edge-disjoint perfect matchings
of the rank-`m`/rank-`m+1` inclusion graph.  Their union is a simple spanning
two-factor, and after suppressing the rank-`m` shore its Johnson factor on
\(\mathcal U\) uses every rank-`m` lower-q1 colour exactly once.

#### Proof

PBBS gives a permutation `f` with

\[
 A\cap f(A)=\varnothing,
 \qquad |f^{-1}(A)\cap f(A)|=m-1.                    \tag{3.2}
\]

Applying the first identity to `f^{-1}(A)` also gives
`A\cap f^{-1}(A)=\varnothing`, so both complements in (3.1) contain `A`.
The second identity follows from the audited fact that `f^2` is a Johnson
factor: substitute `C=f^{-1}(A)` into
`|C\cap f^2(C)|=m-1`.  Both sets in (3.1) have rank `m+1`, so they are
incidence neighbours.  Each map is a bijection, being a
composition of a permutation and complementation, and is therefore a
perfect matching.  Equation (3.2) also gives
`f^{-1}(A) != f(A)`, so their edges at `A` are distinct.

The two upper neighbours of `A` are thus distinct rank-`m+1` supersets of
the same rank-`m` set.  Their intersection is exactly `A`.  Suppressing
`A` consequently creates one Johnson edge with lower colour `A`.  There is
one such suppressed edge for every \(A\in\mathcal X\), proving exactness rather
than mere support.  This proof includes `m=1`; then (3.2) says the two PBBS
neighbours have empty intersection and are distinct.  QED.

This is independently the construction proved in
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`,
Theorems 1.1 and 2.1.  It also identifies the carrier used by the all-depth
theorem.  If `B_{i+1}=f^2(B_i)`, then its rank-`m+1` owner is

\[
 T_i=f(B_i)^c=B_i\cup B_{i+1},
 \qquad T_i\cap T_{i+1}=B_{i+1}.                    \tag{3.3}
\]

Thus the PBBS `q`-edge intersection witnesses lift to the same two-matching
factor, while complementation gives its upper witnesses.  The all-depth
audit supplies support at the deeper ranks; Proposition 3.1 separately
supplies multiplicity-one at lower q1.  Neither statement may be substituted
for the other.

There is a related convention trap.  The bare centered Johnson factor
`f^2` on rank `m` has every adjacent **union** colour exactly once and a
lower-intersection load between one and three.  It is the lift (3.1), or the
equivalent complemented carrier (3.3), that has the lower-q1 palette needed
by `Gamma_k` exactly once.

Call a q1-exact factor `G` **`d`-protected** when:

1. every cyclic positive coordinate run in every physical cycle has length
   at least `d+1`;
2. for every `q=1,...,r-1`, all rank-`r-q` targets occur as intersections of
   cyclic `(q+1)`-windows; and
3. for every possible upper rank, every target occurs as the union of a
   cyclic interval.  It is enough, but not necessary, to demand every
   geodesic fixed-width upper deck.

The audited PBBS chronology theorem supplies the all-depth flag tower at the
two-matching source.  It does **not** assert the growing `d`-residence
condition.  Alternating toggles preserve q1 exactness automatically, but they
do not automatically preserve conditions 1--3.  Define

\[
 \mathscr P_{m,d}=\{G:G\text{ is a `d`-protected q1-exact factor}\}. \tag{3.4}
\]

The exact protected component-reduction problem is

\[
 \boxed{\text{find }G\in\mathscr P_{m,d}\text{ with }c(G)\le2.}       \tag{3.5}
\]

Theorem 2.1 says that any endpoint in (3.5) is a simultaneous alternating
trade of the PBBS factor.  Requiring a path through \(\mathscr P_{m,d}\) after
every primitive toggle is a stronger property and is not needed for the
existence proof.

Equivalently, with the minimum of the empty set interpreted as infinity, the
component clause of endpoint-form UPMBC is exactly

\[
 c_{\rm prot}(m,d):=min_{G\in\mathscr P_{m,d}}c(G)\le2. \tag{3.6}
\]

The algebraic Markov theorem supplies PBBS reachability automatically once
such a q1-exact endpoint exists.  Protected-route theorems are sufficient
ways to prove (3.6), not extra necessities in its statement.

## 4. Exact two-component opening and its target kernels

Suppose \(G\in\mathscr P_{m,d}\) has one or two cycles.  Choose one cut and an
orientation in each cycle.  If there are two cycles, join their exposed ends
by one seam; a Johnson seam is sufficient and is the interface used in the
three audited calibrations.  Let

\[
 T=(T_0,\ldots,T_{W-1})                                  \tag{4.1}
\]

be the resulting ordering of every rank-`r` set exactly once.

We require:

* **linear residence:** every internal positive run of every coordinate in
  `T` has length at least `d+1`;
* **upper safety:** every target of rank greater than `r` is the union of a
  contiguous interval of `T`.

There is an exact finite safe-opening test.  For an upper target `Y` and a
source component `C`, let `W_C(Y)` be all directed occurrences
`(start,length)` of cyclic source intervals in `C` having union `Y`, with
length between one and the component length.  For an occurrence `I`, let
`E(I)` be its `length-1` traversed factor edges and put

\[
 K_C(Y)=\bigcap_{I\in W_C(Y)}E(I),                        \tag{4.2}
\]

with the convention that a component with no witness imposes no surviving
witness.  A cut destroys every source witness in `C` exactly when it lies in
`K_C(Y)`.

Let \(\mathcal A(G)\) be the finite atlas of oriented, residence-safe seams.
For \(a\in\mathcal A(G)\), let `B_Y` contain `a` exactly when

1. its selected cuts destroy every old witness for `Y` on every supporting
   component; and
2. no new suffix--seam--prefix interval has union `Y`.

### Theorem 4.1 (exact safe-opening criterion)

The atlas contains an upper-safe opening if and only if

\[
 \mathcal A(G)\setminus\bigcup_{|Y|>r}B_Y\ne\varnothing.  \tag{4.3}
\]

In particular, the proof-friendly inequality

\[
 \sum_{|Y|>r}|B_Y|<|\mathcal A(G)|                       \tag{4.4}
\]

is sufficient.

#### Proof

Every interval of the opened path either stays inside one opened component
or crosses the unique seam.  An internal source occurrence survives exactly
when its edge span avoids the cut; all occurrences are destroyed exactly by
(4.2).  Every new crossing interval is a suffix followed by the seam and a
prefix.  These two classes exhaust the final intervals, so `B_Y` is exactly
the set of atlas arcs missing `Y`.  Taking the complement proves (4.3), and
the union bound proves (4.4).  QED.

Thus a uniform PBBS safe-opening proof may be attacked by a hereditary
kernel-dispersion bound such as (4.4); component connectivity alone is not
enough.

Failure of (4.3) certifies only that the specified factor `G`, port atlas
`\mathcal A(G)`, and one/two-component opening scheme have no upper-safe
member.  It does not obstruct another factor, a different seam alphabet, a
multi-component opening, or an arbitrary upper-complete middle permutation.

### Corollary 4.2 (edge-disjoint witness reserve)

If the factor has `c<=2` components and every upper target has at least
`c+1` pairwise edge-disjoint cyclic witness intervals, then every choice of
one cut per component preserves upper completeness, before using any new
seam witness.

#### Proof

The `c` selected cut edges meet at most `c` members of an edge-disjoint
witness family, so at least one witness survives.  QED.

This is a strong sufficient hypothesis, not a property currently proved for
PBBS.  The calibrated factors have some low-multiplicity targets and use the
sharper kernel/seam criterion instead.

### Lemma 4.3 (componentwise fixed-depth kernel dispersion)

Let `q>=1` and let `C` be a directed cycle of length greater than `2q`.  For a fixed-depth
target `Y`, let \(\mu_C^q(Y)=t\) be the number of based cyclic `q`-edge
windows with trace `Y`, and let \(K_C^q(Y)\) be the intersection of their
edge spans.
If `t>=1`, then

\[
 |K_C^q(Y)|\le \max\{q-t+1,0\}.                         \tag{4.5}
\]

Consequently, if \(a_{C,t}\) counts the targets with exactly `t` such
occurrences, then

\[
 \sum_{Y:\,\mu_C^q(Y)\ge1} |K_C^q(Y)|
 \le \sum_{t=1}^{q}(q+1-t)a_{C,t}.                      \tag{4.6}
\]

#### Proof

If the kernel is nonempty, cut the cycle at one common kernel edge.  A
`q`-edge window containing that edge has one of `q` consecutive start
positions.  The `t` distinct based windows have start span at least `t-1`,
and the intersection of their edge intervals has length at most
`q-(t-1)`.  If `t>q`, no common edge exists.  Summing by multiplicity gives
(4.6).  QED.

For two source cycles of lengths `L_0,L_1`, define

\[
 \kappa_i(Y)=
 \begin{cases}
 |K_{C_i}^q(Y)|,&C_i\text{ supports }Y,\\
 L_i,&C_i\text{ does not support }Y.
 \end{cases}
\]

Exactly \(\kappa_0(Y)\kappa_1(Y)\) cut pairs destroy all old depth-`q` witnesses
of `Y`.  Hence a union bound over depths and targets gives a cut pair that
destroys no fixed-width protected target whenever

\[
 \sum_{q,Y}\kappa_0(Y)\kappa_1(Y)<L_0L_1.              \tag{4.7}
\]

This is only the unfiltered cut census.  Residence, orientation, and seam
legality may restrict the admissible port atlas; on that atlas the exact
quantity is the number of admissible bad pairs, not the product above.
PBBS supplies at least one canonical window and therefore a kernel of size
at most `q` on a supporting component, but no audited PBBS theorem controls
the componentwise multiplicities \(a_{C,t}\) strongly enough to prove (4.7).
That missing component-dispersion estimate is a precise fixed-width UPMBC
subtarget.  The exact variable-width opening gate remains (4.3), and the
product census must still be intersected with the admissible residence/seam
port atlas.

### Theorem 4.4 (exact one-seam restoration and the common-core obstruction)

Fix the cuts and orientations of two components, writing the first opened
path as `Q_0` and the second as `Q_1`.  Let `Y` be an upper target whose old
cyclic witnesses are all killed by the cuts.  Define `S_0(Y)` to be the
maximal terminal segment of `Q_0` all of whose middle sets are contained in
`Y`, taking it to be empty when the seam-adjacent terminal owner is not
contained in `Y`.  Define `S_1(Y)` analogously as the maximal initial segment
of `Q_1`, again allowing the empty segment.  Then the new seam restores `Y`
if and only if both segments are nonempty and

\[
 \bigcup_{T\in S_0(Y)\cup S_1(Y)}T=Y.                    \tag{4.8}
\]

#### Proof

Any new witness must cross the unique seam, so it is a terminal segment of
`Q_0` followed by an initial segment of `Q_1`.  If its union is `Y`, every
member is contained in `Y`, hence the witness lies inside the two maximal
segments.  Conversely, if (4.8) holds, concatenating the two maximal segments
is itself one crossing interval with union `Y`.  QED.

Let `A` and `B` be the two middle sets adjacent to the seam.  Every restored
killed target contains the seam core \(A\cup B\).  For a Johnson seam this
core has rank `r+1`.  Consequently, if the killed family \(\mathcal K\) is
nonempty, then

\[
 \left|\bigcap_{Y\in\mathcal K}Y\right|<r+1              \tag{4.9}
\]

is an intrinsic obstruction to repairing all of them with this fixed
one-Johnson-seam architecture.
Equations (4.2) and (4.8) together are a necessary-and-sufficient
cut-kernel/witness-atlas test, not merely a fixed-width proxy.

It is not an obstruction to different cuts, another factor, multiple seams,
non-Johnson transitions, or a middle permutation not obtained from a cycle
factor.

## 5. The exact full depth-`d` compiler

The compiler must not be restricted to the `DA=DP` one-core normal form.
The following Boolean system is necessary and sufficient for the actual
depth-`d` antecedent problem.

For a fixed path `T`, define its maximal erosion envelope

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,W-1)}T_i,
 \qquad 0\le p<W+d.                                      \tag{5.1}
\]

If `T` is linearly `d`-resident as required in Section 4, coordinatewise
erosion gives

\[
 D^dP=T.                                                   \tag{5.1a}
\]

Indeed, in one binary coordinate erosion shortens an internal positive run
by `d` at its left edge, and the following `d` adjacent unions restore that
edge.  A non-endpoint-truncated run survives exactly when its length is at
least `d+1`; endpoint-truncated runs are restored by the clipped extreme
source cell.  Thus the linear residence condition in Section 4 is precisely
what is needed for (5.1a).

Use bits `a_(p,x)` and interpret

\[
 A_p=\{x:a_{p,x}=1\}.                                    \tag{5.2}
\]

Impose

\[
 a_{p,x}=0\quad(x\notin P_p),                            \tag{5.3}
\]

\[
 \sum_{x=1}^k a_{p,x}\ge1,                              \tag{5.4}
\]

and, for every `i` and every `x in T_i`,

\[
 \sum_{p=i}^{i+d}a_{p,x}\ge1.                            \tag{5.5}
\]

Let \(\mathcal I_d\) be all source intervals of one through `d` letters.
For every nonempty \(S\subset[k]\) with `|S|<r`, introduce **binary** witness
variables `z_(S,I)` for \(I\in\mathcal I_d\) and impose

\[
 \sum_{I\in\mathcal I_d}z_{S,I}\ge1,                    \tag{5.6}
\]

\[
 \sum_{p\in I}a_{p,x}\ge z_{S,I}\quad(x\in S),          \tag{5.7}
\]

\[
 a_{p,x}\le1-z_{S,I}\quad(p\in I,\ x\notin S).         \tag{5.8}
\]

Call (5.3)--(5.8) `COMP_d(T)`.

### Theorem 5.1 (exact compiler equivalence)

`COMP_d(T)` is feasible if and only if there is a word `A` of length `W+d`
such that every letter is nonempty,

\[
 D^dA=T                                                   \tag{5.9}
\]

and every target of rank below `r` is a contiguous union in `A`.

#### Proof

If (5.3)--(5.5) hold, (5.3) excludes `x` from every `(d+1)`-window whose
corresponding `T_i` omits it, while (5.5) includes every `x in T_i` somewhere
in that window.  Hence (1.2) equals `T_i` coordinatewise.  Equations
(5.6)--(5.8) say exactly that some interval of `A` has union `S`.

Conversely, any antecedent of `T` is pointwise contained in (5.1), since a
source position participates in precisely the displayed middle windows.
Equation (5.9) gives (5.5).  Any interval of at least `d+1` source letters
contains a full `(d+1)`-window, whose union is a rank-`r` member of `T`.
Therefore a target of rank below `r` can only use an interval of at most `d`
letters, yielding a variable satisfying (5.6)--(5.8).  QED.

### Corollary 5.2 (upper-safe path plus compiler proves equality)

If `T` is upper-safe and `COMP_d(T)` is feasible, then

\[
 \nu(k)=W+d=B(k).                                        \tag{5.10}
\]

#### Proof

Lower targets are supplied by Theorem 5.1, and `T_i` itself is the union of
`A_i,...,A_(i+d)`.  If an upper target is

\[
 Y=T_i\cup\cdots\cup T_j,
\]

then

\[
 Y=A_i\cup\cdots\cup A_{j+d}.                            \tag{5.11}
\]

Thus `A` covers every nonempty target in length `W+d`; combine with (1.1).
QED.

## 6. Two-ended q1 absorption

Opening `c<=2` q1-exact cycles deletes at most two distinct lower-q1 colours.
Require the joining seam, when present, to be Johnson.  Let `R_cut` be the
set of deleted cut colours and let `R_int(T)` be the set of rank-`r-1`
intersections on the final path.  Define directly

\[
 Q(T)=R_{\rm cut}\setminus R_{\rm int}(T).                \tag{6.1}
\]

Thus the seam may restore one deleted colour or may be foreign.  In either
case

\[
 |Q(T)|\le2.                                              \tag{6.2}
\]

The first `d` and last `d` source positions form the two boundary halos.
Add to `COMP_d(T)` the requirement that the first missing cut colour, if any,
is realized by an interval wholly in the left halo, and the second by an
interval wholly in the right halo.

### Lemma 6.1 (derivative compatibility of the two cut-colour pins)

For a linearly `d`-resident q1-exact Johnson opening, each deleted cut colour
is individually compatible with its own halo.  In particular, setting the
extreme source letter equal to that cut colour and leaving all other letters
at their maximal erosion values still satisfies `D^dA=T`.

#### Proof

At the left end write the cut colour as

\[
 Q=T_0\setminus\{x\}.
\]

The retained first path edge has colour

\[
 R=T_0\cap T_1=P_1.
\]

The source q1 deck is squarefree, so `Q` and `R` are distinct facets of the
same rank-`r` set `T_0`.  Therefore \(Q\cup P_1=Q\cup R=T_0\).
Replacing `P_0=T_0` by `Q` consequently leaves the first `(d+1)`-window union
equal to `T_0`; the modified source position belongs to no other middle
window.  The right end uses the distinct deleted and retained facets of
`T_(W-1)` in reverse order.  QED.

This lemma proves only that each of the at most two deleted q1 cut colours is
individually derivative-compatible with its designated outer halo.  It does
**not** prove that the two pins and all other lower targets can be installed
simultaneously; that is exactly the remaining feasibility of the pinned
system `COMP_d(T)`.

### Lemma 6.2 (exact two-boundary q1 palette cap)

Let `T=D^dA` be a Johnson path through distinct rank-`r` vertices.  If a
rank-`r-1` target `S` is witnessed by a source interval which avoids the two
extreme source positions, then `S` is an internal Johnson colour of `T`.
If, in addition, `A` covers every rank-`r-1` target, then all such targets
missing from the internal palette number at most two: one may use the left
extreme and one may use the right extreme.

#### Proof

The witness has length at most `d`, because any longer interval contains a
full `(d+1)`-window of rank `r`.  Write it as `[u,v]`, with
`0<u<=v<W+d-1`.  The full `(d+1)`-windows which contain `[u,v]` have start
indices

\[
 [v-d,u]\cap[0,W-1].                                    \tag{6.3}
\]

There are at least two such starts: before clipping there are
`d-(v-u+1)+2>=2`, while avoidance of the two extreme source positions leaves
at least two after either boundary clipping.  Every corresponding middle set
contains `S`.  Two consecutive entries in this nontrivial block are distinct
rank-`r` Johnson neighbours containing the same rank-`r-1` set, so their
intersection is exactly `S`.

Under the additional coverage assumption, any missing target must therefore
use an extreme source position.  The unions of all left-extreme source
intervals form a nested family; two members of rank `r-1` are equal.  Thus
the left end supplies at most one missing target, and the right end supplies
at most one.  QED.

For a q1-exact `c`-component opening with a feasible full compiler, the `c`
deleted cut colours are distinct.  Lemma 6.2 implies that its seams must
restore at least `c-2` of them into the internal palette.  This does not make
more than two components impossible: a many-component opening can work when
its seams recycle enough cut colours.  Reducing to at most two components is
a clean sufficient normalization which makes this palette count automatic.

### Lemma 6.3 (off-diagonal diamond constraint)

A Johnson edge is uniquely determined by its lower and upper q1 labels.  In
particular, a genuinely new seam cannot reproduce both labels of the same
deleted edge.

#### Proof

If the labels are `L` of rank `r-1` and `U` of rank `r+1`, then
`U\setminus L={a,b}` and the unique edge is

\[
 \{L\cup\{a\},L\cup\{b\}\}.                            \tag{6.4}
\]

Thus equality of both labels forces equality of the unordered edge.  QED.

For `c` cuts and `c-1` Johnson seams, let `R^-` be the deleted lower labels
and `Q^-` the seam lower labels.  Feasibility of the unrestricted compiler
requires

\[
 |R^-\setminus Q^-|\le2.                                \tag{6.5}
\]

If the final path is upper-complete, every upper target whose last adjacent
witness was cut must occur among the seam upper labels `Q^+`.  Lemma 6.3
makes this a coupled off-diagonal diamond SDR rather than two independent
palette counts: a seam may recycle the lower
label of one cut and the last upper label of another, but cannot do both jobs
for the same cut unless it simply restores that old edge.  For `c=2`, the
two boundary cells provide capacity for both lower cut labels at q1, freeing
the unique seam to serve upper chronology; simultaneous absorption is still
subject to pinned full `COMP_d(T)` feasibility.  This is exactly the
nonrecycling `k=15` pattern.

At upper q1, “adjacent” loses no arbitrary-interval witnesses: if a
contiguous interval of distinct rank-`r` Johnson vertices has union `U` of
rank `r+1`, every member is an `r`-facet of `U`, and its first adjacent pair
already has union `U`.  Thus a last upper-q1 occurrence can be audited on the
edge palette.

The strict historical rule “the seam colour must equal a deleted cut colour”
is therefore unnecessary.  At `k=15` the winning seam is foreign and both
deleted colours use the two halos.

## 7. The architecture-free gate and the PBBS wrapper

The exact general target exposed by Section 5 does not mention PBBS,
components, protected circuits, or seams.

### Flat-middle carrier--compiler condition `FMCC(m)`

There is a linear ordering

\[
 T=(T_0,\ldots,T_{W-1})
\]

of all members of \(\binom{[2m+1]}{m+1}\), each exactly once, such that:

1. every target of rank greater than `m+1` is the union of a contiguous
   interval of `T`; and
2. the full Boolean system `COMP_d(T)` is feasible.

No Johnson adjacency or cyclic-factor provenance is included in this
condition.

### Theorem 7.1 (exact flat-middle reduction)

`FMCC(m)` implies

\[
 \nu(2m+1)=B(2m+1).                                      \tag{7.1}
\]

Moreover, among length-`W+d` universal words whose `d`th derivative is a
permutation of the middle layer, `FMCC(m)` is necessary and sufficient.

#### Proof

The forward implication is Corollary 5.2: `COMP_d(T)` supplies a nonempty
length-`W+d` antecedent covering every lower target, the entries of `T`
cover the middle layer, and upper completeness of `T` lifts through (5.11).
The lower bound (1.1) gives equality.

Conversely, suppose a universal word `A` of length `W+d` has
`T=D^dA` equal to a middle-layer permutation.  The word `A` itself certifies
`COMP_d(T)` by Theorem 5.1.  Let an upper target `Y` be witnessed by a source
interval `[a,b]`.  Every interval of at most `d+1` source letters is
contained in some full window `[i,i+d]`, where one may choose

\[
 i\in[\max(0,b-d),\min(a,W-1)].
\]

The interval of choices is nonempty because `b-a<=d` and
`0<=a<=b<=W+d-1`.  Thus an upper witness has more than `d+1` letters.  The
union of all full windows inside
the witnessing interval is exactly its source union, because its first and
last source letters occur in the first and last such windows.  Those full
windows form a contiguous interval of `T`, so they witness `Y`.  Hence `T`
is upper-complete and `FMCC(m)` holds.  QED.

The positive-slack deadline theorem does not force an arbitrary optimal word
into this flat-middle normal form.  Thus failure of `FMCC(m)` would refute
this normal form, not by itself refute equality.  For proving the upper
bound, however, existence of one `FMCC(m)` witness is the architecture-free
remaining construction gate.

The PBBS programme attacks `FMCC(m)` through the following stronger wrapper.

### Uniform PBBS--Markov boundary-compiler lemma `UPMBC(m)`

For `k=2m+1`, with `r,W,d` as in Section 1, there exist:

1. a factor \(G\in\mathscr P_{m,d}\) which is a simultaneous alternating-circuit
   transform of the canonical PBBS all-depth factor and has at most two
   physical components;
2. one cut/orientation per component and, when needed, one residence-safe
   seam, producing a linearly `d`-resident path `T` through all `W` middle
   sets;
3. an opening outside every upper forbidden set `B_Y` in (4.3); and
4. a feasible solution of `COMP_d(T)` in which the colours in `Q(T)` are
   realized in distinct outer halos.

Here “alternating-circuit transform” means algebraic reachability in the
q1-factor fibre.  The canonical PBBS source need not itself be `d`-protected,
and no protected primitive-by-primitive route is asserted.

### Theorem 7.2 (uniform PBBS implication)

If `UPMBC(m)` holds for every `m`, then

\[
 \nu(2m+1)=B(2m+1)\qquad\text{for every }m.               \tag{7.2}
\]

#### Proof

Items 1--3 produce an upper-safe middle path.  Item 4 and Theorem 5.1 produce
a length-`W+d` lower-complete antecedent.  Corollary 5.2 gives equality.  QED.

This is a precise sufficient uniform lemma for the PBBS/protected
architecture, and it implies `FMCC(m)`.  Its four clauses must be kept
simultaneous.  PBBS all-depth support alone does not control
residence; q1 Markov connectivity alone does not preserve the shadow tower;
component count alone does not give an upper-safe seam; and marginal Hall
alone does not imply the exact compiler clauses.

Accordingly, every negative statement about protected component reduction,
transversal `C_6` connectors, cut kernels, or the at-most-two-cycle opening
is architecture-specific.  Such a statement can refute a proposed proof of
`UPMBC(m)` but cannot rule out a different `FMCC(m)` chronology.

## 8. Exact calibration at `k=11,13,15`

All three known optimal words have `d=3`.  Their third derivative is an exact
Hamilton ordering of the middle rank, has zero internal-run linear residence
defects, and has no upper hole at any rank.  Endpoint-truncated short runs are
not counted as defects under this convention.

| `k` | protected factor components | opening/seam | fixed lower holes by depth | unrecycled q1 halo colours | word SHA-256 |
|---:|:---|:---|:---|:---|:---|
| 11 | `462` | open one cycle; cut `219--159` | `(1,1,0,0,0)` | `155` | `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850` |
| 13 | `1547,169` | remove `2395--2515`, `2167--2391`; add `2515--2391` | `(1,0,0,0,0,0)` | `2135` | `8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0` |
| 15 | `6390,45` | cuts `22,41`, foreign seam `19065--18041` | `(2,0,0,0,0,0,0)` | `18553,18033` | `f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b` |

For `k=11`, the additional lower-q2 residual is mask `154`.  For `k=13`,
the seam colour `2387` restores the first cut colour, leaving `2135`.  For
`k=15`, the seam colour `17017` equals neither cut colour, and both are
absorbed at the two ends.  The exact linear fixed-window audits give zero
upper holes at every depth in all three cases; unrestricted upper audits do
the same.  The retained words have lengths `465,1719,6438`, respectively,
and independently cover every nonempty mask.

The endpoint factors at `k=11,13` are algebraically PBBS-Markov reachable by
Theorem 2.1.  A protected primitive-by-primitive route from the canonical
PBBS seed was not frozen for those two cases.  At `k=15`, a literal protected
sequence of support `4,6,4` exchanges reduced the audited all-depth factor
through component counts `9 -> 4 -> 3 -> 2` before the successful opening.
That chain begins at the audited nine-cycle endpoint in the fixed-PBBS-
matching fibre; no protected primitive-by-primitive route from the canonical
PBBS factor to that nine-cycle endpoint is frozen.

### The common-Q warning

Let `P` be the maximal erosion (5.1).  The retained certificates satisfy:

| `k` | `DA=DP` | number of differing mask positions |
|---:|:---:|---:|
| 11 | no | 5 |
| 13 | no | 209 |
| 15 | yes | 0 |

Thus the `DA=DP` one-core compiler is a successful specialization, not a
uniform normal form.  Alternative same-chronology one-core certificates now
exist at `k=11` and `k=13`, so the displayed counts are only properties of
the retained words; “positions” means mask positions, not coordinate
incidences.  But the uniform normalization statement is definitively false:
at `k=9`, `COMP_2(T)` is feasible while the `129` targets of ranks at most
three cannot fit into the `128` literal positions forced by `DA=DP`.
Likewise the necessary literal-capacity inequality already fails at `k=19`
and `k=21`.  Therefore a general all-odd proof must use the full exact system
`COMP_d(T)`; one-core Hall may be invoked only as an explicitly verified
optional branch.  Exact proof and hashes are in
`MATH_AUDIT_AD_ALL_ODD_COMPILER_ONECORE_NORMALIZATION_20260729.md`.

## 9. Proved boundary and next attack

The following are now proved:

* the antipodal PBBS two-matching source is q1-exact, independently of its
  all-depth support;
* the same source supplies the all-depth tower;
* alternating circuits are a complete algebraic Markov basis for q1 factors;
* unprotected q1 component reduction is always possible;
* safe opening is exactly the target-kernel avoidance problem (4.3);
* the full length-`W+d` lower compiler is exactly `COMP_d(T)`; and
* for a one/two-cycle Johnson opening, each of its at most two unrecycled q1
  cut colours is individually compatible with its own boundary halo.

The architecture-free construction target is `FMCC(m)`: some upper-complete
middle permutation with feasible full `COMP_d(T)`.  The continuing PBBS lane
attacks it through the stronger `UPMBC(m)`: find a **protected**
at-most-two-cycle Markov endpoint with one kernel-avoiding opening and a
feasible pinned full compiler.  The cases `m=5,6,7` pass, but all have `d=3`;
they do not prove the growing-residence statement.  A viable proof of this
PBBS wrapper must establish either

\[
 \sum_{|Y|>r}|B_Y|<|\mathcal A(G)|                       \tag{9.1}
\]

for a recursively constructed protected endpoint and then solve the compiler,
or a stronger recursive invariant that directly carries a safe port and a
`COMP_d` solution from semilength `m` to `m+1`.

No cardinality heuristic or unprotected Hamiltonization proves this lemma.
Conversely, a sparse protected-connector cut, a cyclic repair dependency, or
a one-seam kernel cover certifies failure only for its specified
factor/library/port choice.  Even a universal protected-route no-go does not
refute endpoint-form `UPMBC(m)`, whose clause 1 permits a simultaneous
algebraic transform; one must exclude every four-clause endpoint/opening/
compiler witness.  None of these local certificates is a no-go for
`FMCC(m)` or for the coefficient-one theorem itself.
