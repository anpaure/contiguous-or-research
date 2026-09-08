# Monotone P/Q short-pin retiming and exact scalar accounting

Date: 2026-07-31  
Status: abstract lemma proved; the c7be singleton instance independently replayed  
Scope: monotone P/Q schedules and their fixed middle order; scalar, Hall, and common-Q conclusions are separated

## 1. Monotone P/Q schedules

Let the coordinate universe be a finite set \(\Omega\), let

\[
T_0,T_1,\ldots,T_{W-1}\subseteq\Omega
\]

be nonempty middle targets, and fix a depth \(h\geq 1\).  Put
\(L=W+h\).  Choose start-hole and deadline-hole sets

\[
X,Y\subseteq\{0,1,\ldots,L-1\},\qquad |X|=|Y|=h.
\]

Write the complements in increasing order as

\[
P=[L]\setminus X=(p_0<\cdots<p_{W-1}),\qquad
Q=[L]\setminus Y=(q_0<\cdots<q_{W-1}).
\]

The monotone pairing assigns row \(i\) the inclusive physical interval

\[
I_i=[p_i,q_i].
\]

We require \(p_i\leq q_i\).  Since both order statistics lie in
\([i,i+h]\), this automatically gives

\[
0\leq q_i-p_i\leq h.                                      \tag{1.1}
\]

At physical position \(p\), define the maximal middle envelope

\[
E_p=\bigcap_{i:p\in I_i}T_i,                               \tag{1.2}
\]

with the intersection of an empty family interpreted as \(\Omega\).

### Lemma 1.1 (maximal-envelope criterion)

There is a nonempty physical word \(B_0,\ldots,B_{L-1}\) satisfying

\[
\bigvee_{p\in I_i}B_p=T_i\qquad(0\leq i<W)                 \tag{1.3}
\]

if and only if

\[
E_p\ne\varnothing\quad(0\leq p<L),
\qquad
\bigvee_{p\in I_i}E_p=T_i\quad(0\leq i<W).                \tag{1.4}
\]

When these conditions hold, the envelope word \(B_p=E_p\) is a realization.

#### Proof

If \(B\) realizes the rows, then every \(B_p\) is contained in every active
target and hence in \(E_p\).  Thus \(E_p\) is nonempty, and enlarging
\(B_p\) to \(E_p\) cannot remove any required bit.  It cannot add a forbidden
bit to row \(i\), because \(E_p\subseteq T_i\) on \(I_i\).  This proves
(1.4).  The converse is immediate by taking \(B=E\).  \(\square\)

## 2. Exact reservation of a named short interval

For the P/Q lower-cell catalogue, a physical interval

\[
J=[a,a+\ell-1],\qquad 1\leq\ell\leq h,                    \tag{2.1}
\]

is admissible in either of two ways.

1. If \(a=p_i\) is a selected start, then \(J\) must be a proper prefix of
   its owner: \(a+\ell-1<q_i\).
2. If \(a\in X\) is an omitted start, then
   \(1\leq\ell\leq\min(h,L-a)\).

Fix a nonempty named target \(S\subseteq\Omega\).  Put

\[
U_J=\bigvee_{p\in J}E_p.                                  \tag{2.2}
\]

For every row-bit incidence \(b\in T_i\), let

\[
H(i,b)=\{p\in I_i:b\in E_p\}                              \tag{2.3}
\]

be its maximal-envelope provider set, and define the mandatory mask of
\(J\) by

\[
M_J=\{b:\text{ for some }i, b\in T_i\text{ and }H(i,b)\subseteq J\}.
                                                                    \tag{2.4}
\]

### Theorem 2.1 (canonical short-pin criterion)

Assume the unpinned schedule satisfies Lemma 1.1.  There is a nonempty word
which realizes every middle row and has exact OR \(S\) on \(J\) if and only
if

\[
M_J\subseteq S\subseteq U_J,
\qquad E_p\cap S\ne\varnothing\quad(p\in J).               \tag{2.5}
\]

When (2.5) holds, the canonical maximal pinned word

\[
F_p=
\begin{cases}
E_p\cap S,&p\in J,\\
E_p,&p\notin J
\end{cases}                                                \tag{2.6}
\]

realizes every middle row and the pin.

#### Proof

Any word with OR \(S\) on \(J\) has every letter there contained in \(S\),
and every middle-legal letter is contained in \(E_p\).  Nonemptiness and
exact pin coverage therefore force the last two conditions in (2.5).  If all
providers of a row bit lie in \(J\), omitting that bit from \(S\) destroys the
row, which forces \(M_J\subseteq S\).

Conversely, the letters (2.6) are nonempty.  Their OR on \(J\) is

\[
\bigvee_{p\in J}(E_p\cap S)=U_J\cap S=S.
\]

For a bit \(b\in T_i\), either \(b\in S\), in which case every provider in
\(J\) retains it, or \(b\notin S\), in which case \(M_J\subseteq S\) gives a
provider outside \(J\).  Thus no middle bit is lost.  No forbidden bit is
introduced because (2.6) only shrinks the envelope.  \(\square\)

### Corollary 2.2 (singleton socket)

For \(S=\{b\}\), a short interval \(J\) is an exact singleton socket if and
only if

\[
b\in E_p\quad(p\in J),\qquad M_J\subseteq\{b\}.             \tag{2.7}
\]

In particular, a singleton position \(J=\{p\}\) is legal exactly when
\(b\in E_p\) and every other bit which is needed by a row active at \(p\)
has an envelope provider elsewhere in that row.

This condition is stronger than merely having \(b\in E_p\).  Retiming can
open a socket without changing \(E_p\) itself: it is enough to create an
alternate provider elsewhere and thereby shrink \(M_{\{p\}}\).

## 3. Exact event-DAG criterion

The following finite recurrence is an exact decision procedure for a named
short pin, and it optimizes either selected area or exact scalar slots.

At layer \(j\), before reading physical position \(j\), keep

\[
(x,y,A,\sigma,r,R,o),                                      \tag{3.1}
\]

where:

- \(x,y\) are the numbers of start and deadline holes already used;
- \(A\) is the ordered tuple of exact OR accumulators of the active rows;
- \(\sigma\in\{\text{not started},\text{active},\text{done}\}\) is the pin
  phase;
- \(r\) is the number of pin cells remaining, including the current cell;
- \(R\) is the pin OR accumulated so far; and
- \(o\) is the selected-start owner of the pin, or \(\bot\) for an
  omitted-start pin.

Choose hole indicators \(\alpha,\beta\in\{0,1\}\).  If \(\alpha=0\), append
a zero accumulator for row \(j-x\).  The rows active on the current cell are
exactly

\[
j-y,\ j-y+1,\ldots,\ j-x-\alpha,                           \tag{3.2}
\]

so their intersection is the current envelope.  A pin which starts here may
choose any length \(1,\ldots,h\) which stays in \([0,L)\); its owner is
\(j-x\) when \(\alpha=0\), and \(\bot\) when \(\alpha=1\).

Use the current letter

\[
C_j=E_j\cap S
\]

while the pin is active, and \(C_j=E_j\) otherwise.  OR \(C_j\) into every
active middle accumulator and, during the pin, into \(R\).  If \(\beta=0\),
row \(j-y\) ends and its accumulator must equal its target.  Reject the
transition if that ending row is the active pin owner, because a
selected-start lower cell must be a proper prefix.  When the last pin cell is
read, require \(R=S\).  The terminal state is

\[
(h,h,(),\text{done},0,0,\bot).                             \tag{3.3}
\]

### Theorem 3.1 (event-DAG exactness)

A path from the initial state to (3.3) exists if and only if some monotone
depth-\(h\) P/Q schedule realizes all middle rows and has an admissible exact
short pin for \(S\).

At a fixed layer, two histories with the same state have identical feasible
futures.  Therefore keeping only the greatest path weight for each state is
exact for either of the following arc weights:

\[
w_A(j,\alpha,\beta)=j(\alpha-\beta),                        \tag{3.4}
\]

which maximizes selected proper-prefix area, or

\[
w_C(j,\alpha,\beta)
=j(\alpha-\beta)+\alpha\min(h,L-j),                         \tag{3.5}
\]

which maximizes the exact boundary-aware number of physical lower-cell
slots.

#### Proof

The transition is a literal left-to-right replay of (1.2), (1.3), and the
canonical pin (2.6).  The owner check is exactly the proper-prefix rule.
Thus every terminal path decodes to a valid schedule and pin.  Conversely,
Theorem 2.1 permits any valid pinned word to be enlarged to the canonical
word used by the recurrence, so every valid schedule and pin induces a
terminal path.  Future row indices are determined by \(j,x,y\); all past
information relevant to exact row or pin completion is present in (3.1).
Hence identical states have identical continuations, proving dominance.
The identities behind the two weights are proved next.  \(\square\)

## 4. Scalar accounting and retiming price

The selected-start proper prefixes contribute

\[
A(X,Y)=\sum_{i=0}^{W-1}(q_i-p_i).                           \tag{4.1}
\]

Because each complement is the full position set with its holes removed,

\[
\boxed{A(X,Y)=\sum_{x\in X}x-\sum_{y\in Y}y.}              \tag{4.2}
\]

An omitted start \(x\) contributes exactly

\[
c_h(x)=\min(h,L-x)                                         \tag{4.3}
\]

physical short intervals.  Therefore the exact scalar slot count is

\[
\boxed{C_h(X,Y)=A(X,Y)+\sum_{x\in X}c_h(x).}                \tag{4.4}
\]

In particular,

\[
C_h(X,Y)\leq A(X,Y)+h^2,                                   \tag{4.5}
\]

but equality need not hold near the right endpoint.  Equation (3.5), rather
than (3.4) followed by a uniform \(+h^2\), is the correct objective when one
wants the exact all-schedule scalar optimum.

If \(X,Y\) are retimed to \(X',Y'\), then

\[
\Delta A=\sum X'-\sum X-\sum Y'+\sum Y,                    \tag{4.6}
\]

and

\[
\Delta C_h=\Delta A+
\sum_{x\in X'}c_h(x)-\sum_{x\in X}c_h(x).                  \tag{4.7}
\]

Thus moving one deadline hole from \(a\) to \(b>a\) costs exactly
\(b-a\) units of both area and scalar capacity.  Moving one start hole from
\(a\) to \(b>a\) gains \(b-a\) units of area, but its exact scalar change is

\[
(b-a)+c_h(b)-c_h(a).                                       \tag{4.8}
\]

In the terminal boundary strip, the two terms in (4.8) cancel.

### Lemma 4.1 (local effect of one hole slide)

Let \(H'=(H\setminus\{a\})\cup\{b\}\), with \(a<b\), \(a\in H\), and
\(b\notin H\).  If \(z_i\) and \(z'_i\) are the increasing complements of
\(H\) and \(H'\), then \(z'_i\leq z_i\) for all \(i\).  More precisely, if

\[
r=|[0,a)\setminus H|,
\qquad s=|[0,b]\setminus H|-1,
\]

then

\[
z'_r=a,qquad z'_i=z_{i-1}\ (r<i\leq s),                   \tag{4.9}
\]

and every other order statistic is unchanged.

Consequently, whenever both paired schedules are valid, with deadlines fixed,
sliding a start hole right expands row intervals to the left; active-row sets
only grow on \([a,b)\), and maximal envelopes only shrink there.  With starts
fixed, sliding a deadline hole right contracts row intervals from the right;
active-row sets only shrink on \((a,b]\), and maximal envelopes only grow
there.  Outside those physical windows the envelopes are unchanged.

#### Proof

The old complement omits \(a\) and contains \(b\); the new complement inserts
\(a\), shifts the old selected events in \((a,b)\) one order position to the
right, and deletes \(b\).  This is exactly (4.9).  The active-row and envelope
claims follow by comparing starts \(p_i\leq j\), deadlines \(q_i\geq j\), and
intersections of their target sets.  \(\square\)

Envelope inclusion by itself does not prove the retimed schedule valid:
shortening a row can remove its last provider, while adding an active row can
delete a needed envelope bit.  Lemma 1.1 or the event DAG must still be
replayed.

## 5. Scalar, Hall, and common-Q are distinct gates

Suppose \(\Lambda\) distinct lower targets must be assigned.  Even after one
named target has been reserved on one named cell, the scalar condition is
only

\[
C_h(X,Y)-1\geq\Lambda-1,
\]

equivalently \(C_h(X,Y)\geq\Lambda\).  It says nothing about which target can
use which cell.

The exact individual-pin criterion of Theorem 2.1 gives a bipartite
target/cell graph.  A matching saturating all lower targets is a further
necessary Hall gate.  It is still not sufficient for simultaneous physical
letters, because matched cells may overlap.

For a fixed matching \(M\), let \(\bar E_p\) be the envelope after any
pre-reserved pins and define the maximal common cap

\[
Q_p(M)=\bar E_p\cap
\bigcap_{S:p\in M(S)}S.                                    \tag{5.1}
\]

Exactly the same maximalization argument as Theorem 2.1 shows that \(M\) is
simultaneously realizable if and only if every \(Q_p(M)\) is nonempty and
the literal ORs of \(Q(M)\) recover every middle row, every reserved pin, and
every matched lower target.  This is the common-Q gate.  No scalar or
marginal-Hall conclusion implies it.

## 6. The c7be singleton retiming as an example

For the authenticated genuine-four-filter endpoint-reroot chronology

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

we have \(W=12870\), \(h=3\), \(L=12873\), and

\[
X=\{12870,12871,12872\}.
\]

The unrestricted maximum-area schedule uses

\[
Y_0=\{0,1,6386\}.
\]

It has

\[
A_0=32226,\qquad \sum_{x\in X}c_3(x)=3+2+1=6,\qquad C_0=32232.
\]

At position 6389 its envelope is `0xc304`, but its mandatory singleton mask
is `0x8100`; in fact this fixed schedule has no admissible `0x8000` cell.

Retiming the deadline hole `6386 -> 6388` gives

\[
Y_1=\{0,1,6388\},qquad A_1=32224,qquad C_1=32230.          \tag{6.1}
\]

The exact price is two, as predicted by (4.6)--(4.7).  Only two row
deadlines change:

```text
row 6384: 6387 -> 6386
row 6385: 6388 -> 6387.
```

Only two envelopes change:

```text
p6387: 0xd006 -> 0xd206
p6388: 0xd204 -> 0xd304.
```

The socket envelope itself remains `E_6389=0xc304`.  What changes is the
provider geometry: row 6386's bit `0x0100` has provider set `{6389}` before
retiming and `{6388,6389}` afterward.  Hence

```text
M_{6389}: 0x8100 -> 0x8000.
```

Corollary 2.2 now permits the exact cap

```text
Q_6389 = 0x8000.
```

All 12,870 middle rows still replay exactly.  The complete fixed-schedule
catalogue has no `0x8000` cell before retiming and exactly one afterward:
the selected-start singleton `[6389,6389]`, owned by row 6389.

An independent all-schedule event DAG gives both

```text
maximum selected area subject to the singleton = 32224
maximum exact boundary-aware scalar slots       = 32230
```

at the same \(X,Y_1\) and singleton.  Thus this example does not rely on the
optimistic value `32224+9=32233`; its exact scalar capacity is 32,230.

The later marginal Hall pass and successful common-Q construction are
separate gates.  They are not consequences of the retiming lemma.

## 7. Independent audit

```text
scratch/audit_monotone_pq_shortpin_retiming_20260731.py
scratch/monotone_pq_shortpin_retiming_20260731.audit.json
```

At freeze time their SHA-256 values are, respectively,

```text
1b15363eb536bf09767085962bf29541c2fdae17f11e163a6b3b18b4a1401804
46c1e257532d0e31f8ab9b90bd21df60114cd32252b0482a00b4e78a6d034af5
```

The JSON payload hash is

```text
fb7fd96e10685bf5d98796be7b7b29844036f42f7e88247ed70f0f025ddec9e5.
```

The audit imports no project module.  It exhausts 5,217 legal small P/Q
schedules and 1,946 one-hole right slides, checks (4.2)--(4.9), reconstructs
both c7be schedules, enumerates every fixed-schedule short cell, replays the
canonical singleton cap, and independently runs the event DAG under both
objectives (3.4) and (3.5).

This theorem is reusable for other fixed middle chronologies.  It does not
assert that a legal pin, a scalar pass, or a marginal Hall pass alone yields
a universal word.
