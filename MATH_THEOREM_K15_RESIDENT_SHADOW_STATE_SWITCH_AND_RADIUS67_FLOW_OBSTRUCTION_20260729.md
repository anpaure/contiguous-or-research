# The resident `k=15` shadow-state switch theorem and the sharp radius-67 flow obstruction

Date: 2026-07-29

## Status

This note proves four results about the residence-clean strict `k=15`
spiral.

1. Upper `q=1` and lower `q=3` are the two projections of one exact local
   flag state

   \[
       S_i\subset L_i\subset U_i,
       \qquad (|S_i|,|L_i|,|U_i|)=(5,7,9).
   \]

2. Exact factor switches are endpoint-balanced lower-owner replacements.
   Their upper-`q=1` ledger is linear, while their lower-`q=3` ledger is a
   three-edge state-path ledger supported on seam collars.  Residence four
   has an exact finite collar test.

3. The 828 one-end actions that could repair the 67 missing upper-`q=1`
   colours have a short directed-cut obstruction.

4. More strongly, all 1,646 one- and two-end actions at Hamming radius 67
   violate an exact seven-owner capacitated flow inequality.  The inequality
   excludes even fractional endpoint-balanced repair.  Consequently every
   loop-free strict quotient factor covering upper `q=1` differs from the
   resident seed at at least

   \[
                         \boxed{68}
   \]

   lower owners.

The last conclusion is stronger than the earlier CP-SAT `UNSAT` audit: it
now has a solver-free integer certificate.  It does **not** construct a
radius-68 factor, repair the eleven lower-`q=3` holes, preserve the other
shadow layers, or produce a literal contiguous-OR word.

## 1. Frozen seed and notation

Put

\[
    k=15,\qquad r=8,\qquad m=7,
    \qquad W=\binom{15}{8}=6435,
    \qquad N=W/15=429.
\]

Coordinates are cyclically rotated by `C_15`.  Central rank-7 and rank-8
orbits are free.  The frozen seed is

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

with file SHA-256

```text
4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
```

and physical middle-cycle SHA-256

```text
b6c231aa269791db4a5457f5dc32d25f0017495418d17984236357ae6f9e0bda.
```

It is one physical cycle of length `W`, has quotient voltage one, uses every
rank-7 owner exactly once, and has no positive coordinate run of length one,
two, or three.

Write its directed physical rank-8 cycle as

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},
 \qquad i\in\mathbb Z/W\mathbb Z,                         \tag{1.1}
\]

and put

\[
 L_i=T_i\cap T_{i+1}.                                    \tag{1.2}
\]

Thus the `L_i` enumerate all rank-7 sets.  Residence four is exactly

\[
       \beta_i\ne\alpha_{i+t}
       \qquad (t=1,2,3)                                  \tag{1.3}
\]

for all `i`.  The `t=1` part already follows from the perfect lower-`q=1`
rainbow, because equality would give `L_i=L_{i+1}`.

The eleven missing lower-`q=3`, rank-5 orbit representatives are

```text
157, 285, 651, 661, 665, 837, 1187, 1233, 1349, 1585, 2329.
```

All eleven have orbit size 15, so their physical missing mass is 165.

The 67 missing upper-`q=1`, rank-9 representatives are

```text
1519, 1531, 1951, 1975, 1999, 2431, 2495, 2557, 2687,
2939, 2941, 2991, 3059, 3311, 3325, 3391, 3423, 3451,
3515, 3543, 3759, 3799, 3871, 3895, 3933, 3997, 4975,
4983, 5023, 5079, 5367, 5495, 5499, 5611, 5727, 5755,
5807, 5839, 5847, 5867, 5935, 5949, 5981, 5991, 5995,
5997, 6043, 6093, 6575, 6589, 6615, 6621, 6815, 6845,
6991, 7005, 7029, 7069, 7083, 7403, 7413, 7533, 7595,
7851, 8021, 11099, 11627.
```

The first 66 have orbit size 15 and `11627` has orbit size 5, giving physical
missing mass `66*15+5=995`.

At quotient-window level the nonzero load histograms are

\[
\begin{array}{c|c|c|c}
 &\text{covered orbits}&\text{load histogram}&\text{surplus}\\ \hline
\text{upper }q=1&268&1^{145}2^{92}3^{24}4^7&429-268=161\\
\text{lower }q=3&190&1^{54}2^{62}3^{49}4^{21}5^4&429-190=239.
\end{array}                                                \tag{1.4}
\]

In particular, 145 old upper colours and 54 old lower-`q=3` states have a
unique quotient witness and are protected unless a switch recreates them.

## 2. The common shadow-state flag

### Theorem 2.1 (the centered flag identity)

For every `i`, define

\[
 S_i=L_{i-1}\cap L_i\cap L_{i+1},
 \qquad
 U_i=L_{i-1}\cup L_i\cup L_{i+1}.                       \tag{2.1}
\]

Then

\[
\begin{aligned}
 S_i&=T_{i-1}\cap T_i\cap T_{i+1}\cap T_{i+2},\\
 U_i&=T_i\cup T_{i+1}.                                  \tag{2.2}
\end{aligned}
\]

Under residence four,

\[
 S_i=L_i-\{\beta_{i-1},\alpha_{i+1}\},
 \qquad
 U_i=L_i\cup\{\alpha_i,\beta_i\}.                     \tag{2.3}
\]

Consequently

\[
              S_i\subset L_i\subset U_i,
              \qquad (|S_i|,|L_i|,|U_i|)=(5,7,9).       \tag{2.4}
\]

Thus lower `q=3` and upper `q=1` are not independent rankwise rows: they are
the two projections of the same centered rank-`5/7/9` flag.

#### Proof

The intersection of the three consecutive edge owners is

\[
 (T_{i-1}\cap T_i)\cap(T_i\cap T_{i+1})
                    \cap(T_{i+1}\cap T_{i+2}),
\]

which is the four-state intersection in (2.2).  Since consecutive owners are
distinct rank-7 subsets of the intervening rank-8 state,

\[
 L_{i-1}\cup L_i=T_i,
 \qquad L_i\cup L_{i+1}=T_{i+1};
\]

this gives the union identity.

The element inserted on edge `i-1` is in `L_i` but absent from `T_{i-1}`;
the element deleted on edge `i+1` is in `L_i` but absent from `T_{i+2}`.
No other element of `L_i` is lost from the four-state intersection.  The two
elements are distinct by (1.3) with `t=2`, proving the first formula in
(2.3).  The second follows directly from
\(T_i=L_i\cup\{\alpha_i\}\) and
\(T_{i+1}=L_i\cup\{\beta_i\}\).  The ranks follow.  ∎

### Lemma 2.2 (exact local flag parametrization)

Let `P,L,Q` be an oriented two-edge path in `J(15,7)`.  Write uniquely

\[
       P=(L-\{y\})\cup\{x\},
       \qquad Q=(L-\{z\})\cup\{w\},                    \tag{2.5}
\]

where `y,z in L` and `x,w notin L`.  If the induced central path is
residence-clean at its internal labels, then `y!=z` and `x!=w`, and its
centered state is

\[
       S=L-\{y,z\},
       \qquad U=L\cup\{x,w\}.                           \tag{2.6}
\]

Conversely, for every fixed flag

\[
                   S_5\subset L_7\subset U_9,           \tag{2.7}
\]

there are exactly

\[
                         2!\,2!=4                       \tag{2.8}
\]

oriented local paths `P->L->Q` having centered state `(S,L,U)`.

#### Proof

In the notation of Theorem 2.1,

\[
   (y,z,x,w)=(\beta_{i-1},\alpha_{i+1},\alpha_i,\beta_i).
\]

This gives (2.6).  Conversely, order the two elements of `L-S` as `(y,z)`
and independently order the two elements of `U-L` as `(x,w)`, then use
(2.5).  These are the only choices.  This constructs the local shadow state;
embedding it into a global factor still requires endpoint balance, exterior
collars, connectivity, and voltage.  ∎

### Corollary 2.3 (static joint compatibility)

A missing rank-5 orbit `S` and missing rank-9 orbit `U` can be served at one
center only if some translates satisfy \(S\subset U\).  This condition is also
locally sufficient: between fixed physical representatives \(S\subset U\)
there are `binom(4,2)=6` possible rank-7 centers, and Lemma 2.2 gives four
oriented local paths per center.

For the frozen missing sets, the exact orbit-containment degrees on the
rank-5 side are

\[
\begin{array}{c|rrrrrrrrrrr}
S&157&285&651&661&665&837&1187&1233&1349&1585&2329\\ \hline
d(S)&34&32&35&39&37&36&36&40&38&24&38.
\end{array}                                               \tag{2.9}
\]

The degree histogram on the 67 rank-9 vertices is

\[
       2^1,3^4,4^{11},5^{15},6^{14},7^8,8^{10},9^4.      \tag{2.10}
\]

There is therefore no isolated missing target in this static flag graph.
The obstruction below is a chronology/endpoint-capacity obstruction, not a
failure of local rank containment.

## 3. Exact factor-trade algebra

Let \(\mathcal L\) be the 429 rank-7 necklace owners and \(\mathcal V\) the 429
rank-8 necklace vertices.  A catalogue choice `c=(L,a,b)` has distinct
central endpoints

\[
       u(c)=[L+\{a\}],\qquad v(c)=[L+\{b\}]             \tag{3.1}
\]

and upper colour

\[
       \kappa(c)=[L+\{a,b\}].                           \tag{3.2}
\]

Quotient self-loops are excluded.  This loses no strict quotient Hamilton
cycle, because a loop would consume both incidences at one vertex and form
an isolated component.

Put

\[
       \partial c=e_{u(c)}+e_{v(c)}\in\mathbb Z^{\mathcal V}. \tag{3.3}
\]

The resident selector chooses one `c_0(L)` at each owner.  Replacing it by
`c(L)` has endpoint current

\[
             \delta_L=\partial c(L)-\partial c_0(L).    \tag{3.4}
\]

### Theorem 3.1 (owner-exact degree criterion)

For any set \(K\subseteq\mathcal L\) of full lower-owner replacements, the
terminal selector has degree two at every central vertex if and only if

\[
                    \sum_{L\in K}\delta_L=0.            \tag{3.5}
\]

After expanding every choice through its lower incidence vertex, the
symmetric difference of any two degree-two selectors is a disjoint union of
closed alternating even circuits.  Conversely, toggling a sign-compatible
alternating circuit preserves all degrees.  In the grouped replacement
model, the support-minimal packets are the support-minimal nonzero binary
solutions of (3.5); they need not be simple cycles after lower vertices are
contracted.

#### Proof

The seed has endpoint sum `2*1`.  The terminal endpoint sum is the seed sum
plus the left side of (3.5), proving the first assertion.  In the expanded
bipartite inclusion graph, red and blue degrees agree at every upper and
lower vertex.  Pair red and blue incidences and follow them alternately;
each trail closes.  Toggling one closed trail removes and inserts equally
many incidences at every visited vertex.  Contracting lower vertices can
identify or group portions of these trails, so simple contracted cycles are
not the general minimal objects.  ∎

A solution of (3.5) is only a quotient 2-factor.  To recover one strict
physical spiral, the terminal quotient factor must also be one cycle and its
voltage must be coprime to 15.

### Theorem 3.2 (exact shadow ledgers)

Let a terminal factor be obtained by deleting a set of old choice orbits and
inserting the same number of new choice orbits.

For every rank-9 orbit `U`, its upper-`q=1` load satisfies exactly

\[
 \lambda'_9(U)=\lambda_9(U)
    -\#\{\text{deleted choices of colour }U\}
    +\#\{\text{inserted choices of colour }U\}.          \tag{3.6}
\]

Delete the changed physical seams from the seed cycle and retain the common
path interiors.  Let `c_5(S)` count terminal four-state windows wholly inside
these retained paths, allowing reversal, and let `b_5^+(S)` count terminal
four-state windows meeting at least one inserted seam.  Then

\[
                    \lambda'_5(S)=c_5(S)+b_5^+(S).       \tag{3.7}
\]

Thus an old supported target is preserved exactly when the right side stays
positive, and a hole is repaired exactly when its new-seam term is positive.
One inserted seam lies in three cyclic three-edge windows, so `b` changed
choice orbits create at most `3b` new quotient lower-`q=3` occurrences before
multi-seam windows are deduplicated.

#### Proof

Equation (3.6) is the signed choice-colour ledger.  Every terminal
three-edge window either lies wholly inside a retained path or meets an
inserted seam, giving the disjoint partition (3.7).  Reversal does not change
an intersection.  A fixed edge belongs to the three three-edge windows
starting two, one, and zero edges before it.  ∎

### Lemma 3.3 (the three-state seam signature)

Orient one inserted seam as

\[
       T_0=L\cup\{a\}\longrightarrow T_1=L\cup\{b\}.    \tag{3.8}
\]

In a residence-four terminal factor, the three lower-`q=3` states of the
windows containing this seam are

\[
\begin{aligned}
 L-\{\beta_{-2},\beta_{-1}\},\qquad
 L-\{\beta_{-1},\alpha_1\},\qquad
 L-\{\alpha_1,\alpha_2\}.                               \tag{3.9}
\end{aligned}
\]

Their complementary 2-subsets of `L` form the length-two path

\[
 \{\beta_{-2},\beta_{-1}\}
   -\{\beta_{-1},\alpha_1\}
   -\{\alpha_1,\alpha_2\}                               \tag{3.10}
\]

in `J(L,2)`.  Thus the three possible `q=3` gains of one seam are coupled;
they are not three independent target bits.

#### Proof

Intersect respectively the four states in the windows starting at edges
`-2,-1,0`.  Residence four makes all displayed deletions distinct where
needed and keeps the indicated elements in `L`.  Consecutive complementary
pairs share exactly the displayed middle element.  ∎

### Lemma 3.4 (exact residence collar)

Assume the seed has residence at least four and terminal segment interiors
are retained, possibly reversed.  The terminal cycle has residence at least
four if and only if

\[
       \beta'_p\ne\alpha'_{p+t}\qquad(t=1,2,3)           \tag{3.11}
\]

for every closed edge interval from `p` through `p+t` containing an inserted
seam.

For one isolated seam at edge zero, the only insertion/deletion index pairs
to inspect are

\[
\begin{gathered}
(-3,0),\\
(-2,0),(-2,1),\\
(-1,0),(-1,1),(-1,2),\\
(0,1),(0,2),(0,3).                                      \tag{3.12}
\end{gathered}
\]

The two distance-one pairs are automatic from the lower rainbow, leaving
seven genuine tests.  With nearby seams, one jointly checks the union of
these collars; one may not certify each seam independently.

#### Proof

A short terminal run whose closed edge span contains no inserted seam lies
wholly in one retained path.  It was already a seed run, possibly read in
reverse, contradicting seed residence.  Hence every possible new short run
is among (3.11).  Conversely, (3.11) excludes every run of lengths one to
three.  Listing the intervals of lengths one, two, and three containing edge
zero gives (3.12).  ∎

Theorems 3.1--3.2 and Lemma 3.4 are the promised exact statewise switch
criterion: endpoint balance preserves degree two, (3.6)--(3.7) preserve and
repair the two shadow supports, and (3.11) preserves residence.  Connectivity
and unit voltage remain separate global tests.  Component signatures are
additive only when no three-edge shadow window and no residence collar meets
seams from two different packets.

## 4. The sharp radius-67 action system is complete

Let `H_9` be the set of 67 missing upper colours.  Let `b` be the number of
lower owners whose catalogue choice differs from the resident selector.

### Proposition 4.1 (sharp-budget rigidity)

Every upper-`q=1`-complete selector has `b>=67`.  If `b=67`, then:

1. every new choice has a colour in `H_9`;
2. the 67 new colours are all distinct;
3. every member of `H_9` is used exactly once;
4. no old upper colour is reinserted; and
5. an old colour of seed load `h` is deleted at most `h-1` times.

#### Proof

An unchanged lower-owner choice cannot introduce a seed-missing colour, and
one changed choice has only one upper colour.  Hence at least 67 choices must
change.  Equality leaves exactly one new choice for each missing colour and
no spare choice for an old-colour relay.  The last assertion is necessary to
retain every old colour.  ∎

Accordingly, a **sharp action** `a` consists of a lower owner `ell(a)`, the
deletion of its resident choice, and the insertion of a choice whose colour
is one prescribed target `t(a) in H_9`.  Individually `q=1`-safe actions only
delete an old colour of seed load at least two.  Put

\[
       \delta_a=\partial c_{\rm new}(a)
                         -\partial c_{\rm old}(a).       \tag{4.1}
\]

There are exactly 1,646 such one- or two-end actions.  They split as

\[
        828\text{ one-end},\qquad
        816\text{ disjoint two-end},\qquad
        2\text{ zero-endpoint-current}.                  \tag{4.2}
\]

The sharp radius-67 system asks for binary `x_a` satisfying

\[
\begin{aligned}
 \sum_{a:t(a)=t}x_a&=1 &&(t\in H_9),\\
 \sum_{a:\ell(a)=L}x_a&\le1 &&(L\in\mathcal L),\\
 \sum_a x_a\delta_a&=0,                                 \tag{4.3}
\end{aligned}
\]

together with the old-colour deletion capacities from Proposition 4.1.
Conversely, any solution of these constraints is an owner-exact degree-two
selector covering all upper-`q=1` colours.  It need not be connected,
unit-voltage, residence-clean, or lower-`q=3` complete.

Thus (4.3) is a necessary subsystem of every sharp valid carrier.  The next
two sections prove that even this subsystem is infeasible.

## 5. A short directed cut for all 828 one-end actions

For a one-end action, cancel the common endpoint and orient the remaining
unit current from the removed endpoint to the inserted endpoint.  Put

\[
\begin{aligned}
 X=\{&1823,1879,1947,1949,2895,2907,3019,\\
     &3495,3693,5363,5741,6773\}\subset\mathcal V.      \tag{5.1}
\end{aligned}
\]

Direct exact catalogue inspection gives the following partition of all 828
arcs:

\[
\begin{array}{c|rrrr}
&X\to X&X\to\bar X&\bar X\to X&\bar X\to\bar X\\ \hline
\text{number of actions}&8&0&30&790.
\end{array}                                               \tag{5.2}
\]

The missing colour `6991` has exactly ten one-end actions.  All ten enter
`X`:

\[
\begin{array}{c|c|c}
\text{tail}&\text{head}&\text{lower owner}\\ \hline
2971&3693&923\\
1901&5741&1645\\
1755&1947&1691\\
3471&3495&1819\\
3993&1947&1945\\
5077&2895&2639\\
5805&2895&2891\\
5021&3495&3367\\
4951&3693&3661\\
5843&5363&5331.
\end{array}                                               \tag{5.3}
\]

### Theorem 5.1 (one-end cut obstruction)

No selection containing one one-end action for every missing upper colour
can have zero endpoint current.

#### Proof

Zero endpoint current makes the selected directed arcs a circulation, so
the number entering every vertex subset equals the number leaving it.
Equation (5.2) says no available action leaves `X`.  The selected action for
colour `6991` is one of (5.3), so at least one selected action enters `X`.
This gives strictly positive net influx and is impossible.  ∎

This proof uses neither lower-owner capacities nor old-colour capacities.
It does not cover the 818 non-one-end actions, which may move two endpoints
at once (or, for two exceptional actions, have zero endpoint current).

## 6. The complete 1,646-action capacitated-flow obstruction

The full obstruction is a weighted transshipment cut.  The following
elementary alternative is useful independently of `k=15`.

### Lemma 6.1 (owner-capacitated potential certificate)

Let actions `a` have a target `t(a)`, a unit-capacity owner `ell(a)`, and an
integer endpoint current `delta_a`.  Suppose there are integer vertex
potentials `q_v`, nonnegative owner prices `r_L`, and target demands `y_t`
such that

\[
        y_{t(a)}\le \langle q,\delta_a\rangle+r_{\ell(a)}
        \qquad\text{for every action }a,                 \tag{6.1}
\]

but

\[
                       \sum_t y_t>\sum_Lr_L.             \tag{6.2}
\]

Then there is no even fractional nonnegative solution of

\[
 \sum_{a:t(a)=t}x_a=1,
 \qquad \sum_{a:\ell(a)=L}x_a\le1,
 \qquad \sum_ax_a\delta_a=0.                            \tag{6.3}
\]

#### Proof

Multiply (6.1) by `x_a` and sum.  The target equations, endpoint balance,
and nonnegative owner prices give

\[
\begin{aligned}
 \sum_t y_t
 &=\sum_a y_{t(a)}x_a\\
 &\le \left\langle q,\sum_ax_a\delta_a\right\rangle
       +\sum_Lr_L\sum_{a:\ell(a)=L}x_a\\
 &\le\sum_Lr_L,
\end{aligned}
\]

contradicting (6.2).  ∎

### Theorem 6.2 (the seven-owner certificate)

For the 1,646 sharp `k=15` actions, Lemma 6.1 holds with only the following
seven positive owner prices:

\[
\begin{array}{c|rrrrrrr}
L&1749&1939&2873&2905&3371&3661&3669\\ \hline
r_L&59&57&11&18&168&334&289.
\end{array}                                               \tag{6.4}
\]

There is an integer potential `q` on the 429 central vertices, with 361
nonzero entries.  Define, rather than separately trusting a target table,

\[
 y_t=\min_{a:t(a)=t}
       \bigl(\langle q,\delta_a\rangle+r_{\ell(a)}\bigr).\tag{6.5}
\]

Exact integer evaluation over all actions gives

\[
        \min_a\bigl(
        \langle q,\delta_a\rangle+r_{\ell(a)}-y_{t(a)}
        \bigr)=0,                                        \tag{6.6}
\]

and

\[
             \sum_{t\in H_9}y_t=991,
             \qquad \sum_Lr_L=936.                      \tag{6.7}
\]

Therefore (4.3) is infeasible even over the reals.

#### Proof

The full integer potential is frozen in

```text
scratch/k15_radius67_lower_owner_farkas_certificate.json
```

with SHA-256

```text
5b0d4367ef6c61e3722557e7ed032a7d35869d7a317df9f4ffd5960b02499feb.
```

The solver-free verifier

```text
scratch/audit_k15_radius67_lower_owner_farkas.py
```

has SHA-256

```text
65d3dac84bd77365ff1ee039f06c421ef80cca9842983e48dd54fb4a8f390dbd.
```

It reconstructs the stable catalogue and all actions, checks choice-table
SHA-256

```text
8d09676a3c073c5bb688c6ea61d8561087f560ebcc1fac775b9a97d33b1cf08a
```

and action-table SHA-256

```text
ca2c7f8557440d98c1f8cb4113967e4586d74d86367c5db4c7c5e76611a147ed,
```

derives every `y_t` by the exact minimum (6.5), and verifies (6.6)--(6.7)
using integers only.  The maximum action slack is 2007; 65 of the 67 `y_t`
are nonzero, with `y_1951=y_8021=0`.  Lemma 6.1 now applies.  ∎

An independent audit rebuilt all 1,646 actions, checked that every old and
new choice has two distinct quotient endpoints, rechecked both catalogue
digests and every action slack, and verified the summation signs in Lemma
6.1.  It returned `PASS`.  In particular, there is no hidden quotient-loop
or endpoint-multiplicity convention in the certificate.

The support (6.4) is the readable bottleneck: endpoint balance can teleport
potential only by using those seven lower owners, but their total weighted
capacity is 936 while the 67 target commodities demand 991.  The dense
vertex potential is the exact accounting device that makes this statement
valid for every one- and two-end action.  This is a weighted flow cut, not an
unweighted seven-owner Hall-neighbourhood claim.

Notably, the proof does not use:

* old-colour deletion capacities;
* integrality of the action variables;
* connectivity or quotient voltage;
* residence; or
* any lower-`q=3` condition.

### Corollary 6.3 (sharp Hamming lower bound)

Every loop-free strict `k=15` quotient factor covering every upper-`q=1`
orbit differs from the resident seed at at least 68 lower owners.  The same
lower bound holds after imposing residence, lower-`q=3`, connectivity, unit
voltage, all other shadows, or compiler conditions.

#### Proof

Proposition 4.1 gives `b>=67`.  If `b=67`, its replacements solve the
necessary system (4.3), contrary to Theorem 6.2.  ∎

## 7. Why parity alone cannot explain the complete obstruction

Let `D` be the `429 x 1646` endpoint-current matrix and let `R` be the
`67 x 1646` target-incidence matrix.  Exact row reduction over `F_2` gives

\[
       \operatorname{rank}D=414,
       \qquad
       \operatorname{rank}\binom DR=481=414+67.          \tag{7.1}
\]

Equivalently, `R` maps `ker D` onto all of `F_2^67`.  In particular there is
a mod-2 endpoint-balanced action vector having odd incidence at every target.
Thus no linear parity invariant made only from endpoint balance and target
parities can prove full-model infeasibility.  The at-most-one owner
capacities in Theorem 6.2 are genuinely doing work.

The 14 untouched central rows are represented by

```text
703, 989, 1013, 1017, 2009, 2025, 2535,
3049, 3445, 3645, 3699, 4005, 5043, 5555.
```

Among the other 415 degree rows, their total sum is the only dependency.
The exact parity and one-end-cut verifier is

```text
scratch/audit_k15_radius67_parity_and_oneend_cut.py
```

with SHA-256

```text
9cb2d04718e5bf02a61580c416d6b84c363eca01aa48237aa35320a5e8c9c4a3.
```

Its frozen output is

```text
scratch/k15_radius67_parity_oneend_cut.audit.json
```

with SHA-256

```text
2fc6d3e3a8ab7be83fd2d13bbbcdba728b4415f54e63218daa2d2bb1a5d7b9e5.
```

## 8. Consequences for lower-`q=3` repair and alternating packets

The lower-`q=3` gate alone has the elementary support lower bound

\[
                         b\ge\lceil11/3\rceil=4          \tag{8.1}
\]

from Lemma 3.3.  It is negligible compared with the now-proved upper-`q=1`
bound `b>=68`, but it is not independent of the upper choices.  Any proposed
packet must use the common flag state of Theorem 2.1, and its three potential
`q=3` gains at each seam obey the `J(L,2)` path constraint (3.10).

The previously stored 67-change upper-colour scaffold covers eight of the
eleven missing rank-5 orbits, and a 69-change marginal scaffold covers all
eleven.  Neither contradicts Corollary 6.3: neither scaffold has degree two.
Their usefulness is only as a target-profile hint beyond the sharp radius.

For a genuine terminal packet, the exact checklist is now:

1. choose one catalogue choice at every lower owner;
2. satisfy the integral endpoint equation (3.5);
3. make the quotient factor one cycle with unit voltage modulo 15;
4. pass the joint multi-seam residence collar (3.11);
5. keep every old upper colour and add every member of `H_9` via (3.6);
6. keep every old rank-5 state and add all eleven missing ones via (3.7),
   with each seam signature constrained by (3.9)--(3.10); and
7. separately check the 47 lower-`q=2` holes, the 27 rank-10 upper holes,
   the one rank-11 upper hole, cut survival, and the literal lower compiler.

No single clean `C6` or `C8` can meet item 5, and no packet changing at most
67 owners can do so while preserving degree two.  What remains is an
integral alternating-circuit sum changing at least 68 owners and obeying one
common chronology.  A solution of only the marginal shadow ledgers is not
enough; it must pass endpoint balance and the shared state-path/collar
conditions before compiler ownership is considered.

## 9. Precise proved/open boundary

Proved here:

* the exact rank-`5/7/9` centered state identity;
* the four local realizations of every fixed flag;
* the exact endpoint-balance criterion for lower-owner replacements;
* the exact upper-`q=1`, lower-`q=3`, and residence seam ledgers;
* the 12-vertex directed cut excluding all 828 one-end sharp actions;
* the seven-owner integer-potential cut excluding all 1,646 sharp actions,
  even fractionally; and
* the strict lower bound of 68 changed lower owners.

Not proved:

* existence at radius 68 or any larger prescribed radius;
* a residence-clean degree-two factor repairing the named `q=1/q=3` holes;
* preservation or repair of the other lower and upper layers;
* quotient connectedness and unit voltage after such a repair;
* a cut retaining all required upper witnesses; or
* an exact common-owner compiler and literal contiguous-OR word.

The sharp next mathematical gate is therefore no longer a radius-67 action
selection.  It is a radius-at-least-68 alternating compound circuit with one
common physical chronology whose seam states satisfy (3.9)--(3.11) and whose
terminal factor passes the remaining graded shadow and compiler tests.
