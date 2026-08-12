# Fixed-H plus-collar planting in the Middle Levels factor, and the exact rooted-host residue

Date: 2026-08-01  
Lane: additive-constant regeneration / owner-q1 planting  
Status: unconditional q1 two-factor extension theorem; exact phase, upper-palette, residence, and topology scope recorded.  This does **not** prove a fully guarded Pascal child or `nu(k)=B(k)+O(1)`.

## 0. Outcome

Let `ML_m` be the containment graph between ranks `m-1` and `m` of
`[2m-1]`.  Each shore has

\[
                         W={2m-1\choose m}
\]

vertices and the graph is `m`-regular.

The following extension statement is unconditional.

> **Small protected-factor theorem.**  Every subgraph `P` of `ML_m` with
> maximum degree at most two and
> \[
>                              |E(P)|\le m-2                 \tag{0.1}
> \]
> is contained in a spanning two-factor of `ML_m`.

Consequently, for each fixed `H`, any `H` pairwise vertex-disjoint
**plus-phase** terminal collar paths whose total incidence-edge length is
`O(Hd)` can be planted simultaneously in an exact owner/q1 factor once

\[
                              O(Hd)\le m-2.                  \tag{0.2}
\]

Since the OR-word depth is `d=Theta(sqrt(m))`, (0.2) holds in all sufficiently
large dimensions.  This removes the abstract owner-degree and q1-injection
part of the fixed-`H` host hypothesis: no positive-density centre menu is
needed merely to extend a bounded bank of already specified alternating
paths to a q1-rainbow factor.

The theorem embeds the **selected terminal plus phase only**.  It does not
put the old-minus and plus realizations of a ternary packet into the same
factor.  Normally their union has degree four at switched vertices and
cannot be a subgraph of any two-factor.  Old-minus and plus are alternative
states of a dynamic packet, not simultaneous static obligations.  They may
both be prescribed only when their union is itself 2-bounded and still
satisfies (0.1).

Three gates remain and are not semantic qualifications:

1. the completion is an arbitrary two-factor, with as many as `W/3`
   components, not a Hamilton factor or an `O(H)`-component factor;
2. ordinary Ore--Ryser completion does not enforce the adjacent-upper union
   palette; an explicit `ML_4` factor misses one upper colour;
3. residence outside the protected collars, arbitrary-width upper witnesses
   outside them, and the common cap are not imposed.

Thus the result is a genuine planting theorem for the q1 skeleton, and it
pinpoints the remaining statement as a **rooted, upper-decorated,
state-filtered completion theorem**, rather than a factor-existence theorem.

## 1. The middle-shadow surplus

Write

\[
 {cal L}={ [2m-1]\choose m-1},\qquad
 {cal U}={ [2m-1]\choose m}.
\]

For `A subset L`, let `N(A) subset U` be its upper shadow and put

\[
 a=|A|,\qquad c=W-a,\qquad g=|N(A)|-|A|.                   \tag{1.1}
\]

### Lemma 1.1 (sharp coarse middle-shadow surplus)

For every nonempty `A subseteq L`,

\[
                         g\ge \min\{m-1,c\}.               \tag{1.2}
\]

#### Proof

Complementation sends `A` to an `a`-member family of `m`-sets and sends
`N(A)` to its lower shadow.  By Kruskal--Katona, its shadow is at least the
shadow `K_m(a)` of the first `a` `m`-sets in colex order.

We prove the required arithmetic form rather than invoking it as an
unstated corollary.  Write `partial_k(t)` for the Kruskal--Katona numerical
lower-shadow function.

First note the following auxiliary bound:

\[
 1\le t\le {2k-2\choose k}
 \quad\Longrightarrow\quad
 \partial_k(t)-t\ge k-1.                              \tag{1.3}
\]

Indeed, if `t=binom(2k-2,k)`, this follows from

\[
 {2k-2\choose k-1}-{2k-2\choose k}\ge k-1.            \tag{1.4}
\]

Otherwise write the first step of the canonical binomial expansion as

\[
 t={x\choose k}+b,qquad
 k\le x\le2k-3,qquad 0\le b<{x\choose k-1}.          \tag{1.5}
\]

The remainder expansion has top index at most `x-1<=2k-4`.  Its colex
family of `(k-1)`-sets is therefore supported on at most `2k-3` points.
On those points ranks `k-1` and `k-2` have equal size, and direct incidence
double counting gives

\[
                         \partial_{k-1}(b)\ge b.       \tag{1.6}
\]

The Kruskal--Katona formula now gives

\[
 \partial_k(t)-t
 =\left[{x\choose k-1}-{x\choose k}\right]
   +\left[\partial_{k-1}(b)-b\right].                 \tag{1.7}
\]

Put `D_x=binom(x,k-1)-binom(x,k)`.  We have `D_k=k-1`, and

\[
 D_{x+1}-D_x={x\choose k-2}-{x\choose k-1}\ge0
 \qquad(k\le x\le2k-3).                               \tag{1.8}
\]

Thus (1.3) follows from (1.6)--(1.8); equation (1.4) is the endpoint of the
same monotonicity calculation.

Return to `k=m`.  Put

\[
 A_0={2m-2\choose m},qquad
 K={2m-2\choose m-1},qquad W=A_0+K,qquad c=W-a.
\]

If `a<=A_0`, (1.3) immediately gives `K_m(a)-a>=m-1`.

Suppose `a>A_0`, and write `a=A_0+b`, so `b=K-c`.  The colex recursion is

\[
                         K_m(a)=K+\partial_{m-1}(b). \tag{1.9}
\]

View the first `b` rank-`(m-1)` sets on `[2m-2]` as a family `F`, and let
`Q` be the rank-`(m-2)` sets missing from its lower shadow.  Every upper
neighbour of `Q` lies in the `c`-member complement of `F`.  Complementing
`Q` inside `[2m-2]` gives a family of rank-`m` sets.  Apply (1.3) with
`k=m` to this complemented family: its lower shadow is the complement of
the upper shadow of `Q`, and hence

\[
             |\nabla Q|\ge |Q|+m-1.                  \tag{1.10}
\]

Since `nabla Q` lies in a `c`-set family,

\[
                         |Q|\le\max\{0,c-(m-1)\}.    \tag{1.11}
\]

Finally, using
`K-A_0=binom(2m-2,m-1)-binom(2m-2,m)`, (1.9) simplifies exactly to

\[
 K_m(a)-a=c-|Q|.
\]

Equations (1.10)--(1.11) therefore give

\[
 K_m(a)-a\ge \min\left\{m-1,{2m-1\choose m}-a\right\}.     \tag{1.12}
\]

This proves (1.2).  \(\square\)

The scalar statement (1.12), including every equality transition, is replayed
from the binomial expansion for `2<=m<=12` by the audit.

Define the truncated two-shadow

\[
 S_2(A)=\sum_{U\in{cal U}}\min\{2,d_A(U)\},\qquad
 d_A(U)=|\{L\in A:L\subset U\}|.                           \tag{1.4}
\]

### Lemma 1.2 (the exact capacity-two margin)

For every nonempty `A subseteq L`,

\[
 S_2(A)-2|A|\ge \min\{m-2,2c\}.                           \tag{1.5}
\]

#### Proof

First suppose `g>=m-1`.  For `1<=j<=m`,

\[
                 \min\{2,j\}\ge1+{j-1\over m-1}.          \tag{1.6}
\]

Also `sum_U d_A(U)=ma`.  Summing (1.6) over `N(A)` gives

\[
\begin{aligned}
 S_2(A)
 &\ge |N(A)|+{ma-|N(A)|\over m-1},\\
 S_2(A)-2a
 &\ge {m-2\over m-1}g\ge m-2.                             \tag{1.7}
\end{aligned}
\]

Now suppose `g<m-1`.  Lemma 1.1 forces `c<m-1` and `g=c`, hence
`N(A)=U`.  Every `U` has at most `c` lower neighbours outside `A`, so

\[
                         d_A(U)\ge m-c\ge2.
\]

Therefore `S_2(A)=2W` and

\[
                         S_2(A)-2a=2c.                     \tag{1.8}
\]

Equations (1.7)--(1.8) prove (1.5).  \(\square\)

The two terms in (1.5) are exactly the two resources used below: the global
middle-shadow margin `m-2` and the `2c` protected-edge capacity in the
complement of `A`.

## 2. Extending a protected bank to a two-factor

### Theorem 2.1 (small protected-factor theorem)

Let `P subseteq ML_m` satisfy

\[
                     \Delta(P)\le2,\qquad |E(P)|\le m-2.  \tag{2.1}
\]

Then `ML_m` has a spanning two-factor containing every edge of `P`.

#### Proof

Suppose not, and choose an edge-minimal subgraph `H subseteq P` which is not
extendable.  Put

\[
 b(v)=2-d_H(v),\qquad G_0=ML_m-E(H).                        \tag{2.2}
\]

Completing `H` to a two-factor is exactly the bipartite `b`-factor problem
in `G_0`.  Ore--Ryser therefore supplies `A subseteq L` such that

\[
 \sum_{x\in A}b(x)>
 \sum_{U\in{cal U}}\min\{b(U),d_{G_0}(U,A)\}.             \tag{2.3}
\]

No edge of `H` is incident with `A`.  Indeed, if `e=xU in E(H)` with
`x in A`, delete `e` from `H`.  On the left of (2.3), `b(x)` rises by one.
On the right, restoring `e` and raising `b(U)` can increase the one term
`min(b(U),d(U,A))` by at most one.  The strict integer violation survives,
contradicting edge-minimality.

Consequently

\[
 b(A)=2|A|,\qquad d_{G_0}(U,A)=d_A(U).                     \tag{2.4}
\]

For every `U`,

\[
 \min\{2-d_H(U),d_A(U)\}
       \ge \min\{2,d_A(U)\}-d_H(U).                        \tag{2.5}
\]

Writing `h=|E(H)|` and summing (2.5), the right side of (2.3) is at least
`S_2(A)-h`.  Thus (2.3) implies

\[
                         h>S_2(A)-2|A|.                    \tag{2.6}
\]

Every lower endpoint of `H` lies in `L\A`, which has size `c`, and its
degree in `H` is at most two.  Hence

\[
                         h\le2c.                           \tag{2.7}
\]

Also `h<=|E(P)|<=m-2`.  Lemma 1.2 and (2.7) give

\[
 h\le\min\{m-2,2c\}
   \le S_2(A)-2|A|,
\]

contradicting (2.6).  \(\square\)

This proof is not a density heuristic.  It checks every Ore--Ryser cut, and
the strict inequality in (2.6) is why the endpoint `m-2` is included.

### Corollary 2.2 (fixed-H plus-phase collar planting)

Fix `H`.  For task `j`, let `P_j` be the incidence lift of its selected
terminal plus-phase owner path together with every `d`-scale boundary edge
which must be literally retained.  Assume the `P_j` are vertex-disjoint
alternating paths and put

\[
                          h=\sum_j |E(P_j)|.                \tag{2.8}
\]

If `h<=m-2`, there is a q1-rainbow spanning owner two-factor containing all
the `P_j`.

In particular, if every protected packet/collar has at most `C d+C` lifted
incidences, then all `H` collars embed whenever

\[
                         H(Cd+C)\le m-2.                   \tag{2.9}
\]

For fixed `H,C` and `d=Theta(sqrt(m))`, (2.9) holds eventually.

#### Scope of preservation

Any adjacent-upper witness represented by an edge wholly inside a protected
path survives.  Any longer OR witness whose complete owner interval lies
inside such a path also survives as a literal consecutive subpath (possibly
with the global cycle orientation reversed).  Residence assertions whose
entire run and both boundary states lie inside the protected collar are
likewise retained.

This is **not** a proof of global residence or global upper completeness.
The unprotected factor edges and the joins at collar endpoints are selected
only by the `b`-factor theorem.  They may create short runs elsewhere or
fail to provide unprotected upper targets.

## 3. Why ordinary Ore--Ryser does not also solve the upper palette

At a lower vertex `L`, a two-factor chooses two owners

\[
                    L\cup\{a\},\quad L\cup\{b\}.
\]

Their adjacent-upper colour is the **paired** value

\[
                         L\cup\{a,b\}.                     \tag{3.1}
\]

There are `W` such occurrences but only

\[
 {2m-1\choose m+1}={m-1\over m+1}W<W                     \tag{3.1a}
\]

rank-`m+1` colours.  Hence literal upper-palette **injectivity is
arithmetically impossible** on this odd host.  The correct row is
surjectivity, with exactly `2W/(m+1)` unavoidable excess occurrences (and,
in stronger constructions, a controlled excess design).

Ore--Ryser sees the two incidences separately.  It has no row for their
pairing.  The exact augmented variables would be

\[
 x_{L,\{a,b\}}\in\{0,1\},                                 \tag{3.2}
\]

with one chosen pair at each `L`, owner degree two at every middle owner,
and the covering inequalities

\[
 \sum_{L,\{a,b\}:L\cup\{a,b\}=R}x_{L,\{a,b\}}\ge1
 \quad(R\in{[2m-1]\choose m+1}).                          \tag{3.3}
\]

This is a correlated three-resource integer system, not a bipartite
`b`-factor.

The separation is literal already at `m=4`.  Order the 35 rank-three masks
of `[7]` lexicographically.  The following two perfect matchings, listed by
their rank-four owner masks in that order, are edge-disjoint:

```text
M1 = 71,75,23,51,99,45,85,53,77,27,43,89,57,83,105,15,30,39,
     102,58,46,90,54,114,106,29,60,78,116,86,101,120,92,108,113

M2 = 23,15,83,43,75,77,29,39,71,57,45,105,53,113,101,46,54,102,
     86,27,106,78,51,90,99,30,108,92,60,85,116,58,89,120,114
```

Their union is a spanning q1 two-factor, of incidence component sizes `10`
and `60`, but its paired unions cover only 20 of the 21 rank-five masks.
The missing colour is

\[
                              91=\{0,1,3,4,6\}.             \tag{3.4}
\]

Thus an Ore--Ryser completion can be q1-exact and still fail the immediate
upper row.  The example does not prove that no *other* completion of the
same protected bank is upper-complete.  It proves the precise methodological
point: the ordinary cut theorem cannot enforce (3.3), so an upper-decorated
extension theorem remains necessary.

## 4. Component count and the rooted-host gate

Every component of a simple middle-level two-factor is an even cycle.  The
incidence graph has no four-cycle, so every component has at least six
vertices.  Since the factor spans `2W` vertices,

\[
                    c(F)\le\left\lfloor {W\over3}\right\rfloor.         \tag{4.1}
\]

This is the only component bound supplied by Theorem 2.1.  It is bulk-sized,
not `O(H)`.  Opening and concatenating such a factor can therefore cost
`Theta(W)` seams, which is useless for an additive-constant induction.

There is, however, an exact positive normal form which says what additional
certificate would give both the upper row and `O(H)` components.

### Theorem 4.1 (upper-decorated near-factor certificate)

Properly two-edge-colour the protected bank

\[
                         P=P_0\mathbin{\dot\cup}P_1,        \tag{4.2}
\]

which is possible because `P` is a maximum-degree-two bipartite graph.  Let
`M_0` be a perfect matching of `ML_m-P_1` containing `P_0`.

For an edge `e=LU` outside `M_0`, define

\[
 \operatorname{up}_{M_0}(e)=M_0(L)\cup U,\qquad
 \lambda_{M_0}(e)=\{L,M_0^{-1}(U)\}.                       \tag{4.3}
\]

The first is a rank-`m+1` colour.  The second is an **edge-labelled** link on
the lower shore: distinct incidence edges remain distinct link objects even
if their unordered endpoint sets agree.  Thus `Lambda(Q)` below is a
multigraph, and graphic independence forbids loops, parallel two-cycles and
ordinary cycles.  (In `ML_m`, an opposite pair of links would itself give an
incidence four-cycle, so it cannot actually occur; the labelled convention
keeps the rank argument valid without using that simplification.)

Suppose there is a matching `Q subseteq ML_m-M_0` such that

1. `P_1 subseteq Q`;
2. `|Q|=W-s`;
3. `up_{M_0}(Q)` covers every rank-`m+1` colour;
4. the `W-s` edge-labelled links
   `Lambda(Q)={lambda_{M_0}(e):e in Q}` are graphic-independent; and
5. after deleting the endpoints of `Q`, the remaining bipartite graph
   `ML_m-M_0` has a perfect matching.

Then `P` extends to an upper-surjective q1 two-factor with at most `s`
components.

#### Proof

Let `R` be the residual perfect matching in condition 5 and put

\[
                            M_1=Q\cup R.                    \tag{4.4}
\]

Then `M_0,M_1` are edge-disjoint perfect matchings and contain `P_0,P_1`,
respectively.  Their union is a q1 two-factor containing `P`.  Condition 3
is precisely its adjacent-upper surjectivity.

The union of two perfect matchings is encoded by the permutation

\[
                    \pi=M_0^{-1}\circ M_1\quad\text{on }L. \tag{4.5}
\]

Its permutation cycles are exactly the factor components.  Equivalently,
if `Gamma(M_1)` is the undirected graph with edges
`lambda_{M_0}(e)`, then

\[
            c(M_0\cup M_1)=W-r_{\rm gr}(\Gamma(M_1)).       \tag{4.6}
\]

Because the `W-s` labelled edges of `Lambda(Q)` are graphic-independent,
its graphic rank is
`W-s`.  Graphic rank is monotone when the residual edges are added, so
(4.6) gives `c<=s`.  \(\square\)

Condition 5 is once again an ordinary Hall condition, now on only `s`
vertices per shore.  Thus Theorem 4.1 isolates the genuinely correlated
part in a near-perfect matching `Q`; the last completion is not a new
common-cap problem.

There is also an exact converse with the familiar safe-cut qualification.
Let `F=M_0 union M_1` be an upper-surjective factor with `c` components.
If one can choose one `M_1` edge from each component, avoiding `P_1`, such
that deleting all `c` chosen occurrences leaves every upper colour still
witnessed, then the remaining set

\[
                         Q=M_1\setminus D                  \tag{4.7}
\]

satisfies Theorem 4.1 with `s=c`: deleting one permutation edge from each
cycle makes `Lambda(Q)` a forest, and the removed edges themselves are the
residual perfect matching.  Hence the extra hypothesis can be stated
equivalently as an **upper-transparent cut in every component**.

For fixed `H`, a certificate with `s=O(H)` would close precisely the owner,
q1, immediate-upper, and seam-count rows.  Theorem 2.1 alone constructs no
such `Q`.

### Corollary 4.2 (bounded-damage version for the additive conjecture)

In Theorem 4.1, weaken condition 3 by allowing `t` rank-`m+1` colours to be
absent from `up_{M_0}(Q union R)`.  Then the resulting factor has at most
`s` components and at most `t` immediate-upper holes.  Opening one edge in
each component can destroy at most `s` further upper colours.  Therefore a
certificate with

\[
                              s+t=O(H)                      \tag{4.8a}
\]

is already sufficient for an additive-constant terminal construction: the
bounded eviction/append step pays those named colours once.

Conversely, no upper-transparent safe-cut hypothesis is needed merely to
obtain bounded damage.  From any upper-surjective `c`-component factor,
delete one unprotected edge per component.  The resulting path forest loses
at most `c` upper witnesses.  Thus the exact upper-transparent converse
above is the coefficient-one version; the `O(1)` programme needs only
bounded components and bounded named damage.

One cannot silently replace Theorem 2.1 by a Hamilton extension claim.  The
authenticated `J(5,3)` four-edge protected cut in
`MATH_THEOREM_O1_PROTECTED_Q1_HAMILTON_EXTENSION_CUT_20260801.md` has
pairwise-distinct owners, lower colours and upper colours, belongs to a
q1-rainbow factor, and belongs to no q1-rainbow Hamilton factor.  Its size
four lies outside the asymptotic range `h<=m-2` at `m=3`, so it does not
refute a large-dimension theorem.  It does refute the inference

\[
                  \text{factor extension}\Longrightarrow
                  \text{rooted Hamilton extension}.       \tag{4.8}
\]

The exact missing owner-layer statement is therefore:

> **Upper-decorated bounded-component extension gate.**  Given the selected
> `H` plus-phase collar paths (with their endpoint states and named upper
> witnesses), find a spanning q1 factor containing them, satisfying (3.3),
> and having `O(H)` components; preferably find one rooted Hamilton cycle.

Even the unprotected `H=0`/one-component face asks for one middle-levels
Hamilton projection whose lower intersections are exact and whose paired
upper unions are surjective: the doubly-rainbow Hamilton object isolated
earlier in the programme.  Thus the remaining gate contains a known central
open construction already before residence or common-cap guards are added.

If this gate holds, only `O(H)` seams remain, and the existing common-cap and
protected-witness machinery can price them at additive `O(H)`.  Theorem 2.1
proves the unadorned factor part of this statement and no more.

## 5. Relation to old-minus packet states

For clarity, the static and dynamic quantifiers are:

* `P^+` is the incidence path bank required in the terminal child.  This is
  what Corollary 2.2 embeds.
* `P^-` is the old packet state before the ternary/C6 exchange.  It need not
  be present in the terminal factor.
* A serial packet proof may move through `P^-`, toggle a balanced circuit,
  and finish at `P^+`, returning all old resources dynamically.
* Requiring `P^- union P^+` in one static factor is a different assertion.
  Theorem 2.1 applies only if this union is 2-bounded and has at most `m-2`
  incidence edges.  Most nontrivial switches fail the degree condition.

This distinction prevents a false doubling of the collar bank and says
exactly which phase has now been planted.

## 6. What is proved and what remains

The fixed-`H` owner/q1 situation is now split cleanly.

### Proved

1. Every 2-bounded protected incidence bank of size at most `m-2` extends to
   an exact q1 two-factor.
2. Therefore any fixed number of `d=Theta(sqrt(m))` plus-phase protected
   collar paths embeds for all sufficiently large `m`.
3. Every named local witness and every fully contained residence run in
   those paths is retained literally.

### Not proved

1. adjacent-upper completion (the paired constraints (3.3));
2. `O(H)` component count or rooted Hamilton completion;
3. global residence and all-width upper coverage on the unprotected bulk;
4. a feasible integral common cap after the bulk completion.

So the requested unconditional theorem with all four guards is not yet
available.  The strongest correct replacement is the q1 two-factor theorem
plus the upper-decorated bounded-component gate above.

### 6.1 Exact interface with the Regenerative pull--cell lemma

The corrected pull--cell reduction in
`MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md`
asks, in the terminal plus phase, for one literal task cell per packet and a
complete damage set meeting only `O(1)` cells of a reference compiler
matching.  It does **not** require the terminal compiler to be common to the
minus phase.

Corollary 2.2 supplies exactly one previously conditional row of that
reduction:

\[
 \boxed{\text{fixed terminal plus collars}
        \Longrightarrow\text{one exact owner/q1 two-factor containing them}.}
                                                               \tag{6.1}
\]

It therefore eliminates a separate q1 collision or owner-degree loss from
the pull--cell damage ledger.  A task cell and every immediate witness lying
inside its protected collar survive the completion literally.

It does **not** supply the pull--cell ticket itself.  In the notation of the
bounded-eviction theorem, Theorem 2.1 proves neither

\[
                         \tau_i-b_i\in E(H_{\rm final})       \tag{6.2}
\]

for a chosen compiler cell nor the bound

\[
                 \left|D\cap C(M_0)\right|=O(1).             \tag{6.3}
\]

Nor does it ensure that the arbitrary factor completion has the bounded
topology and unprotected upper witnesses needed to define the final physical
word.  Thus the implication chain is now

\[
\begin{array}{c}
\text{selected, cap-certified plus packets}\cr
\Downarrow\quad\text{(this theorem, if total lifted size }\le m-2)\cr
\text{exact q1 two-factor containing the packet paths}\cr
\Downarrow\quad\text{(still open)}\cr
\text{upper-decorated }O(H)\text{-component host}\cr
\Downarrow\quad\text{(still open)}\cr
\text{literal pull cells with bounded complete damage.}
\end{array}                                                   \tag{6.4}
\]

Phase decoupling is essential in (6.4): applying Theorem 2.1 to
`P^- union P^+` would usually violate degree two and would reintroduce a
false simultaneous-state requirement that the regenerative lemma explicitly
removed.

## 7. Audit

Run

```text
python3 scratch/audit_fixed_h_collar_q1_two_factor_20260801.py
```

The dependency-free replay checks:

* the Kruskal--Katona scalar surplus for every size through `m=12`;
* the truncated two-shadow inequality over every nontrivial shore subset at
  `m=3`;
* every protected family of size at most `m-2` at `m=3,4` by an independent
  max-flow `b`-factor replay;
* the explicit `ML(7)` upper-palette counterexample and its component profile.

Canonical audit payload SHA-256:

```text
523d74d1b50a7ea34367382f6a9dcd9e8a8cbc67794bba364b7b66551dc78c10
```

Dependencies used at exact scope:

* Kruskal--Katona for Lemma 1.1;
* Ore--Ryser's bipartite `b`-factor criterion for Theorem 2.1;
* `MATH_THEOREM_O1_PROTECTED_Q1_HAMILTON_EXTENSION_CUT_20260801.md` only
  for the finite rooted-Hamilton warning.
