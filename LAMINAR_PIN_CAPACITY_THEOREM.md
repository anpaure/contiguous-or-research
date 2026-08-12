# Laminar pin-capacity coupling for universal contiguous-OR words

## 1. Purpose and status

The rank-filtration theorem bounds the number of low-rank components, while
coordinate pin survival restricts which targets can live in each component.
Those two restrictions cannot be imposed independently: the same component
must supply both the physical interval capacity and the required coordinates.

This note gives an unrestricted all-dimensional coupling.  It assumes no
fixed derivative row, grading, endpoint schedule, or middle-level path.

Let `A=(A_1,...,A_n)` be a zero-free universal word on `[k]`.  For
`2<=r<=k`,
put

\[
 \mathcal L_{<r}=\{S\subseteq[k]:1\le |S|<r\},\qquad
 L_r=|\mathcal L_{<r}|.
\]

Let `X_r={i:|A_i|<r}` and let `C_r` be the set of nonempty interval
components of `X_r`.  For `C in C_r`, write

\[
 n_C=|C|,\qquad V_C=\bigcup_{i\in C}A_i,\qquad
 D_C=[k]\setminus V_C.
\]

If `O_b={i:b in A_i}` is the actual occurrence (pin) set of coordinate `b`,
then

\[
 b\in D_C\quad\Longleftrightarrow\quad O_b\cap C=\varnothing. \tag{1.1}
\]

Thus `D_C` is the exact component-level pin deficit.

Write

\[
 \beta_r(k)=\binom kr+\tau(k,r)
\]

for the rank-specific lower bound from rank counting.

## 2. Physical capacity inside a low component

Let `z_r` be the number of distinct rank-`r` masks that occur literally as
entries of `A`.  Every other rank-`r` target has every witness wholly inside
one component of `X_r`: a witness for a nonliteral `r`-set cannot contain an
entry of rank at least `r`.

Choose one witness for every nonliteral rank-`r` target.  Let `q_C` be the
number chosen in component `C`.  Then

\[
 \sum_{C\in C_r}q_C=\binom kr-z_r.                       \tag{2.1}
\]

Put `t_C=n_C-q_C`.  Equal-rank incomparability gives `q_C<=n_C`; in fact
`t_C>=1`.  If `q_C=n_C`, the selected incomparable intervals would use all
left and all right endpoints of the component and hence would all be
singletons, contradicting `|A_i|<r` on `C`.

Define

\[
 K_C=t_Cq_C+\binom{t_C+1}{2}.                            \tag{2.2}
\]

The segment-capacity lemma says that at most `K_C` distinct masks below rank
`r` can be represented wholly inside `C`.  Indeed, after ordering the `q_C`
selected rank-`r` witnesses, every interval of length at least `t_C+1`
contains one of them.  Hence every lower-rank witness has length at most
`t_C`, and there are exactly `K_C` such physical intervals.

The numbers `q_C` and `K_C` depend on this witness choice.  The conclusion
below holds for every such choice.  When it is applied at several ranks, the
rank-row witness choices may be made independently.

## 3. The component Hall inequality

### Theorem 3.1 (laminar pin-capacity coupling)

With the notation above, for every family `F subseteq L_{<r}`,

\[
 \boxed{
 |F|\le
 \sum_{C\in C_r}
 \min\left\{K_C,
   |\{S\in F:S\cap D_C=\varnothing\}|
 \right\}.}                                             \tag{3.1}
\]

The same word satisfies (3.1) simultaneously at every rank `2<=r<=k`, and
rank-filtration stability supplies the simultaneous node bound

\[
 |C_r|\le n-\beta_r(k)+1.                                \tag{3.2}
\]

#### Proof

Choose one witness for every `S in F`.  Because `|S|<r`, every entry of its
witness is a nonempty submask of `S` and therefore has rank below `r`.  The
witness lies in one component `C`; assign `S` to that component.

The number assigned to `C` is at most `K_C` by Section 2.  It is also at most
the number of members of `F` contained in `V_C`, because an interval inside
`C` has OR contained in `V_C`.  Containment in `V_C` is equivalent to being
disjoint from `D_C`.  Summing over components proves (3.1).  Equation (3.2)
is the original-word consequence of rank-filtration stability.  QED.

This is an exact coarse component-assignment constraint, not an interval
realizability criterion.  Replacing every minimum by `K_C` recovers the
physical component-capacity relaxation.  Replacing it by the eligibility
count recovers the coordinate-support cover.  Equation (3.1) requires the
two resources to occur in the same components.

## 4. Explicit pin-load and moment inequalities

For `1<=a<r` define

\[
 H_{r,a}(v)=\sum_{s=a}^{r-1}\binom{v-a}{s-a}.
\]

Fix an `a`-set `Q` and apply (3.1) to all lower targets containing `Q`.
Only components with `Q subseteq V_C` can serve them, and therefore

\[
 \boxed{
 H_{r,a}(k)\le
 \sum_{C:Q\subseteq V_C}
   \min\{K_C,H_{r,a}(|V_C|)\}.}                          \tag{4.1}
\]

This is a coordinatewise pin-load inequality: every target requiring all
pins in `Q` must be paid for by physical capacity in a component meeting all
of those pin sets.

Averaging (4.1) over all `a`-sets gives the scalar hierarchy

\[
 \boxed{
 \binom ka H_{r,a}(k)\le
 \sum_{C\in C_r}\binom{|V_C|}{a}
       \min\{K_C,H_{r,a}(|V_C|)\}.}                     \tag{4.2}
\]

For the complete lower ideal, (3.1) itself gives

\[
 \boxed{
 L_r\le\sum_{C\in C_r}
       \min\left\{K_C,\sum_{s=1}^{r-1}\binom{|V_C|}{s}\right\}.} \tag{4.3}
\]

At `a=r-1`, equation (4.1) says that every `(r-1)`-set is contained in the
coordinate union of some low component.  The earlier transversal conclusion
(`|C_r|<r` forces a coordinate-complete component) is a coarse corollary of
this component eligibility system.

More directly, if the empty deficit is declared to have infinite
transversal cost, then

\[
 \tau\bigl(\{D_C:C\in C_r\}\bigr)\ge r.                 \tag{4.4}
\]

Indeed, a nonempty hitting set `Q` of size below `r` would itself be a lower
target but would meet every deficit, so it would be eligible for no
component.  In particular, fewer than `r` components force one `D_C` to be
empty.  Equation (3.1) is the capacitated refinement of this transversal
law.

The joint minimum is genuinely stronger than its two marginals.  For
example, at `k=4,r=3`, an abstract two-component profile with

\[
 (K_1,K_2)=(10,3),\qquad (|V_1|,|V_2|)=(2,4)
\]

passes both separate totals

\[
 K_1+K_2\ge L_3=10,qquad
 \sum_j\sum_{s<3}\binom{|V_j|}{s}\ge10,
\]

but (4.3) gives only `min(10,3)+min(3,10)=6`.  This example is only a
strictness witness for the relaxation, not a proposed OR word.

## 5. Exact cross-rank deficit merge law

The component systems really are one laminar onion.  Since `X_r subseteq
X_{r+1}`, every component of `C_r` lies in a unique component of `C_{r+1}`.
Fix a parent `P in C_{r+1}`.  Let `Ch(P)` be its children in `C_r`, and put

\[
 E_r(P)=\{i\in P:|A_i|=r\}.
\]

As before, write

\[
 V_P=\bigcup_{i\in P}A_i,\qquad D_P=[k]\setminus V_P.
\]

The parent is the disjoint union of its children and these exact-rank
positions.  Consequently its pin deficit satisfies the exact identity

\[
 \boxed{
 D_P=
 \left(\bigcap_{C\in Ch(P)}D_C\right)
 \cap
 \left(\bigcap_{i\in E_r(P)}([k]\setminus A_i)\right),} \tag{5.1}
\]

where an empty intersection is `[k]`.

Define the newly supplied coordinates at this merge by

\[
 G_r(P)=\left(\bigcap_{C\in Ch(P)}D_C\right)\setminus D_P.
\]

Every coordinate in `G_r(P)` occurs in an exact-rank-`r` entry of `P`, so

\[
 G_r(P)\subseteq\bigcup_{i\in E_r(P)}A_i,
 \qquad |G_r(P)|\le r|E_r(P)|.                           \tag{5.2}
\]

The sets `E_r(P)` partition all literal positions of rank `r`.  If `a_r`
is their number, summing gives the global pin-erosion budget

\[
 \boxed{\sum_{P\in C_{r+1}}|G_r(P)|\le r a_r.}           \tag{5.3}
\]

Equations (3.1), (3.2), and (5.1)--(5.3) are the promised all-rank coupling:
near-extremality limits the number of component nodes; the Hall inequalities
force coordinate and physical capacity into those same nodes; and the merge
law charges every disappearance of a common child deficit to actual
rank-`r` pins.

## 6. Two structural corollaries

### Corollary 6.1 (near-extremal coordinate separator)

Suppose `A` has length `beta_r(k)+c`.  In its canonical rank-`r` reduction,
let `h_r` count entries above rank `r`, let `delta_r` count repeated literal
rank-`r` occurrences after one copy of each distinct value is retained, put
`e=h_r+delta_r`, and let `s` be the number of low components.  If

\[
 c-e+1<r,                                                \tag{6.1}
\]

then one reduced low component has coordinate union `[k]`.

Let `H` be the convex hull, in the original word, of the surviving positions
of that component.  Then `OR(H)=[k]`.  For every proper rank `1<=u<k`, the
number of rank-`u` masks not represented wholly inside `H` is at most

\[
 n-|H|.                                                  \tag{6.2}
\]

In particular `H` itself represents `[k]`, and it covers at least

\[
 (2^k-1)-(k-1)(n-|H|)                                   \tag{6.3}
\]

nonempty masks.

#### Proof

Rank-filtration stability gives `s<=c-e+1<r`.  Apply the transversal law
(4.4) in the reduced word: fewer than `r` nonempty deficits are impossible,
so one component is coordinate-complete.  Its original convex hull remains
coordinate-complete.

Fix a proper-rank target absent from `H` and choose a witness.  The witness
cannot meet both sides of `H`, since then it contains `H` and has OR `[k]`.
If it uses a position strictly left of `H`, charge it to its left endpoint;
if it uses a position strictly right of `H`, charge it to its right endpoint.
At a fixed
charged endpoint the interval ORs form an inclusion chain, so at most one
target of any fixed rank is charged there.  This proves (6.2); summing the
proper ranks and observing `OR(H)=[k]` proves (6.3).  QED.

The weaker but sometimes handier sufficient condition `c+1<r` uses an
original low component directly, since `|C_r|<=c+1`.

### Corollary 6.2 (slack-one component rigidity)

If some low component has `t_C=1`, then:

* its `n_C-1` adjacent-pair ORs are `n_C-1` distinct rank-`r` masks;
* every mask below rank `r` represented in that component occurs as a
  literal entry.

Indeed, its `q_C=n_C-1` selected rank-`r` witnesses have length at most two
and cannot be singletons, so they exhaust the adjacent pairs.  Every interval
of length at least two contains one of them and has rank at least `r`.

## 7. Verification

The independent finite checker

```text
python3 scratch/check_laminar_pin_capacity.py
```

reconstructs all interval ORs in every stored exact certificate for
`2<=k<=10` and `k=12`.  At every rank it selects the nonliteral rank-row
witnesses, checks `t_C>=1`, the assigned lower-target capacities, every
fixed-`Q` inequality (4.1), and the rank-filtration node bound.  It also
checks every parent/child deficit identity and erosion budget.  All checks
pass.  The proof, rather than the finite checker, covers arbitrary target
families in (3.1).

## 8. Scope

The theorem is necessary, not sufficient.  Coordinate union `V_C` only says
which labels are eligible for `C`; it does not assert that all eligible labels
are realized there.  The capacities `K_C` are upper bounds and need not be
tight.  Conversely, (5.3) counts newly supplied coordinates, not all changes
in the detailed occurrence sets.

No contradiction to `nu(k)=B(k)` is claimed.  Segment capacity and the
uncapacitated transversal observation were already available in this
project; the substantive new step is their min-coupled family inequality and
its laminar pin packaging.  It is a necessary coarse assignment system, not
an exact characterization of interval realizability.
