# `k=17`: the radius-three multicore causal-anchor meet and the ten-million obstruction

**Date:** 2026-08-02  
**Lane:** A, pure theorem / D prelaunch sieve  
**Status:** exact finite theorem and light read-only ledger arithmetic.  No SAT
instance is built or solved here.  The theorem gives a proof-complete stronger
sieve when complete occurrence-labelled core relations are supplied.  The
currently frozen marginal tables do not supply those relations and therefore
do not certify an output of at most `10,000,000` packets.

## 1. Declared face and formal dirty banks

Let `R` be the frozen catalogue of `N=16667` primitive one-for-one recuts.
Its immutable key is `(base,old_cut,new_cut)`.  Write `beta(g)` for the base
of `g`, and

\[
 \mathcal C_r=\{S\subseteq R:|S|=r,\ \beta\text{ is injective on }S\}.
                                                               \tag{1.1}
\]

For every \(T\in\mathcal C_0\cup\cdots\cup\mathcal C_3\), `B[T]` is the
**formal** final bank obtained by applying all members of `T` and rebuilding occurrences,
roles, colours, q1 atoms, capacities, guards and blockers directly from its
cut vector.  `B[T]` exists even when a zero-265 row of `T` is nonzero.  No
singleton or pair is discarded before its use in a three-recut truth table.

Let `L0` be a finite authenticated family of unconditional occurrence-
labelled q1 contradictions in \(B[\varnothing]\).  Treat two named traces or two
permitted embeddings as separate entries if either could survive after a
move.  For `K in L0`, let `D(K)` be its complete load-bearing dependency
cone: demanded rows, effective providers and complete footprints, occurrence
and role keys, capacities, conflicts, complements, guards and blockers.
Conditional successor cores are not members of `L0`; they remain a later
footprint-dependent filter.

For a datum `d in D(K)`, write `v_d(T)` for its full content-key value in
`B[T]`.  Equality here is literal occurrence-labelled equality, not equality
of a degree, owner mask or colour count.

## 2. Causal clutters and their exact meet

Define

\[
 \delta_K(T)={\bf1}\{\exists d\in D(K):v_d(T)\ne v_d(\varnothing)\}
                                                               \tag{2.1}
\]

and the support-three causal clutter

\[
 \mathcal A_3(K)=\min_{\subseteq}
 \{T\in\mathcal C_1\cup\mathcal C_2\cup\mathcal C_3:\delta_K(T)=1\}.
                                                               \tag{2.2}
\]

The minimum is by set containment.  Define the radius-three upward closure

\[
 \operatorname{Up}_3(\mathcal H)=
 \{S\in\mathcal C_1\cup\mathcal C_2\cup\mathcal C_3:
                  \exists A\in\mathcal H,\ A\subseteq S\}.       \tag{2.3}
\]

The **multicore meet clutter** is

\[
 \mathcal M=\min_{\subseteq}\left\{
     \bigcup_{K\in\mathcal L_0}A_K:
     A_K\in\mathcal A_3(K),\
     \bigcup_K A_K\in\mathcal C_1\cup\mathcal C_2\cup\mathcal C_3
                         \right\}.                            \tag{2.4}
\]

Repeated equal unions in (2.4) are one physical key.  A canonical provenance
record is the lexicographically least vector of per-core anchor keys whose
union is that key.

### Theorem 2.1 (complete multicore causal-anchor join)

The following identity holds exactly:

\[
 \bigcap_{K\in\mathcal L_0}\operatorname{Up}_3(\mathcal A_3(K))
                  =\operatorname{Up}_3(\mathcal M).              \tag{2.5}
\]

Every support-three bank not rejected by an unchanged trace from `L0` lies
in the support-three part of (2.5).  Hence enumerating the shadow of `M` is
a proof-complete prefilter for all unconditional cores.  It can contain
false promotions, because changing one datum need not destroy every
transported copy of a core, but it has no false omission.

#### Proof

If `S` is in the left side, choose for every `K` an anchor `A_K` contained
in `S`.
Their union `U` is compatible, has size at most three, and is contained in
`S`.  Some inclusion-minimal union from (2.4) is contained in `U`, so `S`
belongs to the right side.  Conversely, a union in (2.4) contains an anchor
of every core.  Every support containing it belongs to every upward closure,
proving (2.5).

If the named trace of `K` does not persist in `B[S]`, then
`delta_K(S)=1`.  Among subsets of `S` with value one choose an inclusion-
minimal subset; it belongs to `A_3(K)`.  Thus a packet escaping every
unchanged trace lies in every upward closure, and then in (2.5).  This uses
the final value on `S`; no monotonicity of datum changes is assumed.
\(\square\)

The meet can be built incrementally without a Cartesian product over all
cores.  Starting with `M^(1)=A_3(K_1)`, set

\[
 \mathcal M^{(j+1)}=\min_{\subseteq}\{A\cup B:
 A\in\mathcal M^{(j)},\ B\in\mathcal A_3(K_{j+1}),\
 A\cup B\in\mathcal C_{\le3}\}.                             \tag{2.6}
\]

Induction using (2.5) proves that the last clutter is `M`.

### Corollary 2.2 (contextual singleton and pair cores)

Let \(C\in\mathcal C_c\), \(c<3\), and let `K` be an unconditional
contradiction in the fixed context `B[C]`.  Replace `B[T]` in (2.1) by
\(B[C\cup T]\), replace the
root value by `B[C]`, and restrict to compatible completions of size at most
`3-c`.  Theorem 2.1 holds verbatim in that rooted context.

In particular:

* a core of a clean singleton `B[{a}]` requires a complete residual clutter
  of one- and two-recut causes, not merely the list of partners which broke
  the core in a clean Hamming-two child; and
* a checked core `K_p` of a closed Hamming-two bank `B[p]` defines an exact
  third-recut breaker set

\[
 X_p(K_p)=\{g:\ p\cup\{g\}\in\mathcal C_3,\
                   D(K_p)\text{ changes from }B[p]
                   \text{ to }B[p\cup\{g\}]\}.             \tag{2.7}
\]

Only triples \(p\cup\{g\}\) with \(g\in X_p(K_p)\) can escape that named core.
A Hamming-two numeric proof or core hash without occurrence-labelled
transport data does not instantiate (2.7).

## 3. Base-local role/palette joins and ternary completeness

For a native q1 atom `e=(tau,eta,c)`, its final legality on this one-for-one
face has the typed form

\[
 I_e(S)=G^\mathrm{tail}_e(S)G^\mathrm{head}_e(S)P_c(S).   \tag{3.1}
\]

The endpoint factors depend only on the selected state at their endpoint
bases.  A forced-role relocation is likewise detected at its literal owner
base.  The palette factor is evaluated from the exact additive law

\[
 m_S(c)=m_0(c)+\sum_{g\in S}
 \left({\bf1}_{\mathrm{new}(g)=c}
       -{\bf1}_{\mathrm{old}(g)=c}\right).                \tag{3.2}
\]

Let `X,Y,Z` be typed primitive-support relations, for example tail, head and
palette supports, and put \(x_b=|X\cap R_b|\), with analogous notation.  The
exact number of ordered distinct-base pair witnesses is

\[
 J_2(X,Y)=|X||Y|-\sum_b x_b y_b.                            \tag{3.3}
\]

The exact number of ordered distinct-base triple witnesses is

\[
\begin{split}
 J_3(X,Y,Z)={}&|X||Y||Z|
 -|Z|\sum_b x_b y_b-|Y|\sum_b x_b z_b-|X|\sum_b y_b z_b\\
 &+2\sum_b x_b y_b z_b.                                     \tag{3.4}
\end{split}
\]

Formula (3.4) is inclusion-exclusion on the three equal-base events.  Exact
palette multiplicity, endpoint state, role identity and all proper-subset
minimality tests are then applied to each witness.  Role constraints and
(3.2) can only delete witnesses from (3.3)-(3.4).  Different typed witnesses
may project to the same physical support, so the support key is the sorted
primitive `rid` list; retain all witness provenance but emit that key once.

### Corollary 3.1A (functional ternary supplier on the frozen palette)

The frozen palette ledgers certify that all 7,612 baseline-selected lower
colours are distinct, all 20,477 candidate-cut lower colours are distinct,
and no candidate new colour is baseline-selected.  Consequently
\(g\mapsto\operatorname{new}(g)\) is injective on \(R\).  A previously
unselected colour \(c\) has at most one supplier, denoted \(\sigma(c)\), and
a baseline-selected colour has only its unique old-base remover.

Therefore palette status itself has no inclusion-minimal binary or ternary
compensation support.  An inclusion-minimal ternary atom must have the
functional form

\[
 \{g_{\rm tail},g_{\rm head},\sigma(c)\},                 \tag{3.4a}
\]

where the first two recuts create the two endpoint states and
\(\sigma(c)\) supplies the previously unselected colour.  If \(c\) is
baseline-selected, atom activation has support at most two.  If
\(b_s=\beta(\sigma(c))\), and \(X,Y\) are the tail/head creator relations,
then the exact ordered endpoint-witness count before final truth filtering is

\[
 (|X|-x_{b_s})(|Y|-y_{b_s})
       -\sum_{b\ne b_s}x_b y_b.                           \tag{3.4b}
\]

Indeed, injectivity makes the palette supplier unique; distinct-base
compatibility excludes both endpoint creators from its base, and the last
sum excludes equal endpoint bases.  A creator coinciding with the supplier
only lowers the support.  The hashes authenticating the two finite palette
inputs are
\(\texttt{bcaa7f353d00504edb954d448d7537f7f4d2c851d929be89df98e1c66be373f8}\)
for the projection ledger and
\(\texttt{4ad806b8b8ae3eecfd560abec3709de8ab74cd04f198771924d5d09b3e9b8c23}\)
for the frozen baseline-colour ledger.

This removes multi-supplier palette ambiguity but does not bound the
tail/head creator relation.  That occurrence-labelled relation is one of
the missing native tables.

For any Boolean occurrence or guard datum define its primitive ternary
residue on `S={g,h,k}` by

\[
 j_d(S)={\bf1}\{v_d(S)\ne v_d(\varnothing)\}
         \prod_{T\subsetneq S}{\bf1}\{v_d(T)=v_d(\varnothing)\}. \tag{3.5}
\]

For non-Boolean data, the indicators in (3.5) mean literal content-key
equality.  The support-three part of `A_3(K)` includes `S` whenever (3.5) is
one for a datum of `D(K)`.

### Lemma 3.1 (proof-safe locality catalogue)

Assume the complete dependency cone of every core is present.  Direct
base/role/capacity changes, all exact two-factor joins, and the exact
tail--head--palette joins (3.4), followed by the eight-bank truth test
(3.5), generate every member of `A_3(K)`.

#### Proof

A dependency-cone datum changes directly, or because the truth or footprint
of an incident native atom, guard or blocker changes.  Direct occurrence,
role and capacity states are base-local.  An atom change is determined by
the three factors in (3.1), with its palette value fixed by (3.2).  If one
primitive supplies all changed factors the minimal support has size one; if
two primitives suffice it is in a two-factor join; if three are necessary,
their bases are distinct and they occur in the typed triple join (3.4).
The literal truth test (3.5) retains exactly the inclusion-minimal causes.
Complete footprints include conflicts on resources outside the positive
row, so blocker and capacity changes are not missed. \(\square\)

This lemma is not a small-count theorem.  A tail, head and palette support
can have a large Cartesian join.  Its value is that the join is finite,
sparse when the physical supports are sparse, and complete for genuinely
ternary residues.

### Lemma 3.2 (dirty-subset safety)

No predicate which rejects a triple because one of its proper subsets is
zero-265-dirty is proof-safe.  The five zero-265 values are imposed only on
the direct final bank `B[S]`.

#### Proof

For a zero row `r`, write its exact order-three expansion as

\[
 z_r(ghk)=z_r(\varnothing)+\sum_i\Delta_i z_r
          +\sum_{i<j}\Delta_{ij}z_r+\Delta_{ghk}z_r.       \tag{3.6}
\]

The last term records a newly activated provider, a removed demand, a role
move, a changed blocker or another genuine final-net compensation.  It is
not determined by the singleton and pair values.  It can cancel the debt of
every proper subset.  Direct construction of all eight subset banks retains
this term, whereas proper-subset pruning deletes it. \(\square\)

Thus the complete prelaunch order is: form the causal meet on formal banks,
retain all unary, binary and ternary residues, and only then intersect its
shadow with the five literal final zero rows.

## 4. Exact clutter-shadow count and no-duplicate generator

Split the antichain `M` by size as `M_1,M_2,M_3`.  Put

\[
 s_b=|M_1\cap R_b|,\qquad n'_b=n_b-s_b,\qquad N'=\sum_b n'_b,              \tag{4.1}
\]

where `n_b=|R_b|`.  Let `G=(R minus M_1,M_2)` be the simple graph of joined
pair anchors.  Minimality ensures that no edge of `M_2` is incident with a
vertex of `M_1`.

For `v in G` and a base `c`, let `d_c(v)` be the number of neighbours of `v`
on base `c`.  Define the compatible-wedge and triangle counts

\[
 W_\triangle=\sum_v\sum_{c<d}d_c(v)d_d(v),                \tag{4.2}
\]

where `c,d` are distinct from `beta(v)`, and let `T_triangle` be the number
of triangles of `G`.  Every triangle automatically occupies three distinct
bases.

Write

\[
 e_3(n)=\sum_{b<c<d}n_b n_c n_d.                            \tag{4.3}
\]

### Theorem 4.1 (exact radius-three shadow formula)

The number `C(M)` of compatible support-three packets containing at least
one joined anchor is

\[
\boxed{
\begin{split}
 C(\mathcal M)={}&e_3(n)-e_3(n')\\
 &+\sum_{uv\in M_2}\bigl(N'-n'_{\beta(u)}-n'_{\beta(v)}\bigr)
   -W_\triangle+T_\triangle+|M_3|.
\end{split}}                                               \tag{4.4}
\]

#### Proof

The first difference counts exactly the triples containing a vertex of
`M_1`.  Remove all such vertices.  For an edge `uv`, the number of compatible
third vertices is `N'-n'_{beta(u)}-n'_{beta(v)}`.  Summing this over edges
counts a remaining triple once for each graph edge it contains.

A compatible triple containing `r` graph edges contributes `r` to the edge
sum, `binom(r,2)` to `W_triangle`, and one to `T_triangle` exactly when
`r=3`.  Therefore its contribution to

\[
             r-{r\choose2}+{\bf1}_{r=3}
\]

is one for `r=1,2,3`.  This proves the middle line.  By antichain
minimality, a member of `M_3` contains no singleton or pair anchor, so the
last term is disjoint from the preceding terms. \(\square\)

Formula (4.4) also supplies an exact no-duplicate generator.  First emit
triples containing a singleton anchor under their least contained singleton;
then, on the remaining vertex set, emit triples containing a pair anchor
under their least contained edge; finally emit each key in `M_3`.  A sorted
three-`rid` packet key occurs in exactly one stage and under exactly one
primary anchor.

## 5. Frozen threshold consequences

A read-only rebuild from the frozen cut-choice and round-02 bank ledgers
gives

\[
 N=16667,\qquad \#\{b:n_b>0\}=3803,\qquad
 \sum_b n_b^2=118143,\qquad \max_b n_b=39.                 \tag{5.1}
\]

For a singleton recut on base `b`, its compatible radius-three shadow is

\[
 Q_b=\frac{(N-n_b)^2-\left(\sum_c n_c^2-n_b^2\right)}2.    \tag{5.2}
\]

The minimum occurs at a base with `n_b=39` and is

\[
                         \min_b Q_b=\boxed{138186881}.    \tag{5.3}
\]

### Corollary 5.1 (necessary and sufficient ten-million test)

On the frozen histogram, \(C(\mathcal M)\le10000000\) is possible only if

\[
                              M_1=\varnothing.            \tag{5.4}
\]

When (5.4) holds, the exact necessary and sufficient test is

\[
 \sum_{uv\in M_2}(N-n_{\beta(u)}-n_{\beta(v)})
       -W_\triangle+T_\triangle+|M_3|\le10000000.         \tag{5.5}
\]

A convenient sufficient test is

\[
                         16665|M_2|+|M_3|\le10000000,     \tag{5.6}
\]

because every endpoint base of an edge contains at least one recut and
`-W_triangle+T_triangle<=0`.  For example, `|M_2|<=600` and
`|M_3|<=1000` imply the requested bound.  Equation (5.5), not (5.6), is the
sharp test and may permit a larger highly overlapping pair clutter.

For comparison, the current single-root `A21` hitting family has the already
frozen exact shadow

\[
                              2909465711,                 \tag{5.7}
\]

so the root fan alone is nearly three orders of magnitude above the target.

## 6. Exact shadow of the 3664 Hamming-two portfolio

Let `P3664` be the graph whose vertices are primitive recut keys and whose
edges are the 3,664 keys in
`scratch/threadD_k17_exact3664_q1_20260802/cases.tsv`.  A read-only parser
independent of the case producer reconstructed the base histogram from

* `k17_two_cut.candidates.tsv`, SHA-256
  `fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6`;
* `round02.bank.tsv`, SHA-256
  `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`;
  and
* `cases.tsv`, SHA-256
  `860924cbb256d320ee35790e98ebd1e78bf0b01cdabf1bdbf9fdaef0929fa109`.

Applying the middle line of (4.4) gives

\[
\begin{array}{rcl}
 |E(P3664)|&=&3664,\\
 \displaystyle\sum_{uv\in E}(N-n_{\beta(u)}-n_{\beta(v)})
     &=&61006005,\\
 W_\triangle&=&708238,\\
 T_\triangle&=&0,\\[2mm]
 |\operatorname{shadow}_3(P3664)|
     &=&61006005-708238+0\\
     &=&\boxed{60297767}.
\end{array}                                                \tag{6.1}
\]

Thus “append one arbitrary recut to every closed Hamming-two case” still
has 60,297,767 distinct compatible packets, over six times the requested
ceiling.  To shrink this class proof-safely one needs the occurrence-
labelled sets `X_p(K_p)` from (2.7); the sufficient pre-dedup condition

\[
                         \sum_{p\in P3664}|X_p(K_p)|
                                  \le10000000              \tag{6.2}
\]

would require an average at most `2729.257641921` third recuts per case,
and the residual no-portfolio-edge classes consume part of the same budget.

The edge shadow (6.1) is **not** a complete radius-three generator.  A
locally dirty pair can be repaired only by its third recut; three proper
pairs can retain different stored cores while the full triple disturbs all
of them; and a primitive tail--head--palette residue can first occur at
support three.  Such packets need contain no edge of `P3664`.

## 7. Why the current marginals cannot certify the stronger sieve

The presently frozen native tables supply:

1. `anchors.tsv`: the 21 root-fan singleton anchors;
2. the 13 clean-anchor semantic profiles and binary persistent/exact-build
   classifications;
3. `counts_union.tsv`: marginal counts by anchor;
4. `map.tsv` and `groups.tsv`: 3,664 anchor-relative **binary** delta keys,
   all in singleton equality classes; and
5. checked numeric q1 cores for the 3,664 final pair banks.

They do not supply:

* a frozen complete `L0` dependency-cone and embedding manifest;
* `A_3(K)` for multiple unconditional traces;
* the two-partner residual clutters of the singleton cores;
* exact tail, head, palette and role relations with their ternary joins;
* eight-bank truth tables for dirty pair repair; or
* the third-recut transport sets `X_p(K_p)` for the 3,664 pair cores.

The certificate archive contains 3,664 `core.cnf` files but no variable-to-
occurrence `.map` files.  Those cores prove the named pair formulas UNSAT,
but as frozen they cannot identify which arbitrary third recut changes a
core literal, provider, footprint, blocker or role.  Rebuilding and freezing
that transport information is new light semantic analysis, not a consequence
of the existing hashes.

### Theorem 7.1 (lower-marginal indistinguishability obstruction)

No rule using only singleton and pair dependency marginals can proof-safely
omit a radius-three support on the assertion that every proper subset
retains a core.  This remains true after intersecting any finite number of
such marginal core profiles and after inspecting the proper-subset zero-265
values.

#### Proof

Fix three distinct-base recuts `g,h,k`.  Consider two formal
occurrence-labelled completions which agree on every bank `B[T]` for
`T proper subset {g,h,k}`.  In the first, a named core datum is unchanged on
the full triple.  In the second, add a load-bearing atom `e` whose tail state
is enabled only by `g`, whose head state is enabled only by `h`, and whose
previously unselected colour is inserted by `k`.  This obeys endpoint-base
locality, (3.1), and the additive palette law (3.2).  The atom is absent in
every proper subset and present in the full triple, so it can enlarge a
positive core row or invalidate a named blocker only in the full triple.

For several cores use one such load-bearing atom per dependency cone, with
the same three factor supports.  All singleton and pair core marginals are
still identical.  The new atoms may be chosen outside the five zero-265
interfaces, leaving those proper-subset marginals identical as well.  Or,
for dirty repair, the same ternary activation can supply the final provider
which cancels a proper-subset debt.  Therefore the two completions receive
the same verdict from every rule based only on the stored lower marginals,
while one has a persistent trace and the other has a genuine ternary escape.

This is an information statement about the marginals, not a claim that the
frozen raw bank realizes every abstract completion.  Inspecting the raw bank
through the exact joins of Section 3 resolves the ambiguity; the current
marginal files do not. \(\square\)

Consequently, the existing marginal data alone support only the previously
frozen `2,909,465,711` root-anchored universe.  Any smaller complete count
must cite newly frozen occurrence-labelled causal relations or literal
unchanged-core certificates on the omitted ternary supports.  Assuming
that binary persistence is monotone under a second partner would be false.

## 8. Exact finite gate for a future launch

A proof-safe attempt at the ten-million target must freeze, before packet
generation:

1. every unconditional core trace and complete `D(K)`;
2. per-datum direct, tail, head, palette and role support relations;
3. exact pair and triple join outputs after (3.2) and (3.5), including dirty
   subset truth tables;
4. each per-core clutter `A_3(K)` and the sequential meet (2.6);
5. the deduplicated joined clutters `M_1,M_2,M_3`; and
6. an audit containing `e3(n)-e3(n')`, the edge-completion sum,
   `W_triangle`, `T_triangle`, `|M_3|` and the total (4.4).

The launch threshold is certified exactly when that audit satisfies (5.5).
If it does not, the theorem proves a count obstruction for that declared
multicore sieve; it does not license dropping anchors.  If the required
relations are absent, the verdict is `UNPROVED_THRESHOLD`, not a claimed
small catalogue.

No SAT, rank-ten, residence, topology or compiler conclusion is made here.
Passing the causal meet and zero-265 remains only a promotion to the exact
unconditional/successor-core semantic filters.
