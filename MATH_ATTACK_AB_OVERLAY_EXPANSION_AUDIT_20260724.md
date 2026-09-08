# Independent mathematical audit: ownership-overlay expansion and fragmentation

Date: 2026-07-24

Audited source:

```text
MATH_ATTACK_AB_OVERLAY_EXPANSION_REPORT_RAW_20260724.md
```

## Verdict

**PASS after four exact scope/boundary corrections and minor notation
repairs.**

The occurrence-pair algebra, containment-leakage identities, fragmentation
bounds, fair-heat constants, Max-Cut law, direct endpoint formulas, layered
join/coarsening theorem, and implication scale are correct.  In particular,
the factors `4` and `1/4` in the fair heat identities, the Catalan residue
scale, and the signs in the coarsening formula all check exactly.

The required corrections are:

1. The nontrivial owner-component conclusions in Theorem 2.1 require
   `m>=2`.  At `m=1` the owner-orbit graph has one isolated vertex.
2. The graph `Gamma_tau(F)` contains one edge per **transposition orbit** of
   off-diagonal bipartite ownership edges.  It is not literally the raw
   quotient with all bipartite edge multiplicities retained; that raw
   quotient has multiplicity `2a_CD` between distinct owners.
3. In Theorem 5.1, when `z=0`, the equality case is `d_K=0` for every
   component.  The phrase “has the sign of `z`” only makes sense for
   `z!=0`.
4. The fixed-word vector in Section 16 is nonzero only for `r>=2` (and, in
   general, `r<=n-2`).  At rank one it is identically zero.  The intended
   central-window application satisfies this condition for all sufficiently
   large `m`.

There is also one important scope clarification, already partly acknowledged
in the raw report: Section 13 gives a counterexample to the universal
**fixed-middle-set proof** of direct equivariance, not a counterexample to
direct component equivariance.  No nonequivariant direct endpoint component
is constructed there.

No correction changes the final substantive conclusion: fragmentation alone
does not prove positive fair heat, and the positive-cut/local-minimum lemma
remains open.

## 1. Conventions and inputs

The audit uses the following standard facts about an exact middle wreath
factor `F` on `n=2m+1` coordinates.

1. Each wreath owns exactly `n` distinct middle sets.
2. The middle-set families of the `B=Cat_m` owners partition the complete
   middle layer.
3. Applying a coordinate permutation to every owner gives another exact
   factor.
4. A bipartite ownership component owns the same set of middle roots on its
   two sides, so choosing either whole side componentwise gives an integral
   exact factor.

The overload comparison and the previously established implications from
fixed-window overload to MWB and then to the unlabelled OR theorem are inputs
to the raw report.  They are not reproved here.  The audit verifies that the
new overlay results feed those inputs with the claimed normalization.

## 2. Audit of the owner-orbit graph

### 2.1 Symmetry and row sums

For

```text
a_CD=|W_m(C) intersection tau W_m(D)|,
```

application of `tau` is a bijection to

```text
W_m(D) intersection tau W_m(C),
```

so `a_CD=a_DC`.  Exactness of `tau F` gives

```text
sum_D a_CD=n.
```

These claims are correct.

### 2.2 Diagonal formula

Let `d=d_C` be the shorter cyclic distance between the transposed
coordinates.  Among the length-`m` windows of `C`, exactly

```text
m-d     contain both coordinates,
m-d+1   contain neither coordinate.
```

These `n-2d` windows are fixed as sets.  Two distinct length-`m` cyclic
windows differing by one deleted and one inserted point must be consecutive
windows.  Their exchanged endpoints have cyclic distance `m`.  Hence an
additional exchanged pair occurs exactly when `d=m`, contributing two
windows.  Therefore

```text
a_CC=n-2d+2*1_(d=m).
```

Equation (2.1) is correct.

### 2.3 Exact meaning of `Gamma_tau(F)`

For `C!=D`, an off-diagonal middle set counted by `a_CD` is paired under
`tau` with a distinct middle set counted by `a_DC`.  It cannot be fixed by
`tau`: a fixed set would be owned by both `C` and `D` in the exact factor.
Thus the off-diagonal bipartite ownership edges form two-element `tau`-orbits.

The graph in the raw report places `a_CD` edges between `C,D`.  This is
exactly one edge for each such two-element orbit.  Its connected components
are indeed the bipartite ownership components after the canonical diagonal
owner pairs are identified.

The proof sentence saying that the off-diagonal ownership edges “give
exactly” `Gamma_tau(F)` should therefore be read as “their `tau`-orbits give
exactly `Gamma_tau(F)`.”  If every raw bipartite edge were retained after
identification, the multiplicity between `C,D` would instead be `2a_CD`.
All displayed degree and edge formulas in the report use the orbit-graph
convention and are correct under that convention.

### 2.4 Degree, cycle rank, and averaging

For `m>=2`,

```text
deg(C)=n-a_CC=2*min(d_C,m-1)>=2.
```

Every degree is even.  Hence each connected owner-orbit component is
nontrivial, Eulerian, has even cuts, and contains a multigraph cycle.  The
edge and cycle-rank formulas

```text
|E(K)|=sum_(C in K) min(d_C,m-1),
|E(K)|-|K|+1
 =1+sum_(C in K)(min(d_C,m-1)-1)
```

are correct.

For a uniform coordinate pair, the shorter distance is uniform on
`1,...,m`.  Therefore

```text
E_tau min(d_C,m-1)
 =[(1+...+(m-1))+(m-1)]/m
 =(m+1)/2-1/m.
```

Summing over the `B` owners verifies (2.4), the average-degree constant
`m+1-2/m`, and the stated lower bound on total cycle rank.

### Required boundary correction

At `m=1`, `n=3` and `B=1`.  The unique owner has `a_CC=3`, and the loopless
owner-orbit graph has one vertex of degree zero.  It neither has two owners
nor contains a cycle.  Thus the structural bullets following (2.2) require
`m>=2`.  The formulas themselves remain valid at `m=1`.

No later leakage theorem uses the missing `m=1` case: its standing range
`1<=q<=m-1` is empty there.

## 3. Audit of cyclic containment and leakage

### 3.1 Lemma 3.1

For an `(m-q)`-set `S`, the positional complement has size `m+q+1`.
A middle window containing `S` is complementary to a length-`m+1` cyclic
window lying in this complement.  If the complement runs have lengths
`ell_i`, their number is

```text
h_C(S)=sum_i (ell_i-m)_+.
```

Because `m+q+1<2(m+1)`, at most one term is nonzero, and it is at most
`q+1`.  Equality occurs exactly when the whole complement is one run,
equivalently when `S` is a cyclic `(m-q)`-interval.  Lemma 3.1 is correct,
including its equality case.

### 3.2 Theorem 3.2

A genuine cyclic occurrence contributes zero to `e_K(S)`; a nongenuine
owner contributes an integer in `0,...,q`.  This proves

```text
0<=e_K(S)<=q(s-x_K(S)).
```

The middle-root union of one transposition ownership component is
`tau`-invariant.  Counting its roots containing `S` and `T=tau S` gives

```text
(q+1)x_K(S)+e_K(S)
=(q+1)x_K(T)+e_K(T),
```

which is exactly (L).

For total leakage, each of the `ns` owned middle roots contains `C(m,q)`
rank-`m-q` subsets, while the component has `ns` genuine cyclic
rank-`m-q` occurrences.  This verifies

```text
sum_S e_K(S)=ns(C(m,q)-(q+1)).
```

Globally, a fixed `S` has `C(m+q+1,q)` middle supersets, yielding (3.5).
All constants and signs in Section 3 are correct.

## 4. Audit of fragmentation consequences

Assume `x>=y`.  From (L), nonnegativity of `e_K(S)`, and the upper bound on
`e_K(T)`,

```text
(q+1)(x-y)<=q(s-y).
```

The symmetric case proves (4.1).  Its six listed consequences are all
correct.  In particular:

```text
s=2       => |x-y|<=1 for every q,
q=1,s<=3  => |x-y|<=1.
```

If `S` is globally absent, each component of owner-size at most `L` contains
at most

```text
b=floor(qL/(q+1))
```

copies of `T`.  Convex filling by blocks of size `b` maximizes the number of
within-component pairs and proves (4.3).

The Euclidean-division presentation assumes `b>=1`.  This is automatic in
the intended regime `m>=2`, because owner components have size at least two;
otherwise the zero-cap case should be split off separately.  “Component
size” here means the number of owner vertices in the orbit graph, not the
number `2s` of vertices before the two bipartite sides are identified.

## 5. Audit of the residual occurrence-pair identity

Let

```text
x=sum_K x_K,
y=sum_K y_K,
z=x-y,
d_K=x_K-y_K.
```

Direct expansion gives

```text
2D_p=z^2-sum_K d_K^2,
D_p=sum_(K<J)d_K d_J.
```

Writing `a=sum|d_K|` gives

```text
2M_p=a-|z|,
2R_p=sum d_K^2-a,
2B_p=z^2-|z|,
```

and hence

```text
D_p=B_p-M_p-R_p.
```

Theorem 5.1 and the interpretation `M_p=min(P,N)` are correct.

### Equality-case correction

For `z!=0`, equality `D_p=B_p` holds exactly when every nonzero `d_K` has
the sign of `z` and magnitude one.  For `z=0`, equality holds exactly when

```text
d_K=0 for every K.
```

The raw wording should include this separate zero case, since “the sign of
`z`” is undefined when `z=0`.

The bounds

```text
-xy<=D_p<=C(|x-y|,2)
```

are algebraically sharp.  As the raw report later notes for its sample sign
patterns, algebraic sharpness does not assert realization by a complete
exact factor.

For a connected overlay, there is one `d_K=z`, so `D_p=0`.  For owner-size
two components, (4.1) gives `|d_K|<=1`, so `R_p=0` but `M_p` can remain.
These conclusions are correct.

## 6. Leakage-gradient and parity identities

Substitution of

```text
d_K=(e_K(T)-e_K(S))/(q+1)
```

into the preceding identity gives (HG-L) with the exact denominator
`2(q+1)^2`.  No unsigned leakage bound can determine its sign.

For `epsilon=|z| mod 2`,

```text
G_p=(z^2-epsilon)/2,
C_p=(sum d_K^2-epsilon)/2.
```

Using

```text
floor(|z|/2)=(|z|-epsilon)/2
```

verifies (7.1), (7.2), and `G_p-C_p=D_p`.  The parity constant and all
factors of two are correct.

## 7. Audit of fair heat and the conditional implication

On a moved target pair, the effect of component `K` is `(-d_K,d_K)`.
Therefore its contributions are

```text
A_tau: 2z^2,
V_tau: 2 sum_K d_K^2.
```

It follows that

```text
A_tau-V_tau=4*mathscr D_A(F,tau).
```

The floor-corrected energy differs from a squared norm only by a linear term
whose total is invariant across exact factors.  Independent fair signs have
variance `V_tau/4`, while the midpoint contracts the coherent squared norm
by `A_tau/4`.  Hence

```text
E mathcal Q_A(F_epsilon)
=mathcal Q_A(F)-(A_tau-V_tau)/4
=mathcal Q_A(F)-mathscr D_A(F,tau).
```

Theorem 7.1 is correct.  For `Psi_A=mathcal Q_A/2`, the expected decrease is
`mathscr D_A/2`.

Assuming `(RF_A)`, conditional expectation gives (8.1).  At a global
minimizer, either the energy is already below the threshold on which
`(RF_A)` is required, or comparison with the child gives (8.2).  This
case split should be kept explicit, but the conclusion is valid.

The normalization is also correct:

```text
Cat_m=W/n,
H_A*Cat_m=O_A(W/sqrt(m))=o(W).
```

The one-step additive residue has the extra factor `1/n`; the terminal
fixed-window bound does not.  A rate `1-eta_A/n` needs order
`n log W=Theta(n^2)` steps to reduce a worst-scale initial energy to the
Catalan scale.  The minimizer argument avoids that iteration.

The implications from fixed-window overload onward are unlabelled and rely
on the previously audited transfer theorems.  Nothing here proves a common
labelled or nested owner resolution.

## 8. Audit of the Max-Cut and cube-orientation formulas

If `I` is a set of components and `D_I=sum_(K in I)d_K` on one target pair,
switching `I` changes its energy by

```text
-2 D_I(z-D_I)
=-2 sum_(K in I,J notin I)d_K d_J.
```

Summing proves (9.1).  A fair random cut crosses each unordered component
pair with probability one half, so its expected decrease is exactly
`mathscr D_A`, as claimed.

All vertices of one transposition component cube have the same unoriented
component partition, and fair resampling from any vertex is uniform on that
cube.  Thus

```text
mathscr D_A(F,tau)
=mathcal Q_A(F)-average_cube mathcal Q_A.
```

Its cube average is zero.  At a global exact-factor minimizer the gap is
nonpositive for every transposition.  Equations (10.1)--(10.2) are correct,
and they correctly show why orientation-blind expansion statistics cannot
force positive fair heat at every cube vertex.

This does not obstruct a correlated positive cut, nor the thresholded
alternative in `(RF_A)`.

## 9. Audit of arbitrary endpoint overlays and the parity floor

For a direct overlay between `F` and `sigma F`, choosing either side of each
bipartite ownership component is an integral exact factor.  If
`Delta_K=b_K-a_K`, the random child has midpoint

```text
(mu+sigma mu)/2
```

and independent centered noise of variance

```text
sum_K ||Delta_K||^2/4.
```

This proves (11.1).

For each target `S`, direct expansion gives

```text
(sum_K Delta_K(S))^2-sum_K Delta_K(S)^2
=2(P_S^L+P_S^R-C_S^LR),
```

so (11.2) is correct.  Without component equivariance its negative term is
same-target left/right mixing; it cannot be replaced by a single common
owner count involving `S` and `sigma^-1 S`.

For integer endpoint difference `delta_S`,

```text
(delta_S^2-1_(delta_S odd))/4
=floor(delta_S^2/4).
```

This verifies (12.1)--(12.2).  If the total difference at a coordinate is
odd, at least one integer component difference is odd, so its component
square sum is at least one; hence `C_sigma,q>=0`.

For integers `a=x-c_q,b=y-c_q`, the inequality

```text
2 floor((x-y)^2/4)<=a(a-1)+b(b-1)
```

has residual

```text
(a+b)(a+b-2)/2       if a-b is even,
(a+b-1)^2/2          if a-b is odd.
```

The first is nonnegative because `a+b` is an even integer; there is no even
integer strictly between zero and two.  Summing over the permutation-stable
rank layer counts each energy term twice and proves `G_sigma,q<=Q_q(F)`.
All parity-floor constants are correct.

## 10. Audit of the short-permutation example

For the cyclic order `0,1,...,2m` and

```text
sigma=(0 m)(1 m+1),
```

with `m>=2`, neither transposed pair can be wholly contained in a length-`m`
window.  Each pair has exactly one length-`m` window avoiding both members,
and those two avoiding windows differ.  A set fixed by this product of
disjoint transpositions would have to contain both or neither member of each
pair.  Therefore no middle window is fixed by `sigma`.

This correctly disproves extension of the one-transposition argument that
identifies owner sides using a fixed middle-set edge.  It does **not** show
that the diagonal overlap is empty, that the owner and its image are in
different direct components, or that a direct component is nonequivariant.

For example, already at `m=2`, the middle windows `{0,1}` and `{2,3}` are
exchanged by `sigma=(0 2)(1 3)`.  Thus the displayed example has no fixed
middle window but still has a moved diagonal pair.  This is not a
counterexample to the raw report, which eventually states the correct
caveat; it shows that the section title “Failure of direct equivariance” must
be read as “Failure of the universal fixed-edge proof of direct
equivariance.”

No actual counterexample to direct component equivariance for a general
short permutation is proved in the report.

## 11. Audit of the layered join/coarsening theorem

Treat repeated wreaths in different layers as distinct layer copies.  For a
global layered component `Omega`, every vertex of `K_(i-1)` has all `n`
interface ownership edges in `K_i`, and conversely.  The induced bipartite
interface is `n`-regular on both sides, so

```text
|K_(i-1)|=|K_i|.
```

The one-transposition diagonal overlap joins every `C` to `tau_i C`.
Therefore

```text
tau_i K_(i-1) subseteq K_i.
```

Equal cardinalities make this an equality.  Iteration proves

```text
K_L=sigma K_0.
```

Closure under every ownership edge shows that adjacent `K_i` own the same
middle-root set.  The layer-zero root sets of distinct global components are
disjoint and cover the middle layer, so independent endpoint-side choices
are integral exact factors.

Collapsing the canonical diagonal spines identifies every layer copy of one
base owner.  Pulling interface `i` back to `F` gives the transposition

```text
rho_i=sigma_(i-1)^-1 tau_i sigma_(i-1).
```

The global equivalence relation is therefore exactly the join

```text
P_w=P_1 join ... join P_L.
```

Theorem 14.1 is correct.  Appending a letter can only coarsen the endpoint
bundle partition.  If one interface partition is connected, the join is
connected and the layered endpoint cube has only the two endpoint choices
`F` and `sigma F` (possibly the same factor as an unlabelled set).  With one
bundle,

```text
V_sigma=A_sigma,
G_sigma=C_sigma,
```

so the restricted fair gap is zero.

A direct `F`--`sigma F` ownership edge cannot cross layered bundles because
both endpoint owners own the same middle root.  Hence every layered bundle
is a union of direct endpoint components.  The direct overlay may be finer,
so layered connectedness does not imply direct connectedness.  All
connectedness and coarsening directions in Section 14 are correct.

## 12. Audit of the equivariant occurrence and merge formulas

For a layered endpoint bundle,

```text
b_K(S)=x_K(sigma^-1 S),
Delta_K(S)=x_K(sigma^-1 S)-x_K(S).
```

Substitution into the general endpoint identity, followed by reindexing
`S`, gives

```text
A_sigma,q-V_sigma,q
=4 sum_S P_S^sep-2 sum_S C_(S,sigma^-1 S)^sep.
```

The parity floors cancel, giving (15.2).  For a transposition the two
orientations of one moved pair have equal cross terms, and the formula
reduces to Theorem 5.1's pair expression.

When bundles `U,V` merge, their lost same-target separated pairs and lost
cross-orbit separated pairs give exactly

```text
-sum_S x_U(S)x_V(S)
+1/2 sum_S[
 x_U(S)x_V(sigma^-1 S)
 +x_V(S)x_U(sigma^-1 S)]
=-1/2 <Delta_U,Delta_V>.
```

Thus (15.1)--(15.3), including the sign, are correct.  Coarsening can help
or hurt and raw component count has no monotone heat implication.

The leakage proof also extends to a layered bundle because its middle-root
set is `sigma`-invariant.  The resulting identity uses
`T=sigma^-1 S`; no transposition-specific step is needed.

## 13. Audit of the fixed-word signed obstruction

If a word of `L` transpositions touches at most `2L<=n-4` coordinates, four
untouched coordinates `a,b,c,d` exist.  On rank `r`, put

```text
v(S)=(1_(a in S)-1_(b in S))
     (1_(c in S)-1_(d in S)).
```

For

```text
2<=r<=n-2,
```

this vector is nonzero.  Expanding it as

```text
1_(a,c subseteq S)-1_(a,d subseteq S)
-1_(b,c subseteq S)+1_(b,d subseteq S)
```

shows directly that its total and every point marginal vanish.  Every word
letter fixes all four marked coordinates, hence fixes `v`.  The endpoint
permutation and every sequential midpoint projection leave this signed
`U_2` direction unchanged.

### Required rank correction and counterexample

At `r=1`, every singleton misses at least one of the two marked coordinate
pairs, so

```text
v identically equals 0.
```

For instance, `m=2,q=1` gives `n=5,r=1`; even the empty word leaves four
untouched coordinates, but the displayed vector is zero.  Section 16 must
therefore include `r>=2`.  The intended band `q<=A sqrt(m)` has
`r=m-q>=2` for all sufficiently large `m`, so the asymptotic obstruction is
unchanged.

The result remains only a signed-space obstruction.  It does not realize
the direction as a nonnegative exact-factor difference and therefore is not
an exact-factor counterexample.

## 14. Implication and counterexample scope

The exact logical ledger after correction is:

### Unconditional

1. Owner-orbit formulas and Eulerian/cycle conclusions for `m>=2`.
2. Containment leakage and component imbalance.
3. Duplicate separation in small owner components.
4. Residual occurrence, leakage-gradient, and parity identities.
5. Fair heat, Max-Cut, and cube-average formulas.
6. Direct endpoint heat and parity bounds.
7. Layered endpoint equivariance and join/coarsening.
8. Fixed-word signed obstruction in ranks `2<=r<=n-2`.

### Conditional or external-input dependent

1. `(RF_A)` and `LM_A` remain unproved.
2. Fixed-window overload implies MWB and the unlabelled OR asymptotic only
   through the previously audited transfer results.
3. No labelled common-owner synchronization follows.
4. No direct-component nonequivariance counterexample follows from Section
   13.
5. The sign patterns `d=(1,-1)` and `d=(1,1)` are algebraic examples only,
   not complete exact-factor constructions.
6. The fixed-word `U_2` vector is a signed tangent direction only.

The global-minimizer observation is consistent with `(RF_A)`: at a minimizer
every fair cube gap is nonpositive, so a thresholded positive-gap theorem
can hold there only by forcing the energy into the Catalan residue regime.
A positive correlated component cut may exist even when the fair gap is
nonpositive, which is why `LM_A` is strictly weaker than `(RF_A)`.

## 15. Exact corrections to make in the raw report

1. In Theorem 2.1, insert `m>=2` before the claims that every component has
   at least two owners and contains a cycle.
2. Replace “off-diagonal ownership edges then give exactly
   `Gamma_tau(F)`” by “the two-element `tau`-orbits of off-diagonal ownership
   edges give exactly `Gamma_tau(F)`.”
3. In Theorem 5.1, state the equality case as:

   ```text
   if z!=0: all nonzero d_K have sign(z) and magnitude one;
   if z=0: all d_K are zero.
   ```

4. Rename Section 13 to “Failure of the universal fixed-edge proof beyond
   one transposition,” or retain its existing final caveat prominently.
5. In Section 16, add `2<=r<=n-2` to the nonzero-vector claim.
6. Repair the two malformed TeX tokens `\frac12` in (5.1) and `+\frac14`
   in the proof of (7.5), together with the malformed `\left\lfloor` in
   (7.1).  These are typesetting defects only.

With these changes, the final proved/open ledger is mathematically sound.

## Conclusion

The report's central positive theorem survives independent audit:
transposition-invariant ownership converts every component occurrence
imbalance into a signed difference of noncyclic-containment leakage, and
small owner components suppress residual same-sign concentration.  The
exact heat gap is nevertheless a cross-component sign-correlation quantity.
Neither owner-graph cycle pressure, component size, fragmentation count,
fixed-word coarsening, nor connectedness determines its sign.

Accordingly the lane ends where the raw report says it does: a proof still
requires the thresholded fair alignment theorem, the weaker positive-cut
local-minimum theorem, or a genuinely state-dependent sequential routing
argument.  The audit supplies no hidden implication to a labelled theorem
and no additional exact-factor counterexample.
