# A two-edge insurance connector closes the adjacent-upper cut row for one shortest collar

Date: 2026-08-01  
Lane: fixed-`H` q1 / adjacent-upper rooted planting  
Status: exact conditional theorem.  The upper-safe common cuts are now
automatic from one protected connected path.  Existence of an
upper-surjective Hamilton completion containing that path remains open.

## 0. Outcome

For one shortest rotating-hole collar, the bare statement

> upper-surjective aligned Hamilton target `=>` upper-safe common opening

is false already in the first legal dimension `m=4`.  An exact `ML(7)`
fixture has a reverse residual cycle every one of whose common edges is the
unique provider of its adjacent-upper colour.

There is nevertheless a deterministic repair.  Add a protected two-edge
Johnson path between the long-path endpoint `D` and the short-path endpoint
`C`.  The all-plus gadget becomes one path.  After reverse toggling, the
connector becomes a triangle, all three of whose edges have the same upper
colour.  One connector edge is therefore an automatically safe common cut.

The second cut is forced safe by the global upper excess.  If

\[
 W={2m-1\choose m},\qquad
 R_m={2m-1\choose m+1},\qquad
 \Delta_m=W-R_m={2W\over m+1},                         \tag{0.1}
\]

then every upper-surjective Hamilton target has at least `Delta_m+1` edges
whose upper colour has multiplicity at least two.  The protected connected
path has only `h+7` edges, and

\[
                         \Delta_m+1>h+7                  \tag{0.2}
\]

for every `m>=4` and `1<=h<=m-3`.  Hence one repeated-colour edge lies on
the unprotected bulk segment.  Cutting it together with one connector edge
preserves the complete adjacent-upper palette in both phases.

The incidence lift of the protected connected path has exactly

\[
                              2(h+7)                       \tag{0.3}
\]

edges and maximum degree two.  The fixed-`H` protected two-factor theorem
therefore embeds it whenever `2(h+7)<=m-2`, which holds eventually for
`h=Theta(sqrt(m))`.  That theorem does not make the completion Hamiltonian
or upper-surjective; this is the remaining correlated rooted-target gate.

## 1. Shortest collar notation

Let `Gamma` have size `2m-1`.  Fix

\[
 E=L+d,\qquad F=L+a,\qquad U=L+a+d,qquad |L|=m-1,       \tag{1.1}
\]

and a ternary choice `b in L`, `c notin U`.  Its old and plus triples are

\[
 \{AB,CD,EF\},\qquad \{AF,CB,ED\},                     \tag{1.2}
\]

where

\[
\begin{aligned}
 A&=U-b,& B&=L-b+a+c,\\
 C&=L-b+c+d,& D&=L+c.
\end{aligned}                                           \tag{1.3}
\]

Let the shortest resident return rail of depth `h` be

\[
 F=V_1\longrightarrow V_2\longrightarrow\cdots
 \longrightarrow V_{h+2}\longrightarrow V_0=E,          \tag{1.4}
\]

constructed from distinct `x_0,...,x_(h-1) in L-{b}` and the exterior
label `y` as in
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`.
Its `h+2` lower colours and upper colours are private from (1.2).

## 2. The connector

Assume

\[
 1\le h\le m-3,
 \qquad r\in L\setminus\{b,x_0,\ldots,x_{h-1}\}.         \tag{2.1}
\]

Put

\[
                     R=L+c+d,\qquad T=R-r.               \tag{2.2}
\]

Since

\[
                         D=R-d,qquad C=R-b,              \tag{2.3}
\]

the two edges

\[
                         D\longrightarrow T\longrightarrow C            \tag{2.4}
\]

form a Johnson path.  Its lower colours are

\[
                         L-r+c,qquad L-\{b,r\}+c+d,      \tag{2.5}
\]

and both upper colours are `R`.

### Lemma 2.1 (literal resource audit)

The path (2.4) has the following properties.

1. `T` is different from every owner of the rotating-hole collar.
2. The two lower colours (2.5) are distinct from one another, from all
   three ternary lower colours, and from every rail lower colour.
3. Its two upper colours equal the upper colour of `ED` in the plus phase
   and of `CD` in the old phase:
   \[
                 D\cup T=T\cup C=E\cup D=C\cup D=R.       \tag{2.6}
   \]
4. The all-plus support becomes the simple directed path
   \[
        A,V_1,V_2,\ldots,V_{h+2},V_0,D,T,C,B.             \tag{2.7}
   \]
   It has `h+7` physical edges and pairwise-distinct lower-q1 colours.

#### Proof

Equations (2.3) show Johnson adjacency and (2.5).  The first connector
lower contains `c` and omits `r`; the second contains `c,d` and omits
`b,r`.  Rail lowers contain no `c`, while the ternary lowers are

\[
                         L-b+a,\qquad L-b+c,\qquad L.      \tag{2.8}
\]

The only possible equality with `L-b+c` would require `r=b`, excluded in
(2.1).  Every internal rail owner contains `y`, whereas `T` does not;
comparison with `A,B,C,D,E,F` is immediate from (2.1)--(2.3).  The path
description and edge count now follow literally. \(\square\)

The equality (2.6) is deliberate.  The connected extension is **not** a
four-resource matching on the upper shore: it uses the colour `R` three
times locally.  It is instead a legal q1 protected path inside the
upper-surjective host.  Upper injectivity is arithmetically impossible on
this odd host anyway; the correct requirement is surjectivity.

## 3. Reverse topology and exact multiplicity invariance

Let `P+` denote (2.7), and suppose a directed q1-rainbow Hamilton cycle
`H+` contains it with the displayed orientation.  Its complementary edges
form one directed path from `B` back to `A`.

Reverse the ternary triple in (1.2), leaving the rail and connector fixed.
The result has exactly three components:

1. the resident sidecar cycle
   \[
             E-F-V_2-\cdots-V_{h+2}-E;                    \tag{3.1}
   \]
2. the triangle
   \[
                              D-T-C-D;                     \tag{3.2}
   \]
3. the bulk cycle consisting of `AB` plus the complementary `B`-to-`A`
   Hamilton path.

For an edge set `G`, write

\[
             \mu_G(S)=|\{uv\in G:u\cup v=S\}|.           \tag{3.3}
\]

### Lemma 3.1 (reverse preserves every upper multiplicity)

If `H-` is obtained from `H+` by the reverse toggle, then

\[
                              \mu_{H^-}=\mu_{H^+}.         \tag{3.4}
\]

The analogous equality holds for the lower-q1 multiplicity vector.

#### Proof

The rail and connector are common.  On the changed ternary triple, the old
and plus upper multisets are both

\[
                  \{L+a+d,\ L-b+a+c+d,\ L+c+d\},       \tag{3.5}
\]

and the lower multisets are both

\[
                         \{L-b+a,\ L-b+c,\ L\}.         \tag{3.6}
\]

All other Hamilton edges are unchanged. \(\square\)

Thus reverse toggling itself never damages the adjacent-upper palette.  The
only possible loss comes from opening edges.

## 4. The repeated-edge floor

### Lemma 4.1 (upper excess forces many safe occurrences)

Let `G` have `W` edges and cover all `R_m` upper colours.  Then at least

\[
                               \Delta_m+1                 \tag{4.1}
\]

edges of `G` have an upper colour of multiplicity at least two.

#### Proof

Let `t` be the number of upper colours having multiplicity at least two.
Since `W>R_m`, one has `t>=1`.  The number of occurrences on these colours
is

\[
 \sum_{\mu(S)\ge2}\mu(S)
 =\sum_{\mu(S)\ge2}(\mu(S)-1)+t
 =\Delta_m+t\ge\Delta_m+1.                              \tag{4.2}
\]

\(\square\)

For `m=4`, `Delta_4=14`, so (0.2) holds.  Moreover

\[
 {\Delta_{m+1}\over\Delta_m}={2(2m+1)\over m+2}\ge3
 \qquad(m\ge4),                                         \tag{4.3}
\]

while `h+7<=m+4`.  This proves (0.2) for all stated parameters.

## 5. Upper-safe common opening theorem

### Theorem 5.1 (one-collar upper insurance)

Let `m>=4`, `1<=h<=m-3`, and let `H+` be an adjacent-upper-surjective,
directed q1-rainbow Hamilton cycle containing the connected protected path
(2.7).  Reverse the ternary triple.  Then there are two edges common to
both phases such that cutting both gives:

* in the old phase: the resident cycle (3.1), one opened triangle path and
  one opened bulk path;
* in the plus phase: two paths obtained by opening the Hamilton cycle;
* in both phases: exactly the same two missing lower-q1 colours; and
* in both phases: complete adjacent-upper surjectivity.

#### Proof

Cut either connector edge, say `DT`.  Its upper colour is `R`.  In the plus
phase, `TC` and `ED` remain providers of `R`; in the old phase, `TC` and
`CD` remain providers.  Thus this common cut opens (3.2) and is upper-safe.

By Lemma 4.1 and (0.2), some repeated-upper edge `e` of `H+` lies outside
the `h+7` protected path edges.  Every outside edge belongs to the unique
complementary `B`-to-`A` path, and is common to the two phases.  Cut `e`.
If `up(e)!=R`, its original multiplicity was at least two and no other cut
has its colour.  If `up(e)=R`, then before cutting there were the three
local `R` providers in (2.6) plus `e`, so the two cuts still leave at least
two.  Lemma 3.1 transfers this argument verbatim to the reverse phase.

Both cuts are common and the original Hamilton cycle is q1-rainbow, so the
two phases lose the same two distinct lower colours.  The component claims
follow from (3.1)--(3.2) and the complementary-path description. \(\square\)

### Exact criterion without the connector

For completeness, if reverse toggling produces residual cycles
`C_1,...,C_s`, let `E_i` be the eligible common cut edges on `C_i` and put

\[
                         b(S)=\mu_{H^+}(S)-1.              \tag{5.1}
\]

One upper-safe common edge can be chosen from every residual cycle iff the
bipartite graph

\[
                  i\sim S\quad\Longleftrightarrow\quad
                  \exists e\in E_i\text{ with }up(e)=S    \tag{5.2}
\]

has a left-saturating `b`-matching.  Equivalently, for every
`I subseteq [s]`,

\[
                    |I|\le\sum_{S\in N(I)}b(S).           \tag{5.3}
\]

This is the exact paired-upper cut row.  Theorem 5.1 installs a literal
local certificate for one cycle and uses the global excess to certify the
other.

## 6. Interface with the protected two-factor theorem

The incidence lift of (2.7) is an alternating path with exactly
`2(h+7)` edges and maximum degree two.  Therefore
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
gives:

\[
                 2(h+7)\le m-2
 \quad\Longrightarrow\quad
 \text{a spanning q1 two-factor containing (2.7)}.        \tag{6.1}
\]

For `h=Theta(sqrt(m))`, (6.1) holds in all sufficiently large dimensions.
This is an unconditional connected-path planting theorem at the owner/q1
level.

It does **not** prove that the completion is Hamiltonian or covers every
adjacent-upper colour.  The exact remaining all-dimensional statement is:

> extend the protected path (2.7) to one adjacent-upper-surjective directed
> q1-rainbow Hamilton cycle.

Once that statement is available, Theorem 5.1 closes the reverse/common-cut
upper row with no additional Hall or last-witness hypothesis.

## 7. Minimal warning fixture

The connector cannot simply be omitted from the theorem.  The first legal
host is `m=4`: at `m=3`, the set outside `U` has size one, so distinct
ternary and rail exterior labels `c,y` do not exist.

On `ML(7)`, the audit fixture

```text
scratch/o1_ml7_collar_upper_unsafe_cut_20260801.audit.json
```

is a directed q1-rainbow Hamilton cycle containing the canonical aligned
`h=1` plus collar and covering all 21 rank-five upper colours.  Reverse
toggling has component sizes

\[
                              4+5+26.                    \tag{7.1}
\]

The four common edges on the five-cycle have upper colours

\[
                              47,107,122,118,             \tag{7.2}
\]

all of multiplicity one.  Therefore every common opening of that residual
cycle loses an upper colour.  This refutes automatic safe cutting, not the
existence of a favorable or insured target.

## 8. Audit

Run

```text
python3 scratch/audit_o1_shortest_collar_upper_insurance_connector_20260801.py
python3 scratch/audit_o1_ml7_collar_upper_unsafe_cut_20260801.py
```

The first replay checks all legal canonical `r` choices for
`4<=m<=10`, `1<=h<=m-3`: owner ranks, path simplicity, Johnson adjacency,
q1 injectivity, old/plus lower and upper multiplicity equality, the local
triple `R` provider, incidence size `2(h+7)`, reverse topology and (0.2).
The second independently replays the finite warning fixture without a SAT
solver.
