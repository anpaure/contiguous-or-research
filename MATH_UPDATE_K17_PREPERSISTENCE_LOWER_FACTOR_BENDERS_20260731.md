# K17 pre-persistence lower-factor and guarded Benders rows

## 0. Scope

This note isolates constraints which may be imposed while an all-upper-target
CEGAR is still choosing seams and witness blocks. The conclusions concern
the exact lower-rainbow Hamilton-path projection; direction, residence, and
literal upper intervals remain separate guarded constraints.

Let \(V\) be the \(N\) rank-\(r\) owners, let \(\mathcal C\) be the \(N\)
rank-\((r-1)\) lower colours, and put

\[
                 \chi(uv)=u\cap v.
\]

Fix a lower-rainbow Johnson 2-factor \(F\). For each colour \(c\), denote by
\(f_c\) its unique edge in \(F\). Let \(E^\star\) be a fixed physical
Johnson-edge catalogue containing \(F\). Opposite directed realizations of
one physical edge are represented by one undirected selector \(q_e\).

## 1. Exact undirected lower-factor projection

Use binary endpoint variables \(p_v\), omitted-colour variables \(z_c\), and
physical-edge variables \(q_e\). Consider

\[
 \sum_{e\ni v}q_e+p_v=2,
 \qquad \sum_vp_v=2,                                      \tag{1.1}
\]

\[
 \sum_{e:\chi(e)=c}q_e+z_c=1,
 \qquad \sum_cz_c=1,                                      \tag{1.2}
\]

and the graphic rows

\[
             \sum_{e\in E^\star[S]}q_e\le |S|-1
             \qquad(\varnothing\ne S\subseteq V).         \tag{1.3}
\]

### Theorem 1.1

The integral solutions of (1.1)--(1.3) are exactly the undirected spanning
Johnson paths which use every lower colour except one exactly once.

#### Proof

Summing (1.1) gives \(\sum_eq_e=N-1\). Rows (1.3) make the selected graph a
forest, so a forest on \(N\) vertices with \(N-1\) edges is a spanning tree.
Equation (1.1) bounds every degree by two and gives exactly two degree-one
vertices; hence the tree is a spanning path. Equation (1.2) gives the
claimed rainbow colour ledger. The converse is immediate. \(\square\)

This theorem does **not** orient the path. A prescribed family of directed
blocks must still be compatible with one of its two global orientations.

## 2. Exact colour-source and endpoint/ejection conservation

Define the physical source-cut variable

\[
                         c_c=1-q_{f_c}.                    \tag{2.1}
\]

Subtracting the source-factor contribution from (1.1)--(1.2) gives two
exact identities:

\[
 \boxed{
   \sum_{e\in E^\star\setminus F:\chi(e)=c}q_e+z_c=c_c
 }                                                            \tag{2.2}
\]

for every colour, and

\[
 \boxed{
   \sum_{e\in E^\star\setminus F:e\ni v}q_e+p_v
      =\sum_{c:v\in f_c}c_c
 }                                                            \tag{2.3}
\]

for every owner. Thus a nonfactor edge cuts its *colour-source* factor edge,
while its two endpoint incidences must be paid for by source cuts at the two
endpoints. An endpoint consumes one cut incidence rather than providing
slack.

Summing (2.3) yields

\[
        |\{\hbox{selected nonfactor edges}\}|
          =|\{\hbox{source cuts}\}|-1.                      \tag{2.4}
\]

Every additional ejection cut therefore requires one additional return
edge. Equations (2.2)--(2.3), rather than scalar equation (2.4), are the
strong exact rows for a variable-cut master.

There are two different cut variables which must not be conflated.  A seam
set-cover scaffold has an already-made cut indicator \(\widehat c_c\), often
defined only by its selected seam endpoints.  The eventual path has the
physical source-cut variable \(c_c\), and unrestricted completion permits
\(c_c=1\) even when \(\widehat c_c=0\).  Substituting \(\widehat c_c\) for
\(c_c\) in (2.2) is exact only for the retained-old/no-extra-ejection face.
If the eventual \(c_c\)'s are deferred, the safe eager projection is seam
colour simplicity plus disjointness from source edges protected by selected
guards.  Unprotected source-colour conflicts are ejection obligations, not
no-goods.

## 3. Exact OR guards and the collision rows

For every witness/provider choice \(w\), let \(R(w)\) be the set of distinct
physical edges which that choice forces to survive in the eventual path.
For each physical edge \(e\), define the exact OR

\[
       g_e=\bigvee_{w:e\in R(w)}y_w.                         \tag{3.1}
\]

All direct seam-choice variables which force \(e\) are included among the
reasons in (3.1). In a binary model the fail-closed encoding is

\[
 g_e\ge y_w\quad(e\in R(w)),
 \qquad
 g_e\le\sum_{w:e\in R(w)}y_w.                              \tag{3.2}
\]

The upper bound is omitted only when \(g_e\) is deliberately allowed to
represent an independently selected edge. One must never add reasons
arithmetically: two targets protecting the same physical edge consume one
edge, not two.

Since \(q_e\ge g_e\), (2.2)--(2.3) imply the eager rows

\[
 \boxed{
   \sum_{e\in E^\star\setminus F:\chi(e)=c}g_e+z_c
      \le c_c\le 1-g_{f_c}
 }                                                            \tag{3.3}
\]

and

\[
 \boxed{
   \sum_{e\in E^\star\setminus F:e\ni v}g_e+p_v
      \le\sum_{c:v\in f_c}c_c
      \le 2-\sum_{c:v\in f_c}g_{f_c}.
 }                                                            \tag{3.4}
\]

The left side of (3.3) is the physical colour-source cut implication; the
right side is protected-source retention. Adding them gives
\(g_{f_c}+\sum_{\chi(e)=c,e\notin F}g_e+z_c\le1\). The
omitted-colour term is essential: a colour already occupied by a protected
source edge or a return seam cannot also be the unique hole.

Likewise every forced cycle is final for that bank:

\[
              \sum_{e\in E^\star[S]}g_e\le |S|-1.           \tag{3.5}
\]

For integral guards, (3.5) is separated by an ordinary union-find cycle
test. Rows (3.3)--(3.5) are exactly the colour, owner-degree, and graphic
independence tests on the forced bank. They do not by themselves certify
extendability.

For a compact implementation, (3.3) may be written as a per-colour
guard-consensus/reservation disjunction. Introduce one selector
\(\ell_{c,e}\) for each physical edge of colour \(c\), impose

\[
          \ell_{c,f_c}=1-c_c,\qquad
          \sum_{e\notin F:\chi(e)=c}\ell_{c,e}+z_c=c_c,
 \qquad g_e\le\ell_{c,e},
 \qquad y_w\le g_e\quad(e\in R(w),\ \chi(e)=c).             \tag{3.6}
\]

A witness which forces two distinct physical edges of one colour is thereby
forbidden. Different witnesses may share one edge without double charging.
This is the exact binary guard-consensus projection for one colour; pairwise
witness conflicts are a weaker projection of (3.6). It becomes the actual
physical-edge selector formulation only when \(\ell_{c,e}=q_e\) is linked.

## 4. Exact incidence-flow Benders separator

Rows (3.3)--(3.5) catch local collisions. A diffuse forced bank can still
violate a residual Hall cut. Let

\[
 I=(V,\mathcal C;D),
 \qquad (v,c)\in D\iff c\subset v,
\]

be the owner--colour incidence graph. A physical edge \(uv\) of colour
\(c\) uses incidences \((u,c)\) and \((v,c)\). Define the exact incidence OR

\[
 \rho_{v,c}=\bigvee_{e:\,v\in e,\chi(e)=c}g_e.               \tag{4.1}
\]

It must itself be linearized exactly:

\[
 \rho_{v,c}\ge g_e\quad(v\in e,\chi(e)=c),\qquad
 \rho_{v,c}\le\sum_{e:\,v\in e,\chi(e)=c}g_e.               \tag{4.1a}
\]

Set

\[
                b_v=2-p_v,
        \qquad b_c=2(1-z_c).                                \tag{4.2}
\]

The local forced-degree rows are

\[
       \deg_\rho(v)\le b_v,
       \qquad \deg_\rho(c)\le b_c.                         \tag{4.3}
\]

For every \(X\subseteq V\), \(Y\subseteq\mathcal C\), residual incidence
completion requires

\[
 \boxed{
  2|X|-p(X)+
    \sum_{(v,c)\in D:\,v\notin X,\ c\in Y}\rho_{v,c}
  \le
  2|Y|-2z(Y)+|D\cap(X\times(\mathcal C\setminus Y))|.
 }                                                            \tag{4.4}
\]

### Theorem 4.1

On the incidence graph \(D\), (4.3)--(4.4) are necessary and sufficient for
extending the forced incidence set to an incidence \(b\)-matching with
degrees (4.2). They are valid linear Benders rows while the witness guards
remain variable.

#### Proof

For an integral guard choice, delete the forced incidences and give owner
and colour vertices residual demands

\[
                 d_a=b_a-\deg_\rho(a).
\]

Give every residual incidence capacity one in the network
\(s\to V\to\mathcal C\to t\). Expanding the capacity condition for the cut
whose source side is \(\{s\}\cup X\cup Y\) gives exactly (4.4). Integral
max-flow proves sufficiency. The same derivation with capacities
\(1-\rho_{v,c}\) separates (4.4) at a fractional master point, provided the
physical-edge ORs obey (3.2) and the incidence ORs obey (4.1a). \(\square\)

The theorem is exact only for the incidence \(b\)-matching projection on
\(D\). It does not encode which pair of owner incidences is realized by an
allowed physical edge, much less by a directed seam/collar or a chosen
history state; nor does it impose graphic connectivity. Thus restricting
\(E^\star\) by pair/collar/history compatibility cannot in general be
represented merely by deleting incidences from \(D\). A passing flow is not
a physical completion certificate. A failing flow is an exact master-level
obstruction.

## 5. Proof-safe CEGAR schema

1. **Physical OR layer.** Build (3.1) by physical edge identity, not by
   target count or source-tail count. Include old-target witnesses, new
   interval witnesses, provider seams, and upper-\(q_1\) pair witnesses.
2. **Eager exact rows.** Impose (3.3), (3.4), physical
   opposite-orientation at-most-one, and lazy forced-cycle rows (3.5). If
   full residual edge selectors are present, replace the inequalities by
   exact equalities (2.2)--(2.3).
3. **Flow recourse.** Separate (4.3)--(4.4) by max-flow. Persist the
   resulting \((X,Y)\) row and the physical-edge-to-incidence OR map.
4. **Common-independence recourse.** Only after the preceding projections
   pass, solve the directed tail/head/colour/graphic extension. An UNSAT
   no-good is valid only for the exact persisted guard assumptions, or for a
   deletion-minimal assumption core replayed against the complete arc
   catalogue.
5. **Literal replay.** Recheck arbitrary-width upper intervals, residence,
   direction, and the final compiler word.

There is no ordinary flow theorem for the last common-independence step: a
directed seam simultaneously consumes a tail, a head, and a colour, and the
graphic rows couple all of them. The max-flow separator in Section 4 is the
strong exact polynomial projection, not a replacement for that step.

## 6. Exact incumbent consequences

### 6.1 Superseded 650-hole incumbent

The earlier persisted bank had collision profile

\[
 (1,1)^{387}(2,0)^{42}(2,1)^1(3,0)^2
\]

in (nonfactor multiplicity, protected-source multiplicity). Hence 432
colours violated (3.3), with physical-edge repeat excess

\[
                  387+42+2+4=435.                           \tag{6.1}
\]

### 6.2 Persisted 361-hole round-three candidate

The newly persisted candidate is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        hard_allcegar_round3.candidate.json
    SHA-256
        3ec5113dbf1db39bbdb2a778146dbb19bbc1e84028f2335e2a7886b903d4842a
    payload
        745081446e35a3fa4f9ae2ca69cd03ad48a8ee1f71e5f91a1159db34c5a5d657

Its solver-free lower replay is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        hard_allcegar_round3.lower.audit.json
    SHA-256
        21b4806f87bb830464d85275db44fc51c679ba16011ede891115658ddf221866
    payload
        9fe69dcfefdbc865a76d82c7f16ff5e71f96fc18dda3383622d1cf56a572df95

The persisted selection has 1,557 seams, 2,189 cuts, and 361 remaining upper
holes

\[
                     11^{266}12^{88}13^7,
\]

with upper rank ten complete. Its exported forced bank is a graphic forest
of 7,422 distinct physical edges and maximum owner degree two, but it has
305 overfull lower colours and exact repeat excess 310. The collision
profile is

\[
                   (1,1)^{277}(2,0)^{23}(2,1)^5.            \tag{6.2}
\]

Thus the advertised protected bank has 305 offending colours in (3.3), and

\[
                    277+23+2\cdot5=310                     \tag{6.3}
\]

forced physical edges must be released before that exact bank can be
lower-rainbow.  Of these, selected seam-colour duplicate excess 28 is an
obstruction to retaining the fixed arcs themselves.  The remaining
protected-source/seam conflicts are conditional on retaining the exported
witness bank and may disappear under provider reselection.
The full partial graph has 1,063 lower-colour repeats and 1,695 missing
colours; it consists of 632 paths plus one untouched source 3-cycle. These
are necessary residual ledgers, not a completion.

The audit also records that selected old-target retention witnesses were not
exported. Thus the 7,422-edge bank is only the forced subset reconstructible
from the candidate, not the complete soft-all-old bank. Its 305 violations
remain decisive because adding omitted forced edges cannot repair a
colour-capacity violation.

### 6.3 Persisted 323-hole upper Pareto candidate

The later persisted candidate is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        hard_allcegar_round4.candidate.json
    SHA-256
        2c29f2f804ab5f08d3059fe3a3455fd9c174a30e35c18f450a9132422d22f15d
    payload
        19cf63f1d64e70e28cd72d191ddd754ba27f43b79a8deb97c199edeccfb72251

Literal replay confirms 1,564 seams, 2,209 scaffold cuts, upper rank ten
complete, and 323 remaining upper holes

\[
                       11^{224}12^{94}13^5.
\]

Its topology is 645 paths and two cyclic components containing 16 owners.
The 1,564 selected seams use only 1,527 lower colours, so the exact
unrestricted fixed-seam obstruction is duplicate excess 37.  In addition,
1,061 distinct seam colours still have their source-factor edge present in
the scaffold.  Those 1,061 are **not** an unrestricted obstruction: an
unprotected source edge may be released by a later ejection cut.

Consequently the retained-scaffold row

\[
        \sum_{a:\chi(a)=c}x_a\le \widehat c_c,
\]

with \(\widehat c_c\) equal to the already-made scaffold cut, is too strong
for arbitrary residual completion.  The exact unrestricted row instead uses
the eventual source-cut variable \(c_c\) from (2.1), giving the sandwich

\[
 \sum_{e\notin F:\chi(e)=c}g_e+z_c
       \le c_c\le1-g_{f_c}.                                \tag{6.4}
\]

If eventual cut variables are not yet in the master, its proof-safe eager
projection is only

\[
 \sum_{a:\chi(a)=c}x_a\le1,
 \qquad
 g_{f_c}+\sum_{a:\chi(a)=c}x_a\le1,                       \tag{6.5}
\]

where the second row applies to source edges protected by selected
witness/run guards.  Thus the frozen 323 arcs cannot be completed unchanged
because of the 37 seam duplicates.  Their 1,061 unrecycled source colours
are potential ejection obligations and belong in endpoint/flow recourse,
not in a fixed-candidate no-good.

The exact scoped lower-gate replay is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        hard_allcegar_round4.lower_gate.audit.json
    SHA-256
        7519ee3bb62cd8faf82fe83a0409216b25dbde28b7ed3ebbce6667c4a213a084
    payload
        67e46097ff3c62a6a69157b6ae242df1e0ba6975069f78c20f087af0ba488ae2

The soft-all-old model subsequently persisted a separate 437-hole candidate
with upper rank ten complete.  Its 1,601 seams have duplicate-colour excess
32, so it too is only upper-cover evidence, not a fixed-seam completion
face.  Its objective's 1,364 predicted old-witness losses are conservative;
literal replay gives the 437 actual upper holes.  Upper-\(q_1\) exactness
alone does not imply any of (2.2)--(4.4).

### 6.4 Persisted 2,649-target exact-active candidate

The first exact-active run made all 2,649 accumulated old targets explicit
alternatives between an old interval and a new seam witness, and imposed
seam-colour injectivity.  Its persisted candidate has 2,908 seams, 4,111
scaffold cuts, complete upper rank ten, and 751 literal upper holes

\[
                         11^{548}12^{194}13^9.
\]

All 2,649 active choices are exported: 1,140 use seam witnesses and 1,509
use old intervals, in addition to the 1,838 original-hole seam witnesses.
The seams use 2,908 distinct lower colours, so this candidate eliminates the
fixed-seam duplicate obstruction.  Of the 1,884 seam colours whose source
edge survives the scaffold, 742 source edges are unprotected and remain
valid ejection obligations.  The other 1,142 are protected by the exported
witness/run bank and violate (6.5).  The forced bank also contains one
graphic cycle.  Hence the fixed seam set is colour-simple, but this selected
witness bank is not a valid unrestricted residual face; provider/guard
reselection is required before incidence flow.

The frozen artifacts are

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        exactactive2649_round0.candidate.json
      SHA fd7594bc0cd6bd050e21997d4444e7be795bd0db0a92c079e44afd51b7f345b4
    scratch/threadD_k17_alltarget_residual_completion_20260731/
        exactactive2649_round0.lower_gate.audit.json
      SHA 18b5d274ec4a6867767ad969fbaacb64a08347f2ec3d73dfccf9e8f69816eab9
      payload 8e963fe465dd6b04508590f518cd53e056c2205e3598f10ca1b81d6d7b14b292

A corrected exact-active master now imposes both seam-colour injectivity and
selected-guard/source-colour disjointness.  It still requires a lazy forced-
cycle row and the eventual ejection/endpoint/incidence recourse before any
factor claim.

### 6.5 Guarded active-2,649 run: exact resource status

The corrected guarded master was run on H100 under an explicit CPU and
address-space cap.  It produced no incumbent.  The wrapper ended with status
`137`, and `/usr/bin/time` records signal 9 at

\[
 1701.48+110.02=1811.50\ {\rm CPU\ seconds},
 \qquad 15{:}42.13\ {\rm wall},
\]

with maximum RSS \(59{,}907{,}628\) KiB (about \(57.13\) GiB).  The last
solver line has `best: inf` at solver wall time \(755.69\) s.  No
`candidate_round0.json` or output `result.json` exists.  The copied
`exactactive2649.result.json` is only the infeasible input hint.

Thus the exact status is `UNKNOWN_RESOURCE_LIMIT`, not UNSAT.  In
particular, there is no persisted guarded bank on which incidence flow,
topology, or literal replay can be performed.  The frozen audit is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        guarded_active2649_h100/AUDIT.md

with producer SHA
`eec4cad69e32814c37f0b12bb81491201cf8c3032f8f082846905c955f9ad6bf`,
run-log SHA
`881c03420dcd3b957e4c7977bd69f4842efb6fafd67980c6bf8b51c3d9dea465`,
and resource-log SHA
`a685f9267f46584bf5c0efacde346b2ddac05d8dd11043265881575c5f150cb6`.

### 6.6 Exact fixed-bank obstruction and the first necessary release

Freezing the 2,908 colour-simple seams of the infeasible hint makes the
selected-guard question solver-free.

**Proposition 6.6 (fixed-seam guard factorization).**  Let \(S\) be a fixed
colour-simple directed seam bank, \(C(S)\) its canonical source-tail cuts,
and \(\Gamma(S)\) its seam-colour set.  Let \(R_a\) be the mandatory
run-guard tails of \(a\in S\).  For every required target \(T\), let
\(\mathcal P_T(S)\) contain every old or seam-witness support available with
this fixed seam bank.  Then a simultaneous selected protection bank exists
if and only if

\[
 R_a\cap C(S)=\varnothing,
 \qquad \chi(R_a)\cap\Gamma(S)=\varnothing
       \quad(a\in S),                                    \tag{6.6a}
\]

and, for every \(T\), some \(P\in\mathcal P_T(S)\) satisfies

\[
 P\cap C(S)=\varnothing,
 \qquad \chi(P)\cap\Gamma(S)=\varnothing.                \tag{6.6b}
\]

Here \(\chi(P)\) denotes the colours of the protected source edges indexed by
the tails in \(P\).  Indeed, necessity is the literal cut and colour guard.
For sufficiency choose one support in (6.6b) independently for each target:
protected old edges may be shared, so there is no cross-target capacity
constraint.  This is a reusable exact theorem for any fixed seam bank; it
does not choose the bank or complete its residual factor.

For the present bank, every selected seam has a mandatory run-guard set.
For each required upper target the audit enumerates every old prefix witness
and every suffix/seam/prefix support, then applies (6.6a)--(6.6b).

The exact replay fails both tests.  The mandatory run conflicts form a graph
on 1,619 selected seams with 1,145 incompatibility edges.  It is bipartite,
and the persisted maximum matching and minimum vertex cover both have size
702.  Hence every run-compatible subbank of this frozen seam set releases at
least 702 seams.  This is an exact lower bound, not a heuristic conflict
count.  With all 2,908 seams and their 4,111 cuts frozen, 921 of the 4,487
required targets have no compatible support even after enumerating all
support forms:

\[
 921=522\text{ original holes}+399\text{ active-old targets}
      =11^{768}12^{150}13^3.                              \tag{6.6c}
\]

The full-support and old one-shortest-catalogue zero sets coincide here.
The audit separately records 1,921 selected seam colours whose source edge
is not in a mandatory run guard; these are ejection obligations and are not
used as failures.

Thus witness reselection on the frozen seam set is exactly impossible.  The
weakest valid next relaxation is to release a vertex cover of the mandatory
run incompatibility graph, allow replacement seams, recompute the physical
cuts, and restore the affected target disjunctions.  Seam-colour injectivity
and selected-protected-source disjointness must not be relaxed.

The H100 replay used one CPU, 2.86 seconds wall, and 105,068 KiB peak RSS.
The producer/audit and independent certificate are

    scratch/threadD_audit_k17_fixedbank_guard_reselection_20260731.py
      SHA 482ad798bf1bea9af0afbbf70a2e61e4ac7e9ff08635723bc30619088fe6b8aa
    scratch/threadD_k17_fixedbank_guard_reselection_20260731/
        exactactive2649_fixedbank_guard_reselection.audit.json
      SHA d080c6b7e9f561a961cdc340cb4382a12ccc9272b6ead533b06cf021797ccf0b
      payload 3c2113cb8e9b7b2a8f6d5f468415e7ff99c88e26131bad914fd377e3e35e9d2e
    scratch/threadD_k17_fixedbank_guard_reselection_20260731/
        independent_certificate.audit.json
      SHA 77a3b420902805397bcf8b25e46d5047a6a41f71f4a8662738e4685503775884
      payload 45453c62966770f22251b335f61c9caf9c172f1a97008e9b852b18c4d321997d

For the unfrozen master, the repeated rows

\[
 r+\sum_{a:\chi(a)=c}x_a\le1\qquad(r\in R_c)
\]

have been replaced by the exact extended formulation

\[
 r\le g_c\quad(r\in R_c),\qquad
 g_c+\sum_{a:\chi(a)=c}x_a\le1.                          \tag{6.7}
\]

Eliminating the unpriced existential guard \(g_c\) recovers the old rows,
also fractionally.  This removes the multiplicative clique expansion that
caused the 57-GiB run.  This first colour-guard value is existential and is
not exported as an exact OR; physical protection is reconstructed from the
selected reasons.

For a one-solve master there is a still smaller exact encoding.  For every
source tail \(t\), let \(R_t\) be the deduplicated reasons protecting its old
edge and impose

\[
 g_t=\max_{r\in R_t}r,
 \qquad g_t+\widehat c_t\le1,
 \qquad g_t+\sum_{a:\chi(a)=\chi(f_t)}x_a\le1.           \tag{6.8}
\]

Here \(\widehat c_t\) is the scaffold cut at tail \(t\).  Since \(g_t\) is the
Boolean OR of the reasons, (6.8) is exactly equivalent to every original
reason/cut and reason/colour row, and \(g_t\) is safe to export.  It reduces
millions of separate implications to 24,310 guarded ORs.  A multi-round
CEGAR must rebuild these ORs after adding new reasons; the current executable
therefore permits aggregate protection only with one solve.

### 6.7 Exact banked-\(q_1\) coupling and its boundary

The fully coupled one-solve face must also prevent residual ejection from
destroying upper-\(q_1\) coverage.  The frozen source has exactly all

\[
                 \binom{17}{10}=19{,}448
\]

rank-ten adjacent unions.  For each such target \(T\), introduce an exact-one
designation among

* an old source edge \(f\) with endpoint union \(T\), in which case its tail
  is passed through the exact protection guard (6.8); and
* a selected service seam \(a\) with endpoint union \(T\), in which case the
  designation implies \(x_a=1\).

This designation does not assert that only one physical witness survives.
It banks one witness which is guaranteed to survive every subsequent
include-protected residual completion.  Conversely, any surviving old or
selected-seam witness can be designated, so the formulation is exact for the
**banked-\(q_1\) face**.  The chosen old tails and chosen \(q_1\) seams are
exported literally with the candidate.

This face is stronger than unrestricted residual completion: a later
zero-gain/return edge not present in the service catalogue could create a
rank-ten union after all current providers were cut.  If the banked face is
infeasible or only resource-unknown, the weakest semantic relaxation is to
move the rank-ten cover rows into the residual physical-edge recourse.  That
relaxation is no longer the bare ghost max-flow, because it adds one cover row
for every rank-ten union; it must be solved with the topology/directed return
model or by sound Benders separation.  It is not legitimate simply to leave
the chosen \(q_1\) source edge unprotected.

### 6.8 Exact support-antichain scope

There is a second, independent boundary on an UNSAT claim from the current
service master.  For a target \(T\) and selected seam \(a\), let
\(\mathcal P_{T,a}\) be the family of literal old-source tail sets whose
retention makes one suffix/seam/prefix interval witness \(T\).  Compatibility
with a fixed cut/colour bank is monotone under inclusion: if
\(P\subseteq Q\) and \(Q\) is compatible, then \(P\) is compatible.  Hence
one may discard every support which strictly contains another support, but
one may not in general discard incomparable supports merely because one has
larger cardinality.

**Proposition 6.8 (support-antichain reduction).**  The exact literal
selected-support formulation for a fixed service catalogue is obtained by
retaining the inclusion-minimal antichain

\[
 \min_{\subseteq}\mathcal P_{T,a}
\]

for every pair \((T,a)\).  With a variable \(y_{T,a,P}\) for each retained
support, impose

\[
 \sum_{a,P}y_{T,a,P}=1,
 \qquad y_{T,a,P}\le x_a,
 \qquad y_{T,a,P}\le g_t\quad(t\in P).                 \tag{6.9}
\]

This is necessary and sufficient for the banked literal witness face.  The
proof is just monotonicity: any discarded nonminimal support can be replaced
by a contained minimal one, whereas two incomparable supports can be blocked
by different cut or seam-colour choices.

The running active-2,649 producer stores only one minimum-cardinality support
per \((T,a)\).  Every SAT incumbent is therefore sound, because its exported
support is literal.  A proved UNSAT from that executable is scoped to this
canonical-one-support atlas; it is not an UNSAT theorem for the complete
literal service atlas.  The fixed-bank Proposition 6.6 audit is unaffected:
that separate replay enumerates every support form and its 921-target zero
set agrees with the older one-shortest catalogue on that frozen bank.

Finally, both the active-2,649 designations and the banked-\(q_1\) rows are
stronger than unrestricted residual completion.  A later return edge may
itself create a required interval.  The weakest fully unrestricted
relaxation is therefore to put those cover rows on the exact residual
physical-path variables, not to weaken selected-protected-source guards.

### 6.9 Compressed banked-\(q_1\) run: exact status

The compressed one-solve implementation of (6.8), together with all 2,649
active designations, seam-colour injectivity, and the full banked-\(q_1\)
designation, was run on H100 with two workers and an explicit 2,000-CPU-second
limit.  It found no incumbent and produced no solver result or candidate.
The wrapper ended with status 137 after signal 9 at the CPU limit:

\[
 1980.59+22.31=2002.90\ {\rm CPU\ seconds},
 \qquad 17{:}54.45\ {\rm wall}.
\]

Peak RSS was 22,192,176 KiB (about 21.16 GiB), with no swap.  Presolve reduced
1,891,398 initial Boolean variables to 1,836,075 variables and 739,962
constraints.  The exact status is `UNKNOWN_RESOURCE_CPU_LIMIT`, not UNSAT.
In particular, there is no bank on which residual flow, topology, residence,
or literal all-target replay can be run.

The frozen run used producer SHA
`69db8345cdd9205671ef096fe6e03ef4c1e1880cd5102d9b3e9ca7ce25083308`.
That source lacked only the later fail-closed assertion that the source
rank-ten unions equal the whole universe; independent replay of this input
gives all \(19{,}448\) targets.  Its support catalogue nevertheless has the
canonical-one-support scope of Proposition 6.8.

The exact frozen audit is

    scratch/threadD_k17_alltarget_residual_completion_20260731/
        guarded_active2649_q1guard_bflowready_h100/AUDIT.md
      SHA faec67fea0000c4f2fdf3bfb020d6702e995d7ae548ebb3c8f25dd43aeb351ac

with run-log SHA
`cbe33b50c4f6cc5974876d04f6205f2093f96305675b24e2ee606eed6116fea3`
and resource-log SHA
`f0f381144e00a88ce9a9cccb304908d63ae8129cad4ba260074b8a86c0b25a0c`.

## 7. Exact include-protected residual theorem

For the unrestricted Johnson residual catalogue, the strongest polynomial
recourse is sharper than a generic incidence projection.  Fix a valid bank
\(K\) of selected seams plus the old physical edges protected by the
**selected** guards, and fix an omitted colour \(z\notin\chi(K)\).  Contract
the saturated colours \(\chi(K)\), remove \(z\), and add a dummy colour
\(\partial\) of demand two adjacent to every owner.  Owner \(v\) has demand
\(2-\deg_K(v)\); every remaining real colour and \(\partial\) has demand two.
This \(b\)-flow is feasible if and only if, for every owner set \(X\) and
right-shore set \(Y\),

\[
 \sum_{v\in X}(2-\deg_K(v))
 \le 2|Y|+|D_z\cap(X\times(L_z\setminus Y))|.             \tag{7.1}
\]

Two owners chosen at one real colour always determine the unique Johnson
edge having that intersection, so (7.1) is exact for the undirected
degree-cover face.  It automatically ejects an unprotected source edge
whose colour is used by a seam.  A protected source edge of that colour is
already a fatal local bank conflict.

Flow success may contain cycles.  Exact undirected path topology is obtained
by adding the graphic independence rows to the owner and colour partition
systems; direction, collar histories, residence, arbitrary-width upper
coverage, compiler feasibility, and literal verification remain subsequent
gates.  The old balanced-factor solver
`scratch/solve_k17_prescribed_incidence_bflow_20260731.py` is not path-exact:
its SAT result may be cyclic and its UNSAT result need not exclude a path
with a ghost endpoint colour.

The dependency-clean statements and certificate requirements are in

    MATH_THEOREM_K17_INCLUDE_PROTECTED_RESIDUAL_BFLOW_20260731.md
    MATH_AUDIT_K17_GUARDED_RESIDUAL_GHOST_FLOW_AND_LITERAL_PIPELINE_20260731.md

The executable contracted separator is

    scratch/threadD_audit_k17_include_protected_ghost_flow_20260731.py

It now has a fail-closed `--require-banked-q1` mode which replays every one of
the 19,448 exported rank-ten designations before permitting an ejection.  For
the topology lift,

    scratch/threadD_audit_k17_include_protected_hamilton_recourse_20260731.py

adds both orientations of every residual Johnson edge, fixes the directed
bank, enforces one use of every nonomitted lower colour, and uses a boundary
dummy plus `AddCircuit`.  Thus its SAT object is one directed Hamilton path,
not a path plus cycles.  Its independent replay checks the full owner order,
fixed bank, exact lower palette, unprotected ejections, and arbitrary-width
upper coverage.  Residence and the lower compiler remain downstream.  The
corresponding executable SHAs are
`6bc120526a5c366d9a8f775109fbd9357c8430ba7b1adbf4e9d1a0803f0e48b3`
and
`37350ea88c331dd27c7a81e87c9dc1368a319d43d82bcbfc56124589c53e10be`.

## 8. Carrier symmetry is not compiler covariance

The frozen K16 anatomy supplies a necessary modelling separation for K17.
Its odd parent has \(c=2\) cyclic components; the even two-rail lift gives
exactly \(2c=4\) strict spirals, and opening them into one path uses
\(2c-1=3\) physical seams.  This symmetry is real at carrier level.  The
decoded compiler is not correspondingly equivariant: only 6,535 of the
12,870 acted-on positions obey the \(H=\mathbb Z_5\) letter covariance, and
the letter multiset has \(L^1\)-distance 3,148 from its \(H\)-rotation.

**Proposition 8.1 (physical Benders scope).**  Carrier symmetry may be used
to enumerate or compress candidate carrier blocks.  A Benders row returned
by the compiler is proof-valid only after projection onto literal physical
master data: selected physical edges or seams, protected source occurrences,
owner degrees, lower colours, endpoints, pins, and literal target/host
incidences.  No equality or covariance constraint on equivariant compiler
letters follows from carrier symmetry alone.

Indeed, for physical master state \(x\) and compiler variables \(A\), the
relevant projection is

\[
 \mathcal Q=\{x:\exists A\ C(x,A)\}.
\]

Replacing \(A\) by an equivariant subspace produces a smaller auxiliary
projection unless a separate theorem proves equality with \(\mathcal Q\).
Symmetry of \(x\), or of the uncapped envelope, is not such a theorem.  The
K16 certificate is a literal counterexample to the inference “symmetric
carrier implies symmetric selected compiler”: its carrier is organized by
four co-oriented spirals while its successful integral common-cap word spends
that symmetry.

Consequently, an orbit-aggregated cut is allowed only when it is the exact
sum or quotient lift of valid **physical** rows, with all coefficients,
boundary pins, and capacities replayed.  Averaging compiler letters, imposing
letter-orbit equality, or transferring a quotient dual through a noncovariant
pin is invalid.  The present K17 cut schema already obeys this rule: it accepts
only literal seam terms and exact protected-source-tail guards; the residual
separators use physical owner--colour incidences and endpoints.

Term syntax alone is not a provenance proof: an invalid covariance assertion
could be expanded into physical-looking coefficients.  The loader therefore
also replays the cut payload, the physical min-cut audit and service hashes,
the audit payload and physical scope, every fixed-edge support term, and both
sides of the inequality.  A row is loaded only when those data reconstruct it
exactly.  The lightweight regression

    scratch/test_threadD_k17_physical_benders_provenance_20260731.py

accepts two independently audited physical rows with 169 and 263 terms and
rejects a coefficient mutation even after its outer JSON payload is
recomputed.

The frozen anatomy and replay are

    MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md
      SHA 3367a823c8ebdd1b3c0d2b37422ea7fbe151f24bcfe47c0bb8c4c29a071b5c9a
    scratch/k16_three_primary_spiral_braid_anatomy_20260731.audit.json
      SHA 3eac8320442d39fcacf4d0f54c762b83f682bfcbf6e04a20855297f60da78546
      payload b072e033234c8ca6107298d074529f3f1e94e8abb7ede8944aed4d3858f013b6

## 9. Global-matching-first quotient master

The residual-Kneser extension question is no longer an existential gate.
For a clean free subgroup \(H\), the quotient of the complete lower--upper
diamond graph is a balanced regular bipartite multigraph, so it has a perfect
matching.  The exceptional filters must be defined as the restriction of that
global matching, not prescribed beforehand.  When \(v_3(2m-1)=1\), this
restriction automatically gives exactly \(2\operatorname{Cat}_a\) filter
orbits, global extendability, distinct opposite endpoints on each typed shore,
and pairwise-distinct physical middle endpoints.

The typed-shore qualification is essential: after complement-identifying both
shores as one Kneser label space, a lower- and an upper-family opposite label
may coincide.  That auxiliary equality is not a physical palette collision.

The exact matching/forest/closure/voltage master chooses one
occurrence-labelled quotient perfect matching and simultaneously requires its
middle-edge lift to satisfy degree at most two and every graphic forest cut.
The resulting \(\operatorname{Cat}_m/h\) quotient paths are oriented and
closed with literal edge-orbit records; one quotient circuit row enforces a
single contracted cycle, and its total voltage must be a unit modulo \(h\).
A final linear carrier deletes one declared **physical phase occurrence**,
not a whole quotient orbit.

Private sockets are a further physical collar/compiler hypothesis, not a
consequence of the global matching theorem.  Their module is exact only after
an exhaustive refined-atom catalogue is supplied: a refinement replaces,
rather than duplicates, its parent atom's physical resource record, and
exclusive resources receive literal union-capacity or incompatibility rows.
Plain Hall is exact only in the pre-certified disjoint-block specialization.

Thus the surviving gate is Hamilton-compatible structure inside the global
quotient perfect-matching polytope.  It is not residual palette Hall.  The
exact matching/forest/closure/voltage core and the conditional
refined-socket/Benders schema are in

    MATH_REDUCTION_GLOBAL_QUOTIENT_MATCHING_PHYSICAL_FOREST_SOCKET_VOLTAGE_20260731.md

The existing seam-set-cover executable is downstream physical recourse, not
the new quotient master.  It remains useful only after the quotient choice is
expanded to its complete literal lift.  Compilation stays separate and may
break every carrier symmetry.  An incumbent physical min-cut pulls back
unguarded only for orbit-complete atom variables; phase, orientation, socket,
protected-tail, and compiler decisions require explicit master guards or an
exact incumbent no-good.

The global matching theorem is

    MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md

No statement here proves a K17 word or \(\nu(17)=B(17)\).

Every quotient candidate should persist its complete atom-to-physical-lift
map, gains, exceptional representatives, socket resources, and phase-labelled
boundary.  After materialization, every downstream physical candidate should
persist the selected directed seams, physical source cuts including
ejections, chosen witness blocks, physical-edge OR bank \(g\), incidence OR
bank \(\rho\), and endpoint/hole choices (or leave the last two explicitly
variable in recourse).  Installing (3.3)--(3.5) and the separator (4.4)
rejects a genuinely incompatible guard bank while leaving unprotected
source-colour ejections available. Nothing here proves a K17 word or
\(\nu(17)=B(17)\).

## 10. Integral-correlation diagnostics on every incumbent

The current upper-cover objective is now instrumented against the exact
Catalan matching reductions.  For every persisted successor bank the
producer and independent replay compute:

1. rank-eight Johnson edge-colour multiplicities;
2. rank-ten upper-turn multiplicities;
3. rank-seven lower-turn multiplicities at every defined directed triple;
4. path/cycle topology and undefined turn slots;
5. the represented-rail ordered-four-transversal defect; and
6. only for one literal lower-rainbow \({\rm ML}(17)\) Hamilton cycle, the
   exact alternating occurrence-SDR flow.

The last test is the simultaneous residual-cross-edge formulation of the
authoritative gap--Hall theorem.  Fixing the upper representatives gives
the gap-vs-lower-colour perfect-matching instance.  Leaving both sides
variable gives one integral network with colour demands
\(c_U-1,c_L-1\); a flow of value

\[
\binom{17}{9}-\binom{17}{10}=4862
\]

is equivalent to alternating representatives.  The frozen
\({\rm ML}(7)\) counterexample replays as flow \(13/14\), agreeing with
the exhaustive best fixed-upper gap matching \(20/21\).  One standard
incidence-hexagon toggle repairs that same cycle and replays as (14/14),
with a spanning \(\operatorname{Cat}_4=14\)-path decoration.  Thus both turn
surjections remain only necessary, but the first obstruction is movable.

The recursive state is now exact: choose the alternating SDR jointly with a
transparent gluing tree.  A fixed decoration crosses a hex toggle exactly
when its selected local turn-colour multisets agree separately on both
shores and the selected boundary types of the retained fragments alternate
after reconnection.  The (m=4) census has 31 alternating hexes, 16
Hamilton outputs, 10 decorable outputs, and 6 outputs sharing a fixed forest
decoration with the source.  Consequently neither an arbitrary frozen SDR
nor an arbitrary published gluing tree is a valid recursive invariant.

The finite K17 signal is already sharp.  The source 11-cycle factor has
zero rank-ten turn holes but 3826 rank-seven turn holes.  The persisted
hard361, hard323, quick650, soft437, and active2649 banks also have zero
rank-ten holes but respectively

\[
4411,\ 4442,\ 4611,\ 4442,\ 4929
\]

rank-seven holes.  None reaches gap--Hall.  Even after every currently
undefined turn slot is filled, retaining all defined turns would still
require respectively

\[
3173,\ 3176,\ 2800,\ 3037,\ 2671
\]

defined turn positions to change.  These are fixed-internal-turn
obstructions, not unrestricted edit-distance bounds.

Current seam JSONs contain only the old-only rank-nine rail, so the direct
four-transversal ledger is explicitly partial; the infinity and cross rails
must be exported as typed \((L,U,T,H)\) atoms before a complete PASS is
possible.  Conversely an arbitrary complete four-transversal is not called
middle-levels-resolvable without its Hamilton-extension certificate.

The reduction, implementation, exact finite table, and scope are frozen in

    MATH_AUDIT_THREAD_D_K17_INTEGRAL_CORRELATION_AND_GAP_HALL_20260731.md

Every successful future Hamilton-flow audit exports the literal occurrence
witness, not only its hash.  Transparent toggles must then be checked on the
expanded bipartite middle-levels factor, because the three changed incidence
half-edges can reverse retained fragments; a Johnson-successor delta alone
does not certify boundary alternation.

No retracted Greene--Kleitman \(W/2\) linear-subforest bound is used.
