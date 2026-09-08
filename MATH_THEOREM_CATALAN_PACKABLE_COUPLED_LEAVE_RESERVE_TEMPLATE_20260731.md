# A packable coupled-leave reserve template at the Catalan critical scale

Date: 2026-07-31  
Status: exact conditional packing and absorption lemmas, an exact
fully-disjoint critical-scale no-go for universal leave pairs, and finite
audits; no variable-filler supply theorem and no all-dimensional Catalan
matching theorem are claimed

> **Supersession note (later 2026-07-31).**  The local variable-filler gap
> stated here has now been closed for every endpoint pair with
> `|L-U|>=3`: arbitrary prescribed start and end diamonds extend to one
> absorber.  See
> `MATH_THEOREM_CATALAN_INDEPENDENT_BOUNDARY_ABSORBER_20260731.md`.
> The global fully-disjoint budget and coupled-leave packing gates in this
> note remain valid.

## 0. Verdict

The single-pair Boolean absorber has a more rigid resource normal form than
is visible from its alternating outer path.  After a suitable tail/head
orientation, its off support is contained in its on support in each middle
role, and switching on adds exactly one head port above the lower endpoint
and one tail port below the upper endpoint.  In the currently proved
construction these two ports are coupled by one filler coordinate:

\[
                 (h,t)=(L+c,U-c),\qquad c\in U\setminus L.       \tag{0.1}
\]

Thus the present boundary menu is diagonal, not a Cartesian product.
At independent middle-pool density `Theta(1/m)`, this has vanishing local
availability.  A variable-filler construction would have to replace (0.1)
by a large product-like compatibility relation.

There is also a separate global constraint.  If the complete supports of
all stored absorbers are required to be pairwise resource-disjoint, a
reserve with `p` template edges which repairs a leave of size `r` must obey

\[
                              p\le K+r,                         \tag{0.2}
\]

where `K=Cat_m` is the number of unused resources in either middle role.
On banks of size `K`, a graph which matches *every* pair of `r`-subsets
needs at least `K(K-r+1)` edges.  For every proper leave `r<K`, this is
strictly larger than `K+r`.  Consequently neither a fixed nor a variable
filler can produce an arbitrary-cross-pair robust reserve under the strong
fully-disjoint storage semantics.

The weakest viable exact interface is instead a **coupled-leave template**:
a bounded-degree bipartite graph `P` is stored, and the bulk construction is
required to leave a pair `(S,T)` for which `P[S,T]` has a perfect matching.
The theorem below gives exact boundary-clone Hall conditions, a deterministic
core-menu packing condition, and the final switching implication.  These are
sufficiency conditions only.  Supplying the variable-filler catalogues,
forcing the bulk leave into the coupled family, and eliminating directed
physical cycles remain open.

## 1. Critical counts and the oriented absorber normal form

Put

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal X=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1}.
\]

Write

\[
 K=\operatorname{Cat}_m=\frac1{m+1}\binom{2m}m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 Q=|\mathcal X|=(m+1)K=N+K.                       \tag{1.1}
\]

The two middle roles are denoted by disjoint copies
`mathcal X_T,mathcal X_H`.  A complete ordered-diamond matching has `N`
atoms, uses `N` resources in each middle role, and leaves exactly `K` in
each role.

For `L in mathcal L` and `U in mathcal U`, use the notation of the
single-pair absorber.  Let

\[
 L=L_0,U_0,L_1,\ldots,U_{s-1},L_s,U
\]

be its alternating outer path, where

\[
 Z_i=L_i\cup L_{i+1},\qquad C_i=L_i+c,qquad
 D_s=L_s+d=U-c.                                    \tag{1.2}
\]

### Lemma 1.1 (oriented two-port normal form)

The absorber can be oriented so that

\[
\begin{array}{c|c|c}
 &T\text{-support}&H\text{-support}\\ \hline
 M^-&\{Z_i:0\le i<s\}&\{C_i:1\le i\le s\}\\
 M^+&\{Z_i:0\le i<s\}\cup\{D_s\}&
      \{C_i:0\le i\le s\}.
\end{array}                                                   \tag{1.3}
\]

In particular, the off support is contained in the on support in both
roles; the on state adds exactly

\[
             t=U-c\in\partial^-U,qquad
             h=L+c\in\partial^+L,                    \tag{1.4}
\]

where

\[
 \partial^+L=\{L+x:x\notin L\},\qquad
 \partial^-U=\{U-y:y\in U\}.
\]

Both boundary sets have order `m+1`.  If `s=|L-U|`, each role-support
union has exactly `s+1` resources.

#### Proof

Orient the atom `L_i U_i` in the on state as `Z_i -> C_i`, orient the
final atom `L_s U` as `D_s -> C_s`, and orient the atom `L_{i+1}U_i` in
the off state as `Z_i -> C_{i+1}`.  Every arrow is a Johnson edge with the
displayed lower intersection and upper union.  The distinctness proof in
the single-pair theorem applies separately to both roles.  Formula (1.3)
is now literal, and (1.4) follows from (1.2).  \(\square\)

As `c` ranges through `U-L`, the proved construction supplies exactly the
diagonal menu

\[
 B_{L,U}=\{(L+c,U-c):c\in U\setminus L\},qquad
 |B_{L,U}|=s+2\le m+1.                              \tag{1.5}
\]

Changing the order of the exchanged coordinates or the other held-out
coordinate changes the core schedule but not this coupling law.

## 2. Why a variable boundary filler is locally the right target

Take independent Bernoulli reserve pools in the two middle roles, each of
density `q`.  Ignoring core conflicts, the different pairs in (1.5) use
different variables in both pools.  Hence the exact probability that a
fixed endpoint pair has some available diagonal boundary pair is

\[
                 1-(1-q^2)^{s+2}\le(m+1)q^2.         \tag{2.1}
\]

For `q=C/m`, this is `O(C^2/m)`.

By contrast, suppose an absorber catalogue offered every pair in
`H_L times T_U`, where `H_L subset partial^+L` and
`T_U subset partial^-U`.  Its boundary availability probability would be

\[
 \bigl(1-(1-q)^{|H_L|}\bigr)
 \bigl(1-(1-q)^{|T_U|}\bigr).                       \tag{2.2}
\]

When both banks have order `m+1` and `q=C/m`, (2.2) tends to
`(1-e^{-C})^2`, a positive constant.  Thus product-like variable fillers
remove the *local* density bottleneck.  Nothing in this section proves
that such absorbers exist, that their cores pack, or that they evade the
global budget in Section 5.

## 3. Coupled-leave reserve templates

Let `P=(A,B;E)` be a simple bipartite graph with
`A subset mathcal L` and `B subset mathcal U`.  For `r>=0`, define its
accepted leave relation

\[
 \mathfrak F_r(P)=\{(S,T):S\subseteq A,\ T\subseteq B,
   |S|=|T|=r,\ P[S,T]\text{ has a perfect matching}\}.          \tag{3.1}
\]

For every `e=LU in E`, an absorber candidate consists of

1. internal outer supports `I_L(e),I_U(e)` of the same order `s_e`;
2. an off core with `s_e` tail resources and `s_e` head resources; and
3. one on-only boundary port `h_e in partial^+L` and one on-only boundary
   port `t_e in partial^-U`.

The internal supports are required to avoid the endpoint banks:
`I_L(e) cap A=emptyset` and `I_U(e) cap B=emptyset`.
The full support of a candidate is the union of its internal outer
supports, its off core, and its two boundary ports.  A family is **fully
support-disjoint** if internal lower supports, internal upper supports,
tail-role supports and head-role supports are pairwise disjoint in their
respective universes.  Endpoint vertices in `A union B` are not internal
resources.

### Theorem 3.1 (exact coupled-leave absorption)

Assume the following data.

1. Every edge of `P` has one chosen absorber candidate, and the chosen
   candidates are fully support-disjoint.
2. A bulk ordered-diamond matching `M_0` is disjoint from every full
   absorber support.
3. For some `(S,T) in mathfrak F_r(P)`, the union of `M_0` with every off
   state covers every outer vertex except exactly `S union T`.

Let `J` be any perfect matching of `P[S,T]`.  Replace the off state by the
on state precisely for the edges of `J`.  The resulting atoms cover both
outer palettes `mathcal L,mathcal U` perfectly and are injective in each
middle-role palette `mathcal X_T,mathcal X_H`.  Equivalently, they form an
ordered four-transversal.  If their
directed physical graph is additionally acyclic, its lift is a spanning
`K`-path forest.

#### Proof

Every off state covers exactly its internal outer vertices.  Switching an
edge `LU` on preserves that coverage and additionally covers `L` and `U`.
Because `J` is a matching, the switched endpoint vertices are exactly
`S union T`, once each.  Full support disjointness preserves tail and head
injectivity under any collection of switches, and the bulk was assumed
disjoint.  The outer palettes are now both perfect.  Their common order is
`N`, so exactly `N` tails and heads are used.  The final forest assertion
is Euler's identity on an acyclic directed graph with `Q` physical vertices
and `N=Q-K` edges.  \(\square\)

The acyclicity hypothesis is separate: local acyclicity of every absorber
does not exclude a directed cycle using several absorbers and bulk atoms.

## 4. Exact boundary-bank and core-packing gates

A variable-filler supply theorem must solve two different problems.  This
section gives exact conditional gates for them.

For each template edge `e=LU`, make one head clone and one tail clone.
The head clone has a list `H_e subset partial^+L`; the tail clone has a
list `T_e subset partial^-U`.  Let `C_H` and `C_T` be the two clone-to-port
bipartite graphs.  Write `B_e subseteq partial^+L times partial^-U` for
the boundary pairs actually realized by the local absorber catalogue.

### Lemma 4.1 (boundary-clone Hall)

There are globally injective choices

\[
                         h_e\in H_e\quad(e\in E)       \tag{4.1}
\]

if and only if, for every set `F subseteq E`,

\[
                         |F|\le\left|\bigcup_{e\in F}H_e\right|. \tag{4.2}
\]

The analogous condition with `T_e` is necessary and sufficient for
globally injective tail ports.  If all edges incident with `L` use a common
bank `H_L`, (4.2) is equivalently

\[
 \sum_{L\in S}d_P(L)\le\left|\bigcup_{L\in S}H_L\right|
                         \quad\text{for every }S\subseteq A,     \tag{4.3}
\]

and similarly on the upper shore.

#### Proof

This is Hall's theorem applied to the edge clones.  In the common-bank
case, clones with the same endpoint have identical neighbourhoods.  For a
fixed support `S`, the full collection of its clones is the strongest Hall
row; every subcollection has no larger demand and the same or a smaller
support set.  \(\square\)

Separate head and tail Hall conditions can be combined edge by edge only
when the local boundary compatibility relation contains the selected
product pairs.  A sufficient hypothesis is

\[
                         H_e\times T_e\subseteq B_e.    \tag{4.4}
\]

The diagonal menu (1.5) does not satisfy (4.4) except for singleton
subbanks.  Thus two marginal boundary matchings do not by themselves prove
a variable-filler absorber packing.

After boundary ports are fixed, let `mathcal C_e` be the menu of admissible
cores for edge `e`; all entries are already disjoint from the endpoint
banks, bulk support, and chosen boundary ports.  Two cores conflict when
they share an internal outer resource, a tail resource, or a head resource.

### Lemma 4.2 (ordered bounded-conflict core packing)

Suppose the template edges can be ordered `e_1,...,e_p` and there are
numbers `kappa_{ji}` such that any one core in `mathcal C_{e_j}` conflicts
with at most `kappa_{ji}` cores in `mathcal C_{e_i}`.  If

\[
             |\mathcal C_{e_i}|>
             \sum_{j<i}\kappa_{ji}\qquad(1\le i\le p),          \tag{4.5}
\]

then one can choose pairwise nonconflicting cores, one from every menu.

In particular, if conflicts occur only between neighbours of a dependency
graph of maximum earlier degree `delta`, any chosen core excludes at most
`kappa` entries of a neighbouring menu, and every menu has at least
`delta kappa+1` entries, then the cores pack.

#### Proof

Choose greedily in the displayed order.  Once cores have been chosen for
the first `i-1` edges, their union forbids at most the right side of (4.5)
entries of `mathcal C_{e_i}`.  At least one entry remains.  \(\square\)

Lemmas 4.1 and 4.2 deliberately separate boundary supply from core supply.
They are not estimates for the Boolean catalogue: an all-`m` proof must
actually construct product-compatible boundary banks and verify (4.5), or
replace it by a stronger packing argument.

Two useful numerical consequences make the bounded-degree and codegree
hypotheses explicit.  First, because every clone list is contained in a
boundary of order `m+1`, boundary Hall forces

\[
              d_P(L)\le m+1,\qquad d_P(U)\le m+1.      \tag{4.6}
\]

Second, suppose a core uses at most `w` typed resources, conflicts occur
only across a dependency graph of maximum earlier degree `delta`, and for
every resource `x` and every neighbouring menu `mathcal C_f`, at most
`lambda` members of `mathcal C_f` contain `x`.  Then a chosen core excludes
at most `w lambda` members of a neighbouring menu.  Hence the explicit
condition

\[
                  |\mathcal C_e|\ge
                  \delta w\lambda+1                 \tag{4.7}
\]

implies core packing by Lemma 4.2.  For the canonical length-`s_e` path,
the off core has `s_e` resources in each of the four typed classes
`I_L,I_U,X_T,X_H`, so one may take `w=4s_e<=4(m-1)`.  Neither a bounded
`delta` nor a useful `lambda` has yet been proved for a critical Boolean
catalogue.

## 5. The critical fully-disjoint redundancy tax

The next lemma is independent of the absorber length distribution.

Before using middle resources, full disjointness and avoidance of the
endpoint banks already impose the exact outer budget

\[
 S:=\sum_{e\in E(P)}s_e
       \le \min\{N-|A|,N-|B|\}.                     \tag{5.0}
\]

This is a necessary packing row, not a sufficient one.  At critical banks
`|A|=|B|=K`, it reads `S<=(m-1)K`.

### Lemma 5.1 (role-resource capacity)

In the setting of Theorem 3.1, let `p=|E(P)|` and let the bulk leave have
size `r` on each outer shore.  Then

\[
                              p\le K+r.                \tag{5.1}
\]

#### Proof

Let `S=sum_e s_e`.  All off states together contain `S` atoms.  Since the
bulk plus the off states leave `r` outer vertices on each shore, the bulk
contains `N-r-S` atoms.  Thus their baseline union uses `N-r` resources in
each middle role.  Lemma 1.1 shows that every one of the `p` fully stored
absorbers reserves one additional on-only resource in each role.  Full
support disjointness therefore requires

\[
                         N-r+p\le Q=N+K,
\]

which is (5.1).  \(\square\)

If `P` spans equal banks of order `b` and contains a perfect matching, write
`p=b+xi`.  Equation (5.1) says

\[
                         \xi\le K+r-b.                \tag{5.2}
\]

For the critical bank `b=K`, every routing edge beyond a fixed perfect
matching costs one unit of leave capacity: `xi<=r`.

### Lemma 5.2 (exact universal-leave Hall condition)

Let `P` have two shores of order `b`.  Every pair of `r`-subsets induces a
perfect matching if and only if

\[
 |N_P(X)|\ge b-r+|X|
       \quad\text{for every }X\text{ on the left with }1\le|X|\le r.
                                                               \tag{5.3}
\]

Consequently

\[
                    \delta(P)\ge b-r+1,qquad
                    |E(P)|\ge b(b-r+1).              \tag{5.4}
\]

#### Proof

Fix `X` with `|X|<=r`.  Among all right `r`-sets, the smallest possible
intersection with `N_P(X)` has order

\[
                       \max(0,|N_P(X)|-(b-r)).
\]

Hall's condition for every such right set is therefore exactly (5.3).
Applying this to every subset of an arbitrary left `r`-set proves
sufficiency; necessity follows by choosing the worst right set.  The
singleton rows give (5.4).  \(\square\)

### Theorem 5.3 (no proper universal leave on a fully-disjoint critical bank)

Suppose `|A|=|B|=K`, `1<=r<=K`, all stored absorber supports are fully disjoint, and
the template is required to absorb every pair of `r`-subsets.  Then

\[
                              r=K.                    \tag{5.5}
\]

In particular, no proper leave `r<K` has such a template.

#### Proof

Put `t=K-r`.  If `t>=1`, Lemmas 5.1 and 5.2 give

\[
          K(t+1)\le p\le K+r=2K-t.
\]

But

\[
          K(t+1)-(2K-t)=(t-1)K+t>0,
\]

a contradiction.  \(\square\)

This is a scoped no-go.  It does not exclude reserves whose unused boundary
ports are shared between mutually exclusive switches, dynamically exposed,
or regenerated after the actual leave is known.  It also does not exclude
a coupled-leave template.

### Corollary 5.4 (minimal critical template)

Let `pi:A->B` be a bijection on banks of order `b<=K`, and let `P` consist
only of the `b` edges `L pi(L)`.  Then

\[
 \mathfrak F_r(P)=\{(S,\pi(S)):S\subseteq A,\ |S|=r\}.           \tag{5.6}
\]

Thus, conditional on boundary and core packing plus a bulk leave of the
form `(S,pi(S))`, Theorem 3.1 absorbs the leave with degree one and the
minimum possible number of template edges.  This is an edge-minimal
fully-disjoint critical reserve interface; stronger accepted
leave relations require extra template edges.  It is a conditional
template, not a Boolean supply theorem.

## 6. Finite independent audit

The script

```text
scratch/audit_catalan_packable_reserve_template_20260731.py
```

independently performs the following checks.

1. For every endpoint pair and every diagonal filler through `m=5`, it
   reconstructs the oriented absorber, verifies every ordered diamond,
   role injectivity, physical distinctness within each state, support
   containment, and the two singleton differences in (1.4).
2. It confirms the exact diagonal boundary-menu size `s+2` for every pair.
3. It exhausts every equal-shore bipartite graph of order at most four and
   verifies that direct universal `r`-subset matchability is equivalent to
   (5.3).
4. It checks (1.1) and the first proper-leave contradiction
   `2K>2K-1` for `m=2,...,10`.

The resulting JSON is

```text
scratch/catalan_packable_reserve_template_20260731.audit.json
```

## 7. Exact remaining supply problem

The theorem reduces a fully-disjoint critical reserve proof to four named
and noninterchangeable obligations:

1. **boundary factorization:** construct banks whose compatibility contains
   the required products (4.4), or solve the coupled boundary selection
   directly;
2. **boundary Hall:** prove the clone conditions (4.2) in both roles;
3. **core packing:** construct sufficiently local core menus and verify
   (4.5), or replace it by an independently justified stronger theorem;
4. **coupled bulk leave:** force the almost-perfect bulk matching into
   `mathfrak F_r(P)` and then exclude or switch away directed physical
   cycles.

The later variable-filler exchange theorem
`MATH_THEOREM_H2_CATALAN_VARIABLE_FILLER_EXCHANGE_AND_CROSS_SEPARATED_BANK_20260731.md`
does solve the *local* product boundary row for nonincident endpoint pairs,
at the sharp cost of one transferred actuator.  It does not supply the
pairwise-disjoint internal cores required here, and its `(1,2)/(2,1)` role
tax must be included when instantiating the candidate semantics.  Theorem
5.3 also shows that asking for every cross-pair leave is too strong under
fully-disjoint storage.  No all-`m` Catalan Linear Matching, Regenerative
Shadow--Braid theorem, or contiguous-OR equality follows from this note.
