# K16 fixed75 at count 106: residual-31 normal form and exact portal blocks

> **Subsequent authoritative update (2026-07-30).** The marked price-four
> closed-walk theorem now eliminates all 1,024 profiles on this exact face and
> proves the fixed-`F75` conditioned floor 107. The authoritative closure is
> `MATH_THEOREM_L_K16_FIXED75_CONDITIONED_FLOOR107_PRICE4_CLOSED_WALK_20260730.md`.
> This note remains the exact residual-atlas and portal-block reduction.

Date: 2026-07-30

## 0. Verdict and scope

Retaining the authenticated D4 fixed75 block reduces a count-106
service-plus-balance solution to a balanced capacity-one packet of exactly 31
seams.  Its exact direct-dual ledger is

\[
                         Q+R=5,                         \tag{0.1}
\]

where \(Q\) is repeated target price and \(R\) is total seam slack.

The authenticated five-lock theorem reduces all equality cases to exactly

\[
                         4^5=1024                       \tag{0.2}
\]

normal forms.  In each of five price-one lock triples one chooses either one
slack symbol or one of the three targets to repeat.  This is an exact theorem,
not a search heuristic.

An exact portal-block characterization is also proved below.  It reduces each
normal form to a finite vertex-disjoint cycle-block exact-cover problem.  The
old individual tight-return test remains exact only for a cycle having one
positive-slack portal.  For multiple portals the correct replacement is a
cyclic chain of tight paths, or equivalently a bounded-slack return test.

No count-106 packet is constructed or excluded here.  The seam-level model is
implemented, but a solver `INFEASIBLE` status is not promoted to a theorem
without a checked proof or an exhaustive solver-free block audit.  Any positive
packet still certifies only the reduced service/balance/capacity system until
the physical separation, q1, residence, all-depth, and compiler rows are
independently replayed.

## 1. Frozen data

For a seam \(e:u\to v\), let \(H(e)\) be its frozen target set.  The exact
scale-two certificate supplies

\[
 b_t\in\{1,2,4\},\qquad \sum_t b_t=207,
\]

an integral port potential \(y\), and nonnegative integral slack

\[
 s(e)=2+y_v-y_u-\sum_{t\in H(e)}b_t.                  \tag{1.1}
\]

The D4 audit proves that the named fixed block \(E_0\) is a tight balanced
capacity-one union of

\[
                         3C_{15}+C_{30}.               \tag{1.2}
\]

It contains 75 seams on 75 ports and services 60 targets exactly once, with
price histogram

\[
                         45\cdot2+15\cdot4=150.        \tag{1.3}
\]

The complementary 33 targets have histogram

\[
                         15\cdot1+15\cdot2+3\cdot4    \tag{1.4}
\]

and total price 57.  In particular all fifteen price-one targets remain in
the residual shore.

The five authenticated lock triples are

\[
\begin{aligned}
T_0&=\{35044,36935,40066\},\\
T_1&=\{37320,41102,47364\},\\
T_2&=\{33906,36417,51235\},\\
T_3&=\{33337,50976,58385\},\\
T_4&=\{41872,49436,61960\}.
\end{aligned}                                         \tag{1.5}
\]

They partition exactly the residual price-one targets.

## 2. Exact residual-31 reduction

### Theorem 2.1 (fixed75 residual equivalence)

Let \(X\) be a binary balanced port-capacity-one selection of 106 seams that
contains \(E_0\) and services all 93 targets.  Then

\[
                         P:=X\setminus E_0             \tag{2.1}
\]

is a binary balanced capacity-one selection of 31 seams, uses no fixed port,
and satisfies \(Q(P)+R(P)=5\).

Conversely, if a 31-seam packet \(P\) is balanced, capacity one, disjoint from
the fixed ports, and has one of the exact target/slack profiles in Theorem 3.1,
then \(E_0\cup P\) is a reduced count-106 service/balance/capacity witness.

#### Proof

The fixed block is balanced, so subtracting it preserves balance.  Since it
already has capacity one on 75 ports, capacity one of the union forces \(P\)
off those ports.  Its cardinality is \(106-75=31\).

For the combined balanced selection the potential in (1.1) telescopes:

\[
 212=2\cdot106=\sum_t b_t\mu_t+\sum_e s(e)x_e
               =207+Q+R.                              \tag{2.2}
\]

Thus \(Q+R=5\).  Conversely the fixed block is tight and services its 60
targets once.  A residual profile from Theorem 3.1 services every other
target with precisely the declared repeats, hits no fixed target, and has
the declared slack.  Balance, capacity, service, and count therefore hold for
the union.  QED.

Equivalently, on the packet alone,

\[
 2|P|=62=57+Q(P)+R(P).                                \tag{2.3}
\]

## 3. The exact \(4^5\) normal form

For a balanced circulation \(Z\), define its five-lock syndrome

\[
 \sigma_j(Z)=\sum_e |H(e)\cap T_j|Z_e\pmod2.          \tag{3.1}
\]

Servicing every target once gives the baseline syndrome `11111`, because
each \(T_j\) has size three.  An extra occurrence of a target in \(T_j\)
toggles bit \(j\).  Price-two and price-four repeats toggle no lock bit.

The authenticated closed-walk automaton proves, even for arbitrary splitting
into nonnegative circulations and with capacity omitted, that for
\(0\le R\le3\) the attainable syndrome set is exactly

\[
 \mathcal S_R=\{z\in\mathbb F_2^5:|z|\le R,
                         \ |z|\equiv R\pmod2\}.        \tag{3.2}
\]

The fixed block is tight and meets no lock target, so (3.2) applies unchanged
to the residual packet.

### Theorem 3.1 (complete integral count-106 normal form)

Every count-106 equality profile is encoded uniquely by a word

\[
                         \alpha\in\{S,0,1,2\}^5.       \tag{3.3}
\]

At coordinate \(j\):

* `S` contributes one unit to the scalar total slack;
* digit \(a\in\{0,1,2\}\) repeats target \(T_j[a]\) exactly once.

Thus

\[
 R(\alpha)=|\{j:\alpha_j=S\}|,
 \qquad Q(\alpha)=5-R(\alpha),                         \tag{3.4}
\]

all nondeclared targets occur exactly once, and no fixed-block target is hit
by the residual packet.

The number of profiles with slack \(R\) is

\[
 \binom5R3^{5-R},                                      \tag{3.5}
\]

giving the exact census

```text
R          0    1    2   3   4  5
profiles 243  405  270  90  15  1
```

and total 1024.

#### Proof

For \(R=3\), equation (0.1) gives \(Q=2\).  A price-two repeat, two extra
copies of one price-one target, or two price-one repeats from one lock leaves
syndrome weight five.  This is outside \(\mathcal S_3\).  Repeats in two
distinct locks give syndrome weight three and are the only possibility.

For \(R=2\), \(Q=3\).  A price-two repeat plus a price-one repeat gives
syndrome weight four.  Three price-one repeat units give an allowed syndrome
only when they toggle three distinct locks, producing weight two.  Hence
exactly one target is repeated in each of three distinct locks.

For \(R=1\), \(Q=4\).  A price-four repeat, two price-two repeats, or a
price-two repeat plus two price-one units toggles at most two locks and leaves
syndrome weight at least three.  The shell \(\mathcal S_1\) contains only the
five unit vectors.  Therefore four distinct locks are toggled, once each.

For \(R=0\), \(Q=5\) and \(\mathcal S_0=\{00000\}\).  Turning baseline
`11111` into zero needs an odd price-one repeat count in every lock.  Five
units of repeat price force exactly one in each lock.

For \(R=4\), arithmetic alone gives \(Q=1\), hence one price-one target is
repeated.  For \(R=5\), \(Q=0\), hence service is exact.  These six cases are
precisely (3.3)--(3.4), and the repeated targets determine the digits
uniquely.  Equation (3.5) and the displayed census follow.  QED.

The `S` symbols are bookkeeping symbols for scalar slack.  They do **not**
assign slack units to particular seams or locks.  For example a profile with
three `S` symbols permits one slack-three portal, a slack-two plus a slack-one
portal, or three slack-one portals.

This is an integral multiplicity theorem.  It does not decompose the
fractional count-106 polytope into 1,024 faces: fractional target repeats need
not choose one digit in each nonslack lock.

## 4. Exact seam-level model on one normal-form face

Fix \(\alpha\), put \(R=R(\alpha)\), and define the exact residual demand

\[
 d_\alpha(t)=
 \begin{cases}
 2,&t\text{ is the target selected by a digit of }\alpha,\\
 1,&t\text{ is any other residual target}.
 \end{cases}                                           \tag{4.1}
\]

Delete every seam touching a fixed port, every seam hitting a target already
serviced by \(E_0\), and every seam with slack exceeding \(R\).  On the
remaining bank the exact face is

\[
\begin{aligned}
x_e&\in\{0,1\},\\
\sum_{e\in\delta^+(v)}x_e&=\sum_{e\in\delta^-(v)}x_e\le1&&\text{for every port }v,\\
\sum_e x_e&=31,\\
\sum_{e:t\in H(e)}x_e&=d_\alpha(t)&&\text{for every residual target }t,\\
\sum_e s(e)x_e&=R.                                    \tag{4.2}
\end{aligned}
\]

The last row follows from the preceding rows and (1.1), but retaining it is
a useful fail-closed replay check.  The bank deletion and the cyclic-SCC
deletion are exact: every positive edge of a finite balanced digraph lies on
a directed cycle.

The H100-only driver

```text
scratch/solve_k16_fixed75_residual30_packet_20260730.py
SHA-256 97bf7795c696c9e99092fd33fdd58ff2bfeb32d384da4719dee2541967c4ec57
```

now implements (4.2).  Despite its historical filename, the v3 schema accepts
`--combined-count 106` and requires one exact `--normal-form`.  For example:

```text
python3 scratch/solve_k16_fixed75_residual30_packet_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json \
  --fixed-audit scratch/l_k16_d4_cycle_blocks_20260730.audit.json \
  --combined-count 106 --normal-form SSS01 \
  --slack-total 3 --slack-pattern any \
  --seconds 300 --workers 1 --output NEW.json
```

`--slack-pattern any` is exhaustive for the profile.  A digit string such as
`21` may instead restrict the positive seam slacks to a named partition for
diagnosis.  Such restricted runs must not be mistaken for the whole profile.

## 5. Portal blocks

Let \(G_0\) be the directed graph of allowed tight seams on the unfixed ports.
A seam of positive slack is called a portal.

### Lemma 5.1 (cycle decomposition with portals)

Every feasible packet in (4.2) is a vertex-disjoint union of directed simple
cycles.  Each selected cycle is exactly one of the following.

1. A tight simple cycle in one strongly connected component of \(G_0\).
2. A portal block
   \[
    e_1P_1e_2P_2\cdots e_pP_p,                         \tag{5.1}
   \]
   where \(1\le p\le R\), the \(e_i:u_i\to v_i\) are positive-slack
   portals in cyclic order, and \(P_i\) is a tight directed path from
   \(v_i\) to \(u_{i+1}\), indices modulo \(p\).  Zero-length paths are
   allowed.  All ports in the concatenation are distinct except for the
   closing endpoint, and
   \[
                         \sum_{i=1}^p s(e_i)            \tag{5.2}
   \]
   is the slack of the block.

Conversely, any vertex-disjoint family of objects of types 1 and 2 is a
balanced capacity-one packet.

#### Proof

Balance plus outdegree at most one makes every nonempty connected component
of the selected residual digraph a directed simple cycle (a loop is a
one-cycle).  Removing the positive-slack edges of one cycle leaves the tight
paths in (5.1).  Since every portal has positive integral slack, their number
is at most the total slack.  The converse follows by concatenation and
vertex-disjoint union.  QED.

Compress the tight SCCs.  Tight edges between SCCs form a DAG.  Two portals
\(e,f\) can be consecutive only if the SCC of the head of \(e\) reaches the
SCC of the tail of \(f\) in this DAG.  Thus every portal block projects to a
directed cycle in the portal-compatibility relation.

For one portal, this says exactly that its head has a tight return path to its
tail.  This is the old 107-portal pruning theorem.  With two or more portals,
an individual portal need not have a tight return path: the other portals may
cross the missing SCC cuts.  Applying the one-portal test separately in such
a branch is unsound.

### Lemma 5.2 (bounded-slack return criterion)

Let \(\delta_R(a,b)\) be the minimum total positive slack of a directed walk
from \(a\) to \(b\), truncated at \(R+1\).  An allowed seam
\(e:u\to v\) lies on some directed closed walk of total slack at most \(R\)
if and only if

\[
                         s(e)+\delta_R(v,u)\le R.       \tag{5.3}
\]

Consequently every seam violating (5.3) may be deleted from (4.2).  At
\(R=1\), for a slack-one seam, (5.3) is precisely the tight-return test.

#### Proof

If a closed walk contains \(e\), deleting that occurrence leaves a walk from
\(v\) to \(u\), proving necessity.  Conversely a minimizing return walk
concatenated with \(e\) is a closed walk of the displayed total slack.  QED.

Because slack is a nonnegative integer at most five, (5.3) is a polynomial
bounded-cost reachability computation.  Tight-SCC compression first removes
zero-cost cycles.  The resulting six cyclic cores, one for each
\(R=0,\ldots,5\), are shared by every normal form having that \(R\); the
choice of digits changes only the target-demand vector.

For packet-specific pruning, refine \(\delta_R\) by path length.  A selected
seam in a 31-seam packet must have a return path of length at most 30 and
slack at most \(R-s(e)\).  The exact test is reachability in states
`(tight SCC, slack used, length used)`, optionally crossed with the 32 lock
syndromes.  Omitting the length coordinate merely weakens the pruning; it
does not make (5.3) unsound.

## 6. Exact cycle-block master

For fixed \(\alpha\), enumerate every simple tight cycle and every simple
portal block of total length at most 31, slack at most \(R\), and target
service vector coordinatewise at most \(d_\alpha\).  Distinguish parallel
seam IDs.  For a block \(B\), store

\[
 (V(B),E(B),\ell(B),r(B),h_B),                         \tag{6.1}
\]

where \(V(B)\) is its port set, \(\ell(B)\) its seam count, \(r(B)\) its
slack, and \(h_B(t)\) its exact target multiplicity.

### Theorem 6.1 (portal-block exact cover)

The normal-form face (4.2) is feasible if and only if there are binary block
variables \(z_B\) satisfying

\[
\begin{aligned}
\sum_B\ell(B)z_B&=31,\\
\sum_B r(B)z_B&=R,\\
\sum_B h_B(t)z_B&=d_\alpha(t)&&\text{for every residual target }t,\\
\sum_{B:v\in V(B)}z_B&\le1&&\text{for every port }v.  \tag{6.2}
\end{aligned}
\]

#### Proof

Lemma 5.1 maps every seam solution to its unique selected-cycle family, which
satisfies (6.2).  Conversely a solution of (6.2) selects vertex-disjoint
directed cycles; their seam union satisfies every row of (4.2).  QED.

This gives a proof-safe construction route:

1. build the bounded-slack cyclic core using (5.3);
2. enumerate ordered portal tuples with total slack at most \(R\);
3. join consecutive portals by exact tight paths in the condensation DAG;
4. retain the literal seam IDs, internal port sets, and full 33-coordinate
   service vector, not only the five-bit syndrome;
5. solve (6.2);
6. replay the union directly from the raw seam binary.

The five-bit phase is a safe hash/pruning coordinate, but is not a substitute
for exact target multiplicities or port-disjointness.  Likewise SCC-level
reachability is sufficient for a closed walk only before enforcing simple,
vertex-disjoint literal realization; an accepted block must retain and replay
its actual paths.

A finite no-go for one normal form requires either a solver-free exhaustive
block audit or a checked CNF/OPB proof for (6.2).  Trusted CP-SAT
`INFEASIBLE`, a time limit, or failure to generate a block is not such a
certificate.

## 7. Frozen atlas and replay tools

The full 1,024-profile atlas is generated by

```text
scratch/build_l_k16_fixed75_residual31_c106_atlas_20260730.py
SHA-256 53a3be0355d2905882c729ca4e260418f6fceb6c68445c2b6432d161c2fd614b

scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json
SHA-256 a08a6d8f42b9e9e70b0e7278edfd5492032eb7733a3710c53e821101597a7125
payload b892695f00b0bc1120c3d9dd0c920b573cf36954e5aac0c236c4685f566b2ce0
```

It pins the exact D4 audit, scale-two certificate, and authenticated
five-lock audit, verifies the residual price histogram and lock partition,
and emits every exact demand-vector hash.

A positive solver candidate can be independently replayed at the reduced
level by

```text
scratch/audit_l_k16_fixed75_residual31_c106_candidate_20260730.py
SHA-256 cd2f84f645a4a4fc8f47e1487521afd6368717c8ca5535f6ff2e012cbaf456ba
```

The verifier requires 106 distinct seam IDs containing the exact fixed75,
checks endpoint balance and capacity one, checks every target multiplicity,
recomputes every seam slack, and verifies \(Q+R=5\).  Its PASS remains a
reduced witness only; it deliberately does not claim physical compilation.

## 8. Sharp remaining boundary

The count-105 search is closed globally in the frozen service/balance
relaxation by the authenticated five-lock theorem.  On the fixed75 face, the
next constructive problem is now exact and finite:

> Find one solution of (6.2) for one of the 1,024 normal forms, or certify all
> 1,024 block masters infeasible with replayable exhaustive/proof artifacts.

Only after a reduced count-106 packet is independently replayed should the
physical separation, q1, residence, all-depth, and compiler objectives be
optimized.  Nothing in this note proves that fixed75 is the correct global
count-106 face, nor that a reduced count-106 packet extends to a literal word.
