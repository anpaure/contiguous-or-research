# Mathematical conclusion and exact frontier

## 1. Problem and proposed formula

Let `A=(A_1,...,A_L)` be a word of nonempty subsets of `[k]`, and put

\[
 U(i,j)=A_i\cup A_{i+1}\cup\cdots\cup A_j.
\]

Let `nu(k)` be the least `L` for which every nonempty subset of `[k]` is
some `U(i,j)`.  Define

\[
 r=\lceil k/2\rceil,\qquad
 W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

\[
 d(k)=\min\left\{d\ge0:dW+{d+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d(k).
\]

The conjecture is

\[
 \boxed{\nu(k)=B(k).}
\]

The rigorous status on 2026-07-28 is:

* `nu(k)>=B(k)` is proved for every `k`;
* equality is certified for every `k<=14`;
* the first open case is `k=15`, where
  \[
  W=6435,\qquad d(15)=3,\qquad B(15)=6438;
  \]
* no length-6438 word is known; the authoritative frozen carrier/compiler
  incidence graph has exact Hall deficiency `29`, and an exact chain of
  shadow-safe segment braids currently improves it to `21`.

No all-`k` upper-bound proof is currently known.

## 2. General lower bound

For a nonzero word of length `L`, write

\[
 C_i^{(j)}=A_i\cup\cdots\cup A_{i+j}
 \qquad(0\le j\le L-i).
\]

For each start `i`, these cells form an inclusion chain.  Let `f_i` be the
number of its cells of rank below `r`, and let `F_i=i+f_i` be the endpoint
of its first cell of rank at least `r`; put `F_i=L+1` if the entire column
stays below `r`.  A column may contain several rank-`r` cells with the same
label, but it witnesses at most one distinct rank-`r` target, at its
threshold endpoint.

The following three facts are the complete deadline argument.

1. `F_i` is nondecreasing: deleting the first letter cannot make a union
   larger, so `f_{i+1}>=f_i-1` whenever the comparison is nonvacuous.
2. Two different rank-`r` targets cannot have the same finite endpoint `F_i`:
   intervals ending at a common position are nested, and nested equal-rank
   sets are equal.
3. If `L=W+e`, the `W` distinct middle deadlines imply the depth cap
   \[
   f_i\le \min(e,L-i+1).
   \]

For completeness, if `v_1<...<v_p<=L` are all distinct finite deadline
values, then `p>=W`.  When `F_i=v_t`, monotonicity gives `i>=t` and room for
the later values gives `v_t<=L-(p-t)`, so `f_i=v_t-i<=L-p<=e`.  If
`F_i=L+1`, then `i>=p+1` and the same bound follows.  The column length gives
the second part of the minimum.

Every target of rank below `r` must occur among these cells.  Hence

\[
 \Lambda\le\sum_i f_i
 \le\sum_{i=1}^{L}\min(e,L-i+1)
 =eW+{e+1\choose2}.
\]

Thus `e>=d(k)` and `nu(k)>=B(k)`.  Stirling gives the correct asymptotic

\[
 \boxed{d(k)=\sqrt{\pi k/8}+O(1)}.
\]

## 3. Flat-carrier reduction

Let `(DX)_i=X_i\cup X_{i+1}`.  Then

\[
 (D^qA)_i=A_i\cup\cdots\cup A_{i+q}.
\]

The successful finite constructions seek a word of length `W+d` for which

\[
 D^dA=T,
\]

where `T=(T_1,...,T_W)` is an ordering of every rank-`r` set.  Under this
normal form, intervals of length at least `d+1` are unions of consecutive
carrier entries, while all shorter intervals occur in the rows
`A,DA,...,D^(d-1)A`.

Precisely,

\[
 \bigcup_{t=p}^{q}A_t
 =\bigcup_{i=p}^{q-d}T_i
 \quad(q-p+1\ge d+1),
 \qquad
 \bigcup_{t=p}^{p+s}A_t=(D^sA)_p
 \quad(0\le s<d).
\]

This separates the upper and lower *descriptions*, but it does not make
them independent.  All lower rows must arise from one physical word `A`.
In particular, an SDR of abstract erosion-envelope cells is not sufficient
unless the selected cell values can be realized simultaneously by the same
letters of `A` while retaining `D^dA=T`.

There is an exact test for that simultaneous realization.  Let a pin system
`Pi` assign a target `S_c` to selected physical intervals `I_c`, including
all central pins `(d,i)->T_i`.  For each coordinate put

\[
 Q_x=[0,W+d-1]\setminus
 \bigcup_{c:\,x\notin S_c} I_c.
\]

Then one nonempty physical word realizes every pin if and only if

\[
 Q_x\cap I_c\ne\varnothing
 \quad(c\in\Pi,\ x\in S_c),
 \qquad
 \{x:p\in Q_x\}\ne\varnothing
 \quad(0\le p<W+d).
\]

When these conditions hold, the maximal common realization is simply

\[
 A_p=\{x:p\in Q_x\}.
\]

Thus Hall is exact only after the physical intervals and all their negative
coordinate requirements have been fixed.  Separate rankwise SDRs do not
imply this common-pin criterion.

## 4. Exact residence criterion and forced boundary pair

For each coordinate `x`, inspect its binary incidence word along `T`.
Coordinatewise, a binary preimage of `T` under `D^d` exists exactly when
every internal run of ones has length at least `d+1`; boundary runs may be
shorter.  For a word whose letters are required to be nonempty, one must
additionally require a legal coordinate at every physical position.  This
extra condition is automatic for the resident Johnson carriers used in the
finite constructions, but not for an arbitrary ordering `T`.

The maximal legal erosion envelope at physical position `j` is

\[
 E_j=\bigcap_{i:\ i\le j\le i+d}T_i,
\]

and the run condition is exactly what makes the canonical maximal erosion
recover all carrier windows.

If `T` is a Johnson path

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},
\]

then every interior physical letter in any realization satisfies

\[
 \boxed{\{\alpha_j,\beta_{j-d-1}\}\subseteq A_j.}
\]

The two forced elements coincide exactly at a coordinate run of the minimum
allowed length `d+1`.  Thus minimum residence runs are useful: they create
the singleton-capable and other small compiler cells required by the lower
ideal.  Conversely, a one-piece standard sliding-window carrier has two
distinct forced elements in every interior letter when `r>d+1`, leaving only
`O(d)` boundary singleton positions.  This rules out the naive universal-
cycle construction for large `k`.

Explicitly, if `T_i={x_i,...,x_(i+r-1)}`, then every fully interior source
letter satisfies

\[
 A_j\supseteq\{x_j,x_{j+r-d-1}\}.
\]

The two symbols are distinct because their positions are separated by a
positive distance smaller than `r` inside one repetition-free set window.
Only the `2d+2` boundary positions escape the two-port condition, whereas
the `k` singleton targets require `k` distinct singleton letters.  Since
`d=Theta(sqrt(k))`, this standard one-piece ucycle architecture fails for
all sufficiently large `k`.

There is a sharper lower-level form.  For a resident Johnson carrier define

\[
 P_j=\bigcap_{i:\,i\le j\le i+d}T_i.
\]

On the flat interior, `P` is a rank-`(r-d)` Johnson path and

\[
 P_j\setminus P_{j+1}=\{\alpha_j\},\qquad
 P_j\setminus P_{j-1}=\{\beta_{j-d-1}\}.
\]

Every physical realization is a pinning of this controller:

\[
 (P_j\setminus P_{j-1})\cup(P_j\setminus P_{j+1})
 \subseteq A_j\subseteq P_j.
\]

### Native grading on a resident Johnson controller

There is a useful rigidity which rules out several tempting abstract Hall
repairs.  On every fully interior position of a depth-`d` resident Johnson
carrier,

\[
 |P_j|=r-d,
 \qquad |P_j\triangle P_{j+1}|=2.
\]

Moreover, for `0<=s<d`, the native trace of a depth-`s` compiler cell has
the forced rank

\[
 \left|P_j\cup P_{j+1}\cup\cdots\cup P_{j+s}\right|=r-d+s.       \tag{4.1}
\]

Indeed, the deletions in any `d` consecutive carrier transitions are
distinct: a repeated deletion would require an intervening re-entry followed
by an internal positive run shorter than `d+1`.  The same argument makes the
successive controller additions distinct through the compiler window, giving
(4.1).  Boundary controller cells, whose defining intersection is clipped,
must be treated separately.

For `k=15`, `(r,d)=(8,3)`, so interior native cells have ranks `5,6,7` at
depths `0,1,2`.  In particular, the abstract repair which changes free
depth-zero cell `5617` from trace `2574` to rank-six trace `2575` is not
physically realizable by a resident Johnson carrier; nor can a depth-one cell
have rank-seven native trace `2607`.  The grade-compatible splitter for the
remaining `2/1` circuit must retain a depth-two native `2607` cell and create
a distinct depth-one native `2575` cell.  This is exactly the graded split
shape of the certified `H23 -> H22` descent.

On each internal maximal coordinate run `[u,v]` in `P`, the selected
positions carrying that coordinate must include `u` and `v` and have gaps at
most `d+1`; these conditions are also sufficient coordinatewise.  If `p_x`
is the number of controller incidences, `t_x` the number of carrier
incidences, and `i_x` the number of internal carrier runs, then

\[
 p_x=t_x-di_x.
\]

For an exact middle deck this gives the global congruence

\[
 p_x\equiv {k-1\choose r-1}\pmod d.
\]

This controller-and-pinning description is the most precise current form of
the lower compiler.

## 5. Exact global formulation

For a start position `i` and coordinate `x`, let `n_i(x)` be the next
position at or after `i` containing `x`.  Then

\[
 U(i,j)=\{x:n_i(x)\le j\}.
\]

Consequently the interval unions from `i` are exactly the initial unions of
the finite-time blocks in the ordered partition of coordinates by equal
next-occurrence time; the block at time infinity is never included.  Passing
from `i` to `i+1` removes the first block and reinserts its elements according
to their later occurrences.  This is the exact move-to-front/stable-deletion
compatibility missing from an arbitrary symmetric-chain decomposition or
minimum monotone Venn diagram.

## 6. Pascal recursion and seams

The odd/even lifts are governed by the two Pascal decompositions of the new
middle layer.  If `z` is the new coordinate, then

\[
 { [2m+2]\choose m+1}
 ={[2m+1]\choose m+1}
 \sqcup \{\{z\}\cup X:X\in{[2m+1]\choose m}\},
\]

and

\[
 {[2m+1]\choose m+1}
 =\{\{z\}\cup T:T\in{[2m]\choose m}\}
 \sqcup {[2m]\choose m+1}.
\]

They explain why the finite lifts use old middle sets, adjacent
intersections, and adjacent unions.  They do not by themselves provide one
chronology preserving residence, all shadows, and the physical lower
compiler.  The `k=14` six-piece braid is a finite successful instance; every
five-piece version in the audited odd-to-even lift template fails for a
structural endpoint shortage.

## 7. The missing theorem, corrected

A direct sufficient all-`k` theorem must construct an ordering `T` and one
physical word `A` satisfying items 1--4 below.  A recursive Pascal proof must
additionally establish items 5--6:

1. `T` lists every rank-`r` set exactly once;
2. every internal coordinate run in `T` has length at least `d+1`;
3. unions of consecutive blocks of carrier entries cover every upper target;
4. `D^dA=T` and the first `d` derivative rows of this same `A` cover every
   lower target;
5. the Pascal sectors can be braided while preserving 1--4;
6. every seam/component-joining operation obeys a cut-aware protected-
   occurrence budget.

Condition 6 is essential when coverage is propagated from protected parent
occurrences.  It is unnecessary only if the final child chronology and all
its windows are recomputed and verified directly.  Scalar multiplicity at
least two is not enough:
there is a fully verified rank-four Johnson transition system on `[12]`
whose every depth-three label has load at least two but for which every
connected re-pairing loses labels.  On a rigid contact tree the exact local
support condition is

\[
 m_S-d_S+a_S\ge1\qquad\text{for every protected label }S,
\]

where `d_S` and `a_S` count deletions and recreations made by the chosen
bridges.

Proving this corrected Shadow--Braid theorem would give
`nu(k)<=W+d(k)` and therefore equality.  Its failure would refute only the
flat-carrier/Pascal-braid architecture, not the formula itself.

## 8. Current frontier

The clean status is therefore:

\[
 \boxed{\text{general lower bound proved; exact through }k=14;
 \quad k=15\text{ open at outer Hall deficiency }19.}
\]

The decisive object is no longer merely another middle-layer ordering.  It
is one shadow-preserving, residence-compatible chronology carrying a single
integral lower compiler, with cut-aware protection at every seam.

For the frozen `k=15` carrier, the Hall-29 residual has now been sharpened
further.  Every one of its 35 peeled targets has a unit-boundary exposure,
but 29 distinct target/cell addresses require at least 24 controller pins;
an explicit optimistic 24-pin incidence certificate attains that bound.
Any physical completion still needs one compensated rank-five Johnson
controller satisfying the statewise rank equations, the coordinate
congruences above, forced ports and run-gap rules, all retained reservations,
and the upper shadows.  The incidence certificate is therefore a sharp
relaxation, not a length-6438 word.

There is now a strict, fully audited segment-braid descent from the frozen
carrier,

\[
 H29\xrightarrow{\mathrm{RF}(471,2327,5456)}H28
 \xrightarrow{\mathrm{FF}(322,556,3940)}H27
 \xrightarrow{\mathrm{FF}(784,1712,6357)}H26
 \xrightarrow{\mathrm{FR}(3259,3823,5264)}H25.
\]

Every state preserves the exact middle deck, Johnson adjacency, depth-three
residence, every upper shadow through depth seven, global upper coverage, and
the same four-hole immediate-lower support size.  The seven zero-candidate
targets are unchanged.  Exhaustive enumeration from the Hall-26 endpoint
selects the Hall-25 move above.  A second exhaustive scan proves Hall 25 is a
one-move local minimum for this complete four-type catalogue (551,986 Johnson
moves, 12,029 resident moves, and 9,233 upper-safe moves).  This is not a
global obstruction.  Full details and reconstruction are in
`MATH_K15_THREE_CUT_SEGMENT_BRAID_DESCENT_20260728.md`.

The Hall-25 local minimum is nevertheless escapable by bounded lookahead:

\[
 H25\xrightarrow{\mathrm{FR}(1512,2458,4103)}H25
 \xrightarrow{\mathrm{FR}(2664,3491,6201)}H24.
\]

The first braid creates a genuine portal into the old DM shore while a new
gap-25 shore replaces it; the second braid discharges that replacement shore.
Every protected invariant above is preserved.  A separate two-braid Pareto
path gives `(Hall,zero)=(25,7)->(26,6)->(25,6)`, proving that the zero-target
floor can also be reduced, although not yet on the Hall-24 branch.  These exact
two-braid mechanisms are recorded in
`MATH_K15_TWO_BRAID_DM_PORTAL_ESCAPE_20260728.md`.

The same mechanism then repeats:

\[
 H24\xrightarrow{\mathrm{FF}(212,3732,4717)}H24
 \xrightarrow{\mathrm{FF}(210,1501,4867)}H23.
\]

This pair removes an entire `161/160` DM component rooted at mask `20516`,
with no replacement DM target.  The Hall-23 state again preserves the middle
deck, residence, every upper shadow, and the four-hole lower palette; its seven
zero-candidate targets remain the unresolved floor.

A third neutral/improving pair,

\[
 H23\xrightarrow{\mathrm{RF}(3799,4497,6039)}H23
 \xrightarrow{\mathrm{FR}(740,4051,6137)}H22,
\]

discharges the small `2/1` DM component `{4877,4909}`.  This shows that the
bounded-lookahead ear mechanism applies beyond the large rank-four-root
components.

The formerly separate zero-target branch now merges back into the Hall
frontier:

\[
(22,7)\xrightarrow{\mathrm{FF}(882,2606,3222)}(23,6)
\xrightarrow{\mathrm{RF}(1500,4943,6184)}(22,6).
\]

Hence this intermediate carrier simultaneously has Hall deficiency `22` and
only six zero-candidate targets, while preserving every protected invariant.
Its canonical DM shore is `1006/984`.  One word realizes 983 native pins plus
the exceptional repin `2607 -> 2575`, displacing `2607`; thus 984 distinct
DM-shore pins coexist and the critical-shore common-pin gap is exactly 22.
This is not a global maximum-matching lift.  On the seven-zero H22 branch,
the endpoint controller also retains the preceding two discharges
cumulatively: it realizes 1146 pins on the former 1168-target H24 shore,
missing exactly the current 22 roots.

Exhaustive current-source scans find no H21 one-braid neighbour of either
H22 carrier.  The seven-zero state has no Hall-neutral zero-six neighbour—the
unique zero-reducing braid goes to `(23,6)`—and the six-zero state has no
zero-five neighbour at any Hall score.  The next finite gate is therefore a
new bounded-lookahead router/splitter (or creator/compensator), not another
greedy one-braid descent.

The direct radius-two class has also been closed.  The six-zero state has
`684` distinct nontrivial protected-neutral first braids.  None changes the
projected shore of the remaining circuit `{2575,2607}`, and none creates a
candidate for any of the six zero targets.  Exactly two relocate the shared
physical circuit cell; their `18,194` eligible second braids contain no H21
or zero-five state.  Seven representative distance-one creator corridors,
covering the circuit and all six zero roots, contribute another `63,783`
exact second braids and again contain no descent.  This is a no-go only for
the stated direct/near-creator radius-two catalogue.

The complete neutral-first beam then finds exactly the missing remote route:

\[
 (22,6)\xrightarrow{\mathrm{FF}(1320,5339,6194)}(22,6)
 \xrightarrow{\mathrm{FR}(778,2292,6368)}(21,6).                \tag{8.1}
\]

Both moves preserve the exact deck, Johnson chronology, depth-three
residence, every upper support layer, and four immediate-lower holes.  The
neutral braid replaces the old `160/159` component rooted at `449` by a
`24/23` component rooted at `458`; the second braid discharges that new
component.  Its common-core contracted boundary rank is `17 -> 18`.  The
final canonical DM shore is `846/825`, decomposes into 21 gap-one components,
and all 825 right cells are distinct native traces of the one maximal erosion
word.  More strongly, those 825 native pins plus 24 pins on the discharged
component give 849 simultaneous literal pins on the former 870-target shore:
one duplicated native-`462` cell is shrunk to the exposed root `458`, changing
only controller positions 778 and 779.  Thus the former shore's literal
common-pin gap is exactly 21.  This is still not a common-word lift of one full
global maximum matching.  The exact certificate is
`MATH_K15_H22_TO_H21_REMOTE_COMPONENT_COMPRESSION_20260728.md`.

The same mechanism has now been repeated prospectively at the next frontier.
Among all `687` nonidentity protected Hall-21-neutral braids, the unique
minimum-DM state has shore `702/681` (the next best is `814/793`, versus the
canonical `846/825`).  It is reached and discharged by

\[
 (21,6)\xrightarrow{\mathrm{RF}(1510,5017,6136)}(21,6)_{702/681}
 \xrightarrow{\mathrm{RF}(885,1393,3668)}(20,6).              \tag{8.2}
\]

Independent reconstruction gives matching ranks
`16362,16362,16363`, lower-hole vectors
`(4,18,9,1,0,0,0)`, `(4,18,11,1,0,0,0)`,
`(4,18,11,1,0,0,0)`, and zero holes in every upper layer throughout.
The neutral braid replaces only the rooted `169/168` component at `1920`
by a rooted `25/24` component at `1801`; the improving braid removes that
smaller component and leaves the other twenty component target sets
unchanged.  The two contracted boundary ranks are again `24 -> 24` and
`17 -> 18`.

This second descent also pays a literal common-word unit.  In the final
carrier, the former 25-target component has native traces equal to all 24
nonroots, with trace `1833` duplicated at physical cells `9334` and `9599`.
Shrinking either copy by

```text
(1577,809) -> (1545,777)
```

realizes the missing root `1801` while preserving every central window, all
657 final-DM native pins, and all other component pins.  Hence one word
realizes `682=702-20` simultaneous pins on the former shore.  This remains a
shore-local certificate, not a common-word lift of one full 16,363-edge
matching.  The exact carrier theorem and common-word audit are
`MATH_K15_DM_COMPRESSION_ROUTER_H20_20260728.md` and
`scratch/audit_k15_h21_h20_rooted_native_common_q.py`.

The Hall-20 neutral recursion has now produced and independently verified the
next descent:

\[
 (20,6)\xrightarrow{\mathrm{RF}(180,2764,4210)}(20,6)
 \xrightarrow{\mathrm{FR}(123,722,4710)}(19,6).              \tag{8.3}
\]

The matching ranks are `16363,16363,16364` and the positive DM shores are
`677/657`, `677/657`, and `516/497`.  The neutral braid is not a compression:
it fuses the rooted `161/160` and `160/159` components exposed at `8217` and
`8218` into one `321/319` two-root native forest while leaving the remote
`24610` component's abstract profile unchanged.  The improving braid then
duplicates the common profile `{24610,25634}`, splits two paired profiles,
and saturates that entire remote `161/160` component.  Thus Hall 19 is a
physical profile-routing descent, not merely another minimum-shore descent.

There is again an exact shore-local common-word witness.  Native target
`25634` has physical cells `1212` and `4713`; shrinking either copy to the
exposed root `24610` preserves the other copy, every central window, all 497
native pins on the final positive shore, and all 160 non-root pins of the
discharged component.  Hence one controller realizes `658=677-19` literal
pins on the former Hall-20 shore.  This is not a common-word lift of a full
16,364-edge matching and does not prove `nu(15)=6438`.  The abstract theorem,
literal audits, and exact route are frozen in
`MATH_THEOREM_K15_MULTIROOT_NATIVE_FOREST_PROFILE_ROUTER_20260728.md` and
`MATH_K15_DM_PROFILE_ROUTER_H19_20260728.md`.

The full direct one-braid neighbourhood of the Hall-19 carrier is also now
exhausted: 548,377 Johnson candidates yield 11,957 resident candidates and
9,164 upper-safe candidates, but no Hall-18 state.  Its best score remains
`(19,6)`.  The next finite experiment is therefore the same validated
recursion with a stronger ranking coordinate: enumerate Hall-19-neutral
states and score both DM compression and physical duplicate/root readiness,
because the Hall-20 to Hall-19 router left the decisive abstract component
profile unchanged.

The smallest abstract edit of `{2575,2607}` is one added incidence, but the
native grading lemma above rejects the two most tempting realizations.  A
depth-zero cell cannot change from rank-five trace `2574` to rank-six `2575`,
and a depth-one cell cannot change from rank-six `2606` to rank-seven `2607`
inside a resident controller.  The exact grade-compatible target is now:

\[
 \boxed{\text{retain one depth-two native }2607\text{ cell and create one
 depth-one native }2575\text{ cell}.}
\]

The graded portal is physically real but has fixed collateral.  Exactly ten
such two-braid portals occur in the complete neutral-first census; all improve
the old shore to gap 21 but create a remote Hall-25 shore by losing the same
five lower supports.  Every portal-preserving third braid is support-
nongaining, and the unique Hall-22 repair forms a two-cycle with the portal.
This separate no-go is recorded in
`MATH_K15_GRADED_PORTAL_AND_FIXED_COLLATERAL_20260728.md`.

The exact remote-split mechanism, cumulative common-controller certificate,
two-colour residual-circuit classification, and regenerative safe-swap
groupoid theorem are recorded in
`THREAD_D_H22_NEUTRAL_ROUTER_CIRCUIT_SPLITTER_THEOREM_20260728.md`.

The required compound is now an exact integral object.  Cutting H25 into
retained segments makes every deck-exact reconnection an alternating-cycle
port circulation, with a separate one-component condition.  The H25
maximum-deficiency shores form a residual-DM lattice with `9,256` optional
balanced SCCs and at least `2^5760` members, but the minimum signed collar
current over the entire lattice is one integral maximum-closure/min-cut
problem.  The certified two-braid path above is a positive Hall-layer
multi-collar: its exact 58-cell boundary bank gains one contracted matching
rank and therefore opens every H25 maximum shore simultaneously.  This does
not finish the construction: Hall zero, the necessary `h_1<=2,h_2<=5`
corridor, and one common physical compiler word must still be satisfied by
one integral continuation.  The theorem-level reduction and exact audit are
`THREAD_D_H25_MULTI_COLLAR_CROSS_STRATUM_CIRCULATION_20260728.md`.

The first controller-lift census further separates local service from global
compensation.  Of the `1,602` retained Hall-service UNIT pin types, `1,318`
admit an isolated locally legal rank-five state replacement.  Their induced
middle-deck replacement digraph is acyclic, and none of the `1,318` edits
retains any advertised target/cell address after its forced deletion.  Hence
no separated repair assembled only from those service edits can preserve the
exact middle deck or physically serve its advertised target.

This is not an all-UNIT no-go.  The full theoretical UNIT graph has `10,370`
locally admissible arcs and nontrivial directed cycles, including an explicit
pairwise separated 3-cycle preserving the exact middle deck.  A complete
two-state census finds `59` target-safe local export blocks and three whose
two deck imbalances are individually routable in the ambient graph.  None is
already a closed physical circuit: the known closures conflict in controller
position, and upper-shadow preservation and the one-common-word criterion
remain unaudited.  Thus the smallest positive finite target is now one
**collective target-safe compensated deck circuit**, not a collection of
independent Hall-service collars.
