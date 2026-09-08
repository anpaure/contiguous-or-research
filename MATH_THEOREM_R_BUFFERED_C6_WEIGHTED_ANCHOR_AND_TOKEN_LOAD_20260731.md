# Buffered C6 packets: exact weighted anchor loads and a private-anchor counterexample

Date: 2026-07-31  
Lane: R, independent resource-load audit  
Status: exact counting theorem, exact Hall/Rado reduction, and a
dimension-uniform counterexample to the claim that bounded task congestion
or pairwise-disjoint source incidences alone imply `O(m)` global token load.
No packet-abundance or all-`k` upper theorem is claimed.

## 0. Verdict

The source-incidence C6 catalogue has three different load scales.  For a
fixed source incidence, a token can occur in exactly `m^2`, `m`, or `1`
candidate circuits, according to its role.  Consequently a restricted
anchor family has the exact weighted load

\[
                         m^2N_0(r)+mN_1(r)+N_2(r).       \tag{0.1}
\]

Here `N_j(r)` counts assigned anchors at which the token `r` occurs in a
role with `j` free C6 coordinates suppressed: source-fixed, one-free, or
zero-free respectively.

This has three immediate consequences.

1. If two distinct task lists of quadratic size use the same source
   incidence, their common fixed source token already has quadratic
   cross-list load.  Thus strict token-disjoint composition requires an
   **injective**, not merely `O(1)`-congested, task-to-anchor assignment.
2. Even pairwise endpoint-disjoint source incidences do not suffice.  There
   is an explicit family of `m` such anchors and a rank-`(m+1)` owner token
   which occurs in `m` choices from every list, hence has cross-list load
   `m(m-1)`.
3. `O(m)` load follows from the stronger weighted-code conditions: fixed
   source tokens are private against every other list, every token is in a
   one-free role at `O(1)` anchors, and in a zero-free role at `O(m)`
   anchors.  The same conditions must be proved separately for physical,
   colour, and cap-ticket tokens.  Local C6 geometry gives no cap-ticket
   dispersion theorem.

The all-incidence atlas is much worse: its exact incidence-token load is
`6m^2`, while either vertex-shore load is `3(m+1)m^2`.  This independently
checks the full-atlas calculation in the buffered-hexagon reduction.

## 1. The exact source-incidence catalogue

Let `Omega` have size `2m+1`.  A directed source incidence is

\[
             e=(C,U),\qquad |C|=m,\qquad U=C+a.          \tag{1.1}
\]

For `b in C` and `c notin U`, the associated incidence C6 is

\[
 C, U, U-b, U-b+c, C-b+c, C+c.                    \tag{1.2}
\]

There are exactly `m^2` labelled candidates through `e`.  Its six incidence
edges, in cyclic order, are

\[
\begin{array}{lll}
 E_0=(C,U),&E_1=(U-b,U),&E_2=(U-b,U-b+c),\\
 E_3=(C-b+c,U-b+c),&E_4=(C-b+c,C+c),&E_5=(C,C+c).
\end{array}                                             \tag{1.3}
\]

All edges are read as rank-`m`--rank-`(m+1)` incidences.  A whole C6 switch
touches the three rank-`m` vertices, the three rank-`(m+1)` vertices, and all
six displayed incidences.  Adding protected collars or cap paths can only
increase this support.

### Lemma 1.1 (exact role multiplicities at one anchor)

For fixed `e=(C,U)`, the number of labelled candidates containing a fixed
token in each role is:

\[
\begin{array}{c|c|c}
\text{token type}&\text{role}&\text{multiplicity}\\ \hline
\text{rank }m&C&m^2\\
              &U-b&m\\
              &C-b+c&1\\ \hline
\text{rank }m+1&U&m^2\\
                &U-b+c&1\\
                &C+c&m\\ \hline
\text{incidence}&E_0&m^2\\
                 &E_1&m\\
                 &E_2,E_3,E_4&1\\
                 &E_5&m
\end{array}                                             \tag{1.4}
\]

The roles in any one row-rank are disjoint.

#### Proof

The source tokens `C,U,E_0` are independent of `(b,c)`.  In `U-b`, `E_1`,
`C+c`, and `E_5`, one parameter is determined and the other is free, giving
`m`.  Every remaining displayed token determines both `b` and `c`, giving
one.  A source role cannot equal a nonsource role because `b in C` and
`c notin U`; similarly, a one-free role cannot equal a zero-free role of
the same rank.  This proves the table.  QED.

### Lemma 1.2 (exact suspended gain-one token inventory)

The correlated gain-one packet has the same three-scale phenomenon.  Use
the notation of the suspended-hex theorem.  Write its designated target as

\[
 A=(D,V;(D+p,i),(D+q,j)),\qquad V=D+p+q,\qquad |D|=n,
                                                               \tag{1.5}
\]

and index its `2n(n-2)` formal packets by

\[
 b\in D,\qquad c\notin V,qquad (a,s)=(p,q)\text{ or }(q,p).
                                                               \tag{1.6}
\]

Ignoring the displayed literal-slot indices only in the notation, the
complete old/new support is

\[
\begin{array}{c|c}
\text{type}&\text{tokens}\\ \hline
\text{lower}&D,\ D-b+a,\ D-b+c\\
\text{upper}&V,\ V-b+c,\ D+c+s\\
\text{owner slots}&D+p,\ D+q,\ V-b,\ D+c,\
                   D-b+p+c,\ D-b+q+c.
\end{array}                                                   \tag{1.7}
\]

For one fixed target list their exact multiplicities are

\[
\begin{array}{c|c}
\text{token role}&\text{multiplicity}\\ \hline
D,V,D+p,D+q&2n(n-2)\\
D-b+p\text{ or }D-b+q&n-2\\
D-b+c&2\\
V-b+c&2\\
D+c+p\text{ or }D+c+q&n\\
V-b&2(n-2)\\
D+c&2n\\
D-b+p+c\text{ or }D-b+q+c&2.
\end{array}                                                   \tag{1.8}
\]

If a pointwise lower-to-upper cap pairing is tokenized, the complete packet
has the six semantic pair tokens

\[
\begin{array}{c|c}
\text{pair role}&\text{multiplicity}\\ \hline
(D,V)&2n(n-2)\\
(D-b+a,V-b+c)&1\\
(D-b+c,D+c+s)&1\\
(D-b+a,V)&n-2\\
(D,D+c+s)&n\\
(D-b+c,V-b+c)&2.
\end{array}                                                   \tag{1.9}
\]

#### Proof

Substitute `K=D-b` in the six lower/upper/owner formulas of the suspended
hex.  The target resources do not depend on any parameter.  A token
`D-b+p` fixes `b` and the orientation, leaving `c` free; `D+c+p` fixes `c`
and the orientation, leaving `b` free.  The tokens `D-b+c` and `V-b+c`
fix `(b,c)` but occur in both orientations.  The owner `V-b` fixes `b`,
while `D+c` fixes `c`; both are orientation-independent.  Finally each of
the two owners `D-b+p+c,D-b+q+c` occurs once in each orientation.  This
gives (1.8).  The old atoms are the first three appropriate pairings and
the new atoms the last three; the same parameter recovery gives (1.9).
QED.

In particular, even before a buffer or cap ticket is attached, every
candidate in one target list contains the same four target resources
`D,V` and the two prescribed target slots (counted as four typed resources,
with the slots occurrence-labelled).  Same-target task congestion therefore
has the same quadratic obstruction as Corollary 3.2.

## 2. Independent audit of the full-atlas loads

There are

\[
       I={2m+1\choose m}(m+1)                           \tag{2.1}
\]

directed incidences and `Im^2` labelled anchored candidates.  Every
geometric incidence C6 is anchored once at each of its six incidences.

### Theorem 2.1 (exact full-atlas load)

Every fixed incidence token occurs in exactly

\[
                              6m^2                       \tag{2.2}
\]

labelled candidates.  Every fixed rank-`m` vertex and every fixed
rank-`(m+1)` vertex occurs in exactly

\[
                            3(m+1)m^2                    \tag{2.3}
\]

labelled candidates.

Hence a candidate in the list anchored at `e=(C,U)` has, through `E_0`
alone, exactly `5m^2` candidates in other lists sharing a token.  Through
either fixed endpoint `C` or `U`, its cross-list token load is

\[
                  (3(m+1)-1)m^2=(3m+2)m^2.             \tag{2.4}
\]

#### Proof

Double-count candidate--incidence pairs.  There are `Im^2` anchored
candidates and six incidences per C6, and incidence transitivity makes the
load uniform, giving (2.2).  Each candidate has three vertices on each
shore.  Both shore sizes are `{2m+1 choose m}`.  Thus the uniform load is

\[
 {3Im^2\over {2m+1\choose m}}=3(m+1)m^2.
\]

Subtract the `m^2` candidates in the candidate's own list to obtain
(2.4); the incidence calculation is identical.  QED.

This is an obstruction to the unpruned full atlas, not to a carefully
selected and load-balanced subatlas.

## 3. Exact restricted-anchor formula

Let `A` be a family of source incidences.  Assign `q_e` task lists to
`e in A`, each using the complete local C6 catalogue.  For a vertex or
incidence token `r`, let

* `N_0(r)` be the sum of `q_e` over source-fixed occurrences of `r`;
* `N_1(r)` be the sum over the one-free roles in (1.4); and
* `N_2(r)` be the sum over the zero-free roles in (1.4).

### Theorem 3.1 (weighted token identity)

The total number of candidates in all assigned lists which contain `r` is
exactly

\[
                    \Lambda(r)=m^2N_0(r)+mN_1(r)+N_2(r). \tag{3.1}
\]

For a candidate `p in P_tau`, its cross-list load through `r` is (3.1)
minus the multiplicity of `r` in `P_tau`.

#### Proof

Sum the mutually exclusive role multiplicities in Lemma 1.1 over the
assigned anchor multiset.  Removing one task list gives the cross-list
formula.  QED.

### Corollary 3.2 (same-anchor congestion must be one)

Suppose every task list has size at least `alpha m^2`, and every packet in a
list contains its anchor incidence token.  If two tasks use the same anchor,
then every packet in either list has cross-list load at least
`alpha m^2` through that token.  Therefore a uniform `O(m)` token-load
theorem forces `q_e<=1` for all sufficiently large `m`.

Thus the first assignment problem is ordinary matching.  If `G=(T,A;E)` is
the actual task--eligible-anchor graph, an injective assignment exists if
and only if

\[
                         |N_G(X)|\ge |X|\qquad(X\subseteq T).    \tag{3.2}
\]

Allowing constant anchor capacity `K>1` and checking only
`|X|<=K|N(X)|` is insufficient for the strict token model.

### Theorem 3.3 (a sufficient weighted-code condition)

Assume one task per chosen anchor and the following conditions for every
1. If `r` is source-fixed at a chosen anchor, it occurs in no candidate
   list at any other chosen anchor.
2. Among chosen anchors, `r` occurs in one-free roles at at most `A`
   anchors.
3. Among chosen anchors, `r` occurs in zero-free roles at at most `Bm`
   anchors.

Then

\[
                         \lambda_\times(r)\le(A+B)m.             \tag{3.3}
\]

If a buffered packet contains at most `s_col,s_phy,s_cap` nonanchor tokens
of the three declared types and their corresponding constants in (3.3) are
`K_col,K_phy,K_cap`, then its cross-list conflict degree is at most

\[
 m\bigl(s_{col}K_{col}+s_{phy}K_{phy}+s_{cap}K_{cap}\bigr).     \tag{3.4}
\]

In particular, if the total support is at most `s_0d+s_1` and all three
typed loads have one common constant `K`, then

\[
                    \Delta\le K(s_0d+s_1)m=O(md).               \tag{3.5}
\]

#### Proof

Source privacy removes every `m^2` cross-list term.  Lemma 1.1 then bounds
the one-free contribution by `Am` and the zero-free contribution by `Bm`.
Summing the token-conflict neighborhoods of one packet proves (3.4)--(3.5).
QED.

For the bare suspended correlated hex, the complete resource support has
three lower colours, three upper colours, and six literal owner slots.  If
the pointwise cap pairing is also tokenized, its six old/new atom incidences
are an additional semantic token bank.  Thus the local core has respectively
`6`, `6`, and at most `6` tokens of the three types before protected
windows and full cap paths are attached.  The exact constants in (3.4)
apply type by type; calling the whole packet merely `O(d)` does not prove
any of the three `K` bounds.

### Corollary 3.4 (bounded reachable-task salvage)

Suppose the current regenerative state has at most `H` nonexceptional
tasks, with `H` independent of `m`.  Assign them injectively to anchors, and
assume every source-fixed physical/colour token is private against all other
assigned lists.  If every remaining physical or colour token occurs in at
most `kappa m` candidates of any one list, then its external load is at most

\[
                         (H-1)\kappa m.                         \tag{3.6}
\]

Consequently packets with at most `s_0d+s_1` such tokens have physical and
colour conflict degree at most

\[
             (H-1)\kappa m(s_0d+s_1)=O(md).                    \tag{3.7}
\]

#### Proof

Only the other `H-1` lists contribute to cross-load, and each contributes
at most `kappa m` occurrences of the token.  Sum over the token support of
one packet.  QED.

This is a genuine positive distinction.  For the source-incidence table,
all noncore roles have per-list multiplicity at most `m`, so `kappa=1`.
For the suspended gain-one table (1.8), the canonical owner-slot roles have
per-list multiplicity at most `2n`, so one may take `kappa=2` after
identifying `n` with the side parameter.  The local semantic cap-pair table
(1.9) has noncore multiplicity at most `n`, so it also obeys this bounded-
task salvage.  This statement concerns local pair tokens only, not the
complete alternating-path ticket needed by a global common-cap compiler.

The same conclusion does **not** follow for a cap/core token occurring in
every candidate of a list.  With list size `L=Theta(m^2)`, a token shared by
all candidates of each of `H` lists has external load
`(H-1)L=Theta(m^2)` even when `H=2`.  Thus bounded reachable-task count
closes the local physical/colour row after source privacy, but cap tickets
and any shared core/witness token still need their own privacy or
low-multiplicity theorem.

## 4. Pairwise-disjoint anchors still have quadratic load

### Proposition 4.1 (one-free owner-star obstruction)

For every `m>=2`, there are `m` source incidences with pairwise-distinct
lower endpoints and pairwise-distinct upper endpoints, one task per anchor,
such that one rank-`(m+1)` token has cross-list load `m(m-1)` for a packet
containing it.

#### Proof

Fix `W in {Omega choose m+1}`.  Choose distinct

\[
 c_1,\ldots,c_m\in W,qquad
 a_1,\ldots,a_m\in\Omega\setminus W.
\]

This is possible because `|W|=m+1` and `|Omega-W|=m`.  Put

\[
                    C_i=W-c_i,qquad U_i=C_i+a_i.                \tag{4.1}
\]

The `C_i` are distinct and the `U_i` are distinct, so the source incidences
`e_i=(C_i,U_i)` are endpoint-disjoint.  Also `c_i notin U_i`.  For every
`b in C_i`, the candidate `H(e_i;b,c_i)` has its last upper vertex

\[
                              C_i+c_i=W.                         \tag{4.2}
\]

Thus exactly `m` candidates in each of the `m` lists contain `W`.  A packet
in one list containing `W` meets `m` packets in each of the other `m-1`
lists, giving cross-list load `m(m-1)`.  QED.

The obstruction is the failure `N_1(W)=m`; source endpoint privacy controls
`N_0` but not `N_1`.  A pruning may delete these `m` candidates from each
quadratic list, so Proposition 4.1 does not rule out a deliberately
load-balanced positive-density subcatalogue.  It does rule out deriving
the load bound from pairwise-disjoint anchors alone.

### Corollary 4.2 (the unpruned owner star defeats both transversal bounds)

For the `m` lists in Proposition 4.1, put `L=m^2`.  Every displayed packet
containing `W` has conflict degree at least

\[
                              \Delta=m(m-1).                    \tag{4.3}
\]

Haxell's sufficient row `L>=2Delta` fails for every `m>=3`.  The symmetric
LLL row also fails already from this lower bound, because

\[
 e\,{2L\Delta+1\over L^2}
   =e\left(2{m-1\over m}+{1\over m^4}\right)>1
          \qquad(m\ge2).                                      \tag{4.4}
\]

This does not prove that the owner-star lists lack an independent
transversal: packets avoiding `W` remain.  It proves exactly that the two
black-box sufficient inequalities cannot be certified from the unpruned
lists and endpoint privacy.

## 5. Exact Hall/Rado scope of the anchor selection

The basic task-to-anchor matching is governed by (3.2).  The weighted-code
rows are additional selection constraints.  For one declared anchor subset
`S` with quota `h`, let `M_S` be the partition matroid on anchors with

\[
              r_{M_S}(Y)=|Y\setminus S|+min\{h,|Y\cap S|\}.    \tag{5.1}
\]

Rado's theorem gives an exact task-to-anchor assignment using at most `h`
members of `S` if and only if

\[
                         r_{M_S}(N_G(X))\ge|X|
                                \qquad(X\subseteq T).            \tag{5.2}
\]

Taking `S` to be the one-free neighborhood of one token gives the exact
single-token quota cut.  Simultaneous quotas for all physical, colour and
cap tokens are not represented by one such partition matroid unless the
quota family has additional laminar/matroidal structure.  The proof-safe
finite formulation is the binary system

\[
\begin{aligned}
 &\sum_{e\in N(\tau)}x_{\tau e}=1 &&(\tau\in T),\\
 &\sum_\tau x_{\tau e}\le1 &&(e\in A),\\
 &m^2N_0^x(r)+mN_1^x(r)+N_2^x(r)\le K_rm &&(r\text{ a token}),
\end{aligned}                                                   \tag{5.3}
\]

plus source privacy.  A violated Rado row (5.2) is a decisive cut for its
declared resource quota.  Passing all one-resource cuts separately is only
a relaxation of the common binary system (5.3).

## 6. Cap tickets are a separate global gate

The incidence C6 table controls only the local circuit.  A complete
common-cap ticket may traverse vertices and sink capacities arbitrarily far
from that circuit.  There is no implication from (1.4) to `O(m)` cap-token
load.

### Proposition 6.1 (cap cut-vertex obstruction)

Suppose two task sources can reach their permitted cap sinks only through
one cap-one vertex `z`.  Then the cap gammoid has

\[
                       r(\{\tau_1,\tau_2\})=1<2.                \tag{6.1}

\]

Hence no pair of vertex-disjoint complete tickets exists, even if the two
local C6 supports are resource-disjoint and each task has `Theta(m^2)`
formal local candidates.  If every candidate ticket in each list uses `z`,
then every packet has at least the full size of the other list as cross-list
cap load, namely `Omega(m^2)`.

#### Proof

Deleting `z` separates both sources from every permitted sink.  Menger's
theorem gives maximum vertex-disjoint linkage one, which is the gammoid rank
in (6.1).  The load assertion is immediate.  QED.

Thus cap-ticket existence requires the literal all-set Rado cuts

\[
                     r_{cap}\!\left(\bigcup_{\tau\in X}P_\tau\right)
                        \ge |X|\qquad(X\subseteq T),             \tag{6.2}

\]

and the Haxell route additionally needs a **menu-load** theorem: every cap
vertex and sink token occurs in at most `O(m)` options from all other lists.
Equation (6.2) certifies one linkage; it does not certify that the entire
candidate menu has low load.

## 7. Exact surviving theorem target

For the actual Pascal child, the bounded-load step separates into four
claims, none of which follows from the quadratic local C6 count.

1. Define the literal task--eligible-source graph after all protected
   witness, residence and boundary guards; prove the injective Hall rows
   (3.2), up to a bounded exceptional task set.
2. Select the matching so its source-fixed tokens are globally private and
   its one-free/zero-free anchor profiles satisfy Theorem 3.3.
3. Prove the same `O(m)` load independently for buffered witness tokens and
   for complete cap/topology tickets; the cap Rado cuts (6.2) are necessary.
4. Only then use the support bound `O(d)` to obtain `Delta=O(md)` and apply
   Haxell/LLL.

The full atlas and Proposition 4.1 are exact counterexamples to omitting
Step 2.  Proposition 6.1 is an exact counterexample to inferring Step 3 from
local geometry.  A positive theorem must therefore be a correlated
anchor-selection-and-routing result, not a consequence of bounded task
congestion alone.
