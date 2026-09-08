# `k=17` R2: synchronized common master at `ae88fc0b...`

Date: 2026-08-01  
Lane: R2 / common attachment-state matching  
Status: exact theorem and read-only audit rebase; no new finite search and no
minimum-support witness

## 0. Result and exact boundary

The frozen rooted flag factor is

```text
scratch/laneK_k17_commonfirst_serial_20260801/
  common_serial02_4213_seed20260801.final_rows.tsv
SHA256 ae88fc0b489a5b436ca3c2fe10462d80a18aed6cec8e03df871d5abe96561beb
```

Its independently rebuilt lower chronology and common-live projection are

```text
roots / owners / attachment states                 1430 / 1430 / 12870
loop-free packet turns / labelled state arcs                2244 / 17952
packet matching / zero-out / zero-in                       1171 / 42 / 216
both-live root-owner incidences                                  1929
common both-live matching / deficiency                         1141 / 289
canonical Hall root shore / owner neighbourhood                 306 / 17.
```

The exact Dulmage--Mendelsohn regions of the common-live graph have sizes

\[
\begin{array}{c|rr}
 &\text{roots}&\text{owners}\\ \hline
\mathrm{PLUS}&306&17\\
\mathrm{CORE}&1011&1011\\
\mathrm{MINUS}&113&402.
\end{array}                                                    \tag{0.1}
\]

There is an exact two-level common master around this factor.

1. Palette-neutral rooted circuits choose the complete final flag at every
   root.  Literal option-labelled attachment states and transition arcs are
   then activated from the aggregate final flag table, not by adding
   per-circuit gains.
2. A first bipartite matching selects states simultaneously by root and
   attachment owner.  A second bipartite matching selects literal transitions
   between those same states.  Eliminating the second matching gives the exact
   max-closure/Benders family

   \[
      \boxed{M+x(X)-x(\Gamma^+(X))\le1430
             \qquad(X\subseteq\Omega).}                       \tag{0.2}
   \]

At `M=1430`, (0.2) is Hall's theorem for a directed state cycle cover.
It is not merely the frozen `1141` common-live projection.  The latter is a
necessary outer relaxation and supplies exact DM pricing cuts.

The tight-shore structure can be stated without enumerating every shore.
The minimal deficiency-289 shore is `306 -> 17`; the maximal one is
`1317 -> 1028`.  A single added common incidence crosses every current
deficiency-289 shore if and only if it goes from a DM-PLUS root to a
DM-MINUS owner.  For several addition-only incidences, the equivalent
condition is a new PLUS-to-MINUS path in the old residual DM condensation.

This does **not** certify a smallest rooted-circuit support.  One incidence is
the graph-theoretic minimum, and a unary neutral circuit could in principle
realize it.  The frozen source-relative catalogue contains `2545` unary and
`215304` indecomposable binary circuits, but its recorded selector is a
heuristic audit rather than an independently certified bounded-support
decision proof.  A jointly useful pair of unary moves also remains possible.
Thus support three is only the first unsearched **primitive** circuit arity;
it is not a proved minimum and no support-three witness is claimed here.

Even a perfect common transversal would still omit connected topology,
voltage, upper rows, opening, residence beyond the declared rooted recurrence,
and the compiler.

## 1. Palette-neutral circuit layer

Let `P` be the 1,430 roots.  The incumbent flag at root `q` is `f_q^0`.
For a literal flag `f` at `q`, let

\[
 r_q(f)\in\mathbb Z^{\mathcal K}                         \tag{1.1}
\]

be its complete exact type/lower-target resource vector.  The same rank-six
target uses the same coordinate whether it is the inner or outer member of
the nested flag.  Put

\[
             \partial_q(f)=r_q(f)-r_q(f_q^0).            \tag{1.2}
\]

A rooted circuit `c` consists of distinct roots `S(c)` and one nonincumbent
literal flag `f_q^c` on each root in its support, with

\[
             \sum_{q\in S(c)}\partial_q(f_q^c)=0.         \tag{1.3}
\]

Thus every circuit preserves all type masses and every tight lower target.
Fix any declared finite circuit bank `C`.  The theorem permits arbitrary
support sizes; the current unary/binary catalogue is only one possible bank.
For a root-disjoint packet use binary `z_c` and impose

\[
             \sum_{c:q\in S(c)}z_c\le1\qquad(q\in P).     \tag{1.4}
\]

Let `p_qf` choose the final flag.  The exact channels are

\[
 p_{qf_q^0}=1-\sum_{c:q\in S(c)}z_c,                     \tag{1.5}
\]

and, for `f != f_q^0`,

\[
 p_{qf}=\sum_{\substack{c:q\in S(c)\\f_q^c=f}}z_c.       \tag{1.6}
\]

Hence `sum_f p_qf=1`.  Retaining the redundant audit rows

\[
       \sum_{q,f}r_{qj}(f)p_{qf}=b_j\qquad(j\in\mathcal K) \tag{1.7}
\]

is proof-safe: (1.3)--(1.6) imply them, while a mismatch detects a bad
catalogue, channel, or rank-six-role convention.

The root-conflict rows alone are not an integral LP description of a general
circuit multigraph.  The variables remain binary; for support at most two,
an LP implementation also needs the ordinary blossom inequalities.  The raw
flag/resource matrix is likewise not totally unimodular.

## 2. Literal activation and the common-live outer matching

Let `Omega` be the option-labelled aligned attachment states

\[
       s=(q,f,o,a,\sigma),                              \tag{2.1}
\]

where `q` is the root, `f` is a complete flag option at `q`, `o` is the
rank-nine attachment-owner orbit, and `(a,sigma)` records the literal aligned
incidence.  Let `A` be the complete option-labelled literal transition
multiset.  Because flag identity is part of a state, this universe is fixed
before circuit selection.

For every literal arc `alpha=(s,t)`, let `c_alpha` say that its two endpoint
flags are final.  The exact Boolean conjunction is

\[
\begin{aligned}
 c_\alpha&\le p_{\operatorname{root}(s),f(s)},\\
 c_\alpha&\le p_{\operatorname{root}(t),f(t)},\\
 c_\alpha&\ge
 p_{\operatorname{root}(s),f(s)}+
 p_{\operatorname{root}(t),f(t)}-1.
\end{aligned}                                                \tag{2.2}
\]

Define exact outgoing, incoming, and both-live bits

\[
 \ell_s^+=\bigvee_{\alpha:\operatorname{tail}\alpha=s}c_\alpha,
 \qquad
 \ell_s^-=\bigvee_{\alpha:\operatorname{head}\alpha=s}c_\alpha,
 \qquad
 b_s=\ell_s^+\wedge\ell_s^-.                             \tag{2.3}
\]

The standard OR/AND linearizations are exact for binary variables.  If more
than one state column can project to the same root-owner pair, define

\[
 e_{qo}=\bigvee_{s:\operatorname{root}(s)=q,
                       \operatorname{owner}(s)=o}b_s.       \tag{2.4}
\]

For the frozen ae88 table the 1,929 both-live states project without
duplicates, but (2.4) is the safe general definition.

For a root set `R` and owner `o`, let

\[
 n_{R,o}=\bigvee_{q\in R}e_{qo}.                         \tag{2.5}
\]

If `C` denotes the maximum common-live root-owner matching, its exact Hall
epigraph is

\[
 C+|R|-\sum_o n_{R,o}\le1430
            \qquad(R\subseteq P).                       \tag{2.6}
\]

For a fixed circuit incumbent, a root-owner maximum matching and alternating
reachability separate (2.6).  At the frozen table the canonical row is

\[
                    C+306-17\le1430,                     \tag{2.7}
\]

so `C <= 1141`.  This is the precise use of the authenticated `306 -> 17`
shore.  It is not frozen as a universal sufficient cut: after a circuit
packet, the matching and DM decomposition must be rebuilt.

Equivalently, one may retain common-state matching variables `w_s` with

\[
 w_s\le b_s,qquad
 \sum_{s:\operatorname{root}(s)=q}w_s\le1,qquad
 \sum_{s:\operatorname{owner}(s)=o}w_s\le1,qquad
 C=\sum_sw_s.                                             \tag{2.8}
\]

For fixed liveness bits this is an integral bipartite matching problem.
Equations (1.4)--(2.8) therefore select palette-neutral circuits and a
common attachment-state matching jointly.

## 3. Full common state transversal and exact transition recourse

To seek a complete occurrence-state object, use binary `x_s` and impose

\[
 \sum_{s:\operatorname{root}(s)=q,\ f(s)=f}x_s=p_{qf}
                    \qquad(q\in P,f),                       \tag{3.1}
\]

\[
 \sum_{s:\operatorname{owner}(s)=o}x_s=1
                    \qquad(o\in O),                         \tag{3.2}
\]

and optionally the redundant live gate `x_s <= b_s`.  Summing (3.1) over
flags gives one selected state at every root; (3.2) gives one at every owner.
Thus

\[
                         x(\Omega)=1430.                    \tag{3.3}
\]

For a state family `X`, define the fixed literal head neighbourhood

\[
 \Gamma^+(X)={t\in\Omega:
          \text{some }s\in X\text{ has }(s,t)\in\mathcal A\}. \tag{3.4}
\]

For fixed `x`, the transition subproblem is

\[
 \max\sum_{\alpha\in\mathcal A}y_\alpha                 \tag{3.5}
\]

subject to

\[
 \sum_{\alpha:\operatorname{tail}\alpha=s}y_\alpha\le x_s,
 \qquad
 \sum_{\alpha:\operatorname{head}\alpha=t}y_\alpha\le x_t,
 \qquad y_\alpha\ge0.                                  \tag{3.6}
\]

Every arc whose endpoint flag is not final has a zero endpoint capacity, so
an extra `y_alpha <= c_alpha` is redundant but useful as a defensive check.
For fixed integral `x`, (3.5)--(3.6) is an integral bipartite matching.

### Theorem 3.1 (exact max-closure common master)

Let `mu(x)` be the optimum of (3.5)--(3.6).  Then

\[
 \boxed{
 \mu(x)=1430-
   \max_{X\subseteq\Omega}
      \bigl(x(X)-x(\Gamma^+(X))\bigr).}                  \tag{3.7}
\]

Consequently maximizing `M` subject to

\[
 \boxed{
 M+x(X)-x(\Gamma^+(X))\le1430
       \qquad(X\subseteq\Omega)}                         \tag{3.8}
\]

is exactly equivalent to retaining the transition matching subproblem.
At `M=1430`, the selected states admit one incoming and one outgoing literal
transition each.

#### Proof

Let `Z={s:x_s=1}`.  For `X subset Z`, the selected head neighbourhood is
`Gamma+(X) intersect Z`, whose cardinality is `x(Gamma+(X))`.  Hall's
deficiency form therefore gives

\[
 \mu(x)=1430-
  \max_{X\subseteq Z}
       \bigl(|X|-|\Gamma^+(X)\cap Z|\bigr).               \tag{3.9}
\]

For arbitrary `X subset Omega`, put `X'=X intersect Z`.  Then
`x(X)=|X'|` and `Gamma+(X') subset Gamma+(X)`, so

\[
 x(X)-x(\Gamma^+(X))
 \le |X'|-|\Gamma^+(X')\cap Z|.                          \tag{3.10}
\]

Thus allowing all `X subset Omega` does not enlarge the maximum beyond the
selected subsets, while selected subsets are already included.  Equations
(3.7)--(3.8) follow.  At `M=1430` every one of the 1,430 tail and head
capacities is saturated, giving the claimed directed cycle cover.  \(\square\)

Under the established state-arc convention, a selected arc pairs its tail
root with the attachment-owner orbit of its head state.  One saturated tail
at every root and one saturated head at every selected owner therefore make
the induced `H` incidence perfect as well.

The cycle cover may have many quotient components and zero voltage.  No
Hamiltonicity or physical lift follows from Theorem 3.1.

## 4. Proof-safe min-cut/Benders separation

For a master incumbent `(z,p,x,M)`, separate (3.8) by the network

```text
source -> tail state s       capacity x_s
tail s -> head t             capacity 1431 for every literal arc s -> t
head state t -> sink         capacity x_t.
```

Capacity `1431` is safely larger than the total positive state weight.  If
the source side contains tail family `X`, closure forces every member of
`Gamma+(X)` onto the source side.  Hence

\[
 \max_X\bigl(x(X)-x(\Gamma^+(X))\bigr)
          =1430-\operatorname{mincut}.                    \tag{4.1}
\]

A row is violated exactly when `M` exceeds this min-cut value.  The
source-side tail family yields the Benders row (3.8).  For integral `x`, the
same certificate is obtained from a maximum transition matching followed by
alternating reachability.

The complete fail-closed order is therefore:

1. solve the binary circuit/final-flag master;
2. rebuild all option-pair transition activation and state liveness;
3. separate the common-live root-owner matching (2.6);
4. select one state per root and owner by (3.1)--(3.2);
5. separate (3.8) by max closure/min cut;
6. at `M=1430`, materialize and independently replay the 1,430 transition
   matching arcs.

The two matching subproblems are integral separately.  Their correlation
with binary circuit and flag selection is not thereby integral; the outer
variables must remain binary.

The fixed-neighbourhood rows (3.8) are globally valid only because states
and arcs are option-labelled over the complete declared menu.  A cut built
from an incumbent-only arc set is not valid after column generation unless
it is guarded or lifted to the expanded option universe.

## 5. The complete current tight-shore lattice

Fix a maximum matching of the frozen common-live graph `G_0`.  Contract its
matching edges, keep unmatched vertices as singleton atoms, orient every
unmatched incidence root-to-owner, and contract strongly connected
components.  In this DM condensation, a maximum-deficiency Hall shore is a
forward-closed component family which contains every PLUS component, contains
no MINUS component, and makes an arbitrary closure-compatible choice of CORE
components.

For ae88, the PLUS components total `306/17`, the CORE components total
`1011/1011`, and the MINUS components total `113/402`.  It follows that the
minimal and maximal deficiency-289 shores are

\[
 (P_{\min},N_0(P_{\min}))=(P^+,O^+),
       \qquad |P_{\min}|/|N_0(P_{\min})|=306/17,           \tag{5.1}
\]

and

\[
 (P_{\max},N_0(P_{\max}))
   =(P\setminus P^-,O\setminus O^-),
       \qquad |P_{\max}|/|N_0(P_{\max})|=1317/1028.       \tag{5.2}
\]

### Theorem 5.1 (one-incidence all-tight-shore crossing)

An added common-live incidence `e=(q,o)` crosses every current
deficiency-289 shore if and only if

\[
                         q\in P^+,qquad o\in O^-.          \tag{5.3}
\]

#### Proof

Every tight shore contains the minimal left shore `P+`, and every tight
neighbourhood is contained in the maximal neighbourhood `O minus O-`.
Therefore (5.3) puts the tail inside every tight shore and its head outside
every tight neighbourhood, proving sufficiency.

Conversely, crossing the minimal shore forces the tail into `P+`.  Crossing
the maximal shore forces the head outside `O minus O-`, hence into `O-`.
This proves necessity.  \(\square\)

The same statement is the usual DM augmenting-path criterion: adding
`P+ -> O-` joins an alternating path from an unmatched root to an alternating
path ending at an unmatched owner.  A set of addition-only incidences crosses
every current tight shore exactly when the augmented old residual
condensation contains a PLUS-to-MINUS path.

## 6. Deletions, near-tight shores, and the exact gain condition

A rooted circuit changes complete endpoint flags.  It can both create and
delete transition witnesses; a common-live incidence can change even at an
unchanged root when its last incoming or outgoing witness touches a changed
root.  Thus a PLUS-to-MINUS added incidence is only an optimistic filter for
a circuit packet.

For every root set `R`, put

\[
 d_0(R)=|R|-|N_0(R)|,qquad
 \kappa_C(R)=|N_C(R)|-|N_0(R)|,                        \tag{6.1}
\]

where `G_C` is the fully rebuilt final common-live graph.  Hall's theorem
gives, for every integer `t >= 0`,

\[
 \boxed{
 \nu(G_C)\ge1141+t
 \quad\Longleftrightarrow\quad
 \kappa_C(R)\ge d_0(R)-289+t
       \quad\text{for every }R\subseteq P.}              \tag{6.2}
\]

In particular, a genuine first gain requires

\[
                  \kappa_C(R)\ge d_0(R)-288
                         \qquad(R\subseteq P).             \tag{6.3}
\]

Hence every old deficiency-289 shore must gain at least one **net distinct
owner**, every deficiency-288 shore may suffer no net loss, and all other
shores retain their corresponding allowance.  A fresh maximum matching and
alternating min cut in `G_C` is an exact separator for (6.3).  Testing only
the frozen `306 -> 17` shore is not sufficient.

## 7. What “smallest support” means here

Define changed-root support relative to ae88 by

\[
 \sigma(F)=|\{q:f_q\ne f_q^0\}|.                       \tag{7.1}
\]

There are three different minima which must not be conflated.

1. **Incidence minimum.** One new `P+ -> O-` common incidence is necessary
   and sufficient in the addition-only graph problem.  This minimum is one
   edge, not a claim about how many flags must change.
2. **Primitive circuit arity.** The ae88 catalogue has `2545` unary and
   `215304` indecomposable binary circuits.  Its selector log reports no
   individually improving common-primary move and then chooses two binary
   secondary moves, but the frozen status is heuristic and supplies no
   independent rejected-candidate proof.  Primitive support three is the
   next catalogue class, characterized by three nonzero resource deltas

   \[
                         v_1+v_2+v_3=0.                    \tag{7.2}
   \]

   It is the first unsearched primitive arity, not a witnessed or proved
   minimum.
3. **Total packet support.** Two unary circuits can be jointly useful because
   one may activate the last incoming witness and the other the last outgoing
   witness of the same crossing state.  Thus total support two remains open
   even if every single unary and binary atom is neutral.  In a fully
   proof-safe decision sequence, support one must also be independently
   closed rather than inferred from a heuristic ranking pass.

Therefore the only unconditional rooted-circuit lower bound currently frozen
is the trivial `sigma >= 1` for a nonidentity repair.  No successful minimum
support is identified by the existing artifacts.

An exact minimum-support decision uses changed-root binaries

\[
 d_q=1-p_{qf_q^0},qquad \sum_qd_q\le s,                \tag{7.3}
\]

the complete resource rows, literal activation (2.2)--(2.4), and either:

* target `C >= 1142` with exact common matching separation, to certify a
  first common-live gain; or
* target `M=1430` with the full state master (3.1)--(3.8), to certify a
  common root/owner/`H` cycle cover.

A minimum `s` requires both an independently replayed witness at `s` and a
proof of infeasibility for every smaller bound, for example checked SAT/DRAT
or a complete branch-and-cut certificate.  One Hall shore or one heuristic
empty sweep cannot certify this minimum.

## 8. Exact audit protocol and scope

A positive common-master artifact must freeze:

1. the source factor, declared circuit/flag menu, state universe, arc universe,
   loop convention, and all hashes;
2. every selected circuit, its changed roots, literal options, exact delta
   vector hash, zero-sum check, and root-conflict check;
3. the byte-exact final row table and redundant type/lower-target replay;
4. the selected 1,430 state IDs with flag, root, owner, attachment, and phase;
5. either the materialized 1,430 transition arcs, or a maximum matching and
   alternating Hall/min-cut witness with sorted identifier hashes; and
6. for a minimum claim, a separately checkable infeasibility certificate at
   every smaller support bound.

The present theorem freezes no new positive solution.  It proves the exact
master, the exact separation oracle, the ae88 tight-shore/DM structure, and
the honest minimum-support boundary only.

Explicitly excluded are connected quotient topology, voltage, upper rows,
opening, residence outside the declared rooted age recurrence, source-word
chronology beyond the literal state arcs, and the compiler.  A perfect
common-live root-owner matching alone would not even prove compatible
statewise flow.  A perfect `M=1430` witness for (3.8) would prove a directed
state cycle cover, but none of the excluded downstream properties.

## 9. Frozen read-only inputs

```text
scratch/laneK_k17_commonfirst_serial_20260801/
  common_serial02_4213_seed20260801.final_rows.tsv
    ae88fc0b489a5b436ca3c2fe10462d80a18aed6cec8e03df871d5abe96561beb
  common_serial02.owner_demand.independent.audit.json
    5d64e638e21b1e51d523b6428f98be65d8cb9b849b96d5d7c94cfc043a57b4eb
  common_serial02.common_live_dm.independent.audit.json
    fa9ccc19049efbe94468b16a0cda6a4eb4205fbd3454b82f2637084a7e51c87b
  common_serial02_ae88.common_state_dm_o3.audit.json
    55951bf1c64ab6bd4d65aef231b0879f3614d32e68db499f89120349bdcf852a
  common_serial02_ae88.common_state_dm_o3.cut.tsv
    2da82e87a19ef9c167c11aa76bc08ac4a66a871f31d0ffcb58a24b1f617c6949
  common_serial02_ae88.common_state_dm_o3.components.tsv
    c64d351e509caad5a93a99a28caa6bf2f6713528b3174bbd0b65c9695a2069f0
  common_serial03_ae88_seed20260801.catalogue.tsv
    28ee08bdcac1f654694aca842288dccf74a9f6dcb67b676119a71713a229ce8b
  common_serial03_ae88_seed20260801.audit.json
    8f2e57271a2102cf0818d6e5f38bd4465e87d5dbb0ae1930ed52901352a452c3

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  serial_chain_ae88fc.support12_counts.audit.json
    998a21c5af85dc16899775fd9a265b2460878dd38ed00bf830da7fcd3596fdba
```

The O3 DM components file freezes SCC sizes and regions, not vertex-to-SCC
membership or condensation arcs.  The full tight-shore theorem above follows
from DM theory and the certified region totals; a future finite
minimum-support certificate must additionally freeze the rebuilt condensation
or an equivalent sequence of matching/min-cut transcripts.
