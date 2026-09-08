# Adversarial audit: reciprocal-height PBBS approximation and atomic lopsided compiler

Date: 2026-07-30  
Lane: R, pure mathematics  
Method: hand proof audit only; no web access, finite search, SAT, or remote job.

Audited notes:

* `MATH_THEOREM_R_ALLK_PBBS_RECIPROCAL_HEIGHT_SQRTLOG_APPROXIMATION_20260730.md`;
* `MATH_THEOREM_R_ALLK_ATOMIC_LOPSIDED_COMPILER_AND_PBBS_NATIVE_MULTIPLICITY_OBSTRUCTION_20260730.md`;
* the directly imported PBBS height, seam, terminal-mountain, and
  run-boundary theorems.

## 0. Verdict

The following claims are valid with the scopes stated in the theorem notes.

1. Unconditionally,

   \[
   \boxed{
   \nu(k)=O\!\left(\sqrt{\log(k+2)}
          {k\choose\lfloor k/2\rfloor}\right),}     \tag{0.1}
   \]

   so the approximation factor relative to `B(k)` is
   `O(sqrt(log k))=o(sqrt(k))`.
2. Assignment-incompatible atomic events form the exact useful lopsided
   dependency graph.  The candidate-specific product inequalities in the
   theorem are a valid all-arity integral compiler criterion.
3. The native within-piece PBBS atlas does not satisfy the common
   multiplicity hypothesis.  Under `b` residence-safe cuts,

   \[
   L_{\le3}\ge\max\{0,W-(k-1)b\}.                  \tag{0.2}
   \]

4. Higher conflicts do not reduce to pairs in the full pruned atlas.  If
   `r-2d-1>=1`, `2<=j<=d+1`, and
   `Q=2^(r-2d-2)-1>=j-1`, exact minimal banks give

   \[
   D_j(V_{\{x\}})\ge |V_{\{x\}}|(Q)_{j-1};         \tag{0.3}
   \]

   hence `D_4>M^2/16` eventually whenever `M>0`.
5. Neither obstruction disproves a pruned, correlated, or weighted
   compiler.  The all-arity lopsided pressure normalizes size-`j` banks by
   their product probabilities.  The precise unresolved PBBS condition is
   simultaneous survival of tight ports and exterior deep sockets under
   one residence-safe, upper-complete rethreading, followed by the
   candidate-opposing pressure bounds.

No `B(k)+O(k)` construction is proved.  It follows only from the explicit
conditional interface in Theorem 7.1 of the compiler note.

## 1. Audit of the growing-height approximation

For `n=2m+1`, `W=binom(n,m)`, and `B_m=W/n`, the imported quotient ledger
is

\[
 {L_H-W\over W}\le {2H\over n}
 +4(5H-1){\overline\nu_H\over B_m}
 +2(5H-1){Z_H\over B_m}.                            \tag{1.1}
\]

The two estimates used in it are uniform in `H`:

\[
 \overline\nu_H\le
 \sum_{h\le H-1}{b_{m,h}\over h+2}
 \le C{B_m\over\sqrt m},                           \tag{1.2}
\]

\[
                         Z_H\le(2H+2)n^{2H+2}.       \tag{1.3}
\]

The first is the full reciprocal-height sum, not the later fixed-`A`
notation; the second is the all-`H` voltage-itinerary count in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, (17.2).  Therefore the
choice

\[
                         H=\lceil\sqrt{2m\log(m+2)}\rceil             \tag{1.4}
\]

is legal.  It satisfies `2H<=m+1` eventually and
`H log n=o(m)`.  Hence the second term in (1.1) is `O(sqrt(log m))`, while
the first is smaller and `HZ_H/B_m=o(1)` by the Catalan lower bound.

The literal PBBS construction covers exactly the central ranks
`m+1-H,...,m+1+H`.  Every outside rank `s` has
`|s-n/2|>=H`; Hoeffding gives

\[
 {R_H\over2^n}\le2e^{-2H^2/n}=O(m^{-4/3}),
 \qquad {R_H\over W}=O(m^{-5/6}).                  \tag{1.5}
\]

Appending those masks literally cannot destroy a central witness.  The
even lift `A,{z},z+A` is literal and exact, and
`binom(2m+2,m+1)=2binom(2m+1,m)`.  This proves (0.1) for both parities.

## 2. Audit of the atomic lopsided theorem

An atomic event prescribes one value in each of several independent target
parts.  Two events which agree wherever both prescribe a value are
lopsided nonneighbors.  Conditional on the outside variables, avoiding
all such agreeing events is decreasing in the match indicators for the
fixed event.  This gives

\[
 \Pr(B_E\mid\text{avoid compatible events})\le\Pr(B_E),             \tag{2.1}
\]

with the required direction.

Every incompatible neighbor of `E` uses an alternative to at least one
`v in E`.  Repeating factors in `(0,1]` only decreases their product, so

\[
 \prod_{F\in\Gamma_{\rm lop}(E)}(1-y_F)
 \ge\prod_{v\in E}\prod_{F\in\mathcal A(v)}(1-y_F).                 \tag{2.2}
\]

The hypotheses `p_E<=y_E/prod_(v in E)c_v` and
`prod_(F in A(v))(1-y_F)>=1/c_v` therefore imply the asymmetric lopsided
local lemma exactly.  The additive form follows from
`log(1-y)>=-y/(1-y)`.

For residual lists of size at least `M`, uniform sampling and
`y_E=(c/M)^|E|` give the all-arity condition

\[
 \prod_{j\ge2}(1-(c/M)^j)^{\widetilde D_j(v)}\ge1/c.                \tag{2.3}
\]

At `c=sqrt(e)`, its logarithmic sufficient form and the pair-only bound

\[
 \widetilde D_2(v)\le{M^2-e\over2e}                 \tag{2.4}
\]

have the stated constants.  This is stronger and more asymmetric than the
old common `M^2/16` profile, but it still requires control of every arity.

The corrected unit-closure algorithm is exact: conditioning `V_s` to `v`
discards events prescribing an alternative in `V_s`, contracts events
containing `v`, and leaves other events unchanged.  Unary residual events
delete their candidate.  Omitting the first operation would be unsound;
the final theorem note includes it.

The equal-interval lemma is also exact.  If `(S,I)` and `(R,I)` have
different labels, a coordinate in their symmetric difference has every
allowed occurrence in the anchor interval deleted by the other candidate.
Thus compatible selectors are injective target-to-interval matchings, and
forced shallow candidates must reserve their physical intervals through
unit closure.

## 3. Audit of the native multiplicity obstruction

For a nonclipped source interval `I=[a,b]` of length `ell<=d`, maximal
erosion satisfies

\[
 P(I)=\bigcap_{j=b-d}^{a}T_j,
 \qquad |P(I)|=r-d+\ell-1.                         \tag{3.1}
\]

Strict residence makes the relevant departures distinct.  Therefore a
rank-`(r-1)` target forces `ell=d` and is the natural Johnson-edge facet.
Constant endpoint extension shows that a mixed-ramp interval reaching the
flat part obeys the same identity; only a wholly clipped ramp needs the
separate formula.

At each endpoint the facets omitting the second and third departure
coordinates have at most one and two ramp candidates.  If `n_S` is the
number of endpoint owners containing facet `S`, `U_0` counts unseen facets,
and the `b` deleted-edge facets are subtracted once, the exact excess is

\[
 X=\sum_{S:n_S>0}
   (n_S-1-1_{\{S\ {m cut}\}})=kb-W+U_0.           \tag{3.2}
\]

Charging repeated selected endpoint incidences to `X` gives (0.2).  The
one-cut-per-component corollary is explicitly conditional: raw PBBS has
short positive runs, so no theorem says one cut per component is
deadline-resident.

## 4. Audit of shallow and deep flags

For a strict lower flag `S=cap_(i=a)^bT_i` with `1<=q=b-a<=d`, the source
interval `[b,a+d]` has envelope exactly `S`.  Such choices make no negative
deletion from maximal erosion and may be conditioned simultaneously when
the selected opening retains their occurrences.

If `q>d`, no `S`-candidate may meet `[a+d,b]`.  For `p<b`, the departure
`P_p minus P_(p+1)` lies in `F_p minus S`; at `p=b`, the entering
difference `P_b minus P_(b-1)` comes from the owner transition `b-d-1`
inside `[a,b]` and is outside `S`.  Thus every mandatory core in the deep
central region contains an outside-`S` coordinate.  PBBS all-depth flag
loads count owner occurrences, not compiler sockets.

## 5. Audit of the exact higher-conflict bank

Fix a singleton candidate `({x},{p})`.  Its core is `{x}`.  Choose a
central `d+1` source window with `p` at one endpoint in a direction where
the neighboring erosion state omits `x`, and include one extra erosion
state beyond the other endpoint.  Their stable intersection has size at
least `r-2d-1`; after reserving `y`, it supplies

\[
                         Q=2^{r-2d-2}-1              \tag{5.1}
\]

nonempty optional subsets.  Partition the other `d` positions into
`j-1` nonempty consecutive blocks and attach distinct optional subsets to
their mandatory cores.  The resulting labels are distinct strict lower
targets, all omit `y`, and their intervals together with `{p}` partition
the central window.

The family kills the central `y` row.  Every proper subfamily occupies at
most `d` positions and cannot cover an untruncated central window; disjoint
intervals cannot kill one another's positive anchor row, and mandatory
cores preserve source nonemptiness.  Thus every family is an exact minimal
size-`j` conflict and (0.3) follows.

Since singleton candidates are one-position intervals,
`M<=|V_{\{x\}}|<=W+d`.  At `j=4`, condition
`16(Q)_3>W+d` implies `D_4>M^2/16`.  With
`r=(k+1)/2` and `d=O(sqrt(k))`, the exponent comparison
`3(r-2d-2)-2>k+1` holds eventually.  This is a full-atlas theorem only;
candidate deletion can remove the bank.

The lopsided normalization is quantitatively consistent.  If the
auxiliary candidate probabilities are at most `1/M_0`, with
`M_0>c>1` and `c^2<m_xM_0`, the whole displayed bank contributes at most

\[
 {c^2(Q/M_0)
  \over(1-cQ/M_0)(1-c^2/(m_xM_0))}                 \tag{5.2}
\]

to the opposing pressure of a singleton candidate.  At `c=sqrt(e)`,
`m_x>=2`, `M_0>=4`, and `Q/M_0<=1/10`, this is below `1/2`.  Thus the
exponential raw count is not an obstruction after probability
normalization; all other kernels still have to be bounded.

## 6. PBBS tight ports and the exact remaining condition

The audited terminal-mountain family gives raw first returns of gap
`2d+1` indexed by height-bounded Dyck roots, with count at least

\[
 {2\over L+2}\sin^2{\pi\over L+2}
 \left(4\cos^2{\pi\over L+2}\right)^{m-d},
 \qquad L=\lfloor d/2\rfloor.                      \tag{6.1}
\]

At deadline scale its logarithm is `2m-2d-O(log m)`, much larger than the
stable-cube exponent `m-2d-1`.  This is raw cyclic supply, not a resident
compiler theorem.

For deletion-only opening, a tight run survives as a singleton port unless
both boundary edges are cut.  A cut Johnson edge supplies two coordinate-
run boundary incidences, so at most one tight run per cut is destroyed in
aggregate.  This does not give a per-label survivor bound and does not
cover exterior-moving rethreading.

The exact positive target is now sharply scoped: in one upper-complete,
deadline-resident chronology, retain/construct enough tight and exterior
sockets, condition shallow envelope-exact flags with exact interval
reservation, and verify the all-arity candidate-opposing inequalities.
Omitting at most `Ck` lower targets then gives `B(k)+Ck` by literal
appending.  None of the currently audited PBBS/Pascal theorems proves this
simultaneous condition.
