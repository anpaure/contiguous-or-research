# One-sided product-SCD flag fusion and the residence dichotomy

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver,
probabilistic black box, or web input is used.

## 0. Result

This note combines the two-colour product-SCD union paths with the
one-sided part of the diverse compiler/collar.  Only missing lower
shadows are charged; upper loads and positive multiplicities are ignored.
Throughout the global specialization,

\[
                         W=\binom{2m}{m}.                           \tag{0.0}
\]

The local fusion problem has an exact answer.  Let two directed Johnson
paths be joined by one Johnson seam.  Assume each path is internally safe
through depth \(H\).  Then their fusion is safe through depth \(H\) if
and only if no coordinate inserted before or at the seam is removed
within the next \(H\) edges.  In that case every old lower flag is
preserved, every crossing flag has the correct rank, and the one-sided
missing-shadow loss is exactly zero.  The two path components become one,
so an \(O(H)\) component collar is paid once rather than twice.

If the outgoing lower tower of the first path was already prescribed,
there is still an exact constant-loss fusion.  Let
\(\alpha=(a_1,\ldots,a_H)\) be its old deletion port and
\(\beta=(b_1,\ldots,b_H)\) the actual deletion port after fusion.  The
number of changed tower flags is exactly

\[
 d_{\rm pref}(\alpha,\beta)
  =\#\left\{q\le H:
       \{a_1,\ldots,a_q\}\ne\{b_1,\ldots,b_q\}
     \right\}.                                                    \tag{0.0a}
\]

In particular, one adjacent transposition in the deletion port changes
exactly one assigned depth.  Subject to the same residence-safety
condition, it fuses two paths with missing-target increase and literal
repair charge at most \(1\).  A bounded local
permutation of the port has \(O(1)\) loss.  Thus the requested
sub-\(H\) interface exists locally; exact equality of the whole ordered
port is unnecessary.

There is also a sharp obstruction.  If the shortest cross-seam positive
residence has length \(\rho\le H\), then at least one crossing lower flag
is invalid at every depth

\[
                         q=\rho,\rho+1,\ldots,H.                   \tag{0.1}
\]

Thus a flag-preserving fusion loses at least \(H-\rho+1\) typed flags.
It has \(O(1)\) loss only when \(\rho\ge H-O(1)\), and \(o(H)\) loss
only when \(\rho=H-o(H)\).

For a product-SCD path of length \(h\), the forward direction inserts
only \(A\)-coordinates and removes only \(B\)-coordinates.  Reversing it
interchanges these roles.  Hence a high-end to high-end fusion of paths
of lengths \(h_1,h_2=o(H)\) has the following dichotomy:

* if their active \(A\)-insertion sets and the seam ports are compatible,
  the fusion has zero one-sided loss;
* if the active sets overlap, then \(\rho\le h_1+h_2+2=o(H)\), so the
  loss is \(H-o(H)\).

The low-end statement is identical with \(A,B\) interchanged.  Therefore
there is no universal \(\Omega(H)\) lower bound for *every* pair, but
there is no genuinely intermediate repair of a positive residence: for
the short paths carrying almost all product-SCD components, an
\(o(H)\)-loss fusion must be residence-free.  Once it is residence-free,
bounded port permutations give the constant-loss mechanism above.

The number of product-SCD diagonal paths of length at least \(L\) is
exactly

\[
 \binom m{\lfloor(m-L)/2\rfloor}^{\!2}.                           \tag{0.2}
\]

When \(H/\sqrt m\to\infty\), one may choose \(L=o(H)\) so that (0.2)
is \(o(W/H)\).  Consequently a global construction with final component
count \(o(W/H)\) and total lower loss \(o(W)\) must join all but
\(o(W/H)\) of the original \(\Theta(W/\sqrt m)\) paths by exactly safe
seams.  This is the precise surviving endpoint problem: construct a
near-spanning stateful \(H\)-memory walk cover whose aggregate prefix-cut
cost is \(o(W)\).  Pairwise endpoint compatibility is not sufficient,
as corrected in Section 7.  A uniform \(O(1)\) cost per seam is acceptable
because there are only
\(\Theta(W/\sqrt m)=o(W)\) original paths; one loss at every depth is
not.

## 1. Lower flags and positive residence

Let

\[
                         X_0,X_1,\ldots,X_s
\]

be a directed path in \(J(n,m)\), written edgewise as

\[
                         X_{t+1}=X_t-a_t+b_t.                    \tag{1.1}
\]

For a window of \(q\) edges, define its lower flag

\[
                         L_q(t)=\bigcap_{j=0}^qX_{t+j}.          \tag{1.2}
\]

Call the path *lower \(H\)-safe* when

\[
                         |L_q(t)|=m-q                            \tag{1.3}
\]

for every available \(t\) and \(1\le q\le H\).

A positive residence is a pair of edges \(u<v\) and a coordinate \(x\)
such that

\[
                         b_u=x=a_v.                              \tag{1.4}
\]

Its inclusive length is

\[
                         \rho(u,v)=v-u+1.                        \tag{1.5}
\]

### Theorem 1.1 (one-sided residence criterion)

A directed Johnson path is lower \(H\)-safe if and only if it has no
positive residence of length at most \(H\).

#### Proof

Consider the \(q\)-edge window beginning at \(X_t\).  Its intersection
is obtained from the \(m\) coordinates initially present by deleting
the distinct initially present coordinates which disappear at least once
during the window.  It has rank \(m-q\) precisely when every one of the
\(q\) edge removals deletes a different coordinate already present in
\(X_t\).

If \(b_u=a_v=x\) with both edges in the window, then \(x\) was inserted
after the initial state and its later removal does not delete a new
coordinate from that initial state.  Thus the intersection has rank at
least \(m-q+1\).  Conversely, if a removal fails to delete a new
initial coordinate, then its label was either inserted earlier in the
window or was removed, reinserted, and removed again.  In both cases
there is an insertion followed by a later removal of the same coordinate
inside the window.  This is a positive residence of length at most \(q\).
The equivalence follows. \(\square\)

This criterion is strictly one-sided.  A removal followed by a later
reinsertion does not restore the coordinate to an intersection and is
therefore harmless unless the same coordinate is removed again.

## 2. Exact fusion theorem

Let

\[
 P=(X_{-r},\ldots,X_0),\qquad
 Q=(Y_0,\ldots,Y_s)                                             \tag{2.1}
\]

be lower \(H\)-safe paths, with \(r,s\ge H\) after including their
chosen endpoint collars.  Suppose

\[
                         Y_0=X_0-a_0+b_0                         \tag{2.2}
\]

is a Johnson edge.  Insert this edge and concatenate \(P\), the seam,
and \(Q\).

### Theorem 2.1 (zero-loss one-sided fusion)

The fused path is lower \(H\)-safe if and only if no insertion edge on
the left side or at the seam and no later removal edge on the seam or
right side carry the same coordinate at inclusive distance at most
\(H\).

When this condition holds:

1. every lower flag wholly inside \(P\) or \(Q\) is unchanged;
2. every crossing window supplies a rank-\((m-q)\) lower flag;
3. no previously covered lower target is lost; and
4. any per-component lower collar is required only at the two outer ends
   of the fused path.

Thus the fusion has exactly zero one-sided missing-shadow loss.

#### Proof

The only windows whose edge lists change are those crossing the seam.
Theorem 1.1 says exactly that all such windows are safe under the stated
cross-residence condition.  Windows internal to the two old paths are
unchanged.  Hence all their old literal witnesses survive, while the
crossing windows add valid flags.  A linear collar depends only on the
two outer endpoints after the paths are concatenated, so the internal
pair of endpoint collars disappears. \(\square\)

The theorem is directly compatible with the bridge-one residence
compiler: the same no-positive-residence condition is its exact local
lifting criterion.  No lower quota or balancing assertion is used.
Duplicates among the new crossing targets are harmless in the one-sided
missing-shadow problem.

## 3. A prescribed flag port is rigid

Suppose an endpoint \(X\) is assigned a nested lower tower

\[
 X=F_0\supset F_1\supset\cdots\supset F_H,
 \qquad |F_q|=m-q.                                               \tag{3.1}
\]

Put

\[
                         d_q=F_{q-1}\setminus F_q.               \tag{3.2}
\]

### Lemma 3.1 (deletion-word recovery)

An \(H\)-safe continuation from \(X\) realizes the prescribed tower
(3.1) if and only if its first \(H\) removal labels are

\[
                         d_1,d_2,\ldots,d_H                       \tag{3.3}
\]

in this order.

#### Proof

For an \(H\)-safe continuation, Theorem 1.1 gives

\[
 \bigcap_{j=0}^qX_j
     =X\setminus\{a_0,\ldots,a_{q-1}\}.                         \tag{3.4}
\]

Successive differences of the nested sets in (3.4) recover
\(a_{q-1}\) uniquely.  Comparing with (3.2) proves both directions.
\(\square\)

Thus a terminal lower tower places no identity constraint on insertion
labels, although residence safety still constrains them; it fixes the
deletion labels completely.
This is the exact interface between W's one-hot atlas and a diverse
compiler collar.

Exact preservation is more rigid than the one-sided theorem needs.  For
two deletion words \(\alpha=(a_1,\ldots,a_H)\) and
\(\beta=(b_1,\ldots,b_H)\), define the prefix-cut distance

\[
 d_{\rm pref}(\alpha,\beta)
 =\#\left\{q\in[H]:
       \{a_1,\ldots,a_q\}\ne\{b_1,\ldots,b_q\}
   \right\}.                                                     \tag{3.5}
\]

### Theorem 3.2 (exact constant-loss port recoupling)

Assume both continuations are lower \(H\)-safe and start at the same
endpoint owner \(X\).  Replacing the continuation with deletion port
\(\alpha\) by one with deletion port \(\beta\) changes exactly
\(d_{\rm pref}(\alpha,\beta)\) members of the endpoint lower tower.

In particular:

1. if \(\beta\) is obtained from \(\alpha\) by swapping the adjacent
   entries in positions \(r,r+1\), exactly the depth-\(r\) flag changes;
2. if the permutation is supported on an interval of \(s\) consecutive
   positions, at most \(s-1\) flags change; and
3. boundedly many bounded intervals give \(O(1)\) total loss,
   independently of \(H\).

#### Proof

The depth-\(q\) endpoint flags are

\[
 F_q^\alpha=X\setminus\{a_1,\ldots,a_q\},
 \qquad
 F_q^\beta=X\setminus\{b_1,\ldots,b_q\}.                         \tag{3.6}
\]

They agree exactly when the two prefix sets agree, proving (3.5).  An
adjacent transposition crosses only the cut after its first swapped
entry.  A permutation supported on \([r,r+s-1]\) leaves every prefix cut
outside \([r,r+s-2]\) invariant.  The three assertions follow.
\(\square\)

This theorem gives the requested local fusion explicitly.  Choose a
residence-safe endpoint seam and use a diverse collar whose outgoing
deletion order is the old order with one adjacent pair swapped.  The two
monotone paths become one component; all assigned lower flags except one
survive.  No upper assertion is made.

### Proposition 3.3 (literal adjacent-swap collar)

Let \(a_1,\ldots,a_H\) be distinct elements of an owner \(X\), and let
\(c_1,\ldots,c_H\) be distinct elements outside \(X\).  For a permutation
\(\sigma\in\mathfrak S_H\), put

\[
 X_t^\sigma
   =X\setminus\{a_{\sigma(1)},\ldots,a_{\sigma(t)}\}
      \cup\{c_1,\ldots,c_t\},
 \qquad 0\le t\le H.                                             \tag{3.7}
\]

Every sequence \((X_t^\sigma)_{t=0}^H\) is a lower \(H\)-safe Johnson
path, and all of them have the same endpoints

\[
                         X,\qquad
                         X\setminus\{a_1,\ldots,a_H\}
                           \cup\{c_1,\ldots,c_H\}.                \tag{3.8}
\]

If \(\tau\) is one adjacent transposition, replacing the \(\sigma\)-path
by the \(\sigma\tau\)-path is a two-step Johnson diamond.  It changes
exactly one member of the endpoint lower tower and creates no
positive residence.

#### Proof

At step \(t\), (3.7) removes one previously unremoved member of \(X\)
and inserts the fresh label \(c_t\).  No inserted label is ever removed,
so Theorem 1.1 proves safety.  The endpoint depends only on the two
unordered label sets, proving (3.8).  Adjacent orders agree before the
two swapped removals and again after both have occurred; their two
intermediate owners are opposite corners of the corresponding Johnson
square.  Theorem 3.2 gives the one-flag assertion. \(\square\)

Thus a diverse collar can absorb an adjacent deletion-order mismatch
without extra collar length: substitute the alternate diamond and, in
the worst case, append the one displaced lower target literally.

## 4. The exact loss forced by one cross residence

Assume both sides contain \(H\) collar edges, so every crossing window
discussed below exists.  Let \(\rho\) be the minimum inclusive length of
a cross-seam positive residence.

### Theorem 4.1 (typed and occurrence loss)

If \(\rho\le H\), then for every \(q\) with \(\rho\le q\le H\) there
is a crossing \(q\)-window whose intersection has rank greater than
\(m-q\).  Hence a fusion which is required to preserve its assigned
one-hot lower flag at every depth loses at least

\[
                         H-\rho+1                               \tag{4.1}
\]

typed flags.

If the residence lies at least \(H\) edges from both outer collar ends,
the number of invalid crossing window occurrences is at least

\[
             \sum_{q=\rho}^{H}(q-\rho+1)
             ={(H-\rho+1)(H-\rho+2)\over2}.                    \tag{4.2}
\]

#### Proof

Let the insertion occur on edge \(u\) and the removal on edge \(v\), so
\(v-u+1=\rho\).  For every \(q\ge\rho\), a \(q\)-edge interval can be
chosen to contain both edges.  Theorem 1.1 makes its lower flag invalid.
The depths in (4.1) have different target ranks, so they are distinct
typed losses.  With full collars, the left endpoint of a \(q\)-window
containing both edges has \(q-\rho+1\) possible positions.  Summing gives
(4.2). \(\square\)

Corollary 4.2 is the sharp asymptotic threshold:

\[
 \begin{array}{c|c}
 \text{desired local typed loss}&\text{necessary residence length}\ \\ \hline
 O(1)&\rho\ge H-O(1),\\
 o(H)&\rho=H-o(H),\\
 \rho=o(H)&\text{loss }H-o(H).
 \end{array}                                                     \tag{4.3}
\]

This is a flag-preservation lower bound.  A global construction may try
to cover the displaced target somewhere else, but that is a separate
target reassignment problem and no longer a local flag-preserving fusion.

## 5. Specialization to product-SCD paths

Fix a split \(A\mathbin{\dot\cup}B\), \(|A|=|B|=m\), and symmetric
chains

\[
 C_a\subset\cdots\subset C_{m-a},
 \qquad
 D_b\subset\cdots\subset D_{m-b}.                              \tag{5.1}
\]

Their rank-\(m\) diagonal is

\[
 V_t=C_{i+t}\cup D_{j+h-t},qquad 0\le t\le h.                  \tag{5.2}
\]

In the forward orientation, every edge inserts the next \(C\)-increment
from \(A\) and removes the next \(D\)-increment from \(B\).  Let

\[
 I_A(P)=C_{i+h}\setminus C_i,qquad
 I_B(P)=D_{j+h}\setminus D_j.                                  \tag{5.3}
\]

Both sets have size \(h\).  Reversing \(P\) removes \(I_A(P)\) and
inserts \(I_B(P)\).

Consider a high-end to high-end seam: traverse \(P\) forward, cross one
Johnson edge, and traverse \(Q\) backwards.  Ignore for the moment the
two seam labels themselves.

### Theorem 5.1 (short product-path dichotomy)

If

\[
                         I_A(P)\cap I_A(Q)\ne\varnothing,         \tag{5.4}
\]

then the fused path has a cross positive residence of length at most

\[
                         h(P)+h(Q)+2.                            \tag{5.5}
\]

If the intersection in (5.4) is empty and neither seam label creates a
positive residence of length at most \(H\), the fusion is lower
\(H\)-safe and has zero rank/chronology loss.  If an old terminal tower
was prescribed, its exact identity loss is the prefix-cut distance
(3.5), which may be one under an adjacent port swap.

The low-end to low-end statement is the same with
\(I_A\) replaced by \(I_B\).

#### Proof

A coordinate in (5.4) is inserted somewhere on the forward traversal of
\(P\) and removed somewhere on the reverse traversal of \(Q\).  There
are at most \(h(P)\) edges from its insertion to the end of \(P\), one
seam edge, and at most \(h(Q)\) edges to its removal.  This gives (5.5),
with one harmless unit allowed for endpoint convention.  If the active
sets are disjoint, the forward path inserts only \(A\)-labels and the
reverse path removes only \(A\)-labels, so no interior cross residence is
possible.  The explicit seam-label hypothesis removes the only remaining
possibilities.  Theorem 2.1 finishes the proof. \(\square\)

### Corollary 5.2 (no intermediate short-path seam)

If \(h(P)+h(Q)=o(H)\), then a high-end fusion has either

* zero residence loss, with exact assigned-tower loss given by (3.5),
  under the port-disjointness condition; or
* at least \(H-o(H)\) typed lower-flag loss.

Thus an \(O(1)\) or \(o(H)\) local fusion cannot be obtained by a small
perturbation of an overlapping endpoint port.  The overlap must be
removed entirely, apart from labels placed at distance \(H-o(H)\) in a
larger auxiliary collar.

There is a literal local product-chain example on the zero-loss side of
the dichotomy.

### Proposition 5.3 (an exact residence-free product-chain seam)

Let \(C,C'\) be two symmetric \(A\)-chains of the same length \(h\),
with bottom/top pairs

\[
                         S-U\subset S,
 \qquad
                         S'-V\subset S',                           \tag{5.6}
\]

where \(|U|=|V|=h\).  Suppose

\[
                         U\cap V=\varnothing,
 \qquad
                         S'=S-x+y,                                \tag{5.7}
\]

with \(x\notin U\) and \(y\notin V\).  Pair both chains with the same
symmetric \(B\)-chain \(D\) of the matching length.  Let \(P,Q\) be the
two rank-\(m\) product diagonals.

Then the high endpoint of \(P\) is Johnson-adjacent to the high endpoint
of \(Q\).  Traversing \(P\) forward, using the seam \(x\to y\), and
traversing \(Q\) backward is lower \(H\)-safe for every

\[
                         H\ge h(P)+h(Q)+2                         \tag{5.8}
\]

after arbitrary residence-free outer completion.  The seam itself has
zero one-sided missing-shadow loss.

#### Proof

The common \(B\)-chain gives the same bottom \(B\)-set at the two high
endpoints, while (5.7) makes their \(A\)-sets Johnson-adjacent.  The
forward traversal of \(P\) inserts exactly the alphabet \(U\).  The
backward traversal of \(Q\) removes exactly \(V\).  These are disjoint.
The seam removes \(x\notin U\), so it does not remove a recent insertion,
and it inserts \(y\notin V\), so the reverse path does not remove the
seam insertion.  No cross positive residence exists.  Theorem 2.1 gives
the conclusion. \(\square\)

The proposition is a local construction inside two prescribed symmetric
chains.  It does not prove that one fixed global SCD admits a
near-spanning system of such pairs; that is precisely the endpoint-forest
gate in Section 7.

## 6. Almost all product-SCD paths are short

Let

\[
                         c_m=\binom m{\lfloor m/2\rfloor}.         \tag{6.1}
\]

The global product-SCD cover has exactly \(c_m^2\) nonempty rank-\(m\)
diagonal paths.  A chain of minimum rank \(a\) has length
\(m-2a\), and the diagonal of two chains has length

\[
                         h=m-2\max(a,b).                         \tag{6.2}
\]

### Theorem 6.1 (exact long-path census)

For every integer \(L\ge0\), the number of product-SCD paths of length at
least \(L\) is

\[
 \boxed{
                         P_{\ge L}
      =\binom m{\left\lfloor(m-L)/2\right\rfloor}^{\!2}.}         \tag{6.3}
\]

Moreover

\[
 {P_{\ge L}\over c_m^2}
                  \le \exp\left(-{L^2-O(L)over m}\right).       \tag{6.4}
\]

#### Proof

The condition \(h\ge L\) is equivalent to

\[
                         a,b\le\left\lfloor{m-L\over2}\right\rfloor.
\]

The number of SCD chains with minimum at most \(t\) is exactly
\(\binom mt\), because each such chain contains one rank-\(t\) set.
Squaring proves (6.3).  The usual product of successive central binomial
ratios, followed by \(\log(1-x)\le-x\), gives (6.4). \(\square\)

Put

\[
                         g={H\over\sqrt m}\longrightarrow\infty
\]

and choose, for example,

\[
                         L=\left\lceil\sqrt{4m\log g}\right\rceil. \tag{6.5}
\]

Then

\[
                         L=o(H),\qquad
                         P_{\ge L}=o(W/H).                       \tag{6.6}
\]

Indeed (6.4) makes the fraction of long paths \(O(g^{-3})\), while

\[
                         c_m^2
       =\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.       \tag{6.7}
\]

Thus the short-path dichotomy applies to every path except a leave already
small enough for the desired final component bound.

**Correction to the original static-forest claim.**  Pairwise-safe seams
do not compose through a short intermediate path.  An insertion before
the first seam can remain resident through that path and be removed after
the second seam, although neither pairwise test sees both events.  The
global object must therefore carry the last \(H-1\) insertion labels as a
state.  The local two-path theorems above remain valid.

## 7. The corrected global endpoint gate: an \(H\)-memory automaton

Delete the \(o(W/H)\) long paths in (6.6).  A static compatibility graph
on their endpoints is not sufficient.  Here is the smallest
counterexample.

Choose distinct labels \(a,b,c,d,x\), start from a middle owner containing
\(a,b\) but not \(c,d,x\), and take three consecutive exchanges

\[
 (a\to x),\qquad (b\to c),\qquad (x\to d).          \tag{7.1}
\]

Regard the first and third exchanges as two seams and the middle exchange
as one short intermediate path.  The first seam together with the middle
path is lower safe, and the middle path together with the second seam is
lower safe.  In the latter pair, \(x\) is simply present in the initial
owner and its removal is legitimate.  But the full three-edge word has a
positive residence: \(x\) is inserted on the first edge and removed on
the third.  Its depth-three intersection therefore has rank \(m-2\), not
\(m-3\).  Fresh disjoint exchanges may be appended outside this word to
supply arbitrary external collars.  Thus pairwise compatibility is not
transitive.

The correct state before an exchange at time \(t\) is the ordered queue

\[
 {\cal I}_t=(b_s:t-H+1\le s<t),                    \tag{7.2}
\]

with labels carrying their ages and expired labels deleted.  The exchange
\(a_t\to b_t\) is lower legal exactly when

\[
                         a_t\notin{\cal I}_t.       \tag{7.3}
\]

After the exchange, append \(b_t\) and retain only the last \(H-1\)
entries.  Theorem 1.1 proves that this finite-memory update is necessary
and sufficient for lower \(H\)-safety.

Every oriented product-SCD path, together with chosen entry and exit
seams, therefore defines a partial deterministic transition

\[
                         \Phi_P:{\cal I}_{\rm in}
                            \longmapsto{\cal I}_{\rm out},       \tag{7.4}
\]

obtained by reading its complete exchange word.  It is undefined if a
test (7.3) fails.  Prefix-cut cost is attached to a realized transition,
not merely to an unordered pair of original endpoints, because the
incoming history can change the legal outgoing port.

### Theorem 7.1 (stateful formulation)

A proposed concatenation of the short product-SCD paths is lower
\(H\)-safe if and only if its seams and oriented path words form a valid
walk in the automaton (7.2)--(7.4).  If the resulting walk cover has
\(p\) components, its outer collars cost \(O(Hp)\).  Its assigned-tower
loss is the sum of the prefix-cut changes along the actual automaton
trajectories.

Conversely, any globally valid flag-preserving fusion projects to an
endpoint path forest together with a consistent automaton state on every
oriented incidence.  After removing the \(o(W/H)\) residence-unsafe seams
allowed by Corollary 5.2, that decorated forest has total prefix-cut cost
\(o(W)\).  The undecorated forest alone need not lift.

#### Proof

Reading the concatenated exchange word and applying (7.3) is exactly the
absence of every positive residence of inclusive length at most \(H\).
Theorem 1.1 gives the first equivalence.  The collar and prefix-cut
statements are Theorems 2.1 and 3.2 applied along the realized state
trajectory.  The converse records the last \(H-1\) insertions at every
incidence of an already valid fusion; Corollary 5.2 supplies the same
exception count as before. \(\square\)

The exact remaining combinatorial lemma is therefore stateful:

> **Residence-free product-SCD \(H\)-memory path cover.**  Choose the
> two-colour rectangle phases, path orientations, literal Johnson seams,
> and one consistent trajectory of the queue automaton (7.2)--(7.4), so
> that all but \(o(W/H)\) components coalesce and the aggregate
> prefix-cut cost is \(o(W)\).

If every intermediate block had length at least \(H\), all incoming
history would expire before its exit and the old static forest would be
valid.  Section 6 proves the opposite regime is dominant: almost all
product-SCD paths have length \(o(H)\).  Hence the memory state is
load-bearing, not cosmetic.

## 8. Audited boundary

Proved:

* the exact one-sided positive-residence criterion;
* a zero-loss flag-preserving fusion theorem;
* rigidity of a preassigned lower flag tower;
* the exact prefix-cut metric and a one-loss adjacent-port fusion;
* a literal same-endpoint Johnson-diamond realization of that fusion;
* the sharp \(H-\rho+1\) typed-loss lower bound;
* the zero-versus-\(H-o(H)\) dichotomy for short product-SCD paths;
* the exact product-SCD long-path census; and
* reduction of the global component problem to a low-weight, stateful
  residence-free \(H\)-memory path cover.

Not proved:

* abundance of literal Johnson edges between compatible product-SCD
  endpoints;
* a near-spanning low-weight residence-free \(H\)-memory path cover;
* simultaneous preservation of the upper flags—the present theorem is
  deliberately one-sided;
* a common one-hot reassignment when a local flag tower is not preserved;
  or
* coefficient one.

The conclusion is sharp for the requested local question.  Ordinary
\(O(H)\)-per-seam loss is not unavoidable: a residence-free seam has
zero loss, and one adjacent port swap has loss one.  But for the short
paths which dominate the global cover, every positive-residence overlap
causes \(H-o(H)\) loss.  The viable global route is therefore a
near-spanning stateful walk cover of residence-safe seams with bounded
aggregate prefix-cut cost, not an ordinary endpoint forest and not an
amortized collection of residence-unsafe seams.

## 9. Complement-equivariant fusion

For a directed owner path \(P=(X_t)\), write

\[
                         \kappa P=(X_t^c)                         \tag{9.1}
\]

with the same time order.  Lower and upper flags satisfy the exact
identity

\[
                         L_q(\kappa P)=U_q(P)^c.                  \tag{9.2}
\]

Call a path *upper \(H\)-safe* if every \(q\)-window has union rank
\(m+q\).  The upper analogue of Theorem 1.1 says this holds exactly when
there is no coordinate which is removed and then reinserted within a
controlled window.  Consequently:

### Lemma 9.1 (signed residence criterion)

A path and its complement are both lower \(H\)-safe if and only if the
original path is both lower and upper \(H\)-safe.  Equivalently, in every
\(H\)-edge window no physical coordinate is used by two different
Johnson exchanges.

#### Proof

Under complementation, the removal label of an edge becomes its insertion
label and conversely.  Thus a positive residence in \(\kappa P\) is a
removal-then-reinsertion residence in \(P\).  Apply Theorem 1.1 and
(9.2). \(\square\)

Let \({\cal P}\) be a path partition on which complementation induces a
path involution \(P\mapsto\kappa P\).  A selected endpoint path forest
\({\cal F}\) is *complement-equivariant* when

\[
                         e\in{\cal F}\quad\Longleftrightarrow\quad
                         \kappa e\in{\cal F},                  \tag{9.3}
\]

with end ports and component orientations paired by complement.  A
component may be paired with a distinct complementary component or may
be self-complementary with reversed endpoint order.

For a seam \(e\), let \(w^-(e)\) be its lower deletion-port prefix-cut
cost and let \(w^+(e)\) be the analogous prefix-cut cost of its insertion
port.  Then

\[
                         w^-(\kappa e)=w^+(e),
 \qquad
                         w^+(\kappa e)=w^-(e).                    \tag{9.4}
\]

### Retracted claim 9.2 (static equivariant forest criterion)

**This paragraph is false as stated for the same reason as the original
Theorem 7.1.**  A complement-equivariant endpoint forest does not
automatically give correct
lower and upper flags through depth \(H\) precisely when every selected
seam is both lower and upper \(H\)-safe.  For a seam orbit
\([e]=\{e,\kappa e\}\), its exact assigned lower loss on the two orbit
members is

\[
                         w_{\rm orb}([e])=w^-(e)+w^+(e),           \tag{9.5}
\]

and the upper loss is the same.  Hence a complement-equivariant forest
with \(p=o(W/H)\) components and

\[
                         \sum_{[e]}w_{\rm orb}([e])=o(W)          \tag{9.6}
\]

has \(o(W)\) total assigned loss over both signs, while its outer collars
cost \(o(W)\).

The displayed orbit cost identities remain valid for one isolated pair
of seams.  The asserted global implication does not: a protected window
may cross two complement-paired seam orbits through a short intermediate
path.  Section 7's counterexample and its complement give a signed
counterexample.  The corrected criterion is the signed-memory automaton
below.

Before edge \(t\), retain both age-ordered queues

\[
 {\cal I}_t=(b_s:t-H+1\le s<t),\qquad
 {\cal D}_t=(a_s:t-H+1\le s<t).                    \tag{9.7}
\]

The next exchange \(a_t\to b_t\) is legal for both signs exactly when

\[
                         a_t\notin{\cal I}_t,\qquad
                         b_t\notin{\cal D}_t.       \tag{9.8}
\]

After the exchange, expire the oldest labels and append \(b_t\) to
\({\cal I}\) and \(a_t\) to \({\cal D}\).  Complementation swaps the two
queues and conjugates every block transition.

### Theorem 9.3 (equivariant signed stateful criterion)

Assume the atomic path family is permuted by complementation.  A
complement-equivariant concatenation is simultaneously lower and upper
\(H\)-safe if and only if its full oriented exchange words and seams
admit trajectories of (9.7)--(9.8).  For the resulting
complement-invariant family,

\[
             \mu_q^+(U)=\mu_q^-([2m]\setminus U).                 \tag{9.9}
\]

Hence every lower hole, quota, or assigned-prefix estimate transfers
exactly to the upper sign.  If the stateful cover has \(o(W/H)\)
components and \(o(W)\) lower assigned loss, its total signed assigned
loss and outer-collar cost are \(o(W)\).

#### Proof

The two tests in (9.8) exclude respectively insertion-then-removal and
removal-then-insertion residences.  Lemma 9.1 and the queue proof in
Section 7 give safety.  Equation (9.2), summed over the
complement-invariant family, gives (9.9). \(\square\)

For \(m\ge2\), complementation fixes no middle owner and no Johnson edge.
It fixes no finite path component setwise: an involutory path
automorphism is the identity or reversal; the former fixes a vertex,
while the latter fixes a vertex or a central edge, and a central fixed
edge would join complementary middle sets, which are not Johnson
adjacent.  Thus path components and seams occur in free complement
orbits.  Self-complementary **cycle** components can occur, with
complement acting by a fixed-point-free half-rotation.  They cost no
exception if cycles are admitted; if a linear path is required, opening
each such cycle must be charged in the final collar/component ledger.

A merely one-sided residence-free forest need not meet this theorem.
The local construction in Proposition 5.3 illustrates the gap.  Its two
paths use the same \(B\)-chain, so their active \(B\)-increment sets are
identical.  Along the forward/reverse fusion those labels are removed and
then reinserted within at most \(2h+2\) edges.  Thus Proposition 5.3 is
lower safe but upper unsafe whenever \(h>0\) and \(2h+2\le H\).

## 10. The actual product-SCD endpoint graph

There is a preliminary component-level issue.  A fixed SCD is not in
general carried to itself chainwise by complement.  In fact no SCD of
\(B_m\), \(m\ge2\), can be chainwise complement-stable.

### Lemma 10.1 (chainwise complement obstruction)

No symmetric-chain decomposition of \(B_m\), \(m\ge2\), is permuted as
a collection of chains by set complementation.

#### Proof

The unique chain containing \(\varnothing\) is a saturated maximal chain
from \(\varnothing\) to \([m]\).  Its complement image is another chain
containing both endpoints, so a complement-stable decomposition would
force that maximal chain to be self-complementary.  Let its rank-one
member be \(\{x\}\).  Its rank-\((m-1)\) member contains \(x\) by
nestedness, while complement stability would make it
\([m]\setminus\{x\}\), a contradiction. \(\square\)

Therefore complementation does not automatically define the involution
assumed in Theorem 9.3 on W's original path components.  Let
\(E_{\rm int}\) be their internal owner edges and put

\[
 A_{\rm comp}=E_{\rm int}\setminus\kappa E_{\rm int}.            \tag{10.1}
\]

Any construction which changes only endpoint seams must cut every edge
of \(A_{\rm comp}\) before it can become complement-equivariant.  Thus
\(|A_{\rm comp}|\) is an additional fragmentation ledger.  No
\(o(W/H)\) bound for it is presently proved.

On a complement-coherent subfamily, Lemma 9.1 imposes a second exact
restriction.  Consider two positive-length product paths joined at their
high endpoints.

### Lemma 10.2 (same-half seams are signed-unsafe)

If the endpoint Johnson edge swaps two coordinates both in \(A\), then
the two high endpoints have the same \(B\)-part.  That set belongs to one
unique \(B\)-chain at one fixed rank, so the two forward paths' active
\(B\)-segments share their first increment.  The high-end
forward/reverse seam therefore has a removal-then-reinsertion residence.

If the endpoint edge lies wholly in \(B\), the two paths share an active
\(A\)-increment and have an insertion-then-removal residence.  Hence no
same-half high seam between two positive-length paths is simultaneously
lower and upper \(H\)-safe when the paths have length \(o(H)\).  The
low-end statement is identical.

#### Proof

For an \(A\)-internal endpoint edge, equality of the \(B\)-parts places
both sets in the same unique SCD chain.  Starting at the common high-end
rank, both nonempty active chain segments contain the adjacent chain
increment, so the active \(B\)-sets overlap.  The first path removes that
label and the reversed second path inserts it.  Lemma 9.1 detects the
upper failure.  The \(B\)-internal case is the lower-sign dual. \(\square\)

Thus every signed-safe seam in the short-path core must exchange one
coordinate of \(A\) with one coordinate of \(B\).  These cross-half seams
have a useful exact grading.  If the two half-chain minimum ranks are
\(a,b\), put

\[
                         r=\max(a,b),
 \qquad
                         h=m-2r.                                  \tag{10.2}
\]

Every rank-\(m\) product path at level \(r\) has low/high \(A\)-ranks
\(r,m-r\).  A cross-half endpoint seam therefore joins only adjacent
levels

\[
                         r\longleftrightarrow r+1.                \tag{10.3}
\]

The exact number of paths at level \(r\le\lfloor m/2\rfloor\) is

\[
 N_r=\binom mr^2-\binom m{r-1}^2.                                \tag{10.4}
\]

Indeed \(\binom mr^2\) counts chain pairs with both minima at most \(r\),
and subtraction removes the pairs already present below level \(r\).

### Proposition 10.3 (the level-parity cut is harmless)

Let

\[
                         \Delta_m=\left|\sum_r(-1)^rN_r\right|.   \tag{10.5}
\]

Every cross-half path forest has at least \(\Delta_m\) components, but

\[
                         \Delta_m=o(W/H)                         \tag{10.6}
\]

uniformly for \(H\le m\).

#### Proof

The graph in (10.3) is bipartite by the parity of \(r\), so each path
component has parity-shore imbalance at most one.  This proves the lower
bound.

If \(m=2M\), the alternating Vandermonde identity gives

\[
 \sum_{r=0}^{2M}(-1)^r\binom{2M}{r}^2
       =(-1)^M\binom{2M}{M}.                                    \tag{10.7}
\]

Symmetry and telescoping (10.4) show
\(\Delta_m=\binom mM\), exponentially smaller than \(W/H\).

If \(m=2M+1\), the positive sequence \(N_r\) is increasing for
\(0\le r\le M\), so the alternating-sum bound gives

\[
 \Delta_m\le N_M
   =\binom mM^2\left(1-{M^2\over(M+2)^2}\right)
   =O\left({1\over m}\binom mM^2\right)
   =O\left({W\over m^{3/2}}\right).                              \tag{10.8}
\]

Since \(H\le m\), this is \(o(W/H)\). \(\square\)

The obvious graded Hall cut therefore does not obstruct the desired
forest.  The surviving expansion problem is narrower:

> **Complement-equivariant signed stateful expansion.**  After cutting
> the complement-asymmetric internal edges and the \(o(W/H)\) long paths,
> prove that the cross-half endpoint system has a complement-equivariant
> walk cover carrying valid signed-memory trajectories (9.7)--(9.8), with
> \(o(W/H)\) components and orbit-prefix cost \(o(W)\).

No generic pairwise-seam statement proves this.  It is a stateful
expansion theorem for the actual product-SCD endpoint system, with five
simultaneous constraints: complement closure, cross-half level adjacency,
disjoint \(A\)- and \(B\)-active ports throughout every sliding
\(H\)-window, consistent memory updates, and low prefix-cut weight.  The
parity profile has enough capacity; complement fragmentation and
stateful safe-neighbour expansion remain open.

## 11. The exact two-queue transition

For completeness, write the signed state without suppressing the
off-by-one convention.  Immediately before edge \(t\), let

\[
 \begin{split}
  {\cal I}_t&=(b_s:t-H+1\le s<t),\\
  {\cal R}_t&=(a_s:t-H+1\le s<t),
 \end{split}                                                     \tag{11.1}
\]

in chronological order.  Entries before the beginning of the word are
omitted.  The order records ages; each queue has length at most \(H-1\).
The transition \(a_t\to b_t\) is signed legal exactly when

\[
                  a_t\notin{\cal I}_t,
             \qquad b_t\notin{\cal R}_t.                        \tag{11.2}
\]

After a legal transition,

\[
 \begin{split}
 {\cal I}_{t+1}&=\operatorname{tail}_{H-1}({\cal I}_t,b_t),\\
 {\cal R}_{t+1}&=\operatorname{tail}_{H-1}({\cal R}_t,a_t).
 \end{split}                                                     \tag{11.3}
\]

### Theorem 11.1 (exactness, complement, and necessary memory)

An exchange word preserves every lower and upper flag through depth
\(H\) if and only if every update (11.2) is legal.  Under set
complementation,

\[
                  (X,{\cal I},{\cal R})
        \longmapsto (X^c,{\cal R},{\cal I}),                    \tag{11.4}
\]

and every legal transition is carried to a legal transition.  Hence a
state-valid component and its complement simultaneously preserve the two
signed flag systems.

The \(H-1\) age range is sharp.  No automaton which forgets whether a
specified label occurred \(H-1\) edges earlier can decide all depth-
\(H\) extensions correctly.

#### Proof

The first test in (11.2) forbids exactly an insertion at time \(s<t\)
followed by a removal at time \(t\) with \(t-s+1\le H\).  By Theorem
1.1 this is equivalent to lower safety.  The second test is the
complemented statement and is equivalent to upper safety.  An edge
\(a\to b\) becomes \(b\to a\) under complement, proving (11.4).

For sharpness, compare two legal histories having identical last
\(H-2\) insertion labels, but with a label \(x\) inserted exactly
\(H-1\) edges ago in only the first history.  The next edge may remove
\(x\).  It creates a residence of inclusive length \(H\) in the first
history and none in the second.  The removal-queue version is dual.
\(\square\)

An oriented product path together with its entry seam is therefore not
an edge of a static endpoint graph.  It is a partial map

\[
 \Psi_Q:(X,{\cal I},{\cal R})
       \dashrightarrow (Y,{\cal I}',{\cal R}')                  \tag{11.5}
\]

obtained by reading the seam and the entire path word.  The incoming
queues can contain labels contributed by

\[
                         \left\lceil {H\over \ell}\right\rceil  \tag{11.6}
\]

previous paths when typical path length is \(\ell\).  At
\(H=\sqrt m\,\omega\) and \(\ell=\Theta(\sqrt m)\), this is
\(\Theta(\omega)\) earlier path components.  This is the exact reason a
pairwise-safe endpoint forest cannot be iterated.

## 12. The calibrated forbidden-history calculation

The queue size itself does not produce an exponential-in-
\(\sqrt m\) loss.  The following elementary calculation gives the right
scale.

### Lemma 12.1 (uniform alphabet avoidance)

Let \(F\subset[m]\), \(|F|=f\), and let \(U\) be a uniformly chosen
\(\ell\)-subset of \([m]\).  Then

\[
 \Pr(U\cap F=\varnothing)
     ={\binom{m-f}{\ell}\over\binom m\ell},                    \tag{12.1}
\]

and, when \(f+\ell=o(m)\),

\[
 \log\Pr(U\cap F=\varnothing)
    =-{f\ell\over m}
       +O\left({f\ell(f+\ell)\over m^2}\right).               \tag{12.2}
\]

#### Proof

The ratio in (12.1) is exact.  Write it as

\[
                  \prod_{i=0}^{\ell-1}
                    \left(1-{f\over m-i}\right)
\]

and use \(\log(1-x)=-x+O(x^2)\), uniformly because
\(f+\ell=o(m)\). \(\square\)

Suppose a candidate product path of length \(\ell\) has one active
alphabet in each half, and the two alphabets are uniform after independent
coordinate conjugation of the halves.  Avoiding the entire relevant
incoming insertion and removal queues is stronger than the exact
age-sensitive tests (11.2), and hence supplies a valid lower bound.  If
the two relevant forbidden sizes have sum at most \(2H+O(1)\), then for

\[
                         H=\sqrt m\,\omega,
             \qquad \ell=C\sqrt m,                              \tag{12.3}
\]

Lemma 12.1 gives

\[
             \Pr(\hbox{survival})
                    \ge \exp(-(2C+o(1))\omega).                 \tag{12.4}
\]

For \(\omega=\log\log m\), this is

\[
                         (\log m)^{-2C+o(1)}.                   \tag{12.5}
\]

The estimate remains subpolynomially small uniformly on a core
containing all but \(o(W/H)\) product paths.  Indeed take

\[
 \ell_-={\sqrt m\over\omega},
 \qquad
 \ell_+=\sqrt{m\bigl(\log\omega+3\log\log\omega\bigr)}.         \tag{12.6}
\]

The exact census (6.3), with the central binomial ratio expanded by its
successive factors, gives

\[
 \#\{h<\ell_-\}=O(c_m^2/\omega^2),
 \qquad
 \#\{h>\ell_+\}
     =O\left({c_m^2\over\omega(\log\omega)^3}\right).           \tag{12.7}
\]

Both are \(o(c_m^2/\omega)=o(W/H)\).  On the remaining core, full-queue
avoidance has probability at least

\[
             \exp\bigl(-O(\omega\sqrt{\log\omega})\bigr)
                         =m^{-o(1)}.                             \tag{12.8}
\]

There is therefore no single-history entropy obstruction.

For scale, if \(X\) contains \(a\) coordinates of the first half, its
number of cross-half Johnson neighbours is exactly

\[
                         a^2+(m-a)^2\ge {m^2\over2}.             \tag{12.9}
\]

The product-SCD path density is of order \(m^{-1/2}\), since

\[
                         {c_m^2\over W}
                    =\left({2\over\sqrt\pi}+o(1)\right)m^{-1/2}.
                                                                    \tag{12.10}
\]

Thus an ideally mixed endpoint set has \(\Theta(m^{3/2})\) raw
candidates per endpoint.  Combining (12.4) with this benchmark leaves

\[
               m^{3/2}e^{-O(\omega)}
                   ={m^{3/2}\over(\log m)^{O(1)}}               \tag{12.11}
\]

safe candidates for length \(\Theta(\sqrt m)\), and (12.8) leaves
\(m^{3/2-o(1)}\) on the full core.

Equations (12.11) and (12.8) are annealed benchmarks, not a theorem for
one fixed product SCD.  Conditioning on a literal endpoint and on a
reachable queue can correlate the active alphabets completely.  Nor
does polynomial minimum degree imply a near-spanning path cover.  The
next section gives the exact expansion statement which is sufficient.

## 13. A sufficient history-conditioned Hall theorem

Work after deleting the exceptional paths in (12.7) and, for the signed
equivariant version, after passing to a complement-coherent core.  Let
\({\cal O}\) be the set of complement orbits of the remaining product
paths.  Discarding at most \(K-1\) further orbits, partition it into
equal shelves

\[
                    {\cal O}_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}{\cal O}_K,
             \qquad |{\cal O}_j|=n.                             \tag{13.1}
\]

A conveyor state over shelf \(j\) is a state-valid paired component
which uses one orbit from each of some consecutive shelves ending at
\(j\), together with its current owner, the two queues (11.1), and the
chosen endpoint port.  Suppose shelf \(j\) has already been incorporated.
There is then one current conveyor state for each orbit of
\({\cal O}_j\).  Form the bipartite graph

\[
                         B_j({\cal C}_j)                         \tag{13.2}
\]

whose left vertices are these \(n\) actual current states and whose
right vertices are the orbits in \({\cal O}_{j+1}\).  Join a state to an
orbit if some literal cross-half Johnson seam and some allowed
orientation/port of that orbit make (11.5) defined, make the
complementary transition defined, and have orbit-prefix cost at most a
fixed constant \(C\).  A chosen edge includes one such witness.

Let

\[
 d_j({\cal C}_j)
   =\max_{S\subseteq L(B_j)}\bigl(|S|-|\Gamma_{B_j}(S)|\bigr)_+ \tag{13.3}
\]

be its Hall deficiency.

### Theorem 13.1 (layered two-queue conveyor)

Choose the matchings shelf by shelf.  For every sequence of actual state
families produced in this way, use a maximum matching in
\(B_j({\cal C}_j)\).  The resulting complement-equivariant,
signed-state-valid path cover uses every orbit in (13.1) and has at most

\[
                         p\le n+\sum_{j=1}^{K-1}d_j({\cal C}_j) \tag{13.4}
\]

paired components.  Its total orbit-prefix cost is at most
\(C|{\cal O}|\), and its outer collar length is \(O(Hp)\).

Consequently, for \(H=\sqrt m\,\omega\), it is sufficient to find
\(K\) and shelves for which

\[
 {K\over\omega}\longrightarrow\infty,
 \qquad
 \sum_{j=1}^{K-1}d_j({\cal C}_j)=o(|{\cal O}|/\omega)           \tag{13.5}
\]

along the constructed sequence.  Then the physical component count is
\(o(W/H)\), the two outer signed collars cost \(o(W)\), and bounded seam
cost totals \(O(W/\sqrt m)=o(W)\).

#### Proof

Initially shelf 1 contributes \(n\) components.  At interface \(j\), a
maximum matching has size \(n-d_j\).  Each matched edge joins one old
component to one orbit of the new shelf.  Each of the \(d_j\) unmatched
right orbits starts a new component.  All right orbits, matched or not,
are the \(n\) current component ends for the next stage.  Induction gives
(13.4).  Every matched edge was defined using the full incoming queues,
so Theorem 11.1 proves signed validity globally, including windows
crossing several earlier seams.  Complement closure follows from
(11.4).

Since \(|{\cal O}|=Kn\), the first term in (13.4) is
\(|{\cal O}|/K=o(|{\cal O}|/\omega)\), and (13.5) handles the second.
The collar and prefix estimates follow by summation. \(\square\)

The Hall condition has an exact mixing form.  For a balanced bipartite
graph \(B=(L,R;E)\),

\[
 d(B)=\max_{\substack{S\subseteq L,\ T\subseteq R\\E(S,T)=\varnothing}}
                  (|S|+|T|-n)_+.                               \tag{13.6}
\]

Thus (13.5) asks that every reachable-history-conditioned empty
rectangle have total excess \(o(|{\cal O}|/\omega)\) over all shelves.
This is the precise endpoint mixing/expansion theorem needed.  It is
stronger than mixing of the undecorated product endpoints: its left side
contains the actual two queues produced by all previous shelf choices.

### Corollary 13.2 (uniform reachable-state expansion)

Suppose \(K/\omega\to\infty\) and there is
\(\varepsilon_m=o(1/\omega)\) such that, for every shelf interface and
every conveyor state family reachable from the earlier shelves,

\[
 \max_{\substack{S\subseteq L,\ T\subseteq R\\E(S,T)=\varnothing}}
                         (|S|+|T|-n)_+
                    \le \varepsilon_m n.                        \tag{13.7}
\]

Then the conclusion of Theorem 13.1 holds.

#### Proof

Equations (13.6) and (13.7) give
\[
 \sum_jd_j\le K\varepsilon_m n
            =\varepsilon_m|{\cal O}|
            =o(|{\cal O}|/\omega),
\]
which is (13.5). \(\square\)

Polynomial state degree does not imply (13.6).  For example, let every
one of the \(n\) left states have the same set of \(d=m^{10}\) legal
right neighbours and no others.  Every state has polynomially many safe
extensions, and the construction can be doubled with the queue-swap
involution (11.4), yet

\[
                         d(B)=n-d=\Theta(n).                     \tag{13.8}
\]

Therefore the calculation in Section 12, by itself, cannot prove the
desired cover.  It must be upgraded to uniform control of the physical
empty rectangles (13.6), or to a structured deterministic shelving for
which the accumulated deficiencies in (13.5) are small.

## 14. The remaining exact product-SCD gate

There is an exact raw-degree identity for the actual endpoint resolution.
Fix the SCD of one \(m\)-cube, take
\(0\le r\le\lfloor m/2\rfloor-1\), and let \(\lambda(Z)\) be the minimum
rank of the unique chain containing \(Z\).  Put

\[
 C_r=\binom mr,\qquad B_r=C_r-C_{r-1},\qquad h=m-2r.            \tag{14.1}
\]

A high endpoint at level \(r\) is a pair

\[
 (S,T),\qquad |S|=m-r,\quad |T|=r,\quad
                  \max(\lambda(S),\lambda(T))=r.                \tag{14.2}
\]

There are \(N_r=B_r(C_r+C_{r-1})\) such pairs.  Define

\[
 \begin{split}
 p_r(S)&=|\{x\in S:\lambda(S\setminus\{x\})=r+1\}|,\\
 q_r(T)&=|\{y\notin T:\lambda(T\cup\{y\})=r+1\}|.
 \end{split}                                                     \tag{14.3}
\]

### Proposition 14.1 (exact adjacent-level branching)

The number of cross-half seams from \((S,T)\) to high endpoints at level
\(r+1\) is

\[
 D_r(S,T)=(m-r)\bigl(p_r(S)+q_r(T)\bigr)-p_r(S)q_r(T).          \tag{14.4}
\]

Moreover

\[
 \sum_{|S|=m-r}p_r(S)
  =\sum_{|T|=r}q_r(T)
  =(h-1)C_r,                                                    \tag{14.5}
\]

and hence the average over the actual level-\(r\) endpoint set satisfies

\[
 {1\over N_r}\sum_{(S,T)}D_r(S,T)
   \ge { (m-r)(h-1)C_r\over C_r+C_{r-1}}.                       \tag{14.6}
\]

In particular, throughout any band with
\(h=\Theta(\sqrt m)\), the raw average endpoint degree is
\(\Omega(m^{3/2})\), for every choice of the underlying SCD.

#### Proof

After removing \(x\in S\) and inserting \(y\notin T\), the new pair has
ranks \(m-r-1,r+1\).  It is a level-\((r+1)\) endpoint exactly when
\(\lambda(S-x)=r+1\) or \(\lambda(T+y)=r+1\).  Inclusion-exclusion over
the \((m-r)^2\) pairs \((x,y)\) gives (14.4).

There are \(B_{r+1}\) chains of minimum rank \(r+1\).  Each of their top
sets, of rank \(m-r-1\), has \(r+1\) supersets of rank \(m-r\).
Therefore
\[
 \sum_Sp_r(S)=(r+1)B_{r+1}
  =(r+1)(C_{r+1}-C_r)=(h-1)C_r.
\]
The bottom-set count proving the \(q_r\) identity is identical.

For a fixed \(S\), the number of \(T\)'s for which (14.2) holds is
\(C_r\) if \(\lambda(S)=r\), and \(B_r\) otherwise.  It is therefore at
least \(B_r\).  Thus
\[
 \sum_{(S,T)}\bigl(p_r(S)+q_r(T)\bigr)
             \ge 2B_r(h-1)C_r.                                 \tag{14.7}
\]
Since \(0\le p_r,q_r\le m-r\),
\[
 p_rq_r\le{m-r\over2}(p_r+q_r).
\]
Combine this with (14.4), (14.7), and
\(N_r=B_r(C_r+C_{r-1})\) to obtain (14.6). \(\square\)

Proposition 14.1 upgrades the heuristic raw-degree scale in (12.11) to
an SCD-independent average theorem.  It still does not prove the Hall
gate: the mass in (14.5) may concentrate on a small set of endpoint
ports, and a reachable queue may prune precisely those ports.  The
missing deterministic input is an anti-concentration or empty-rectangle
bound for the quantities (14.3) after chronological queue pruning and
after shelving.

For a reachable signed state \(\sigma=(X,{\cal I},{\cal R})\), let
\({\cal A}(\sigma)\) be the family of chronological removal/insertion
words of all literal cross-half endpoint ports available from \(X\).
The exact obstruction is a dynamic transversal: the aged labels in
\({\cal I}\) and \({\cal R}\) may meet every word in a large target
shelf at a still-forbidden position.  In that event the corresponding
rectangle in (13.6) is empty even though the unconditioned endpoint graph
expands.

Independent coordinate conjugation proves (12.1) for each fixed word
and fixed history, but one global SCD conjugation does not independently
randomize the exponentially many reachable histories.  Hence no union
bound or first-moment argument presently upgrades (12.8) to (13.5).
What has been proved is the following sharp reduction:

1. static pairwise endpoint safety is false under repeated fusion;
2. the exact replacement is the two-queue automaton (11.1)--(11.3);
3. complement symmetry swaps the queues and therefore preserves both
   signs along every state-valid paired component;
4. at \(H=\sqrt m\log\log m\), a fixed history removes only a
   subpolynomial fraction of uniformly conjugated path options, leaving
   polynomial candidate degree under endpoint mixing; and
5. the layered Hall-deficiency criterion (13.5), equivalently the
   history-conditioned empty-rectangle bound (13.6), is sufficient for
   a near-spanning state-valid cover with coefficient-one-compatible
   \(o(W)\) interface cost.

The unresolved theorem is not a generic random-path assertion.  It is a
uniform empty-rectangle theorem for the actual product-SCD endpoint
resolution, simultaneously over the \(\Theta(\omega)\)-path histories
encoded in each reachable state.  A counterexample must exhibit such a
positive-density dynamic-transversal rectangle; an existence proof must
eliminate all of them with total Hall excess \(o(W/H)\).
