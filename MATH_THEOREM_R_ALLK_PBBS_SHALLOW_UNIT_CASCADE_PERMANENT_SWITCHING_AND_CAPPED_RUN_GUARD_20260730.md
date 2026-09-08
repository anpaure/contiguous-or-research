# PBBS shallow unit cascade, permanent switching, and target-capped run/guard completion

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` compiler lane  
Status: exact fixed-chronology implications and a sharp conditional PBBS
completion theorem.  No unconditional `B(k)+O(k)` conclusion is claimed.

## 0. Outcome

The permanent-minor route from handoff item 1987 has a concrete obstruction
in every one-piece strict PBBS/Pascal interval geometry, but the obstruction
occurs **before** recursive unit closure and is not a compiler no-go.
Proposition 2.3 gives the exact exceptional-seam parameter for an actual
multi-piece PBBS opening; the published cycle factor alone does not bound it
strongly enough.

For odd `k=2m+1`, in a single strict linear opening, after `W` facet targets
are conditioned on `W` distinct length-`d` columns, the raw residual
rank-`(r-2)` shore has

\[
 e(\mathcal A,R)
 \le W+2+(2d^2+1){r\choose2}.                         \tag{0.1}
\]

Since

\[
 |\mathcal A|={m\over m+2}W,                         \tag{0.2}
\]

every fractional matching saturating that shore and satisfying `x_e<=u`
has

\[
                         u\ge1-{2\over m+2}-o(1).     \tag{0.3}
\]

If ordinary Hall holds, a `1-o(1)` fraction of this shore has degree one.
Thus exact unit closure must condition almost the entire layer before any
spread matching measure can be used.  At the next staged graph the
rank-`(r-3)` shore still forces

\[
                         u\ge {1\over5}-o(1).          \tag{0.4}
\]

This proves a two-step **Pascal shallow-layer cascade**.  It does not rule
out continuing the cascade.

There is also a measure-level obstruction before injection.  On every
deadline-dense residual face, the same-column pair conflicts alone force
every common-fugacity candidate-opposing product certificate to have

\[
                         \max_e x_e
                         \ge1-{1\over\sqrt{2e}}-o(1).               \tag{0.4a}
\]

Thus uniform product pruning cannot replace the matching law.  This does
not exclude asymmetric fugacities or a distribution supported directly on
injective matchings.

After recursive closure, weighted permanent deletion ratios have an exact
alternating-component certificate.  For two residual edges `e,f`, let
`mathfrak B_H(e,f)` be the weight of pairs `(M_11,M_00)` in which `e,f`
lie in the same component of `M_11 triangle M_00`.  Then

\[
 Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).     \tag{0.5}
\]

If, in every prefix-conditioned graph,

\[
 \mathfrak B_H(e,f)
 \le {\gamma\over d}Z_{10}Z_{01},                    \tag{0.6}
\]

then every run/guard conflict `F`, whose size is at most `d+1`, satisfies

\[
 {\Pr(F)\over\prod_{e\in F}x_e}
 \le \left(1+{\gamma\over d}\right)^{|F|(|F|-1)/2}
 \le e^{\gamma|F|/2}.                                \tag{0.7}
\]

Thus the permanent constant is `C_0=e^(gamma/2)`.  No negative association
is assumed.

Finally, raw conflict count is not the right alteration cost.  Orient each
conflict to one of its target parts.  If its oriented load at target `S` is
`L_S`, the expected number of **distinct** deleted targets is at most

\[
                         \sum_S\min\{1,L_S\}.          \tag{0.8}
\]

This can be `O(k)` even when the all-arity conflict polynomial is
exponential.  The report gives a complete run/positive-guard cover
polynomial and an exact two-matching component-cube criterion using (0.8).

The smallest surviving PBBS theorem is therefore not generic robust
expansion.  It is:

1. recursively close the forced shallow Pascal layers with only `O(k)`
   omissions and no physical contradiction; then
2. prove either the alternating guard-bridge estimate (0.6) together with
   target-capped run/guard pressure `O(k)`, or construct a two-matching
   overlay whose complete component-signature pressure is `O(k)`.

Current PBBS theorems prove neither step simultaneously.

The quantitative cascade below is stated for odd `k`, where the PBBS
owner factor is available.  An even-dimensional conclusion requires an
odd/even Pascal lift whose promoted collars satisfy the same unit-closure
and run/guard-pressure hypotheses.  The known Pascal envelope identities
do not by themselves imply those hypotheses, so no automatic even transfer
is claimed.

## 1. Fixed chronology and staged candidate graphs

Put

\[
 k=2m+1,\qquad r=m+1,\qquad
 W={2m+1\choose m},                                   \tag{1.1}
\]

put

\[
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 d=\min\left\{j\ge0:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.                                     \tag{1.2}
\]

The number of interval columns of lengths `1,...,d` in a source of length
`W+d` is

\[
 N_0=dW+{d+1\choose2}=\Lambda+\sigma,
 \qquad 0\le\sigma<W+d,                              \tag{1.2a}
\]

where the strict upper bound follows from the minimality of `d`.

Throughout the shallow-layer count assume `2<=d<r`; this holds for all
sufficiently large `m`, and `d=Theta(sqrt(m))`.  Let

\[
 T=(T_0,\ldots,T_{W-1})                               \tag{1.3}
\]

be one strict linearly `d`-resident rank-`r` chronology: every `T_i` has
rank `r`, consecutive terms are adjacent in the Johnson graph, and every
untruncated positive coordinate run has length at least `d+1`.  Endpoint
runs are treated one-sided.  Let

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i
 \qquad(0\le p<W+d)                                  \tag{1.4}
\]

be its maximal erosion.  Use the certified nonempty mandatory cores

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}),              \tag{1.5}
\]

where a term involving a nonexistent source neighbor is omitted.  For an
interval `I` of length at
most `d`, put

\[
 P(I)=\bigcup_{p\in I}P_p,qquad F(I)=\bigcup_{p\in I}F_p.
\]

Put `mathcal L={S subseteq [k]:1<=|S|<=r-1}`.  The raw candidate graph has
a target vertex `S` for every `S in mathcal L` and an edge `(S,I)` exactly
when

\[
                         F(I)\subseteq S\subseteq P(I).              \tag{1.6}
\]

The necessity of the core inclusion is Lemma 1.1 of
`MATH_THEOREM_R_ALLK_RUN_BOUNDARY_CONFLICT_GIRTH_TWO_20260730.md`;
the present graph deliberately retains every envelope-feasible candidate,
so it is a fail-safe supergraph of any further PBBS pruning.

Assume that the `W` rank-`(r-1)` facet targets have mutually compatible
envelope-exact candidates on `W` distinct length-`d` columns.  Condition
those edges, reserve their columns, perform every deterministic candidate
deletion and conflict contraction they cause, and optionally omit `O(k)`
singleton targets.  Pause before conditioning the newly created unit parts
and call the resulting graph `G_2`.  Any such deletions only strengthen the
edge upper bounds below.

Section 2 is conditional only on this explicit facet reservation and does
not assume that the subsequent forced choices are physically compatible.
Section 3 adds the explicit hypothesis that the first forced layer closes
without contradiction.

For any interval lying wholly in the flat interior, and hence meeting
neither clipped endpoint ramp, the strict-residence calculation gives

\[
                         |P(I)|=r-d+|I|-1.             \tag{1.7}
\]

There are at most `d^2` intervals of length at most `d` meeting either
endpoint ramp, hence at most `2d^2` ramp exceptions in total.  Every source
interval of length at most `d` lies in some rank-`r` owner window, so

\[
                         |P(I)|\le r.                 \tag{1.8}
\]

The bounds below deliberately overcount the exceptional intervals.

## 2. Rank-`(r-2)` spread obstruction and forced units

Let

\[
 \mathcal A={ [k]\choose r-2},\qquad
 a=|\mathcal A|={2m+1\choose m-1}={m\over m+2}W,      \tag{2.1}
\]

and put

\[
 E_0=2d^2+1,qquad
 U_2=W+2+E_0{r\choose2}.                              \tag{2.2}
\]

### Theorem 2.1 (raw post-facet capacitated-cut obstruction)

The number of edges of `G_2` incident with `mathcal A` satisfies

\[
                         \boxed{e_{G_2}(\mathcal A,R)\le U_2.}      \tag{2.3}
\]

Consequently, if `o_2` targets of `mathcal A` are omitted and a fractional
matching saturates all the others with `x_e<=u`, then

\[
 \boxed{
 u\ge {a-o_2\over U_2}.}                            \tag{2.4}
\]

For `o_2=O(k)`,

\[
 u\ge1-{2\over m+2}-O\!\left({k^3\over W}\right)=1-o(1).          \tag{2.5}
\]

#### Proof

For a nonexceptional interval of length at most `d-2`, (1.7) gives
`|P(I)|<=r-3`, so it has no rank-`(r-2)` candidate.  For length `d-1`,
one has `|P(I)|=r-2`, so the column serves at most the single label `P(I)`.
There are exactly

\[
                         W+d-(d-1)+1=W+2              \tag{2.6}
\]

length-`(d-1)` columns.  There are `W+1` length-`d` columns, of which `W`
are reserved, so only one remains.  Each of that column and the at most
`2d^2` ramp exceptions supports at most `binom(r,2)` rank-`(r-2)` labels by
(1.8).  This proves (2.3).

The capacitated Hall inequality with target set `mathcal A\setminus O_2`
and interval-side set empty is

\[
                         u\,e(\mathcal A\setminus O_2,R)
                         \ge a-o_2.                   \tag{2.7}
\]

Use (2.3).  Since `d=O(sqrt(k))` and `W` is exponential, the additive term
in `U_2` is `O(k^3)=o(W)`, proving (2.5).  QED.

### Corollary 2.2 (almost all rank-`(r-2)` rows are forced)

Assume ordinary Hall feasibility on the retained rank-`(r-2)` shore.  The
number `g_2` of degree-one targets in that shore obeys

\[
 \boxed{
 g_2\ge2(a-o_2)-U_2.}                               \tag{2.8}
\]

For `o_2=O(k)`, this is

\[
 g_2\ge {m-2\over m+2}W-2-E_0{r\choose2}-O(k)
       =(1-o(1))W.                                   \tag{2.9}
\]

Their unique columns are pairwise distinct.  Hence exact unit closure must
condition all these edges unless it omits their target parts.

#### Proof

Every retained target has degree at least one.  If `g_2` have degree one
and all others have degree at least two, then

\[
 e\ge g_2+2(a-o_2-g_2)=2(a-o_2)-g_2.                 \tag{2.10}
\]

Combine this with (2.3).  Two degree-one target rows with the same unique
column violate Hall on that pair, proving distinctness.  QED.

This is not infeasibility.  It proves that the probability measure must be
introduced only **after** the forced shallow layer is closed.

### Proposition 2.3 (seam-parametric version for an actual opening)

The preceding count has an exact form which does not assume one globally
strict flat interior.  In any length-`W+d` linearization, let `xi` be the
number of interval columns of length at most `d-1` for which the flat rank
formula (1.7) is not certified, and let `h_d` be the number of unreserved
length-`d` columns.  Then

\[
 \boxed{
 e(\mathcal A,R)
 \le W+2+(\xi+h_d){r\choose2}.}                     \tag{2.11}
\]

Hence every cap-`u` saturation after `o_2` omissions satisfies

\[
 \boxed{
 u\ge {a-o_2\over W+2+(\xi+h_d)\binom r2}.}          \tag{2.12}
\]

#### Proof

Count every length-`(d-1)` column once, giving `W+2`.  A certified flat
column of shorter length serves no rank-`(r-2)` target.  Overcount every
uncertified column and every residual length-`d` column by all
`binom(r,2)` possible rank-`(r-2)` subsets of one owner.  The capacitated
cut proves (2.12).  QED.

If a linearization has `s` internal nonresident seams and every owner
footprint avoiding those seams is certified strict resident, the crude
purely geometric ledger is

\[
 \xi\le2d^2+s{(d-1)(3d-2)\over2}.                    \tag{2.13}
\]

Indeed an interval `[a,b]` of length `ell` uses the owner footprint
`[a-d,b]`; a fixed seam can meet at most `d+ell-1` such footprints.  Sum
over `ell=1,...,d-1`.  Thus a bounded-seam opening
inherits Theorem 2.1, whereas the published PBBS cycle factor with
Catalan-many separately opened components does **not** obtain (2.5) from
this count alone.  Proposition 2.3 is the checkable interface for the
actual chosen opening; no globally strict PBBS linearization is silently
assumed.

### Theorem 2.4 (deadline-density collision obstruction to product pruning)

Consider any residual face obtained from the raw graph by conditioning
target--column pairs, omitting `h` targets, and deleting further candidates
or columns.  Let `L` be its number of residual target parts and `N` the
number of residual columns supporting at least one candidate.  Then

\[
                         N\le L+\sigma+h.             \tag{2.14}
\]

In particular, if Hall holds and `L/(sigma+h) tends to infinity`, then
`L/N tends to 1`.

Now independently choose a candidate in each target part according to row
laws `pi_(s,I)`.  Put

\[
 \ell_I=\sum_s\pi_{s,I},\qquad
 u=\max_{s,I}\pi_{s,I}.                              \tag{2.15}
\]

Fix `c>1`.  Suppose the standard common-fugacity candidate-opposing
certificate is imposed: every positive candidate `v` satisfies

\[
 \sum_{E\in\mathcal A(v)}
 {c^{|E|}\Pr(E)\over1-c^{|E|}\Pr(E)}\le\log c,       \tag{2.16}
\]

with positive denominators.  Then the same-column pair conflicts alone
force

\[
 \boxed{
 (1-u)\left({L\over N}-u\right)_+
 \le {\log c\over c^2}\le {1\over2e}.}              \tag{2.17}
\]

Consequently, on every deadline-dense face with `L/N=1-o(1)`,

\[
                         u\ge1-{1\over\sqrt{2e}}-o(1).              \tag{2.18}
\]

Thus a common-fugacity product measure cannot be spread.  In particular,
uniform `M`-candidate pruning fails (2.16) asymptotically for every fixed
or growing `M>=2`.  This theorem does **not** exclude asymmetric fugacities
and does not apply to a law supported on injective matchings; it explains
why the permanent/injection step is indispensable.

#### Proof

Initially there are `Lambda` target parts and `N_0=Lambda+sigma` columns.
Conditioning one pair removes one target and one column.  Omitting a target
removes no required column, and all other deletions only reduce the column
count.  This proves (2.14).

For a positive candidate `v=(s,J)`, and every `I!=J`, choosing both
`(s,I)` and `(t,I)` is a same-column pair conflict opposing `v`.  Since
`y/(1-y)>=y`, (2.16) gives

\[
 c^2\sum_{I\ne J}\pi_{s,I}(\ell_I-\pi_{s,I})\le\log c.             \tag{2.19}
\]

Multiply by `pi_(s,J)`, sum first over `J` and then over `s`, and use
`1-pi_(s,I)>=1-u`.  The left side is at least

\[
 c^2(1-u)
 \left(\sum_I\ell_I^2-\sum_{s,I}\pi_{s,I}^2\right)
 \ge c^2L(1-u)\left({L\over N}-u\right),            \tag{2.20}
\]

because `sum_I ell_I=L`, Cauchy--Schwarz gives
`sum_I ell_I^2>=L^2/N`, and `sum_(s,I)pi_(s,I)^2<=uL`.
The left side is nonnegative, so take the positive part and divide by `L`.
Finally `max_(c>1) log(c)/c^2=1/(2e)`, attained at `c=sqrt(e)`.
Equation (2.18) follows by solving the limiting quadratic.  For a uniform
`M`-list law, `u=1/M`, and the left side of (2.17) tends to
`(1-1/M)^2>=1/4>1/(2e)`.  QED.

## 3. The next rank still has constant concentration

Assume `d>=3`, `o_2=O(k)`, and that conditioning all degree-one edges from
Corollary 2.2 produces no physical contradiction.  Contract all deterministic
consequences, pause before conditioning newly created rank-`(r-3)` units,
and call the staged graph `G_3`.  At most `E_0` of
the forced columns can be a ramp exception or the sole unreserved
length-`d` column.  Therefore the number `L_1` of unreserved
length-`(d-1)` columns in `G_3` satisfies

\[
 \boxed{
 L_1\le {4W\over m+2}+4
       +E_0\left({r\choose2}+1\right)+2o_2.}          \tag{3.1}
\]

Indeed at least `2(a-o_2)-U_2-E_0` flat length-`(d-1)` columns were forced,
and subtraction from the original `W+2` gives (3.1).

Let

\[
 \mathcal B={ [k]\choose r-3},\qquad
 b=|\mathcal B|
 ={m(m-1)\over(m+2)(m+3)}W,                          \tag{3.2}
\]

and define

\[
 U_3=W+3+(r-2)L_1+E_0{r\choose3}.                    \tag{3.3}
\]

### Theorem 3.1 (second-stage rank-`(r-3)` cut)

The number of residual edges incident with `mathcal B` is at most `U_3`.
If `o_3` targets of this layer are omitted and a fractional matching
saturates the rest with cap `u`, then

\[
                         \boxed{u\ge {b-o_3\over U_3}.}             \tag{3.4}
\]

For `o_2+o_3=O(k)`,

\[
                         \boxed{u\ge {1\over5}-o(1).}               \tag{3.5}
\]

#### Proof

A nonexceptional interval of length at most `d-3` has envelope rank at
most `r-4`, so cannot serve `mathcal B`.  A length-`(d-2)` interval has
envelope rank `r-3` and serves at most one target; there are `W+3` such
columns.  Every remaining nonexceptional length-`(d-1)` column has envelope
rank `r-2` and serves at most

\[
                         {r-2\choose r-3}=r-2        \tag{3.6}
\]

targets.  The ramp exceptions and sole length-`d` column contribute at most
`E_0 binom(r,3)` further incidences.  This proves the edge bound (3.3), and
the capacitated cut proves (3.4).

Now (3.1) gives

\[
 (r-2)L_1\le(4+o(1))W,                               \tag{3.7}
\]

while every `E_0` term is polynomial and hence `o(W)`.  Thus
`U_3\le(5+o(1))W` and `b=(1-o(1))W`, proving (3.5).  QED.

The theorem does not say that one fifth of this layer is forced.  Further
unit propagation changes the active target shore, so extending the cascade
requires a new length-by-length reservation ledger.

## 4. Weighted alternating-component switching

Let `H=(L,R;E)` be any residual target/interval graph with positive edge
weights, and let every matching under discussion saturate `L`.  Fix two
disjoint extendable edges `e,f`.  Write `Z_ab` for the total weight of
matchings in which the inclusion indicators of `(e,f)` are `(a,b)`.

Write `Z_H` for the left-saturating matching partition function and
`H\ominus F` for deletion of all endpoints of a partial matching `F`.
If `x_e=Pr_H(e)`, cancellation of edge weights gives the exact permanent-
minor identity

\[
 {\Pr_H(e,f)\over x_e x_f}
 ={Z_H Z_{H\ominus\{e,f\}}\over
   Z_{H\ominus e}Z_{H\ominus f}}.                  \tag{4.0}
\]

Thus every pair estimate below is literally a weighted permanent deletion-
ratio estimate, not an appeal to negative association.

For an ordered pair `(M_11,M_00)`, its symmetric difference is a disjoint
union of alternating cycles and right-to-right alternating paths.  Define

\[
 \mathfrak B_H(e,f)
 =\sum_{(M_{11},M_{00}):\ e,f\ {\rm in\ one\ component}}
       w(M_{11})w(M_{00}).                           \tag{4.1}
\]

### Theorem 4.1 (same-component permanent inequality)

\[
 \boxed{
 Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).}  \tag{4.2}
\]

Consequently, if

\[
                         \mathfrak B_H(e,f)
                         \le\beta Z_{10}Z_{01},       \tag{4.3}
\]

then

\[
 \boxed{
 \Pr_H(e,f)\le(1+\beta)\Pr_H(e)\Pr_H(f).}           \tag{4.4}
\]

#### Proof

For every nonexceptional pair `(M_11,M_00)`, the edges `e,f` lie in
distinct symmetric-difference components.  Swap between the two matchings
the component containing `f`.  The result lies in
`Omega_10 times Omega_01`, remains left-saturating, and has the same product
weight because its edge multiset is unchanged.  The operation is invertible
on its image.  The total weight of all nonexceptional pairs is therefore at
most `Z_10 Z_01`, proving (4.2).

Put `Z=Z_11+Z_10+Z_01+Z_00`.  Equation (4.2) gives

\[
 Z_{11}Z
 \le (Z_{11}+Z_{10})(Z_{11}+Z_{01})
       +\mathfrak B_H(e,f).                         \tag{4.5}
\]

The denominator on the right is at least `Z_10Z_01`; (4.3) proves (4.4).
QED.

### Theorem 4.2 (prefix switching implies permanent-minor control)

Let `F={e_1,...,e_j}` be an extendable partial matching with `j<=d+1`.
Fix `gamma>=0` and assume that for every ordering of `F`, every prefix
endpoint-deleted graph `H\ominus{e_1,...,e_h}`, and every two remaining
edges, the direct pair bound (4.4) holds with factor `1+gamma/d`.  When
`Z_10Z_01>0`, it is enough to certify (4.3) with

\[
                         \beta={\gamma\over d}.       \tag{4.6}
\]

Then

\[
 \boxed{
 {\Pr_H(F)\over\prod_{e\in F}x_e^H}
 \le\left(1+{\gamma\over d}\right)^{j(j-1)/2}
 \le e^{\gamma j/2}.}                               \tag{4.7}
\]

Thus the cylinder bound holds with `C_0=e^(gamma/2)`.

#### Proof

In a prefix graph, (4.4) says that conditioning one further edge increases
the marginal of another by at most `1+gamma/d`.  Conditioning the `i-1`
earlier edges therefore increases the marginal of `e_i` by at most
`(1+gamma/d)^(i-1)`.  Multiply for `i=2,...,j`.  Since `j-1<=d`,

\[
 {j(j-1)\over2}\log(1+\gamma/d)
 \le {\gamma j\over2}.                              \tag{4.8}
\]

QED.

The direct prefix hypothesis includes forced and zero-status cases, for
which the ratio certificate (4.3) need not be defined.

### Corollary 4.3 (checkable switch supply)

Suppose every exceptional pair counted by `mathfrak B_H(e,f)` has at least
`q` separating switches into `Omega_10 times Omega_01`; every output has
product weight at least `eta` times its input product; and every output is
the image of at most `b` switching incidences, counted with multiplicity.
Then

\[
                         \mathfrak B_H(e,f)
                         \le {b\over q\eta}Z_{10}Z_{01}.             \tag{4.9}
\]

In particular, for `gamma>0`,

\[
                         q\eta\ge {bd\over\gamma}                  \tag{4.10}
\]

proves the hypothesis of Theorem 4.2.  This is the exact `Omega(d)`
external switching supply required when `b,eta` are bounded.

#### Proof

Double-count weighted input--output incidences of the separating switches.
Every exceptional input contributes at least `q eta` times its own product
weight, while every output pair is charged at most `b` times.  QED.

For `gamma=0`, the required statement is instead
`mathfrak B_H(e,f)=0` for every relevant pair.

## 5. PBBS interval-link graph and the external guard-bridge gate

For a residual unit-closed PBBS graph `H`, define its interval-link graph
`mathcal J_H`.  Its vertices are residual physical interval columns, and
two columns `I,J` are adjacent when some residual target `S` has both
candidate edges.  Before unit deletions, this is exactly the existence of a
strict residual target satisfying

\[
                         F(I)\cup F(J)
                         \subseteq S
                         \subseteq P(I)\cap P(J).     \tag{5.1}
\]

### Lemma 5.1 (component separation gives zero bad-pair mass)

Every alternating component of two saturating matchings projects to a
connected subgraph of `mathcal J_H`.  Hence, if the interval columns of
`e,f` lie in distinct components of `mathcal J_H`, then

\[
                         \mathfrak B_H(e,f)=0.         \tag{5.2}
\]

This separation persists under further prefix deletion.

#### Proof

At every target visited by an alternating component, the two matching
edges connect the two corresponding interval columns by one link of
`mathcal J_H`.  Thus its projected interval set is connected.  Deleting
targets, columns, or candidate edges cannot join two link components.  QED.

The stable conflict bank exhibits the local obstruction sharply.  If one
tagged chart and block partition from item 1987 survives the displayed unit
closure, fix that retained bank.  Its auxiliary labels are

\[
                         R_h=F(J_h)\cup Z_h,qquad
                         R_h\cap C=Z_h.               \tag{5.3}
\]

The role tags and the label determine `h` and `Z_h`.  Inside this bank the
target part of `R_h` therefore has exactly one interval column, `J_h`.
The subgraph consisting only of tagged-bank candidate edges is a star
forest and has no alternating cycle.  Every
switch used to prove (4.6) must use an external interval

\[
 I'\ne J_h,qquad F(I')\subseteq R_h\subseteq P(I'),                 \tag{5.4}
\]

or, more generally, an external guard bridge satisfying (5.1).  Exact unit
closure says only that a second interval exists when the target part is not
forced.  Present PBBS all-depth support and terminal-return bounds give no
`Omega(d)` multiplicity, weight ratio, or preimage bound for such bridges.

Thus (4.10), specialized to the literal guard condition (5.1) in every
prefix residual graph, is the sharp checkable PBBS permanent-expansion
lemma.

## 6. Target-capped alteration

Let `mathcal C` be the complete inclusion-minimal physical conflict family
in a residual matching graph, and let `mu` be any law on its saturating
matchings.  For every conflict `F`, choose coefficients

\[
 \alpha_{F,S}\ge0\quad(S\in T(F)),\qquad
 \sum_{S\in T(F)}\alpha_{F,S}=1,                    \tag{6.1}
\]

where `T(F)` is its target-part set.  Put

\[
 L_S=\sum_{F:\ S\in T(F)}\alpha_{F,S}\Pr_\mu(F\subseteq M).       \tag{6.2}
\]

### Theorem 6.1 (capped target-oriented alteration)

For an upper-complete deadline-resident chronology and an initially omitted
target family `O`,

\[
 \boxed{
 \nu(k)\le B(k)+|O|+
 \left\lfloor\sum_S\min\{1,L_S\}\right\rfloor.}    \tag{6.3}
\]

#### Proof

Sample a saturating matching.  For every occurring conflict, independently
choose one of its target parts with law `alpha_(F,.)`, and delete the union
`D` of all chosen targets.  This union hits every occurring minimal
conflict, so the surviving submatching is physically compatible.  For a
fixed target,

\[
 \Pr(S\in D)
 \le\min\left\{1,
       \sum_{F:\ S\in T(F)}\alpha_{F,S}\Pr(F\subseteq M)\right\}.
                                                               \tag{6.4}
\]

Sum over `S`.  Since `|D|` is integral, one joint outcome has size at most
the floor in (6.3).  Literal appending proves the result.  QED.

If the cylinder estimate

\[
 \Pr(F\subseteq M)\le C_0^{|F|}\prod_{e\in F}x_e                  \tag{6.5}
\]

is known, substitute its right side in (6.2).  Theorem 6.1 strictly
strengthens raw conflict-mass alteration: exponentially many conflicts
oriented to one target cost at most one deletion.

For a fixed matching `M`, let `tau(M)` be the minimum number of target parts
hitting every conflict contained in `M`.  The true deterministic obstruction
to additive `O(k)` in this architecture is

\[
                         \min_{M\ {\rm saturating}}\tau(M)=\omega(k),
                                                               \tag{6.6}
\]

not an exponential count of conflicts.  Stable-bank conflicts form stars
through their anchor target and can have hitting cost one per anchor bank.

## 7. Background-aware PBBS run/guard cover polynomial

Assume every source position has the certified nonempty core (1.5), so
source-empty conflicts are impossible.  Let `Theta_0` be the compatible
family of candidates already conditioned by recursive unit closure.  Its
fixed negative background for coordinate `x` is

\[
 E_x=\{p:x\in P_p\},                                  \tag{7.1}
\]

and

\[
 D_x^0=E_x\cap
 \bigcup_{(S,I)\in\Theta_0:\ x\notin S}I.             \tag{7.2}
\]

For coordinate `x` and a residual interval column `J`, define

\[
 q_x(J)=C_0
   \sum_{e=(S,J):\ x\notin S}x_e.                    \tag{7.3}
\]

For a nonempty source-position set `U`, let

\[
 \mathfrak C_x(U)=
 \sum_{\mathcal J\in\operatorname{MinCov}(U)}
       \prod_{J\in\mathcal J}q_x(J),                \tag{7.4}
\]

where `MinCov(U)` is the family of inclusion-minimal covers of `U` by
residual interval columns.  Let `mathcal W_x` be all consecutive `d+1` position windows contained
in `E_x`.  Compatibility of `Theta_0` implies

\[
 W_0\setminus D_x^0\ne\varnothing
 \quad(W_0\in\mathcal W_x).                          \tag{7.5}
\]

Define

\[
 \mathfrak R^0=
 \sum_x\sum_{W_0\in\mathcal W_x}
       \mathfrak C_x(W_0\setminus D_x^0).            \tag{7.6}
\]

For a forced or residual candidate `a=(S,I)` and `x in S`, put

\[
 U_{a,x}^0=(E_x\setminus D_x^0)\cap I.               \tag{7.7}
\]

Every such set is nonempty after exact closure: otherwise the forced family
is incompatible or the residual candidate has a unary conflict.  For every
target `S`, define the forced-plus-residual guard load

\[
\begin{aligned}
 \mathfrak G_S^0={}&C_0
 \sum_{e=(S,I)\ {\rm residual}}x_e
 \sum_{x\in S}\mathfrak C_x(U_{e,x}^0)\\
 &+\sum_{a=(S,I)\in\Theta_0}
 \sum_{x\in S}\mathfrak C_x(U_{a,x}^0).
\end{aligned}                                                       \tag{7.8}
\]

The second line has no anchor marginal and no extra factor `C_0`: its
anchor is fixed with probability one.

For alteration purposes, every contracted forced-anchor guard conflict is
used in its **lifted** form obtained by adjoining that deterministic anchor.
Formally, sample a residual matching and extend it by all of `Theta_0` as
deterministic probability-one edges before testing these lifted events.
Their probability is unchanged, but their target sets now include the
forced anchor targets and Theorem 6.1 applies literally.

### Theorem 7.1 (complete contracted run/guard polynomial)

Assume `T` is upper-complete.  Under (6.5),

\[
 \boxed{
 \nu(k)\le B(k)+|O|+
 \left\lfloor
 \mathfrak R^0+\sum_S\min\{1,\mathfrak G_S^0\}
 \right\rfloor.}                                    \tag{7.9}
\]

#### Proof

Use the exact all-arity run-component/positive-guard classification in
Theorem 2.1 of
`MATH_THEOREM_K_ALLK_SCARCE_FIRST_PORT_HALL_AND_POSITIVE_DENSITY_COMPILER_20260730.md`.
Classify a minimal contracted conflict first as a run conflict.  The fixed
background already covers `D_x^0`; its residual negative columns therefore
form an inclusion-minimal cover of `W_0 minus D_x^0` for some
`W_0 in mathcal W_x`.  Expanding (7.4) chooses one negative candidate on
each residual column.  Dropping distinct-target and matching extendability
conditions only overcounts, while the factors `C_0` give the cylinder
weight in (6.5).  Thus the expected number of run conflicts is at most
`mathfrak R^0`.

Every remaining contracted conflict is a positive-guard conflict.  For a
residual anchor `e=(S,I)`, its negative columns minimally cover
`U_(e,x)^0`, and the anchor contributes `C_0x_e`.  For a forced anchor
`a in Theta_0`, its residual negative columns minimally cover
`U_(a,x)^0`, while the anchor has probability one.  These are exactly the
two lines of (7.8).  Orient each guard conflict to its anchor target `S`.
If that target was forced, deleting it removes one conditioned candidate
and hence relaxes every run/guard condition; downward closure makes this
safe.  Theorem 6.1 gives (7.9), paying raw count for run conflicts and
capped distinct-target cost for all guards.  QED.

Every residual cover here has at most `d+1` members for a run and at most
`d` for a guard.  Including a residual anchor gives conflict size at most
`d+1`; a forced anchor is deterministic.  Therefore Theorem 4.2 applies to
every random cylinder.  If some source core is empty, a third source-empty
cover polynomial must be added; it is not silently omitted.

### Corollary 7.2 (checkable post-closure PBBS expansion theorem)

Suppose `T` is upper-complete, recursive unit closure has total omissions
`|O_cl|=O(k)`, every prefix-conditioned residual graph satisfies the direct
pair bound of Theorem 4.2 for one constant `gamma`, and the marginals of its
weighted saturating-matching law obey

\[
 \mathfrak R^0+\sum_S\min\{1,\mathfrak G_S^0\}=O(k)   \tag{7.10}
\]

when (7.1)--(7.8) are evaluated with `C_0=e^(gamma/2)`.  Then

\[
                         \boxed{\nu(k)\le B(k)+O(k).}  \tag{7.11}
\]

#### Proof

Theorem 4.2 supplies (6.5) for every contracted run/guard conflict.  Apply
Theorem 7.1 and include `|O_cl|=O(k)`.  QED.

## 8. Two-matching PBBS component cube

There is a deterministic alternative to permanent estimates.  Let `M^0`
and `M^1` be two saturating matchings in the same fully unit-closed residual
face.  Work with the complete **contracted** conflict family produced by
that closure and lift every forced-background event by its deterministic
anchors (equivalently, adjoin the forced family `Theta_0` to both matchings
before testing physical conflicts).  Target orientations use these lifted
target sets.  Their symmetric difference
has components `mathcal K`.  Independently
choose, on each component, the `M^0` or `M^1` shore.

A physical conflict `F subseteq M^0 union M^1` is:

1. impossible under component switching if it uses both shores of one
   component;
2. fixed if all its edges lie in `M^0 cap M^1`; or
3. otherwise an exact forbidden partial assignment of component bits.

Conflicts assembled from several components must be included even if they
occur in neither endpoint matching.

For every shore-consistent conflict choose target orientations as in (6.1),
and let `p_F` be the product probability of its component signature.  Put

\[
 \mathfrak H_\triangle
 =\sum_S\min\left\{1,
       \sum_{F:\ S\in T(F)}\alpha_{F,S}p_F\right\}.                \tag{8.1}
\]

### Theorem 8.1 (component-cube completion)

If `T` is upper-complete, recursive closure omitted `O_cl`, the overlay includes the complete
shore-consistent run/guard conflict family, and

\[
                         |O_{cl}|+\mathfrak H_\triangle=O(k),       \tag{8.2}
\]

then

\[
                         \boxed{\nu(k)\le B(k)+O(k).}               \tag{8.3}
\]

#### Proof

Every component choice is a saturating matching in the same face.  Apply
Theorem 6.1 to the product law on component bits.  Fixed conflicts have
`p_F=1` and are charged to their oriented target hitting set.  QED.

An exact zero-deletion alternative is the candidate-opposing cluster
criterion or private-pivot descent on this component-signature hypergraph.

## 9. Sharp proved boundary

Proved as exact fixed-chronology implications under their displayed
conditioning hypotheses:

1. the raw post-facet graph has no `o(1)`-cap fractional matching;
2. Hall feasibility forces almost all rank-`(r-2)` rows to be units;
3. after those units are conditioned consistently, the next rank still has
   cap at least `1/5-o(1)`;
4. every common-fugacity product-pruning certificate on a deadline-dense
   face has a marginal of size at least `1-1/sqrt(2e)-o(1)`;
5. same-component alternating mass is the exact error term in the pair
   permanent inequality;
6. an `Omega(d)` bounded-congestion external guard-switch supply gives an
   absolute all-arity permanent constant;
7. target-capped alteration and the complete run/guard polynomial retain
   every arity without negative association; and
8. a two-matching component cube with capped pressure `O(k)` gives the
   desired additive bound integrally.

Not proved:

1. no theorem yet closes the forced shallow Pascal cascade in an actual
   residence-safe, upper-complete PBBS opening with only `O(k)` omissions;
2. after full closure, no PBBS theorem supplies two saturating matchings or
   `Omega(d)` external guard bridges in every prefix residual graph;
3. the product-pruning obstruction does not exclude a genuinely asymmetric
   atomic certificate;
4. neither the pressure in (7.10) nor (8.2) is presently bounded by
   `O(k)`; and
5. therefore no unconditional `B(k)+O(k)` or coefficient-one theorem
   follows.

The concrete obstruction is sharp in scope: it kills the proposed direct
spread/permanent measure **before** recursive closure, but it does not kill
the recursive Pascal route.  A genuine no-go for the latter would have to
prove that every fully closed saturating matching has target-conflict
hitting number `omega(k)`.
