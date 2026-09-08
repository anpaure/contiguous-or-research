# Variable-filler exchange absorbers and a cross-separated Catalan boundary bank

Date: 2026-07-31  
Status: exact local theorems and finite audits; no critical-scale internal
packing, robust leave theorem, physical cycle theorem, or all-`m` Catalan
linear matching theorem is claimed

## 0. Verdict

The fixed-filler absorber's boundary correlation can be removed, but not
for free.

For every nonincident outer pair

\[
 L\in { [2m]\choose m-1},\qquad U\in {[2m]\choose m+1},
 \qquad L\not\subset U,
\]

and every two **distinct**, independently prescribed labels
`c,d in U-L`, there is, for `m>=3`, an alternating Boolean absorber whose
new lower and upper boundary resources are respectively

\[
                         L+c,\qquad U-d.
\]

It is not nested.  At one internal lower vertex `W` it performs the exact
actuator exchange

\[
 R^+\setminus R^- = \{L+c,U-d,W+d\},\qquad
 R^-\setminus R^+ = \{W+c\}.                       \tag{0.1}
\]

Thus independent boundary labels cost one private `1-for-1` middle
actuator, or one extra vertex in the complete two-state support.  This tax
is necessary for this goal: if `R^- subset R^+` and the two added resources
are `L+c,U-d`, incidence conservation forces `c=d`.  Incident pairs
`L subset U` have an even more elementary obstruction: for the two
coordinates `c!=d` of `U-L`, the alleged independent resources are
literally equal, `L+c=U-d`.

There is also a deterministic positive boundary bank.  Put

\[
 K=\operatorname{Cat}_m,\quad N=mK,
 \quad d_0={m+1\choose2},\quad
 q=\left\lfloor {N\over m^2+d_0}\right\rfloor.     \tag{0.2}
\]

One can choose Johnson-independent banks `A` of `q` lower vertices and
`B` of `q` upper vertices with no containment from `A` to `B`.  Every
subcubic bipartite endpoint template on `A,B` then has a proper list edge
colouring `c_e in U_e-L_e`; the resources `L_e+c_e,U_e-c_e` are globally
distinct.  This removes the fixed-pair random `p^2` boundary gate on a
bank of order `Theta(K/m)`.  It does **not** pack the absorber interiors and
does not reach a `K`-gadget robust reserve.

## 1. The incidence identity

For an inclusion edge `(A,B)` with `|A|=m-1`, `|B|=m+1`, let its two
middle vertices be `X,Y`.  Coordinatewise,

\[
                         \mathbf1_X+\mathbf1_Y
                      =  \mathbf1_A+\mathbf1_B.     \tag{1.1}
\]

Consider any alternating-path absorber with off and on outer matchings.
Suppose both states are middle-injective, the states cover the same
internal outer vertices, and the on state additionally covers endpoints
`L,U`.  Summing (1.1) over the two states gives

\[
 \sum_{X\in R^+}\mathbf1_X-
 \sum_{X\in R^-}\mathbf1_X
                         =\mathbf1_L+\mathbf1_U.    \tag{1.2}
\]

This identity uses middle resources with multiplicity; middle injectivity
makes them ordinary sets here.

### Lemma 1.1 (nested independently-labelled boundary no-go)

If `R^- subset R^+` and

\[
                       R^+\setminus R^-
                           =\{L+c,U-d\},            \tag{1.3}
\]

where `c notin L` and `d in U`, then `c=d`.

#### Proof

The left side of (1.2), using (1.3), is

\[
 \mathbf1_{L+c}+\mathbf1_{U-d}
 =\mathbf1_L+\mathbf1_U+\mathbf e_c-\mathbf e_d.
\]

Comparison with (1.2) forces `e_c=e_d`.  Hence `c=d`. \(\square\)

The lemma is path-independent.  In particular, no amount of interior
schedule entropy can turn the nested two-new-resource absorber into one
with independently labelled boundary additions.

## 2. A one-switch variable-filler absorber

Let `c,d` be distinct elements of `U-L`, put

\[
                         K_0=U-\{c,d\},             \tag{2.1}
\]

and choose a simple lower Johnson path

\[
 L=L_0,L_1,\ldots,L_t=K_0                         \tag{2.2}
\]

inside `[2m]-{c,d}` such that `t>=2` and the edge unions

\[
                         Z_i=L_i\cup L_{i+1}        \tag{2.3}
\]

are distinct.  Call such a path colourful.  Fix a switch index
`1<=j<t`, put `W=L_j`, and set

\[
 f_i=\begin{cases}c&i<j,\\d&i\ge j,\end{cases}
 \qquad V_i=Z_i+f_i.                               \tag{2.4}
\]

The alternating support is

\[
             L_0,V_0,L_1,V_1,\ldots,V_{t-1},L_t,U. \tag{2.5}
\]

Its off state uses `(L_{i+1},V_i)`, `0<=i<t`; its on
state uses `(L_i,V_i)`, `0<=i<t`, together with `(L_t,U)`.

### Theorem 2.1 (exact variable-filler exchange)

The two states in (2.5) cover the same internal outer vertices, while the
on state additionally covers `L,U`.  In each state every physical middle
vertex is distinct.  Moreover (0.1) holds, the two states intersect in
exactly `2t-1` middle resources, and their union has exactly

\[
                              2t+3                 \tag{2.6}
\]

middle resources.

#### Proof

Each internal upper vertex `V_i` contains both adjacent lower vertices.
Its two middle resources on the on edge are

\[
                         Z_i,\quad L_i+f_i,
\]

and those on the off edge are

\[
                         Z_i,\quad L_{i+1}+f_i.
\]

The final edge contributes `K_0+c=U-d` and `K_0+d=U-c`.

All `Z_i` omit `c,d`.  Every other resource contains exactly one of
`c,d`; within either tag its lower base is one of the distinct path
vertices.  Hence all resources in either state are distinct.  Direct
cancellation of the tagged lists leaves

\[
 \begin{aligned}
  R^+\setminus R^-&=\{L_0+c,K_0+c,L_j+d\},\\
  R^-\setminus R^+&=\{L_j+c\},
 \end{aligned}
\]

which is (0.1).  The `t` resources `Z_i`, the `j-1` common `c`-tagged
resources, and the `t-j` common `d`-tagged resources give intersection
size `2t-1`; (2.6) follows. \(\square\)

The switch therefore replaces the occupied private actuator `W+c` by the
private actuator `W+d` while consuming the independently chosen boundary
resources `L+c,U-d`.  Compared with a constant-filler support on the same
path, whose union has `2t+2` resources, the exact tax is one resource.

### Corollary 2.2 (the one-transfer tax is optimal)

Consider the reserve semantics in which the independently prescribed
resources `L+c,U-d` are absent in the off state and are the endpoint
resources consumed by the on state.  Any middle-injective support with
`t` off edges has

\[
                         |R^-|=2t,\qquad |R^+|=2t+2.
\]

If its complete two-state union had only `2t+2` resources, then necessarily
`R^- subset R^+`; the two new resources would be exactly `L+c,U-d`.
Lemma 1.1 would force `c=d`.  Hence for `c!=d`,

\[
 |R^-\setminus R^+|\ge1,\qquad
 |R^-\cup R^+|=2t+2+|R^-\setminus R^+|\ge2t+3.    \tag{2.7}
\]

Theorem 2.1 attains equality, so one transferred actuator and one extra
support vertex are optimal under these semantics.

There is a compatible ordered orientation.  Orient every common `Z_i` as
a tail, every internal auxiliary as a head, and orient the final edge with
tail `U-d` and head `U-c`.  Then

\[
 R^-_{\rm tail}\subset R^+_{\rm tail},\qquad
 R^+_{\rm tail}\setminus R^-_{\rm tail}=\{U-d\},   \tag{2.8}
\]

while

\[
 R^+_{\rm head}\setminus R^-_{\rm head}
       =\{L+c,W+d\},\qquad
 R^-_{\rm head}\setminus R^+_{\rm head}=\{W+c\}.  \tag{2.9}
\]

Reversing every ordered edge exchanges the roles.  Consequently, for `p`
already packed gadgets of which `h` use distinct boundary labels, the
extra on-state slot counts can be balanced between the two roles at

\[
                         p+\lceil h/2\rceil         \tag{2.10}
\]

per heavier role: diagonal gadgets cost `(1,1)`, while an off-diagonal
gadget costs `(1,2)` or `(2,1)`.  Equation (2.9) is only a role ledger; it
assumes orientation freedom and says nothing about whether the named
resources are mutually disjoint.

### Lemma 2.3 (the required colourful path exists)

For `m>=3`, `L not subset U`, and distinct `c,d in U-L`, a path (2.2)
always exists.

#### Proof

Let `s=|L-U|`, which is also the Johnson distance from `L` to `K_0`.
If `s>=2`, replace the `s` coordinates of `L-U` one at a time by the `s`
coordinates of `(U-L)-{c,d}`.  This monotone geodesic is simple and its
successive unions are distinct.

If `s=1`, write `L=A+a` and `K_0=A+b`, where `|A|=m-2`.  Since
`A,a,b,c,d` occupy `m+2` coordinates, at least `m-2>=1` coordinates remain.
Choose one, `x`, and use the two-edge path

\[
                         A+a,\ A+x,\ A+b.
\]

Its two unions `A+a+x` and `A+b+x` are distinct. \(\square\)

For `m=2,s=1`, deleting `c,d` leaves only the two lower endpoints, so no
such internal switch path exists.  The finite audit records this exception.

### Lemma 2.4 (incident-pair obstruction)

If `L subset U`, write `U-L={c,d}`.  Then

\[
                           L+c=U-d,\qquad L+d=U-c.  \tag{2.11}
\]

Thus distinct coordinate labels cannot represent distinct independently
reserved boundary middle vertices for an incident pair.  This obstruction
precedes any choice of absorber path.

### Corollary 2.5 (full prescribed diamonds at distance at least three)

The stronger local theorem in

```text
MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md
```

shows that if `|L-U|>=3`, not merely one resource but the entire Boolean
diamond above `L` and the entire Boolean diamond below `U` may be prescribed
independently.  A closed construction gives an alternating support of at
most `2m+1` edges with both states physically middle-injective.  Its proof
uses a prescribed first transition, an exceptional filler, and then a
constant filler; it is not the nested two-new-resource gadget and is not
being counted by the exact one-transfer ledger (2.6)--(2.10).

The theorem's deterministic orbit audit covers every prescribed boundary
pair at every canonical distance `3<=s<m` through `m=8` (11,489 cases).
This corollary provides complete local port freedom, while Theorem 2.1
provides the sharper resource accounting for the one-port product menu.

## 3. A deterministic cross-separated boundary bank

The lower and upper outer shores both have size

\[
                  N={2m\choose m-1}={2m\choose m+1}=mK.       \tag{3.1}
\]

Both Johnson graphs `J(2m,m-1)` and `J(2m,m+1)` have degree `m^2-1`, so a
greedy independent-set choice deletes at most `m^2` candidates per chosen
vertex.  A fixed lower vertex is contained in exactly

\[
                              d_0={m+1\choose2}      \tag{3.2}

upper vertices.

### Theorem 3.1 (cross-separated banks)

With `q` as in (0.2), there are sets `A` of `q` lower vertices and `B` of
`q` upper vertices such that

1. `A` is Johnson-independent;
2. `B` is Johnson-independent; and
3. no `L in A` is contained in any `U in B`.

#### Proof

Greedily choose `q` Johnson-independent lower vertices; this is possible
because `q m^2<=N`.  Delete from the upper shore every superset of a chosen
lower vertex, at most `q d_0` vertices.  At least

\[
                  N-q d_0\ \ge\ q m^2
\]

upper vertices remain.  A second greedy Johnson-independent selection
therefore supplies `q` upper vertices.  The deletion gives property 3.
\(\square\)

In particular every cross pair has `|U-L|>=3`.

### Theorem 3.2 (subcubic diagonal boundary selection)

Let `F` be any bipartite graph on subbanks of `A,B` with maximum degree at
most three.  For each edge `e=LU`, give it the list

\[
                               C_e=U-L.              \tag{3.3}
\]

There are choices `c_e in C_e`, proper at both endpoints, such that all
middle resources

\[
                         H_e=L+c_e,\qquad T_e=U-c_e  \tag{3.4}

are pairwise distinct.

#### Proof

Every list has size at least three.  Galvin's bipartite list-edge-colouring
theorem gives a proper list edge colouring because the list size is at
least `Delta(F)`.

For two edges at a common endpoint, properness makes their resources on
that shore distinct.  At different lower endpoints, equality of two
`H` resources would make those endpoints distinct facets of one middle
set, hence Johnson-adjacent, contrary to independence of `A`.  The dual
argument handles two `T` resources.  Finally, `H_e=T_f` would imply
`L_e subset U_f`, contrary to cross-separation. \(\square\)

The theorem selects a shared filler separately on each edge; it is a
deterministic, globally correlated boundary construction, not an
independent random-pool assertion.  Since `q=Theta(K/m)`, it is also not a
critical `K`-gadget bank.

## 4. The weakest literal packing condition and a strong ledger

Let `F` be a bounded-degree bipartite endpoint template.  For every edge
`e`, let `O_e` be its internal outer vertices and let `R_e^-`, `R_e^+` be
its off/on middle-resource sets.  Let `mathcal J` be the family of endpoint
matchings that may be selected to absorb admissible leaves.

The exact pairwise test is: for each two edges `e!=f` and each state pair
`sigma,tau in {-,+}` which occurs for `(e,f)` in some `J in mathcal J`,
require `R_e^sigma` and `R_f^tau` to be disjoint.  When `mathcal J`
contains the empty selection, every singleton, and every jointly
selectable endpoint matching, this expands to the following transparent
conditions:

1. the sets `O_e` are pairwise disjoint and avoid all endpoint banks;
2. `R_e^-` and `R_f^-` are disjoint for `e!=f`;
3. `R_e^+` and `R_f^-` are disjoint for all `e!=f`; and
4. `R_e^+` and `R_f^+` are disjoint whenever some `J in mathcal J`
   contains both `e,f`.

Together with the exact endpoint condition that every admissible equal
leave has a covering matching in `F`, the preceding state-pair test is the
weakest literal finite check in this note.  A simpler strong template makes the complete
supports `R_e^- union R_e^+` pairwise disjoint; this implies conditions
2--4 but may waste resources.

For `q` one-switch gadgets with colourful path lengths `t_e`, the strong
template has the exact middle ledger

\[
                         \sum_e(2t_e+3)\le {2m\choose m}=(m+1)K. \tag{4.1}
\]

At the critical count `q=K`, (4.1) forces

\[
                         {1\over K}\sum_e t_e\le {m-2\over2}.  \tag{4.2}
\]

This is one half-step stricter than the fixed-filler nested ledger and
shows that the actuator tax is material at critical scale.  The bank in
Theorem 3.1 and the boundary choice in Theorem 3.2 do not construct the
internal sets `O_e,R_e^\pm` satisfying these conditions.  That schedule
packing, robust correlation with a bulk leave, and directed-cycle removal
remain open.

## 5. Independent audits

The solver-free script

```text
scratch/audit_catalan_variable_filler_exchange_absorber_20260731.py
```

checks every ordered nonincident outer pair and every ordered distinct
label pair through `m=5`.  It replays outer coverage, all middle resources,
(0.1), (1.2), and the exact support sizes.  It passes `456,880` exchange
gadgets (`900`, `21,280`, and `434,700` for `m=3,4,5`) and records the 24
excluded `m=2,s=1` label cases.

The separate script

```text
scratch/audit_catalan_cross_separated_boundary_bank_20260731.py
```

constructs the greedy banks for `m=2,...,8`, exactly list-colours a
canonical maximum-degree-three endpoint template, and checks every literal
resource in (3.4).  The audited bank sizes are

```text
m : 2  3  4  5  6  7   8
q : 0  1  2  5 13 39 114.
```

The finite colouring replay audits the construction, while the all-`m`
existence statement in Theorem 3.2 uses Galvin's theorem.

Frozen provenance at the time of this note is:

```text
MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md
  SHA-256 75d344bcbf1746ae85051d783a098f52a6f14d766d607f9d4ae9704430975186
scratch/audit_boolean_prescribed_boundary_absorber_20260731.py
  SHA-256 c0f76bdaab147f6a65bf8860476c5ef7d679e422fc97c35c00670a49db2d4553
scratch/boolean_prescribed_boundary_absorber_m4_m8_20260731.audit.json
  SHA-256 a1458d0b556586fe637072247d94a32e67d69444138ce4b61d34ac70e82c0811

scratch/audit_catalan_variable_filler_exchange_absorber_20260731.py
  SHA-256 4a7490fe973ca9d361cd19833953360644541070bdcc0f04d60dff8e8557ff18
scratch/catalan_variable_filler_exchange_absorber_m2_m5_20260731.audit.json
  SHA-256 b7ecc50ac5c2bb379c72a0f5726e96a45ed107af68e4f9f4e7a1d7d51b492e09
  payload c5fb7f854cf040563cb0d691f190fc282e5ff1bdae117e12f440bf14a29257ad

scratch/audit_catalan_cross_separated_boundary_bank_20260731.py
  SHA-256 9a491f519dec44cb2e990ceb11fea3171a9a3f9d607e2c61057110f8c9332c15
scratch/catalan_cross_separated_boundary_bank_m2_m8_20260731.audit.json
  SHA-256 91426ef4f1c2ef4774fee5d7d9637b5e395748eeba17b1d7435afe6ae6b1855f
  payload 1345794f64cb27b1d87ee216c19df159e3e8dc56175dfdc5ec04952b5fb58c4c
```

No statement here proves a private internal core at scale `K`, an
almost-perfect matching whose leave lands in this bank, a physical linear
forest, residence/deep-shadow/compiler acceptance, or `nu(k)=B(k)` in a
new dimension.
