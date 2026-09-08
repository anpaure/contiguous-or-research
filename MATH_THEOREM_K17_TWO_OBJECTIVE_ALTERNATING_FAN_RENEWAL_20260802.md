# K17 two-objective alternating-fan renewal

**Date:** 2026-08-02  
**Status:** exact finite calibration and conditional renewal theorem.  The
finite data authenticate one residence-payload packet and one upper-payload
star-C8 at different states.  They do not authenticate their composition or
a uniform fan at every guarded state.

## 1. Literal state and objectives

Let `X` be the product-state hard face whose vertices retain the complete
factor, rebuilt pair variables, all frozen guards, ordinary non-`D` q1,
protected boundary, connected augmented topology, and the two literal opened
rank-ten decks.  Thus each state in the present K17 component has ordinary q1
`19412/19412` and opened q1 `19448/19448` in each orientation.  An arc is a
current-state alternating circuit whose head also lies in `X`; a packet is a
path in this graph.  Any persistent ticket not determined by the factor is an
additional state coordinate.

For opening `o in {0,1}`, write

\[
 R_o(x)=\hbox{number of positive runs of lengths one or two},
\]

and let `h_{o,r}(x)` be the number of missing opened targets of rank `r`.
Rank ten is a hard zero coordinate.  Put

\[
 H_o(x)=\sum_{r=11}^{17}h_{o,r}(x),\qquad
 V(x)=(R_0,H_0,R_1,H_1).                              \tag{1.1}
\]

The two openings are never minimized coordinatewise against one another.
For an ordered path `x_0,...,x_t`, evaluate every arc at its actual tail.
Then, despite nonlinear pair and chronology interactions,

\[
 \sum_{i=1}^t\bigl(V(x_i)-V(x_{i-1})\bigr)
       =V(x_t)-V(x_0).                                 \tag{1.2}
\]

This telescoping identity, not a sum of root-local primitive scores, is the
two-objective packet ledger.

## 2. Authenticated low-residence upper payload

The parent state is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_escape_res1980/model
SHA-256 ad031d96fb53155c3671806a6c5294e04852f73814920b70dd5c87e72ad94c82
```

The upper payload is the star-C8

```text
core       33913
labels     13,1,14,12
old y      75418,59038,90856,67103
new y      75412,59039,90862,67102
```

Its endpoint has SHA-256
`833953e576c9e3c40f9f951d09ce74c3a9ff01b90628798048f791eca9c02c8c`.
A fresh parser independently reports, in both literal openings,

```text
opened q1                    19448/19448 -> 19448/19448
residence                    1980 -> 1983
holes ranks 11,12,13         (1516,269,4) -> (1512,267,3)
holes ranks 14,...,17        (0,0,0,0) -> (0,0,0,0)
```

Hence its exact per-opening payload is

\[
        (\Delta R_o,\Delta h_{o,11},\Delta h_{o,12},
         \Delta h_{o,13})=(3,-4,-2,-1),
 \qquad (\Delta R_o,\Delta H_o)=(3,-7).                \tag{2.1}
\]

The same replay reports one component and ordinary q1 `19412/19412`; a
fresh extension satisfies all `7,164,257` round-five CNF clauses.  The
independent semantic and full-CNF audit SHAs are, respectively,

```text
228083d482922bb73ad5773a1593e5900e9a3cf4b36a2c9e43e0373e6a7689fb
03545a246ea285307984ac7664bae5068fd13634796e543722217a78e0230e99
```

The producer's exact closed-shore comparison additionally proves that the
orientation-zero terminal deck contains the orientation-zero parent deck
and has seven new targets.  The fresh independent replay proves the numerical
improvement in both openings, but does not independently upgrade this
set-inclusion statement to orientation one.

The producer sampled twenty million proposals and found `3152` accepted
closed candidates.  This authenticates the displayed witness, not catalogue
exhaustion or optimality.

## 3. Exact lexicographic encoding

For one opening,

\[
 0\le H_o\le\sum_{r=11}^{17}{17\choose r}=21778.
\]

Consequently

\[
                    S_o=21779R_o+H_o                  \tag{3.1}
\]

is an exact mixed-radix encoding of lexicographic `(R_o,H_o)`.  The earlier
neutral-C6/activated-star-C8 residence packet has per-opening cost
`(-1,+1)`, hence `Delta S_o=-21778`.  The upper star-C8 (2.1) has
`Delta S_o=65330`.  Thus the latter is intentionally rejected by a
residence-first lexicographic objective: it is an upper payload bought with
residence, not a lexicographic residence improvement.

Across two openings, use successive optimal faces on the full ordered vector
`(R_0,R_1,H_0,H_1)` (or the declared alternative order), or retain the pair
`(S_0,S_1)` under product order.  Taking the best value of each coordinate
from a different orientation is invalid.

On a bounded layered product-state graph, let `P_0` be its integral unit
source-to-sink flow polytope.  For objective rows `c_i`, recursively set

\[
 \mu_i=\min\{c_i^Tf:f\in P_{i-1}\},\qquad
 P_i=P_{i-1}\cap\{c_i^Tf=\mu_i\}.                     \tag{3.2}
\]

Each `P_i` is an optimal face and remains integral.  Equation (3.2) is the
exact lex oracle.  For product/Pareto acceptance, lift the two accumulated
costs into the layered state and test reachability of the desired quadrant;
adding two resource inequalities directly to an unlifted flow LP need not
preserve integrality.

## 4. Two-payload alternating-fan theorem

Let `Y subseteq X` be endpoint closed.  Suppose that the regenerated fan at
a state contains packets of the following state-relative types, all of whose
physical prefixes lie in `X` and whose endpoints lie in `Y`:

```text
Q (residence payload): Delta R_o <= -a, Delta H_o <=  b;
U (upper payload):     Delta R_o <=  c, Delta H_o <= -d,
```

for both openings and fixed positive integers `a,d` and nonnegative `b,c`.
No base-local additivity is assumed.

### Theorem 4.1 (exchange-rate Lyapunov renewal)

If

\[
                         bc<ad,                        \tag{4.1}
\]

choose a rational `w` with

\[
                   \frac ba<w<\frac dc.               \tag{4.2}
\]

Here `d/c=+infinity` when `c=0`.

Then every available `Q` or `U` packet strictly decreases

\[
                  L_w(x)=\sum_{o=0}^1(wR_o(x)+H_o(x)). \tag{4.3}
\]

After clearing denominators, `L_w` is a nonnegative integer potential.
Therefore, if every state of `Y` outside a declared terminal face has at
least one such fan branch, repeated regeneration reaches that face in
finitely many packets.  If the fan hypothesis is known only on an interior
subset, the conclusion is only finite arrival at its boundary; a separate
boundary completion theorem is necessary.

#### Proof

For `Q`, `Delta L_w <= 2(-aw+b)<0`; for `U`,
`Delta L_w <= 2(cw-d)<0`.  Endpoint closure regenerates the hypothesis.
The scaled potential cannot descend indefinitely.  The final sentence is
forced because absence of a branch outside the quantified subset is not a
contradiction.  \(\square\)

### Theorem 4.2 (Pareto superpacket)

If a state-relative schedule contains `n` packets of type `Q` and `m` of
type `U`, and remains in `X` throughout, then its endpoint obeys

\[
 \Delta R_o\le-na+mc,\qquad \Delta H_o\le nb-md.       \tag{4.4}
\]

There are positive integers `m,n` making both right sides strict negative if
and only if `bc<ad`; equivalently

\[
                      \frac ca<\frac nm<\frac db.      \tag{4.5}
\]

with the evident interpretation when `b=0`.  If every state outside a
declared terminal face in an endpoint-closed family admits such a complete
schedule, repeated commits reach that face after finitely many
coordinatewise-decreasing schedules.  If the condition is known only while
all four coordinates are positive, the conclusion is only arrival at their
boundary.

For the two authenticated calibrations

```text
Q: (-1,+1)     a=b=1
U: (+3,-7)     c=3,d=7.
```

The exchange interval is `3<n/m<7`; the least positive choice is `m=1,n=4`,
and its formal endpoint bound is

\[
                         4Q+U\le(-1,-3)                \tag{4.6}
\]

in each opening.  This is an exact exchange-rate calculation, not a finite
K17 path claim: the two packets were authenticated at different states, and
their state-relative composability and renewal supply remain unproved.

The weight `w=2` lies in `(1,7/3)` and makes each calibrated packet decrease
`2R_o+H_o` by exactly one per opening.  This weighted potential is a renewal
certificate under Theorem 4.1; it is not the lexicographic score (3.1).

## 5. Exact obstruction

Positive residence, q1 multiplicity, and connectedness do not by themselves
state the fan hypothesis: they neither specify the chronology fragment
junctions nor guarantee an alternating circuit with the needed provider and
upper payload.  For a bounded regenerated product graph, the exact
counter-cut at `x` is

\[
 \operatorname{Reach}(x)\cap
 \{y:\Delta R_o(y)<0,\ \Delta H_o(y)<0\text{ for }o=0,1\}
 =\varnothing.                                        \tag{5.1}
\]

Lifted-cost reachability decides (5.1).  An empty outgoing hard-legal fan is
the one-vertex minimal cut.  More generally, the reachable shore with no arc
to an accepting lifted state is the exact Farkas reachability cut; for a
fixed scalar potential, a nonnegative Bellman--Ford reduced-cost potential
certifies absence of a negative accepting path.  A sampled miss is neither
certificate.

For the complete finite hard-state graph, the global obstruction is a sink
strongly connected component whose Pareto-minimal vertices are outside the
declared terminal face.  No current frozen K17 artifact enumerates that graph.

## 6. Scope

The finite claim is factor-, guard-, topology-, q1-, and opened-chronology
exact.  The theorem supplies a proof-safe two-objective search and renewal
interface.  It does not prove uniform fan expansion, simultaneous residence
and upper completion, source realization, a lower compiler, residency, or a
word.
