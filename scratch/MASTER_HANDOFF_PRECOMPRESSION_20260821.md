# ARCHIVED pre-compression handoff (superseded 2026-08-22)

This 2026-08-21 snapshot is retained only for recoverability and provenance.
It is superseded by `MASTER_HANDOFF.md` and must not be used as the current
proof frontier.

# Universal contiguous-subarray OR arrays: master theorem handoff

This is the compact mathematical state of the project: proved theorems,
authenticated finite certificates, exact conditional reductions, reusable
no-go results, and the conjectures that are still genuinely open.  Search
diaries, timeouts, seed histories, superseded claims, and failed proof sketches
are omitted.  A cited artifact certifies only its displayed scope; it never
licenses the composition of independently constructed objects.

"Self-contained" here means that every retained statement gives the objects,
hypotheses, quantifiers, and conclusion needed to use it.  Proof files are
cited for auditability instead of being recopied in full.  The only
reference-scoped data are the byte-hashed finite-instance ledger in Section
6.2 and the canonical witness files in Sections 3 and 5.7.  Conjectures and
conditional implications are labelled as such.

## 1. Problem, exact state model, and notation

Identify a `k`-bit mask with a subset of `[k]`.  For a word

\[
A=(A_1,\ldots,A_n),\qquad
U(i,j)=\bigcup_{p=i}^j A_p,
\]

let `N(k)` be the least `n` for which all subsets of `[k]`, including the
empty set, occur as some `U(i,j)`.  Let `nu(k)` be the analogous minimum when
all letters are nonempty and only nonempty targets are required.

**Zero theorem.**

\[
N(k)=\nu(k)+1.
\]

Deleting every zero from a full word preserves all nonempty interval unions;
conversely, one zero at an endpoint adds the empty target.

**Move-to-front theorem.**  At a right endpoint `j`, group only coordinates
that have occurred in `A_1,...,A_j` by equal last-occurrence time, most recent
first (the state before `A_1` is empty):

\[
P_j=(B_1,\ldots,B_t).
\]

The distinct suffix unions ending at `j` are exactly the prefix unions
`B_1`, `B_1 union B_2`, ..., `B_1 union ... union B_t`.  Appending a nonempty
letter `X` performs the exact transition

\[
(B_1,\ldots,B_t)\longmapsto
(X,B_1\setminus X,\ldots,B_t\setminus X),
\]

after empty blocks are deleted.  Hence `nu(k)` is the shortest walk through
ordered set partitions under arbitrary-set move-to-front updates whose prefix
unions cover the nonempty Boolean lattice.

For a set sequence `X`, define its OR derivative by

\[
(DX)_i=X_i\cup X_{i+1},\qquad
(D^qX)_i=\bigcup_{p=i}^{i+q}X_p.
\]

Every interval union of `A` is one entry of its derivative triangle
`A,DA,D^2A,...`.

Throughout, `[x]_+=max(x,0)` and
`Cat_m=binom(2m,m)/(m+1)`.  `SCD` abbreviates symmetric-chain
decomposition.

## 2. Sharp general lower bound

For `1<=r<=k`, put

\[
M_r={k\choose r},\qquad
\Lambda_r=\sum_{s=1}^{r-1}{k\choose s},
\]

and let

\[
\tau_r=\min\left\{t\ge0:
\Lambda_r\le tM_r+{t+1\choose2}\right\}.
\]

Set `B(0)=0`.  For `k>=1`,

\[
\boxed{\nu(k)\ge B(k):=\max_{1\le r\le k}(M_r+\tau_r).}
\]

The maximum is attained at `r=ceil(k/2)`; with
`r=ceil(k/2)`, `W=binom(k,r)`, `Lambda=Lambda_r`, and

\[
d(k)=\min\{d\ge0:dW+{d+1\choose2}\ge\Lambda\},
\]

one has `B(k)=W+d(k)` and

\[
d(k)=\sqrt{\pi k/8}+O(1).
\]

**Proof kernel.**  Choose one witness interval for every rank-`r` target and
sort by left endpoint.  Equal-rank witnesses are noncontaining, so in a word
of length `M_r+t` their endpoints have the form

\[
[i+\alpha_i,i+\beta_i],\qquad
0\le\alpha_i\le\beta_i\le t.
\]

Thus every interval of length at least `t+1` contains a rank-`r` witness.
Every lower target must use one of the
`tM_r+binom(t+1,2)` shorter intervals, giving the bound.

**Endpoint-chain strengthening.**  In any word of length `W+e`, the sorted
middle witnesses satisfy `i<=ell_i<=u_i<=i+e`; all strict-lower targets
therefore lie in at most `W+e` endpoint chains of length at most `e`.
In the static graph having `d` labelled slots at every rank-`r` owner and an
edge `S--(T,j)` exactly when `S subset T`, the lower-target Hall deficiency is
at most

\[
h=(\Lambda-dW)_+\le {d+1\choose2}.
\]

These conclusions require no carrier, factor, symmetry, or grading ansatz.
For a universal word of length `B(k)=W+d`, after choosing one witness for
every middle and strict-lower target, write
`sigma=dW+binom(d+1,2)-Lambda`.  For a selected witness `[a,b]`, its
last-occurrence depth is the number `j_b` of nonempty recency blocks whose
successive prefix unions are needed to reach its middle target; maximum depth
means `j_b=d+1`.  Define first-occurrence depth symmetrically from `a`.
At least `[W-sigma]_+` selected middle witnesses are forced to have maximum
length `d+1` and maximum last-occurrence depth; these maximum-length witnesses
occupy one contiguous interval in endpoint order.  At least
`[W-2sigma]_+` witnesses have both maximum first- and maximum last-occurrence
depth, without a contiguity claim
(`ENDPOINT_SATURATION_INDEPENDENT_AUDIT.md`).

## 3. Exact finite theorem

The lower bound is attained for every `0<=k<=16`.  The historically decisive
closure in each dimension was:

| `k` | `nu(k)` | first mechanism that closed the case |
|---:|---:|---|
| 0 | 0 | the empty word |
| 1 | 1 | the singleton word and the one-target bound |
| 2 | 2 | a direct two-letter construction and endpoint count |
| 3 | 4 | three singleton positions cannot realize all three two-sets |
| 4 | 7 | Sperner-equality rigidity forces one position beyond width |
| 5 | 12 | the odd two-middle-layer obstruction forces `W+2` |
| 6 | 21 | general Sperner-equality rigidity plus an attaining word |
| 7 | 37 | the odd two-middle-layer obstruction plus a graded word |
| 8 | 72 | the rank-count bound plus a graded fixed-window construction inspired by the `k=7` pattern |
| 9 | 128 | short-cell saturation forces `D^2A` to enumerate rank five; a compatible middle-level factor exists |
| 10 | 254 | a Johnson chronology with complete two-sided shadows and exact delay-two factor labeling |
| 11 | 465 | quotient SAT found a resident all-shadow voltage-two carrier; a safe cut and exact compiler completed it |
| 12 | 926 | one-hole recovery completed the 924-state central path and its natural factor |
| 13 | 1719 | two perfect carrier cycles were cut and joined by one Johnson seam; the compiler absorbed the lost boundary colour |
| 14 | 3434 | a six-piece odd-to-even `A/B` braid supplied exact depth-two residence and compilation |
| 15 | 6438 | resident cycles of lengths `6390+45`, an upper-safe nonrecycling seam, two boundary colours, and the generalized compiler |
| 16 | 12873 | one common-cap SAT model assigned all 26,331 residual lower targets injectively to short cells while enforcing a shared nonempty source letter at every position |

For every `1<=k<=16`, `answers/kNN.word` is the canonical nonzero witness;
`N(k)=nu(k)+1`.  `answers/README.md` records every SHA-256 and a uniform
exhaustive verifier.  The `k=16` word passed four independent complete
`65,535/65,535` replays; the separate bound `B(16)=12873` then proved
optimality.  Historically, `k=12` closed before `k=11`.  The frontier proof
records are
`K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`; `answers/k12.word` together
with its verifier; `MATH_K13_EXACT_1719_CERTIFICATE_20260728.md` together
with `scratch/k13_exact_1719.certificate.json`;
`MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`;
`K15_OPTIMAL_6438_TWO_CYCLE_ARBITRARY_SEAM_CERTIFICATE_20260729.md`; and
`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.

No older interval for `k=11,13,14,15,16` is current.

The same `k=11` certificate is a finite structural reset: `D^3A` enumerates
all rank-six owners; consecutive-owner intersections and unions cover their
two turn-colour shores; the two occurrence matrices both have full rank 792;
every internal coordinate run has length at least four; all shadows through
depth five occur; and the decoded owner support is a 132-path forest.  It is
not a recursive socket theorem
(`MATH_THEOREM_ML11_GUARDED_FULL_RESET_PACKET_20260731.md`).

## 4. Exact unrestricted and flat compiler calculus

**Unrestricted normal form.**  Choose one interval `I_S=[ell_S,r_S]` for
each nonempty target `S`, and put
`L_p={S:ell_S=p}`, `R_q={S:r_S=q}`.  Every nonempty `L_p` and `R_q` is an
inclusion chain; these two ordered chain partitions are orthogonal
(`|L_p cap R_q|<=1`) and triangular (`p<=q` whenever their intersection is
nonempty).  Conversely, any such pair assigns distinct intervals.  Put

\[
Z_x=[n]\setminus\bigcup_{S:x\notin S}I_S.
\]

It realizes every assigned target iff `I_S cap Z_x` is nonempty for every
`x in S`; the realization is nonzero in all `n` positions iff
`union_x Z_x=[n]`, while otherwise deleting empty positions gives a shorter
nonzero word.  Equivalently, a nonzero universal word exists iff there is an
ordered triangular orthogonal chain pair with pin survival.  This is the
exact unrestricted reduction (`GLOBAL_FLAG_RIGIDITY.md`).

The following is a construction theorem, not a claim that every optimum has
this form.

Fix `W=binom(k,r)`, a rank-`r` chronology
`T=(T_1,...,T_W)` with every `T_i in binom([k],r)`, and depth `d`.

**Factorization theorem.**  There is a possibly-empty-letter sequence `A`
with `D^dA=T` iff every internal run of ones in every coordinate-incidence
word of `T` has length at least `d+1`; boundary runs may be shorter.  The
coordinatewise maximal factor is

\[
A_j^{\max}=\bigcap_{\max(1,j-d)\le i\le\min(W,j)}T_i.
\]

A nonzero factor of length `W+d` exists exactly when
`A_j^max` is nonempty for every `1<=j<=W+d`.

**Exact lower compiler.**  Assign every strict-lower target `S` injectively
to an interval `J_S` of length at most `d`.  For each coordinate `x`, define

\[
E_x=[W+d]\setminus\bigcup_{i:x\notin T_i}[i,i+d],\qquad
Q_x=E_x\setminus\bigcup_{S:x\notin S}J_S.
\]

The assignment is realizable iff `J_S cap Q_x` is nonempty for every `x in S`,
`[i,i+d] cap Q_x` is nonempty for every `x in T_i`, and
`union_x Q_x=[W+d]`.  Taking `A_j={x:j in Q_x}` then spells a valid nonzero
factor.  This common-`Q`/negative-window closure is exact; the older one-core
identity `DA=DP` is not without loss (the optimal `k=9` word is a
counterexample).

**Exact upper oracle.**  From a candidate start `i`, let
`delta_i(x)=min{q>=0:x in T_(i+q)}`, taking the minimum over valid linear
indices (or modulo `W` in a declared cyclic chronology) and setting an empty
minimum to `+infinity`.  Start at the first owner `T_i` of a maximal
consecutive run satisfying `T_j subseteq S` (if the whole cyclic chronology
is contained in `S`, any start may be used).  A target `S` occurs as a union
of consecutive central owners iff some such start `i` has all outside
coordinates arriving after all coordinates of `S`:

\[
\max_{x\in S}\delta_i(x)<\min_{y\notin S}\delta_i(y).
\]

Fixed-width proxy rows do not replace this arbitrary-width test.

More precisely, suppose the carrier is a rank-`r` Johnson path
`T_(i+1)=T_i-{alpha_i}+{beta_i}` for `1<=i<W`, where `alpha_i` is the deleted
coordinate and `beta_i` the inserted coordinate, and suppose it satisfies
the run criterion above.  Put

\[
P_j=\bigcap_{i:\,i\le j\le i+d}T_i.
\]

At every flat-interior position `d+2<=j<=W-1`,
`P_j\P_(j+1)={alpha_j}` and
`P_j\P_(j-1)={beta_(j-d-1)}`; every factor obeys

\[
(P_j\setminus P_{j-1})\cup(P_j\setminus P_{j+1})
 \subseteq A_j\subseteq P_j.
\]

Thus the maximal erosion `P` is the exact lower controller: a compiler must
choose `A_j` inside `P_j`, contain the two displayed forced port sets, and
meet every lower-target interval assigned in the exact compiler above.  An
abstract system of distinct representatives (SDR) that ignores these
constraints is insufficient.

Consequently a flat word of length `W+d` is universal exactly when:

1. `T=D^dA` enumerates every rank-`r` target exactly once;
2. `A,DA,...,D^{d-1}A` realize every strict-lower target; and
3. consecutive unions of `T` realize every upper target.

References:
`THREAD_A_UNRESTRICTED_COMP_TWO_BOUNDARY_LAMINAR_HALL_THEOREM_20260729.md`,
`MATH_AUDIT_AD_ALL_ODD_COMPILER_ONECORE_NORMALIZATION_20260729.md`, and
`MATH_THEOREM_BINARY_CSPACE_EXACT_UPPER_INTERVAL_ORACLE_20260729.md`;
the Johnson-controller form is in
`MATHEMATICAL_CONCLUSION_EXACT_FRONTIER_20260728.md`.

## 5. Durable structural theorems

### 5.1 Universal constraints and upper bounds

For every coordinate set `Q`, deleting all letters meeting `Q` leaves a
universal word on `[k]\Q`.  Hence

\[
\#\{i:A_i\cap Q=\varnothing\}\ge\nu(k-|Q|),
\]

and, for every integer `0<=t<=k`, after averaging over all `t`-sets,

\[
\sum_i {k-|A_i|\choose t}\ge {k\choose t}\nu(k-t).
\]

Here an out-of-range binomial coefficient is zero.

This is `MATH_THEOREM_K_ALL_COORDINATE_DELETION_CAP_AND_K17_SURPLUS_20260731.md`.
For every fixed integer `C>=0`, as `k->infinity`, every length-`W+d+C`
universal word has total letter-coordinate incidence at least `c_C rW` for
some constant `c_C>0`; this excludes only architectures with `o(rW)` total
occurrence mass.
See
`MATH_THEOREM_ARCHITECTURE_FREE_ADDITIVE_C_DIAGONAL_RUN_NORMALIZATION_20260803.md`.

In a nonzero universal word on `[k]` of length `n`, for `1<=s<=k`, every
physical interval whose union has rank `s` has length at most the exact
simultaneous cap

\[
c_s(n)=\min\!\left(n,
\min_{\substack{r>s\\{k\choose r}\le n}}(n-{k\choose r}),
\min_{\substack{r\le s\\{k\choose r}\le n}}
       (n-{k\choose r}+{s\choose r})\right),
\]

where an empty minimum is `+infinity`.  In particular
`#{i:|A_i|<=s}>=binom(k,s)+tau_s`.
See `CONTAINMENT_MULTIPLICITY_INDEPENDENT_AUDIT.md`.

For `2<=r<=k`, truncate the problem to all nonempty targets of ranks at most
`r`, and put `beta_r=binom(k,r)+tau_r`.  If a zero-free covering word has
length `beta_r+c` for an integer `c>=0`, let
`h_r` count entries above rank `r`, and let `m_R` be the multiplicity of the
literal rank-`r` letter `R`, so
`delta_r=sum_R[m_R-1]_+`.  Canonically reduce the word by deleting every
entry above rank `r` and all but one occurrence of every literal rank-`r`
value; let `s_r` count the nonempty components of lower-rank positions in
that reduced word.  Then

\[
h_r+\delta_r+s_r-1\le c.
\]

At `c=0` there are no higher entries or duplicate rank-`r` literals; all
literal rank-`r` entries are distinct and lie in the two boundary blocks
around one contiguous core, and that core covers the complete strict lower ideal
(`RANK_FILTRATION_STABILITY.md`, `BOUNDARY_CORE_RIGIDITY_AUDIT.md`).

To state the endpoint-blocker barrier, give nonnegative weights `x_S` to
nonempty targets subject to `sum_(S in C)x_S<=1` for every inclusion chain
`C`.  For an interval of union `T`, the endpoint argument gives the sharp
weighted cap `length<=n-sum_(S not subset T)x_S`.  Even after optimizing
these weights target by target and imposing every nested Hall inequality on
the number of physical intervals below each resulting length threshold, the
least permitted `n` is exactly `B(k)`.  Any stronger lower bound must retain
named-cell competition, both endpoint orders, or coordinate pins
(`BLOCKER_BARRIER_AND_CONTAINMENT_SPECTRUM.md`).

For `k>=2`, the simple top-bit splice gives

\[
\nu(k)\le2\nu(k-1).
\]

The strongest unconditional general construction recorded here is

\[
\boxed{\nu(k)\le(\sqrt2+o(1)){k\choose\lfloor k/2\rfloor}.}
\]

See `SQRT2_CONSTRUCTOR_README_20260727.md`.

As `k->infinity`, there are also literal `(1+o(1))W` words covering every
target whose rank differs from `floor(k/2)` by at most any fixed integer;
quantitatively the same holds for half-width `h=o(sqrt(log k))`.  This is a
band theorem, not a full-cube upper bound.
See `FIXED_DEPTH_SHADOWS.md` and
`OPTIMIZED_ECONOMICAL_QUEUE_BAND_20260724.md`.

### 5.2 Central owner/forest geometry

Let `Omega` have `2m` elements and set
`L=binom(Omega,m-1)`, `X=binom(Omega,m)`, and
`U=binom(Omega,m+1)`.  The Johnson graph `J(2m,m)` has vertex set `X` and
joins two `m`-sets that differ by one exchange.  A physical edge `e=TH` has
lower colour `ell(e)=T cap H`, upper colour `u(e)=T union H`, and represents
the Boolean diamond `ell(e) subset T,H subset u(e)`.  For a physical support
`R`, its occurrence graph `G_R` is bipartite on `L,U` with one edge
`ell(e)--u(e)` for each occurrence `e in R`.  A spanning linear forest is an
acyclic spanning subgraph of maximum degree two; isolated vertices count as
components.

The correct central object is forest-first, not Hamilton-first.  For a fixed
spanning physical linear-forest support `R`, selecting all required lower and
upper colours exactly once is equivalent to a perfect matching in `G_R`
(Hall/Rado).  Such a matching has `binom(2m,m-1)` physical edges and therefore
exactly `Cat_m` path components.  A preselected 2-factor or Hamilton cycle is only a
sufficient specialization and can introduce artificial obstructions.

For the useful 2-factor subclass, let `ML(2m-1)` be the containment graph
between ranks `m-1` and `m` on a `(2m-1)`-set.  Write a factor component as
`A_0,B_0,A_1,B_1,...`, with `A_i subset B_i supset A_(i+1)`.  Select `A`- and
`B`-occurrences so that the turn colours
`A_i cap A_(i+1)` and `B_(i-1) union B_i` are each globally bijective and
selected shore types alternate on every component.  Encode selected
positions by a cyclic binary trace.  Let `f` count all-one traces, and let
`g` count mixed traces in which every positive zero-run has length two and
every one-run is odd.  The physical lift then has cyclomatic number exactly
`2f+g`; it is a `Cat_m`-path forest exactly when `f=g=0`.  For a fixed factor,
choosing the decoration is an occurrence-graph perfect matching.  Conversely,
for a fixed perfect diamond matching `M`, let `Theta(M)` be its forced
Middle-Levels edge support.  It extends to a spanning 2-factor exactly when
the residual bipartite Middle-Levels graph has a `b`-factor with demand
`b(v)=2-deg_(Theta(M))(v)` at every vertex, equivalently a feasible ordinary
bipartite `b`-flow.  This subclass is subordinate to the forest-first theorem.

For `n>=4`, put `X_n=binom([2n],n)`, `N=binom(2n,n-1)`,
`P=binom(2n,n-2)`, and `C=Cat_(n+1)`.  On ground set `X_n`, let `T_down` be
the transversal matroid in which a family is independent when its members
inject into distinct contained `(n-2)`-sets; define `T_up` dually using
distinct containing `(n+2)`-sets.  For every `A subset X_n` with `|A|<=N`,
both duals satisfy `r(A)>=(C/N)|A|`.  Hence, for any `N`-element set `E` and
arbitrary injections `tau,eta:E->X_n`, the pullbacks of `T_up^*` along `tau`
and `T_down^*` along `eta` have a common `C`-element basis.  Moreover the
constant vector `C/N` lies in their common-base polytope, so common bases
admit a distribution with exact marginal `C/N` at every element.

Fix any such basis `Q`.  In the explicit two-coordinate lift, delete
`tau(Q)` from the upper central-owner shore and `eta(Q)` from the lower shore.
A selected physical Johnson edge may use each rank-`(n+2)` upper colour, each
rank-`(n-2)` lower colour, and each declared endpoint-capacity slot at most
once; ordinary owners have capacity two and owners incident with a deleted
basis port have capacity one.  Uniformly over `Q` as `n->infinity`, one can
select `P-o(P)` edges independently on each shore so that each projected
owner graph is a linear forest.  Deleting at most `2C=o(P)` edges incident
with deleted basis ports makes the union of the two attachment graphs
acyclic.  This is asymptotic and shore-by-shore: exact, rooted, no-empty, and
joint physicalization remain open.

Canonical references:

- `MATH_THEOREM_CATALAN_FOREST_SUPPORT_RADO_AND_FOURPARTITE_GATE_20260731.md`;
- `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
- `MATH_THEOREM_CATALAN_D2F_FACTOR_FLOW_AND_RELATIONAL_ROOT_20260731.md`;
- `MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`;
- `MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`.

In `ML(2m-1)` as defined above, every prescribed subgraph of maximum degree
two and at most `m-2` edges extends to a spanning 2-factor.  Separately,
`ML(2m+1)` denotes the rank-`m`/rank-`(m+1)` containment graph on `[2m+1]`.
Fix a coordinate `z` and a Hamilton cycle, retain its `z`-free vertices, and
for each retained rank-`(m+1)` vertex suppress it between its two cycle
neighbours.  The resulting Johnson edges form a `Cat_m`-path forest on the
`z`-free rank-`m` owners and use every `z`-free upper colour exactly once;
its endpoints are exactly the owners `X` whose vertical edge
`X--({z} union X)` belongs to the Hamilton cycle.  The `z`-containing half
gives the dual intersection-exact forest, not necessarily on the same edges.
Protected-subgraph extension and this half-projection theorem do not by
themselves provide a common two-shore forest or a compatible collar order.

In a colour-exact Catalan path forest in `J(2m,m)`—a spanning linear forest
whose rank-`(m-1)` intersection colours and rank-`(m+1)` union colours are
each used exactly once—every coordinate has `Cat_m` positive runs.  After `c`
component-merging Johnson seams the total coordinate-run count is
`2m Cat_m-(m-1)c`; a Hamilton path has `(m+1)Cat_m+m-1`.  At
`k=2m`, call the lower q1 colour of a Johnson adjacency `TH` its intersection
`T cap H`, and call a spanning path q1-complete when every rank-`(m-1)` colour
occurs.  If `mu_C` is its multiplicity, define repeat excess
`E=sum_C[mu_C-1]_+`.  Every q1-complete spanning path has
`E=Cat_m-1` (1,429 at `k=16`), so q1 rainbowness is the wrong target.  See
`MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md` and
`MATH_THEOREM_ZERO_DEFECT_PASCAL_PARTICLE_BRAID_INDUCTION_20260731.md`.

References:
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
and
`MATH_THEOREM_MIDDLE_LEVELS_HALF_PROJECTION_AND_BALANCED_COLLAR_DEPUNCTURING_20260805.md`.

### 5.3 Protected bridges, lower flags, and serialization

An owner-chain atom is a pair `(T,C)` where `T` is a rank-`r` owner and `C`
is an inclusion chain of nonempty strict subsets of `T`.  A fractional factor
assigns nonnegative weights `z_(T,C)` with total weight one at each owner and
total load one at every strict-lower target.  At
`d<=D=ceil(Lambda/W)<=d+1`, such a factor exists using chains of length at
most `D`.  With owner chains restricted to length `d`, add `d` boundary-chain
addresses of capacities `1,2,...,d`, each also of total weight one; then an
exact fractional factor still exists.  The STW-derived anchored construction
rounds the owner portion to an integral depth-`d` packing with leave—the
number of uncovered targets—`O(Lambda k^{-1/16+o(1)})`.  Constant-size
rounding of the full triangular factor and chronology are open.
See `MATH_THEOREM_FRACTIONAL_OWNER_CHAINIZATION_EXACT_DEPTH_DPLUS1_20260801.md`,
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`, and
`MATH_THEOREM_ASYMPTOTIC_SHARP_ANCHORED_CHAIN_FACTOR_FROM_STW_20260801.md`.

For `n=2m+1`, put `W=binom(n,m)`.  There is an explicit permutation `f` of
the `m`-sets (the canonical PBBS map) such that `g=f^2` has at most `Cat_m`
cycles.  Let `P_m` be the cycle cover on the complementary `(m+1)`-set
owners obtained by complement-projecting these `g`-cycles.  For
every `1<=q<=m` and every `(m-q)`-set `S`, some directed `q`-edge `g`-path
has vertex intersection `S`; the load (number of such directed paths) lies
between 1 and `binom(2q+1,q)`.  Fix `1<=H<m`, let `c` be the number of
`g`-cycles, and let `nu_H(P_m)` be the maximum number of projected-edge-
disjoint positive coordinate runs of length at most `H`.  If no such short
run exists, opening and collaring gives a literal word of length at most
`W+2Hc<=W+2H Cat_m`.  In general the proved bound is

\[
W+2H Cat_m+2(5H-1)\nu_H(P_m).
\]

Hence connectivity alone is not the missing gate; short coordinate runs and
common owner/Hall extension remain decisive
(`MATH_PBBS_FLAG_FACTOR_AND_FALSE_CONNECTOR_GATE_20260728.md`).

Call an order-`h` transition—`h` initial-state letters followed by `h+1`
appended letters—an `(h+1)`-owner pivot bridge when its `h+1` consecutive
length-`h+1` unions are distinct rank-`r` sets following a Johnson geodesic,
and the last `ell` letters of every owner window give a strict suffix target
for every `1<=ell<=h`.  For
`2<=h<=r-2` and `k>=r+h`, an explicit bridge exists and all `h(h+1)` suffix
targets inside it are distinct.  With `h=d(k)+1`, for all sufficiently large
`k`, sparse marking and
Turan--Caro--Wei select, outside any prescribed `o(W/(h+1))` owner set, exactly
`W/(r+1)-1` disjoint bridges for `k=2r` and
`Cat_(r-1)-1` for `k=2r-1`, while preserving a `1-O(1/(h+1))` fraction of every
containment star rooted at rank at most `r-h-1`.  Independently, for all
sufficiently large dimensions one can choose the same number of balanced
collars with disjoint owner/endpoint resources, disjoint adjacent-owner union
colours, and the same low-star spread.  The bridge and collar theorems do not
make their two banks compatible and do not construct the complementary
protected factor.

References:
`MATH_THEOREM_FULLY_FLAGGABLE_OVERLAPPING_CORE_PIVOT_BRIDGE_20260805.md`,
`MATH_THEOREM_SPARSE_MARKING_TURAN_SPREAD_PIVOT_BANK_20260805.md`, and
`MATH_THEOREM_JOINT_UPPER_DISJOINT_SPREAD_CATALAN_COLLAR_BANK_20260805.md`.

For lower-chain assignment, an instance declares a finite job set `J`, owners
`T`, a family `C_T` of nested job decks for each owner, named capacity-one
sockets used by each deck, and finitely many nonnegative price functions
`p_a(T,C)` with capacities `b_a`.  Its configuration LP has variables
`z_(T,C)>=0` and the explicit rows

\[
\sum_{C\in C_T}z_{T,C}=1,\qquad
\sum_{T,C:\,j\in C}z_{T,C}=1,\qquad
\sum_{T,C:\,s\text{ used}}z_{T,C}\le1,\qquad
\sum_{T,C}p_a(T,C)z_{T,C}\le b_a.
\]

The first two row families admit the exact fractional owner-chain factors
stated above, and the unconditioned birth-time distribution supplies their
weighted multi-rank Hall inequalities.  Once an upper order, residence, and
literal sockets are fixed, the socket and price rows are additional—not
automatic—constraints.  Selecting one integral deck per owner while meeting
all four row families is the actual configuration gate; scalar or Lorenz
projections do not replace it.  The carry-aware Bellman check is known only
for denominator grids of size at most three.

For residence, let a pairing `P` of `[2r]` split an owner
`T in binom([2r],r)` into `X_P(T)` cross-pairs.  If
`M=L+ceil(3 log_2 r)` for an integer sequence `1<=L=O(sqrt(r))`, then for
all sufficiently large `r` there are three pairings such that every owner has `X_P(T)>=M` in at
least one frame.  Each resulting `M`-dimensional pair cell is a cube with an
explicit Johnson Hamilton cycle whose repeated coordinate transitions are
at least `L` edges apart.  If whole pair cells of dimension at least `M`
partition the middle
layer, then `M<=s_2(r)`, the number of ones in the binary expansion of `r`.
Thus the residence-scale regime requires cut, residue-carrying proper blocks.
See `MATH_THEOREM_THREE_PAIRING_RESIDENCE_COVER_AND_SELECTOR_GATE_20260804.md`,
`MATH_THEOREM_COMPLEMENTARY_AGE_CROSS_STRATUM_COLLARS_20260804.md`, and
`MATH_THEOREM_PAIR_CELL_TWO_ADIC_SELECTOR_OBSTRUCTION_20260804.md`.

Once an upper-complete owner order `mathcal P` and a complete owner-rooted
strict lower-flag assignment `mathcal C`, a trace depth `h`, and admissible
left/right boundary `h`-tuples are fixed, let a layer-`j` state
record the last `h` source letters compatible with their first `j` prescribed
owners/flags, and join two states when the latter is obtained by deleting the
oldest letter and appending one legal new letter.  Sources are the legal
states matching the left boundary tuple and sinks those matching the right
boundary tuple.  A literal word with those fixed data exists exactly when
this layered order-`h` de Bruijn graph has a source--sink path.  Its unit-flow
matrix is totally unimodular.  Thus the remaining gap is not rounding after
`mathcal P,mathcal C` are fixed, but proving

\[
\exists\mathcal P\text{ upper-complete},\quad
\exists\mathcal C\text{ lower-complete},\quad
\text{layered-path}(\mathcal P,\mathcal C)
\]

in one occurrence state.

References:
`MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`,
`MATH_SYNTHESIS_FRACTIONAL_CONFIGURATION_TO_ZERO_DEFECT_ADJACENT_COLLAR_20260805.md`,
`MATH_THEOREM_ODD_ADJACENT_DEPTH_CAPACITY_D_ABSORBER_20260805.md`, and
`MATH_THEOREM_UPPER_FIRST_NAMED_COLLAR_LAYERED_TRACE_FLOW_20260805.md`.

### 5.4 Topology, parity, and regeneration

In a directed degree-one support, an alternating exchange confined to cycle
arcs preserves every vertex's in- and out-degree, so it remains a cycle cover
and cannot remove the last cycle.  Endpoint-bearing donor paths are necessary.
For one cycle and one donor path, support four is necessary, and an explicit
eight-edge Boolean exchange attains it and removes exactly one cycle.

An ordered two-SDR means two edge-disjoint bijections `M_0,M_1` from the same
owner set onto the same mate set, using only allowable incidences.  They
induce `rho=M_1^(-1)M_0` on owners.  An alternating
`C_(2 ell)` switch in one phase multiplies `rho` by an `ell`-cycle; hence a
`C6` switch is even and a `C8` switch is odd.  An explicit protected collar
provides the needed `C8`; closing its four protected paths uses `8m+24`
incidences, with exposure—the maximum number of protected incidences using
one shore resource—at most four.  For every `m>=12`
there is a spanning ordered two-SDR containing the prescribed bounded
actuator bank.  This proves the local parity actuator and large host, not
their joint realization with residence, component fusion, or common cap.

For an occurrence state `Z` and an admissible literal guard `Q`, let `H_Q`
be the bipartite graph whose left vertices are still-required targets, whose
right vertices are legal capacity-one cells, and whose edges are legal
target-to-cell assignments.  Put

\[
V_Q(Z)=\max_{X\subseteq L(H_Q)}(|X|-|N_{H_Q}(X)|),\qquad
V_*(Z)=\min_{Q\ \mathrm{admissible\ literal\ guard}}V_Q(Z).
\]

Along one fixed guard transition `(Z,Q)->(Z',Q')`, put `V=V_Q(Z)` and
`V'=V_(Q')(Z')`.  Relative to a transported maximum matching,
`V'=V+ell-kappa`, where `ell` matched cells are lost and `kappa` is the maximum
number of vertex-disjoint augmenting paths recovered.  Scalar `V` is not
compositional: the exact state is guard-indexed, and pairing-resolved when
sinks vary.

The exact conditional regeneration theorem is this.  Suppose a construction
transports the same typed interface state from dimension `n` to `n+1`, emits
a word of length at most `B(n)+a Phi_n+b` for fixed `a,b>=0`, and has a nonnegative potential
`Phi_n` and nonnegative coefficients `rho_n,beta_n`
satisfying `Phi_(n+1)<=rho_n Phi_n+beta_n`,
`Phi_(n_0) product_(i=n_0)^(n-1) rho_i=O(1)`, and

\[
\sup_n\sum_{j<n}\beta_j\prod_{i=j+1}^{n-1}\rho_i=O(1).
\]

If the displayed terminal allowance includes every parity-transfer charge
(in particular, any such charge is `O(1)`), then `nu(n)<=B(n)+O(1)`.  Uniform `rho_n<=rho<1` and
`beta_n=O(1)` are a sufficient special case.  No compatible protected system
meeting these hypotheses is known.

References:
`MATH_THEOREM_AD_FOUR_RESOURCE_CYCLE_INTERNAL_EXCHANGE_OBSTRUCTION_20260801.md`,
`MATH_THEOREM_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md`,
`MATH_THEOREM_K_EXACT_COMMON_CAP_DEFECT_AND_REGENERATIVE_LINKAGE_20260731.md`,
`MATH_THEOREM_K_MINIMAL_COMMON_GUARD_LINKAGE_STATE_AND_EXPLICIT_CONTRACTION_20260731.md`,
`MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`,
`MATH_THEOREM_ORDERED_TWO_SDR_CIRCUIT_SIGN_AND_COMMON_MATE_PARITY_GATE_20260812.md`,
and `MATH_THEOREM_COMMON_MATE_C8_ALLWIDTH_COLLAR_SPANNING_PHASED_HOST_20260812.md`.

### 5.5 Signed owner lattice and the remaining positivity gate

Fix an owner rank `R`, put `q=d+1`, `c=R-q`, and `M=k-c`, and assume
`d>=1`, `c>=1`, and `M-2>=2(q+1)`.  Let `mathcal L_residual` be the
strict-lower targets not already forced by the carrier.  A closed pure rail
chooses a `c`-set core, a toggle period `2(q+1)<=N<=M`, and a cyclic toggle
order; its named rank-`R` owners are the core plus the consecutive
`q`-windows of that order, and its occurrence state returns to its start.
Record each rail by its owner multiplicities, optional lower-target marks,
and its trace boundary (final occurrence state minus initial state, hence zero
for a closed rail).  Under the displayed hypotheses, the nonmaximal
pure-rail columns (those with `N<M`) generate the full integer owner lattice;
an annotation is genuinely optional when it can be toggled on the identical
physical rail without changing any compulsory row, and every such lower or
upper annotation splits off by a unit difference,
while every closed rail has trace boundary zero.  Therefore the displayed
projection is

\[
\mathbb Z^{\binom{[k]}{R}}\oplus
\mathbb Z^{\mathcal L_{\rm residual}}\oplus\{0\}.
\]

This is only a signed projection theorem.  It does not imply a nonnegative,
owner-disjoint factor or satisfy additional palette, residence, capacity, or
serialization constraints.

Define the point-incidence map by
`P_R e_A=1_A in Z^k` for each rank-`R` owner `A`.  For every named owner `H`,
there exists an explicit integral owner vector `Y_H` satisfying
`P_R Y_H=1_H`, so

\[
Z_H:=e_H-Y_H\in\ker P_R.
\]

If additionally `N=M-2`, `M>=c+2`, `c>q`, and
`binom(N,q)>2q(N+1)^2`, then

\[
Z_H=B^+-B^-,
\]

where `B^+` and `B^-` are genuine simple equal-size owner matchings with
identical point degrees.  No theorem yet lifts this signed residue to
nonnegative owner-disjoint collections of complete closed rails with identical
compulsory data.  Uniform degree
fibres can be disconnected under every switch of support below `R`, so generic
low-order switches do not suffice.  In one fixed legal core `C_core` of size
`c=R-q`, every pure-rail toggle degree is divisible by `q`; a complete core
fibre would
require

\[
q\mid {M-1\choose q-1}.
\]

At `k=17`, `q=4`, `M=12`, but `binom(11,3)=165`.  Therefore the complete
`q`-petal owner fibre over one fixed core cannot be partitioned independently
into pure rails.  This does not rule out incomplete fibres, other packet
families, or a global factor; a pure-rail proof using complete fibres must mix
overlapping cores before forming cyclic decks.

Reference: `MATH_SYNTHESIS_AUG12_INTEGRAL_LATTICE_REBASE_20260812.md` and the
August-12 theorem/audit family indexed in `RESEARCH_INDEX.md`.

### 5.6 Far-rank absorption, the run-length criterion, and central lifts

Let `n=2m+1`, `W=binom(n,m)=n Cat_m`, and `1<=H<=m-1`.
**Far-rank absorption.**  If a word of
length `L` realizes every target of ranks `m-H,...,m+1+H`, appending each
remaining nonempty target as one letter gives

\[
\nu(n)\le L+2\sum_{s=0}^{m-H-1}{n\choose s}-1
       \le L+2^{n+1}e^{-2(H+1)^2/n}-1.
\]

Thus the appended cost is `o(W)` whenever, for example,
`H>=(1/2+epsilon)sqrt(n log n)` for a fixed `epsilon>0`.  This is a
sufficient per-target-repair reduction, not an exact second-order threshold;
smaller `H` can still work if missing targets are repaired in batches.

**Run-length criterion.**  Feeding the proved PBBS collar ledger
(equation (2.2) of `MATH_PBBS_FLAG_FACTOR_AND_FALSE_CONNECTOR_GATE_20260728.md`)
into the absorption theorem gives, at `H=ceil(sqrt(n ln n))`,

\[
\nu(2m+1)\le W\bigl(1+2\sqrt{\ln n/n}\,(1+o(1))\bigr)
+2(5H-1)\,\nu_H(P_m)+O(Wn^{-3/2}).
\]

Consequently, if the canonical cover satisfied
`nu_H(P_m)=o(W/sqrt(n log n))` at that `H`, then
`nu(k)=(1+o(1))W(k)` for all `k` (even `k` via the top-bit splice and
`binom(2m+2,m+1)=2binom(2m+1,m)`).  It is not currently proved to satisfy
this hypothesis.  Counting many short candidate runs is not enough:
`nu_H` is an edge-disjoint packing number.  The criterion concerns the
unbatched PBBS ledger only and does not rule out one-mountain or other
batched repairs.

**Defective central covering.**  Put
`H=ceil(sqrt(n log n))`.  A `DCC(n,H,delta)` is a cyclic singleton word of
length at most `(1+delta)W` in which equal letters are at cyclic distance at
least `m+H+2`, and for which the number of rank-`ell` targets not realized by
clean length-`ell` windows, summed over `m-H<=ell<=m+1+H`, is at most
`delta W`.  Append the first `m+H` symbols to the cyclic word before opening
it; this costs `O(n)=o(W)` and preserves every cyclic band window as a linear
interval.  If `DCC(n,H,delta_n)` exists for every odd `n` with `delta_n->0`,
append its missed band targets and apply far-rank absorption.  This proves
`nu(k)=(1+o(1))W(k)` for all `k`.  The sufficient object does not require a
partition, thresholds, or exact multiplicities.

For calibration, a **doubly exact central cycle** is a cyclic singleton word
of length `W` whose clean `m`-windows and clean `(m+1)`-windows enumerate the
two middle layers.  It is equivalent to a Hamilton cycle
`U_1 subset V_1 supset U_2 subset ...` of `ML(2m+1)` satisfying

\[
b_j=a_{j-m},\qquad
a_j=V_j\setminus U_j,\quad b_j=V_j\setminus U_{j+1}.
\]

The forward direction reads entering and leaving letters from the windows.
Conversely, the shift identity and the conservation equation
`1_(x in U_(j+1))-1_(x in U_j)=1_(a_j=x)-1_(b_j=x)` imply that

\[
c_x=1_{x\in U_j}-\sum_{t=j-m}^{j-1}1_{a_t=x}
\]

is independent of `j`.  Hamilton coverage gives `c_x<=0`, while
`sum_x c_x=m-m=0`; hence every `c_x=0`.  Thus each entry remains for exactly
`m` owner steps, and the word `w_j=b_j` has the claimed windows.  Every
element occurs exactly `Cat_m` times and equal letters have gap at least
`m+1`.  This exact benchmark contains the central
Baranyai--Katona wreath/Chung--Diaconis--Graham difficulty and is much stronger
than DCC.

The published fixed-`k` near-Ucycle construction of Curtis--Hines--Hurlbert--
Moyer does not supply even the central middle row.  For `n=2m,k=m`, rooting a
uniform `m`-subset turns its cyclic gaps into a uniform composition of `2m`
into `m` positive parts, equivalently independent geometric variables
`Pr(X=r)=2^{-r}` conditioned on sum `2m`.  Their Euler tour lists precisely
the subsets whose gap multiset has some uniquely occurring part greater than
one.  A local-limit truncation proves that, for an absolute `delta>0`, the
conditioned composition has no uniquely occurring part with probability at
least `delta`; hence that cycle misses at least `delta binom(2m,m)` central
targets.  The later growing-`k` theorem reaches only `k=o(n)`.  A different
central near-Ucycle remains open, and even one would not automatically cover
the deeper band ranks (`CENTRAL_NEAR_UCYCLE.md`).

Finally, concatenate two permutation passes `sigma,sigma'`.  All `m-1`
seam-crossing `m`-windows are clean iff, for every letter `x`,

\[
\operatorname{age}_{\sigma}(x)+\operatorname{pos}_{\sigma'}(x)\ge m+1,
\]

where age is counted from the right of the first pass and position from the
left of the second.  A pass has only `m+2` internal `m`-windows, so a
near-`W` pass serialization must obtain `(1/2-o(1))W` fresh middle targets
from seam windows.  This is a window count; it does not say that almost every
whole seam is clean.

One further reduction is sound: if
`nu(p)=(1+o(1))W(p)` along the primes, then prime gaps `o(k)` and repeated
top-bit splicing imply the same asymptotic for every `k`.  This does not
construct the prime-dimensional words.

References:
`MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md`
(read with the corrections stated here) and
`MATH_THEOREM_PRIME_TRANSFER_AND_EQUIVARIANT_SUPPLY_20260820.md`.

### 5.7 The stationary eligible-walk plateau

Let a permutation `(c_1,...,c_n)` list letters from most to least recent.
Fix `sigma`, put `f=n-sigma` and `d=sigma+1`, and at each step choose
uniformly one position in `{f,...,n}`, record that letter, and move it to
position one.  This is the bottom-`d`-to-top shuffle.  Its stationary law is
uniform on `S_n`; the published shuffle bounds of Goel and Jonasson give a
polynomial total-variation mixing time when `sigma=o(n)`.

Assume `sigma>=C log n` for a sufficiently large absolute constant,
`sigma=o(n)`, and choose a rank `k` with
`d<=k<=f` and `log binom(n,k)>=c n` for a fixed `c>0`.  Start in stationarity,
put `M=binom(n,k)`, fix any constant `mu>0`, and observe
`L=ceil(mu M)` linear steps after discarding an initial `k-1` boundary steps.  For
a `k`-set `S`, let `X_S` count times at which the last `k` recorded letters
(equivalently, the top `k` recency set) equal `S`.  Then, for every fixed
integer `r>=1`, uniformly in `S`,

\[
\mathbb E(X_S)_{r}=\mu^r(1+o(1)),
\qquad X_S\Rightarrow\operatorname{Poisson}(\mu).
\]

For distinct `S,S'` and fixed `r,q`,

\[
\mathbb E (X_S)_r(X_{S'})_q=\mu^{r+q}(1+o(1)).
\]

Consequently the fraction of rank-`k` sets never observed converges in
probability to `e^{-mu}`.  This is a separate per-rank statement; it gives no
simultaneous rate over a growing band of ranks and no adaptive-rule theorem.
By itself it gives no closure, but Section 5.8 closes any realized path for
`o(W)` additional cost.

**Proof kernel.**  Stationarity gives hit probability exactly `1/M`.  Given
any history, the probability of a specified target window after a gap `g` is
at most

\[
\beta_g=\prod_{j=1}^{\min(g,k)}\frac{\min(j,d)}d.
\]

Equal targets cannot recur at gap below `f`.  Amplify the published bound to
`T=3n T_mix(1/4)`; submultiplicativity gives
`M dbar(T)=o(1)`, where `dbar` is worst-pair total-variation distance, and
`sum_{g<T} beta_g=o(1)`.  At gaps at least `T`, the conditional hit
probability is `1/M+o(1/M)`.  Splitting increasing
time tuples at their short gaps, the simplex count contributes
`L^{r-s}/(r-s)!`; this exactly cancels the factorial converting increasing
tuples to `(X)_r`, while every short gap contributes `o(1)`.  The same merged
tuple count gives the mixed moments.  Applying the one-variable Bonferroni
argument to `X_S+X_{S'}` gives uniform pair vacancy `e^{-2mu}+o(1)`, hence
variance `o(M^2)` for the number of missed sets.

The pure random eligible rule therefore leaves the constant miss plateau
`e^{-mu}` (in particular at the covering scale `mu=1+epsilon`).
Circularizing the observed word changes at most `k-1`
window observations, hence changes the normalized miss statistic by `o(1)`;
that observation alone does **not** prove a cyclic gap floor or return to the
recency state.  The exact bridge theorem in Section 5.8 now supplies both at
polynomial cost.  The plateau proves that pure uniform randomness alone is
insufficient, not that every coverage-oblivious or adaptive rule fails.

Two exact finite gap-window witnesses are frozen as construction data:

- `witnesses/n7_L56.txt`, length 56, cyclic gap at least 6, covering all
  rank-3, rank-4, and rank-5 subsets of `[7]`, SHA-256
  `ae1edfe3beb27df79ff2f4f052c1b19684eec6080fd75f8a2b6cee1610f2c9c6`;
- `witnesses/n9_L198.txt`, length 198, cyclic gap at least 8, covering all
  rank-4, rank-5, and rank-6 subsets of `[9]`, SHA-256
  `c4caf0c89520fc43172dd1a58874dc7a61bdd06cff7ea36b94f5a4e9f96944b4`.

`witnesses/verify_witness.py` (SHA-256
`a3433e2773f441dd3bbfe8e42cfbb84e80026ef744a8e48758af5282a962e061`)
replays both.  These finite data do not imply an asymptotic DCC family.

### 5.8 Exact tail-MTF bridges and the correlated-feedback barrier

Keep the tail-MTF notation of Section 5.7, with `1<=f<n`, and write `T_j`
for moving position `j` to the front.  The directed state graph has polynomial
diameter.  Indeed,

\[
T_j^j=I,
\qquad
T_{i+1}^{i}T_i=(i\ i+1)\quad(f\le i<n).
\]

Conjugating the transposition `(f f+1)` by powers of `T_f` supplies every
star transposition `(j f+1)`, `j<=f`; these star edges together with the tail
adjacencies form a spanning tree on the positions.  Leaf fixing therefore
joins any ordered pair of recency states by a legal directed word of length
less than `n^3`.  The identity loops `T_f^f` and `T_(f+1)^(f+1)` have coprime
lengths, so every ordered pair is joined at the common exact length

\[
R(n,f)=n^3+f^2.                                         \tag{5.8.1}
\]

Consequently every arbitrary `a`-step eligible prefix extends to any fixed
endpoint in exactly `R` more steps, giving `d^a` distinct fixed-endpoint
access words.  Conversely, among trajectories with the same initial state,
terminal state, and length at least `f`, the last `f` emitted letters are
forced; fixed-endpoint blocks of length at most `f` have no freedom.  For two
such trajectories of length `b` and any `k<=f`, at most
`max(0,b-f+k-1)` of their `b` post-move rank-`k` observations can differ.
The first universal switch occurs at length `f+1`: from
`(p_1,...,p_(f-1),q_1,...,q_d)`, the access words

\[
q_1,p_{f-1},...,p_1,q_1
\quad\hbox{and}\quad
q_2,p_{f-1},...,p_1,q_1
\]

have the same endpoint.  More generally the `d` words
`q_j,p_(f-1),...,p_1,q_1,...,q_d` have common length `n+1` and a common
endpoint.  Most importantly, any eligible trajectory can be returned to its initial state in
fewer than `n^3` steps.  Periodically repeating the closed operator word gives
a genuine cyclic singleton word in which equal letters have cyclic separation
at least `f`.  Thus one endpoint bridge or cyclic closure costs
`O(n^3)=o(W)`; for multiple localized blocks the total connector cost is
`sR`, controlled below by taking `a/R->infinity`.  These are no longer
asymptotic gates.  What remains is to
select one path from each exponentially large block palette with summed band
defect `o(W)`.

There is an exact obstruction to solving that selection problem by a
stationarity-preserving feedback kernel.  For `1<=k<=f`, put
`C_k(pi)={pi_1,...,pi_k}`.  The edge `pi->tau=T_j pi` has label

\[
\ell(\pi,j)=C_k(\tau).
\]

For an unseen family `U subset binom([n],k)`, put
`Omega_U={tau:C_k(tau) in U}`, `M=binom(n,k)`, and `rho=|U|/M`.  The
unseen-edge subgraph is exactly the union of all incoming fibers of
`Omega_U`; hence its maximum matching has size

\[
|\Omega_U|=k!(n-k)!|U|=\rho n!,                         \tag{5.8.2}
\]

and it has a perfect or fractional-perfect matching only when `U` is the
whole layer.  Every doubly stochastic eligible kernel has stationary unseen
mass exactly `rho`, because its column sums over `Omega_U` equal
`|Omega_U|`.  If `k<f`, define
`D_k(tau)={tau_2,...,tau_(k+1)}` and let `b(U)` count oriented Johnson edges
from the complement of `U` in `binom([n],k)` into `U`.  All eligible
predecessors of `tau` have old
color `D_k(tau)`, so the exact stationary covered-to-unseen mass is

\[
\frac{b(U)}{M k(n-k)}.                                  \tag{5.8.3}
\]

The corresponding covered-to-unseen subgraph has exact maximum matching
size `b(U)(k-1)!(n-k-1)!`.

More generally, if the conditional next-label law is within
`epsilon_t` in total variation of the uniform rank-`k` law, then its unseen
hit probability is at most `|U_t|/M+epsilon_t`.  Therefore, after
`L=mu M+O(1)` steps,

\[
\mathbb E|U_L|
 \ge M(1-1/M)^L-
 \sum_{t<L}(1-1/M)^{L-1-t}\mathbb E\epsilon_t.          \tag{5.8.4}
\]

Vanishing average conditional TV error leaves at least
`(e^(-mu)-o(1))M` expected misses.  A successful feedback construction must
therefore create and transport strong correlation between the recency state
and its coverage history.  More precisely, from an input state law `p`, a
doubly stochastic eligible kernel has unseen-hit probability at most
`rho+||p-Unif||_TV`; thus a separate kernel for each frozen `U` cannot beat
the coupon plateau from a uniform or approximately uniform conditional state.
For `0<rho<1` and `h in [rho,1]`, this is sharp: among input laws and doubly
stochastic eligible kernels, forcing one-step unseen-hit probability `h`
costs minimum conditional state displacement exactly `h-rho`.  This sharpness
construction does not impose that the current color is covered.

The exact multi-rank ledger identifies the additional correlation needed.
Fix a finite band-rank set `K` with `f>max K`.  At step `t`, let `E_t` be the
common eligible pool and let `S_(t,k,x)` be the rank-`k` window obtained by
choosing `x in E_t`, for `k in K`.  With `Z_(t,k)` the sets
unseen before step `t`, put

\[
b_{t,k,x}=1_{\{S_{t,k,x}\in Z_{t,k}\}},\quad
c_{t,k}=\sum_xb_{t,k,x},\quad h_{t,k}=1_{\{c_{t,k}>0\}}.
\]

Fix `I={t_0,...,T-1}`, weights `w_k>=0`, thresholds `J_k>=1`, and let
`a_I(S)` count offers to `S` while it remains unseen.  Set

\[
E_I=\sum_kw_k\#\{S\in Z_{t_0,k}:a_I(S)<J_k\},
\qquad v_k=w_k/J_k.
\]

Every common-letter schedule `x_t` obeys the weighted snub inequality

\[
\sum_kw_k|Z_{T,k}|\le E_I+C_I,
\qquad
C_I=\sum_{t\in I}\sum_{x\ne x_t}\sum_kv_kb_{t,k,x}.     \tag{5.8.5}
\]

Writing `A_(t,x)=sum_k v_k b_(t,k,x)`, this charge splits exactly into

\[
C_I=\sum_{t,k}v_k(c_{t,k}-1)_+
 +\sum_t\left(\sum_kv_kh_{t,k}-A_{t,x_t}\right).        \tag{5.8.6}
\]

The first term is within-rank crowding; the second is cross-rank **column
discordance**, minimized by choosing a column of maximum `A_(t,x)`.  Thus,
with `w_k=1`, aggregate low-offer mass, normalized crowding, and discordance
all `o(W)` are sufficient for summed band defect `o(W)`.  Separate per-rank late-access
estimates control only the first two.  Nested fans alone do not control the
third: an abstract current fan matrix can have one fresh entry in each of
`R<=min(|K|,|E_t|)` rows, all in different columns, giving zero crowd but
minimum discordance `R-1`.  This is a matrix obstruction, not a reachability
claim for a particular walk.

Finally, let `r->infinity`, `r=o(sqrt(n))`,
`K_r={m-r,...,m+1+r}`, and `R_r=2r+2`.  For a clean cyclic singleton word of
length `T=(1+epsilon_n)W`, where `epsilon_n=o(1)`, let `D_r` be its summed
miss count over `K_r` and
let `Q_r` count repeated step-rank windows.  Since
`binom(n,k)/W=1-O(r^2/n)` uniformly on `K_r`, exactly

\[
Q_r=R_rT-\sum_{k\in K_r}{n\choose k}+D_r.               \tag{5.8.7}
\]

Hence the exact `K_r`-defect target is excess repeats

\[
Q_r-\left(R_rT-\sum_{k\in K_r}{n\choose k}\right)=o(W),\tag{5.8.8}
\]

not merely `o(1)` repeat density.  It implies that at all but `o(T)` times
the chosen nested chain is fresh at `1-o(1)` of these ranks.  Since `U`
additional singleton steps remove at most `U` misses at any one fixed rank,
an `o(W)` terminal phase cannot repair the `(e^{-mu}+o(1))W` central-rank
defect of a typical stationary Poisson prefix of length `mu W`, for fixed
`mu>0`.  More sharply, if that prefix is followed by an arbitrary continuation
inside total length `(1+epsilon)W`, success with probability bounded away
from zero requires

\[
e^{-\mu}\le 1+\epsilon-\mu+o(1).                        \tag{5.8.9}
\]

For `epsilon=o(1)` this fails for every fixed `mu in (0,1]`.  This is
a probabilistic architecture obstruction, not a prohibition on exceptional
prefixes or feedback interleaved from the beginning.

References:
`MATH_CANDIDATE_TAIL_MTF_EXACT_BRIDGES_CYCLIC_CLOSURE_20260821.md`,
`MATH_CANDIDATE_STATIONARY_FEEDBACK_ENDPOINT_OBSTRUCTION_20260821.md`, and
`MATH_CANDIDATE_MULTIRANK_LATE_ACCESS_BARRIER_20260821.md`.

### 5.9 Exponential fixed-endpoint palettes have exact fractional balance

Let

\[
n=2m+1,\quad W={n\choose m},\quad
H=\lceil\sqrt{n\log n}\rceil,\quad
K=\{m-H,\ldots,m+1+H\},
\]

and put

\[
f=m+H+2,\qquad d=n-f+1=m-H,\qquad
R=n^3+f^2,\qquad A=\lfloor e^{n/5}\rfloor.             \tag{5.9.1}
\]

Thus `d<=k<f` for every `k in K`.  Fix cyclic skeleton states
`gamma_1,...,gamma_s`, with `gamma_(s+1)=gamma_1`.  A slot of core length
`a_i<=A` uses the legal sandwich

\[
\gamma_i\xrightarrow{R}\rho
\xrightarrow{a_i\text{ free moves}}\eta
\xrightarrow{R}\gamma_{i+1}.                           \tag{5.9.2}
\]

For each ordered state pair, fix one of the exact bridges supplied by
(5.8.1).  Its observations are ignored in the incidence ledger and can only
add coverage.  Both bridges are essential: the entry bridge permits a
uniformly varying seed `rho` despite the fixed state `gamma_i`, while the exit
bridge restores the prescribed next skeleton state.  A one-bridge block does
not justify both claims.  A core is **band-simple** if its `a_i` post-move
top-`k` sets are distinct for every `k in K`.

Choose the seed `rho` uniformly and each free move uniformly among the `d`
eligible positions.  Let `pi_t` be the core state after `t` free moves and
let \(\mathcal F_t\) be its natural history.  For `1<=k<f`, every
\(\mathcal F_u\)-measurable `k`-set `S`, and every `g>=1`, the protected
recency prefix gives

\[
\Pr(C_k(\pi_{u+g})=S\mid\mathcal F_u)
 \le\prod_{j=1}^{\min(g,k)}{\min(j,d)\over d}.           \tag{5.9.3}
\]

Moreover a top-`k` set cannot return at a positive gap below `f`.  Hence,
uniformly for integers `1<=b<=A`,

\[
\Pr(\text{a band collision})
 \le |K|{b\choose2}{d!\over d^d}
 \le\exp\{-n/10+o(n)\}=o(1).                           \tag{5.9.4}
\]

Conditioning on band-simplicity is therefore legitimate and remains
invariant under every relabeling of `[n]`.  If `M_k=binom(n,k)`, every fixed
rank-`k` target then occurs in a `b`-step core with exact probability
`b/M_k`.

This symmetry removes the fractional Hall/capacity problem completely.
Take `sum_i a_i=W` and augment the rank-`k` target part by `W-M_k` dummy
vertices, so every rank part has size `W`.  The augmented palette hypergraph
has one vertex for every slot and all vertices in these rank parts.  An edge
in slot `i` is one band-simple sandwich path (5.9.2), its slot vertex, and the
claimed real/dummy vertices described next.  Let the random dummy quota
`h_(i,k)` be one of the two integers bracketing
`a_i(W-M_k)/W`, with that mean; choose `h_(i,k)` dummies and
`a_i-h_(i,k)` of the distinct observed targets uniformly.  Each augmented
edge contains the slot vertex and exactly `a_i` vertices of every rank part.
Every real target and dummy has slot-`i` marginal exactly `a_i/W`; summing
over slots gives degree one.  Thus:

> **Exact fractional palette theorem.**  For all sufficiently large odd
> `n`, the full-band fixed-endpoint palette has a fractional perfect
> matching.  It is simultaneous across all ranks in `K`, uses one unit of
> mass in every slot.  With `s=ceil(W/A)`, all but possibly the last
> `a_i=A`, and the last chosen so that `sum_i a_i=W`, its physical length is
> `W+2sR=(1+o(1))W`.

At either middle rank there are exactly `W` real targets and no dummies.
Since `sum_i a_i=W`, equality of all fractional degrees forces every
positive-weight edge in slot `i` to claim `a_i` distinct middle targets.
Thus simplicity at the two middle ranks is necessary in this model; the
unconditioned core law is not itself a fractional perfect matching.

There is also a normalization whose physical length is at most `W`.  Set

\[
a=A,\qquad s=\left\lfloor{W\over a+2R}\right\rfloor,
\qquad N=sa,\qquad q=|K|=2H+2.                          \tag{5.9.5}
\]

Then `s(a+2R)<=W` and

\[
q(W-N)=o(W).                                            \tag{5.9.6}
\]

Indeed, if `L=s(a+2R)`, then

\[
0<W-N=(W-L)+2sR
 <a+2R+{2RW\over a+2R}.                                \tag{5.9.6a}
\]

Since `R=O(n^3)`, `a=exp(n/5+o(n))`, and
`W=exp((log 2)n+o(n))`, this proves both (5.9.6) and
`1-N/W=o(1/n)`.  The largest nonmiddle layer has ratio
`binom(n,m-1)/W=m/(m+2)=1-2/(m+2)`, so for large `n` only ranks `m,m+1`
have `M_k=W>N`; every outer band rank has `M_k<N`.

For an outer rank choose integer quotas

\[
0\le h_{i,k}\le\min(a,N-M_k),\qquad
\sum_{i=1}^s h_{i,k}=N-M_k,                            \tag{5.9.6b}
\]

which exist; choose them by distributing `N-M_k<=sa` as evenly as possible
among `s` bins of capacity `a`.
Augment that rank by `N-M_k` dummies.  In slot `i`, choose uniformly
`h_(i,k)` dummies and `a-h_(i,k)` of the `a` observed targets; at either
middle rank claim all `a` observed targets.  Since
`sum_i h_(i,k)=N-M_k` and `sum_i(a-h_(i,k))=M_k`, the same symmetric core
law gives degree exactly one to every outer real target and dummy, while
every middle target has degree `N/W`.  The total fractional real-target
deficit is therefore exactly

\[
2(W-N)=o(W).                                            \tag{5.9.7}
\]

This is a fractional near-factor, not a DCC: an integral selection of one
path in each slot with only `o(W)` real leave is still required.

The dependence profile makes that last distinction essential.  Clear the
rational weights of the canonical partition model above by one common
denominator, and let `Delta` be the resulting common degree of every vertex.
For `S in binom([n],m)` and `T in binom([n],m+1)` with `S subset T`,

\[
{\operatorname{codeg}(S,T)\over\Delta}
 ={4+o(1)\over n},                                     \tag{5.9.8}
\]

because a core of length `a_i` has `2a_i-1` forced same-time/one-step nested
incidences.  If `S,S'` are distinct real targets in either middle rank and
are Johnson-adjacent, meaning that they differ by exchanging one element,
then

\[
{\operatorname{codeg}(S,S')\over\Delta}
 ={8+o(1)\over n^2};                                   \tag{5.9.8a}
\]

a core has `a_i-1` forced consecutive Johnson adjacencies.  Relabeling
distributes these counts over respectively `W(n-m)` nested pairs and
`Wm(n-m)/2` Johnson edges.  For the canonical uniformly random free-core
law, the history bound (5.9.3), together with (5.9.4), gives normalized
codegree `O(n^(-2))` for every other pair of distinct real targets at either
middle rank.  This uniform theorem uses the actual random tail-MTF law; it
does **not** transfer to an arbitrary branch distribution inside one
common-transformation fiber.  For that later fiber law, Section 5.12 uses a
distance profile and obtains an all-pair bound at the matched central rank
only after antipodal deck pairs are removed.

The dummy lift has genuine entropy.  In the budget model put
`r_(i,k)=a-h_(i,k)` and, for a band-simple path in slot `i`, let

\[
Z_i=\prod_{k\in K\setminus\{m,m+1\}}
 {a\choose r_{i,k}}{N-M_k\choose h_{i,k}}              \tag{5.9.9}
\]

be its number of admissible outer-rank claim decorations.  With balanced
quotas in (5.9.6b), uniformly for every slot `i`,

\[
\log Z_i=(1-o(1))qa\log(N/a),                           \tag{5.9.9a}
\]

so the decoration entropy per edge coordinate is
`(log 2-1/5)n+o(n)`.  Thus the `Theta(1/n)` pair codegree is useful
adjacent-rank flag structure, not a fake degree or a same-rank resource
collision.

The total number of real band resources is

\[
T_K=\sum_{k\in K}{n\choose k}
 =\left(\sqrt{\pi n/2}+o(\sqrt n)\right)W.              \tag{5.9.10}
\]

Consequently an `o(W)` leave requires relative error `o(n^(-1/2))`, not
merely `o(1)`.  In the strongest applicable-looking higher-codegree nibble
bounds, if `Delta_2` is the maximum pair codegree, (5.9.8) forces the
accuracy parameter
`B<=sqrt(Delta/Delta_2)<=(1/2+o(1))sqrt(n)`.  Hence the smallest possible
unlogged leading upper-bound term `T_K/B` is `Omega(W)`, so those bounds do
not imply `o(W)` leave; their actual theorems also fix edge rank.  No standard
nibble, growing-uniformity,
conflict-free, rainbow, independent-transversal, or generic absorption
theorem currently rounds this palette.

This failure cannot be repaired from degree and pair-codegree data alone.
Let a projective plane of order `p` have `b=p^2+p+1` points and lines.  Take
an integer `c>=1`, a disjoint set `U` of size `bc`, put `t=c(p+1)`, and use all hyperedges
`ell dotcup F` with `ell` a projective line and `F in binom(U,t)`.  This
`(c+1)(p+1)`-uniform hypergraph is regular of degree

\[
D=(p+1){bc\choose t},
\]

has maximum normalized pair codegree `Theta(1/p)`.  Uniform edge weights give
a fractional perfect matching of value `b/(p+1)=Theta(p)`.  Yet every two lines meet, so every two
edges meet and the integral matching number is one.  A positive theorem must
use the Boolean flag and tail-MTF chronology; higher codegrees can distinguish
this example.

One diagnostic survives.  At a single middle rank, a linear centrally
chordless core with antipodal pairs removed has maximum normalized pair
codegree `O(n^(-2))`; the leading scale of a hypothetical growing-rank
higher-codegree theorem would then be `O(W/n)=o(W)`.  This is not an
application of any existing theorem.  Section 5.12 gives the exact result
that only this one middle rank must be matched initially; every other rank
may be postponed to a common-path graphic completion.

References:
`MATH_CANDIDATE_FIXED_ENDPOINT_PALETTE_FRACTIONAL_MATCHING_20260821.md` and
`MATH_AUDIT_FIXED_ENDPOINT_PALETTE_MATCHING_BLACKBOX_20260821.md`.

### 5.10 Parity projection is exact, but is not the sharp matching gate

This subsection records a useful exact transition-color theorem and its
fiber obstruction.  Its parity-matching hypothesis is sufficient but is no
longer necessary: Section 5.12 proves that matching the rank-`m` decks alone
is enough, with every other band rank postponed to graphic Hall completion.

Keep the fixed-endpoint palette notation of Section 5.9 and work in its
budget normalization:
`a=A`, `s=floor(W/(a+2R))`, and `N=sa`.  For the core selected in slot `i`
write

\[
\pi_{i,0}\longrightarrow\pi_{i,1}\longrightarrow\cdots
\longrightarrow\pi_{i,a},
\]

and retain as `pi_(i,a+1)` the state after the first step of its fixed exit
bridge.  Put `C_0(pi)=emptyset`.  For every indicated step
`1<=t<=a+1` and every `1<=k<f`, one legal move gives the exact identities

\[
C_{k-1}(\pi_{i,t-1})=C_k(\pi_{i,t-1})\cap C_k(\pi_{i,t}),
\qquad
C_{k+1}(\pi_{i,t})=C_k(\pi_{i,t-1})\cup C_k(\pi_{i,t}). \tag{5.10.1}
\]

Let

\[
P=\{k\in K:k\equiv m\pmod2\},\qquad Q=K\setminus P.  \tag{5.10.2}
\]

For slot `i`, rank `q in Q`, and `1<=t<=a`, define the transition color

\[
B_{i,q,t}=
\begin{cases}
C_{q-1}(\pi_{i,t-1})\cup C_{q-1}(\pi_{i,t}),
   &q-1\in K,\\
C_{q+1}(\pi_{i,t})\cap C_{q+1}(\pi_{i,t+1}),
   &q=\min K.
\end{cases}                                           \tag{5.10.3}
\]

The second case is the sole lower-boundary case and uses `pi_(i,a+1)` only
when `t=a`.  Equation (5.10.1) proves

\[
B_{i,q,t}=C_q(\pi_{i,t}).                              \tag{5.10.4}
\]

Thus, once the full path is selected, every `Q`-rank observation is an exact
transition color of its ordered `P`-rank traces, using the `P`-rank boundary
sets at `t=0` and, solely for the lower-boundary formula, at `t=a+1`.  These
ordered traces plus boundary sets are stronger data than the unordered
claimed-resource projection considered below.  For a band-simple core put

\[
U_{i,q}=\{B_{i,q,t}:1\le t\le a\},\qquad |U_{i,q}|=a. \tag{5.10.5}
\]

For its quotas write `r_(i,q)+h_(i,q)=a`; at an outer rank they satisfy
`sum_i r_(i,q)=M_q` and `sum_i h_(i,q)=N-M_q`, while at a middle rank
`h_(i,q)=0`.  Dummy labels are universal within their rank part and are
partitioned among slots according to the `h_(i,q)` quotas.  Suppose one
common path has been selected in every slot and its `P`-rank claims are
pairwise distinct: every outer `P` real/dummy part is fully covered, while
the middle `P` rank has `N` distinct real claims.  At a
fixed `q in Q`, the remaining decoration is the bipartite `b`-matching from
slot `i`, with demand `r_(i,q)`, to the targets in `U_(i,q)`.  Defect Hall
gives its exact deficiency

\[
\begin{aligned}
\delta_q
 &=\max_{I\subseteq[s]}
   \left(\sum_{i\in I}r_{i,q}
     -\left|\bigcup_{i\in I}U_{i,q}\right|\right)_+\\
 &=\max_{I\subseteq[s]}
   \left(a|I|-\left|\bigcup_{i\in I}U_{i,q}\right|
     -\sum_{i\in I}h_{i,q}\right)_+.                 \tag{5.10.6}
\end{aligned}
\]

This follows by cloning slot `i` exactly `r_(i,q)` times; a maximum-defect
clone set contains every clone of each represented slot.  Distinct `q`
ranks then decouple.  Define **leave** as the number of unused real targets
and **collision** as `sum_T(load(T)-1)_+` over real targets.  After a maximum
matching, fill each unmatched clone with a further target in its own
`U_(i,q)`, distinct from every other claim made by that slot; this is possible because
`r_(i,q)<=|U_(i,q)|=a`.  Fill the universal dummy sets by their quota
partitions.  Each outer omitted rank then contributes at most `2delta_q`;
the omitted middle rank contributes at most `W-N+2delta_q`; and the matched
parity contributes only its middle leave `W-N`.  Therefore

\[
\text{claimed real-resource leave}+
\text{claimed real-resource collision}
 \le 2(W-N)+2\sum_{q\in Q}\delta_q.                   \tag{5.10.7}
\]

Consequently a `P`-resource matching with

\[
\sum_{q\in Q}\delta_q=o(W)                            \tag{5.10.8}
\]

gives the **same paths** a full-band claimed-resource selection with `o(W)`
total defect.  Their cyclic singleton concatenation is therefore a
`DCC(n,H,o(1))`; Section 5.6 then appends its missed band targets and the far
ranks to obtain a universal word of length `(1+o(1))W`.  This is an exact
sufficient theorem, not a heuristic two-parity coupling.

At the central omitted rank `q=m+1` there are no dummies, duplicate mass is
monotone in the slot family, and (5.10.6) becomes

\[
\delta_{m+1}
 =N-\left|\bigcup_iU_{i,m+1}\right|.                  \tag{5.10.9}
\]

If `A_(i,t)=C_m(pi_(i,t))`, then

\[
U_{i,m+1}=\{A_{i,t-1}\cup A_{i,t}:1\le t\le a\}.     \tag{5.10.10}
\]

The central gate is therefore precisely an almost-rainbow union-color
condition on queue-coherent middle-level paths.  It is not automatic from
the fractional marginals: independent symmetric slot samples miss

\[
W(1-a/W)^s=(e^{-1}+o(1))W                              \tag{5.10.11}
\]

central colors in expectation: a fixed target has absence probability
`(1-a/W)^s`, while `a/W=o(1)` and `N/W=sa/W->1`.  In fact
`E delta_(m+1)=N-W+W(1-a/W)^s=(e^(-1)+o(1))W`.  Nor is
the assumed `P`-resource matching currently known to imply (5.10.8).

There is also almost no post-selection fiber in the canonical palette.  Fix
`1<=k<f`; for one slot suppress `i`, write `C_k(t)=C_k(pi_(i,t))`, and let
`x_t` be the letter moved at core step `t`.
For `2<=t<=a`,

\[
C_k(t)\setminus C_k(t-1)=\{x_t\};                     \tag{5.10.12}
\]

these differences recover `x_2,...,x_a`.  In the budget model `a=A>=k`.
If `k=1`, then `C_1(1)={x_1}`.  If `k>=2`, the `k-1` removed-letter
differences `C_k(t-1)\setminus C_k(t)`, `2<=t<=k`, identify every other member
of `C_k(1)` and hence recover `x_1`.  Thus the time-labelled trace recovers
the emitted core word.  It fixes every lower-rank trace; for `k<ell<f`, it
fixes `C_ell(t)` whenever `t>=ell-k+1`, leaving only the first `ell-k`
observations boundary-dependent.

For a simple unordered rank-`k` deck
\(\mathcal P_k=\{C_k(t):1\le t\le a\}\), let

\[
\chi_k=e(J(n,k)[\mathcal P_k])-(a-1)                  \tag{5.10.13}
\]

count its non-temporal Johnson chords, where `J(n,k)` joins two `k`-sets
whose symmetric difference has size two.  The temporal pairs form a
Hamilton path in the induced graph.  Any other legal band-simple chronology
of the same unordered deck uses at most `chi_k` edges outside that path, so
(5.10.1) shows that each adjacent-rank deck lying in `K` changes by at most
`chi_k+1` target replacements.

The central decks are overwhelmingly chordless.  If `2<=g<k<f` and two
rank-`k` windows at lag `g` are Johnson-adjacent, matching their `g-1`
common exiting/entering letters, and writing `i_0,j_0` for the unmatched
exit and entry positions, gives

\[
(g-1)(f-k)\le i_0-j_0\le g-1;                         \tag{5.10.14}
\]

hence necessarily `k=f-1`.  This excludes all short chords at
`k=m,m+1`.  For a long gap `g>=k`, (5.9.3) bounds each fixed endpoint target
by `d!/d^d`; summing over its `k(n-k)` Johnson neighbors and conditioning on
band-simplicity gives, for the budget length `a=A`,

\[
\Pr(\chi_k>0\mid\text{band-simple})
 \le(1+o(1)){a\choose2}k(n-k){d!\over d^d}
 \le\exp\{-n/10+o(n)\}=o(1).                          \tag{5.10.15}
\]

The identical estimate holds with `a` replaced by every core length
`1<=b<=A`, and it holds simultaneously for `k=m,m+1` by a union bound.
Conditioning the band-simple core law also on
`chi_m=chi_(m+1)=0` is relabeling-invariant, and therefore preserves every
exact target marginal and both fractional theorems of Section 5.9.  On this
support, fixing one slot's unordered claimed-resource projection on either
parity fixes its whole middle-rank deck; the opposite central deck can then
differ by at most one boundary target.  Over `s=O(W/A)` slots, slotwise
fiber switches can replace only `o(W)` opposite-central targets.  The
explicit common-endpoint diamonds do not evade this: a diamond begun after
an already recorded core state repeats that state's top-`(f-1)` target after
`f` moves.  One gadget may begin at the unrecorded initial boundary, but
such gadgets cannot be tiled internally in a band-simple core.

Thus this subsection rules out post hoc slotwise parity repair on the
canonical chordless support.  Rare deliberately chorded cores and global
recomposition remain possible.  The current exact integral target is the
strictly weaker one-central/graphic theorem in Section 5.12, not a matching
of all ranks in `P`.

References:
`MATH_CANDIDATE_PARITY_PROJECTION_HALL_REDUCTION_20260821.md` and
`MATH_CANDIDATE_PARITY_FIBER_RIGIDITY_20260821.md`.

### 5.11 Scalar residual sizes cannot support a universal greedy proof

The palette also has an exact adversarial-residual barrier.  Fix a core
length `a<=min_(k in K) binom(n,k)`, integer real claim quotas
`0<=r_k<=a`, and residual densities `0<=delta_k<=1`.  Put
`M_k=binom(n,k)` and let

\[
\mathsf H(M,a,\delta,r)
 =\Pr\{X\ge r\},                                      \tag{5.11.1}
\]

where `X` is hypergeometric with a population of size `M`, exactly
`floor(delta M)` marked elements, and sample size `a`.  There are at most
`n!d^a` seed-labelled free cores.  Therefore, if

\[
n!d^a\prod_{k\in K}\mathsf H(M_k,a,\delta_k,r_k)<1,   \tag{5.11.2}
\]

then there exist residual families
`U_k subseteq binom([n],k)` with
`|U_k|=floor(delta_k M_k)` such that no band-simple core contains `r_k`
members of every `U_k`.
Indeed, choose the `U_k` independently and uniformly; a fixed simple core
has exactly the product hypergeometric success probability, and a union
bound proves (5.11.2).

If `p=r/a>delta'=floor(delta M)/M`, sampling-without-replacement Chernoff
gives

\[
\mathsf H(M,a,\delta,r)\le e^{-aD(p\|\delta')},       \tag{5.11.3}
\]

where

\[
D(p\|q)=p\log{p\over q}+(1-p)\log{1-p\over1-q}.
\]

Use the standard continuous boundary conventions at `0` and `1`.

Put `delta'_k=floor(delta_k M_k)/M_k`.  Thus a sufficient killing condition
is

\[
\sum_{k:r_k/a>\delta'_k}D(r_k/a\|\delta'_k)
 >\log d+{\log(n!)\over a}.                           \tag{5.11.4}
\]

This condition becomes nonvacuous extremely early.  Suppose
`n^3=o(a)`, `a<=e^(n/5)`, `N=sa<=W`, `N=(1-o(1/n))W`, and use the balanced real
quotas `r_k/a=M_k/N+O(1/a)`, with quota `a` at both middle ranks.  For

\[
x=Cn^{-1/3}(\log n)^{2/3},\qquad \delta_k=1-x,         \tag{5.11.5}
\]

take the `2J` ranks at distance at most
`J=floor(sqrt(nx)/16)` from the middle.  If
`p_j=binom(n,m-j)/W`, then for all sufficiently large `n` and
`1<=j<=J`,

\[
1-p_j\le-\log p_j\le {8j(j+1)\over n}.                \tag{5.11.5a}
\]

The symmetric ranks `m-j,m+1+j` therefore have quotas satisfying
`r_k/a>=1-x/4`, and

\[
D(1-x/4\|1-x)\ge {3-\log4\over4}x.                   \tag{5.11.6}
\]

For the exact residual density
`delta'_k=floor((1-x)M_k)/M_k<=1-x<r_k/a`, binary
relative entropy increases in its first argument above `1-x` and decreases
in its second argument below `r_k/a`.  Hence (5.11.6), together with
`r_k/a>=1-x/4`, also lower-bounds `D(r_k/a||delta'_k)`.

Hence the left side of (5.11.4) is
`Omega(sqrt(n)x^(3/2))=Omega(C^(3/2)log n)`, which beats
`log d+log(n!)/a` for large constant `C`.  There are therefore residual
families of density `1-x+o(1)` at every rank for which no next balanced core
exists.

This is a method barrier, not a no-go for the palette.  The adversarial
families need not be reachable after a partial matching.  The theorem says
that residual cardinalities or independent pseudorandomness alone cannot
justify a one-pass greedy extension; a successful proof must maintain a
strong cross-rank invariant or use global augmentation.

For completeness, ordered-trace rigidity has the quantitative full-band
form used by this diagnosis.  Fixing an ordered rank-`m` trace leaves at most

\[
\sum_{\ell=m+1}^{m+1+H}(\ell-m)=O(H^2)                \tag{5.11.7}
\]

core observations undetermined.  Across `s=(1+o(1))W/a` cores this is
`O(WH^2/a)`.  Variable bridge observations add at most
`O(|K|sR)=O(W|K|R/a)`.  Thus the whole-word postprocessing fiber is `o(W)`
when `a>>|K|R`, in particular for `a=A`; under only `a>>n^3`, the first bound
remains a core-ledger statement.  Neither bound applies to global
recomposition that changes the selected central traces.

Reference:
`MATH_CUSTOM_PALETTE_ROUNDING_RESIDUAL_AND_FIBER_BARRIERS_20260821.md`.

### 5.12 Adaptive quotas collapse the integral gate to simultaneous union coverage

Retain the odd-dimensional palette notation

\[
n=2m+1,\quad W={n\choose m},\quad
H=\lceil\sqrt{n\log n}\rceil,\quad
K=\{m-H,\ldots,m+1+H\},
\]

with eligibility floor `f=m+H+2` and `d=n-f+1=m-H` legal tail-MTF
moves.  The results below strictly weaken both the parity-matching target of
Section 5.10 and the later one-central/fixed-quota target.  The decisive
point is an order of quantifiers: after the **bare physical paths** have
been selected, real-versus-dummy claim quotas are only bookkeeping and may
be chosen from the complete observed decks.  This postselection does not
alter the fixed-quota fractional palette or any of its degree/codegree
calculations.

#### Exact postselected Hall theorem

Fix one rank with an `M`-element real-target universe.  Let
`U_1,...,U_b` be arbitrary `a`-element decks, put

\[
A=ab,\qquad V=\left|\bigcup_{i=1}^bU_i\right|,
\]

and choose an integer `0<=R<=min(A,M)`.  Only after all decks are known,
choose real and dummy quotas

\[
r_i+h_i=a,\qquad \sum_i r_i=R,\qquad \sum_i h_i=A-R. \tag{5.12.U1}
\]

For fixed quotas the real-clone Hall deficiency is

\[
\delta(r)=\max_{I\subseteq[b]}
 \left(\sum_{i\in I}r_i-
 \left|\bigcup_{i\in I}U_i\right|\right)_+.        \tag{5.12.U2}
\]

Then the exact postselection optimum is

\[
\boxed{\min_r\delta(r)=(R-V)_+.}                    \tag{5.12.U3}
\]

To prove it, first note that all `V` union targets can be assigned to
containing blocks with capacity `a`: for every target family `X`,
`|X|<=a|N(X)|` because
`X subseteq union_(i in N(X)) U_i`, so capacitated Hall applies.  Retain
`min(R,V)` assignments and let `c_i<=a` be the number assigned to block
`i`.  If `R<=V`,
take `r_i=c_i`; this explicitly matches every clone.  If `R>V`, first
assign all `V` union targets and distribute the remaining `R-V` clones
under the residual capacities `a-c_i`, whose sum is `A-V>=R-V`.  This
constructs deficiency at most `R-V`, while the full-block Hall cut gives
the reverse inequality.  Thus no subset-Hall or graphic obstruction remains
after quota postselection; the actual real-target leave is
`M-V=(M-R)+(R-V)` when `V<=R`.

#### Exact all-rank union-cover criterion

Choose `b` band-simple legal microblocks which, with their checkpoints,
bridges, and collars restored, form a cyclic singleton word of physical
length `W+o(W)` and cyclic equal-letter gap at least `f`.  After omitting
the already charged boundary observations, let every retained rank-`q`
deck be `U_(i,q)` of size `a`, let `B_ch` be their total omitted
rank-incidence charge, put `A=ab`, and define

\[
M_q={n\choose q},\qquad R_q=\min(A,M_q),\qquad
V_q=\left|\bigcup_iU_{i,q}\right|.                 \tag{5.12.U4}
\]

If

\[
\sum_{q\in K}(R_q-V_q)=o(W),\qquad
\sum_{q\in K}(M_q-R_q)=o(W),\qquad B_{\rm ch}=o(W), \tag{5.12.U5}
\]

then the word is `DCC(n,H,o(1))`, and the opening/far-rank theorem of
Section 5.6 gives `nu(n)=(1+o(1))W`.  Indeed (5.12.U3), applied rank by
rank, gives claimed-resource collision plus leave at most

\[
\sum_{q\in K}\bigl((M_q-R_q)+2(R_q-V_q)\bigr)=o(W), \tag{5.12.U6}
\]

with the last condition absorbing the omitted incidence ledger.  In the
one-checkpoint-per-block normalization it follows from `|K|b=o(W)`.
More directly, the exact missed-band identity is

\[
\sum_{q\in K}(M_q-V_q)
=\sum_{q\in K}(M_q-R_q)+\sum_{q\in K}(R_q-V_q)
=o(W).                                                \tag{5.12.U7}
\]

Ignored physical observations can only add coverage, so (5.12.U7), the
length bound, and the cyclic gap are precisely the DCC hypotheses.  This
criterion assumes no pre-matching at any rank.

There is an exact first-order process ledger.  Order the blocks, let
`u_(i,q)` be the number of targets of `U_(i,q)` not seen earlier at rank
`q`, and put `x_(i,q)=a-u_(i,q)`.  Since `R_q=min(A,M_q)>=V_q`,

\[
R_q-V_q=\sum_i x_{i,q}-(A-R_q).                     \tag{5.12.U8}
\]

Thus `A-R_q` is exactly the unavoidable repeat allowance supplied by
dummies; every old-target hit beyond it is union deficit.  The sharp live
postselection problem is to make the sum of (5.12.U8) over the full band
`o(W)` on one cyclic physical trajectory.  Quenched pair bounds,
component-square control, and pre-matching one rank are possible sufficient
methods, not additional necessary gates.

Reference:
`MATH_THEOREM_POSTPONED_GRAPHIC_COALESCENT_AND_DECOUPLING_GATE_20260821.md`.

#### Neutral decks have exact coupon loss

Let `U_1,...,U_b` be adapted random `a`-subsets of an `M`-set.  If for
every target `x` and complete past `F_(i-1)`, almost surely

\[
\Pr(x\in U_i\mid\mathcal F_{i-1})={a\over M},       \tag{5.12.U9}
\]

then the expected number of missed targets is exactly

\[
M\left(1-{a\over M}\right)^b.                      \tag{5.12.U10}
\]

For a fixed target, iterate the conditional avoidance probability
`1-a/M`, then sum over targets.  When `ab/M->1` and `a=o(M)`, (5.12.U10)
is `(e^(-1)+o(1))M`.  If the decks are mutually independent, changing one
deck changes the union size by at most `a`; bounded differences then makes
the miss count concentrate at this value whenever `b=(1+o(1))M/a` and
`a->infinity`.  Conditional neutrality alone gives only the expectation and
does not exclude an exceptional correlated realization.

#### A fixed-quota one-central sufficient route

Suppose `b` band-simple legal microblocks have been selected.  After discarding one
already charged checkpoint per block, let every block retain `a`
post-move observations at every rank, let `B_ch` be the total number of
discarded rank-incidences, put `A=ba`, and define its rank-`k`
deck

\[
U_{i,k}=\{C_k(\pi_{i,t}):1\le t\le a\},\qquad |U_{i,k}|=a. \tag{5.12.1}
\]

Assume `A<=W` and
`M_k=binom(n,k)<=A` for every rank `k in K` other than `m,m+1`.
This is the fixed-quota normalization used in
this route; it is stronger than the adaptive formulation (5.12.U4).

At `k=m,m+1` take real quota `a` and no dummies.  At an outer rank, where
`M_k=binom(n,k)<=A`, choose integers

\[
r_{i,k}+h_{i,k}=a,\qquad
\sum_i r_{i,k}=M_k,\qquad
\sum_i h_{i,k}=A-M_k,                                \tag{5.12.2}
\]

and augment by the corresponding universal dummy labels.  Once the paths
are fixed, the exact real-target Hall deficiency is

\[
\delta_k=\max_{I\subseteq[b]}
 \left(\sum_{i\in I}r_{i,k}
       -\left|\bigcup_{i\in I}U_{i,k}\right|\right)_+. \tag{5.12.3}
\]

If the rank-`m` decks are pairwise disjoint, the other ranks can be
decorated so that retained claimed-resource collision plus leave is at
most

\[
2(W-A)+2\sum_{k\in K\setminus\{m\}}\delta_k.          \tag{5.12.4}
\]

Indeed rank `m` leaves exactly `W-A`; defect Hall matches all but
`delta_k` real clones at rank `k`, and filling the unmatched clones inside
their own decks creates at most `delta_k` collision and at most
`delta_k` leave.  The other middle rank contributes the second baseline
`W-A`; dummies are partitioned according to (5.12.2).  Restoring
`B_ch` discarded rank-incidences adds at most `B_ch` to the charged ledger.
Thus it is enough that

\[
W-A=o(W),\qquad B_{\rm ch}=o(W),\qquad
\sum_{k\in K\setminus\{m\}}\delta_k=o(W).             \tag{5.12.5}
\]

No matching at any other rank, including ranks of the parity of `m`, is
required before this completion.

#### Fixed-quota Hall deficiency is excess cycle rank

Temporally join consecutive members of each `U_(i,k)` into an
`(a-1)`-edge path.  For `I subseteq[b]`, let `Gamma_k(I)` be the union
multigraph of these paths, with `g_k(I)` connected components and
cyclomatic rank

\[
\beta_k(I)=|E(\Gamma_k(I))|-|V(\Gamma_k(I))|+g_k(I).
\]

Writing `h_k(I)=sum_(i in I)h_(i,k)`, direct substitution into
(5.12.3) gives the exact identity

\[
\delta_k=
\max_{I\subseteq[b]}
 \bigl(\beta_k(I)+|I|-g_k(I)-h_k(I)\bigr)_+.          \tag{5.12.6}
\]

Add to each temporal path one private auxiliary root joined to its first
target.  The root is a graphic-matroid device, not a physical observation
or palette resource.  Rado's theorem gives the exact graphic quota
deficiency

\[
\epsilon_k=max_{I\subseteq[b]}
 \bigl(\beta_k(I)-h_k(I)\bigr)_+,qquad
\epsilon_k\le\delta_k\le\epsilon_k+b.                \tag{5.12.7}
\]

Hence pairwise-disjoint rank-`m` decks, the first two conditions in
(5.12.5), and

\[
\sum_{k\in K\setminus\{m\}}\epsilon_k=o(W),\qquad
|K|b=o(W),                                            \tag{5.12.8}
\]

prove (5.12.5).  Tree-like overlap is free up to the additive `b` boundary
term per rank in (5.12.7); beyond it, only cycle rank exceeding the dummy
allowance is charged.  The canonical fractional transition-edge
vectors lie in the corresponding graphic truncation base polytopes at
every postponed rank, jointly with the fractional resource law of Section
5.9.  Thus there is no detached fractional graphic obstruction.  This does
not choose whole legal paths: ordinary spanning-tree or negatively
correlated edge rounding has exponentially too little positive cylinder
mass to contain even one complete palette block.

There is also an exact sequential form.  Let `F` be the forest retained
from earlier augmented paths, let `E` be the next augmented deck path, and
for every old component `C` it meets put `z_C=|V(E) cap V(C)|`.  Then

\[
\kappa(E\mid F)=\sum_C(z_C-1)_+,qquad
\beta(F\cup E)=\kappa(E\mid F).                       \tag{5.12.9}
\]

After block `i`, delete exactly `kappa_(i,k)` new edges to keep a forest.
It follows that

\[
\epsilon_k\le
 Z_k:=\sum_i(\kappa_{i,k}-h_{i,k})_+,qquad
\delta_k\le Z_k+b.                                   \tag{5.12.10}
\]

This is the local statistic a custom nibble must control.

For `a=Theta(n)` there is a precise conditional sufficient theorem.  If,
given the complete past, the next-path law preserves the rank-`m`
packing and for every postponed rank satisfies

\[
\Pr(S,T\in U_{i,k}\mid\text{past})
 \le {C\Lambda_n a\over M_kn^2}\quad(S\ne T),
\qquad
\sum_{C\in\operatorname{comp}(F_{i-1,k})}|C|^2
 \le C'M_ka,                                         \tag{5.12.11}
\]

where `|C|` counts real target vertices; the private roots are auxiliary.
Then

\[
\mathbb E\sum_{i,\,k\in K\setminus\{m\}}\kappa_{i,k}
 =O\!\left({W|K|\Lambda_n\over n}\right)=o(W)       \tag{5.12.12}
\]

whenever `|K|Lambda_n=o(n)`.  The proof is the pair bound
`(Z-1)_+<=binom(Z,2)` summed over forest components.  Neither conditional
pair control nor the component-square invariant in (5.12.11) is known;
annealed codegrees do not imply them after coverage conditioning.

#### Common endpoints give entropy but force a reverse suffix

Let `T_f,...,T_n` be the position-to-top generators.  A length-`ell`
generator word acts on positions by a permutation `sigma in S_n`,
independently of seed labels.  For every fixed `C>1` and
`ell=ceil(Cn)`, pigeonholing the band-simple words by `sigma` produces a
common-transformation family `G_ell` with

\[
|\mathcal G_\ell|\ge{(1-o(1))d^\ell\over n!},\qquad
\log|\mathcal G_\ell|
 \ge(C-1)n\log n-Cn\log2+n-o(n\log n).               \tag{5.12.13}
\]

It may simultaneously be made chordless at both middle ranks.  All its
branches have the same full-state endpoint from every seed.  If `h` is the
order of `sigma`, then

\[
h=\exp(O(\sqrt n\log n))=e^{o(n)},                   \tag{5.12.14}
\]

so `h` arbitrary branches form a branch-independent identity backbone.

This entropy represents genuine deck mobility, not merely many names for
one trace.  After deleting the branch-independent final checkpoint, one
may select representatives in the same fixed-endpoint fiber whose retained
rank-`m` decks have pairwise replacement distance `Omega_C(n)` and whose
number is `exp(Omega_C(n log n))`.  With
`ell=Theta(n log n)`, the code has size
`exp(Omega(n(log n)^2))` and distance `Omega(ell)`.  The estimate is only a
packing in deck space: it gives neither a prescribed residual hit nor a
directional decrease of graphic cycle rank.

There is, however, an exact endpoint obstruction which the entropy count
does not see.  Write a state most-recent first as
`pi=(pi_1,...,pi_n)`, let a legal word have states
`pi_0,...,pi_ell`, and put `eta=pi_ell`.  Reversing a move from a position
at least `f` shifts the first `f-1` entries left.  Hence, for every `k<f`
and `0<=s<=min(ell,f-k)`,

\[
C_k(\pi_{\ell-s})=
 \{\eta_{s+1},\ldots,\eta_{s+k}\}.                  \tag{5.12.15}
\]

Thus the final `min(ell,f-k)+1` rank-`k` observations are functions of the
endpoint alone (and there are `f-k+1` when `ell>=f-k`).  If
common-transformation blocks are repeated without a seed-changing
bridge, their endpoints have period at most `h=ord(sigma)=e^{o(n)}`.
After deleting only the endpoint, every retained rank-`m` deck still
contains a forced target of this period, so pairwise-disjoint decks can use
at most `h` slots, versus `W/ell=e^{Theta(n)}` required slots.  The earlier
one-checkpoint matching interpretation is therefore false.

The exact forced ledger across the full band is

\[
\sum_{k\in K}(f-k)={(2H+2)(2H+3)\over2}.            \tag{5.12.15a}
\]

Deleting the final

\[
q(K_0)=1+\max_{k\in K_0}(f-k)                       \tag{5.12.15b}
\]

observations of each block removes the whole endpoint-determined suffix for
the rank set `K_0`; this is minimal for that purpose.  Thus
`q({m})=H+3` and `q(K)=2H+3`.  With `W/ell` repeated blocks, the full-band
charged ratio is asymptotic to `(2H+2)(2H+3)/ell`: it is
`Theta(log n)`, `Theta(1)`, and `O(1/log n)` for
`ell=Theta(n)`, `Theta(n log n)`, and `Theta(n log^2 n)`, respectively.
Sharp suffix deletion removes this explicit periodic obstruction at the
last scale, but supplies neither the iterated matching nor quenched
regularity.

A stronger rectangular statement supplies genuine independent switch
coordinates before conditioning.  Split a polynomial macro of length
`a_0=t ell` (for example `a_0` the largest multiple of `ell` below `n^5`)
into linear microblocks and record their transformation vector
`(sigma_1,...,sigma_t)`.  Some vector has an exact Cartesian fiber

\[
\mathcal F_{\boldsymbol\sigma}
 =\mathcal F_{\sigma_1}\times\cdots\times
  \mathcal F_{\sigma_t},\qquad
\log|\mathcal F_{\boldsymbol\sigma}|=\Omega(a_0\log n), \tag{5.12.16}
\]

whose uniform product law is globally band-simple and centrally chordless
with failure probability `exp(-Omega(n))`.  Every branch tuple has the same
full state at every linear checkpoint.  With a uniform seed, conditioning
on the good event preserves exact relabeling marginals but need not preserve
coordinate independence; leaving the product law unconditioned preserves
independence and, under that uniform product experiment, permits the
exponentially small bad macro mass to be charged as `o(W)`.  This
removes endpoint, checkpoint, branch-entropy, and global-simplicity
objections, but supplies no coverage-aware selector.

#### Free truncated histories solve the central seed gate

For the central matching subproblem one can avoid full-state endpoint
fibres entirely.  Narrow the legal tail by one position and put

\[
f^\sharp=m+H+3,\qquad k_0=f^\sharp-1=m+H+2,\qquad
d^\sharp=n-k_0=m-H-1.                               \tag{5.12.16a}
\]

An ordered `k_0`-history is a tuple of distinct letters; one step deletes
its oldest letter and appends any of the `d^sharp` letters outside it.
For all sufficiently large `n`,

\[
d^\sharp\ge(k_0-d^\sharp)+2=2H+5,
\]

so the connector theorem of Section 5.13 joins arbitrary prescribed
histories in at most `3k_0+1=O(n)` emissions.

Let `ell=Theta(n log n)` and let `Omega_g` consist of every starting
history together with every legal `ell`-step continuation whose decks are
simple and chordless at all ranks in `K` and contain no maximum-distance
pair at the two middle ranks.  Conditioned on any current history, the
last-occurrence exposure bound for a prescribed rank-`q` endpoint after a
gap `g` is

\[
\Pr(C_q(t+g)=S\mid\mathcal F_t)
 \le\prod_{j=1}^{\min(g,q)}{\min(j,d^\sharp)\over d^\sharp}. \tag{5.12.16b0}
\]

For `g>=q>=d^sharp` this is

\[
B^\sharp={d^\sharp!\over(d^\sharp)^{d^\sharp}}
 =e^{-n/2+o(n)}.                                    \tag{5.12.16b1}
\]

Returns below `f^sharp` are impossible.  A Johnson chord at a gap
`2<=g<q` would match `g-1` entering and exiting letters; summing their
index displacements gives
`(g-1)(f^sharp-q)<=g-1`, contradicting
`f^sharp-q>=2` for `q in K`.  Union bounds over
`|K|ell^2` long returns and `|K|ell^2n^2` long chord endpoints are `o(1)`
by (5.12.16b1); the two maximum-distance middle orbits add only the same
exponentially small order.  Therefore

\[
|\Omega_g|=(1-o(1))(n)_{k_0}(d^\sharp)^\ell.        \tag{5.12.16b}
\]

Uniform full states and generator words project with constant multiplicity
`d^sharp!` onto `(history,continuation)` pairs, and goodness depends only on
that projected path, which justifies this exact normalization.

Under the uniform law on `Omega_g`, relabeling transitivity and deck
simplicity give, for every `q in K` and `S in binom([n],q)`,

\[
\Pr(S\in U_q)={\ell\over {n\choose q}},\qquad
\max_{S\ne T}\Pr(T\in U_q\mid S\in U_q)
 =O\!\left({1\over n^2}+{\ell\over n^3}\right)
 =O(\log n/n^2).                                    \tag{5.12.16c}
\]

The distance-one term is exactly
`2(ell-1)/(ell q(n-q))`; chordlessness removes every other Johnson edge,
and all remaining allowed distance orbits have size `Omega(n^3)`.  At the
central rank take

\[
b=\left\lfloor{W\over\ell}\right\rfloor,\qquad A=b\ell,
\]

and form the weighted slot hypergraph on
`[b] dotcup binom([n],m)`: in slot `i`, every `(u,w) in Omega_g` contributes
the edge `{i} union U_m(u,w)` with equal weight or common multiplicity.  A
slot has degree `|Omega_g|`, while a central target has degree
`(A/W)|Omega_g|`; hence the relative degree imbalance is exponentially
small.  If `r=ell+1` is the slot-edge size and `Delta_2/Delta` the
maximum normalized target-pair codegree, then

\[
r{\Delta_2\over\Delta}=O(\log^2n/n)=o(1),\qquad
\Xi(S):=\sum_{T\ne S}\Pr(T\in U_m\mid S\in U_m)^2
 =O(\log^2n/n)=o(1).                                \tag{5.12.16d}
\]

There is a proved regular first-bite lemma which calibrates exactly this
scale.  In an
`r`-uniform `D`-regular multihypergraph with pair codegree at most
`delta D`, independently mark edges with probability
`p=alpha/(rD)`, `0<alpha<=1`, and retain only isolated marked edges.  A
fixed vertex is covered with probability

\[
{\alpha\over r}e^{-\alpha}
\left(1+O\left(\alpha r\delta+{\alpha\over D}
                         +{\alpha^2\over rD}\right)\right). \tag{5.12.16e}
\]

Indeed an edge has between
`r(D-1)-binom(r,2)delta D` and `r(D-1)` intersecting competitors; sum
`p(1-p)^{|N(e)|}` over the `D` mutually exclusive incident candidates.
Thus one bite is asymptotically regular when `r delta=o(1)` and `D->infinity`.
The displayed palette is only almost regular; this lemma records the local
scale rather than silently asserting an exact regularization.  No proof is
known that iterates growing-rank bites while preserving the
distance-sensitive profile down to `o(W)` leave; fixed-rank nibble theorems
do not supply that diagonal limit.

This relaxed central hypergraph is physically honest.  If it contains a
matching of `t` chosen cores with

\[
W-t\ell=o(W),                                        \tag{5.12.16f}
\]

order them arbitrarily and insert one `O(n)` history connector before each,
including the cyclic closing connector.  The core targets are distinct,
the seam length and rank-`m` seam collision are
`O(tn)=O(W/log n)=o(W)`, and the resulting cyclic singleton word has length
`(1+o(1))W`.  Hence it has central collision plus leave `o(W)`.

This is only a central lift.  Charging every seam observation at every band
rank costs `O(|K|W/log n)`, not `o(W)`.  Full coefficient one still needs
the union criterion (5.12.U5), useful seam coverage, or longer atoms such as
those in Section 5.13.

#### Pair kernels and one good bite do not imply iteration

There is a scale-matched abstract obstruction.  For an `r`-uniform
`D`-regular multihypergraph `G`, define

\[
\delta(G)={\Delta_2(G)\over D},\qquad
\Xi_G(v)=\sum_{w\ne v}
 \left({\operatorname{codeg}_G(v,w)\over D}\right)^2. \tag{5.12.C1}
\]

If `D>=4` and `r>=64 log(2eDr)`, then for arbitrarily large `L` there is an
`r`-partite, `r`-uniform, `D`-regular multihypergraph with `L` vertices in
each part such that

\[
\Delta_2\le2,\qquad
\max_v\Xi_G(v)\le {2(r-1)\over D},\qquad
{r\nu(G)\over |V(G)|}
 \le {32\log(2eDr)\over r}.                         \tag{5.12.C2}
\]

The construction is explicit probabilistically.  On `M=LD` points choose
`r` independent equipartitions into `L` blocks of size `D`.  When
`M/(r^2D^4)->infinity`, a union bound gives a choice in which blocks from
different partitions intersect in at most two.  Put
`Q=log(2eDr)`, `c=16Q/r`, and `s=ceil(cL)`.  For a fixed `s`-set, the
probability that one partition places its points in distinct blocks is

\[
p_s={(L)_sD^s\over(LD)_s}
 \le\exp\{-s(s-1)/(4L)\}.                            \tag{5.12.C3}
\]

Across `r` partitions,
`binom(M,s)p_s^r<=e^{-sQ}=o(1)`, so one can simultaneously forbid every
common partial transversal of size `s`.  Make one hypergraph vertex for
each labelled block and one edge for each point, joining the `r` blocks
which contain it.  Degrees are `D`, codegrees are block intersections, and
matchings are exactly common partial transversals.  For a fixed block,
`t^2<=2t` for intersection sizes `t in {0,1,2}` gives the `Xi` bound.

Taking

\[
r=\Theta(n\log n),\qquad D=\Theta(n^2/\log n)
\]

matches the free-history scales
`Delta_2/Delta=O(log n/n^2)`,
`r Delta_2/Delta=O(log^2 n/n)`, and
`Xi=O(log^2 n/n)`, yet a maximum matching covers only `O(1/n)` of the
vertices.  Declaring one part to be slots gives the same
one-slot-plus-target shape, and parallel copies inflate the absolute degree
arbitrarily without changing any normalized statistic or the matching
number.  This does **not** refute the Johnson/FIFO palette; it proves that
its distance geometry or another global anti-partition property is
essential.

Reference:
`MATH_COUNTEREXAMPLE_GROWING_RANK_LOCAL_KERNEL_NIBBLE_20260821.md`.

#### Successful union selection forces high-order positive alignment

The exact union target itself yields a complementary necessary theorem.
Let `n<=a<=n^C`, `b=floor(W/a)`, `A=ab`, and take the inner band

\[
J=\{m-r_0,\ldots,m+1+r_0\},\qquad
r_0=\lceil(\log n)^2\rceil,\qquad s=|J|.            \tag{5.12.H1}
\]

Suppose selected simple decks satisfy
`sum_(q in K)(R_q-V_q)=o(W)`.  If `x_(i,q)` counts old-target incidences
relative to earlier blocks and `X_i=sum_(q in J)x_(i,q)`, then

\[
\sum_iX_i=o(W).                                     \tag{5.12.H2}
\]

Indeed `sum_i x_(i,q)=A-V_q=(A-R_q)+(R_q-V_q)`, while

\[
\sum_{q\in J}(A-R_q)
 \le\sum_{q\in J}(W-M_q)
 =O(Wr_0^3/n)=o(W).                                 \tag{5.12.H3}
\]

Consequently all but `o(b)` selected blocks have `X_i<=eta_n a` for some
`eta_n->0`.

Now fix in advance, at every slot, a finite relabeling-invariant palette
`Omega_i` of simple legal candidates; each candidate consists of an ordered
history and an `a`-letter continuation, so
`|Omega_i|<=n^{n+a}`.  Freeze the residuals reached before a good index
`b/3<=i<=2b/3`.  If `Y_i(omega)` counts fresh incidences of a uniform
candidate over all `a s` time-rank coordinates, relabeling gives

\[
\mathbb EY_i\le(2/3+o(1))as,                        \tag{5.12.H4}
\]

because the global nonnegative budget (5.12.H2) makes every prefix union at
every inner rank have size at least `(1/3-o(1))W`.  But the actually selected
candidate is in `Omega_i` and has
`Y_i>=as-eta_n a`.  Hence

\[
\Pr_{\Omega_i}(Y_i\ge as-\eta_n a)
 \ge |\Omega_i|^{-1}
 \ge\exp\{-(a+n)\log n\}.                           \tag{5.12.H5}
\]

This is far heavier than `exp(-Omega(as))`.  Thus the freshness indicators
at the reached residual cannot be negatively associated or satisfy an
absolute-constant subgaussian upper-tail bound.  More sharply, with

\[
d_0=\lceil10(a+n)\log n\rceil,                      \tag{5.12.H6}
\]

some `d_0` time-rank coordinates obey

\[
\Pr(\hbox{all are fresh})>
 \prod_{\alpha}\Pr(\alpha\hbox{ is fresh}).         \tag{5.12.H7}
\]

Otherwise the `d_0`th factorial moment, Maclaurin's inequality, and
(5.12.H4) give the contradiction explicitly as follows.  Put
`N=as` and `L=ceil(N-eta_n a)`.  Then
`d_0/N=O(1/log n)`, `(N-L)/N=o(1)`, and

\[
 { {N\choose d_0}\over {L\choose d_0}}
 \le\left(1+{N-L\over L-d_0}\right)^{d_0}
 =(1+o(1))^{d_0}.
\]

If every `d_0`-set had joint all-fresh probability at most the product of
its marginals, the factorial-moment identity and Maclaurin would give
`E binom(Y_i,d_0)<=binom(N,d_0)(2/3+o(1))^{d_0}`.  Markov applied to
`binom(Y_i,d_0)` would therefore bound the probability in (5.12.H5) by
`(3/4)^{d_0}<exp(-(a+n)log n)`, a contradiction.  Thus a successful
construction must deliberately create positive alignment already at order
`Theta(a log n)` among `Theta(a(log n)^2)` freshness coordinates.  This is
a necessary correlation theorem, not a no-go for clustered product/wreath
or coverage-aware selection.

For completeness, the elementary-symmetric bound used here follows by
repeatedly replacing two nonnegative marginals by their average.  At fixed
pair sum, the contribution from terms containing neither is unchanged, the
contribution from terms containing exactly one depends only on that sum, and
the contribution from terms containing both is proportional to their product
and cannot decrease; iteration and continuity make all marginals equal.

Reference:
`MATH_THEOREM_ADAPTIVE_UNION_HEAVY_TAIL_ALIGNMENT_NECESSITY_20260821.md`.

#### Annealed abundance is not a quenched extension theorem

For the retained central deck

\[
D_\pi^\circ(w)=\{C_m(\pi_t):1\le t\le a=\ell-1\}
\]

define

\[
Z_\pi^\circ(R)
=|\{w\in\mathcal G_\ell:D_\pi^\circ(w)\subseteq R\}|.
\]

For a uniformly random residual `r`-set `R` of density `rho=r/W`, a fixed
seed has the exact mean feasible-branch count

\[
\mathbb E_R Z_\pi^\circ(R)
 =|\mathcal G_\ell|{{r\choose a}\over{W\choose a}}.  \tag{5.12.17}
\]

If `a^2=o(r)`, then

\[
\log\mathbb E Z_\pi^\circ
 \ge\ell\log d+a\log\rho-\log(n!)-O(a^2/r)+o(1).   \tag{5.12.17a}
\]

In the stated applications the error is `o(1)`.  Thus linear `ell=Cn` has
annealed entropy down to density
`n^{-gamma}` for every `gamma<1-1/C`; `ell=n log n+O(n)` reaches formal
density `c_0/n` for `c_0>2e`.  For polynomial `ell`, removing all words
whose central deck contains an antipodal pair costs at most an
`exp(-n/2+o(n))` fraction.  On this centrally chordless support, under a
uniform seed and any seed-independent branch law, the **annealed** kernel
satisfies

\[
\max_{S\ne T}
 \Pr(T\in D_\pi^\circ\mid S\in D_\pi^\circ)
 =O\!\left({a\over n^3}+{1\over n^2}\right).         \tag{5.12.18}
\]

None of (5.12.17)--(5.12.18) survives arbitrary adaptive conditioning.
Indeed the density-`m/n=1/2+o(1)` star of all `m`-sets containing a fixed
letter admits no legal central run longer than `m`, because equal accesses
are separated by more than `m`.  At density exactly `1/n`, the modular
families

\[
\left\{S:\sum_{x\in S}x=c\pmod n\right\}
\]

are equal-sized independent sets of `J(n,m)`.  These examples refute any
extension lemma based only on residual size; they do not show that such
residuals are reachable under a global near-matching process.

Finally, the unordered central problem is not short of abstract switches.
Two perfect matchings of the Middle-Levels graph give, from any missing
color family `M` and retained family of `W-r` middle sets, at least
`|M|-2r` distinct-color Johnson chords of maximum degree two.  Restricting
a Middle-Levels Hamilton cycle to those retained sets gives an abstract
path cover with zero central Hall defect and at most `max(1,r)` components.
The missing property is the exact FIFO law: if
`u_t=A_t\setminus A_(t-1)` and `v_t=A_(t-1)\setminus A_t`, a central path
is a sliding-window word precisely when

\[
v_1,\ldots,v_m\text{ are distinct},\qquad
A_0=\{v_1,\ldots,v_m\},
\]

and, for `t>m`,

\[
v_t=u_{t-m}.                                          \tag{5.12.19}
\]

Tail-MTF legality additionally requires that the forced access word have no
equal letters at a positive gap below `f`, including across its seed
boundary.

Moreover, if the recomposed family has `b_1` resulting cores, reducing
defect by `Delta` while keeping the same central sets requires at least
`Delta-b_1` genuinely new temporal edges, and a
recomposition into `F` word fragments creates at most `F(k-1)` new
rank-`k` windows.  Sparse cut-and-paste cannot lift the abstract reservoir.

The exact postselection target is therefore the simultaneous union condition
(5.12.U5), not one-central matching or graphic charge.  A strictly stronger
but concrete sufficient route is still to choose microblocks whose
rank-`m` decks are disjoint and whose postponed-rank total graphic charge in
(5.12.10) is `o(W)`.  For that route, reachable central branch abundance,
the conditional joint pair probabilities in (5.12.11), and the
component-square bound there would suffice.  None is currently proved, and
none is asserted necessary once quotas are chosen after the paths.

#### Static all-rank prefix multicover

There is no set-theoretic incompatibility among the simultaneous rankwise
union targets.  Let `n=2m+1`, put

\[
 \mathcal L_k={ [n]\choose k},\qquad
 W=|\mathcal L_m|=|\mathcal L_{m+1}|,
\]

and for a permutation state `pi=(pi_1,...,pi_n)` write
`C_k(pi)={pi_1,...,pi_k}`.  There are exactly `W` distinct states

\[
 \{\pi_U:U\in\mathcal L_m\}                       \tag{5.12.S1}
\]

such that, simultaneously for every `0<=k<=n`,

\[
 \boxed{\{C_k(\pi_U):U\in\mathcal L_m\}=\mathcal L_k} \tag{5.12.S2}
\]

as supports, and

\[
 C_m(\pi_U)=U,qquad
 U\longmapsto C_{m+1}(\pi_U)\text{ is a bijection}. \tag{5.12.S3}
\]

Here is the complete construction.  The containment graph between
`\mathcal L_m` and `\mathcal L_{m+1}` is `(m+1)`-regular on equal shores, so
fix a perfect matching

\[
 \Phi:\mathcal L_m\to\mathcal L_{m+1},qquad U\subset\Phi(U). \tag{5.12.S4}
\]

Regard the `W` labels `U` as distinguishable tokens, initially occupying
`U` at rank `m` and `\Phi(U)` at rank `m+1`.  Suppose `1<=k<=m` and every
member of `\mathcal L_k` contains at least one token.  Replace a multiply
occupied set by its distinguishable token copies.  For
`T\subseteq\mathcal L_{k-1}`, incidence counting in its upper shadow gives

\[
 |\Gamma(T)|\ge {n-k+1\over k}|T|\ge|T|.           \tag{5.12.S5}
\]

Every shadow member has a token copy, so Hall matches every `(k-1)`-set to
a distinct token on a containing `k`-set.  Send unmatched tokens to arbitrary
contained sets and iterate downward.

Symmetrically, if `m+1<=k<n` and all `k`-sets are occupied, then for
`T\subseteq\mathcal L_{k+1}` its lower shadow obeys

\[
 |\partial(T)|\ge {k+1\over n-k}|T|\ge|T|.         \tag{5.12.S6}
\]

Hall sends a distinct token into every `(k+1)`-set; send the remaining
tokens arbitrarily upward and iterate.  Each token now carries a maximal
chain

\[
 \varnothing=S_0(U)\subset S_1(U)\subset\cdots
 \subset S_n(U)=[n],\qquad |S_k(U)|=k,             \tag{5.12.S7}
\]

with full support at every rank and the fixed middle pair
`S_m(U)=U`, `S_{m+1}(U)=\Phi(U)`.  Ordering the unique differences
`S_k(U)\setminus S_{k-1}(U)` gives the unique permutation `\pi_U` and proves
(5.12.S2)--(5.12.S3).

At rank `k`, the `W` occurrences therefore have union size exactly
`\binom nk`; since this never exceeds `W`, their quota-relative union
deficit is zero and their repeat mass is precisely the unavoidable baseline
`W-\binom nk`.  This is a **static** ensemble, not a DCC.  It controls no
distance between states, generator word, FIFO chronology, repeated windows
on joins, or atom count.  Arbitrary separate serialization is far too long;
one still needs to realize almost all states in `o(W)` legal atoms or find an
equivalent short chronology.

References:
`MATH_THEOREM_STATIC_ALL_BAND_PREFIX_MULTICOVER_20260821.md`,
`MATH_CANDIDATE_CYCLOMATIC_HALL_GRAPHIC_ROUNDING_20260821.md`,
`MATH_THEOREM_GLOBAL_PARITY_CYCLE_RESERVOIR_AND_FIFO_RECOMPOSITION_BARRIER_20260821.md`,
`MATH_THEOREM_COMMON_ENDPOINT_LINEAR_DECK_CODE_20260821.md`,
`MATH_REDUCTION_ONE_CENTRAL_MATCHING_PLUS_GRAPHIC_COLORS_20260821.md`,
`MATH_CUSTOM_PARITY_GRAPHIC_NIBBLE_INVARIANT_20260821.md`, and
`MATH_ATTACK_ONE_CENTRAL_RECTANGULAR_GREEDY_QUENCHED_GATE_20260821.md`.
The exact union-collapse theorem and all-band annealed calibration are in
`MATH_THEOREM_POSTPONED_GRAPHIC_COALESCENT_AND_DECOUPLING_GATE_20260821.md`;
the forced-suffix and free-history central matching audit is in
`MATH_CENTRAL_SLOT_HYPERGRAPH_VARIABLE_R_NIBBLE_AND_SEED_GATE_20260821.md`.

### 5.13 Two-block product atoms and linear universal seams

The following route is independent of the random block palette.  Its new
unconditional ingredient is that only the ordered history seen by the DCC
ranks must be joined; prescribing the entire recency permutation was an
unnecessary cubic cost.

#### Universal truncated-history connector

Let `P(d,k)` be the directed graph on ordered `k`-tuples of distinct
symbols from an alphabet of size `N=k+d`; one step deletes the oldest
symbol and appends any symbol outside the current tuple.  Put `s=k-d`.
If

\[
d\ge s+2,                                            \tag{5.13.1}
\]

then any two vertices `u,v` are joined by a directed path of length at most

\[
3k+1.                                                \tag{5.13.2}
\]

Here is the complete Hall construction.  If `d>=k+1`, restrict to any
`2k+1` symbols containing (u\cup v), rename the restricted parameters,
and obtain `d=k+1`, `s=-1`, `t=0`.  We may therefore assume `d<=k+1` and
put `t=s+1>=0`.  Starting from `u`, append `t` legal symbols while avoiding
`v_1,...,v_t`; the free pool has size `d>t`.  Call the resulting queue
`u'`.  Every shared symbol `u'_j=v_i` then satisfies `j-i<=d-2`: a
survivor from `u` has `j<=k-t=d-1`, while a newly appended symbol avoided
the first `t` target positions and hence has `i>t`.
Seek a permutation `P` of the `N` symbols by assigning each symbol one
position in the interval

\[
\begin{array}{c|c}
x=u'_j=v_i &[j+1,d+i-1]\\
x=u'_j\notin v &[j+1,N]\\
x=v_i\notin u' &[1,d+i-1]\\
x\notin u'\cup v &[1,N].
\end{array}                                           \tag{5.13.3}
\]

For an internal position interval `[a,b]`, only shared-symbol intervals can
be contained in it, and their distinct target indices obey
`a-d+1<=i<=b-d+1`; hence there are at most `b-a+1`.  Prefixes and suffixes
are bounded by the distinct target and source indices, respectively.  The
interval form of Hall's theorem gives `P`.  The lower endpoints in
(5.13.3) make `u'P` legal, the upper endpoints make `Pv` legal, and
appending the initial `t` letters, then `P`, then `v`, uses
`t+N+k=3k+1` symbols.

For the DCC palette take `k=f-1=m+H+1`, `d=m-H`, and `s=2H+1`.
Thus `m>=3H+3` implies (5.13.1), and arbitrary clean DCC boundary histories
join in `O(n)` emissions.  This theorem does not prescribe the complete
bottom-order recency state.

#### Exact coprime two-block atom

Let `A,B` be disjoint `b`-sets with cyclic orders `alpha,beta`.  Let `tau`
be a cyclic binary word of length `b` with `r` `A`-steps and `b-r`
`B`-steps.  At each step emit the next symbol of the indicated periodic
stream.  Write `I_alpha(i,s)` for the set of `s` consecutive entries of
`alpha` ending at cyclic position `i`, and similarly for `beta`.  If
`gcd(r,b)=1`, the first `b^2` length-`b` windows are exactly

\[
\{I_\alpha(i,r)\cup I_\beta(j,b-r):(i,j)\in\mathbb Z_b^2\}, \tag{5.13.4}
\]

each once, and the word has period `b^2`.  Indeed the two stream counters
have sum equal to time modulo `b`; advancing one type period translates
them by `(r,-r)`, which has order `b`.

A balanced cyclic binary schedule means that the numbers of `A`-steps in
any two equal-length cyclic intervals differ by at most one; such mechanical
words exist for every `b,r`.  The position of the `q`th `A`-event differs
from `qb/r` by less than one, and analogously for `B`.  Consequently a
balanced type schedule gives same-label separation at least

\[
\min\left(\left\lfloor{b^2\over r}\right\rfloor,
          \left\lfloor{b^2\over b-r}\right\rfloor\right). \tag{5.13.5}
\]

In particular put `b=2h+1`, `r=h`, and
`tau=BABA...B`.  Its exact minimum separation is at least `2b-2`, so it is
legal for floor `f=b+H+2` whenever `b>=H+4`.  The MSW middle-wreath theorem
supplies cyclic orders on a `b`-set whose length-`h` interval decks partition
the rank-`h` layer; their length-`h+1` decks partition the next layer by
complementation.  Pairing every cyclic order in
an MSW middle-wreath factor on `A` with every one on `B` partitions the
split slice

\[
\mathcal S(A,B)=
 \{S\subseteq A\cup B:|S\cap A|=h, |S\cap B|=h+1\} \tag{5.13.6}
\]

into exactly `binom(b,h)^2/b^2` product atoms, each containing `b^2`
distinct middle targets.  With one additional pivot and
`W=binom(2b+1,b)`, this slice has

\[
|\mathcal S(A,B)|={b\choose h}^2
 =(1+o(1)){W\over\sqrt{\pi b}}.                     \tag{5.13.7}
\]

Every one of these atoms is internally simple simultaneously at all ranks

\[
b-H\le \ell\le b+1+H                               \tag{5.13.8}
\]

when `H<=b-5`.  Equality of two rank-`ell` targets first fixes their `A/B`
counts; each proper nonempty interval set fixes its endpoint in its cyclic
order, and the counter bijection then fixes the time.  This is only
within-atom simplicity; different atoms may collide.

If `Q=O(W/b^2)` such atoms are available, the connector theorem serializes
them with word-length cost `O(Qb)=O(W/b)` and full-band incidence charge

\[
O(|K|W/b)=o(W)                                      \tag{5.13.9}
\]

whenever `|K|=o(b)`.  Thus compatible endpoints are not an obstruction at
the natural quadratic atom scale.

#### Conditional aggregation and the surviving gate

For an even alphabet `A union B`, `|A|=|B|=b`, put
`W_b=binom(2b,b)`, take `b` an odd prime, and assume `H=o(b)`.  Suppose,
conditionally, that for every
`r in {H+2,...,b-H-2}` the rank-`r` subsets of a `b`-set decompose into
tight Hamilton cycles--the growing-rank Baranyai--Katona conjecture, not a
known theorem.  Pair the rank-`r` factor on `A` with the rank-`(b-r)` factor
on `B`, and choose a balanced type word with exactly `r` `A`-steps.  Prime
`b` gives `gcd(r,b)=1`, while
`H+2<=r<=b-H-2` and (5.13.5) give the required separation.  The product
atoms then cover exactly

\[
P=\sum_{r=H+2}^{b-H-2}{b\choose r}^2,\qquad
{2b\choose b}-P
 \le2(H+2){b\choose H+1}^2
 =e^{-\Omega(b)}{2b\choose b}.                      \tag{5.13.10}
\]

Together with (5.13.9), with `W=W_b` in that generic seam estimate, this
conditionally gives a coefficient-one
**middle-layer** singleton word.  It does not give a DCC: the local factors
control only their payload ranks, and the other window decks can collide
between atoms.  The exact remaining product-route conjecture is a coherent
multirank choice of the local factors, orientations, and serialization for
which the total missing-target count over the DCC band is `o(W_b)`.

#### Clustered schedules align phases but leave a linear rigid-bank ledger

For every payload rank `r`, replace the balanced type word by the nested
clustered schedule

\[
\tau_r=A^rB^{b-r},\qquad P_r=\{0,1,\ldots,r-1\}\subset\mathbb Z_b. \tag{5.13.C1}
\]

If one type occupies `c` consecutive phases, the exact minimum recurrence
gap of a fixed symbol in its `b`-cycle stream is

\[
g_b(c)=b\left\lfloor{b\over c}\right\rfloor+(b\bmod c). \tag{5.13.C2}
\]

To see this, write `b=dc+t`, `0<=t<c`.  Advancing by `b` events of that
type crosses `d` full periods and then `t` positions inside the type block.
The nonwrapping physical gap is `db+t`, while the wrapping gap is
`db+(b-c+t)`; the former is the minimum.

Thus for `H+2<=r<=b-H-2` both streams have gap at least `b+H+2`.
Every type run has length at most `b-H-2`; hence every interval of length
between `b-H` and `b+1+H` contains between one and `b-1` events of each
type.  The counter-pair proof of (5.13.4) then makes every such deck
internally simple.  Balance is not necessary.

The nested phase sets give an exact multirank law.  For a base phase `p`
and `0<=q<=b`, put

\[
J_p(q)=\{p+1,\ldots,p+q\}\pmod b,\qquad
z_{r,p}(q)=|P_r\cap J_p(q)|,
\]

\[
\phi_p(r)=r+z_{r,p}(q),\qquad
\psi_p(r)=r-z_{r,p}(q).                             \tag{5.13.C3}
\]

Algebraically these are the `A`-sizes of the corresponding length-`b+q`
extension and length-`b-q` suffix; they represent actual targets whenever
the indicated window is simple, in particular in the admissible DCC-band
range above.  Since `P_(r+1)` adds phase `r`,

\[
\phi_p(r+1)-\phi_p(r)=1+1_{\{r\in J_p(q)\}}\in\{1,2\},
\]

\[
\psi_p(r+1)-\psi_p(r)=1-1_{\{r\in J_p(q)\}}\in\{0,1\}. \tag{5.13.C4}
\]

Therefore, when different admissible payload ranks use the same local cyclic
orders and aligned counter origins, upper targets from different ranks never
collide on one phase diagonal.  Algebraically, with the endpoint schedules
`r=0,b` included, the lower phase map is surjective and has exactly `q`
repeated adjacent transitions.  For genuine atoms restricted to a payload
interval `I`, the lower conclusion holds only for local ranks whose full
`psi_p`-preimage lies in `I`; no truncated-tail coverage is asserted.  This
removes the torus-coordinate collision, not the need for a common order bank.

The rigid alignment has a sharp conditional cost.  For every central local
upper rank `2q<=s<=b-q`, exactly `b-q` of the `b` phase diagonals occur.
Thus, **if** a rigid one-to-one family of common cyclic-order pairs partitions
that Cartesian target profile, it misses exactly a `q/b` fraction of the
profile.  If the same rigid phase-diagonal accounting is used on every
central split profile, `H/sqrt(b)->infinity`, and `H=o(b^(2/3))`, then with
`M_q=binom(2b,b+q)` and `W_b=binom(2b,b)`,

\[
\sum_{q=1}^H\left({q\over b}-e^{-\Omega(b)}\right)M_q
 =\left({1\over2}-o(1)\right)W_b.                  \tag{5.13.C5}
\]

This is a genuine linear obstruction to **rigid** bank alignment, despite
adequate scalar capacity at every rank:

\[
W_b-M_q\ge {q\over b}M_q.                           \tag{5.13.C6}
\]

This follows from
`W_b/M_q=prod_(j=1)^q (b+j)/(b-j+1)>=(1+1/b)^q>=1+q/b`.

The scalar ledger points toward nonrigid redistribution of this surplus into
the skipped phase diagonals.  The exact CSP in (5.13.C19k)--(5.13.C19r)
later proves that no such redistribution can close the **same complete
one-copy clustered bank**; a surviving implementation must alter its
schedule or factor/atom geometry, or reroute linear mass.

Here is the counting kernel.  For `q<=r<=b-q`, a cyclic `q`-phase
interval in `A^rB^(b-r)` has `z=0` in `b-r-q+1` positions, `z=q` in
`r-q+1` positions, and each `1<=z<=q-1` in exactly two positions.  Solving
`s=r+z` and summing gives

\[
 (b-s-q+1)+(s-2q+1)+2(q-1)=b-q.
\]

The phase diagonals are disjoint and `phi_p` is injective, proving the exact
profile count under the stated partition premise.  The excluded split
profiles have hypergeometric mass `e^{-Omega(b)}M_q`, while uniformly for
`q<=H`,

\[
 {M_q\over W_b}
 =\exp\left(-{q^2\over b}+O(q^3/b^2)\right).
\]

Consequently
`b^(-1) sum_(q<=H) qM_q/W_b -> integral_0^infinity x e^(-x^2)dx=1/2`,
which proves (5.13.C5).

There is one unconditional coherent local case.  Put `b=2h+1`, assume
`H<=h-2`, and use the
same MSW middle-wreath factors on `A,B` for both `tau_h` and `tau_(h+1)`.
Their middle decks partition the two profiles `(h,h+1)` and `(h+1,h)`.
At rank `b+1` they cover without collision exactly

\[
\left(1-{1\over b}\right){b\choose h}^2             \tag{5.13.C7}
\]

targets of the balanced `(h+1,h+1)` slice.  At rank `b-1` they cover every
balanced `(h,h)` target, with exact repeat mass `binom(b,h)^2/b`.  These
slices have size only `Theta(W_b/sqrt b)=o(W_b)`, so this is a real
adjacent-rank alignment theorem, not coefficient one.

For one factor-order pair, the two upper sources use phase sets
`P_h={0,...,h-1}` and `P_(h+1)^c={h+1,...,b-1}`: they are disjoint and omit
only phase `h`, giving `b^2-b` distinct upper targets.  The lower sources use
`P_h^c={h,...,b-1}` and `P_(h+1)={0,...,h}`: they cover all phases and overlap
only at `h`, giving `b^2+b` occurrences on `b^2` targets.  MSW decks at both
local middle ranks partition their layers, so different order pairs cannot
collide.  Multiplication by
`|F|^2=(binom(b,h)/b)^2` gives (5.13.C7) and the stated lower repeat mass.

Finally, independent rank-by-rank alignment is quantitatively inadequate.
Even conditional on arbitrary tight-cycle factors, independently relabeling
the factors at different ranks and sides leaves at least

\[
\left({1\over4}-o(1)\right){2b\choose b+1}          \tag{5.13.C8}
\]

rank-`b+1` targets uncovered in expectation.  The two possible source ranks
have independent mean occurrence at most `1/2+o(1)` on almost every split
profile.  Thus the remaining product theorem must couple local order banks
across ranks; neither rigid one-to-one alignment nor independent relabeling
can do it.

Indeed, for a target with `|Y cap A|=s`, the two sources have respectively
`((s-1)/b)binom(b,s-1)^2` and
`((b-s)/b)binom(b,s)^2` total occurrences, spread by relabeling symmetry
over `binom(b,s)binom(b,s-1)` targets.  Their means are therefore

\[
 \lambda_s^-={s(s-1)\over b(b-s+1)},\qquad
 \lambda_s^+={(b-s)(b-s+1)\over bs}.
\]

They depend on disjoint rank-and-side relabelings.  Markov therefore gives
`Pr(Y uncovered)>=(1-lambda_s^-)(1-lambda_s^+)` whenever both means are at
most one.  Uniformly for `s=(b+1)/2+O(b^(2/3))`, both means are
`1/2+O(b^(-1/3))`; the complementary split profiles have hypergeometric mass
`e^{-Omega(b^(1/3))}`.  Summing proves (5.13.C8).

#### Pooled split-profile capacity has only sublinear deficit

The rigid hole ledger is not a scalar capacity obstruction.  Conditionally
assume, for every admissible payload `r`, a tight-cycle factor of the
rank-`r` subsets of `A` and one of the rank-`(b-r)` subsets of `B`; each has
`binom(b,r)/b` cyclic orders.  Put `c_j=binom(b,j)`.  At upper offset `q`, the
split profile with `s` letters in `A` has demand

\[
P_{q,s}=c_sc_{s-q}.
\]

Pooling all clustered payload ranks gives, on the central admissible
profiles, the formal occurrence capacity

\[
T_{q,s}={1\over b}\left[(b-s-q+1)c_s^2
 +(s-2q+1)c_{s-q}^2
 +2\sum_{z=1}^{q-1}c_{s-z}^2\right].               \tag{5.13.C9}
\]

The three terms count `q`-phase intervals with respectively zero, all, or
an intermediate number `z` of `A` phases.  For large `b`, every
`s in [b/4,3b/4]` and `0<=z<=q<=H` gives an admissible payload
`H+2<=s-z<=b-H-2`.  Set `T_(q,s)=0` outside this interval and charge those
exponentially small profiles in full.  Then

\[
\boxed{\sum_{q=1}^H\sum_s[P_{q,s}-T_{q,s}]_+
 =O(W_b b^{-1/4})=o(W_b).}                          \tag{5.13.C10}
\]

Here is the proof kernel.  Write
`a=c_s`, `c=c_(s-q)`, `R=a/c=e^u`, and
`x=s-(b+q)/2`.  Binomial log-concavity gives
`c_(s-z)^2/(ac)>=R^(1-2z/q)`; the intermediate exponents pair to contribute
at least `q-1`.  If
`A=(b-s-q+1)/b` and `B=(s-2q+1)/b`, then
`A+B=1-3q/b+2/b`, `A-B=-2x/b`, and
`sign(u)=-sign(x)`.  Hence

\[
Ae^u+Be^{-u}\ge(A+B)\cosh u,
\qquad
{T_{q,s}\over P_{q,s}}\ge1-{q\over b}+{u^2\over4}. \tag{5.13.C11}
\]

A positive deficit therefore has size at most `(q/b)P_(q,s)` and requires
`|u|<2 sqrt(q/b)`.  Put `d=(b+1)/2`.  The exact binomial-ratio product is

\[
u(x)=\sum_{j=0}^{q-1}\log
 {d-(x+j-(q-1)/2)\over d+(x+j-(q-1)/2)}.
\]

Its offsets are symmetric, so `u(0)=0`; for
`g(y)=log((d-y)/(d+y))`,
`g'(y)=-2d/(d^2-y^2)<=-4/(b+1)`.  Integrating gives

\[
|u|\ge {4q|x|\over b+1},
\]

so only `O(sqrt(b/q))` split profiles can be deficient.  Their
hypergeometric atom size is `O(M_q/sqrt b)` by the uniform central Stirling
bound, whence the rank-`q` deficit is `O(sqrt(q)M_q/b)`.  Finally
`M_q/W_b=prod_(j=1)^q(b-j+1)/(b+j)<=exp(-q^2/(2b))` and
`sum_(q>=1)sqrt(q)exp(-q^2/(2b))=O(b^(3/4))`, proving
(5.13.C10).

Thus the neighboring payload multiplicities are numerically sufficient to
absorb all but `o(W_b)` split-profile demand.  What remains unproved is the
integral assignment of labelled targets to compatible local order pairs,
orientations, and endpoints across every rank; (5.13.C10) is capacity, not
the coherent order-bank matching itself.

#### Integral phase-origin transport is also sublinear

Even choosing one common counter-origin convention across ranks causes no
new linear loss.  At payload `r` there are

\[
N_r=\left({1\over b}{b\choose r}\right)^2           \tag{5.13.C12}
\]

order pairs.  Enumerate them by `j=0,...,N_r-1` and align equal indices
across ranks.  Since `binom(b,r)` is symmetric and unimodal, the rank support
`I_j={r:j<N_r}` of each column is an interval.  Give column `j` the relative
counter-origin shift `theta_j=j mod b`.  Then

\[
x_{r,\theta}:=|\{0\le j<N_r:j\equiv\theta\pmod b\}|,
\qquad |x_{r,\theta}-N_r/b|<1                       \tag{5.13.C13}
\]

simultaneously at every rank.  A relative rotation of one local cyclic order
realizes this shift without changing its target decks, legality, or internal
simplicity.

For fixed `q,s`, let
`S_(r;q,s)={p:phi_p^(q)(r)=s}`.  The clustered count above gives
`sum_r|S_(r;q,s)|=b-q`.  The integer occurrence capacity placed in phase
diagonal `d` is

\[
C_{q,s,d}=b\sum_r\sum_{p\in S_{r;q,s}}x_{r,d-q-p}.
\]

Comparison with (5.13.C9) using (5.13.C13) gives the simultaneous bound

\[
\boxed{\left|C_{q,s,d}-{T_{q,s}\over b}\right|<b^2} \tag{5.13.C14}
\]

for every central `q,s,d`, with the **same** column shifts.  Since `b` is
prime, the equal-bin demand `P_(q,s)/b` is integral.  Therefore the total
equal-phase-bin deficit satisfies

\[
\sum_{q,s,d}\left[{P_{q,s}\over b}-C_{q,s,d}\right]_+
 \le \sum_{q,s}[P_{q,s}-T_{q,s}]_+ +O(Hb^4)
 =O(W_b b^{-1/4})=o(W_b),                            \tag{5.13.C15}
\]

with the same full charge for tail profiles.  The `O(Hb^4)` term comes from
`b^2` discrepancy on `b` diagonals for `O(Hb)` central profiles and is
exponentially negligible relative to `W_b`.

Thus scalar volume **and** the integral counter-origin rounding are solved
conditionally on the local factors.  The arbitrary enumerations inside the
Ferrers columns still need not put compatible labelled cyclic orders at
neighboring ranks; that simultaneous labelled factor coupling is the exact
remaining product gate.

Reference:
`MATH_THEOREM_CLUSTERED_PRODUCT_PHASE_ALIGNMENT_20260821.md`.
The pooled-capacity theorem is
`MATH_THEOREM_CLUSTERED_PROFILE_CAPACITY_DEFICIT_20260821.md`.
The integral phase-origin theorem is
`MATH_THEOREM_CLUSTERED_PHASE_ORIGIN_FERRERS_TRANSPORT_20260821.md`.

#### A coherent physical endpoint island

There is now one genuinely physical multirank coupling, but only on one
balanced split profile at each odd upper offset.  Let `b` tend through odd
primes, assume

\[
 H/\sqrt b\longrightarrow\infty,
 \qquad H=o(b^{2/3}),
\]

fix an odd `q<=H`, and put

\[
 r={b-q\over2},\qquad s={b+q\over2}=b-r,
 \qquad h_q=r-q+1={b-3q+2\over2}.                 \tag{5.13.C16}
\]

Conditionally take a rank-`r` tight-cycle factor `F_r`.  Complementing the
intervals on each of its cyclic orders makes the same order bank a rank-`s`
factor, and `|F_r|=binom(b,r)/b`.  On disjoint `b`-sets `A,B`, use every
order pair `(alpha,beta) in F_r^2` twice: once with payload `r`, once with
payload `s`, with schedules `A^rB^(b-r)` and `A^sB^(b-s)` and the same
counter origin.  The all-`A` endpoint of the first payload and the all-`B`
endpoint of the second both land in

\[
 \mathcal P_q=\{Y:|Y\cap A|=|Y\cap B|=s\},
 \qquad |\mathcal P_q|={b\choose r}^2.             \tag{5.13.C17}
\]

Each source has exactly `h_q` endpoint phases, and each phase has `b`
counter points.  All resulting targets are distinct, so their exact number
is

\[
 \boxed{\left(1-{3q-2\over b}\right){b\choose r}^2}. \tag{5.13.C18}
\]

Here is the complete simplicity argument.  A target in `\mathcal P_q` is a
rank-`s` interval on each local order.  The rank-`s` decks of the common
factor partition the layer, so the two local sets determine both order
coordinates and their interval endpoints.  Different order pairs therefore
cannot collide.  Within one order pair, the upper phase map
`phi_p^(q)(t)` from (5.13.C3) is strictly increasing in `t`; hence the two
payloads cannot collide on a common counter-sum diagonal.  Multiplying
`2h_qb` targets per order pair by `|F_r|^2` proves (5.13.C18).

If `Q_H` is the set of odd integers in `[1,H]`, the uniform local estimate

\[
 {{b\choose(b-q)/2}^2\over W_b}
 ={2+o(1)\over\sqrt{\pi b}}e^{-q^2/b}
\]

and the odd-mesh Riemann sum give

\[
 \sum_{q\in Q_H}{b\choose(b-q)/2}^2=(1/2+o(1))W_b,
 \qquad
 \sum_{q\in Q_H}{3q-2\over b}{b\choose(b-q)/2}^2
 =O(W_b/\sqrt b).                                  \tag{5.13.C19}
\]

The coherent half may in fact use origins which remain in one type run for
the **entire** `H`-band.  Retain only origins whose next `H` types are all
`A` or all `B`.  The two complementary endpoint sources now have
`r-H+1` phases each, so their exact balanced-profile coverage is

\[
 \left(1-{q+2H-2\over b}\right){b\choose r}^2.    \tag{5.13.C19a}
\]

The labelled-simplicity proof above is unchanged, and

\[
 \sum_{q\in Q_H}{q+2H-2\over b}{b\choose(b-q)/2}^2
 =O\left({W_b\over\sqrt b}+{H\over b}W_b\right)
 =o(W_b).                                           \tag{5.13.C19b}
\]

Thus every retained origin chain in every contributing atom of the physical
`(1/2-o(1))W_b` island can have a constant side type throughout the upper
band.

Thus the construction physically covers `(1/2-o(1))W_b` distinct upper
targets with `o(W_b)` holes.  Distinct odd offsets use disjoint complementary
payload pairs, and at most `W_b/b^2` atoms are used, so the linear connectors
cost `O(W_b/b)` symbols and `O(HW_b/b)=o(W_b)` full-band incidences.  This
theorem is conditional on the local factors and physically covers only the
balanced profile, the two endpoint phase types, and odd offsets.  Even
offsets and the remaining split profiles are not physically covered.  The
constant-origin theorem below subsequently shows that interior phase types
are unnecessary for pooled **scalar** capacity; it does not enlarge this
labelled physical island.

More generally, if coherently chosen rank-`s` and rank-`(s-q)` factors have
`K` common oriented cyclic orders, while
`f_t=binom(b,t)/b`, the same proof gives exactly

\[
 K^2b(b-3q+2)
\]

distinct endpoint targets, a fraction
`(1-(3q-2)/b)K^2/(f_sf_(s-q))` of that split profile.  This is a sufficient
common-order criterion, not a necessary one; nonidentical orders might admit
more general interval-coordinate couplings.  The exact CSP below includes
all of them and proves that they still do not close the one-copy clustered
bank at mesoscopic offsets.

#### Literal common-order overlap stops at the `b^(1/4)` scale

The sufficient criterion above cannot be closed by maximizing literal bank
intersections.  Put

\[
 C_t={b\choose t},\qquad f_t={C_t\over b},qquad
 P_{q,s}=C_sC_{s-q},                               \tag{5.13.C19c}
\]

and, after arbitrary orientations and coherent conjugations, let
`K_(q,s)=|F_s cap F_(s-q)|`.  Cardinality alone gives

\[
 K_{q,s}\le\min(f_s,f_{s-q}),
\]

so the actual weighted incompatibility of the literal-intersection criterion
is at least

\[
 P_{q,s}\left(1-{K_{q,s}^2\over f_sf_{s-q}}\right)
 \ge C_sC_{s-q}-\min(C_s,C_{s-q})^2.              \tag{5.13.C19d}
\]

Define the exact forced cardinality lower bound

\[
 L_{b,q}=\sum_{s=q}^b
 \left(C_sC_{s-q}-\min(C_s,C_{s-q})^2\right).      \tag{5.13.C19e}
\]

If `m=floor((b-q)/2)`, then Vandermonde, symmetry, and unimodality give

\[
 L_{b,q}={2b\choose b+q}-A_{b,q},                 \tag{5.13.C19f}
\]

where

\[
 A_{b,q}=\begin{cases}
 2\displaystyle\sum_{j=0}^{m}{b\choose j}^2,
       &b-q\text{ odd},\\[4pt]
 2\displaystyle\sum_{j=0}^{m-1}{b\choose j}^2+{b\choose m}^2,
       &b-q\text{ even}.
 \end{cases}
\]

Indeed, `C_s>=C_(s-q)` exactly for `s<=(b+q)/2`; on that half the minimum
is `C_(s-q)^2`, and reflection `j=b-s` handles the other half, with one
boundary term in the even case.  Restricting both ranks to the central
quarter changes (5.13.C19e) by only `e^{-Omega(b)}W_b` for
`q=O(sqrt b)`.

If `q/sqrt b->c in (0,infinity)`, then

\[
 {{2b\choose b+q}\over W_b}\longrightarrow e^{-c^2}.
\]

Under the probability law
`Pr(J=j)=binom(b,j)^2/W_b`, the mean is `b/2` and the variance is
`b^2/[4(2b-1)]~b/8`.  The cutoff in `A_(b,q)` is
`(b-q)/2+O(1)`, so the hypergeometric central limit theorem gives

\[
 {A_{b,q}\over W_b}\longrightarrow
 2\Phi(-c\sqrt2)=\operatorname{erfc}(c).
\]

Consequently the actual incompatibility at one such offset is at least

\[
 \boxed{\left(e^{-c^2}-\operatorname{erfc}(c)+o(1)\right)W_b.} \tag{5.13.C19g}
\]

The constant is positive: after translating the defining tail integral,

\[
 \operatorname{erfc}(c)
 ={2\over\sqrt\pi}e^{-c^2}\int_0^\infty e^{-u^2-2cu}\,du
 <e^{-c^2}.
\]

Uniformly for `q=o(sqrt b)`, Taylor expansion of the same two terms gives

\[
 {L_{b,q}\over W_b}={2q\over\sqrt{\pi b}}
 +O\left({q^2\over b}+{1\over\sqrt b}\right).
\]

Thus, for `1<<Q<<sqrt b`, the actual incompatibility summed over `q<=Q`
is at least

\[
 \boxed{\left({1+o(1)\over\sqrt\pi}\right)
 {Q^2\over\sqrt b}W_b.}                           \tag{5.13.C19h}
\]

The forced cardinality loss can be `o(W_b)` only for
`Q=o(b^(1/4))`; one `q=Theta(sqrt b)` already forces linear loss.  This is
only a barrier to **literal equality of cyclic orders** across neighboring
factor banks.  It does not obstruct an interval-coordinate coupling between
nonidentical orders, a neighboring-rank multi-cover, or transport of the
one-sided endpoint surplus proved below.  The next theorem is strictly
stronger: it allows every nonidentical coupling in the same physical
one-copy bank and finds a different deterministic obstruction.

Reference:
`MATH_BARRIER_LITERAL_COMMON_ORDER_OVERLAP_B14_20260821.md`.

#### Nonidentical orders: exact CSP and a one-copy mesoscopic barrier

Literal bank intersection is not the full endpoint problem.  The exact
nonidentical-order problem can nevertheless be written and bounded.  Fix an
odd prime `b`, one offset/profile pair, and a retained constant-type length

\[
 t=s-q,\qquad 1\le q\le L\le\min(t,b-s).
\]

Write `C_j=\binom bj`, `f_j=C_j/b`, `W_b=\binom{2b}b`, and

\[
 a_0=b-s-L+1,\qquad a_1=t-L+1,
 \qquad p_i={a_i\over b},\qquad R={C_s\over C_t}.   \tag{5.13.C19i}
\]

Here and below `(x)_+=\max(x,0)`.

Conditionally fix the four tight-cycle factor banks
`\mathcal F_s^A,\mathcal F_s^B,\mathcal F_t^A,\mathcal F_t^B`.
For each rank `k`, the factor property says that
`(\alpha,i)\mapsto I_\alpha(i,k)` bijects
`\mathcal F_k\times\mathbb Z_b` with the rank-`k` layer.
On the `B` side the bank index is the rank of the complement: complementing
the rank-`s` intervals of `\mathcal F_s^B` supplies its physical
rank-`(b-s)` middle deck, and similarly at `t`.
For a cyclic order `\alpha`, let
`I_\alpha(i,k)={\alpha_i,\ldots,\alpha_{i+k-1}}`.  A target is the pair

\[
 (X,Y),\qquad |X|=s,\quad |Y|=t,
\]

where `X` is its `A` part and `Y` is the complement of its `B` part.  Let
`o_s^A(X)=(\alpha,x)` and `o_t^B(Y)=(\delta,y)` be its unique direct
factor occurrences, and set

\[
 \begin{aligned}
 D_0(Y)&=\{(\beta,v):\beta\in\mathcal F_s^B,
                    I_\beta(v,t)=Y\},\\
 D_1(X)&=\{(\gamma,u):\gamma\in\mathcal F_t^A,
                    I_\gamma(u,s)=X\}.
 \end{aligned}                                      \tag{5.13.C19j}
\]

Each payload-`s` atom `(\alpha,\beta)` and payload-`t` atom
`(\gamma,\delta)` has one relative-origin variable
`\theta^0_{\alpha\beta},\theta^1_{\gamma\delta}\in\mathbb Z_b`.  Define
the cyclic masks

\[
 J_0=\{p+q-s:s\le p\le b-L\},\qquad
 J_1=\{p-t:0\le p\le t-L\}\pmod b;
\]

their sizes are `a_0,a_1`.  The target `(X,Y)` is covered by the retained
endpoint sources **if and only if** its clause

\[
 \boxed{
 \bigvee_{(\beta,v)\in D_0(Y)}
 [x+v-\theta^0_{\alpha\beta}\in J_0]
 \ \vee\!
 \bigvee_{(\gamma,u)\in D_1(X)}
 [u+y-\theta^1_{\gamma\delta}\in J_1]}
                                                            \tag{5.13.C19k}
\]

is true.  Indeed, at phase `p` the payload-`s` coordinate sum is
`p+q-s+\theta^0_{\alpha\beta}`, and the retained phases are
`p=s,\ldots,b-L`; the payload-`t` sum is
`p-t+\theta^1_{\gamma\delta}`, with `p=0,\ldots,t-L`.  As the counter
runs, primality makes `s` and `t` traverse every point on the corresponding
sum diagonal.  This proves both directions of (5.13.C19k), so maximizing
physical endpoint coverage is exactly minimizing the unsatisfied clauses of
this finite `\mathbb Z_b`-valued CSP.

Put `d_0(Y)=|D_0(Y)|`, `d_1(X)=|D_1(X)|`, and let `Z_{q,s}` denote the
number of missed targets.
The cross-deck totals are

\[
 \sum_Yd_0(Y)=C_s,\qquad \sum_Xd_1(X)=C_t.          \tag{5.13.C19l}
\]

Thus mutually independent uniform origins, even after arbitrarily correlated
factor conjugations have been fixed, satisfy the exact expectation formula
and Jensen bound

\[
 \begin{aligned}
 {\mathbb E Z_{q,s}\over C_sC_t}
 &=\left[{1\over C_t}\sum_Y(1-p_0)^{d_0(Y)}\right]
   \left[{1\over C_s}\sum_X(1-p_1)^{d_1(X)}\right]\\
 &\ge (1-p_0)^R(1-p_1)^{1/R}.                     \tag{5.13.C19m}
 \end{aligned}
\]

The last step uses convexity of `d\mapsto c^d` for `0<c<1` together with
the two average degrees `R` and `R^{-1}` in (5.13.C19l).

For the complementary profile, if `q,L=o(b)`, this is at least
`1/4-o(1)`.  It is only an independent-origin barrier; deterministic
anti-alignment could beat (5.13.C19m).

The decisive statement is deterministic.  For every choice of the four
factors, all conjugations, and all origins,

\[
 \boxed{
 {Z_{q,s}\over C_sC_t}\ge
 \begin{cases}
 (1-R^{-1})(1-p_0R)_+,&R\ge1,\\[3pt]
 (1-R)(1-p_1/R)_+,&R\le1.
 \end{cases}}                                      \tag{5.13.C19n}
\]

To prove it, suppose `C_s\ge C_t`.  The whole cross bank
`\mathcal F_t^A` has only `bf_t=C_t` rank-`s` occurrences, so at least
`C_s-C_t` direct rows `X` have `d_1(X)=0`.  In any such row, each of the
`f_s` endpoint-`0` orders covers at most the `a_0` coordinates in its mask;
the row therefore misses at least `(C_t-a_0f_s)_+` targets.  Hence

\[
 Z_{q,s}\ge(C_s-C_t)(C_t-a_0f_s)_+.
\]

The symmetric zero-column argument gives
`Z_{q,s}\ge(C_t-C_s)(C_s-a_1f_t)_+` when `C_s\le C_t`; division by
`C_sC_t` is (5.13.C19n).

This pointwise bound becomes linear after summing the split profiles at one
mesoscopic offset.  Define

\[
 g(R)=\begin{cases}
 (1-R)(1-(2R)^{-1})_+,&0<R\le1,\\[3pt]
 (1-R^{-1})(1-R/2)_+,&R\ge1,
 \end{cases}
\]

and, for `c>0`,

\[
 \Gamma_c={2e^{-c^2}\over\sqrt\pi}
 \int_{-\infty}^{\infty}e^{-4u^2}g(e^{-4cu})\,du>0. \tag{5.13.C19o}
\]

Indeed `g(R)>0` throughout `1/2<R<2` except at `R=1`, so the integrand is
positive on a set of positive measure.

If `q/\sqrt b\to c` and `q\le L=o(b)`, then uniformly for
`s=(b+q)/2+u\sqrt b`,

\[
 {C_s\over C_{s-q}}=e^{-4cu+o(1)},\qquad
 {C_sC_{s-q}\over W_b}
 ={2+o(1)\over\sqrt{\pi b}}e^{-c^2-4u^2}.
\]

The mesh-`b^{-1/2}` Riemann sum in (5.13.C19n) therefore gives

\[
 \boxed{\sum_s Z_{q,s}\ge(\Gamma_c+o(1))W_b.}     \tag{5.13.C19p}
\]

It is enough here to sum the admissible central profiles.  For each fixed
`M`, all `|u|\le M` satisfy `L\le\min(s-q,b-s)` for large `b`; first let
`b\to\infty` and then `M\to\infty`, using the Gaussian tails in
(5.13.C19o).

At the strongest endpoint choice `L=q`, let
`I=\{r:b/4\le r\le3b/4\}`.  Every interior clustered type
`1\le z\le q-1` has exactly two phases per payload rank.  Since the rank-`r`
bank has `C_r^2/b^2` atoms and a phase has `b` counter points, all interiors
together have at most

\[
 {2(q-1)\over b}\sum_{r\in I}C_r^2+e^{-\Omega(b)}W_b
 \le {2(q-1)\over b}W_b+e^{-\Omega(b)}W_b=o(W_b)    \tag{5.13.C19q}
\]

occurrences, where ranks outside the central quarter `I` are charged in
full by the exponential tail term.  Each can repair at most one endpoint
hole.  Thus the
**complete one-copy clustered product-factor bank**, including every
interior phase, still misses

\[
 \boxed{(\Gamma_c-o(1))W_b}                        \tag{5.13.C19r}
\]

rank-`(b+q)` targets whenever `q\sim c\sqrt b`.

Three secondary facts sharpen the boundary of this no-go.  First, even if
one pairs arbitrary nonidentical payload-`s` and payload-`t` atoms
one-to-one, a block has at most `(a_0+a_1)b` endpoint occurrences and there
are at most `\min(f_s^2,f_t^2)` blocks.  Its profile coverage is therefore
at most

\[
 \left(1-{q+2L-2\over b}\right)\min(C_s,C_t)^2.    \tag{5.13.C19s}
\]

so the `Q^2W_b/\sqrt{\pi b}` cardinality loss in (5.13.C19h) applies to
every one-to-one two-atom coupling, not only literal intersections.  This
weaker statement does not itself cover the unrestricted CSP; (5.13.C19n)
does.

Second, a full interval-coordinate isomorphism is rigid.  If
`I_\alpha(i,k)=I_\gamma(\pi(i),k)` for every coordinate and
`2\le k\le b-2`, complement so that `m=\min(k,b-k)<b/2`.  The number of
`m`-intervals containing labels at cyclic distance `d` is

\[
 N(x,y)=\max(0,m-d)+\max(0,m-(b-d)),               \tag{5.13.C19t}
\]

which equals `m-1` exactly on cycle edges.  The interval deck reconstructs
the undirected cycle, so `\pi(i)=\varepsilon i+c`, `\varepsilon=\pm1`.
Preserving two-sided sum diagonals forces the same sign on both local maps.
Full isomorphism is therefore only simultaneous rotation or reversal of the
same two cycles.

Third, partial nonidentity is locally cheap.  One adjacent swap changes
exactly the two windows containing one exchanged position but not the other,
so it preserves exactly `b-2` interval coordinates at every nontrivial
rank: a changed set cannot equal an unchanged one without duplicating a
proper interval within one deck, and the two changed predecessor/successor
sets differ on an outside position.  If the two local order pairs differ by
`d_A,d_B` adjacent swaps,
translate the masks `J_0,J_1` to be disjoint.  Deleting at most
`2d_A` exceptional rows and `2d_B` exceptional columns leaves at least

\[
 \boxed{[a_0+a_1-2d_A-2d_B]_+\,b}                 \tag{5.13.C19u}
\]

distinct endpoint targets in that block.  This is `(1-o(1))b^2` when
`q+L+d_A+d_B=o(b)`, but cheap local seams cannot repair the linear global
deficit (5.13.C19r).

The no-go is conditional on the local tight-cycle factors and scoped to one
physical atom for every factor-order pair with the nested type word
`A^rB^(b-r)`.  It rules out lifting the separate endpoint-token matchings
into this complete one-copy clustered bank using only `o(W_b)` repairs.  It
does **not** rule out a changed type schedule, different factor/atom geometry,
linear duplication, or a linear-scale rerouting that somehow avoids linear
extra length.  Directly appending a linear duplicate bank would itself
forfeit coefficient one.  It is a route-specific obstruction, not a
disproof of coefficient one.

Reference:
`MATH_THEOREM_NONIDENTICAL_ENDPOINT_ORDER_CSP_AND_PAIRING_BARRIER_20260821.md`.

#### Constant-side full-chain laws and an exact product-SCD cover

The preceding no-go is physical, not an abstract Boolean-chain obstruction.
Let `A,B` be disjoint `b`-sets and `1\le H<b/2`, and put
`C_j=\binom bj` and `W_b=\binom{2b}b`.  A middle source `U` has size `b`.
An all-`A` full chain chooses an ordered `H`-tuple of distinct
elements of `A\setminus U` and adds its first `q` elements at offset `q`;
an all-`B` chain is symmetric.  For a rank-`(b+q)` target write

\[
 (X_s,Y_t),\qquad t=s-q,\qquad |X_s|=s,\quad |Y_t|=t,
 \qquad P_{q,s}=C_sC_t.                            \tag{5.13.CS1}
\]

Here `Y_t` is the complement of the physical `B` part.  The all-`A`
predecessors have split `t`, while the all-`B` predecessors have split `s`.

There are two exact simultaneous fractional laws.  On every central source,
put mass `1/2` uniformly on all ordered all-`A` full chains and mass `1/2`
uniformly on all all-`B` chains.  Every target with
`1\le q\le H`, `H\le t`, and `s\le b-H` then has load

\[
 \boxed{\lambda_{q,s}={1\over2}{C_t\over C_s}
                    +{1\over2}{C_s\over C_t}\ge1.}           \tag{5.13.CS2}
\]

Indeed it has `\binom sq` all-`A` predecessors, and a uniform ordered
`H`-tuple begins with the prescribed unordered additions with probability
`1/\binom{b-t}q`; their ratio is `C_t/C_s`.  The all-`B` ratio is
`\binom{b+q-s}q/\binom sq=C_s/C_t`.  These are distributions on full
chains, so the same law proves every offset at once.

The cap-faithful version uses

\[
 \alpha_r={r-H+1\over b},\qquad
 \beta_r={b-r-H+1\over b},
 \qquad \alpha_r+\beta_r=1-{2(H-1)\over b}\le1.   \tag{5.13.CS3}
\]

Put total all-`A` mass `\alpha_r` and all-`B` mass `\beta_r` uniformly on
the corresponding full chains, with the unused mass a null outcome.  Its
exact load and target mass are

\[
 \lambda^{\mathrm{phys}}_{q,s}
 =\alpha_t{C_t\over C_s}+\beta_s{C_s\over C_t},
\]

\[
 \boxed{
 P_{q,s}\lambda^{\mathrm{phys}}_{q,s}
 ={(b-s-H+1)C_s^2+(s-q-H+1)C_{s-q}^2\over b}
 =E_{q,s}.}                                        \tag{5.13.CS4}
\]

Thus these subprobability laws on labelled full chains realize the exact
constant-origin endpoint coefficients **simultaneously**.  For
`H=\Theta(\sqrt{b\log b})`, the audited scalar estimate gives

\[
 \sum_{q\le H}\sum_s
 P_{q,s}(1-\lambda^{\mathrm{phys}}_{q,s})_+
 =O(W_b b^{-1/4}\log^{7/4}b)=o(W_b).              \tag{5.13.CS5}
\]

There is also an exact integral solution once the physical caps are removed.
Fix an SCD `\mathcal D` of `2^{[b]}` and a rank `r` with `H\le b-r`.  Let
`E_q` be the rank-`r` sets whose SCD chain reaches rank `r+q`.  Symmetry of
the chains gives

\[
 E_0\supseteq\cdots\supseteq E_H,qquad
 |E_q|=\min(C_r,C_{r+q}).                          \tag{5.13.CS6}
\]

If `2r+q\le b`, symmetry of each chain interval makes every chain through
rank `r` reach `r+q`; if `2r+q\ge b`, every chain through rank `r+q`
crosses rank `r`.  These two cases prove the count in (5.13.CS6).

For any `N\le C_r`, choose the `N` rank-`r` chain labels with greatest top
rank.  At every offset they meet `E_q` in
`\min(N,|E_q|)`, so following the SCD and then appending arbitrary unused
labels gives support exactly `\min(N,C_{r+q})`, the information-theoretic
maximum, at all offsets simultaneously.

Now fix SCDs `\mathcal D_A,\mathcal D_B`.  Represent a split-`r` source by
`(X_r,Y_r)\in\binom Ar\times\binom Br`, and let `a,c` be the bottom ranks
of its two SCD chains.  Make one permanent side choice:

- if `a\le c`, choose `A` and follow the `A` chain upward;
- if `a>c`, choose `B` and follow the `Y` coordinate downward, equivalently
  adding the removed labels to the physical `B` part.

After an SCD endpoint, continue with arbitrary unused labels on that side.
At noncentral sources choose any side with at least `H` missing labels; one
exists because `H<b/2`.  This assigns one full `H`-chain to **every** middle
source.

It covers every target in (5.13.CS1) satisfying the central conditions.
If the target-chain bottoms obey `a\le c`, then
`[c,b-c]\subseteq[a,b-a]`; since `Y_t` exists, the first chain has a
rank-`t` member `X_t`, and source `(X_t,Y_t)` was assigned `A` and reaches
`X_s`.  If `a>c`, the reverse containment supplies `Y_s`, and source
`(X_s,Y_s)` was assigned `B` and reaches `Y_t`.  The assignment was fixed
before `q`, so this proves the whole band at once.

For `H=o(b)`, the total charged mass of the excluded split tails is

\[
 T_{b,H}:=\sum_{q=1}^H
 \sum_{s:\ s-q<H\ \mathrm{or}\ s>b-H}C_sC_{s-q}
 \le2H^2\binom b{2H}^{\!2}=e^{-\Omega(b)}W_b.     \tag{5.13.CS7}
\]

The lower tail has `0\le s-q<s\le2H`, and reflection gives the same upper
tail; `\binom b{2H}=e^{o(b)}` while `W_b=\Theta(4^b/\sqrt b)`.

Exact coverage of every tail target is impossible in this one-chain-per-source
constant-side model.  If `H\ge2`, each
`B\cup\{a\}`, `a\in A`, can only be the first step of an all-`A` chain
from source `B`; that one source covers at most one of them.  Interchanging
the sides gives the unavoidable lower bound

\[
 \boxed{2(b-1)}                                    \tag{5.13.CS8}
\]

on offset-one misses.  Exact MILPs attain `4,8,12` misses for
`(b,H)=(3,2),(5,2),(7,2)` while covering every offset-two target; these
finite optima are evidence only, not an all-`b` upper theorem.

This solves unrestricted labelled Boolean row/column coinstantiation and
cross-offset side consistency.  It does **not** respect cyclic-factor origin
caps, put the SCD trajectories into common cyclic orders, create internally
simple atoms, or serialize them.  The next results show that these omissions
are essential rather than cosmetic.

Reference:
`MATH_THEOREM_CONSTANT_SIDE_CHAIN_FRACTIONAL_AND_SCD_SUPPORT_20260821.md`.

#### An affine nested schedule closes the simultaneous scalar ledger

The constant-side cover is abstract; a different schedule also closes the
**physical scalar** profile ledger.  Let `b=2m+1` tend through odd primes,
put `c_j=\binom bj` and `W_b=\binom{2b}b`, and define the nested phase sets

\[
 R(x)=mx\pmod b,qquad
 P_r=\{x\in\mathbb Z_b:R(x)<r\}.                   \tag{5.13.AF1}
\]

Throughout this affine block, `1\le q\le H<b` and the upper target-profile
range is `q\le s\le b`.

For `J_p(q)=\{p+1,\ldots,p+q\}` put

\[
 z_{r,p}(q)=|P_r\cap J_p(q)|,qquad
 \phi_p(r)=r+z_{r,p}(q).
\]

Exactly one phase enters when `r` increases, so

\[
 \phi_p(r+1)-\phi_p(r)
 =1+1_{\{R^{-1}(r)\in J_p(q)\}}\in\{1,2\}.        \tag{5.13.AF2}
\]

Thus the same schedules are phase-injective across payload ranks at every
offset.  More generally, for any affine rank permutation `R(x)=ax`, if
`h_{q,s}` counts phases whose image omits profile `s`, then

\[
 \boxed{h_{q,s}\le q.}                             \tag{5.13.AF3}
\]

A skip created when the phase of affine rank `t` enters at position
`p+i`, `1\le i\le q`, obeys

\[
 s-1=t+\sum_{j\ne i}
 1_{\{(t+a(j-i)\bmod b)<t\}}.
\]

For fixed `i` every summand is a nondecreasing one-jump function of `t`, so
the right side is strictly increasing and has at most one solution.

Put `P_{q,s}=c_sc_{s-q}` and `M_q=\binom{2b}{b+q}`.  Conditional on
tight-cycle factors at the proper
central payload ranks, one phase of the rank-`r` order-pair bank supplies
`c_r^2/b` formal occurrences.  Hence

\[
 T_{q,s}={1\over b}\sum_{p\in\mathbb Z_b}
 \sum_{\substack{0\le r\le b\\\phi_p(r)=s}}c_r^2. \tag{5.13.AF4}
\]

The `r=0,b` terms are only an algebraic completion; physically they are set
to zero, and only `b/4\le r\le3b/4` is retained.  For `q=1` every nested
schedule has the exact row

\[
 T_{1,s}={(b-s)c_s^2+(s-1)c_{s-1}^2\over b},
 \qquad {T_{1,s}\over c_sc_{s-1}}\ge1-{1\over b}, \tag{5.13.AF5}
\]

Indeed, with `A=b-s`, `B=s-1`, and
`\rho=c_s/c_{s-1}=(A+1)/(B+1)`,

\[
 A\rho+B\rho^{-1}-(A+B)
 ={(A-B)^2(A+B+1)\over(A+1)(B+1)}\ge0.
\]

Thus its entire deficit is at most `M_1/b\le W_b/b`.

The multiplier in (5.13.AF1) has inverse `-2`.  If `q=2u`, the affine ranks
of one `q`-window are the antipodal pairs

\[
 \{t-k,t-k+(m+1):1\le k\le u\};
\]

if `q=2u+1`, add the rank `t+m-u`.  For
`A_r=\{0,\ldots,r-1\}` the pair count
`g_r(y)=1_{A_r}(y)+1_{A_r}(y+m+1)` differs from one on a union of at most
two cyclic intervals of total size `|2r-b|`.  Translating those exceptional
intervals proves the dominant-phase bounds below: in the even case, the
union of the `u` translates has size at most
`|2r-b|+2(u-1)`.  With
`x=s-(b+q)/2`,

\[
 \begin{array}{ll}
 q=2u:&\#\{p:(r,z)=(s-u,u)\}\ge[b-|2x|-q]_+,\\[3pt]
 q=2u+1:&\#\{p:(r,z)=(s-u,u)\ \mathrm{or}\
                    (s-u-1,u+1)\}\ge[b-4|x|-2q]_+.
 \end{array}                                       \tag{5.13.AF6}
\]

For odd `q`, exclude the translated exceptional sets at the two adjacent
thresholds and the unique phase at which the extra rank equals the lower
threshold; every remaining phase realizes one of the two displayed colors.
This is the full odd-offset argument, not an averaging assertion.

Take `H\le C_0\sqrt{b\log b}` and
`|x|\le K\sqrt{b\log b}`.  The uniform expansion

\[
 \log\binom b{b/2+y}
 =\log\binom b{b/2}-{2y^2\over b}
 +O\!\left({G^2\over b^2}+{G^4\over b^3}\right),
 \qquad G=H+K\sqrt{b\log b}+1,
\]

For the gamma-function interpolation
`F(y)=\log\binom b{b/2+y}`, symmetry gives `F'(0)=0`, while
`\psi_1(v)=v^{-1}+O(v^{-2})` gives
`F''(y)=-4/b+O(b^{-2}+y^2b^{-3})`; integrating twice proves the displayed
expansion.

Together with (5.13.AF6), it gives, uniformly for `2\le q\le H`,

\[
 \boxed{{T_{q,s}\over P_{q,s}}
 \ge\exp\!\left({q^2\over b}-\varepsilon_b\right)},
 \qquad
 \varepsilon_b=O\!\left(\sqrt{\log b\over b}\right).        \tag{5.13.AF7}
\]

The two target factors have displacements `x\pm q/2`; the even source has
displacement `x`, while the two odd sources have displacements
`x\pm1/2`.  This gives the gain `q^2/b`; the phase and odd half-step losses
are absorbed into `\varepsilon_b`.  Formula (5.13.AF5) supplies `q=1`.

A profile can therefore be deficient only for `q^2<b\varepsilon_b`, and
then by relative amount at most `\varepsilon_b`.  Since
`\sum_sP_{q,s}=M_q\le W_b`,

\[
 \sum_{q\le H}\sum_{|x|\le K\sqrt{b\log b}}
 [P_{q,s}-T_{q,s}]_+
 =O(W_b b^{-1/4}\log^{3/4}b).                     \tag{5.13.AF8}
\]

The standard Gaussian profile bound

\[
 {P_{q,s}\over W_b}\le{C\over\sqrt b}
 \exp\!\left[-c{q^2+x^2\over b}\right]
\]

makes the omitted split tails `o(W_b)` after choosing `K` large.  All source
ranks in the retained window are central.  Thus the explicit affine family
has total full-band formal deficit

\[
 \boxed{O(W_b b^{-1/4}\log^{3/4}b)=o(W_b).}        \tag{5.13.AF9}
\]

Complementation gives the identical lower-band scalar statement.

These schedules are also physically legal and internally simple inside each
central atom.  Put `f=b+H+2`.  Any physical interval of length `f-1`
contains one type period plus at most `H+1` phases, hence fewer than `b`
events of either type for `b/4\le r\le3b/4`; equal stream symbols are
separated by at least `f`.  Every type interval of length
`b-H,\ldots,b+H+1` has between one and `b-1` events of each type, so its
two local cyclic intervals are proper.  After one period the counters move
by

\[
 (r,b-r)\equiv(r,-r)\pmod b,                      \tag{5.13.AF10}
\]

which has order `b`; the `b` phases occupy the `b` counter-sum diagonals.
The `b^2` starts therefore enumerate every local interval pair once.  Equal
band windows recover both proper interval endpoints and hence the start
time, proving internal simplicity.

This is a deterministic simultaneous-offset **scalar/profile-capacity**
theorem.  It neither constructs the conditional factors nor assigns distinct
labelled targets across their order pairs.  The following obstructions show
that scalar surplus alone does not provide that lift.

Reference:
`MATH_THEOREM_AFFINE_NESTED_BALANCED_SCHEDULE_PROFILE_CAPACITY_20260821.md`.

#### Affine row loads and the physical product-SCD barrier

The affine capacity in (5.13.AF9) does not spread labelled factor rows.
Retain an odd prime `b` and put `C_j=\binom bj` and
`W_b=\binom{2b}b`.  Conditionally fix a rank-`r` tight-cycle factor
`\mathcal F_r` with `f_r=C_r/b` cyclic orders.  For any proper local rank
`k`, define its full within-bank multiplicity array

\[
 n_{r,k}(U)=\#\{(\alpha,i):\alpha\in\mathcal F_r,
                  I_\alpha(i,k)=U\},
 \qquad \sum_U n_{r,k}(U)=C_r.                    \tag{5.13.RL1}
\]

After a uniform label conjugation, a fixed `k`-set sees
`D_{r,k}(X)=n_{r,k}(\pi_r^{-1}X)`.  Put

\[
 \rho_{r,k}={C_r\over C_k},\qquad
 v_{r,k}={1\over C_k}\sum_U n_{r,k}(U)^2-\rho_{r,k}^2,
\]

and let `\sigma_{r,k}` be the fraction of positive entries.  For any nested
schedule let `m_r(q,s)` be the phase multiplicity mapping payload `r` to
split `s`.  For the exact moment laws assume
`1\le t=s-q\le s\le b-1`.  Put `P_{q,s}=C_sC_t`, let `Z_{q,s}` be the
number of missed targets in that split profile, and put
`Z_q=\sum_sZ_{q,s}`.  The exact row and column occurrence laws are

\[
 L^A_{q,s}(X)=\sum_r m_r(q,s)f_rD^A_{r,s}(X),
 \qquad
 L^B_{q,s}(Y)=\sum_r m_r(q,s)f_rD^B_{r,s-q}(Y).    \tag{5.13.RL2}
\]

Under independent rank-and-side conjugations,

\[
 \begin{aligned}
 \mathbb EL^A_{q,s}(X)
   &={1\over bC_s}\sum_r m_r(q,s)C_r^2,\\
 \operatorname {Var}L^A_{q,s}(X)
   &=\sum_r\left({m_r(q,s)C_r\over b}\right)^2v_{r,s},
 \end{aligned}                                     \tag{5.13.RL3}
\]

with the symmetric column formulas.  Moreover

\[
 \Pr(D_{r,k}(X)=0)=1-\sigma_{r,k}\ge(1-\rho_{r,k})_+,
 \qquad v_{r,k}\ge\rho_{r,k}(1-\rho_{r,k})\quad(\rho_{r,k}\le1). \tag{5.13.RL4}
\]

These identities retain every repeated longer/shorter window inside a
factor.  Conjugation only uniformly permutes this fixed multiplicity array;
it creates no within-bank law of large numbers.

For the half-step affine schedule
`P_r=\{x:((b-1)/2)x\bmod b<r\}`, write `b=2h+1`.  Since the multiplier
has inverse `-2`,

\[
 \begin{aligned}
 P_{h-k}&=\{0\}\cup\{2k+3,2k+5,\ldots,2h-1\},\\
 P_{h+1+k}&=\{0,1,3,\ldots,2h-1\}
 \cup\{2h,2h-2,\ldots,2h-2k+2\}.
 \end{aligned}
\]

The first line is for `0\le k\le h-1` (with `P_0=\varnothing` separately)
and the second for `0\le k\le h`.

Now let `q/\sqrt b\to c>0` and
`x/\sqrt b\to d`.  If `q` is even, one main payload has
`m_r=b-O(q+|x|+1)` and every other payload has total phase mass
`O(q+|x|+1)`.  If `q` is odd, two adjacent main payloads each have
`m_r=b/2+O(q+|x|+1)`, and the rest have the same small total.  This follows
directly from the alternating form of the affine prefix word away from one
cyclic interval of length `O(q+|x|+1)`.

For either main rank,

\[
 \alpha(c,d):={C_r\over C_s}=e^{c^2/2+2cd+o(1)},
 \qquad
 \beta(c,d):={C_r\over C_{s-q}}=e^{c^2/2-2cd+o(1)},             \tag{5.13.RL5}
\]

while all minor occurrences total `o(P_{q,s})`: their combined phase
multiplicity is `O(\sqrt b)`, each phase contributes
`O(C_{\lfloor b/2\rfloor}^2/b)`, and
`P_{q,s}=\Theta_c(C_{\lfloor b/2\rfloor}^2)`.  If `q` is even and
`d<-c/4`, the main rank has fewer than `C_s` row occurrences, so at least a
`1-\alpha-o(1)` row fraction is absent **deterministically**; for
`d>c/4` the symmetric column fraction is `1-\beta-o(1)`.  For odd `q`,
the two main conjugations are independent, giving the squared absence
probabilities.  Thus

\[
 {Z_{q,s}\over P_{q,s}}\ge
 \begin{cases}1-\alpha-o(1),&d<-c/4,\\
               1-\beta-o(1),&d>c/4,
 \end{cases}\quad(q\ \mathrm{even}),              \tag{5.13.RL6}
\]

and the expected bounds for odd `q` replace each positive term by its
square.  Since

\[
 {P_{q,s}\over W_b}={2+o(1)\over\sqrt{\pi b}}
 e^{-c^2-4d^2},
\]

Riemann summation yields, on either parity subsequence,

\[
 \boxed{\mathbb EZ_q\ge(\Gamma_c^{\mathrm{parity}}-o(1))W_b}, \tag{5.13.RL7}
\]

where

\[
 \begin{aligned}
 \Gamma_c^{\mathrm{even}}
 &= {4e^{-c^2}\over\sqrt\pi}\int_{c/4}^\infty e^{-4d^2}
       (1-e^{c^2/2-2cd})\,\mathrm d d,\\
 \Gamma_c^{\mathrm{odd}}
 &= {4e^{-c^2}\over\sqrt\pi}\int_{c/4}^\infty e^{-4d^2}
       (1-e^{c^2/2-2cd})^2\,\mathrm d d.
 \end{aligned}
\]

Both constants are positive.  The exact variance formula (5.13.RL3) also
has a positive normalized lower limit on these shoulders.  Thus the affine
schedule solves scalar capacity while its one or two dominant independently
conjugated banks retain a linear labelled deficit.

There is an independent obstruction to compiling the exact product-SCD
cover into ordinary torus atoms.  At payload rank `r`, put
`m=\min(r,b-r)` and `C_{-1}=0`.  Every SCD has
`N_a=C_a-C_{a-1}` chains of bottom rank `a`.  The wider-side matrix

\[
 M^*(X,Y)=1_{\{a(X)\le c(Y)\}}
\]

has row degree

\[
 R_a=\sum_{c=a}^mN_c=C_r-C_{a-1}.                 \tag{5.13.RL8}
\]

By contrast, every physical rank-`r` order-pair torus, with any cyclic type
schedule containing `r` `A` phases and arbitrary origins, has exactly

\[
 K_r=rf_r={r\over b}C_r                           \tag{5.13.RL9}
\]

`A` choices in **every** row: fix the unique owner coordinate of `X`; for
each opposite order its `b` counter cells run through every phase once.
Therefore

\[
 \operatorname {dist}_{\mathrm{Ham}}(M,M^*)
 \ge\sum_{a=0}^m(C_a-C_{a-1})
 \left|C_r-C_{a-1}-{r\over b}C_r\right|.          \tag{5.13.RL10}
\]

For `|r-b/2|=O(\sqrt{b\log b})`, divide by `C_r^2` and use the mesh
`p_a=(C_a-C_{a-1})/C_m`, `u_a=C_{a-1}/C_m`.  The sum converges to

\[
 \int_0^1|1-r/b-u|\,du={ (1-r/b)^2+(r/b)^2\over2}
 ={1\over4}+o(1).
\]

For a sufficiently large fixed `K`, put
`I_b=\{r:|r-b/2|\le K\sqrt{b\log b}\}`.  These central ranks contain
`1-o(1)` of `\sum_rC_r^2=W_b`, so

\[
 \boxed{\sum_{r\in I_b}\operatorname {dist}_{\mathrm{Ham}}(M_r,M_r^*)
 \ge(1/4-o(1))W_b.}                               \tag{5.13.RL11}
\]

This is not an artifact of choosing the wider-side threshold.  On a product
of two SCD chains with unequal bottoms, offset-one coverage forces every
common-rank source toward the wider chain: the pattern `(B,A)` on two
successive ranks misses their intervening target, and the unequal endpoint
forces the induction.  Only equal-bottom products may use a threshold.
Their central fraction is at most

\[
 {\sum_a(C_a-C_{a-1})^2\over C_r^2}=o(1).         \tag{5.13.RL12}
\]

Hence any complete cover on these fixed SCD trajectories is `o(C_r^2)`
from `M^*`, and remains `(1/4-o(1))C_r^2` from every physical row-regular
torus marking.  This is a compilation/Hamming-distance lower bound, not by
itself an equal missed-target bound.  At the balanced offset-one profile the
physical occurrence deficit is exactly at least `C_{(b-1)/2}^2/b=o(W_b)`,
so exact physical coverage is impossible but an asymptotic cover on
different trajectories is not excluded.

Both no-gos are scoped to independent rank conjugations or to the fixed
product-SCD trajectories inside a one-copy factor bank.  Correlated
multirank banks, different containment trajectories/atom geometry, and
linear-scale rerouting remain open.

Reference:
`MATH_OBSTRUCTION_AFFINE_BALANCED_FACTOR_ROW_LOAD_AND_SCD_DIAGONAL_20260821.md`.

#### Random nested spreading leaves a mean-one coupon barrier

Randomizing the nested schedule removes the affine one/two-bank dominance,
but not the independent-conjugation obstruction.  Let `b` be an odd prime,
put `C_j=\binom bj`, `M_q=\binom{2b}{b+q}`, and
`W_b=\binom{2b}b`, and let `R` be a uniform permutation of
`\mathbb Z_b`.  Put

\[
 P_r=\{x:R(x)<r\},\qquad
 \phi_p^q(r)=r+|P_r\cap\{p+1,\ldots,p+q\}|,
\]

and let `m_r(q,s)` count phases mapping payload `r` to split `s`.  For a
fixed labelled target `V` of split `(s,t=s-q)`, conditionally fix the
rank-`r` tight factors, each with `C_r/b` cyclic orders, and let `N_r(V)`
be its number of occurrences from the resulting one-copy product bank.
Let `Z_q` denote the number of missed rank-`(b+q)` targets.  Under
independent rank-and-side conjugations the variables are independent and

\[
 \boxed{\lambda_r:=\mathbb EN_r(V)
 ={m_r(q,s)\over b}{C_r^2\over C_sC_t}},
 \qquad
 \Lambda_{q,s}=\sum_r\lambda_r.                   \tag{5.13.RN1}
\]

This includes every repeated longer/shorter interval inside each factor;
uniform conjugation is used only for its exact target mean.

Write `s=(b+q)/2+x`.  Choose `L\to\infty` with

\[
 {qL\over\sqrt b}\to0,qquad {L^4\over b}\to0.
\]

Uniformly for `|x|\le L\sqrt b` and every candidate `r=s-z`,
`0\le z\le q`, central-binomial expansion gives

\[
 {C_r^2\over C_sC_t}=1+o(1),qquad
 \log{C_r^2\over C_sC_t}
 ={q^2+8x(z-q/2)-4(z-q/2)^2\over b}+o(1).         \tag{5.13.RN2}
\]

Strict phase injection gives `\sum_rm_r(q,s)\le b`, hence every nested
schedule satisfies the mean-one ceiling

\[
 \boxed{\Lambda_{q,s}\le1+o(1)}                  \tag{5.13.RN3}
\]

on this window.

For a uniform schedule, put
`M_{r,z}=\#\{p:|P_r\cap\{p+1,\ldots,p+q\}|=z\}`.  Its exact expected
phase histogram is

\[
 {\mathbb EM_{r,z}\over b}
 ={\binom rz\binom{b-r}{q-z}\over\binom bq}.      \tag{5.13.RN4}
\]

Its largest central atom is `O(q^{-1/2})`.  Transposing two permutation
values changes at most `2q` cyclic windows, so bounded differences and a
union bound apply.  More explicitly,

\[
 \Pr\{|M_{r,z}-\mathbb EM_{r,z}|\ge u\}
 \le2\exp\!\left(-{u^2\over Cbq^2}\right).
\]

The hypergeometric atom bound follows from the adjacent-mass ratio, which
is monotone through its mode, plus Stirling's bounds in a
`\Theta(\sqrt q)` neighborhood of that mode.  Taking
`u=Kq\sqrt{b\log b}` and union-bounding over `r,z` gives, with probability
`1-o(1)`,

\[
 \max_{b/4\le r\le3b/4}\max_z{M_{r,z}\over b}
 \le {C_1\over\sqrt q}+C_2q\sqrt{\log b\over b}=:\varepsilon_b. \tag{5.13.RN5}
\]

If

\[
 q\to\infty,qquad q=o\!\left(\sqrt{b/\log b}\right),
\]

then `\varepsilon_b=o(1)` and (5.13.RN1)--(5.13.RN2) give
`\max_r\lambda_r=o(1)`.  Conditional on such a schedule, Markov's inequality
and independence across payload ranks yield

\[
 \Pr(V\ \mathrm{uncovered})
 =\prod_r\Pr(N_r(V)=0)
 \ge\prod_r(1-\lambda_r).
\]

Because `\sum_r\lambda_r^2\le(\max_r\lambda_r)\Lambda_{q,s}=o(1)`,

\[
 \log\prod_r(1-\lambda_r)
 =-\Lambda_{q,s}-o(1)\ge-1-o(1).
\]

The window `|x|\le L\sqrt b` contains `1-o(1)` of the target layer, so

\[
 \boxed{\mathbb E_{\mathrm{factors}}Z_q
 \ge(e^{-1}-o(1))M_q.}                            \tag{5.13.RN6}
\]

The same random schedule works simultaneously for any polynomial-size list
of admissible offsets after increasing the concentration constant.  If
`Q_0\to\infty` and
`Q_0\le Q_1=o(\sqrt{b/\log b})`, summing expectations gives

\[
 \boxed{\mathbb E_{\mathrm{factors}}\sum_{q=Q_0}^{Q_1}Z_q
 \ge(e^{-1}-o(1))(Q_1-Q_0+1)W_b.}                 \tag{5.13.RN7}
\]

Thus spreading the phase mass converts the few large coupons into many
small ones but leaves total mean at most one; the miss fraction tends to at
least `e^{-1}`.  This no-go uses mutually independent rank-and-side
conjugations.  It does not obstruct correlated multirank factor banks, an
explicit occurrence-to-target matching, deliberate anti-alignment of the
holes, or the top regime `q=\Theta(\sqrt{b\log b})`.

Reference:
`MATH_OBSTRUCTION_RANDOM_NESTED_SCHEDULE_MEAN_ONE_COUPON_20260821.md`.

#### The affine shared-offset object is an exact retirement LP

The scalar affine theorem is the marginal ledger of a genuine nested-chain
fractional object, but an ordinary full-chain matching is much too rigid.
Let `b` be an odd prime, put `C_j=\binom bj` and
`W_b=\binom{2b}b`, and set

\[
 H=\Theta(\sqrt{b\log b}),\qquad g=\lfloor b/4\rfloor,\qquad
 J=\{g,\ldots,b-g\},\qquad L_r=C_r^2.              \tag{5.13.RT1}
\]

Put `m=(b-1)/2` and
`P_r=\{x\in\mathbb Z_b:mx\bmod b<r\}`.  A path type is `i=(r,p)` with
`r\in J`, and

\[
 z_i(q)=|P_r\cap\{p+1,\ldots,p+q\}|,\qquad
 s_i(q)=r+z_i(q),\qquad a_i={L_r\over b}.          \tag{5.13.RT2}
\]

The integer `a_i` is the number of occurrence tokens of this type:
`b\mid C_r` for prime `b` and `0<r<b`.  From a
split-`r` middle source, the number of compatible ordered prefixes through
offset `\ell` is

\[
 D_i(\ell)=(b-r)_{z_i(\ell)}(r)_{\ell-z_i(\ell)},
 \qquad (n)_k=n(n-1)\cdots(n-k+1).                 \tag{5.13.RT3}
\]

This is a formal one-copy occurrence palette.  Its interpretation as a
physical order-pair bank is conditional on the corresponding local
tight-cycle factors; the fractional calculation below does not construct
or coinstantiate those factors.

Give every compatible full-chain edge
`(o,U,V_1,\ldots,V_H)` weight `1/(L_rD_i(H))`.  Then every retained source
and every occurrence token has load one, while every target of profile
`(q,s)` has exact load

\[
 \boxed{\ell(V)={T^{\mathrm{aff}}_{q,s}\over P_{q,s}}},\qquad
 P_{q,s}=C_sC_{s-q},\qquad
 T^{\mathrm{aff}}_{q,s}={1\over b}
 \sum_{\substack{i=(r,p)\\s_i(q)=s}}L_r.          \tag{5.13.RT4}
\]

Indeed, if `z=s-r`, the numbers of compatible sources and targets from one
source are

\[
 N_{r,q,z}={s\choose r}{b+q-s\choose b-r},\qquad
 B_{r,q,z}={b-r\choose z}{r\choose q-z},
\]

and direct factorial cancellation gives

\[
 {N_{r,q,z}\over B_{r,q,z}}={L_r\over P_{q,s}}.   \tag{5.13.RT5}
\]

The same count gives the exact nonzero pair loads.  A compatible
token--source pair has load `1/L_r`, a compatible token--target pair at
`(q,s)` has load `1/P_{q,s}`, and a compatible source--target pair has load

\[
 {n^{\mathrm{aff}}_{r,q,z}\over bB_{r,q,z}},\qquad
 n^{\mathrm{aff}}_{r,q,z}
 =\#\{p:z_i(q)=z\}.                                \tag{5.13.RT6}
\]

For `q<q'`, `V\subset V'`, and profiles `s,s'`, put

\[
 E_{q,s}^{q',s'}={b-s\choose s'-s}
 {s-q\choose(q'-q)-(s'-s)}
\]

and
`n_r(q,s;q',s')=\#\{p:s_i(q)=s,\ s_i(q')=s'\}`.  Then

\[
 \boxed{\ell(V,V')=
 {1\over bP_{q,s}E_{q,s}^{q',s'}}
 \sum_{r\in J}n_r(q,s;q',s')L_r.}                 \tag{5.13.RT7}
\]

Thus (5.13.AF9) is not merely analogous to a joint law: it is exactly this
law's target marginal.  Nevertheless, matching full edges cannot solve the
band.  If an ordinary full-`H` matching has `N` edges, its rank-`(b+H)`
targets force `N\le M_H`, so

\[
 \boxed{\sum_{q=1}^H(M_q-N)
 \ge\sum_{q=1}^H(M_q-M_H)
 =\Omega(\sqrt b\,W_b).}                           \tag{5.13.RT8}
\]

Here `M_q=\binom{2b}{b+q}`: for `q=O(\sqrt b)`, `M_q/W_b` stays bounded
below, whereas `M_H/W_b\le\exp(-cH^2/b)=b^{-\Omega(1)}`.  The correct
object lets a physical chain continue after it stops making real claims.
Let `x_i(q)` be the surviving real mass of type `i` at offset `q`.  Its
exact scalar retirement LP is

\[
 0\le x_i(H)\le\cdots\le x_i(1)\le a_i,\qquad
 \sum_{i:s_i(q)=s}x_i(q)\le P_{q,s},               \tag{5.13.RT9}
\]

with objective

\[
 \Phi(x)=\sum_{q=1}^H\sum_i x_i(q),\qquad
 \mathfrak D_{\mathrm{ret}}
 =\sum_{q=1}^HM_q-\max\Phi(x).                    \tag{5.13.RT10}
\]

Writing `y_i(\ell)` for mass whose last real target is `\ell`, its exact
dual is

\[
 \min\left\{
 \sum_i a_i\alpha_i+\sum_{q,s}P_{q,s}\beta_{q,s}:
 \alpha_i+\sum_{q=1}^{\ell}\beta_{q,s_i(q)}\ge\ell
 \quad\forall i,\ell\right\},
 \quad \alpha_i,\beta_{q,s}\ge0.                  \tag{5.13.RT11}
\]

Indeed a retirement column `(i,\ell)` has profit `\ell`, consumes one unit
of its path capacity, and consumes the profile resource
`(q,s_i(q))` for every `q\le\ell`; these are exactly the displayed dual
constraints.

Every feasible retirement point has an exact labelled fractional lift.
Put `x_i(H+1)=0`,
`y_i(\ell)=x_i(\ell)-x_i(\ell+1)`, and give each compatible retired edge
`(o,U,V_1,\ldots,V_\ell)` weight

\[
 {y_i(\ell)\over a_i}\,{1\over L_rD_i(\ell)}.      \tag{5.13.RT12}
\]

Its token and source loads are at most one, its target load is
`\sum_{i:s_i(q)=s}x_i(q)/P_{q,s}\le1`, and its total real-target mass is
exactly `\Phi(x)`.  Since every nontrivial central
`B_{r,q,z}` or `E_{q,s}^{q',s'}` is at least `g-H`, all fractional pair
loads are
bounded by

\[
 \boxed{\alpha_{\mathrm{pair}}
 \le{1\over g-H}+e^{-\Omega(b)}=O(1/b).}           \tag{5.13.RT13}
\]

Merging all path types at a profile node does not make (5.13.RT9) an
ordinary network flow: an incoming unit could leave on another phase's
continuation.  For `b=2m+1`, `r=m-2`, the phases `p=b-2` and `p=b-3`
have first-three profile paths `(r,r+1,r+1)` and
`(r+1,r+1,r+2)`: they meet at their second profile but have different
histories and continuations.  The labelled incidence matrix also retains
the face

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad\det=-2.
\]

Finite LPs at `b=31,41,61` found no loss beyond the separate-layer scalar
optima for the same central payload truncation.  The next theorem supersedes
that evidence by proving `\mathfrak D_{\mathrm{ret}}=o(W_b)` and giving the
corresponding labelled fractional retired-chain lift.  The later alternating
GK theorem also closes abstract integral growing-rank rounding.  Physical
factor/order-bank/product-atom coinstantiation remains distinct and open.

Reference:
`MATH_THEOREM_AFFINE_FULL_CHAIN_LOADS_RETIREMENT_LP_AND_MATCHING_OBSTRUCTION_20260821.md`.

#### Persistent alternating phases close the affine retirement LP

The half-step word contains enough phase paths which alternate for the
entire band to support an explicit near-saturating retirement point.  Let
`b` be an odd prime, put

\[
 C_t={b\choose t},\qquad L_r=C_r^2,\qquad
 W_b={2b\choose b},\qquad M_q={2b\choose{b+q}},
\]

and, for `u<=r<=b-u`, put `E_(r,u)=C_(r+u)C_(r-u)`.  The two ideal
alternating orientations have masses

\[
\begin{array}{ll}
 A^E_{r,u}=E_{r,u}{b-r-u\over b-2u},&
 B^E_{r,u}=E_{r,u}{r-u\over b-2u},\\[2mm]
 A^O_{r,u}=E_{r,u}{b-r-u\over b+2u+1},&
 B^O_{r,u}=E_{r,u}{r-u\over b+2u+1}.
\end{array}                                                \tag{5.13.PAR1}
\]

At `q=2u` both orientations have profile `s=r+u`; at `q=2u+1`,
orientation `B` has profile `r+u` and orientation `A` has profile
`r+u+1`.  Pascal's identities give

\[
 A^E_{r,u}+B^E_{r,u}=E_{r,u},\qquad
 B^O_{r,u}+A^O_{r-1,u}=C_{r+u}C_{r-u-1},                 \tag{5.13.PAR2}
\]

so the masses fill every exact Boolean quota `P_(q,s)=C_sC_(s-q)`.
Vandermonde gives total masses `M_(2u)` and `M_(2u+1)`.  More importantly,
whenever `u+1<=r<=b-u-1`, they never revive along either path:

\[
 A^E_{r,u}\ge A^O_{r,u}\ge A^E_{r,u+1},\qquad
 B^E_{r,u}\ge B^O_{r,u}\ge B^E_{r,u+1}.                 \tag{5.13.PAR3}
\]

At a boundary the unavailable next mass is defined to be zero, so the same
pathwise conclusion holds with that convention.

The first inequalities only compare denominators.  For the second ones set
`a=r-u-1` and `c=b-r-u-1`.  After positive denominators are cleared, the
`A` difference is

\[
 2a^2u+2a^2+4au^2+8au+4a
 +2c^2u+c^2+4cu^2+4cu+c,
\]

and the `B` difference is its nonnegative reflected expression

\[
 2a^2u+a^2+4au^2+4au+a
 +2c^2u+2c^2+4cu^2+8cu+4c.
\]

Now use `R(x)=((b-1)/2)x mod b` and put `d_r=|2r-b|`.  Since
`R^(-1)(t)=-2t mod b`, the equal-bit edges of `1_(P_r)` form one cyclic
interval of length `d_r`; the complementary linear arc is alternating and
has `b-d_r+1` vertices.  Thus it contains at least

\[
 n_r=\left\lfloor{b-d_r-H+2\over2}\right\rfloor           \tag{5.13.PAR4}
\]

length-`H` origins of each orientation.  On the core `d_r<=b/16`, with
`b>=64` and `H<=b/16`, choose exactly `n_r` origins of each orientation and set
`K_r=n_rL_r/b`.  Clamp each ideal branch to this literal phase capacity:

\[
 \overline A_r(2u)=\min(A^E_{r,u},K_r),\qquad
 \overline A_r(2u+1)=\min(A^O_{r,u},K_r),                 \tag{5.13.PAR5}
\]

and similarly for `B`.  Give every selected phase in an orientation
`\overline A_r(q)/n_r` or `\overline B_r(q)/n_r`, and give every other
phase zero.  Equations (5.13.PAR2)--(5.13.PAR3) show directly that these
weights satisfy all nesting, phase-capacity, and profile-capacity
constraints in (5.13.RT9).

Here is the finite loss estimate.  For a core source put `d=d_r` and
`Delta=d+H`.  Its clamp excess per branch and layer is at most
`Delta L_r/b`.  Also

\[
 {E_{r,u}\over L_r}
 =\prod_{t=0}^{u-1}{(b-r-t)(r-t)\over(r+t+1)(b-r+t+1)}
 \le e^{-u^2/b},                                           \tag{5.13.PAR6}
\]

and the orientation fraction in (5.13.PAR1) moves from its `u=0` value by
at most `2ud/b^2`.  Since that initial fraction is at least `1/4`, for
`2<=u<=sqrt b` the ideal branch has fallen by at least
`u^2L_r/(16b)`; for `u>=sqrt b` it is already below `K_r`.  Hence excess is
possible for at most `6sqrt(Delta+1)` values of `u`, and the total clamp
loss at source `r` is at most

\[
 {24\over b}(d_r+H+1)^{3/2}L_r.                            \tag{5.13.PAR7}
\]

Under `Pr(\mathbf R=r)=L_r/W_b`, the exact hypergeometric moment is

\[
 \mathbb E(2\mathbf R-b)^2={b^2\over2b-1},                 \tag{5.13.PAR8}
\]

while `Pr(|2\mathbf R-b|>b/16)<=2e^{-b/512}`.  Summing
(5.13.PAR7), using Lyapunov's inequality, and charging the omitted tail at
most `H` times its source mass gives the explicit bound

\[
 \boxed{
 {\mathfrak D_{\rm ret}\over W_b}
 \le {24\sqrt2\over b}
 \left[\left({b^2\over2b-1}\right)^{3/4}+(H+1)^{3/2}\right]
 +2He^{-b/512}.}                                            \tag{5.13.PAR9}
\]

Consequently, for `H=O(sqrt(b log b))`,

\[
                    \boxed{\mathfrak D_{\rm ret}=o(W_b).} \tag{5.13.PAR10}
\]

Applying the exact cohort lift (5.13.RT12) to this point gives a labelled
fractional matching in the variable-rank retired-chain hypergraph with real
target-incidence mass

\[
                    \sum_{q=1}^H M_q-o(W_b)                \tag{5.13.PAR11}
\]

and maximum pair load at most `1/(g-H)=O(1/b)`, where
`g=floor(b/4)`.  In (5.13.PAR11), an edge retiring at `ell` is counted once
for each of its `ell` real targets.  Indeed, with
`y_i(ell)=x_i(ell)-x_i(ell+1)`, the cohort identity is

\[
 \sum_{i,\ell}\ell y_i(\ell)=\sum_{q,i}x_i(q),             \tag{5.13.PAR12}
\]

and the affine orbit law distributes the surviving mass uniformly over
each profile's `P_(q,s)` labelled targets.  Central nontrivial extension
degrees are at least `g-H`; all other displayed degrees are exponential.

This closes the simultaneous scalar and labelled **fractional** retirement
gate on genuine physical half-step phase paths.  It is not an integral
growing-rank hypergraph matching theorem and does not coinstantiate common
labelled tight-cycle factors, orders, origins, or physical atoms.

Reference:
`MATH_THEOREM_HALFSTEP_PERSISTENT_ALTERNATING_RETIREMENT_20260821.md`.

#### Local loads and pair codegrees do not round retired chains

The preceding fractional point cannot be rounded by a theorem using only
its part sizes, vertex loads, pair loads, and abstract chain format.  Put

\[
 M_q={2b\choose b+q},\qquad W_b={2b\choose b},\qquad
 H=\Theta(\sqrt{b\log b}),
\]

set `M_(H+1)=0`, and define retirement cohorts

\[
 d_\ell=M_\ell-M_{\ell+1},\qquad
 \sum_{\ell=q}^Hd_\ell=M_q.                               \tag{5.13.LLR1}
\]

There is a finite retired-chain hypergraph with parts
`O,U,T_1,...,T_H`, ordered
`O<U<T_1<...<T_H`, such that

\[
 |O|=|U|=W_b,\qquad |T_q|=M_q,                             \tag{5.13.LLR2}
\]

and a fractional matching which saturates every target, has maximum vertex
load one and maximum pair load at most `2/b`, but every integral matching
has target-incidence deficit

\[
                         \Omega(\sqrt b\,W_b).              \tag{5.13.LLR3}
\]

The construction is exact.  Let

\[
 Q_b=\log(2eb(H+2)),\qquad R=\lceil128Q_b\rceil.            \tag{5.13.LLR4}
\]

For each `ell>=R`, take `ell+2` independent uniform equipartitions of a set
of size `bd_ell` into `d_ell` blocks of size `b`.  Regard each point as a
hyperedge through its containing block in the token cohort, source cohort,
and target cohorts `1,...,ell`.  There is a choice for which every vertex
has degree `b`, every codegree is at most two, and

\[
                         \nu(G_\ell)\le d_\ell/4.           \tag{5.13.LLR5}
\]

For completeness, the probability that two blocks from different
partitions intersect in at least three points is at most
`binom(b,3)^2/binom(bd_ell,3)`, so the expected number of codegree
violations is `O((ell+2)^2b^3/d_ell)=o(1)`.  A matching is a common partial
transversal.  If `r=ell+2`, `L=d_ell`, `D=b`,
`Q=log(2eDr)`, and `s=ceil(16QL/r)`, the expected number of common partial
transversals of size `s` is at most `e^(-Qs)=o(1)`.  Since
`r>=128Q_b`, this gives (5.13.LLR5).  The required `d_ell` are uniformly
exponential because `M_H=W_b b^(-O(1))` and

\[
 d_\ell=M_\ell{2\ell+1\over b+\ell+1}\quad(\ell<H),
 \qquad d_H=M_H.                                           \tag{5.13.LLR6}
\]

In particular `d_ell>=b` for every `1<=ell<=H` once `b` is sufficiently
large.

Give every long-cohort edge weight `1/b`.  For `ell<R`, use the complete
`(ell+2)`-partite hypergraph on `d_ell` vertices per part with edge weight
`d_ell^(-(ell+1))`.  Add `W_b-M_1` isolated token and source vertices.
Then every target has load exactly one, every active token and source has
load one, and all pair loads are at most `2/b`.  Telescoping gives exact
fractional target value

\[
                    \sum_{\ell=1}^H\ell d_\ell
                    =\sum_{q=1}^HM_q.                      \tag{5.13.LLR7}
\]

On the other hand, an integral matching has value at most

\[
 \sum_{\ell<R}\ell d_\ell+{1\over4}
 \sum_{\ell\ge R}\ell d_\ell.                            \tag{5.13.LLR8}
\]

The full sum is `Omega(sqrt(b)W_b)`, because `M_q/W_b` is bounded below
for `q<=sqrt(b)/4`, while the short-cohort contribution is at most
`RW_b=O(W_b log b)`.  This proves (5.13.LLR3).  Parallel edges may be
coalesced without changing any load or matching number, so the example can
be made simple.

This is a parameter-only obstruction, not a counterexample to the affine
Boolean-chain hypergraph: its chains live in the displayed abstract graded
order, not Boolean containment, and it lacks the affine orbit identities.
Therefore the remaining integral theorem must exploit global Boolean or
affine structure, such as residual shadow expansion, affine anti-partition,
or a direct common-order construction.  Fixed-rank nibble estimates applied
only to the `O(1/b)` pair bound cannot close the coefficient-one problem.

Reference:
`MATH_OBSTRUCTION_RETIRED_CHAIN_LOCAL_LOADS_AND_PAIR_CODEGREES_20260821.md`.

#### Alternating Greene--Kleitman chains close abstract integral retirement

The local-parameter obstruction does not apply to the Boolean lattice's
global chain structure.  Order the coordinates of two `b`-letter blocks as

\[
                  A_1,B_1,A_2,B_2,\ldots,A_b,B_b.          \tag{5.13.GK1}
\]

Apply the Greene--Kleitman bracketing: scan from left to right and pair each
zero with the latest unpaired one to its left.  Between consecutive unpaired
coordinates all coordinates are paired internally, hence their separation
is odd.  Therefore their coordinate colours alternate, and so do all upward
edges of every resulting symmetric chain.

A chain with top rank `b+k` has top excess `k`.  At its rank-`b` member it
has `k` unpaired zeros followed by `k` unpaired ones.  The first upper edge
flips the rightmost unpaired zero.  The prefix walk first reaches height
`-k` there, so the coordinate has the parity of `k`.  Thus

\[
        \boxed{\text{the chain is `A`-first iff `k` is odd}.} \tag{5.13.GK2}
\]

Write the middle split as `r=|U\cap A|`, put

\[
 L_r={b\choose r}^{\!2},\qquad
 E_{r,u}={b\choose{r+u}}{b\choose{r-u}},
\]

and let `n_(r,k)` count chains with this split and exact top excess `k`.
For `0<=k<b`, set
`a=r-floor(k/2)` and `c=b-r-ceil(k/2)`.  Ballot-word first-return
decomposition and Lagrange inversion give

\[
 n_{r,k}={
 (k+1){b\choose{a-1}}{b\choose c}
 +k{b+1\choose a}{b-1\choose{c-1}}
 \over b-k}.                                             \tag{5.13.GK3}
\]

Indeed, if `D_A,D_B` are the two alternating-colour excursion series and
`Q=tD_AD_B`, then

\[
 D_A=1+xQ,\qquad D_B=1+yQ,
 \qquad Q=t(1+xQ)(1+yQ),
\]

and a top of excess `k` has series
`(xyt)^kD_A^(k+1)D_B^k`; extracting the remaining `b-k` pairs gives
(5.13.GK3).  Adjacent binomial ratios put this in the telescoping form

\[
 \boxed{
 \begin{aligned}
 n_{r,2u}
  &= {r+u\over b}E_{r,u}
    -{r+u+1\over b}E_{r,u+1},\\
 n_{r,2u+1}
  &= {b-r-u\over b}E_{r,u}
    -{b-r-u-1\over b}E_{r,u+1}.
 \end{aligned}}                                          \tag{5.13.GK4}
\]

The terminal `k=b` chain supplies the final boundary term when `b` is odd.
Summing the parity tails gives exact integral survivor counts

\[
 G^A_{r,u}={b-r-u\over b}E_{r,u},\qquad
 G^B_{r,u}={r+u\over b}E_{r,u}.                           \tag{5.13.GK5}
\]

At even offset `2u` these are the `A`- and `B`-first masses; at odd offset
`2u+1` they are `G^A_(r,u)` and `G^B_(r,u+1)`.  They fill every Boolean
target rectangle exactly and are nonincreasing along their respective
paths.

Now take the physical half-step rank map `R(x)=((b-1)/2)x mod b`.  With
`d_r=|2r-b|`, its equal-bit edges form one interval of length `d_r`, so its
complementary arc supplies at least

\[
 n_r=\max\left\{0,
 \left\lfloor{b-d_r-H+2\over2}\right\rfloor\right\}
                                                               \tag{5.13.GK6}
\]

persistent origins of each alternating orientation.  For odd prime `b`,
each phase has the integer token capacity `L_r/b`; put
`K_r=n_rL_r/b`.  In each split and orientation, retain the `K_r` GK chains
of largest top excess.  Their exact survivor count is

\[
        \min(K_r,G^A_{r,u})\quad\hbox{or}\quad
        \min(K_r,G^B_{r,u}),                               \tag{5.13.GK7}
\]

with the odd indexing above.  There are enough chains because
`n_r<=(b-d_r)/2`, while the two full orientation classes have sizes
`(b-r)L_r/b` and `rL_r/b`.

Partition the retained chains into `n_r` blocks of size `L_r/b` and biject
each block to the occurrence tokens of one persistent phase of the same
orientation.  Every chain's side word agrees with its phase until it
retires.  The GK decomposition makes all selected middle sources and all
selected targets distinct simultaneously at every rank.  A selected
top-excess-zero chain is bookkeeping only and is omitted from the actual
`ell>=1` matching; unused tokens and sources are allowed.  This is therefore
a literal integral occurrence-token/source/labelled-target retired-chain
matching.

The loss is still sublinear.  On `b>=128`, `H<=b/16`, and
`d_r<=b/16`, one has

\[
 K_r\ge {b-d_r-H+1\over2b}L_r,
 \qquad {E_{r,u}\over L_r}\le e^{-u^2/b}.                 \tag{5.13.GK8}
\]

Every positive branch excess is at most `(d_r+H)L_r/b`.  For
`8<=u<=sqrt b`, the `A` branch has fallen by at least
`u^2L_r/(5b)` and the `B` branch by at least `u^2L_r/(16b)`; beyond
`sqrt b` both lie below capacity.  Thus excess is possible only for
`u<8+4sqrt(d_r+H)`, and the splitwise deficit obeys

\[
 D_r\le {64\over b}(d_r+H+1)^{3/2}L_r.                    \tag{5.13.GK9}
\]

Using the squared-binomial moment (5.13.PAR8) and the same tail estimate as
before gives

\[
 \boxed{
 {D_{\rm GK}\over W_b}
 \le {64\sqrt2\over b}
 \left[\left({b^2\over2b-1}\right)^{3/4}+(H+1)^{3/2}\right]
 +2He^{-b/512}.}                                           \tag{5.13.GK10}
\]

Consequently, for odd primes and `H=O(sqrt(b log b))`, there is an integral
retired-chain matching of real-target incidence

\[
             \boxed{\sum_{q=1}^H{2b\choose b+q}-o(W_b).}  \tag{5.13.GK11}
\]

This closes abstract growing-rank rounding for the affine occurrence-token
Boolean-containment object.  It does **not** place the selected chains into
common cyclic tight-factor orders or partition them into physical product
atoms.  A single chain can be embedded as one distinguished product-atom
prefix, but the other counter translations from the same two cyclic orders
need not be the GK chains through their sources and can collide with other
prototype atoms.  That orbit-packing/order-bank coinstantiation is the
remaining product gate.

Reference:
`MATH_THEOREM_BOOLEAN_ALTERNATING_GK_INTEGRAL_RETIREMENT_20260821.md`.

#### The canonical GK first-successor FIFO map is acyclic

The abstract matching cannot be serialized by repeatedly taking the first
GK upper successor in the same fixed linear order.  For a rank-`b` source
`S`, put

\[
 h_S(j)=2|S\cap[1,j]|-j,
 \qquad
 f(S)=\min\{j:h_S(j)=\min_i h_S(i)\},                      \tag{5.13.GKF1}
\]

when the common minimum is negative.  This `f(S)` is the rightmost
unpaired zero, hence the first GK addition.  Since the walk returns to zero,
there is an up-step after `f(S)`, and therefore

\[
                              \boxed{f(S)<\max S.}          \tag{5.13.GKF2}
\]

For an ordered FIFO state
`q_t=(y_(t-b+1),...,y_t)` with source `S_t`, the direct rule appends
`y_(t+1)=f(S_t)` and drops the oldest coordinate.  If `M_t=max S_t`, then

\[
                         M_{t+1}\le M_t,
 \qquad                  M_{t+b}<M_t                       \tag{5.13.GKF3}
\]

whenever those updates exist.  The current maximum is dropped within `b`
steps and cannot be appended before or after that event by (5.13.GKF2).
Since every `b`-set in `[2b]` has maximum at least `b`, the process reaches
`[b]` and stops after at most `b^2` updates.  It has no directed cycle.

In particular, adding the stronger shifted-prefix requirements

\[
 S_{t+1}=S_t-\{y_{t-b+1}\}+\{a_1(S_t)\},\qquad
 a_j(S_{t+1})=a_{j+1}(S_t)                                \tag{5.13.GKF4}
\]

cannot create a cyclic realization.  This obstruction concerns only the
canonical first-successor FIFO rule in one fixed alternating linear order.
Product-atom translations, atom-dependent conjugations, and different
successor maps remain outside its scope.

Reference:
`MATH_OBSTRUCTION_ALTERNATING_GK_DIRECT_FIFO_SUCCESSOR_20260821.md`.

#### A polylogarithmic factor menu needs residual image expansion

There is a rigorous fixed-layer selector escape from the independent-coupon
barriers, but it requires more than uniform target means.  Let `L` be a
source set and `R` a target set,

\[
 \ell=|L|\ge n=|R|,
\]

and let one candidate bank be a single-valued map `F:L\to R`.  A menu of
`K` independent banks `F_1,\ldots,F_K` supplies the bipartite edges
`(u,F_j(u))`.  A sourcewise selector is a matching in this menu graph.  If
`N_G(T)\subseteq L` denotes the source neighborhood of `T\subseteq R`,
Hall's theorem gives the exact deficiency

\[
 n-\nu(G)=\max_{T\subseteq R}\bigl(|T|-|N_G(T)|\bigr)_+.
                                                               \tag{5.13.SEL1}
\]

For `0<\eta\le1`, say that a fresh-bank law has
`\eta`-residual hitting if every deterministic `S\subseteq L` and
`T\subseteq R` with

\[
 |S|\ge\ell-n+|T|
\]

satisfies

\[
 \boxed{\mathbb E|F(S)\cap T|
 \ge |T|\left(1-e^{-\eta|S|/n}\right).}            \tag{5.13.SEL2}
\]

Reveal one fresh bank per round.  If `S` and `T` are the unused sources and
unmatched targets, match one proposing source to every distinct target in
`F_j(S)\cap T`.  A single-valued map cannot use one source for two targets,
so this is a matching.  If `U_j` is the number of unmatched targets and
`\delta=(\ell-n)/n`, then `U_j=u` leaves exactly
`|S|=\ell-n+u` sources.  Conditional residual hitting gives

\[
 \mathbb E(U_{j+1}\mid U_j=u)
 \le u e^{-\eta(\delta+u/n)}.                     \tag{5.13.SEL3}
\]

The function `x e^{-\eta x}` is concave on `[0,1]`.  Thus, for
`a_j=\mathbb EU_j/n`,

\[
 a_{j+1}\le a_j e^{-\eta(\delta+a_j)}.
\]

Dropping `a_j` from the exponent gives
`a_j\le e^{-\eta\delta j}`.  Dropping `\delta` and using
`e^{-\eta a}\le(1+\eta a)^{-1}` gives
`a_{j+1}^{-1}\ge a_j^{-1}+\eta`.  Since `a_0=1`,

\[
 \boxed{{\mathbb EU_K\over n}
 \le\min\left\{{1\over1+\eta K},e^{-\eta\delta K}\right\}.}   \tag{5.13.SEL4}
\]

Markov also gives

\[
 \Pr\!\left(U_K>{n\over\sqrt{1+\eta K}}\right)
 \le{1\over\sqrt{1+\eta K}}.
\]

Hence `\eta K\to\infty` yields a source-disjoint matching covering
`(1-o(1))n` targets with high probability.

For the ideal law in which all `F_j(u)` are independent and uniform on
`R`,

\[
 \mathbb E|F(S)\cap T|
 =|T|\left[1-\left(1-{1\over n}\right)^{|S|}\right]
 \ge |T|(1-e^{-|S|/n}),
\]

so (5.13.SEL2) holds with `\eta=1` and any `K\to\infty`, in particular a
polylogarithmic menu, succeeds sourcewise.

A concrete pair-moment hypothesis implies (5.13.SEL2).  Suppose
`\ell/n\le B` and, for every target `v` and distinct sources `u,u'`,

\[
 \Pr(F(u)=v)={1\over n},\qquad
 \Pr(F(u)=v,\ F(u')=v)\le{C\over n^2}.             \tag{5.13.SEL5}
\]

For `N_v(S)=|\{u\in S:F(u)=v\}|` and `\mu=|S|/n`,

\[
 \mathbb EN_v(S)=\mu,\qquad
 \mathbb EN_v(S)^2\le\mu+C\mu^2.
\]

Cauchy--Schwarz on `N_v1_{\{N_v>0\}}` gives

\[
 \Pr(N_v(S)>0)\ge{\mu\over1+C\mu}
 \ge1-e^{-\mu/(1+CB)}.
\]

Summing over `v\in T` proves residual hitting with

\[
 \boxed{\eta={1\over1+CB}.}                       \tag{5.13.SEL6}
\]

This sufficient condition is not automatic for containment banks: a source
can reach only its containing targets, so its correct marginal kernel is
not globally uniform.  The profilewise or full-orbit version of
(5.13.SEL5) must itself be proved.

There is also an exact necessary support audit that does not assume
transitivity.  Put
`p(V)=\Pr(V\in F(L))`.  A target absent from all `K` independent image sets
cannot be selected, so every successful menu must satisfy

\[
 \boxed{{1\over n}\sum_{V\in R}(1-p(V))^K=o(1).}  \tag{5.13.SEL7}
\]

Under target transitivity this reduces to `(1-p)^K=o(1)`, and when
`p=o(1)` it requires `Kp\to\infty`.  Even this union condition is not
sufficient for matching because Hall deficiencies may remain inside the
covered union.

Containment, exact neighbor marginals, and the correct mean load still do
not imply (5.13.SEL2).  Let `L=\binom{[2b]}b` and
`R=\binom{[2b]}{b+q}`, and put

\[
 W=\binom{2b}b,\qquad M=\binom{2b}{b+q},\qquad
 d=\binom bq.
\]

There exists a deterministic containment map `F:L\to R` with
`U\subset F(U)` and

\[
 \boxed{{|F(L)|\over M}
 \le{\log W+1\over d}+{1\over M}.}                \tag{5.13.SEL8}
\]

Indeed, choose
`m=\lceil(M/d)(\log W+1)\rceil` random targets.  A fixed source is missed
with probability at most `e^{-md/M}`, so the expected number of missed
sources is below one.  Some family of at most `m` targets therefore covers
every source; assigning each source one containing member proves
(5.13.SEL8).

For a uniform label permutation `g`, conjugate this map by

\[
 F_g(U)=gF(g^{-1}U).                               \tag{5.13.SEL9}
\]

Transitivity on containment flags makes `F_g(U)` exactly uniform over the
`d` targets containing `U`.  A fixed target has expected preimage load
`W/M`, because

\[
 W\binom bq=M\binom{b+q}q.
\]

Nevertheless every target selected from `K` independent conjugates lies in
the union of their `K` image sets, so

\[
 \nu(G)\le K|F(L)|.                                \tag{5.13.SEL10}
\]

For `2\le q\le b/2` and `K=\operatorname{polylog}(b)` this is
`o(M)`.  This example need not arise from tight-cycle factors; it proves
that factor geometry must rule out small-image fibers.

For one actual upper offset, after exponentially small split-tail deletion,
a complete candidate product-factor bank has the formal map

\[
 F_q:\mathcal U\to\mathcal V_q,\qquad
 \ell=(1-o(1))W_b,\qquad n=M_q=\binom{2b}{b+q}.    \tag{5.13.SEL11}
\]

Thus the precise positive gate is to prove (5.13.SEL2) for a fresh
candidate bank with `\eta_bK_b\to\infty`.  The corrected nontransitive
necessary audit is

\[
 {1\over M_q}\sum_{V\in\mathcal V_q}
 (1-p_q(V))^{K_b}=o(1),\qquad
 p_q(V)=\Pr(V\in F_q(\mathcal U)).                 \tag{5.13.SEL12}
\]

The theorem is fixed-layer and sourcewise.  Its matching retains at most one
edge per source, so its **abstract selected-edge count** is at most `\ell`,
not `K\ell`.  This is not yet a physical length theorem.  Different offsets
may select different banks at one source; selected targets need not be
nested; different sources inside one indivisible `b^2`-source atom may
choose different banks; and shared factor orders may prevent the selected
edges from coexisting.  Concatenating `K` complete physical banks would cost
`KW_b` and is outside the selector model.  An atomwise coinstantiation or
recomposition theorem is still required before this menu can contribute to
coefficient one.

Reference:
`MATH_THEOREM_POLYLOG_FACTOR_MENU_RESIDUAL_HITTING_SELECTOR_GATE_20260821.md`.

#### Exact labelled containment and token relaxations

The following layers of the order-bank problem are now solved.  They are
relaxations.  By (5.13.C19r) they cannot be lifted inside the unmodified
one-copy clustered factor bank; a physical realization must change the
schedule or factor/atom geometry, or reroute linear mass.  Retain the central
payload interval `I`, put `c_j=binom(b,j)`, and for `1<=q<=H` define

\[
 n_{r,q,z}=
 \begin{cases}
 b-r-q+1,&z=0,\\
 2,&1\le z\le q-1,\\
 r-q+1,&z=q,
 \end{cases}
 \quad
 D_{r,q,z}={b-r\choose z}{r\choose q-z},           \tag{5.13.C20}
\]

\[
 L_r=c_r^2,\qquad
 P_{q,s}=c_sc_{s-q},\qquad
 T_{q,s}={1\over b}
  \sum_{\substack{r\in I\\s-q\le r\le s}}
  n_{r,q,s-r}c_r^2.                                \tag{5.13.C21}
\]

Let `\mathcal U_r` be the split-`r` middle `b`-sets and `\mathcal V_(q,s)`
the split-`s` rank-`(b+q)` sets.  Join `U` to `V` when `U subset V`, set

\[
 \rho_{q,s}=\min(1,P_{q,s}/T_{q,s})
\]

when `T_(q,s)>0` and zero otherwise, and give a containment with
`r=|U cap A|`, `s=|V cap A|`, `z=s-r` weight

\[
 f_q(U,V)=\rho_{q,s}{n_{r,q,z}\over bD_{r,q,z}}.   \tag{5.13.C22}
\]

These weights form an exact fractional matching.  A fixed source sends at
most `b^(-1)sum_z n_(r,q,z)=1`.  A target of split `s` contains
`binom(s,r)binom(b+q-s,b-r)` split-`r` sources, and choosing a containment
flag in the other order gives

\[
 {{s\choose r}{b+q-s\choose b-r}\over
   {b-r\choose z}{r\choose q-z}}
 ={c_r^2\over P_{q,s}}.                            \tag{5.13.C23}
\]

Consequently every such target receives
`rho_(q,s)T_(q,s)/P_(q,s)=min(1,T_(q,s)/P_(q,s))`, and the profile receives
exactly `min(P_(q,s),T_(q,s))`.  Ordinary bipartite matching integrality
therefore supplies, separately for each `q`, a labelled containment matching
of size at least

\[
 \sum_s\min(P_{q,s},T_{q,s}),
\]

and (5.13.C10) makes the aggregate deficit of these separate matchings
`O(W_b b^(-1/4))=o(W_b)`.

Even the fractional cross-offset nesting is exact.  For each source choose
one clustered phase and independent uniform orders of the unused `A`- and
`B`-letters; at offset `q`, append the prefixes of lengths `z_q` and
`q-z_q`.  This gives one law

\[
 U=V_0\subset V_1\subset\cdots\subset V_H          \tag{5.13.C24}
\]

whose `q`th marginal is (5.13.C22) before the rankwise `rho` thinning.
The thinned marginals need not be a law of chains simultaneously real at
every rank, and the separate integral matchings need not be nested.

The physical occurrence-token row creates no further one-color obstruction.
For color `(r,z)` its token supply is

\[
 Q_{r,q,z}={n_{r,q,z}\over b}L_r.                  \tag{5.13.C25}
\]

This is an integer for prime `b`: every central `binom(b,r)` is divisible
by `b`, so `b^2` divides `L_r`.  Also `Q_(r,q,z)<=L_r` because
`n_(r,q,z)<=b`.

The containment graph between `\mathcal U_r` and `\mathcal V_(q,r+z)` is
biregular with degrees

\[
 d_L=D_{r,q,z},\qquad
 d_R={r+z\choose r}{b+q-r-z\choose b-r},
 \qquad L_rd_L=P_{q,r+z}d_R.                       \tag{5.13.C26}
\]

Hall by edge counting therefore matches its smaller shore.  The three-partite
hypergraph with shores consisting of `Q_(r,q,z)` tokens, the sources, and
the targets has matching number

\[
 \min(Q_{r,q,z},L_r,P_{q,r+z})
 =\min(Q_{r,q,z},P_{q,r+z}).                       \tag{5.13.C27}
\]

For a fixed `q`, projecting a token/source/target matching to its containment
edges is consequently an exact, size-preserving reduction to a Boolean
containment matching with the color caps
`|M cap E_(r,z)|<=Q_(r,q,z)`; conversely inject the selected edges of each
color into its tokens.  This collapses token identities, not the competition
among colors or the requirement that all tokens arise from common orders.

References:
`MATH_THEOREM_CLUSTERED_COMPLEMENTARY_PAYLOAD_ENDPOINT_COVERAGE_20260821.md`,
`MATH_THEOREM_CLUSTERED_FRACTIONAL_CONTAINMENT_TRANSPORT_20260821.md`, and
`MATH_THEOREM_CLUSTERED_FULL_ORBIT_LINKS_AND_COLOR_CAP_REDUCTION_20260821.md`.

#### Band-constant endpoint tokens have sublinear separate-offset deficit

There is a stronger simultaneous-phase capacity reduction.  Take the
canonical `H=Theta(sqrt(b log b))` and, in every clustered schedule
`A^rB^(b-r)`, discard every origin whose next `H` types cross a run
boundary.  Exactly `(r-H+1)_+` origins then give one all-`A` chain through
the whole upper band, while `(b-r-H+1)_+` give one all-`B` chain.  These
origins are fixed once, not chosen again at each offset.

At offset `q`, the two endpoint sources for split profile `s` have formal
capacity

\[
 E_{q,s}={1\over b}\left[
 (b-s-H+1)c_s^2+(s-q-H+1)c_{s-q}^2\right],         \tag{5.13.C27a}
\]

when both payloads are in the central quarter; charge all other profiles in
full.  Their aggregate tail mass is exponentially small.  Then

\[
 \boxed{\sum_{q=1}^H\sum_s[P_{q,s}-E_{q,s}]_+
 =O\left(W_b b^{-1/4}\log^{7/4}b\right)=o(W_b).}   \tag{5.13.C27b}
\]

Here is the localization proof.  Write

\[
 s={b+q\over2}+x,\qquad
 a={b-q\over2}-H+1,\qquad
 R={c_s\over c_{s-q}},\qquad u=\log R,\qquad
 \delta_q={q+2H-2\over b}.                         \tag{5.13.C27c}
\]

The exact ratio is

\[
 {E_{q,s}\over P_{q,s}}
 ={(a-x)R+(a+x)R^{-1}\over b}
 =(1-\delta_q)\cosh u-{2x\over b}\sinh u.         \tag{5.13.C27d}
\]

The signs of `u` and `x` are opposite, so the last term is nonnegative.
Thus a positive deficit is at most `delta_qP_(q,s)` and requires
`|u|<2\sqrt{\delta_q}`.  With `d=(b+1)/2`, the exact product

\[
 u(x)=\sum_{j=0}^{q-1}
 \log{d-(x+j-(q-1)/2)\over d+(x+j-(q-1)/2)}
\]

has `u(0)=0` and derivative at most `-4q/(b+1)`.  Hence every deficient
profile satisfies

\[
 |x|\le {b+1\over2q}\sqrt{\delta_q}
 =O\left({\sqrt{b(q+H)}\over q}\right).            \tag{5.13.C27e}
\]

The uniform Gaussian atom bound

\[
 {P_{q,s}\over W_b}\le {C\over\sqrt b}
 e^{-c(q^2+x^2)/b}
\]

therefore gives, for `D_q=sum_s[P_(q,s)-E_(q,s)]_+`,

\[
 {D_q\over W_b}\le
 Ce^{-cq^2/b}\left[{q+H\over b\sqrt b}
 +{(q+H)^{3/2}\over bq}\right].                   \tag{5.13.C27f}
\]

Sum this using `q+H<=2H` and
`sum_(q<=H)e^(-cq^2/b)/q=O(log b)` to obtain
(5.13.C27b); complementation gives the lower band.  This theorem removes
moving phase boundaries and all interior phase types from the scalar capacity
problem.  It also survives the separate-offset token integrality constraints.

For a source `U` of split `r`, give an all-`B` containment `U subset V`
weight

\[
 f_q^\circ(U,V)=
 \rho_{q,r}{b-r-H+1\over b{r\choose q}},           \tag{5.13.C27g}
\]

and an all-`A` containment, whose target split is `r+q`, weight

\[
 f_q^\circ(U,V)=
 \rho_{q,r+q}{r-H+1\over b{b-r\choose q}},
 \qquad
 \rho_{q,s}=\min(1,P_{q,s}/E_{q,s}),               \tag{5.13.C27h}
\]

with the zero convention.  The source load is at most

\[
 {b-r-H+1+r-H+1\over b}\le1.                      \tag{5.13.C27i}
\]

The same choose-in-two-orders identity as (5.13.C23) shows that every target
in profile `s` receives `min(1,E_(q,s)/P_(q,s))`; hence the flow has mass

\[
 F_q^\circ=\sum_s\min(P_{q,s},E_{q,s}).             \tag{5.13.C27j}
\]

Split the two endpoint types into their actual
`(r-H+1)L_r/b` and `(b-r-H+1)L_r/b` band-constant occurrence tokens and
divide the corresponding weights uniformly among them.  On the central
quarter the resulting 3-uniform token/source/target fractional matching has
maximum pair load

\[
 \alpha_q^\circ\le
 {1\over{\lfloor b/4\rfloor\choose q}}+e^{-\Omega(b)}. \tag{5.13.C27k}
\]

For source-target pairs this is the reciprocal of an endpoint extension
degree; token-source and token-target pairs have exponentially small load.
Applying the sampling and Molloy--Reed argument of (5.13.C42)--(5.13.C46)
therefore gives separate integral matchings `\mathcal M_q^\circ`, using only
band-constant endpoint tokens, with

\[
 \boxed{\sum_{q=1}^H
 \left[{2b\choose b+q}-|\mathcal M_q^\circ|\right]=o(W_b).} \tag{5.13.C27l}
\]

Indeed, the scalar part is (5.13.C27b), the `q=1` rounding loss is
`O(W_b b^(-1/3)log^4b)`, and the sum for `q>=2` is
`O(HW_b b^(-2/3)log^4b)=o(W_b)`.  Equation (5.13.C27l) is an integral
endpoint-**orbit** theorem, not one physical family: its selected sources and
tokens may depend on `q`, and its targets need not be nested.  It neither
matches one labelled extension chain through all offsets nor makes the
cyclic orders belong to compatible tight-cycle factors.  The remaining
endpoint problem is a physical two-family order-bank transport/absorption
theorem with phase consistency already built in.

Reference:
`MATH_THEOREM_CONSTANT_ORIGIN_ENDPOINT_PROFILE_CAPACITY_20260821.md`.

#### Product-SCD matchings solve the separate token problems

There is an explicit labelled solution at `q=1` which also supplies the
prototype for every fixed offset.  Write `b=2h+1`, fix arbitrary symmetric
chain decompositions of the Boolean lattices on `A,B`, and put

\[
 c_d={b\choose d}-{b\choose d-1},\qquad 0\le d\le h. \tag{5.13.C28}
\]

There are `c_d` chains with bottom rank `d`.  A pair with bottoms `a,c`
has rank-`b` source diagonal `r in [max(a,c),b-max(a,c)]`.  At `q=1`, if
`a<c`, match the whole target diagonal by adding the next `A`-set in its
chain; if `a>c`, match it by adding the next `B`-set; discard `a=c`.
Different rectangles have disjoint labelled sources and targets.

For `t<=h`, set

\[
 S_t=\sum_{d\le t}c_d={b\choose t},\qquad
 E_t=\sum_{d\le t}c_d^2,\qquad
 F_t={S_t^2-E_t\over2}.                            \tag{5.13.C29}
\]

The two oriented off-diagonal loads at source split `r` both equal
`F_(min(r,b-r))`.  They respect the clustered capacities
`Q_r^A=r binom(b,r)^2/b` and
`Q_r^B=(b-r)binom(b,r)^2/b`, because

\[
 E_t\ge {b-2t\over b}S_t^2,\qquad
 F_t\le {t\over b}S_t^2.                          \tag{5.13.C30}
\]

For completeness, (5.13.C30) is an induction.  With
`x=S_(t-1)/S_t=t/(b-t+1)`, its left side divided by `S_t^2` is at least

\[
 {b-2t+2\over b}x^2+(1-x)^2
 ={b-2t\over b}+{2t\over b(b-t+1)}.
\]

The exact discarded target count is

\[
 D_b=\sum_{d=0}^h c_d^2(b-2d)=O(W_b/\sqrt b).       \tag{5.13.C31}
\]

Indeed, writing `d=h-k`,

\[
 c_{h-k}={b\choose h-k}{2k+2\over h+k+2},\qquad
 {{b\choose h-k}\over{b\choose h}}
 \le e^{-k(k+1)/b};                                \tag{5.13.C32}
\]

the resulting Gaussian sum is `O(\binom(b,h)^2)`, and
`\binom(b,h)^2=O(W_b/\sqrt b)`.  Deleting the exponentially few sources
outside `[H+2,b-H-2]` leaves a genuine central-payload tokenwise matching of
size

\[
 {2b\choose b+1}-O(W_b/\sqrt b).                   \tag{5.13.C33}
\]

The same rectangles give a theorem at general `q`.  For a pair of chain
bottoms `a,c`, put `d=max(a,c)`.  Its source and target local-`A` intervals
are

\[
 R_{a,c}=[d,b-d],\qquad
 S_{a,c}^{(q)}=[\max(a,c+q),\min(b-a,b-c+q)].       \tag{5.13.C34}
\]

A constant shift `s\mapsto r=s-z` saturates the nonempty target interval
exactly when

\[
 z\in
 [\min(q,\max(0,c-a)),\ \max(0,\min(q,q+c-a))].   \tag{5.13.C35}
\]

This follows simply by imposing `R` membership on both endpoints and
`0<=z<=q`.  Hence every unequal-bottom rectangle is target-saturated by
shift `z=0` when `a>c` and by `z=q` when `c>a`, including the near pairs
`|a-c|<q`.  The two endpoint-color loads are at most the same `F_t` as in
(5.13.C29), while their capacities are the `q=1` capacities reduced by
`(q-1)binom(b,r)^2/b`.  Deleting at most

\[
 {2(q-1)\over b}W_b                              \tag{5.13.C36}
\]

edges removes every overload.  The equal-bottom target loss is exactly

\[
 E_{b,q}=\sum_{d=0}^h c_d^2[b-2d-q+1]_+
 \le D_b.                                          \tag{5.13.C37}
\]

Thus for every `q<=H=o(b)` there is a color-cap-respecting tokenwise
matching of size at least

\[
 {2b\choose b+q}
 -O\left(W_b/\sqrt b+qW_b/b+e^{-\Omega(b)}W_b\right). \tag{5.13.C38}
\]

For `q=o(sqrt b)` this is `(1-o(1))W_b`; summing this particular explicit
construction over `q<=Q` gives total `o(W_b)` error only for
`Q=o(sqrt b)`, not for the canonical DCC band.

The discarded equal-bottom rectangles have an exact integral augmentation
form.  Let `J` be any retained source-rank set, let `m_d=c_d^2`, and for
shift `z` retain the interval

\[
 I_{d,z}=J\cap[d+q-z,b-d-z].                       \tag{5.13.C39}
\]

If `R_(r,z)` is an arbitrary integral residual color capacity and
`x_(d,z)` counts level-`d` rectangles assigned shift `z`, feasibility is
equivalent to

\[
 \sum_zx_{d,z}\le m_d,\qquad
 \sum_{d\le\min(h,t_z(r))}x_{d,z}\le R_{r,z},
 \qquad t_z(r)=\min(r-q+z,b-r-z).                 \tag{5.13.C40}
\]

These are prefix constraints and hence a one-commodity flow.  For each
`d`, send the `m_d` units either directly to the sink or into a color chain

\[
 Z_{z,0}\longrightarrow Z_{z,1}\longrightarrow\cdots
 \longrightarrow Z_{z,h+1}\longrightarrow t.
\]

The arc after prefix `k` has capacity

\[
 B_{z,k}=\min\bigl(\{R_{r,z}:\min(h,t_z(r))=k\}
                  \cup\{\sum_dm_d\}\bigr),        \tag{5.13.C41}
\]

and an arc from supply `d` into `Z_(z,d)` has cost minus the desired weight
of assigning `(d,z)`.  Flow on that arc is `x_(d,z)`; conservation makes the
chain-arc flow exactly `sum_(d<=k)x_(d,z)`.  This proves a weight-preserving
correspondence with (5.13.C40), so integral min-cost flow gives an integral
optimum.  It proves no residual-capacity lower bound and couples neither
different offsets nor physical orders.

The full canonical range of offsets is nevertheless solved in the
**separate-offset token relaxation** by small-codegree rounding.  Strengthen
the payload truncation to
`J=[g,b-g]`, `g=floor(b/4)`; its total loss is exponentially small.  For a
fixed `q`, form the 3-uniform hypergraph whose vertices are the tokens of
each color `(r,z)`, the retained sources, and the upper targets, and whose
edges are compatible triples `(o,U,V)`.  Lift (5.13.C22) by

\[
 \theta_q(o,U,V)={f_q(U,V)\over Q_{r,q,z}}.         \tag{5.13.C42}
\]

It has mass `F_q=sum_s min(P_(q,s),T_(q,s))`.  Its maximum weighted pair
load obeys

\[
 \alpha_q:=\max_{x\ne y}\sum_{e\supset\{x,y\}}\theta_q(e)
 \le {1\over{g\choose q}}+e^{-\Omega(b)}.          \tag{5.13.C43}
\]

For a source-target pair this is `f_q(U,V)<=1/D_(r,q,z)` and
`D_(r,q,z)>=binom(g,q)`; token-source and token-target loads are at most
`L_r^(-1)` and `P_(q,s)^(-1)`, respectively.

We use the quantitative fixed-uniformity Molloy--Reed edge-coloring
consequence: after sampling a fractional matching at a scale `D` with
`D max_e theta(e)<=1` and `D alpha` dominating the logarithm of the vertex
count, the sampled `k`-graph has
`Delta<=(1+o(1))D`, `Delta_2<=(1+o(1))Dalpha`, and can be colored with

\[
 D\left[1+O_k\bigl(\alpha^{1/k}
                       \log^4(1/\alpha)\bigr)
     +o(1)\right]                                  \tag{5.13.C44}
\]

matchings.  Chernoff bounds give `(1-o(1))D\theta(\mathcal H)` sampled edges,
so the largest color class gives the corresponding integral matching bound.
Here all nonzero token classes are exponential, while
`binom(g,q)^(-1)=exp(-o(b))` for
`q<=H=Theta(sqrt(b log b))`; hence one may take `D=exp(cb)` and make the
sampling error `o(W_b/H)` uniformly.

With `beta_q=\binom(g,q)^(-1)`, this yields separate matchings `\mathcal M_q`
such that

\[
 F_q-|\mathcal M_q|
 \le O\bigl(F_q\beta_q^{1/3}\log^4(1/\beta_q)\bigr)
      +o(W_b/H).                                    \tag{5.13.C45}
\]

The `q=1` loss is `O(W_b b^(-1/3)log^4b)=o(W_b)`.  For `q>=2`,
`beta_q<=binom(g,2)^(-1)`, so the total rounding loss is

\[
 O(HW_b b^{-2/3}\log^4b)
 =O(W_b b^{-1/6}\log^{9/2}b)=o(W_b).               \tag{5.13.C46}
\]

Adding (5.13.C10) and the tail charge proves

\[
 \boxed{\sum_{q=1}^H
 \left[{2b\choose b+q}-|\mathcal M_q|\right]=o(W_b),} \tag{5.13.C47}
\]

and complementation gives the lower offsets.  The matchings in
(5.13.C47) may use different sources and phases and need not be nested;
they are not a physical product word or a tight-factor construction.

References:
`MATH_THEOREM_Q1_PRODUCT_SCD_COLOR_CAP_MATCHING_20260821.md`,
`MATH_THEOREM_PRODUCT_SCD_GENERAL_Q_FAR_RECTANGLE_MATCHING_AND_SHIFT_GATE_20260821.md`,
`MATH_THEOREM_EQUAL_BOTTOM_SHIFT_AUGMENTATION_IS_NETWORK_FLOW_20260821.md`,
and
`MATH_THEOREM_ALL_OFFSET_TOKEN_ORBIT_SMALL_CODEGREE_ROUNDING_20260821.md`.

#### The canonical hook SCD has a linear interior-phase overload

A tempting simultaneous lift is now ruled out at the correct scale.  Pair
local symmetric chains with bottoms `a,c` and edge lengths
`p=b-2a`, `ell=b-2c`.  In their product grid, the middle diagonal is
`i+j=b-a-c=(p+ell)/2`.  If `a>=c`, partition the grid into the hooks

\[
 C_k:(k,0),(k,1),\ldots,(k,\ell-k),
      (k+1,\ell-k),\ldots,(p,\ell-k),
 \quad0\le k\le p,                                 \tag{5.13.C47a}
\]

and transpose this construction if `a<c`.  A cell `(i,j)` below the bend
belongs to `C_i`, while a cell above it belongs to `C_(ell-j)`; this proves
partition and uniqueness.  Each hook starts at relative rank `k`, ends at
`p+ell-k`, and is symmetric.  Above its unique middle vertex its side word
is

\[
 B^{a-c}A^{b-2a-k}\quad(a\ge c),
 \qquad
 A^{c-a}B^{b-2c-k}\quad(a<c).                      \tag{5.13.C47b}
\]

Consequently the exact number of hooks in the rectangle reaching offset
`q`, and their number `z` of `A`-steps in the first `q` post-middle steps,
are

\[
 N_{a,c}^{(q)}=
 \left[b-2\max(a,c)+1-(q-|a-c|)_+\right]_+,        \tag{5.13.C47c}
\]

\[
 z_q(a,c)=
 \begin{cases}
 (q-a+c)_+,&a\ge c,\\
 \min(q,c-a),&a<c.
 \end{cases}                                       \tag{5.13.C47d}
\]

These follow by counting the active hook indices and reading (5.13.C47b).
Since there are `c_ac_c` rectangles with those bottoms, the total canonical
hook demand in the interior phase colors `1<=z<=q-1` is exactly

\[
 H_q^{\rm int}=
 2\sum_{\substack{0\le a<c\le h\\c-a<q}}
 c_ac_cN_{a,c}^{(q)}.                              \tag{5.13.C47e}
\]

By contrast, on any genuine central payload interval `I`, every interior
clustered color has only two phase origins, so all such colors together have
capacity

\[
 Q_q^{\rm int}(I)={2(q-1)\over b}
 \sum_{r\in I}{b\choose r}^2
 \le {2(q-1)\over b}W_b.                           \tag{5.13.C47f}
\]

There is an absolute `eta>0` such that, uniformly for
`sqrt b<=q<=2sqrt b`,

\[
 H_q^{\rm int}(I)\ge\eta W_b,
 \qquad Q_q^{\rm int}(I)=O(W_b/\sqrt b),            \tag{5.13.C47g}
\]

provided `H/sqrt b->infinity` and `I=[H+2,b-H-2]`.  Here is the complete
lower-bound box.  Write `a=h-i,c=h-j` and take

\[
 2q\le j\le9q/4,qquad 5q/2\le i\le11q/4.
\]

There are `Omega(q^2)` pairs, with `0<c-a=i-j<q` and
`N_(a,c)^(q)=i+j+2-q>=3q`.  Uniformly for
`2sqrt b<=k<=6sqrt b`, the product formula for the binomial ratio gives

\[
 c_{h-k}\ge\gamma {k\over b}{b\choose h}
\]

for an absolute `gamma>0`.  Substitution in (5.13.C47e) gives

\[
 H_q^{\rm int}\ge
 \gamma_1{q^5\over b^2}{b\choose h}^2
 \ge\gamma_2\sqrt b\,{b\choose h}^2
 =\Omega(W_b).
\]

The active source splits in this box lie between
`h-i+q` and `h+j+1`, hence in `I`.  This proves (5.13.C47g).  Therefore an
unchanged canonical-hook injection must delete or non-hook-reroute
`Omega(W_b)` incidences at **each** such offset, and its summed unchanged
deficit on this window is `Omega(sqrt b W_b)`.

The two natural discard ledgers do not repair this.  Equal-bottom rectangles
contain exactly

\[
 E_{b,q}=\sum_{d=0}^h c_d^2[b-2d-q+1]_+
\]

offset-`q` targets, and

\[
 \sum_{q=1}^H E_{b,q}=(3/4+o(1))W_b               \tag{5.13.C47h}
\]

whenever `H/sqrt b->infinity` and `H=o(b^(2/3))`.  Indeed the untruncated
sum is `1/2 sum_d c_d^2(b-2d)(b-2d+1)`; with `d=h-k`, the local estimate
`c_(h-k)/\binom(b,h)=(4k/b)e^(-2k^2/b)(1+o(1))`
reduces it to
`32\int_0^\infty x^4e^(-4x^2)dx=3\sqrt\pi/8`, while
`\binom(b,h)^2\sqrt b/W_b->2/\sqrt\pi`.  The tail past `H` is Gaussian-small.
On the other hand, deleting hook targets whose middle source lies outside
`I` costs at most
`H sum_(r notin I)binom(b,r)^2=o(W_b)`.

This is a barrier to the canonical product-hook SCD and to repairs changing
only `o(W_b)` of its offset-`q` incidences.  It does not refute noncanonical
product-SCDs, adaptive or mixed within-rectangle paths, the equal-bottom
flow, or a bespoke absorber.  Tight-cycle factors are not used in the
combinatorial overload; interpreting the capacities in (5.13.C47f) as
physical occurrence tokens remains conditional on those factors.

Reference:
`MATH_BARRIER_PRODUCT_HOOK_SCD_INTERIOR_PHASE_OVERLOAD_20260821.md`.

#### Coinstantiation and common-order barriers

The preceding integral token theorem is not an automatic total-unimodularity
statement.  In the first joint slot/source/target formulation a column is an
individually realizable triple `(o,U,V)` and the three unit-capacity row
families are the slots, middle labels, and upper labels.  At
`b=11,q=1,r=5,z=1`, take two slots `o_1,o_2`, flags

\[
 U_1\subset V_1,\qquad U_2\subset V_2,
 \qquad U_1\subset V_2,
\]

all of split `(5,6) -> (6,6)`, and columns

\[
 (o_1,U_1,V_1),\qquad(o_1,U_2,V_2),\qquad(o_2,U_1,V_2).
\]

On rows `o_1,U_1,V_2` their matrix is

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad\det=-2.                                    \tag{5.13.C48}
\]

The half-vector has value `3/2`, while every pair of columns conflicts and
the restricted integral optimum is one.  This kills bare TU, network-flow,
or two-matroid reasoning for the three row families, not dense-system
rounding: (5.13.C47) proves that the full token orbit has enough additional
columns.

Failure of automatic integrality persists after fixing actual labelled
factors and origins.  At `b=5`, the two cycles `01234` and `02413` partition
the pairs on each side; their complementary three-decks partition the
triples.  With schedule `AABBB`, take

\[
 c_1=(01234,01234;3),\quad
 c_2=(01234,01234;0),\quad
 c_3=(01234,02413;1),
\]

where the last coordinate is the relative origin, and put

\[
 V_1=\{a_0,a_1,b_0,b_1,b_2,b_3\},\qquad
 V_2=\{a_0,a_1,b_0,b_1,b_2,b_4\}.
\]

Directly sliding the three cyclic words gives `V_1` in exactly `c_1,c_3`
and `V_2` in exactly `c_2,c_3`; the common-order-pair item row contains
exactly `c_1,c_2`.  Hence these rows and columns give (5.13.C48).  For the
complete twenty-origin-column physical packing system the exact fractional
and integral optima are

\[
 \operatorname{LP}=10/3,
 \qquad \operatorname{IP}=2.                       \tag{5.13.C49}
\]

There is an exact family for every odd `b>=5`.  Let
`F=(b-1)/2`, take Walecki Hamilton decompositions
`{alpha_i}_(i<=F),{beta_j}_(j<=F)`, and use every origin of every order pair
with schedule `A^2B^(b-2)`.  For fixed `alpha_i`, the `b` origins of any
`(alpha_i,beta_j)` contain `b(b-2)` members of the same `b^2`-element
split-`(2,b-1)` family

\[
 \mathcal P_i=\mathcal D_2(\alpha_i)\times {B\choose b-1}. \tag{5.13.C50}
\]

The remaining two phases lie in the disjoint families
`\mathcal D_3(\alpha_i)\times\mathcal D_{b-2}(\beta_j)` and have multiplicity
two across the origins.  The `\mathcal P_i` are disjoint because the
rank-two decks form a factor.  The other families are disjoint in `j` by
the complementary rank-`(b-2)` factor and in `i` because a common cyclic
three-set in two edge-disjoint Hamilton cycles would make their two induced
two-edge paths share an edge.  Summing the target rows in `\mathcal P_i` bounds
fractional mass with fixed `i` by `b/(b-2)`.  Conversely, weight every one
of the `F^2b` columns by `1/[F(b-2)]`; its `\mathcal P_i` load is one, its
other target load is `2/[F(b-2)]`, and its item load is
`b/[F(b-2)]<=1`.  Two integral candidates with the same `i` but different
`B` orders intersect because `2b(b-2)>b^2`; two origins of the same order
pair are already excluded by its item row.  Candidates with distinct `i`
are disjoint.
Therefore

\[
 \boxed{\operatorname{LP}(b)={Fb\over b-2},\qquad
        \operatorname{IP}(b)=F,\qquad
        {\operatorname{LP}\over\operatorname{IP}}={b\over b-2}.} \tag{5.13.C51}
\]

The ratio tends to one and the witness is at the negligible extreme payload
`r=2`; it is not a linear coefficient-one obstruction.  The direct factor
independence system is not a matroid either: on `[5]`, the cycles
`C=01234` and `C'=02413` have disjoint pair decks, whereas the cycle
`D=02134` meets both.  Thus `{D}` cannot be augmented by either member of
the larger independent set `{C,C'}`.

Independent relabeling also remains decisively wrong even when all `q+1`
payload sources are retained.  Under mutually independent rank-and-side
conjugations, fix a rank-`(b+q)` target of split `s` and let `N_z` be its
occurrence multiplicity from payload `r=s-z`.  The `N_z`, `0<=z<=q`, are
independent, since they use disjoint conjugation coordinates, and their
means are

\[
 \lambda_0={b-s-q+1\over b}{c_s\over c_{s-q}},
 \qquad
 \lambda_q={s-2q+1\over b}{c_{s-q}\over c_s},      \tag{5.13.C52}
\]

\[
 \lambda_z={2\over b}{c_{s-z}^2\over c_sc_{s-q}}
 \quad(1\le z\le q-1).                             \tag{5.13.C53}
\]

Uniformly for `q<=Q=o(sqrt b)` on a split window containing `1-o(1)` of
the targets, the endpoints are `1/2+o(1)` and every interior mean is
`(2+o(1))/b`.  This follows from the exact product for
`u=log(c_s/c_(s-q))`: on
`|s-(b+q)/2|<=L\sqrt b`, where `L->infinity` and `QL/\sqrt b->0`, one has
`u=o(1)`, and log-binomial second differences give
`c_(s-z)^2/(c_sc_(s-q))=1+o(1)`.

Markov and independence now give

\[
 \Pr(N_0=\cdots=N_q=0)
 \ge\prod_{z=0}^q(1-\lambda_z)=1/4-o(1).           \tag{5.13.C54}
\]

Hence, uniformly for `q<=Q=o(sqrt b)`, the expected miss is **at least**
`(1/4-o(1))binom(2b,b+q)`, and if `Q->infinity` the aggregate expected miss
is at least `(1/4-o(1))QW_b`.  Correlation must be extreme: if every
payload retains its product-uniform marginal and a correlated construction
has `o(1)` expected miss at one such rank, the two endpoint cover events
must each have probability `1/2+o(1)`, intersection `o(1)`, and covariance
`-1/4+o(1)`.  Interior sources have total cover probability `o(1)` by
(5.13.C53), so this follows from inclusion-exclusion.  These are statements
about independent/product-uniform conjugation laws, not a no-go for a
designed correlated bank.

There is also an exact obstruction to compiling the product-SCD matching
atom by atom with no changes.  In one payload-`r` atom, enumerate its local
intervals by `X_u,Y_v`.  At word position `t=bm+s`, the clustered schedule
gives

\[
 u=rm+a_s,qquad v=(b-r)m+b_s+\theta,qquad
 s=u+v-\theta\pmod b.                              \tag{5.13.C55}
\]

Thus the physical next side is `A` on exactly the `r` counter-sum diagonals
`theta+{0,...,r-1}` and `B` on the others.  If
`p_u=bot_A(X_u)` and `q_v=bot_B(Y_v)`, the SCD edge instead wants `A` when
`p_u<q_v`, `B` when `p_u>q_v`, and no edge on equality.

Every active comparison matrix has at least `min(r,b-r)` wrong-side cells,
for every origin.  Indeed, on diagonal `d`, sum
`p_u-q_(d-u)` over `u`; the sum `Delta=sum_up_u-sum_vq_v` is independent of
`d`.  If `Delta>0`, every physical `A` diagonal has a positive entry and
hence a cell wanting `B`; if `Delta<0`, use the `B` diagonals.  If
`Delta=0`, every nonzero diagonal has both signs.  Two identically zero
diagonals would give a nonzero period of `q`, and primality of `b` would
make both sequences the same constant, the inactive case.

If `M_r` SCD edges occur at split `r`, at least `M_r/b^2` atoms are active.
Summing the preceding bound over `b/3<=r<=2b/3`, which contains
`(1-o(1))W_b` selected sources, forces at least

\[
 \boxed{(1-o(1)){W_b\over3b}}                      \tag{5.13.C56}
\]

switches or deletions before the separate cyclic-successor constraint is
checked.  That latter constraint says an `A` edge from `X_u` must add the
actual successor `alpha_(u+r)`, and similarly on `B`; each label is the
entering successor of exactly `binom(b,r)/b` rank-`r` windows in a factor.
The lower bound (5.13.C56) is `o(W_b)`: it forbids a zero-switch compiler,
not an `o(W_b)` six-cycle or longer alternating absorber.

References:
`MATH_BARRIER_CLUSTERED_TOKEN_LABEL_COINSTANTIATION_NONTU_20260821.md`,
`MATH_BARRIER_FIXED_FACTOR_PHASE_LABEL_MATRIX_NONTU_20260821.md`,
`MATH_THEOREM_FULL_MULTIPLICITY_INDEPENDENT_RELABELING_AND_DYCK_NIBBLE_BARRIERS_20260821.md`,
and
`MATH_OBSTRUCTION_Q1_PRODUCT_SCD_COMMON_ORIGIN_DIAGONAL_20260821.md`.

#### Wreath and Dyck matching boundaries

The Petr--Turek Dyck formulation does not immediately supply the missing
small-codegree matching.  Put `n=2k+1`; make one slot for every Dyck path
of semilength `k` and one target vertex for every `k`-subset of `Z_n`.
For each permutation fixing zero and having the slot's rise/fall pattern,
take the hyperedge consisting of that slot and its `n` cyclic `k`-windows.
Petr--Turek's exact interval counts

\[
 \iota_k(k,l)={k\choose l}^2,
 \qquad
 \iota_k(k+1,l)={k\choose l-1}{k\choose l}         \tag{5.13.C57}
\]

show, after multiplying by the compatible label permutations, that every
slot and target has degree `k!^2`.  The mountain slot and the all-rise and
all-fall targets have codegree `k!^2`, so `Delta_2=Delta`.  More robustly,
if disjoint `k`-sets `S,T` partition the nonzero labels and
`a=|S cap A|>k/2`, ballot counting gives

\[
 {\operatorname{codeg}(S,T)\over k!^2}
 =\left({2a+1-k\over a+1}\right)^2.                \tag{5.13.C58}
\]

On a positive-density band `a-k/2=Theta(sqrt k)`, this is `Theta(1/k)`;
the pairs are vertex-disjoint, so projecting away the coverage constraints
of `o(\binom(2k,k))` targets cannot make
`k Delta_2/Delta=o(1)`.  This rules out the raw or negligibly
target-projected small-codegree nibble, not correlated thinning,
augmentation, or a theorem using the global interval geometry.

For the one-rank wreath hypergraph itself, let `1<=r<=b/2`, put
`M=binom(b,r)` and `D=r!(b-r)!`, and use one edge for the `b` cyclic
rank-`r` windows of each oriented cyclic order modulo rotation.  It is
`D`-regular.  If two targets have Johnson distance `d`, direct ordering of
the four interval blocks gives

\[
 {\operatorname{codeg}(S,T)\over D}
 ={2\over{r\choose d}{b-r\choose d}}
 \quad(1\le d<r).                                  \tag{5.13.C59}
\]

For disjoint `S,T` with `b=2r+q`, distributing the `q` outside symbols
between the two blocks gives instead

\[
 {\operatorname{codeg}(S,T)\over D}
 ={q+1\over{r+q\choose q}}.                        \tag{5.13.C60}
\]

Thus in the central regime `b=2r+q`, `r=Theta(b)`, and `q>=3`, the maximum
normalized pair codegree is `Theta(b^(-2))`; the full palette has the
favorable first-bite scale.  But density and one-point regularity do not
support iteration.  Fix `eta>0`, put `a=|A|` for a cut `A subset [b]`, and
assume `eta b<=a,r,b-a,b-r<=(1-eta)b`.  Put `mu=ar/b` and delete the one or two
balanced split levels

\[
 \mathcal K_A={S:|S\cap A|\in\{\lfloor\mu\rfloor,
                                  \lceil\mu\rceil\}\},
 \qquad \mathcal F_A={ [b]\choose r}\setminus\mathcal K_A. \tag{5.13.C61}
\]

Every wreath meets `\mathcal K_A`: along its cyclic windows the integer
counts `x_i=|S_i cap A|` change by at most one and have average `mu`, so
they cross `floor(mu)` or `ceil(mu)`.  Uniform Stirling estimates give
`|\mathcal K_A|=O(M/\sqrt b)`.  Nevertheless every ground-point degree in
`\mathcal F_A` equals

\[
 {r|\mathcal F_A|\over b}+O(Mb^{-3/2}).             \tag{5.13.C62}
\]

Indeed, if `L_j=binom(a,j)binom(b-a,r-j)`, the deleted degrees on the two
sides differ by at most
`b[a(b-a)]^(-1)sum_(j in K)|j-mu|L_j=O(Mb^(-3/2))`.

The same wreath-free support is exactly point-regular after a positive
near-unit tilt.  Set `z_S=|S cap A|-mu`,

\[
 A_1=\sum_{S\in\mathcal F_A}z_S,qquad
 A_2=\sum_{S\in\mathcal F_A}z_S^2,qquad
 y_S=1-{A_1\over A_2}z_S.                          \tag{5.13.C63}
\]

The deleted levels give `|A_1|=O(M/\sqrt b)`, while the exact hypergeometric
variance gives `A_2=Theta(Mb)`.  Hence
`y_S=1+O(b^(-1/2))>0`, its total mass is
`|mathcal F_A|-A_1^2/A_2=(1-O(b^(-1/2)))M`, and
`sum y_S(|S cap A|-mu)=0`, which by side symmetry makes every point load
equal.  Thus a residual of density `1-O(b^(-1/2))`, with almost exact
unweighted and exact fractional one-point regularity, can contain no wreath.
This refutes only a density/degree induction invariant; it neither proves
nor disproves an approximate growing-rank Baranyai--Katona factor.  A
successful nibble must preserve richer split-profile or global mixing.

References:
`MATH_THEOREM_FULL_MULTIPLICITY_INDEPENDENT_RELABELING_AND_DYCK_NIBBLE_BARRIERS_20260821.md`
and
`MATH_OBSTRUCTION_GROWING_RANK_WREATH_BALANCED_SLICE_RESIDUAL_20260821.md`.

#### Radius-two Walecki slices reduce to an open Johnson-code gate

There is a precise partition-based bypass which is neither proved nor ruled
out.  Let

\[
 \Omega_b={ [2b]\choose b},\qquad W_b=|\Omega_b|,
 \qquad d_J(X,Y)=b-|X\cap Y|,
\]

and define the radius-two shell about `C` by

\[
 \Sigma_2(C)=\{X\in\Omega_b:d_J(X,C)=2\}.
\]

Writing `A=[2b]\setminus C`, `B=C`, this is exactly the split slice
`|X\cap A|=2`, `|X\cap B|=b-2`, of size

\[
 S_b=|\Sigma_2(C)|={b\choose2}^2.                 \tag{5.13.C64}
\]

For `b>=5` and distinct centers,

\[
 \boxed{\Sigma_2(C)\cap\Sigma_2(D)=\varnothing
 \quad\Longleftrightarrow\quad d_J(C,D)\ge5.}      \tag{5.13.C65}
\]

One direction is the triangle inequality.  Conversely let
`d=d_J(C,D)<=4` and partition the ground set into
`I=C\cap D`, `U=C\setminus D`, `V=D\setminus C`, and the outside `O`, of
sizes `b-d,d,d,b-d`.  Choose an integer
`max(0,d-2)<=t<=min(2,d)` and prescribe

\[
 |X\cap U|=|X\cap V|=t,qquad
 |X\cap I|=b-2-t,qquad |X\cap O|=2-t.             \tag{5.13.C66}
\]

All choices are feasible for `b>=5`, and the resulting `X` is at distance
two from both centers.  Hence disjoint shells are exactly constant-weight
binary codes of length `2b`, weight `b`, and minimum Hamming distance ten.
If `A(n,d,w)` is the maximum code size, asymptotically full shell packing is
equivalent to the open statement

\[
 \boxed{A(2b,10,b)\sim {W_b\over{b\choose2}^2}.}   \tag{5.13.C67}
\]

The closed Johnson ball of radius two has size

\[
 V_b=1+b^2+{b\choose2}^2=S_b(1+O(b^{-2})).
\]

Thus (5.13.C67) is equivalently an asymptotically perfect radius-two code,
`A(2b,10,b)V_b=(1-o(1))W_b`, meeting the Johnson sphere-packing bound to
relative error `o(1)`.

The associated shell hypergraph has vertex set `Omega_b` and edges
`Sigma_2(C)`.  It is `S_b`-uniform and `S_b`-regular, so edge weight
`1/S_b` is a perfect fractional matching.  If two vertices have Johnson
distance `d`, their codegree is exactly

\[
 \lambda_d=\sum_{t=0}^2
 {b-d\choose2+t-d}{d\choose t}^2{b-d\choose2-t},   \tag{5.13.C68}
\]

with out-of-range coefficients zero.  The four-part decomposition used in
(5.13.C66), now applied to the possible center, proves the formula.  In
particular,

\[
 \lambda_1=(b-1)^2(b-2),\quad
 \lambda_2=(b-2)(5b-11),\quad
 \lambda_3=18(b-3),\quad\lambda_4=36,
\]

and `lambda_d=0` for `d>=5`.  Therefore

\[
 {\Delta_2\over\Delta}={4(b-2)\over b^2}\sim{4\over b},
 \qquad
 S_b{\Delta_2\over\Delta}=\Theta(b^3).            \tag{5.13.C69}
\]

The vanishing normalized codegree does not supply growing-rank rounding:
the uniformity is `Theta(b^4)`.  Pippenger fixes uniformity, and in the
Ehard--Glock--Joos parameters one has at best `delta<=1/4`,
`epsilon=delta/(50S_b^2)=O(b^{-8})`; their required edge-count bound stays
bounded while this hypergraph has `W_b=exp(Theta(b))` edges.  The known
near-optimal constant-weight-code theorems cited in the source keep the
weight fixed, unlike `w=b=(2b)/2` here.

For odd `b`, Walecki factors already realize each individual rank-two shell.
If (5.13.C67) were proved, the corresponding
`Theta(W_b/b^4)` partitions would give `(1-o(1))W_b` pairwise disjoint
**middle targets**, and their `O(b)` connectors would cost only
`O(W_b/b^3)`.  This does not yet give the other DCC ranks.  The exact open
input is the integral packing (5.13.C67), or a Johnson-shell-specific
growing-rank matching theorem; the fractional matching and local codegrees
alone do not prove it.

Reference:
`MATH_REDUCTION_RADIUS2_JOHNSON_SHELL_PACKING_GATE_20260821.md`.

The two-stream torus also has a sharp recursion limit.  With `q` equal
`b`-cycle streams and an `L`-periodic type schedule, at each type phase the
counter vector lies in one translation orbit in `(Z_b)^q`, of size at most
`b`.  Hence at most `Lb` phase/counter states occur, whereas a Cartesian
atom needs `b^q`.  For `L=Theta(qb)`, this is impossible for every fixed
`q>=3` and large `b`.  Recursive amplification must use unequal/coprime
moduli, nonperiodic ranks, or a different wreath mechanism.

#### Scoped rainbow-endpoint gate

For a terminal recency state `pi=(x_1,...,x_n)`, define its legal rank-`m`
fan

\[
\mathcal N_f(\pi)=
 \{\{x_1,...,x_{m-1},x_j\}:f\le j\le n\}.           \tag{5.13.11}
\]

It has `d=m-H` colors.  If a color-simple legal path is unextendable, every
fan color is already used.  More generally, suppose each
`rho in E(P)` is the endpoint of a specified unextendable color-simple path
with exactly the same used owner-color set `U(P)`.  Then

\[
\bigcup_{\rho\in E(P)}\mathcal N_f(\rho)\subseteq U(P). \tag{5.13.12}
\]

This is the exact directed Posa endpoint criterion.  Direct whole-block
replacements inside a fixed common-transformation fiber leave the terminal
state unchanged, so they give only the original `d`-element fan.  Even all
orders above one fixed owner expose only its `m(m+1)` Johnson neighbours.
A useful Posa route therefore needs a variable-endpoint deck-preserving
splice or controlled small-exchange booster.  This statement concerns one
open-path owner deck; it proves neither full-band coverage nor cyclic
closure.

References:
`MATH_THEOREM_TWO_BLOCK_FIFO_PRODUCT_ATOMS_AND_LINEAR_SEAMS_20260821.md`
and `MATH_LEMMA_RAINBOW_POSA_ENDPOINT_GATE_AND_FIXED_FIBER_NOGO_20260821.md`.

## 6. Current `k=17` theorem frontier

The exact numerical status is

\[
\boxed{24313=B(17)\le\nu(17)\le25746.}
\]

The upper certificate is `answers/k17_upper25746.word`, SHA
`f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b`,
with independent exhaustive replay in
`MATH_THEOREM_K17_EXPLICIT_25746_UPPER_20260731.md`.  No length-24,313 word
and no proof of equality is known.

### 6.1 Necessary equality structure

Here `W=24310`, `d=3`, `Lambda=65535`, and the scalar short-window slack is
`7401`.  In the one-pivot flat equality architecture, the admitted cell atlas
has 24,313 singleton positions, 24,312 adjacent pairs, and 16,910 admissible
triples, totaling 65,535 cells.  These cells must biject onto all nonempty
targets of ranks at most eight (the K17-FRS condition).  Feasibility for any
chosen owner order is exactly the existence
of such a bijection satisfying every coordinate's positive and negative pin
intervals.  The tested contiguous-owner order fails this exact test.  This
refutes that architecture/order, not equality itself.

Coordinate deletion gives, for each coordinate, at least `nu(16)=12873`
letters avoiding it, equivalently at most 11,440 letters containing it in a
length-24,313 word.  If the byte-fixed optimal `k=16` word is required as the
entire unmarked subsequence, all internal insertion gaps kill an old target;
only the two endpoints are safe.  Every endpoint lift in that fixed deletion
fibre realizes at most 11,441 of the 12,870 marked rank-nine targets, leaving
deficiency at least 1,429.  Thus that fixed fibre is impossible; rethreaded
or different parents remain open.

References:
`MATH_THEOREM_K17_TIGHT_STAIRCASE_RAINBOW_GUARD_ORBIT_COMPILER_20260731.md`,
`MATH_THEOREM_K_ALL_COORDINATE_DELETION_CAP_AND_K17_SURPLUS_20260731.md`, and
`MATH_THEOREM_K17_SATURATED_COORDINATE_ENDPOINT_SPLIT_CEGAR_20260731.md`.

### 6.2 Strongest finite objects (not jointly composable)

The objects in this ledger are defined by their hashed instances.

1. A connected chronology of all 24,310 rank-nine owners has adjacent-owner
   unions covering all `19,448/19,448` rank-ten targets
   (`fullq1_13.best.model`, SHA
   `e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31`).
   Its two linear openings leave rank-11/12/13 hole profiles `(1528,288,6)`
   and `(1529,288,6)`; independent report SHA
   `6467b91bd7abb14a3ff381ef63a8dca86143e7c00d95caead04bdef8b957f2e2`.
2. A 24,310-owner depth-three suffix table assigns every one of the 65,535
   nonempty rank-at-most-eight targets exactly once; its depth histogram is
   `(1748,3899,18663)` and its SHA is
   `029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1`.
   In a distinct hashed lollipop state combining the table with a full-q1
   factor, the remaining rank-11/12/13 holes are `(1518,278,4)`; that state
   supplies neither literal serialization nor upper-rank closure.
3. In the canonical occurrence-pinned supplier instance (table SHA
   `fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`
   and bundle manifest
   `c1f696934bf93518c236d11d1fee570ec24b2b4b2a9a9e24de01e13526bab0c0`),
   the supplier incidence matrix has rank `16877/16898`, hence deficiency 21.
   The hashed restricted repair classes—unary source, authenticated two-mode
   drop-12 routes, and every branch of target-capable support-one no-`H`
   `S`-source triples—are exhausted and force bilateral recourse.  Bilateral
   or higher-arity child-local repair and different parents remain open.

These three bullets concern different occurrence states.  Combining them is
not a theorem.

Two further scoped no-gos remain useful: all 3,664 fixed round02 distinct-base
Hamming-two faces are DRAT-UNSAT (theorem SHA
`a2a0d71a6951242a7978b3f59d6f43c09c48ad9b983ab10481ab04cc9d592380`),
and every resource-feasible factor in the named clean1666/Y61423 bank/witness
basin that eliminates all named witnesses changes at least 1,561 facets (SHA
`52d24733c8799ae5fb55ef7c43d6a258cb5bc64ec2f30f6eadeee0e05beaa9e9`).
Neither is a global `k=17` no-go.
Finite `k=17` execution was deliberately stopped at item 2724ROOT; no stale
solver or fallback is authoritative.

## 7. Open conjectures and exact remaining gates

Everything in this section is open unless explicitly described as a proved
partial result above.  These statements are retained so work in progress is
not confused with either theorem or discarded chronology.

### 7.1 Global conjectures

1. **Exact formula:** `nu(k)=B(k)` for every `k`.  The first unknown case is
   `k=17`.
2. **Bounded additive gap:** `nu(k)<=B(k)+O(1)`.
3. **Asymptotic coefficient one:** with
   `W(k)=binom(k,floor(k/2))`, `nu(k)=(1+o(1))W(k)`.  The best full-cube
   theorem retained here is only `(sqrt(2)+o(1))W(k)`.

### 7.2 Standalone combinatorial conjectures

In items 5--10, `n=2m+1` and `W=binom(n,m)`.

1. **Sharp owner-chain chronology.**  At depth `d(k)` (or at
   `d(k)+O(1)`), assign every strict-lower target injectively to a labelled
   slot of a containing middle owner so each owner's assigned targets form a
   nested chain, the exact pin-survival tests hold, and the resulting decks
   admit one layered trace path.  Fractional chainization is exact and the
   known integral leave is `o(Lambda)`, but constant leave plus chronology is
   open.
2. **All-price configuration conjecture `FC_D`.**  In the job/socket model of
   Section 5.3 at coefficient one, does a nonnegative mixture of whole nested
   owner configurations cover every job while respecting every socket and
   every boundary price?  Its leading continuum relaxation asks whether the
   Rayleigh socket law can be coagulated into the required exact sums, but the
   finite shoulder and boundary rows remain additional constraints.  The
   associated odd-tropical integer-staircase covariance/Bellman sign is open;
   carry-aware positivity is known only for denominator grids of size at most
   three
   (`MATH_THEOREM_ENDPOINT_CRITICAL_ALL_ROW_ODD_TROPICAL_HIERARCHY_20260812.md`).
3. **Central cap-two selector.**  For every sufficiently large middle
   parameter `m`, does some odd Middle-Levels factor, in the same protected
   occurrence state as the rest of the construction, admit a binary choice of
   one occurrence for every upper colour such that each physical owner is used
   at most twice and the chosen duplicate pattern supports the required second
   factor?  Fractional feasibility and the abstract duplicate design are
   proved; the correlated integral choice is open.
4. **Exact common-basis physicalization.**  Upgrade the two independently
   constructed `P-o(P)` shore forests of Section 5.2 to exact, rooted,
   no-empty forests whose attachment union is acyclic for the same common
   basis.
5. **Cyclic-interval SCD resolution.**  For every `n=2m+1`, find
   Catalan-many cyclic orders and thresholds whose interval chains partition
   the full Boolean lattice.  The DCC of Section 5.6—near-`W` length, the
   stated cyclic letter gap, and total band-target defect `o(W)`—already
   implies asymptotic coefficient one.  Calibration: the rank-`m`
   trace of the exact version is the open Baranyai--Katona wreath
   conjecture at `(2m+1,m)`, so the exact form should not be attacked
   directly; the defective covering form of Section 5.6, which drops
   chains, thresholds, partition, and multiplicity, is the minimal
   sufficient object.
6. **Shallow multiscale wreath.**  At
   `h=(1+o(1))sqrt(m log log m)`, find one cyclic near-factor family `P` of
   total owner mass `W+o(W)` and one marked coordinate set `Z` with the
   following repair cost `o(W)`.  If `c_R` counts its shallow lower holes with
   trace `R subset Z`, pair `R` with `Z minus R`, put
   `c_Pi=c_R+c_(Z minus R)`, `L_|Z|=nu(n-|Z|)+1`, and require
   `Phi_h(P,Z)=sum_Pi min(c_Pi,L_|Z|)=o(W)`.
7. **Multidepth-rainbow splice.**  At the tail-compatible scale
   `H=(1+o(1))sqrt(m log log m)`, construct a
   depth-`H` geodesic middle forest for which

   \[
   Hc+\sum_{q\le H}(M_q^-+M_q^+)+(H^2+2H)\rho_H=o(W),
   \]

   where `c` is its component count, `M_q^-` and `M_q^+` are missing lower
   and upper depth-`q` targets, and `rho_H` is the total number of internal
   positive coordinate runs of length at most `H`.
8. **Mixed-Conjugate Resolution.**  For some parameter sequence with
   `H=sqrt(m omega(m))`, `omega(m)->infinity`, `H<ell=o(m)`, and
   `2ell exp(H^2/m)=o(m)`, form the
   augmented hypergraph whose zero-cost edges are complete length-`2ell`
   coordinate-conjugated blocks, carrying their transported radius and bundled with every certified lower/upper
   depth and whose unit-cost edges are singleton repairs.  Does it have an
   integral perfect matching of repair cost `o(W)`?  The exact fractional
   matching and `o(1)` typed codegrees are proved
   (`MIXED_CONJUGATE_RESOLUTION.md`).
9. **Central complementary bi-packing.**  The interval-packing parameters
   `(n,ell,r)=(2m,m-1,2)` lie outside the Dong--Mao theorem.  The needed
   strengthening asks for complementary palettes, matchings internal to each
   bank, and one acyclic common protected host; even a central packing alone
   would not supply that correlation.  This is a secondary alternative route.
10. **Intermediate letter scale.**  For letters of size
    `s=s(n)` with `1<<s<<m`, formulate a collar/run ledger and a central
    covering-defect ledger for windows of length about `m/s`.  Is there a
    scale at which covering hardness decreases faster than run hardness grows,
    yielding a coefficient-one construction?  The existing erosion
    (`s about m`) and singleton (`s=1`) obstructions do not answer this.

### 7.3 Current DCC/eligible-walk program

Sections 5.7--5.13 now isolate the singleton route at its correct level.
Pure uniform motion has a Poisson miss plateau, and approximate conditional
stationarity cannot improve it enough.  Exact cyclic closure, a linear
truncated-history connector, fractional capacity, and the post-path Hall
calculus are proved.  What remains is a bulk-correlated choice of one legal
physical trajectory.

Take `H=ceil(sqrt(n log n))`, `K={m-H,...,m+1+H}`, and the tail floor
`f=m+H+2`.  In any block architecture with `b` retained simple decks of
size `a`, put

\[
A=ab,\qquad M_k={n\choose k},\qquad R_k=\min(A,M_k),\qquad
V_k=\left|\bigcup_iU_{i,k}\right|.                  \tag{7.3.1}
\]

Subject to physical length `W+o(W)`, cyclic gap at least `f`, and `o(W)`
boundary charge, the exact postselection target is

\[
\boxed{\sum_{k\in K}(R_k-V_k)=o(W),\qquad
       \sum_{k\in K}(M_k-R_k)=o(W).}                \tag{7.3.2}
\]

By Section 5.12 this directly gives `DCC(n,H,o(1))` and hence
`nu(n)=(1+o(1))W`; no rank must be pre-matched.  Order the blocks and put

\[
u_{i,k}=\left|U_{i,k}\setminus\bigcup_{j<i}U_{j,k}\right|,
\qquad x_{i,k}=a-u_{i,k}.
\]

Thus `x_(i,k)` counts old-target hits
across blocks, not internal repetitions.  The first sum is exactly

\[
\sum_{k\in K}\left(\sum_i x_{i,k}-(A-R_k)\right).   \tag{7.3.3}
\]

Thus the constructive problem is simultaneous first-order freshness, after
subtracting the unavoidable outer-rank repeat allowance.  This criterion is
exact inside the retained-block/postselected-quota model; other DCC
architectures may account for their boundary observations differently.

The static prefix-multicover theorem shows that the union equations alone
are mutually compatible: exactly `W` permutation states can cover every rank
support simultaneously, with both middle ranks bijective and zero
quota-relative deficit everywhere.  What it does not provide is the object
needed here--a short legal chronology through those states.  Serializing them
individually has prohibitive transition cost, and no decomposition into
`o(W)` tail-MTF/FIFO atoms is known.

The equivalent global excess-repeat identity in Section 5.8 remains a
useful diagnostic.  On every growing inner subband `K_r` with
`r=o(sqrt(n))`, (7.3.2) forces the chosen nested central chain to be fresh at
`1-o(1)` of its ranks for almost the whole run.  The deterministic snub
ledger gives one sufficient feedback target: aggregate low-offer mass,
normalized within-rank crowding, and cross-rank column discordance are all
`o(W)`.  Conditionally neutral decks have a coupon-scale deficit in
expectation; mutually independent neutral decks have the same deficit with
high probability.  An `o(W)` terminal phase cannot repair a typical
stationary prefix.

Three live proof mechanisms are now cleanly separated.

1. **Central matching plus fixed-quota graphic completion.**  This is
   strictly stronger than (7.3.2), but remains useful.  Pairwise-disjoint
   rank-`m` decks plus total rooted graphic deficiency `o(W)` at the other
   ranks suffice in the fixed normalization
   `A=(1-o(1))W`, `M_k<=A` at every outer rank,
   `B_ch=o(W)`, and `|K|b=o(W)`.  Reachable branch abundance, quenched
   joint-pair bounds, and bounded component-square mass would prove it, but
   none is known and none is necessary for the adaptive-quota route.
2. **Growing-rank central nibble.**  Independently seeded free histories of
   length `Theta(n log n)` have exact relabeling marginals, normalized
   same-rank codegree `O(log n/n^2)`, and
   `r Delta_2/Delta=O(log^2 n/n)=o(1)`.  The `O(n)` connector physically
   lifts any central near-factor with only `O(W/log n)` central seam loss.
   One bite is proved in the exactly regular comparison model; the displayed
   palette itself is only almost regular, and iteration to `o(W)` leave is
   open.
   The equipartition construction (5.12.C1)--(5.12.C3) proves that these
   degree, pair-codegree, and squared-kernel parameters alone cannot justify
   iteration; a Johnson-specific anti-partition or residual-expansion input
   is required.
   Blindly charging these short seams at every band rank is not `o(W)`.
3. **Quadratic product atoms.**  The exact two-block atoms of Section 5.13
   are internally simple throughout the band and their `O(n)` seams have
   total full-band cost `o(W)`.  They exactly factor one split middle slice;
   the presently unproved conditional tight-cycle aggregation would cover
   almost every middle target.
   Clustered schedules align the torus phase maps at every offset and give an
   unconditional exact adjacent-rank MSW slice.  Conditional on the requisite
   growing-rank tight-cycle factors, the scalar profile deficit is
   `O(W_b b^(-1/4))`, one Ferrers columnization rounds all phase origins with
   the same aggregate deficit, and exact fractional containment is carried by
   a nested chain law.  Ordinary bipartite flow gives separate labelled
   containment matchings.  More strongly, the small-codegree token theorem
   gives, separately at every canonical offset, integral
   token/source/target matchings whose **total** target deficit is `o(W_b)`.
   Product-SCDs give explicit versions: at `q=1` their exact equal-bottom loss
   is `O(W_b/sqrt b)`; at general `q=o(b)` the per-offset loss is
   `O(W_b/sqrt b+qW_b/b)`, and the equal-bottom constant-shift augmentation is
   an integral min-cost flow for every fixed residual ledger.
   One can simplify further even at the separate token level: discard every
   origin whose next `H` types cross a clustered run boundary and keep only
   band-constant all-`A` and all-`B` chains.  Their scalar deficit is
   `O(W_b b^(-1/4)log^(7/4)b)`, and the endpoint-only lifted hypergraphs have
   separate integral matchings with aggregate `o(W_b)` target deficit.  The
   selections may depend on the offset and need not be nested or arise from
   compatible factor orders.

   The natural attempt to force simultaneous nestedness by taking the
   canonical product-hook SCD is not the missing lift.  For every
   `q in [sqrt b,2sqrt b]` it demands `Omega(W_b)` interior-color tokens,
   whereas the entire clustered interior palette has only
   `O(W_b/sqrt b)` capacity.  It therefore needs a linear number of
   non-hook reroutings at each such offset; simply deleting equal-bottom
   rectangles costs `(3/4+o(1))W_b` over the band.

   These are relaxation theorems.  Their offsetwise matchings may use
   different middle sources, phases, and nonnested targets, and their tokens
   need not arise from one common tight-factor order bank.  The first physical
   positive island is the complementary-payload theorem: on the balanced
   profile at every odd offset it uses common cyclic orders and origins and
   covers `(1/2-o(1))W_b` targets in aggregate with only
   `o(W_b)` holes.  The origins may be chosen to remain in one type run for
   the entire `H`-band, with hole charge
   `O(W_b/sqrt b+HW_b/b)`.  It physically covers no even offset or
   off-diagonal profile; the scalar theorem for all profiles does not supply
   those labelled targets.

   Literal equality of neighboring factor orders cannot extend this island
   through the band.  The forced bank-cardinality incompatibility summed to
   `Q` is `(1+o(1))Q^2W_b/sqrt(pi b)` for
   `1<<Q<<sqrt b`; it is already linear at `Q=Theta(b^(1/4))`, and one
   `q=Theta(sqrt b)` forces linear loss.  Conditional on the local factors,
   arbitrary nonidentical orders do not rescue the same physical bank: the
   exact CSP (5.13.C19k) and its
   zero-row/column bound imply `(Gamma_c-o(1))W_b` misses at every
   `q~c sqrt b`, even after all clustered interior phases are restored.
   Thus neither literal intersection, one-to-one pairing, nor many-to-many
   reassignment within the complete one-copy `A^rB^(b-r)` factor bank is the
   missing lift.

   Two simultaneous-all-offset questions are now solved at the relaxation
   level.  First, the product-SCD wider-side rule assigns one permanent
   constant side and one full `H`-chain to every middle source and covers
   every central target at every offset; for `H=o(b)` only an exponentially
   small extreme-profile charge remains.  Second, the explicit affine nested
   schedule is legal and internally simple inside each atom and has formal
   scalar deficit `O(W_b b^(-1/4)log^(3/4)b)=o(W_b)`.  Thus neither abstract
   cross-offset chain coinstantiation nor nested phase/profile capacity is
   the remaining gate.

   The affine scalar ledger has an exact joint interpretation, but not as an
   ordinary all-target chain matching.  Its raw whole-chain orbit has source
   and token load one and target load exactly `T_{q,s}/P_{q,s}`; nevertheless
   the rank-`(b+H)` shore alone forces
   `\Omega(\sqrt b\,W_b)` aggregate loss for every full-chain matching.  The
   correct shared-offset relaxation is the phase-preserving retirement LP
   (5.13.RT9)--(5.13.RT11).  Persistent alternating half-step phases now give
   an explicit feasible point with
   `\mathfrak D_{\mathrm{ret}}=o(W_b)` for
   `H=O(\sqrt{b\log b})`; its exact labelled lift has real-target incidence
   `\sum_{q\le H}M_q-o(W_b)` and maximum pair load `O(1/b)`.
   Thus the shared-offset scalar and labelled fractional retirement gates are
   solved.  An exact abstract layer-saturated counterexample with the same
   part sizes, vertex loads, chain format, and pair load at most `2/b` loses
   `\Omega(\sqrt b\,W_b)` integrally, so local nibble parameters cannot round
   it.  The affine Boolean object nevertheless does round: interleaving the
   two coordinate blocks in the Greene--Kleitman SCD makes every upper chain
   alternate, and longest-top selection within each persistent phase capacity
   gives an integral occurrence-token/source/labelled-target retired-chain
   matching of incidence `\sum_{q\le H}M_q-o(W_b)`.  Thus abstract integral
   growing-rank rounding is solved by global Boolean structure.  It still
   does not coinstantiate the chains in common cyclic factor orders or pack
   their full counter-translation orbits into product atoms.

   The most literal serialization of those GK chains is impossible.  In one
   fixed alternating linear order, the first GK addition `f(S)` is always
   below `max S`; under FIFO updating the maximum drops strictly every `b`
   steps, so every run stops within `b^2` updates and no cycle exists.  This
   blocks only the canonical first-successor rule, not atom-dependent
   conjugations, product translations, or a different successor map.

   Their physical lifts fail in sharply different ways.  For the affine
   schedule, almost all mesoscopic phase mass lies in one factor rank (even
   offsets) or two (odd offsets), leaving `\Omega_c(W_b)` deterministic or
   expected labelled misses under independent conjugations.  A uniform
   random nested schedule spreads every rank mass to `o(1)`, but leaves total
   mean at most one and hence an `(e^(-1)-o(1))` independent-coupon miss
   fraction throughout `q->infinity`, `q=o(sqrt(b/log b))`.  Finally, every
   physical torus side matrix is row-regular, while every complete cover on
   the fixed product-SCD trajectories is `(1/4-o(1))W_b` away in aggregate.
   The last statement is a compilation-distance bound, not the same number
   of missed targets.

   There is now an exact fixed-layer correlated-selector gate.  If each of
   `K_b` independent candidate factor banks hits every residual source/target
   pair at rate (5.13.SEL2) with `\eta_bK_b\to\infty`, a greedy sourcewise
   selector leaves only `o(M_q)` targets.  Uniform source marginals and exact
   mean target load do not imply that hypothesis: the containment covering
   map (5.13.SEL8) has the correct conjugated neighbor marginals but only an
   `O(1/b)` image fraction at `q\ge2`, so every polylogarithmic menu still
   matches `o(M_q)` targets.  The current factor hypotheses prove neither
   the residual-hitting condition nor its corrected nontransitive union
   audit (5.13.SEL12).  Even a positive sourcewise selector may choose
   different banks inside one indivisible product atom, so an atomwise
   coinstantiation theorem remains necessary.

   The remaining product gate is therefore either to coinstantiate and
   orbit-pack the explicit integral GK retired chains in common labelled
   factor orders, prove residual hitting and an atomwise lift for a
   polylogarithmic factor menu, or build a different correlated
   occurrence-to-target lift:
   change or correlate the multirank factor/order bank and its containment
   trajectories, change the atom geometry, or reroute a linear fraction of
   the existing atoms without paying linear extra length.  Independent rank
   conjugations, scalar capacity, an ordinary full-chain matching, and the
   fixed product-SCD compiler are now ruled out as sufficient.  Inside any
   new geometry one still needs simultaneous all-offset chain/factor-order
   realization and a common-origin/successor absorber.  A rigid
   one-to-one bank has `(1/2-o(1))W_b` holes; independent full-multiplicity
   relabeling misses at least a quarter of every low-offset layer in
   expectation.  A fixed-factor physical matrix is non-TU, but its explicit
   large-`b` gap has ratio `b/(b-2)->1` at an extreme payload and is not a
   coefficient-one obstruction.  The product-SCD matching cannot be lifted
   with zero atomwise switches: common origins force at least
   `(1-o(1))W_b/(3b)=o(W_b)` repairs.  Finally, a density
   `1-O(b^(-1/2))`, almost point-regular residual can be wreath-free; any
   direct growing-rank factor iteration must preserve a richer split-profile
   or global-mixing invariant.

   A separate rank-two partition bypass is exactly the open Johnson-code
   assertion
   `A(2b,10,b)~W_b/binom(b,2)^2`.  It would pack
   `Theta(W_b/b^4)` Walecki shells and cover `(1-o(1))W_b` disjoint middle
   targets with `O(W_b/b^3)` connector cost.  The shell hypergraph has a
   perfect fractional matching and normalized codegree `Theta(1/b)`, but
   uniformity `Theta(b^4)`; no audited rounding theorem proves the required
   asymptotically perfect code.  Even a proof would supply the middle layer
   only, not the DCC band.

The common-transformation entropy and deck-code theorems remain useful
local reservoirs, but with polynomial block length and exponentially many
slots, repeating one transformation after deleting only its endpoint has the
forced periodic suffix (5.12.15) and cannot supply an exact central deck
matching.  Dense residual stars and modular independent classes
refute a universal residual-size-only extension theorem at their audited
densities and run lengths; they do not exclude invariants special to the
reachable residual process.
Generic detached spanning-tree/negative-cylinder rounding does not lift to
whole FIFO paths; recomposition with `o(W)` resulting fragments cannot repair
linear defect; and fixed-endpoint replacements have no Posa endpoint
expansion.

There is also a sharp necessary correlation scale.  On the logarithmic
inner band of (5.12.H1), a successful selector has only `o(a)` old hits in
a typical selected block, while a uniform candidate at a middle-stage
residual has mean freshness at most `(2/3+o(1))as`.  Therefore the palette
must put at least `exp(-O(a log n))` mass on an `Omega(as)` upper deviation
and must exhibit positive all-fresh correlation on some
`Theta(a log n)` coordinates.  Negative association or an ordinary diffuse
subgaussian tail is incompatible with success; annealed one/two-point control
is merely insufficient and may coexist with the required high-order
alignment.  This is a design requirement, not a no-go for clustered
product/wreath structure.

The live conjecture is therefore to prove (7.3.2), either by a correlated
eligible-walk rule, an iterated growing-rank matching/augmentation theorem,
or coherent multirank product aggregation.  Once this bulk union freshness
is obtained, cyclic serialization and far-rank absorption are already
proved.

### 7.4 Route-specific construction gates

1. **Protected owner-cycle normality:** after `O(1)` terminal corrections,
   put the required all-owner demand in the nonnegative semigroup of protected
   closed-rail columns across overlapping cores, with occurrence-compatible
   lower flags.
2. **Protected upper forest:** find a Middle-Levels Hamilton cycle, or an
   equivalent upper-exact forest, containing the Catalan-scale prescribed
   collar stems.
3. **Conditioned lower lift:** make the birth-time/adjacent-depth lower construction
   survive the chosen upper chronology and residence, including separately
   priced boundary sockets.
4. **Resident proper-block selector:** cut the proved good pair-cell cycles
   into residue-carrying resident paths, cover every owner, and splice them
   without losing upper or adjacent-owner witnesses.
5. **All-width occurrence selector:** for every repeated adjacent-owner colour,
   choose one compatible occurrence while preserving every higher witness and
   a component-breaking forest.
6. **Topology:** satisfy component-port Hall, or build a protected octagon
   merger tree, while retaining the witness bank and residence.
7. **Private-prefix common-cap coinstantiation:** the compatible even suffix
   router is explicit once private prefixes are planted; the open task is to
   plant those literal prefixes with actual capacity-one cells in the same
   occurrence state as the owner/lower/upper construction.
8. **Layered serialization:** choose upper-complete owners and lower-complete
   flags for which the exact layered de Bruijn path of Section 5.3 exists.
9. **Regenerative coinstantiation:** local all-width current, parity, and the
   large phased host are proved.  Construct one recursively compatible
   successor spine that also carries residence, component fusion, and common
   cap while satisfying the bounded-convolution criterion of Section 5.4;
   unrelated good states in successive dimensions do not suffice.
10. **Finite `k=17`:** inside the canonical deficiency-21 parent, find a
    bilateral or higher-arity child-local supplier repair, or build a different
    complete owner/lower/upper state.  Success must still satisfy chronology,
    residence, ranks 11+, common cap, serialization, and one literal-word
    replay.

Any completion following this all-dimensional route must coinstantiate the
applicable structural gates in each dimension and transport one compatible
interface state; independent witnesses do not compose.  Gate 10 is the
separate finite `k=17` base problem, and alternative proof routes need not
pass through every listed gate.

## 8. Claims that must not be revived

- Fractional marginals, independently constructed per-rank Hall matchings,
  signed lattice span, or bounded codegrees do not by themselves imply one
  nonnegative **simultaneous physical** carrier.  This statement must not be
  misread as a fixed-offset matching obstruction: ordinary Boolean
  containment is bipartite-integral, and Section 5.13 now gives integral
  token/source/target matchings at every separate offset with aggregate
  `o(W_b)` deficit.  The alternating GK theorem now also gives one integral
  nested retired-chain matching on persistent affine phase tokens.  What
  remains is to coinstantiate such chains in shared cyclic factor orders and
  collision-free physical product atoms.  Determinant-two
  and determinant-three faces block automatic TU of more literal joint
  formulations; they do not contradict the dense token-rounding theorem or
  the conditional Hall-deficiency formulas in Sections 5.10 and 5.12, which
  start after the bare physical paths have been fixed.  Likewise, separately
  verified owner, lower, upper, residence, topology, and cap objects cannot
  be composed without a shared occurrence state.
- In particular, the exact fractional block-palette matching of Section 5.9
  is not an integral DCC.  Relative pair codegree `Theta(1/n)`, enormous
  degree, growing rank, and a fractional perfect matching do not suffice:
  the projective-decoration family there has the same generic parameter
  profile but matching number one.  Any rounding theorem must exploit the
  nested Boolean flags and the common tail-MTF path choice.
- Exact relabeling marginals and codegrees obtained from a uniform seed are
  **annealed** statements.  Conditioning a branch on avoidance of the
  evolving central residual can amplify postponed-rank pair probabilities
  arbitrarily.  Product-cell microblocks are independent before conditioning
  on whole-core simplicity or coverage; they need not remain independent
  afterward.
- The postselected-quota theorem does not make the earlier fixed-quota
  fractional hypergraph integral.  It applies only after bare physical paths
  have been chosen, when real/dummy claims can be assigned as bookkeeping;
  it reduces the remaining Hall calculation to global union size but does
  not choose paths with large unions.
- Conversely, the exact static family of `W` permutation states covering
  every rank support is not a physical union-cover construction.  It proves
  that the rankwise requirements are set-theoretically compatible, but gives
  no short order of the states, tail-MTF/FIFO joins, or control of observations
  made during transitions.  Serializing one state at a time destroys the
  coefficient-one length budget.
- The detached transition-edge vectors are exactly forest-roundable in the
  relevant graphic matroids, but an ordinary spanning-tree or
  negative-cylinder rounding almost surely contains no full legal palette
  path.  Conversely, whole path-bundle forest independence is not a matroid.
  Fractional graphic integrality therefore does not perform the required
  path lift.
- The estimates `r Delta_2/Delta=o(1)` and `Xi=o(1)`, together with the
  isolated-edge calculation (5.12.16e), validate one small bite in the
  exactly regular comparison model only; the displayed palette is merely
  almost regular.  They do not justify an exact regularization, iteration, a
  near-perfect central matching, or `o(W)` full-band union deficit.
- This failure is not merely a limitation of the proof.  The equipartition
  construction of (5.12.C1)--(5.12.C3) gives exact regular slot--target
  multihypergraphs with the same asymptotic values of
  `r Delta_2/Delta` and `Xi`, arbitrarily large absolute degree, but maximum
  matching covering only `O(1/n)` of the vertices.  It rules out every
  parameter-only iteration based on those local statistics; it is not a
  counterexample to the Johnson free-history palette, whose global structure
  could still supply the missing anti-partition or residual-expansion input.
- Exact one- and two-point freshness laws are also too weak for the adaptive
  union target.  On the logarithmic inner band, (5.12.H1)--(5.12.H7) show
  that almost every middle-stage block used by a successful construction
  must lie in an `exp(-O(a log n))` simultaneous-freshness upper tail, and
  some `Theta(a log n)` coordinates must be positively upper-orthant
  correlated.  Negative association, a product Chernoff law, or comparable
  diffuse subgaussian behavior cannot produce this.  This is a necessary
  alignment condition, not a no-go for clustered wreath/product structure.
- Collapsing each same-time nested flag to one atom removes the adjacent-rank
  pair codegree only by forgetting collisions of equal coordinate targets.
  Reintroducing those collisions as conflicts recreates a polynomially too
  large conflict degree; restricting in advance to a target-disjoint flag
  factor is precisely the unresolved tail-MTF-compatible chain-factor gate.
- On the canonical chordless palette support, fixing one slot's unordered
  middle deck permits at most one opposite-central target replacement.  Hence
  independent slotwise fiber switches alter only `o(W)` targets and cannot
  repair a linear parity defect.  This does not rule out rare chord-rich cores
  or global recomposition between slots.
- Pairwise `Omega(n)` replacement distance among retained rank-`m` decks in
  one fixed-endpoint code is local capacity only.  It neither hits a
  prescribed residual, preserves an already selected rank-`m` packing, nor
  implies `Omega(n)` new rank-`(m+1)` transition colors or cycle descent.
- Repeating a fixed full-state transformation after deleting only its final
  checkpoint does not free the rest of the endpoint collar.  Formula
  (5.12.15) forces `f-k` retained rank-`k` suffix targets, periodic with the
  transformation order; at rank `m` this prevents an exact deck matching on
  exponentially many slots.  The triangular expression (5.12.15a) is the
  raw forced-suffix mass; deleting one common suffix at every band rank costs
  `|K|q(K)`, asymptotically twice as much.  A one-checkpoint claim must not be
  revived.
- The `O(n)` truncated-history connector solves endpoint compatibility, not
  all seam accounting.  It gives `o(W)` central cost for `Theta(n log n)`
  cores and `o(W)` full-band cost for `Theta(n^2)` product atoms.  Blindly
  discarding its windows at every rank between shorter cores costs
  `O(|K|W/log n)`, which is not sublinear.
- Dense residual sets of the correct cardinalities need not admit even one
  next balanced core: Section 5.11 gives an exact hypergeometric/KL
  construction with unused density
  `1-Theta(n^(-1/3)(log n)^(2/3))`.  This refutes a universal next-core lemma
  based only on residual cardinalities or independently random residuals, not
  global near-factor methods or invariants special to dynamically reachable
  residuals.
- Even for the one-central formulation, the density-`1/2+o(1)` star of
  middle sets containing a fixed letter has no legal run longer than `m`,
  while each modular sum class has density exactly `1/n` and contains no
  Johnson edge.  These are counterexamples to arbitrary-residual extension,
  not evidence that a well-designed reachable residual process must fail.
- The unordered Middle-Levels graph has a linear distinct-color chord
  reservoir and an exact zero-defect abstract path cover, but these objects
  need not obey the FIFO identity `v_t=u_(t-m)`.  When the recomposed family
  uses `o(W)` resulting cores, repairing linear defect while keeping the same
  middle sets requires linearly many new temporal edges; cutting into `F`
  word fragments creates only `F(k-1)` new rank-`k`
  windows.  Sparse reset-separated recomposition is therefore not a lift.
- Exact two-block torus atoms and tight-cycle factors at their payload ranks
  do not imply coherent multirank coverage: internal simplicity says nothing
  about collisions between different atoms.  The same periodic torus trick
  cannot be recursively amplified with three or more equal streams in the
  natural regime `L=Theta(qb)`: an `L`-periodic schedule visits at most `Lb`
  counter states, while a Cartesian atom requires `b^q`.
- Clustered schedules solve the phase monotonicity problem only inside an
  aligned local-order bank.  If a rigid one-to-one common-order family
  partitions each relevant Cartesian profile, it still has exactly a `q/b`
  upper-profile hole fraction at offset `q`, summing to
  `(1/2-o(1))W_b` across the audited central offsets.  Conditional on the
  requisite tight-cycle factors, full-multiplicity independent rank-and-side
  relabeling leaves **at least** `(1/4-o(1))` of every rank
  `b+q`, uniformly for `q<=Q=o(sqrt b)`, uncovered in expectation; if
  `Q->infinity`, the aggregate expected miss is at least
  `(1/4-o(1))QW_b`.  This is an independent-law failure, not an impossibility
  for correlated banks; successful product-uniform marginals must make the
  two endpoint events almost disjoint, with covariance `-1/4+o(1)`.  The
  available layer-size surplus is sufficient rank by rank.  Under the same
  conditional factor premise, pooling all payload multiplicities leaves only
  `O(W_b b^(-1/4))=o(W_b)` split-profile capacity deficit.  Thus the rigid
  and independent ledgers must not be revived as volume impossibilities.
  Ferrers columns also give one simultaneous integral phase-origin rounding,
  labelled fractional containment lives on one nested chain law, and every
  separate-offset token relaxation rounds with aggregate `o(W_b)` loss.
  Phase-bin, Boolean-containment, and separate token integrality are therefore
  not the gate; compatibility of the **same labelled cyclic orders and
  nested sources across offsets** remains open.
- The constant-side product-SCD theorem removes the unrestricted
  set-theoretic all-offset chain-cover obstruction only.  It does not respect
  cyclic-factor origin caps or compile its SCD trajectories into physical
  torus atoms.  In fact every physical rank-`r` side matrix is row-regular,
  while every complete cover on those fixed product-SCD trajectories is
  `(1/4-o(1))W_b` away in aggregate Hamming distance.  That is a compiler
  distance, not an equal missed-target count; it does not obstruct different
  trajectories, correlated banks, or an absorber.
- The affine nested schedule closes the simultaneous scalar ledger, its
  persistent-alternation point closes the labelled fractional chain ledger,
  and the alternating GK construction closes the abstract labelled
  **integral** retired-chain ledger.  None of these coinstantiates common
  cyclic factor orders or physical product atoms.  The affine schedule's one
  or two dominant independently conjugated factor banks have
  `\Omega_c(W_b)` mesoscopic misses.  Replacing it by a uniform
  random nested schedule makes every coupon small but, under independent
  rank-and-side conjugations, still leaves at least an
  `(e^{-1}-o(1))` target fraction uncovered throughout
  `q\to\infty`, `q=o(\sqrt{b/\log b})`.  These are independent-bank
  barriers only; deliberate multirank correlation remains open.
- The raw affine whole-chain law has the exact scalar target marginals, but
  an ordinary full-`H` matching necessarily loses
  `\Omega(\sqrt b\,W_b)` in aggregate because every edge occupies the last
  rank.  The correct object is the phase-preserving retirement LP.  Every
  feasible retirement point has a labelled fractional lift, and the explicit
  persistent-alternation point now proves
  `\mathfrak D_{\mathrm{ret}}=o(W_b)` with pair load `O(1/b)`.  This does not
  imply integral rounding from local parameters.  Indeed, a layer-saturated
  abstract retired-chain hypergraph with the same layer sizes, maximum vertex load
  one, and pair load at most `2/b` has
  `\Omega(\sqrt b\,W_b)` integral target-incidence deficit.  The obstruction
  is parameter-only and not Boolean.  The alternating GK SCD supplies exactly
  the missing global structure and gives an integral occurrence-token,
  source, and labelled-target retired-chain matching with aggregate
  `o(W_b)` target deficit.  It does not give a common factor-order/product-atom
  realization.  Merging equal-profile nodes in a scalar flow still illegally
  switches path identity, and the determinant-two labelled face remains a
  warning about that formulation.
- The canonical GK first-successor FIFO map is not the missing physical lift.
  Its added coordinate is always below the current source maximum; that
  maximum drops strictly every `b` updates, so the process stops within
  `b^2` updates and has no cycle.  This rules out one fixed linear-order
  successor rule only.  Product translations, atom-dependent conjugations,
  and different successor maps remain possible.
- A polylogarithmic menu of independently conjugated banks is useful only
  after proving residual image expansion, not from one-point marginals or
  exact mean load.  The residual-hitting recurrence gives an
  `O((\eta K)^{-1})` fixed-layer miss fraction, and uniform same-target pair
  control is one sufficient hypothesis.  But a conjugated
  containment-respecting covering map has the correct uniform-neighbor
  marginal and mean load while a polylogarithmic menu matches only `o(M_q)`
  targets.  The general necessary audit is the nontransitive average
  `M_q^{-1}\sum_V(1-p_q(V))^K=o(1)`.  Even when sourcewise selection works,
  it may split one physical atom among several banks; no `K`-free physical
  length or coefficient-one conclusion follows without atomwise
  coinstantiation.
- The token/source/target incidence matrix and even a fixed-factor physical
  phase--label matrix contain determinant-two minors.  The fixed `b=5`
  physical LP has optimum `10/3` versus integer optimum `2`, and the Walecki
  family at every odd `b` has gap ratio `b/(b-2)`.  These facts rule out
  automatic TU/network-flow integrality of those literal formulations.  They
  are not coefficient-one no-gos: the large-`b` ratio tends to one, its
  witness is at the negligible payload `r=2`, and the full dense token
  hypergraph is separately roundable.  Likewise, the direct system of cyclic
  orders with disjoint rank-two decks is not a matroid, but a richer extended
  formulation is not excluded.
- The product-SCD constructions are actual labelled Boolean-containment
  matchings and respect the abstract clustered color caps.  They are still
  tokenwise: an occurrence token of a color cannot be relabelled independently
  once one factor order and origin is fixed.  At `q=1`, every active atom has
  a wrong common-origin diagonal, forcing at least
  `(1-o(1))W_b/(3b)` switches or deletions.  This forbids a zero-switch
  compiler only; the cost is `o(W_b)`, so cross-rectangle six-cycle or longer
  absorption remains viable.  The equal-bottom min-cost-flow theorem removes
  fixed-`q` integrality, not residual-capacity, cross-offset, or physical-order
  consistency.
- A simultaneous symmetric-chain lift cannot be justified merely because
  each post-middle chain word has at most one side switch.  In the canonical
  product-hook SCD, a positive target fraction switches at an interior time
  when `q=Theta(sqrt b)`, but each interior clustered color has only two
  origins.  This forces `Omega(W_b)` deletions or non-hook reroutings per
  audited offset; discarding all equal-bottom rectangles costs
  `(3/4+o(1))W_b` in aggregate.  This blocks the canonical hook and its
  `o(W_b)` modifications only, not adaptive/mixed product-SCDs, the
  endpoint-only constant-origin route, or a bespoke absorber.
- Complementary payloads physically cover `(1/2-o(1))W_b` targets across
  odd offsets with `o(W_b)` holes, conditional on the local factors; their
  origins may be constant in one type run throughout the entire band.
  This is only one balanced profile and its two endpoint phase types.  It
  does not physically cover even offsets or off-diagonal split profiles and
  does not by itself prove coefficient one.  Interior phase types are not
  needed for scalar capacity, but no labelled endpoint assignment follows.
- Literal common-order intersection is not a DCC-band extension of that
  theorem.  The different neighboring bank sizes force linear weighted
  incompatibility by `Q=Theta(b^(1/4))`, and one
  `q=Theta(sqrt b)` already forces `Theta(W_b)`.  This cardinality lower
  bound does not touch the complementary balanced diagonal, where the bank
  sizes agree.  Conditional on the local tight-cycle factors, the stronger
  exact nonidentical-order CSP treats the full endpoint bank: its
  zero-coordinate rows and columns force
  `(Gamma_c-o(1))W_b` misses at `q~c sqrt b`, while all restored interior
  phases contribute only `o(W_b)` occurrences.  Hence arbitrary
  conjugations, origins, one-to-one pairings, and many-to-many use of the
  same complete one-copy clustered bank cannot be repaired by `o(W_b)`
  seams.  This is not a general coefficient-one obstruction: it leaves
  changed type schedules, different factor/atom geometries, and linear-scale
  rerouting open.
- Keeping only common all-`A`/all-`B` origins through the whole band has
  `o(W_b)` pooled scalar endpoint deficit and, at every offset separately,
  integral token/source/target matchings with aggregate `o(W_b)` deficit.
  This still does not imply one simultaneous physical assignment: the chosen
  sources and tokens may change with `q`, the targets need not be nested, and
  the same cyclic order serves many sources.  The two endpoint families still
  require compatible factor banks and one common target-disjoint chain
  realization.  The CSP obstruction proves that such a realization cannot
  lie inside the unmodified one-copy clustered product-factor bank.
- The raw Petr--Turek Dyck-slot hypergraph is regular but has
  `Delta_2=Delta`; after projecting away `o(binomial(2k,k))` target
  constraints, a positive-density complementary-pair band still has
  normalized codegree `Theta(1/k)`.  This blocks only a direct generic
  small-codegree nibble.  Separately, a wreath-free residual can have density
  `1-O(b^(-1/2))`, point-degree variation `O(Mb^(-3/2))`, and an exact
  positive point-regular fractional weighting.  That refutes density plus
  one-point-regularity as an iteration invariant, not the growing-rank wreath
  conjecture or a split-profile-aware nibble.
- The radius-two Johnson-shell hypergraph has a perfect fractional matching
  and `Delta_2/Delta~4/b`, but its uniformity is
  `binom(b,2)^2=Theta(b^4)`.  These facts do not imply an asymptotically
  perfect shell packing; generic growing-rank counterexamples already forbid
  such an inference, and the audited constant-weight-code theorems keep the
  weight fixed rather than `b=n/2`.  The shell-code assertion remains an open
  middle-layer bypass, not a DCC construction.
- Fixed common-endpoint branch replacements have Posa endpoint family of
  size one.  Even all recency orders over one fixed owner expose only
  `m(m+1)` owner colors.  Endpoint expansion therefore requires a
  variable-endpoint deck-preserving splice or controlled exchange; local
  branch entropy and deck distance do not provide it.
- An alternating exchange confined to directed cycle arcs preserves every
  in/out degree and therefore cannot remove the last cycle.  Endpoint-bearing
  support is necessary.
- Whole residence-scale pair cells cannot partition the middle layer in the
  required regime: the proved two-adic divisor bound is `M<=s_2(r)`.  Cut,
  residue-carrying blocks are necessary for that architecture.
- The August-20 sparse-descent volume claim is false.  A cut-chain segment
  containing `s` targets has bottom depth at least `s`; summing gives descent
  demand at least `Lambda=Theta(W sqrt(n))`, not `W sqrt(n)/(4C)`.  Any saving
  must come from a proved sharing of departures across concurrent windows.
- A multi-swap collar with at most `t` coordinate exchanges per step joining
  endpoint owners at Johnson distance `Delta` needs at least `ceil(Delta/t)`
  steps.  Thus arbitrary endpoints do not admit an `O(sqrt(n))` collar when
  `t=Theta(sqrt(log n))`.
- In the PBBS ledger, the number of short run intervals is not the maximum
  projected-edge-disjoint packing number `nu_H(P_m)`.  Counting many short
  intervals therefore proves no corresponding packing bound.  The August-20
  queue-flush argument also used a false persistence invariant, so it
  establishes neither an `Omega(W/H)` packing nor failure of the conditional
  run criterion in Section 5.6.  A run-floored Middle-Levels factor likewise
  does not automatically supply complete band flags.
- The pure stationary tail-MTF rule has the Poisson plateau of Section 5.7.
  More generally, for every frozen unseen family, every doubly stochastic
  eligible kernel under a uniform input state has unseen mass exactly equal
  to its density; approximate
  conditional stationarity with vanishing average TV error over `Theta(M)`
  steps retains the plateau.  This rules out static
  stationarity-preserving feedback, not correlated adaptive rules.
- A just-served letter has deterministic dead time `n-sigma-1` before it can
  return to the eligible bottom pool.  Repair arguments that assume immediate,
  independently sampled access to prescribed letters are invalid.
- For a cyclic word `w` of length `L`, let
  `D={q:w_q!=w_(q+n)}`.  The number of distinct length-`k` windows, even as
  sequences, is at most `gcd(L,n)+k|D|`.  Thus an exact period-`n` word has at
  most `n` such windows, and central near-complete coverage forces
  `|D|>=(1-o(1))2W/n`; genuine order innovation is necessary.
- Fix coverage side information and a deterministic eligible rule that ignores
  the internal order of the bottom `sigma+1` letters.  Its permutation map has
  nonempty fibers of size `sigma+1`; from a uniform input its image has density
  `1/(sigma+1)`.  This blocks immediate uniform total-variation mixing for
  that deterministic class only.  Random mixtures and age-aware rules are not
  covered; the live target in Section 7 is simultaneous bulk union freshness.

## 9. Verification and reference map

On 2026-08-21 the following were replayed on the H100 host from the exact
bytes named here:

- every `answers/k01.word` through `answers/k16.word` matched the SHA-256 in
  `answers/README.md` and covered all `2^k-1` nonempty targets;
- `answers/k17_upper25746.word` matched SHA-256
  `f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b`
  and covered `131071/131071` nonempty targets;
- the two Section 5.7 gap-window witnesses matched their displayed hashes and
  passed `witnesses/verify_witness.py`;
- the Section 5.8 tail-MTF operator identities were checked through `n=7`,
  all-state reachability and exact directed diameters through `n=9`, and the
  common-endpoint gadgets through `n=8`; the largest observed diameter was
  30 at `(n,f)=(9,8)`, versus the proved bound 729;
- the endpoint-fiber and lifted-boundary counts were exhaustively checked in
  every tractable case through `n=5`, and the multi-rank snub algebra was
  checked on 1,157,354 binary fan matrices and 200,000 corrected-index random
  histories;
- the Section 5.9 return bound and no-return claim were exhaustively checked
  through `n=8`; its recurrence, collision, length, and balanced-quota algebra
  were also checked at the finite ranges used in its independent audit;
- the Section 5.10 transition identities and exact Hall deficiency passed the
  exhaustive finite checks recorded in the parity proof file; the short-chord
  and gadget claims passed the exact checks recorded in the rigidity file;
- the Section 5.11 hypergeometric Chernoff inequality was checked on 908,534
  parameter tuples with population at most 60, and its in-band trace claims
  passed exhaustive small tail-MTF checks;
- the Section 5.12 cyclomatic/Rado identities agreed with exhaustive
  augmented-edge enumeration on 1,800 finite path/quota systems, and every
  vertex subset of `J(3,2)` and `J(5,3)` passed the asserted forest
  inequalities;
- the postselected-quota identity was independently checked on 12,000
  finite Hall systems, the narrowed-tail orbit bound through `n=5001`, and
  the rooted coalescent identities on 12,000 finite ledgers;
- the static all-rank prefix multicover was constructed and checked at
  `n=3,5,7,9,11`, producing respectively `3,10,35,126,462` states with full
  rank support and bijective middle layers; its H100 script has SHA-256
  `b0e8b4102cdddd9bd4da923cd518635aa772c60f7ccca100e327e5a1364b55ea`;
- the two-block torus theorem was checked for all 912 coprime binary
  schedules with `b<=10`, the exact product factors for `b=3,5,7`, and the
  connector construction on all 209,408 audited endpoint instances with
  alphabet size at most ten;
- the clustered-product phase audit checked every admissible parameter and
  band rank for `b=5,7,11,13,17`, including every phase map in its monotonicity
  theorem and the exact adjacent-rank per-order-pair counts; its H100 audit
  script has SHA-256
  `21515f809faf2ac8d22a0a7f2421aba52420463f19ed92a19e2416730cb3f198`;
- the clustered profile-capacity formula was checked by direct phase
  enumeration for `b=11,13,17,23,31`; its pointwise localization and
  aggregate deficit were checked through `b=10003`, where
  `b^(1/4) deficit/W_b` was `0.104709...`; the H100 audit script has SHA-256
  `cc29909b8cdfcc125515f8747f04bf4971e67098504b936ae25f7139d111615c`;
- the Ferrers phase-origin transport was checked for
  `b=11,13,17,23,31,43`, simultaneously over every audited offset, profile,
  and diagonal; its H100 audit script has SHA-256
  `32e183aefa8a7c2e159c34dfe28b337c0ed5e749e055cb551a432706f7bce106`;
- the fractional-containment source/target loads, choose-in-two-orders
  identity, and exact profile values were replayed for
  `b=11,13,17,23,31,43`; its H100 script has SHA-256
  `2d7de75474fa3e5553548864ae017106b259b1fc13f27d04d6eca9df6ddb9dd4`;
- the full-orbit color-cap integer programs at
  `(b,q)=(5,1),(5,2),(7,1),(7,2)` attained their scalar bounds, and the
  restricted token--label determinant-`-2`, fractional-`3/2`, integer-`1`
  face replayed exactly; the two scripts have SHA-256
  `b274f2f8ea35d3650bee99f4afef4e3098b52d4c3c0f5318107018f30e7ab8e8`
  and
  `e15e702153ed123c6ea154f9449d9d712cc4d6e6bd7be4458956a5bf6ff65def`;
- the fixed-factor `b=5` physical bank replayed its middle and upper
  simplicity, determinant `-2`, exact `10/3` versus `2` optima, and direct
  factor exchange failure; the Walecki gap family passed through `b=13`.
  Its H100 script has SHA-256
  `09fa784002bf65a30afa0b5c06de54f4ed023e2c0d795beac0951711052f24cf`;
- the full-multiplicity source means and coupon bounds passed at
  `b=101,211,401,809,1601`, while the Dyck degrees and codegrees passed
  through `k=4`; its H100 script has SHA-256
  `20149c84d4256ae9ed803f28f902d2f9cc24e5d05a62cc022069496f76166cf5`;
- complementary-payload endpoint counts passed for
  `b=11,13,17,23,31,43`, and the odd-offset aggregate approached one half
  through `b=10003`; its H100 script has SHA-256
  `f66dd02bd769813e5d352871d247e60fa69a98ad1add40a777c6e4dc5bb49adb`;
- the constant-origin endpoint formula, localization window, and aggregate
  deficit were replayed through `b=503`; its H100 script has SHA-256
  `b3f1869731a88fdc3e47cff2bb90adf27cd20323fb98677299e176114e3a4ee0`;
- the literal common-order cardinality identity was checked for every offset
  at `3<=b<=61`, its pointwise bound through `b=30`, and its one-offset and
  small-offset asymptotics through `b=10007`; its H100 script has SHA-256
  `ace14cca1f58d9ae7e9743f19289c1251fac5d6c67010ffac4fd891517fa746a`;
- the nonidentical-order audit directly matched physical endpoint words to
  the exact CSP in five `b=5,7` cases, checked the zero-coordinate
  row/column counts and deterministic bound in three asymmetric `b=7`
  cases, exhausted interval-deck rigidity and adjacent swaps at `b=5,7`,
  checked the partial seams at `b=7,11`, and exhausted the two-sided sign
  rule at `b=5,7,11`; its H100 script has SHA-256
  `8d2ef3a9a3d149db3c8ae392357457d9142237c777d9d84ba520138afb803b14`;
- the constant-side audit checked every fractional load for `3\le b\le13`
  at the audited `H\le3`, every SCD support law through `b=9`, every central
  wider-side product cover through `b=9` at the audited `H\le3`, and the two
  extreme target families through `b=9`;
  its H100 script has SHA-256
  `be15334658e903dc125899b935dbb6535c1b16cbec57f7ae79b6a9990d3976f7`.
  Separate exact MILPs at `(b,H)=(3,2),(5,2),(7,2)` attained respectively
  `4,8,12` offset-one misses and zero offset-two misses; that script has
  SHA-256
  `fb6476615e9f14ae13cb7de399cb30e7398c836605a8c7f2e52941dd8c4b7434`;
- the affine nested-capacity audit exhausted the random-permutation
  expectation through `b=7`, the exact `q=1` row through `b=39`, every
  affine multiplier at primes through `31` for the audited offsets, and the
  dominant half-step phase bound for odd `b\le81`.  It also checked physical
  torus simplicity at the audited primes, the finite `T\ge P` diagnostic for
  odd `b\le81`, and profile numerics at `b=31,61,101,151,251`; its H100
  script has SHA-256
  `7911877ed2fc7c84e2729a3b89ca2fc4944823fe2758d698e7cfcc4b63f3239c`;
- the affine row-load/SCD audit checked the exact phase-multiplicity law at
  odd primes through `101` for `q\le15` and the audited central
  displacements, Walecki window moments at `b=5,7`, every forced SCD side
  word for odd `b\le15`, the row-regular Hamming bound through `b=1009`,
  and mesoscopic profile diagnostics through
  `b=2003`; its H100 script has SHA-256
  `bbfce61fc45c1a9b381575521dbac5a32495da96f042a6109c9984eef994c6d4`;
- the random nested-schedule audit exhausted every permutation and offset
  through `b=7` and `q\le3` at `b=8`, checked the central binomial-ratio
  expansion for `q\le12` through odd `b<80`, tested seeded phase histograms at
  `b=101,251,509,1009,2003,4001`, and replayed 5,000 finite coupon-product
  inequalities; its H100 script has SHA-256
  `1a07cdae5778c1948d4bc2b19118fa8eca3b3edc64a2dc33fd3df001be1c895c`;
- the affine full-chain/retirement audit checked the choose identities and
  central extension bounds at primes through `43`, exact raw target loads at
  primes through `31`, target-pair loads at `b=7,11,17`, and the full-chain
  obstruction at `b=101,251,503,1009`.  Its retirement LP at
  `b=11,17,31,41,61` matched the separate scalar optima for the same central
  payload truncation within the stated feasibility tolerance, and its
  phase-switch witness passed through odd `b=81`; its H100 script has SHA-256
  `853638b0bc8f2a4902575fab50f83197fb61cc5cc53d08f62871d67788f072ea`;
- the persistent-alternation retirement audit checked 37,680 exact Boolean
  identities, 45,512 literal phase-origin counts, 186 moment/tail cases,
  76,000 decay inequalities, and 1,801 exact LP and finite-bound instances.
  It verified every nesting and profile-capacity constraint by rational
  arithmetic; its H100 script has SHA-256
  `0d96e06cbbf715088e19ca59a6120219b55eaed0fa66ecf4b0eb2790f420a0f6`;
- the retired-chain local-load obstruction audit checked 234 exact cohort
  identities, 12 equipartition-gadget constant regimes, 653,596 asymptotic
  inequalities, and 354 central binomial-ratio bounds.  Its H100 script has
  SHA-256
  `30194c4b9effcb3afc9cb3b99136e0f285521a8ecca21ab367c1af269604141f`;
- the alternating GK audit constructed every chain and all `2^(2b)` Boolean
  vertices at `b=3,5,7`, checked the refined top formulas, parity tails,
  longest-top selection, token divisibility, and simultaneous source/target
  disjointness exactly, and replayed the finite clamp inequalities at
  `(b,H)=(257,8),(521,16),(1031,32)`; its H100 script has SHA-256
  `6d832d17a2b02177b73b69f55c5a4a5fe0a12b60d82031aaa63b7a6b60eb0087`;
- the direct-GK FIFO audit exhausted all ordered distinct queues through
  `b=6`, including 665,280 states at `b=6`, and found no cycle; it checked
  the first-minimum formula, strict-below-maximum successor, every defined
  `b`-step descent, and the `b^2` stopping bound.  Its H100 script has
  SHA-256
  `c63ec093855b4a1c69d33fd66e03c0ca3c3c0f16367ce6432b91627f2da86c98`;
- the residual-hitting selector audit exhaustively averaged every ideal map
  through `n=5`; simulated the greedy recurrence at
  `n=100,300,1000` and `K=2,5,10,25`; checked the collapsed map for
  `2\le n<30`; and constructed containment covering maps for
  `2\le b\le6` and `q\le2`.  The complete `b=5` physical-factor menus at
  `q=1,2` and `K\le8` were matching diagnostics only.  Its H100 script has
  SHA-256
  `6008679ab0cb505755d7431bb501e6ca90e9874a2e118667ff28767ba9619881`;
- the exact `q=1` product-SCD matching was enumerated through `b=11` and
  its loss formula through `b=1009`; the general-`q` rectangle formulas and
  cap ledgers passed through `b=503`, including the determinant-two shift
  minor.  Their H100 scripts have SHA-256
  `200957e89c28af8653d04f243e86b0ab694becda6e5a1d484ecabf7c8b3adb68`
  and
  `aada591fe04ebc3935f631beeb5af34d54430cf62d7a48bd58df1f2bff449e9f`;
- the equal-bottom prefix network agreed with direct LPs for every audited
  `q` through `b=13`; its H100 script has SHA-256
  `5fa7c4b4c6308e558e49997c7cedf6e49c306394a28dff9efd3aae46d575070f`;
- the canonical product-hook path partition and exact offset/color ledgers
  were exhaustively replayed for every odd `b<=19`; the asymptotic audit
  evaluated the interior overload and equal-bottom ratios at
  `b=101,251,503,1009,2003`.  Its H100 script has SHA-256
  `ee77a88e8e78425a41a12d2a7e6fffa99b96befeb858c05f1d126f78bb5d1238`;
- the common-origin diagonal lemma was exhaustively checked on all `59049`
  sequence pairs at `b=5`, and the phase/cell bijection at
  `b=5,7,11,13`; its H100 script has SHA-256
  `dbe681bc59a6ae34969d542ad074ca5b26da5d6659fadcc104e0a871b51e101b`;
- the all-offset token theorem's exact fractional quantities passed through
  `b=251` and its aggregate asymptotic proxies through `b=1000003`; its
  H100 script has SHA-256
  `ca6666e4360a80d081dc49de2a54dc5ec6cdf0cf186625c0ec1cbc96dd151781`;
- the growing-rank wreath script checked the exact pair-codegree profile,
  balanced-slice transversal, and weighted point balance for every audited
  odd `b<=9`; its H100 script has SHA-256
  `7b2e6ee186ad8ee8c931a182fdf5817221f1c90c0eee802f269badb15085e9a8`;
- the radius-two Johnson-shell equivalence and codegrees were brute-force
  checked at `b=5,6,7`, and the symbolic formulas and maximum-codegree claim
  through `b=199`; its H100 script has SHA-256
  `26165d08fdbc3a951fb16864d785ee036e646b83e69616e223a2477e346e91f7`;
- the central forced-suffix identity was checked on 29,164 finite legal
  words, history-graph regularity through `n=8`, and the free-history
  relabeling degree/codegree identities at `n=5,7`;
- the rainbow terminal-fan and fixed-owner counts were exhaustively checked
  through `m=5`; the Posa criterion itself is the one-line maximality proof
  in Section 5.13, not an empirical assertion;
- the unordered reservoir and sparse-recomposition bounds were checked on
  600 random Middle-Levels reservoir instances, 2,000 block-color incidence
  graphs, and 9,600 cyclic fragment recompositions; common-transformation
  fibers were exhaustively grouped in the finite cases recorded in their
  proof file;
- the one-central Hall ledger was checked on 6,000 finite defect systems,
  the sequential component identity on 5,500 systems, and the modular
  residual classes were verified equal and Johnson-independent for
  `n=5,7,9,11`;
- direct recomputation of `B(k)` gave the exact table through `k=16` and
  `B(17)=24313`.

These replays verify constructions and arithmetic.  The general statements
were separately checked against their cited proofs; the existence assertions
in Section 7 remain conjectures regardless of finite evidence.

The proof-safe exact structural synthesis is
`MATH_SYNTHESIS_AUG12_INTEGRAL_LATTICE_REBASE_20260812.md`.  The corrected
far-tail/DCC reductions are extracted from
`MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md`;
the prime transfer is in
Theorem P1 of
`MATH_THEOREM_PRIME_TRANSFER_AND_EQUIVARIANT_SUPPLY_20260820.md`; later
conditional material in that file is not imported here.

The stationary eligible-walk proof is the repaired content of Blocks 70--71
and 74.1--74.3 of
`MATH_CANDIDATE_COHORT_CONSTRUCTION_20260820.md`.  That candidate file is an
exploratory log, not an authority for its other claims.  Its mixing input is
Sharad Goel, *Analysis of top to bottom-k shuffles* (2006,
arXiv:math/0603209), and Johan Jonasson, *Biased random-to-top shuffling*
(2006, arXiv:math/0607124).  The two finite
gap-window words and their verifier live in `witnesses/` and are hash-bound in
Section 5.7.

The three independently hostile-audited Section 5.8 sources are
`MATH_CANDIDATE_TAIL_MTF_EXACT_BRIDGES_CYCLIC_CLOSURE_20260821.md`
(SHA-256 `8824d4347fc25e01ddb62a31abfa2b519316fe9923bef689c003067e84ddc7e9`),
`MATH_CANDIDATE_STATIONARY_FEEDBACK_ENDPOINT_OBSTRUCTION_20260821.md`
(SHA-256 `cce24fd5e8ffa2b9ac60e93727b5470913a1095959e759d11a654026ab4b57d9`),
and `MATH_CANDIDATE_MULTIRANK_LATE_ACCESS_BARRIER_20260821.md`
(SHA-256 `0edbcec66bedab8c171af24187b1d74338dfc40b3e6e8024146fd41726005496`).
Their computations were sanity checks on H100; the stated results follow from
the explicit proofs.

The independently hostile-audited Section 5.9 fractional theorem is
`MATH_CANDIDATE_FIXED_ENDPOINT_PALETTE_FRACTIONAL_MATCHING_20260821.md`
(SHA-256 `c3f762f4e4b0bbb432afdfc3140d9220c4a3523a1d9ba249bf042dc31b8c21fd`).
The theorem-by-theorem rounding audit is
`MATH_AUDIT_FIXED_ENDPOINT_PALETTE_MATCHING_BLACKBOX_20260821.md`
(SHA-256 `471fee3b739d1f72e226260bbe4b11d047666540dd2c4135ac26f69faaa8311a`).
The former proves exact fractional balance; the latter proves only that the
named published black boxes do not supply the required integral near-factor.

The independently hostile-audited parity reduction and rigidity sources are
`MATH_CANDIDATE_PARITY_PROJECTION_HALL_REDUCTION_20260821.md`
(SHA-256 `8d71c3f5c7de59db57e00a2a99ff1c434fbfbc3d88d1daa485e9d9a3da6b4d61`)
and `MATH_CANDIDATE_PARITY_FIBER_RIGIDITY_20260821.md`
(SHA-256 `d1c85262b2e657e64756c8857793591802411f9de34986e588daf15ec988e308`).
The first gives the exact same-path colored-Hall reduction; the second proves
the scoped ordered-trace and chordless-deck rigidity statements.

The independently hostile-audited residual barrier is
`MATH_CUSTOM_PALETTE_ROUNDING_RESIDUAL_AND_FIBER_BARRIERS_20260821.md`
(SHA-256 `bb07517e24b10382de33d6022a758b40bc12964e9c6edca8201c54c601a5fbb9`).
It is a barrier to scalar-residual greedy arguments, not an impossibility
theorem for global palette rounding.

The independently hostile-audited Section 5.12 sources are
`MATH_CANDIDATE_CYCLOMATIC_HALL_GRAPHIC_ROUNDING_20260821.md`
(SHA-256 `0ec44c9d9d28fc92c5dfe63fad2dcedb75359d41cf9ea042a1f246e0bc940691`),
`MATH_THEOREM_GLOBAL_PARITY_CYCLE_RESERVOIR_AND_FIFO_RECOMPOSITION_BARRIER_20260821.md`
(SHA-256 `dc3a27f4c9aaf36928bfdef8e842ad13bf353f4155390f1296c29614421b4862`),
`MATH_THEOREM_COMMON_ENDPOINT_LINEAR_DECK_CODE_20260821.md`
(SHA-256 `0a83281560aa2481bff34e47f146df2d01d0b5e9d27ad85be2d0b860973f6159`),
`MATH_REDUCTION_ONE_CENTRAL_MATCHING_PLUS_GRAPHIC_COLORS_20260821.md`
(SHA-256 `0d80452215fc1776c5b28ca10d4114700fa4e51a5b5bcfe458722354db688170`),
`MATH_CUSTOM_PARITY_GRAPHIC_NIBBLE_INVARIANT_20260821.md`
(SHA-256 `6536f67838e84c6bf4976ca5c6e137c1e06dd3a77a0b38dd47b2b3e3e2cf3829`), and
`MATH_ATTACK_ONE_CENTRAL_RECTANGULAR_GREEDY_QUENCHED_GATE_20260821.md`
(SHA-256 `75f1a54ffb1224c142b062b0d2b1f0a816134757051fe2fc224cab6fa05f68e9`).
They respectively prove the graphic reformulation, the dense checkpoint and
FIFO/reservoir theorems, genuine fixed-endpoint deck mobility, the
one-central reduction, the sequential component-charge criterion, and the
annealed-versus-quenched residual calibration.  None proves the final
common-path selection asserted only as open in Section 7.3.  These are now
strictly stronger proof strategies than the adaptive union-cover criterion;
they remain valid but no longer define the exact gate.

The independently hostile-audited adaptive union theorem is
`MATH_THEOREM_POSTPONED_GRAPHIC_COALESCENT_AND_DECOUPLING_GATE_20260821.md`
(SHA-256 `80f786f83a818f4d9abbae289196fa73309878a9a4b4196d3eaa63b2151065d4`).
It proves the exact postselected-quota formula, the all-rank union-cover DCC
criterion, the first-order repeat ledger, the narrowed-tail all-band
annealed pair bound, and the scoped coalescent/coupon statements.  It does
not construct the common paths.

The independently hostile-audited static prefix-multicover theorem is
`MATH_THEOREM_STATIC_ALL_BAND_PREFIX_MULTICOVER_20260821.md`
(SHA-256 `f343a4bceb3f1b9cebca9a48fa71f61851790088d161e8939f29c5db3726eaf1`;
H100 script SHA-256
`b0e8b4102cdddd9bd4da923cd518635aa772c60f7ccca100e327e5a1364b55ea`).
It constructs exactly `W` permutation states whose prefixes cover every
rank support simultaneously and are bijective at both middle ranks.  This
removes a static set-system obstruction only; no short FIFO/tail-MTF
chronology or sublinear-transition atomization is supplied.

The independently hostile-audited linear seam and product-atom theorem is
`MATH_THEOREM_TWO_BLOCK_FIFO_PRODUCT_ATOMS_AND_LINEAR_SEAMS_20260821.md`
(SHA-256 `b12a0d33997d273179e2ea70f11c9e01d92976a9c054c55d34b414c991443232`).
Its tight-cycle aggregation is explicitly conditional and middle-layer
only; coherent multirank aggregation remains open.  The scoped endpoint
criterion and fixed-fibre no-go are in
`MATH_LEMMA_RAINBOW_POSA_ENDPOINT_GATE_AND_FIXED_FIBER_NOGO_20260821.md`
(SHA-256 `da383e9db8d95852a5b0a30efd6e50e2487b994632975d4ffb5633904a5b213d`).

The forced-suffix, free-history central palette, first-bite, and exact
central near-factor lift are in
`MATH_CENTRAL_SLOT_HYPERGRAPH_VARIABLE_R_NIBBLE_AND_SEED_GATE_20260821.md`
(SHA-256 `cd4503b1d5acac5ada972bf4f47bff9b461694352dc58163bce116b90117dd2b`).
These results solve central seed compatibility, not the all-rank union
target.

The independently hostile-audited parameter-only nibble obstruction is
`MATH_COUNTEREXAMPLE_GROWING_RANK_LOCAL_KERNEL_NIBBLE_20260821.md`
(SHA-256 `09993652da46dfcfcef979cb8f8450e0501cff0552ff8dad4eca1dc55b551b76`).
It constructs regular slot--target multihypergraphs at the exact central
`r Delta_2/Delta` and `Xi` scales whose maximum matchings cover only
`O(1/n)` of the vertices.  Its conclusion is limited to local-parameter
theorems and does not refute a Johnson-specific global matching argument.

The independently hostile-audited high-order necessity theorem is
`MATH_THEOREM_ADAPTIVE_UNION_HEAVY_TAIL_ALIGNMENT_NECESSITY_20260821.md`
(SHA-256 `4e17d21c1078b4910978b501e2026b2fe80af0bda71769df344f8131221b3c63`).
It proves the inner-band old-hit ledger, the unavoidable heavy
simultaneous-freshness tail, and positive upper-orthant correlation at order
`Theta(a log n)`.  These are necessary conditions on a successful selector,
not an existence theorem or a global impossibility theorem for adaptive
union coverage.

The independently hostile-audited clustered phase-alignment theorem is
`MATH_THEOREM_CLUSTERED_PRODUCT_PHASE_ALIGNMENT_20260821.md`
(SHA-256 `38d51551fee0eb03792543d5c5f4d4f7403c8ec7b5ad19a25afd5036a26b5e7f`).
It proves clustered legality and band simplicity, the exact monotone phase
maps, the rigid-bank aggregate hole ledger, the unconditional adjacent-rank
MSW alignment, and the independent-relabeling miss calculation.  It does not
provide a nonrigid multirank order-bank alignment.  The later exact CSP
proves that the unmodified one-copy clustered version is impossible at
mesoscopic offsets; alignment after changing the schedule or atom geometry
remains open.

The independently hostile-audited pooled split-profile capacity theorem is
`MATH_THEOREM_CLUSTERED_PROFILE_CAPACITY_DEFICIT_20260821.md`
(SHA-256 `7d7054f544c1a8161092d014639c5866f0bb5f44f2bf6af996a9b76eb899e386`).
Conditional on the requisite complementary-rank tight-cycle factors, it
proves that the aggregate positive split-profile capacity deficit is
`O(W_b b^(-1/4))=o(W_b)`.  It is a numerical/transport-capacity theorem, not
an integral labelled order-bank assignment.

The independently hostile-audited integral phase-origin theorem is
`MATH_THEOREM_CLUSTERED_PHASE_ORIGIN_FERRERS_TRANSPORT_20260821.md`
(SHA-256 `3d79759b87592061e3061e15bb35b23ffa7ae315259e28de1dea89523aa569bc`).
It places arbitrary rankwise factor orders into nested Ferrers columns and
assigns one physical relative origin per column so that every central
profile/diagonal capacity differs from its fractional value by less than
`b^2`, simultaneously at all offsets.  Its total equal-bin deficit remains
`O(W_b b^(-1/4))`; it supplies no cross-rank compatibility of the labelled
cyclic orders inside a column.

The independently hostile-audited fractional containment theorem is
`MATH_THEOREM_CLUSTERED_FRACTIONAL_CONTAINMENT_TRANSPORT_20260821.md`
(SHA-256 `a40a867e8624e66b6b94a31a250fa542f27f5418c5792ff4e1cbe46d1a640d61`;
H100 script SHA-256
`2d7de75474fa3e5553548864ae017106b259b1fc13f27d04d6eca9df6ddb9dd4`).
It gives the exact symmetric labelled flow of value
`sum_s min(P_(q,s),T_(q,s))`, separate integral containment matchings, and
one unthinned nested fractional chain law.  It does not coinstantiate the
rankwise thinnings, factor cycles, or orders.

The independently hostile-audited full-orbit reduction is
`MATH_THEOREM_CLUSTERED_FULL_ORBIT_LINKS_AND_COLOR_CAP_REDUCTION_20260821.md`
(SHA-256 `03b5b64c64b4d5433beae8720aa28e595d985e06a5cc2627baa91db775aff429`;
H100 script SHA-256
`b274f2f8ea35d3650bee99f4afef4e3098b52d4c3c0f5318107018f30e7ab8e8`).
It proves optimal matching in each biregular one-color link and the exact
collapse of occurrence-token rows to color capacities.  The companion
restricted-incidence warning is
`MATH_BARRIER_CLUSTERED_TOKEN_LABEL_COINSTANTIATION_NONTU_20260821.md`
(SHA-256 `534e4f06c3211be21ef603c2de9cef5e877d57a3f5b247c7f3f1de2222152c39`;
H100 script SHA-256
`e15e702153ed123c6ea154f9449d9d712cc4d6e6bd7be4458956a5bf6ff65def`).
Its determinant-two restricted face rules out automatic TU only; it is not a
gap theorem for the full dense orbit.

The independently hostile-audited fixed-factor formulation barrier is
`MATH_BARRIER_FIXED_FACTOR_PHASE_LABEL_MATRIX_NONTU_20260821.md`
(SHA-256 `bd7fba2c5760e1af4909c029e2b6071c1aca44fdbda09bba5a3c956042fcb70a`;
H100 script SHA-256
`09fa784002bf65a30afa0b5c06de54f4ed023e2c0d795beac0951711052f24cf`).
It proves a determinant-two minor and exact `10/3` versus `2` gap at `b=5`,
the Walecki family with ratio `b/(b-2)` for every odd `b`, and failure of the
direct factor-deck matroid axiom.  Its large-`b` witness is extreme-rank and
has vanishing relative gap, so it is not a coefficient-one no-go.

The independently hostile-audited full-multiplicity and Dyck barriers are in
`MATH_THEOREM_FULL_MULTIPLICITY_INDEPENDENT_RELABELING_AND_DYCK_NIBBLE_BARRIERS_20260821.md`
(SHA-256 `30d0cbb2221197b93deb22eef722e3a9d328a447cae6161cdf69486518377fcb`;
H100 script SHA-256
`20149c84d4256ae9ed803f28f902d2f9cc24e5d05a62cc022069496f76166cf5`).
It proves the at-least-quarter independent-relabeling miss at every
`q<=Q=o(sqrt b)`, the necessary endpoint anti-alignment for successful
product-uniform marginals, and the raw/negligibly target-projected Dyck
codegree obstruction.  Correlated banks and structure-aware matching remain
open.

The independently hostile-audited coherent physical endpoint theorem is
`MATH_THEOREM_CLUSTERED_COMPLEMENTARY_PAYLOAD_ENDPOINT_COVERAGE_20260821.md`
(SHA-256 `a2b0152cebc4fdefc2ce2d148eecea6018620d151901576af495c96857741d30`;
H100 script SHA-256
`f66dd02bd769813e5d352871d247e60fa69a98ad1add40a777c6e4dc5bb49adb`).
Conditional on the local tight-cycle factors, it uses common complementary
orders and band-constant origins to cover `(1/2-o(1))W_b` actual targets over
the odd balanced profiles, with hole charge
`O(W_b/sqrt b+HW_b/b)=o(W_b)`.  Other profiles and even offsets remain
physically open; the later scalar theorem covers their capacity only.

The independently hostile-audited constant-origin scalar theorem is
`MATH_THEOREM_CONSTANT_ORIGIN_ENDPOINT_PROFILE_CAPACITY_20260821.md`
(SHA-256 `2d97228b0d83472aa296fe3ca42e8ad3ca694c90acac8f513900868b9d6cf3e2`;
H100 script SHA-256
`b3f1869731a88fdc3e47cff2bb90adf27cd20323fb98677299e176114e3a4ee0`).
After discarding every origin whose next `H` types cross a run boundary, it
proves pooled endpoint deficit
`O(W_b b^(-1/4)log^(7/4)b)=o(W_b)` using only common all-`A` and all-`B`
chains.  Its lifted endpoint-only token hypergraphs also have separate
integral matchings with aggregate `o(W_b)` deficit.  Cross-offset nesting,
labelled order-bank realization, and factor compatibility remain open.

The independently hostile-audited literal-overlap barrier is
`MATH_BARRIER_LITERAL_COMMON_ORDER_OVERLAP_B14_20260821.md`
(SHA-256 `b8d73b23879259bace7608254f2995f8c4eaddeea79565d76f22bd86d7c92d4b`;
H100 script SHA-256
`ace14cca1f58d9ae7e9743f19289c1251fac5d6c67010ffac4fd891517fa746a`).
It proves the exact forced cardinality lower bound for literal intersections,
its positive one-offset Gaussian limit at `q=Theta(sqrt b)`, and the
aggregate `b^(1/4)` threshold.  These are lower bounds only for identical
cyclic-order overlap.  The next theorem closes nonidentical transport inside
the same one-copy clustered factor bank, but not after changing its schedule
or atom geometry.

The independently hostile-audited exact nonidentical-order CSP and
one-copy-bank barrier is
`MATH_THEOREM_NONIDENTICAL_ENDPOINT_ORDER_CSP_AND_PAIRING_BARRIER_20260821.md`
(SHA-256 `4924fd2e9c582885a1ad6685fa86e79c999d9ba8838fc79e013fcacf2920973f`;
H100 script SHA-256
`8d2ef3a9a3d149db3c8ae392357457d9142237c777d9d84ba520138afb803b14`).
Conditional on the local tight-cycle factors, it gives the exact
cyclic-interval CSP (5.13.C19k), the independent-origin
Jensen bound, the deterministic zero-coordinate bound (5.13.C19n), and the
positive constant `Gamma_c` in the mesoscopic lower bound.  Even after all
interior phases are restored, the complete one-copy clustered
`A^rB^(b-r)` factor bank misses `(Gamma_c-o(1))W_b` targets at
`q~c sqrt b`, for every choice of factors, conjugations, and origins.
Full interval isomorphisms are dihedral and adjacent swaps give the exact
local seam bound (5.13.C19u).  The result rules out `o(W_b)` repair of this
one physical bank only; altered schedules, factor/atom geometries, and
linear-scale rerouting remain open.

The independently hostile-audited constant-side chain theorem is
`MATH_THEOREM_CONSTANT_SIDE_CHAIN_FRACTIONAL_AND_SCD_SUPPORT_20260821.md`
(SHA-256 `f996eafe69309583cf15ca04b4b048846aa1ed12170c4a132e96c0860dea3dd1`;
H100 audit-script SHA-256
`be15334658e903dc125899b935dbb6535c1b16cbec57f7ae79b6a9990d3976f7`;
finite-MILP SHA-256
`fb6476615e9f14ae13cb7de399cb30e7398c836605a8c7f2e52941dd8c4b7434`).
It proves the exact simultaneous fractional laws (5.13.CS2)--(5.13.CS5),
the one-fiber nested SCD support theorem, and the wider-side product-SCD
assignment covering every central target at every offset.  The extreme
tail is exponentially small but not empty.  The integral cover is an
unrestricted Boolean-chain result: it supplies no physical origin caps,
factor orders, internally simple atoms, or serialization.

The independently hostile-audited affine nested scalar theorem is
`MATH_THEOREM_AFFINE_NESTED_BALANCED_SCHEDULE_PROFILE_CAPACITY_20260821.md`
(SHA-256 `6b2f22fdc9e18bbcf746cb18c35658e8b50857973c25fd346501659536032b82`;
H100 script SHA-256
`7911877ed2fc7c84e2729a3b89ca2fc4944823fe2758d698e7cfcc4b63f3239c`).
It proves the exact affine hole bound, dominant phase counts, full-band
scalar deficit `O(W_b b^{-1/4}\log^{3/4}b)=o(W_b)`, and physical
legality/internal simplicity of each central atom.  It is conditional on
the required local factor counts when interpreted physically and proves no
labelled order-bank assignment.

The independently hostile-audited affine row-load and product-SCD compiler
barrier is
`MATH_OBSTRUCTION_AFFINE_BALANCED_FACTOR_ROW_LOAD_AND_SCD_DIAGONAL_20260821.md`
(SHA-256 `821362005b652549de6866e35b78b5508fca0b282d59312238533ea6d18add03`;
H100 script SHA-256
`bbfce61fc45c1a9b381575521dbac5a32495da96f042a6109c9984eef994c6d4`).
It gives the exact row/column means and variances, proves a positive
mesoscopic labelled miss for the affine one/two dominant independently
conjugated banks, and shows that any complete cover on the fixed product-SCD
trajectories is `(1/4-o(1))W_b` from a physical row-regular torus marking.
The last quantity is Hamming compilation distance, not target deficit;
correlated banks and different trajectories remain open.

The independently hostile-audited random nested coupon barrier is
`MATH_OBSTRUCTION_RANDOM_NESTED_SCHEDULE_MEAN_ONE_COUPON_20260821.md`
(SHA-256 `7b704d219ae8d863a3c401fab4099233d652355aa064a2a7e0f70ea4efa8c3e6`;
H100 script SHA-256
`1a07cdae5778c1948d4bc2b19118fa8eca3b3edc64a2dc33fd3df001be1c895c`).
It proves that random nested phase spreading makes each central coupon
`o(1)` but leaves total mean at most one and hence at least an
`(e^{-1}-o(1))` expected miss fraction under independent rank-and-side
conjugations.  It does not obstruct correlated multirank factors or an
explicit anti-aligned occurrence-to-target matching.

The independently hostile-audited shared-offset retirement theorem is
`MATH_THEOREM_AFFINE_FULL_CHAIN_LOADS_RETIREMENT_LP_AND_MATCHING_OBSTRUCTION_20260821.md`
(SHA-256 `df6b7a56a30636d6d1b7de582a21cc84937606bde43f1616772821efcc60f82f`;
H100 script SHA-256
`853638b0bc8f2a4902575fab50f83197fb61cc5cc53d08f62871d67788f072ea`).
It identifies the affine capacity as the exact target marginal of one raw
whole-chain orbit law and computes all pair loads.  Ordinary full-chain
matching has `\Omega(\sqrt b\,W_b)` aggregate deficit.  The exact
phase-preserving retirement LP and dual replace that false object, and every
feasible point has a labelled fractional lift with maximum pair load
`O(1/b)`.  Its formerly open scalar optimum is closed by the next theorem,
and abstract integral growing-rank rounding is closed by the later
alternating-GK theorem.  Physical factor-order/product-atom coinstantiation
remains open.

The independently hostile-audited persistent-alternation retirement theorem
is
`MATH_THEOREM_HALFSTEP_PERSISTENT_ALTERNATING_RETIREMENT_20260821.md`
(SHA-256 `c7a253de6765ee096b0a5c76bd1946f272209e5c14c457f1c139957059a47069`;
H100 script SHA-256
`0d96e06cbbf715088e19ca59a6120219b55eaed0fa66ecf4b0eb2790f420a0f6`).
It gives an exact two-orientation Boolean flow, embeds persistent alternating
origins in the physical half-step word, clamps them to literal phase
capacities, and proves the finite estimate (5.13.PAR9).  Hence
`\mathfrak D_{\mathrm{ret}}=o(W_b)` for
`H=O(\sqrt{b\log b})`.  Its exact labelled retired-chain lift has
real-target incidence `\sum_{q\le H}M_q-o(W_b)` and maximum pair load
`O(1/b)`.  This is a fractional theorem on genuine affine paths, not an
integral matching or a common factor/order-bank coinstantiation theorem.

The independently hostile-audited local-parameter rounding obstruction is
`MATH_OBSTRUCTION_RETIRED_CHAIN_LOCAL_LOADS_AND_PAIR_CODEGREES_20260821.md`
(SHA-256 `4c33c7b4958230c26d68f34b330d3d46fb1d9e2c7de2395a3571857d6925f186`;
H100 script SHA-256
`30194c4b9effcb3afc9cb3b99136e0f285521a8ecca21ab367c1af269604141f`).
It constructs an abstract graded retired-chain hypergraph with the exact
layer sizes `M_q`, an exactly target-saturating fractional matching, maximum
vertex load one, and pair load at most `2/b`, while every integral matching
loses `\Omega(\sqrt b\,W_b)` target incidences.  It rules out a rounding
theorem based only on those local parameters and the partite chain format.
It is not a counterexample to the affine Boolean-chain hypergraph, whose
global orbit and containment structure are absent from the construction.

The independently hostile-audited alternating-GK integral theorem is
`MATH_THEOREM_BOOLEAN_ALTERNATING_GK_INTEGRAL_RETIREMENT_20260821.md`
(SHA-256 `ec05b81a0748f0a25e61b2ab2c71a58f8097791d7fec9094504fff26eee25103`;
H100 script SHA-256
`6d832d17a2b02177b73b69f55c5a4a5fe0a12b60d82031aaa63b7a6b60eb0087`).
It proves that interleaved Greene--Kleitman chains alternate exactly,
derives the split-refined top and parity-tail identities
(5.13.GK3)--(5.13.GK5), and selects the longest chains within each literal
persistent-phase token capacity.  The result is an integral
occurrence-token/source/labelled-target retired-chain matching of incidence
`\sum_{q\le H}M_q-o(W_b)` for `H=O(\sqrt{b\log b})`.  It closes abstract
growing-rank rounding by using global Boolean structure.  It does not pack
the selected chains into full product-atom translation orbits or common
cyclic tight-factor orders.

The independently hostile-audited direct-successor obstruction is
`MATH_OBSTRUCTION_ALTERNATING_GK_DIRECT_FIFO_SUCCESSOR_20260821.md`
(SHA-256 `de4dcd0be7632abdfad58ac72cfd1ebba54a63e2007e3c1a06f0934fb4e1dd6c`;
H100 script SHA-256
`c63ec093855b4a1c69d33fd66e03c0ca3c3c0f16367ce6432b91627f2da86c98`).
For one fixed alternating linear order, the first GK successor is always
below the current source maximum.  Consequently the FIFO maximum drops
strictly every `b` updates, every run stops within `b^2` updates, and no
cycle exists.  This blocks only canonical first-successor serialization;
product translations, atom-dependent conjugations, and different successor
maps are outside its scope.

The independently hostile-audited residual-hitting selector theorem is
`MATH_THEOREM_POLYLOG_FACTOR_MENU_RESIDUAL_HITTING_SELECTOR_GATE_20260821.md`
(SHA-256 `6fdf33134e0f68e8db74d341f989e7a87e95cbc22f84d2b3e481ccd42ffd52fa`;
H100 script SHA-256
`6008679ab0cb505755d7431bb501e6ca90e9874a2e118667ff28767ba9619881`).
It proves the exact greedy recurrence (5.13.SEL3), the
`O((\eta K)^{-1})` fixed-layer selector deficit, and the pair-moment
sufficient condition `\eta=(1+CB)^{-1}`.  It also constructs a
containment-respecting conjugated covering map with exact uniform-neighbor
marginals and correct target mean but image fraction
`O((\log W)/\binom bq)`, so polylogarithmic menus can still have
`o(M_q)` matching size.  The nontransitive support audit
(5.13.SEL12) is necessary only.  Residual hitting is not proved for the
physical factor banks, and a successful sourcewise selector still needs
atomwise coinstantiation; no `K`-free physical serialization or
coefficient-one conclusion is asserted.

The independently hostile-audited product-SCD theorems are
`MATH_THEOREM_Q1_PRODUCT_SCD_COLOR_CAP_MATCHING_20260821.md`
(SHA-256 `86b7cf295ea0b5419d9418f94965abe950c492a20db7637bab0aeab23e0a47ad`;
H100 script SHA-256
`200957e89c28af8653d04f243e86b0ab694becda6e5a1d484ecabf7c8b3adb68`)
and
`MATH_THEOREM_PRODUCT_SCD_GENERAL_Q_FAR_RECTANGLE_MATCHING_AND_SHIFT_GATE_20260821.md`
(SHA-256 `1908c6ba60812b6a20dca94ca14930c435e74ea7f4077541578f10a127df8047`;
H100 script SHA-256
`aada591fe04ebc3935f631beeb5af34d54430cf62d7a48bd58df1f2bff449e9f`).
They give explicit labelled tokenwise matchings with exact q=1 loss and the
general per-offset error in (5.13.C38).  The general aggregate estimate is
sublinear only for `Q=o(sqrt b)`, and neither theorem realizes common orders.

The independently hostile-audited equal-bottom augmentation theorem is
`MATH_THEOREM_EQUAL_BOTTOM_SHIFT_AUGMENTATION_IS_NETWORK_FLOW_20260821.md`
(SHA-256 `ed5162e1cb13861538744dd14b9920d01d6165f0ce09717c0e2614c1f7dc701e`;
H100 script SHA-256
`5fa7c4b4c6308e558e49997c7cedf6e49c306394a28dff9efd3aae46d575070f`).
It is an exact integral min-cost-flow representation for arbitrary integral
fixed-`q` residual color capacities.  It proves no residual cut bound,
cross-offset coupling, or physical-order lift.

The independently hostile-audited all-offset token rounding theorem is
`MATH_THEOREM_ALL_OFFSET_TOKEN_ORBIT_SMALL_CODEGREE_ROUNDING_20260821.md`
(SHA-256 `59fdbe51cae5e5f6c1e8b4f96525ff84e4813cf9c47e4638d6d8c28a9c8dd0da`;
H100 script SHA-256
`ca6666e4360a80d081dc49de2a54dc5ec6cdf0cf186625c0ec1cbc96dd151781`).
It applies quantitative Molloy--Reed edge coloring to the lifted fractional
flow and proves aggregate `o(W_b)` target deficit across every separate
canonical offset.  Nested-chain and common-factor/order realization are not
part of the theorem.

The independently hostile-audited canonical-hook barrier is
`MATH_BARRIER_PRODUCT_HOOK_SCD_INTERIOR_PHASE_OVERLOAD_20260821.md`
(SHA-256 `fcd97f636c82683e251c7468215a01837e05987c6311ce04593546b0f51cf0b7`;
H100 script SHA-256
`ee77a88e8e78425a41a12d2a7e6fffa99b96befeb858c05f1d126f78bb5d1238`).
It proves `Omega(W_b)` interior-color overload at every
`q in [sqrt b,2sqrt b]`, an `Omega(sqrt b W_b)` summed unchanged-hook
deficit on that window, and the exact `(3/4+o(1))W_b` equal-bottom discard
ledger.  This blocks only the canonical hook and `o(W_b)` modifications of
its affected offsets, not noncanonical or absorbed product constructions.

The independently hostile-audited common-origin obstruction is
`MATH_OBSTRUCTION_Q1_PRODUCT_SCD_COMMON_ORIGIN_DIAGONAL_20260821.md`
(SHA-256 `86bb6629e65c73791780fef4aa193efb2bc917d6dc030fb923877d69f3a0b166`;
H100 script SHA-256
`dbe681bc59a6ae34969d542ad074ca5b26da5d6659fadcc104e0a871b51e101b`).
It proves the exact diagonal side mismatch and the
`(1-o(1))W_b/(3b)` repair lower bound for compiling the q=1 product-SCD
matching.  This is an `o(W_b)` zero-switch obstruction, not a coefficient-one
barrier.

The independently hostile-audited growing-rank wreath residual obstruction
is
`MATH_OBSTRUCTION_GROWING_RANK_WREATH_BALANCED_SLICE_RESIDUAL_20260821.md`
(scope-fixed SHA-256
`17378330ee7a8562e56b2b70e3b851af035400f2e1869b46de66aae00bb433b8`;
H100 script SHA-256
`7b2e6ee186ad8ee8c931a182fdf5817221f1c90c0eee802f269badb15085e9a8`).
It proves the exact wreath pair-codegrees and a density
`1-O(b^(-1/2))` wreath-free residual which is almost unweighted and exactly
fractionally point-regular.  It refutes only density/one-point-regularity as
an iteration invariant; the approximate growing-rank factor remains open.

The independently hostile-audited Johnson-shell reduction is
`MATH_REDUCTION_RADIUS2_JOHNSON_SHELL_PACKING_GATE_20260821.md`
(SHA-256 `7f6bcbf740e3001039010cc9ce1ee6549dab141f88dcbeb8d51976f32522812e`;
H100 script SHA-256
`26165d08fdbc3a951fb16864d785ee036e646b83e69616e223a2477e346e91f7`).
It proves that disjoint rank-two Walecki slices are exactly a
distance-ten constant-weight code and that near-full middle coverage is
equivalent to an asymptotically perfect radius-two code in `J(2b,b)`.  The
shell hypergraph has a perfect fractional matching and the exact codegrees
in (5.13.C68), but no applicable growing-rank rounding theorem.  The code
assertion and every all-band lift remain open.

The indexed theorem/audit files cited above contain the full proofs and
artifact hashes; `RESEARCH_INDEX.md` is the lookup table.  The chronological
`MATHEMATICAL_HANDOFF.md` is provenance only and loses to this file or any
later independently audited certificate when they conflict.
