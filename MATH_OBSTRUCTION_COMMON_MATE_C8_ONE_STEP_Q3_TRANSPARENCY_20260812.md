# A q2-neutral common-mate `C8` cannot be one-step q3-transparent

**Date:** 2026-08-12
**Method:** exact three-owner union comparison in the Johnson factor
**Status:** unconditional local no-go.  It applies to the canonical
common-mate telescope, including the private odd actuator.  It does not
assert a q3 support hole: a changed target may have another provider.

## 1. The common-mate circuit

Put

\[
                         C=K-\{s\}
\]

and use five active labels `s,a,b,x,c`.  The four changed lower owners are

\[
\begin{array}{c|c|c|c}
i&L_i&R_i&U_i\\ \hline
1&C+s+a&C+s+a+b&C+s+a+c\\
2&C+a+b&C+a+b+x&C+a+b+c\\
3&C+b+x&C+s+b+x&C+b+x+c\\
4&C+s+x&C+s+a+x&C+s+x+c.
\end{array}                                         \tag{1.1}
\]

Here `R_i` is the old circuit upper neighbour and `U_i=L_i+c` is the
untouched common mate.  After switching the circuit, the new circuit
neighbour at `L_i` is `R_(i-1)` (indices modulo four):

\[
                         R_0:=R_4.                  \tag{1.2}
\]

The signed two-owner turn current telescopes because

\[
                         R_i\cup U_i

\]

runs through the same four values as
`R_(i-1) union U_i`.  This is the common-mate q2-zero theorem.

## 2. The next upper owner has only one fresh coordinate

Follow the oriented factor forward from `L_i` across the fixed mate
`U_i`.  Let `P_i` be the next lower vertex and `W_i` its other upper
neighbour.  Thus the old local owner chronology contains

\[
                         R_i,\ U_i,\ W_i,            \tag{2.1}
\]

while after the circuit switch it contains

\[
                         R_{i-1},\ U_i,\ W_i.        \tag{2.2}
\]

Since `U_i` and `W_i` meet at the rank-`m-1` vertex `P_i`, they are
Johnson adjacent.  Therefore

\[
                         |W_i\setminus U_i|=1.       \tag{2.3}
\]

The continuation really is unchanged by the circuit switch: every `U_i`
contains the fresh label `c`, while no circuit upper `R_j` does.  Hence
`P_i` is not one of the four switched lower owners, so its two incident
factor edges remain fixed.

## Theorem 2.1 (one-step q3 transparency is impossible)

For every choice of the exterior continuation `W_i`,

\[
 R_i\cup U_i\cup W_i
 \ne
 R_{i-1}\cup U_i\cup W_i                            \tag{2.4}
\]

at each of the four changed owners.

### Proof

Suppress the fixed core `C`.  The two unions before adjoining `W_i` are

\[
\begin{array}{c|c|c|c}
i&R_i\cup U_i&R_{i-1}\cup U_i&
 (R_i\cup R_{i-1})\setminus U_i\\ \hline
1&\{s,a,b,c\}&\{s,a,x,c\}&\{b,x\}\\
2&\{a,b,x,c\}&\{s,a,b,c\}&\{x,s\}\\
3&\{s,b,x,c\}&\{a,b,x,c\}&\{s,a\}\\
4&\{s,a,x,c\}&\{s,b,x,c\}&\{a,b\}.
\end{array}                                         \tag{2.5}
\]

For the two unions in row `i` to become equal after adjoining `W_i`, the
set `W_i` must contain both labels in the last column: one is present only
on the old side and the other only on the new side.  Both labels lie
outside `U_i`.  But (2.3) permits `W_i` to contain only one label outside
`U_i`.  This contradiction proves (2.4). \(\square\)

The same argument applies in the reverse direction after reversing the
factor orientation.

## 3. Consequences

1. The common-mate `C8` is exactly q2-neutral but has a nonzero local
   three-owner current for every one-step exterior continuation.
2. Therefore the private odd actuator cannot be promoted to an all-width
   transparent packet merely by choosing its immediate successor edges.
3. Any successful use must provide at least one of:
   * literal backup occurrences for the four changed q3 values;
   * a compound multi-step collar whose total q3 current cancels;
   * another circuit with the opposite q3 current; or
   * a larger annulus in which these four rows telescope globally.
4. The theorem concerns equality of occurrence currents.  It does not say
   that a negative q3 occurrence is unique, so it is not by itself a
   support no-go.

This is the exact boundary between the positive q2 theorem and the still
open `q>=3`/socket chronology gate.

The obstruction is only to holding the outgoing continuation fixed at
the same lower cut.  It is bypassed by the coherent four-port collar in
`MATH_THEOREM_COMMON_MATE_C8_ONE_STEP_COLLAR_Q2_Q3_ZERO_ODD_SOCKET_20260812.md`:
there the complete outgoing segment is transported, and occurrences are
identified by the unchanged incoming sockets.  The resulting global q3
current is exactly zero.

## 4. The q3 support loss can nevertheless be insured finitely

The preceding obstruction concerns equality of local currents.  It does
not make q3 support an abstract ordered-two-SDR obstruction.

### Lemma 4.1 (three-owner backup path)

Every set `T` of rank `m+1` or `m+2` is the union of a simple three-owner
Johnson path of rank-`m` sets.  Moreover, for any fixed family of such
targets and any fixed forbidden vertex bank, pairwise vertex-disjoint
backup paths avoiding that bank exist for all sufficiently large `m`.

#### Proof

If `|T|=m+1`, choose distinct `a,b,c in T` and use

\[
                         T-a,\quad T-b,\quad T-c.    \tag{4.1}
\]

Every consecutive intersection has rank `m-1`, and the three-set union is
`T`.

If `|T|=m+2`, choose distinct `a,b,c,d in T` and use the owners with
missing pairs

\[
                         \{a,b\},\quad\{b,c\},\quad\{c,d\}.       \tag{4.2}
\]

Consecutive missing pairs share one element, so consecutive owners meet
in rank `m-1`; the three missing pairs have empty common intersection, so
the owner union is `T`.

There are linearly many choices in (4.1) and quartically many in (4.2).
A fixed previously used owner or lower intersection excludes only a lower-
order subfamily.  Greedy choice therefore supplies pairwise vertex-
disjoint paths for every fixed target family once `m` is large. \(\square\)

### Corollary 4.2 (abstract q3-support insurance)

For one common-mate `C8`, at most eight length-three owner windows change:
two windows through each of the four reconnected factor cuts.  Every lost
value has rank `m+1` or `m+2` and contains the common core `C=K-s`, because
both `R_i` and `U_i` contain `C`.  For each distinct lost value `T_j`,
reserve four private labels `d_(j,1),...,d_(j,4)` in `C`.  If
`|T_j|=m+1`, use the owners

\[
 T_j-d_{j,1},\quad T_j-d_{j,2},\quad T_j-d_{j,3};   \tag{4.3}
\]

if `|T_j|=m+2`, use

\[
 T_j-\{d_{j,1},d_{j,2}\},\quad
 T_j-\{d_{j,2},d_{j,3}\},\quad
 T_j-\{d_{j,3},d_{j,4}\}.                           \tag{4.4}
\]

These are the paths in Lemma 4.1, and the private missing-core labels make
paths for distinct targets vertex-disjoint.  Protect one such path for
each distinct lost value, colour the paths alternately, and include them
with the old actuator bank while forbidding the actuator's four new edges.

Let `D` be the union of the at most 32 reserved core labels.  The resulting
bank has constant size and lies in the bounded face over `C-D`.  The
bounded phased-bank extension theorem
places it in one ordered two-SDR for all sufficiently large `m`.  Switching
the actuator leaves every backup path untouched.  Hence the actuator can
be made q3-**support** safe, despite Theorem 2.1.

This still does not solve all widths.  A four-cut switch can affect a
number of longer crossing windows growing with the lengths of the exterior
arcs.  Protecting q3 backups alone gives no q4-or-wider theorem; that is
where a compound annulus or full-union shield remains necessary.
