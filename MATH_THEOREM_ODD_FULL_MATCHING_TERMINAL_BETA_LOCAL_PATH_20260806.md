# The terminal odd beta conversion has a literal path in the full matching contraction

**Date:** 2026-08-06  
**Method:** exact physical-edge/first-nonquiet matching dynamics; no
computation or search  
**Status:** independently audited proof of the formerly missing *local
directed path*. It replaces
the false relay-clock path in
MATH_THEOREM_ODD_RELAY_CLOCK_TERMINAL_BETA_COLLAR_20260806.md.
The macroscopic occurrence-labelled return of the completed collar to its
fixed berth remains a separate scheduling interface.
The authoritative audit is
MATH_AUDIT_ODD_FULL_MATCHING_BETA_AND_TAGGED_RETURN_20260806.md.

## 1. Local coordinates and the forced matching

Write the four consecutive local coordinates as

\[
                           u\mid v\mid b\mid g .
\tag{1.1}
\]

Here \(uv\) is the returned head \(H=02\), \(b=B_1\), and the first two
scan pairs, in scan order, are

\[
                           p_1=(g,b),\qquad p_2=(v,u).
\tag{1.2}
\]

Thus the physical line \(u|v|b|g\) is read in the reflected scan
orientation. The returned head is literally the next scan pair \(p_2\);
it is not an external block appended to a separately prepared clock.

The selected nonquiet rows are exactly

\[
 01\longleftrightarrow10,\qquad
 02\longleftrightarrow11,\qquad
 12\longleftrightarrow21,
\tag{1.3}
\]

while \(00,20,22\) are quiet. Let \(N\) denote the involution in
(1.3). A displayed macrostep below consists of one physical unit transfer
across an edge of (1.1), followed by the forced matching edge. If the
physical endpoint leaves \(p_1\) nonquiet, that matching edge is \(N\) on
\(p_1\). If it leaves \(p_1=20\), the adjacent pair \(p_2=(v,u)\) is
selected when nonquiet. There is no intervening scan pair.

## 2. The \(B_1:0\to2\) branch

The required source and target are

\[
                0201\longrightarrow0021.
\tag{2.1}
\]

They mean respectively

\[
 H\mid B_1=0,\ p_1=10
 \quad\longrightarrow\quad
 00\mid B_1=2,\ p_1=12.
\]

There is the following exact directed route:

\[
\begin{array}{rclcl}
0201&\xrightarrow{\,v\to b\,}&0111
    &\xrightarrow{\,11\to02\text{ on }p_1\,}&0120,\\
0120&\xrightarrow{\,v\to u\,}&1020
    &\xrightarrow{\,02\to11\text{ on }p_1\,}&1011,\\
1011&\xrightarrow{\,b\to g\,}&1002
    &\xrightarrow{\,01\to10\text{ on }p_2\,}&0102,\\
0102&\xrightarrow{\,v\to b\,}&0012
    &\xrightarrow{\,21\to12\text{ on }p_1\,}&0021.
\end{array}
\tag{2.2}
\]

At the third physical endpoint \(1002\), \(p_1=20\) is genuinely quiet
and \(p_2=(v,u)=01\) is next and therefore first nonquiet. Its forced edge
\(01\to10\) changes \(1002\) directly to \(0102\). Thus (2.2)
intentionally transforms the returned-head pair \(p_2\) into the
compensating target block.

## 3. The \(B_1:2\to0\) branch

The other nontrivial source and target are

\[
                0221\longrightarrow2201,
\tag{3.1}
\]

that is,

\[
 H\mid B_1=2,\ p_1=12
 \quad\longrightarrow\quad
 22\mid B_1=0,\ p_1=10.
\]

Here \(p_1\) remains the selected row throughout:

\[
\begin{array}{rclcl}
0221&\xrightarrow{\,v\to u\,}&1121
    &\xrightarrow{\,12\to21\text{ on }p_1\,}&1112,\\
1112&\xrightarrow{\,v\to u\,}&2012
    &\xrightarrow{\,21\to12\text{ on }p_1\,}&2021,\\
2021&\xrightarrow{\,b\to v\,}&2111
    &\xrightarrow{\,11\to02\text{ on }p_1\,}&2120,\\
2120&\xrightarrow{\,b\to v\,}&2210
    &\xrightarrow{\,01\to10\text{ on }p_1\,}&2201.
\end{array}
\tag{3.2}
\]

Every physical transfer is legal in the capacity-two path, and every
following matching edge in (3.2) is forced by (1.3).

## 4. The neutral branch

When \(a_1=1\), the beta coordinate already has its target value
\(B_1=B_1^*=2\). Only \(H=02\) must become the neutral collar block
\(20\). The first two macrosteps of (3.2) give exactly

\[
                         0221\longrightarrow2021,
\tag{4.1}
\]

and restore \(p_1=12\).

## 5. Directed and occurrence-labelled conclusion

### Theorem 5.1 (local full-matching beta path)

For every beta branch \(a_1\in\{0,1,2\}\), one returned head block and the
first scan pair admit a directed path in the *actual* fixed matching
contraction which:

1. writes the required complemented collar block;
2. changes \(B_1\) to \(B_1^*\);
3. restores the selected target row \(p_1=c(B_1^*)\); and
4. changes only the adjacent returned-head pair \(p_2\) among later scan
   pairs.

The path uses no false quiet classification and no work-through-the-clock
lifting argument.

#### Proof

Equations (2.2), (3.2), and (4.1) list every physical edge and every forced
matching edge. In (2.2), the only matching edge not on \(p_1\) is the
single intended transformation \(01\to10\) on \(p_2\). In the other two
branches \(p_1\) is nonquiet at every physical endpoint and is therefore
the forced selected row. The displayed endpoints are the required literal
targets.

All majority checkpoints and all minority checkpoints within each branch
are distinct. At the unique quiet-\(p_1\) checkpoint in (2.2), the literal
state \(p_2=01\), together with the shore, forces the displayed \(p_2\)
edge and distinguishes the step. Hence every branch is a simple directed
path in the full state graph.

The \(a_1=0\) and \(a_1=2\) paths have different total local masses, three
and five. The neutral path is a prefix of the mass-five route, so it must
retain the already proved exterior source record—literal target/residual
data which recovers \(a_1\)—until it terminates. With that record fixed,
different source branches cannot meet. Thus the local routes are
occurrence-labelled under exactly the persistent-record hypothesis already
available in the zipper-split teardown. \(\square\)

## 6. What remains

This theorem closes the local-dynamics error identified by
MATH_AUDIT_ODD_COLLAR_FIRST_ENDPOINT_BIT_AND_RELAY_BETA_20260806.md.
It does **not** by itself prove the whole terminal collar theorem. The
completed target collar still has to be returned to its fixed berth while:

1. the persistent exterior source record remains readable;
2. the marked corridor or visible-cart decoder identifies its occurrence;
3. the target \(p_1\) row remains the selected shadow clock; and
4. the actual teardown order avoids target extremes in any corridor theorem
   whose stationary alphabet excludes them.

The remaining odd gate is therefore a macroscopic return schedule, not the
formerly claimed three-coordinate matching handoff.
