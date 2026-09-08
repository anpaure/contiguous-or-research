# Flexible SCD detachment is exact through `m=8`, but acyclicity is an independent row

Date: 2026-08-01  
Lane: Thread D / fixed-`M_0` SCD detachment  
Status: exact finite SAT replay for `m=4,...,8`; exact typed phase
grammar and certificate theorem; exact `m=4` counterexample to automatic
acyclicity and to the canonical strict-potential subcatalogue.  No all-`m`
detachment theorem is claimed.

## 0. Outcome

The flexible long-ear CNFs are genuinely positive.  Their decoded models
have maximum rooted indegree and outdegree one, no directed cycle, complete
upper and lower palettes, and therefore exactly `Cat_m` path components for
each `m=4,...,8`.

The finite witnesses do **not** reveal a phase formula depending only on a
coordinate rank, a Greene--Kleitman free-position index, or the canonical
owner-sum potential.  Both aligned/reverse phases occur from `m=6` onward,
and many selected arrows decrease the canonical potential.

This is not merely an artefact of the solver output.  The flexible `m=4`
catalogue contains an exact palette/head-injective feasible detachment with
a directed five-cycle.  Consequently no fixed standard-SCD potential can
make **every** feasible detachment acyclic.  Moreover, if every new arrow is
required to increase the canonical owner-sum potential, the full exact
`m=4` system is infeasible: all `768` assignments in the positive option
product were replayed, `21` pass provider/head/tail injectivity, and all
`21` fail the untouched-head release row.

Thus the proof-safe all-dimensional target is not “prove that detachment is
automatically acyclic.”  It is either

1. construct one typed detachment and impose graphic circuit cuts; or
2. enlarge the long-ear grammar and then prove a monotone matching theorem
   in the enlarged catalogue.

## 1. Exact flexible phase grammar

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
\]

and freeze the standard four-row matching `M_0`.  On a standard SCD chain
write

\[
 R\subset S\subset L\subset U\subset W,
 \qquad x=L-S,\quad y=U-L,
\]

when the indicated rows exist.  Put `P(X)=M_0^{-1}(X)` whenever `X` is a
physical owner.

Write

\[
 N_m={2m-1\choose m}={2m-1\choose m-1},\qquad
 C_m=\operatorname{Cat}_m.                            \tag{1.0}
\]

### 1.1 An `aU'` target

Choose a central facet `L=U'-b`.  The first new rooted edge is always

\[
 aS\longrightarrow P\bigl(a(S+b)\bigr),             \tag{1.1}
\]

and has new upper colour `aU'`.

There are the following exact old-colour return phases.

* If `S<L` is short, the unique phase is

  \[
  zS\longrightarrow P(zL)=L.                         \tag{1.2}
  \]

* If `R<S<L` is long, the aligned `C` phase is

  \[
  azR\longrightarrow P\bigl(az(R+x)\bigr),           \tag{1.3}
  \]

  while the reverse `D` phase is

  \[
  zS\longrightarrow azR.                             \tag{1.4}
  \]

In every case the second edge has the old upper colour `azL`.  Thus the
operation replaces one `azL` provider by two edges with colours
`azL,aU'`.

### 1.2 An all-`G` target `W'`

Choose a provider facet `U=W'-v` whose standard chain contains
`R<S<L<U`, and choose `t in L`.  Put

\[
 V=L-t,\qquad C=zL,\qquad D=z(V+y).
\]

The first new edge is

\[
 L\longrightarrow P(L+v),                            \tag{1.5}
\]

with new upper colour `W'`.  The second tail is `zV`.  It is legal in
exactly either of the following two cases:

\[
\begin{array}{c|c|c}
\text{phase}&M_0(zV)&\text{second head}\\ \hline
A&C&P(D),\\
R&D&P(C).
\end{array}                                          \tag{1.6}
\]

The second physical edge has old upper colour `zU` in either orientation.

The target sectors have sizes

\[
 E={2m-3\choose m}={2m-3\choose m-3},\qquad
 J={2m-3\choose m+1}={2m-3\choose m-4}.             \tag{1.7}
\]

They are precisely the missing `a`-only and all-`G` upper sectors of the
isolated seed.

## 2. The exact certificate theorem

Let one option of (1.1)--(1.6) be chosen for every one of the `E+J`
missing targets.  Require:

1. **provider injectivity:** no seed provider is replaced twice;
2. **new-head injectivity:** all two new rooted heads in all chosen options
   are distinct;
3. **auxiliary-tail injectivity:** all second rooted tails are distinct;
4. **untouched-head release:** if a new head is the head of an old seed
   provider, then that provider is among the replaced providers.

### Theorem 2.1 (typed exactness)

After replacing the chosen providers and retaining every unchosen seed
provider, conditions 1--4 imply:

* every rank-`(m+1)` upper colour occurs exactly once;
* every selected rank-`(m-1)` lower colour occurs exactly once;
* rooted indegree and outdegree are at most one;
* physical degree is at most two.

The support is a `Cat_m`-component physical path forest if and only if its
rooted directed graph has no directed cycle.

#### Proof

Each option retains the old provider colour with its second edge and adds
its advertised missing target with its first edge.  Target exactness and
provider injectivity therefore give the complete upper palette exactly
once.

The first tails are the distinct replaced-provider tails.  The second-tail
signature banks in (1.2)--(1.6) are disjoint from the first-tail banks;
condition 3 handles collisions within them.  Every displayed rooted edge
has physical intersection equal to its rooted tail, so the lower colours
are distinct.

Condition 2 handles collisions among new heads.  Condition 4 handles the
only remaining collision, with an unchanged provider head.  Hence rooted
in/outdegree is at most one.  Since `M_0` is a bijection between roots and
physical owners, each physical owner can occur at most once as an outgoing
endpoint and once as an incoming endpoint, giving degree at most two.

Such a finite support is a disjoint union of paths and cycles.  An
undirected cycle is directed because every vertex on it has one incoming
and one outgoing edge.  Thus excluding directed cycles is necessary and
sufficient.  Finally `N_m` vertices and `N_m-C_m` edges leave `C_m`
components. \(\square\)

Theorem 2.1 is the exact all-`m` **rule schema** extracted from the long-ear
grammar.  What is not proved is that its four injectivity/release rows and
the graphic row have a simultaneous solution for every `m`.

## 3. Decoded finite witnesses

The generator is

`scratch/search_scd_global_seed_detachment_sat_20260801.cpp`.

The retained H100 directory is

`/home/amodo/or15/work/root_scd_detachment_20260801/`.

The exact model replay gives:

\[
\begin{array}{c|r|r|r|r|r|r|r|r}
m&E+J&\text{options}&\text{clauses}&aC&aD_{\rm long}&aD_{\rm short}&zA&zR\\ \hline
4&6&38&282&0&4&1&0&1\\
5&28&262&3890&0&14&7&0&7\\
6&120&1572&40440&23&37&24&19&17\\
7&495&8704&352275&108&132&90&45&120\\
8&2002&45698&2711250&473&498&316&137&578
\end{array}                                           \tag{3.1}
\]

The resulting edge counts are respectively

\[
 21,84,330,1287,5005,
\]

and the component counts are

\[
 14,42,132,429,1430=\operatorname{Cat}_m.
\]

Every replay has maximum rooted indegree/outdegree one and zero directed
cycles.  Among the two new arcs per option, the numbers which do not
strictly increase the canonical physical-owner potential

\[
 \Phi(X)=\sum_{i\in X}i
\]

are `2,15,82,394,1472` for `m=4,...,8`.  The witnesses are therefore not
instances of the canonical monotone subcatalogue.

## 4. Exact potential obstruction at `m=4`

Use one-based coordinates `G={1,2,3,4,5}`, `a=6`, `z=7`.  Select option
variables

\[
                      \{2,14,18,22,26,32\}.          \tag{4.1}
\]

They choose one option for every target, use distinct providers, new heads
and auxiliary tails, and satisfy every untouched-head release clause.  The
result has `21` distinct upper colours, `21` distinct lower colours and
maximum physical degree two.  Nevertheless its roots contain the directed
cycle

\[
 \{2,3,6\}\to\{1,2,6\}\to\{1,5,6\}
 \to\{4,5,6\}\to\{3,4,6\}\to\{2,3,6\}.             \tag{4.2}
\]

The corresponding physical owners are

\[
 \{2,3,4,6\},\{1,2,3,6\},\{1,2,5,6\},
 \{1,4,5,6\},\{3,4,5,6\}.                           \tag{4.3}
\]

Thus a fixed potential on standard SCD roots or owners cannot certify
every feasible detachment.

There is also no repair obtained merely by keeping the canonical potential
positive.  At `m=4`, the six targets have respectively

\[
                         3,4,4,4,2,2                 \tag{4.4}
\]

options for which both new physical arrows strictly increase `Phi`.
Exhausting their `768` products leaves `21` assignments after
provider/head/tail injectivity, and every one violates an untouched-head
release.  This is a sharp scoped no-go for the current grammar, not for an
expanded multi-ear packet.

## 5. What remains

The finite evidence supports the following weaker conjecture only:

> For every `m>=4`, the full flexible phase grammar admits a selection
> satisfying conditions 1--4 and the graphic circuit inequalities.

A proof must correlate phase, provider, release, and graphic choices.  It
cannot be reduced to an anonymous phase-zero capacity-two matching, nor can
acyclicity be deleted from the model.  A useful recursive proof would
export either a graphic-matroid state or a bounded family of component
endpoint tickets; the standard coordinate-sum order is insufficient.

## 6. Artifacts and hashes

Local source and replay:

* `scratch/search_scd_global_seed_detachment_sat_20260801.cpp`  
  SHA `16faf809cdb88942df4702874165d9f276e0e6ca182ceada33009ff229931911`;
* `scratch/audit_threadD_scd_flexible_detachment_phase_rule_20260801.py`  
  SHA `d4b4b1fa56857bb73134528f44557bd969ad9ffd18d966947c5f8c93c0a30998`;
* `scratch/threadD_scd_flexible_detachment_phase_rule_20260801.audit.json`  
  SHA `459c3b0e3d81e0934e11def1765eaa6695340d841e61b94c97b1e21b4c80996b`.

Remote CNF SHA values for `m=4,...,8` are

\[
\begin{array}{c|l}
4&96d35dc68efb551ae0ee5cd52f1f25a97cd86075d39ba468dc4666c7429181f0\\
5&f81378ed95968269752e3ecdf177905cdc415c67a5c51d65ca0940ca8b9eb5d1\\
6&2826821cb72870bcd10662d03553e9d37c40b81fe063180e8ebdd834b7603b3c\\
7&87e2bde1feb5e811d59d6b0061d0e3ee7575b904e9aadba8b1158269521ee384\\
8&305bd5694da5158e2982ca369e435bc90c37ffa8810c864caa95fe8479f9e047
\end{array}
\]

and the corresponding SAT-output SHA values are

\[
\begin{array}{c|l}
4&182bf5e4690f0c8b625992bbcb98fe01b96edca24cc719ccee4c3c301fe54aff\\
5&82e2e70ebf892c07682ec1525a18cc9c125e6bdc7f7c1b955bd150c5f9c0c273\\
6&a5d1e7f624cb9f31e9fe6677df58f015390240e866e13f8e47a5ca515bf74e75\\
7&031a9755e912a0221035fa549ea9f5241bfef6e0ca1f618b84590fbfd3c93af1\\
8&4a6a1fd1e93ec7a56401a9294924207132ac5144a41faebbc24d8eb50ce2aa00.
\end{array}
\]

The audit reconstructs the option ordering directly from `M_0`, decodes
the five SAT outputs, replays degree and cycle rows, verifies (4.1)--(4.3),
and exhausts the positive-potential product (4.4).  It performs no SAT
search.
