# One successor collar makes the common-mate `C8` q2/q3-transparent with an odd socket action

**Date:** 2026-08-12
**Method:** explicit Boolean-incidence collar and incoming-socket chronology
**Status:** unconditional finite local theorem and abstract ordered-two-SDR
planting.  It gives exact q2 and q3 current zero and the required odd
four-socket action.  It makes no q4-or-wider, residence, or recursive MNW
subtree claim.

## 1. Cyclic normal form

Let `C` have rank `m-3`.  Choose distinct active labels

\[
 q_0,q_1,q_2,q_3,c,z\notin C.                       \tag{1.1}
\]

All indices below are modulo four.  Put

\[
\begin{aligned}
 L_i&=C+q_i+q_{i+1},\\
 R_i&=C+q_i+q_{i+1}+q_{i+2},\\
 U_i&=C+c+q_i+q_{i+1},\\
 P_i&=C+c+q_{i+1},\\
 W_i&=C+c+q_{i+1}+z.
\end{aligned}                                       \tag{1.2}
\]

The `L_i,P_i` have rank `m-1`, and the `R_i,U_i,W_i` have rank `m`.
Every displayed containment is literal.  The old bank consists of the
four paths

\[
 \boxed{R_i-L_i-U_i-P_i-W_i\qquad(i\in\mathbb Z_4).}             \tag{1.3}
\]

Colour their four consecutive edges `0,1,0,1`.  The phase-zero `C8`
switch is

\[
                         L_iR_i\longmapsto L_iR_{i-1}.            \tag{1.4}
\]

All vertices in (1.2) are distinct.  The four proposed new edges in
(1.4) are distinct and absent from the old bank.

This specializes the common-mate detour by taking

\[
 (q_0,q_1,q_2,q_3)=(s,a,b,x),                       \tag{1.5}
\]

where `U_i=L_i+c` are the four q2-telescoping common mates.  The new point
is the common fresh successor label `z`.

## 2. Exact q2 transparency

Put

\[
                         T_i=C+c+q_i+q_{i+1}+q_{i+2}.             \tag{2.1}
\]

At `L_i`, the old and new two-owner turns are

\[
 R_i\cup U_i=T_i,
 \qquad
 R_{i-1}\cup U_i=T_{i-1}.                         \tag{2.2}
\]

Therefore the complete signed q2 current on the `L_i` bank is

\[
 \sum_i([T_{i-1}]-[T_i])=0.                         \tag{2.3}
\]

The turns at `P_i` are fixed because neither `U_iP_i` nor `P_iW_i` is
switched.  Hence the whole packet has exactly zero q2 current.

## 3. Exact q3 transparency

Orient every old path in (1.3) from `R_i` to `W_i`.  Let `V_i` be the
upper owner immediately preceding the incoming socket `R_i` in the
ambient factor.  The two length-three owner windows meeting the displayed
segment are

\[
                         V_i,R_i,U_i
 \qquad\text{and}\qquad
                         R_i,U_i,W_i.                \tag{3.1}
\]

After (1.4), the segment entering through `R_i` is

\[
                         R_i-L_{i+1}-U_{i+1}-P_{i+1}-W_{i+1};     \tag{3.2}
\]

the preceding exterior owner `V_i` is unchanged.

### Theorem 3.1 (pointwise q3 preservation)

Under the incoming-socket identification `R_i -> R_i`, both windows in
(3.1) retain exactly the same union after the switch:

\[
\begin{aligned}
 V_i\cup R_i\cup U_i
   &=V_i\cup R_i\cup U_{i+1},\\
 R_i\cup U_i\cup W_i
   &=R_i\cup U_{i+1}\cup W_{i+1}.
\end{aligned}                                       \tag{3.3}
\]

Consequently the complete occurrence-labelled q3 current is zero.

#### Proof

The first identity follows from

\[
 R_i\cup U_i=T_i=R_i\cup U_{i+1}.                  \tag{3.4}
\]

For the second, `W_i` and `W_(i+1)` each add the same fresh label `z` to
subsets already contained in `T_i`:

\[
\begin{aligned}
 R_i\cup U_i\cup W_i
 &=T_i+z,\\
 R_i\cup U_{i+1}\cup W_{i+1}
 &=T_i+z.
\end{aligned}                                       \tag{3.5}
\]

These are the only length-three owner windows meeting a reconnected edge;
all other windows are copied literally. \(\square\)

The fixed-continuation no-go in
`MATH_OBSTRUCTION_COMMON_MATE_C8_ONE_STEP_Q3_TRANSPARENCY_20260812.md`
is not contradicted.  That theorem holds the outgoing continuation `W_i`
fixed at the lower cut `L_i`.  The present collar transports the complete
outgoing segment and compares occurrences by the unchanged **incoming**
socket `R_i`, so `W_i` is coherently replaced by `W_(i+1)`.

## 4. Exact socket action and parity

Before the switch, the four displayed directed socket paths are

\[
                         R_i\longmapsto W_i.         \tag{4.1}
\]

After the switch, (3.2) gives

\[
                         R_i\longmapsto W_{i+1}.     \tag{4.2}
\]

Thus the exported lower-shore/owner socket action is the four-cycle

\[
                         i\longmapsto i+1.           \tag{4.3}
\]

It is odd.  Equivalently, (1.4) is a one-phase incidence `C8`, so the
ordered-two-SDR sign theorem gives the same sign `-1`.

### Corollary 4.1 (connector-faithful parity actuator)

The collar (1.3) simultaneously supplies:

1. exact q2 current zero;
2. exact occurrence-labelled q3 current zero;
3. a declared four-in/four-out terminal bank; and
4. the odd cyclic reconnection of that bank.

In particular it pays the parity tax of the persistent MNW creator branch
when used as one **additional**, vertex-disjoint odd actuator, without
assigning an unpriced abstract transposition to its exported endpoints.
Collaring the already-counted creator itself does not change the fact that
source plus creator contains two odd `C8`s; that paired bank still needs
this extra odd copy (or another odd action).

## 5. Ordered-two-SDR planting

The sixteen old incidences in (1.3) form a proper two-coloured linear
forest in the bounded face over `C` (`t=2`).  Declare the four new edges
`L_iR_(i-1)` initially forbidden.  The bounded phased-bank extension
theorem in
`MATH_THEOREM_SMALL_PROTECTED_FORBIDDEN_FACTOR_AND_PHASED_LOCAL_TWO_SDR_20260812.md`
therefore gives the following.

### Theorem 5.1 (abstract host)

For every sufficiently large `m`, an ordered two-SDR `(M_0,M_1)` of
`ML_m` contains all old edges (1.3) in their prescribed phases and avoids
all new edges (1.4).  Switching (1.4) produces another ordered two-SDR and
has the q2, q3, and socket properties of Corollary 4.1.

The same actuator can be planted vertex-disjointly beside any other fixed
bounded-face phase bank, after reserving disjoint active labels.

### Corollary 5.2 (odd completion of the paired MNW bank)

Adjoin one private copy of this actuator to the phase-zero source `C8`,
the phase-one common-mate creator `C8`, and any fixed `C6` transport bank.
The correction copy contributes zero q2 and q3 current and one odd socket
four-cycle.  Hence the complete three-`C8` bank is odd, while its q2 and
q3 currents are exactly those of the original source-plus-creator bank.

This is an abstract bounded occurrence theorem.  It does not prove that
the private four sockets coincide with the two inherited MNW endpoint
relocations; embedding its four-cycle into that exact recursive socket
system remains the connector-interface row.

## 5.3 Exact two-socket transposition

The four-socket actuator has a literal two-socket quotient; no abstract
parity assignment is necessary.

### Theorem 5.3 (alternating-socket first return)

For every sufficiently large `m`, the old bank (1.3) can be completed by
four pairwise vertex-disjoint, properly coloured private paths

\[
                         Q_i:W_i\longrightarrow R_i             \tag{5.1}
\]

so that the old displayed bank consists of four alternating factor cycles.
Mark only the two occurrence sockets

\[
                         B=\{R_0,R_2\}.              \tag{5.2}
\]

Then the old first-return permutation on `B` is the identity, whereas
after the `C8` switch (1.4) it is the transposition

\[
                         (R_0\ R_2).                 \tag{5.3}
\]

The switch remains exactly q2- and q3-transparent.

#### Proof

At the endpoints of the old path `R_i-L_i-U_i-P_i-W_i`, the incident
colours are respectively zero and one, and both endpoints lie on the upper
shore.  Their port parities are opposite.  The private bounded-face
connector lemma therefore supplies (5.1), mutually disjoint and avoiding
the four proposed new edges.  Include the four closed coloured cycles and
the forbidden new bank in the protected-and-forbidden factor theorem;
their total size is constant, so an ambient ordered two-SDR exists for all
large `m`.

Before the switch, every `R_i` lies on its own displayed cycle.  Thus the
first return of each marked socket in (5.2) is itself.  After the switch,
(4.2) sends the four incoming sockets in the cyclic order

\[
                         R_0,R_1,R_2,R_3,R_0.         \tag{5.4}
\]

The first marked socket encountered after `R_0` is `R_2`, and vice versa,
which proves (5.3).

The closing paths are fixed in both phases.  The q2 proof is unchanged.
For q3, the exterior predecessor `V_i` in (3.1) is simply the last owner
on `Q_i`; Theorem 3.1 allowed arbitrary fixed `V_i`.  Hence q3 remains
pointwise unchanged. \(\square\)

### Corollary 5.4 (literal crossed endpoint actuator)

Cut the two marked occurrences in (5.2).  The old state reconnects the
two labelled endpoint pairs in parallel; the switched state reconnects
them crosswise.  Therefore the actuator supplies exactly the odd
two-endpoint relocation forced by the socket-parity theorem for the
persistent-creator MNW branch.

This closes the topology/sign row for a bounded abstract occurrence bank.
It still does not identify these private sockets with the inherited MNW
recursive terminals while preserving q4+ windows; that embedding is the
remaining connector-faithful recursive-interface problem.

## 6. Sharp remaining width

The one-step theorem does not claim q4 transparency.  It has, however, a
linear-depth extension.

Reuse the one-step successor as `z_1=z`, and choose any further labels
distinctly, so that

\[
                         z_0=c,z_1=z,z_2,\ldots,z_H \tag{6.1}
\]

On the \((2m-1)\)-point middle-levels ground set this requires

\[
                         1\le H\le m-3.             \tag{6.1a}
\]

Under this condition, replace the single terminal `W_i` by the owner rail

\[
 W_{i,j}=C+q_{i+1}+z_{j-1}+z_j,
 \qquad 1\le j\le H.                                \tag{6.2}
\]

The connecting lower facet between `U_i` and `W_(i,1)` is
`C+q_(i+1)+c`; between `W_(i,j)` and `W_(i,j+1)` it is
`C+q_(i+1)+z_j`.  They are all distinct, so this is a simple Johnson rail.

### Theorem 6.1 (depth-`H` transparent collar)

For every `1<=H<=m-3`, the switch (1.4) with the rails (6.2) has zero signed
owner-window current at every width

\[
                         2\le q\le H+2.              \tag{6.3}
\]

It retains the odd socket action

\[
                         R_i\longmapsto W_{i+1,H}.   \tag{6.4}
\]

#### Proof

For `0<=j<=H`, the union of the incoming owner `R_i` and the first `j+1`
owners of output rail `i` is

\[
 R_i\cup U_i\cup W_{i,1}\cup\cdots\cup W_{i,j}
   =T_i+\{z_1,\ldots,z_j\}.                         \tag{6.5}
\]

The corresponding prefix of output rail `i+1` has exactly the same union:

\[
 R_i\cup U_{i+1}\cup W_{i+1,1}\cup\cdots\cup W_{i+1,j}
   =T_i+\{z_1,\ldots,z_j\}.                         \tag{6.6}
\]

An owner window of width at most `H+2` which crosses a switched incidence
consists of an unchanged suffix of the incoming arc, followed by `R_i`,
and a prefix appearing in (6.5).  Equations (6.5)--(6.6) preserve its
union occurrence-by-occurrence.  Windows not crossing a switched incidence
are copied literally.  This proves (6.3).  The rethread still advances the
complete output rail by one cyclic index, giving (6.4). \(\square\)

The four old rails contain

\[
                         8H+8                       \tag{6.7}
\]

selected incidences, and the new `C8` bank has four forbidden incidences.
Closing the four rails privately costs at most 72 further selected
incidences by the bounded-face connector lemma (`t=2`).  Therefore the
complete phase-fixed bank is covered by the protected-and-forbidden factor
theorem whenever, for example,

\[
                         8H+84\le m-2.               \tag{6.8}
\]

The private-connector proof remains valid here because (6.8) leaves
linearly many unused labels outside the fixed core.  In particular the
OR-word depth `H=d(k)=Theta(sqrt(m))` satisfies (6.8) for all sufficiently
large `m`.

Thus a depth-`d` odd socket actuator can be made transparent throughout
the entire short owner-window band `q<=d+2` while remaining inside the
small protected-factor budget.

Windows extending beyond the end of the rail are not controlled.  More
generally, the four-cut rethread can alter arbitrarily long crossing
intervals after grafting into large exterior bodies.

Therefore the finite protected phase gate has advanced to the exact
frontier

\[
 \boxed{\text{all }q\le H+2\text{ zero + odd socket action, with
 windows beyond the collar open}.}                  \tag{6.9}
\]

Closing the remaining long windows requires an annulus telescope,
full-union shields, or protected external witnesses.  None is inferred
from the bounded ordered-two-SDR host.

## 7. A near-shortest all-width collar

There is also a completely local all-width solution, at linear rather
than deadline scale.  Let

\[
 Z=\{z_1,\ldots,z_H\}
 =[2m-1]\setminus(C\cup\{q_0,q_1,q_2,q_3,c\}),
 \qquad H=m-3.                                      \tag{7.1}
\]

Use the neutral rail (6.2) through all of `Z`.  Choose labels
`t_i in C` and `d_i in Z`, with the `t_i` pairwise distinct and the `d_i`
pairwise distinct and disjoint from `z_(H-1),z_H`.

Colour the active-coordinate cycle with two colours by parity of the
index.  For each `i`, let `alpha_i` be the even-indexed and `beta_i` the
odd-indexed member of

\[
                         \{q_{i+2},q_{i+3}\}.        \tag{7.2}
\]

After `W_(i,H)`, append the three Johnson owners

\[
\begin{aligned}
 G_{i,1}&=(C-t_i)+q_{i+1}+z_{H-1}+z_H+d_i,\\
 G_{i,2}&=(C-t_i)+q_{i+1}+\alpha_i+z_H+d_i,\\
 F_i&=(C-t_i)+q_{i+1}+\alpha_i+\beta_i+d_i.
\end{aligned}                                       \tag{7.3}
\]

Every consecutive pair in (7.3), including `W_(i,H),G_(i,1)`, differs by
one swap.  The intervening lower facets are globally distinct: successively
they contain

\[
\begin{gathered}
 (C-t_i)+\{q_{i+1},z_{H-1},z_H\},\\
 (C-t_i)+\{q_{i+1},z_H,d_i\},\\
 (C-t_i)+\{q_{i+1},\alpha_i,d_i\}.
\end{gathered}                                      \tag{7.4}
\]

The private missing-core label `t_i` separates every bridge facet from the
neutral rail and from every other bridge.

### Theorem 7.1 (all-width transparent odd collar)

For all sufficiently large `m`, the four old paths obtained by adjoining
(7.3) to the complete neutral rails have the following properties.

1. Both old and switched owner paths are simple Johnson paths with simple
   lower-q1 palettes.
2. The `C8` switch has zero signed owner-window current at **every** width.
3. The old socket map `R_i -> F_i` becomes

   \[
                            R_i\longmapsto F_{i+1},  \tag{7.5}
   \]

   an odd four-cycle.
4. The union of every complete outgoing collar is the full ground set
   `[2m-1]`.

#### Proof

Johnson adjacency and lower-colour simplicity follow from (6.2)--(7.4).
Owner simplicity follows from the active index on every neutral rail and
the private missing-core labels on the bridge.

Up to the end of the neutral rail, prefix equality is Theorem 6.1.  At
`G_(i,1)`, the lost core label `t_i` and the new tag `d_i` both already
belong to the accumulated union `C union Z`, so equality persists.

Fix the incoming socket `R_i`.  The only active coordinate absent from
`T_i` is `q_(i+3)`.  That coordinate belongs to both target pairs

\[
 \{q_{i+2},q_{i+3}\}
 \quad\text{and}\quad
 \{q_{i+3},q_i\}                                   \tag{7.6}
\]

for output rails `i` and `i+1`.  Its introduction stage in (7.3) is
determined solely by the parity of its own index, so it is introduced at
the same stage on both rails.  The other active coordinate introduced on
either rail already belongs to `T_i`.  Hence every prefix ending in the
bridge has the same union before and after the switch.

At the end of the bridge, one output collar contains

\[
 C\cup Z\cup\{q_0,q_1,q_2,q_3,c\}=[2m-1].           \tag{7.7}
\]

Thus a crossing interval ending inside the collar is preserved by prefix
equality, while one extending beyond it contains the full collar and has
union `[2m-1]` in both phases.  Intervals not crossing a switched incidence
are copied literally.  This proves all-width current zero.  The complete
output path is still shifted from index `i` to `i+1`, proving (7.5).
\(\square\)

### Proposition 7.2 (linear length is forced for a full-union shield)

Any rank-`m` Johnson owner path on `[2m-1]` whose union is the full ground
set has at least `m` owners.

#### Proof

The first owner contributes `m` coordinates and every Johnson step adds at
most one new coordinate.  Reaching `2m-1` coordinates therefore requires
at least `m-1` steps, hence `m` owners. \(\square\)

The collar in Theorem 7.1 uses

\[
                         m+1                        \tag{7.8}
\]

outgoing owners (`U_i`, `m-3` neutral owners, and three bridge owners), so
it is within one owner of the sharp full-union lower bound.

Its four old paths contain

\[
                         8m+8                       \tag{7.9}
\]

selected incidences before any exterior closing paths.  This necessarily
lies outside the `m-2` allowance of the small protected-factor theorem.
Accordingly Theorem 7.1 is an explicit local phase/deck/socket module, but
not yet a spanning ordered-two-SDR host theorem.

The all-width problem has therefore separated cleanly:

\[
 \boxed{
 \text{linear, near-shortest transparent collar exists; its protected
 global planting is open}.}                         \tag{7.10}
\]

That large-bank planting must also retain residence, the recursive MNW
terminal partition, and the lower/common-cap tickets; none follows from
the local collar algebra.
