# Two conjugate sectors exchange their internal deck, but exact q1 sockets close them into a cycle

Date: 2026-08-01  
Lane: AD, shared-bank residence refresh  
Status: exact two-block exchange theorem, exact source/native/residence collar,
and exact local no-go.  An endpoint-to-endpoint conjugate bank or a
three-or-more-block delta router remains open.  No common-cap or global
OR-word completion is claimed.

**Quantifier correction.**  The cycle no-go below concerns a transparent
exchange which preserves the old named owner/q1 multisets inside a fixed
degree-two chronology.  It does not apply when the global factor is chosen
anew around the refreshed paths.  Under that weaker and now authoritative
quantifier, the refreshed paths are a positive protected diamond bank; see
`MATH_THEOREM_AD_REFRESHED_A_SECTOR_PROTECTED_DIAMOND_BANK_AND_ACCUMULATION_GATE_20260801.md`.

## 0. Verdict

The proposed coordinate-conjugation mechanism is real but does not give an
old-row-transparent local recurrence refresh.

If two ordered owner blocks are pointwise conjugate under a coordinate
transposition, conjugating both blocks exchanges them.  Their owner
multiset and every internal physical edge, lower intersection, and upper
union are preserved exactly.  Only four exterior ports remain.

There is, however, a sharp obstruction at those ports.  A fixed owner that
is Johnson-adjacent to both conjugate endpoint owners is transparent on
exactly one q1 shore, never both.  Its nonconstant q1 colour orbit uniquely
determines that physical owner.  Hence cancelling all boundary q1 deltas
forces opposite switch directions to use the same socket owner.  In a
degree-two chronology, the two conjugate paths and the two paired sockets
therefore form a closed cycle.  They cannot be an exact transparent proper
submove of a larger Hamilton path.

There is one precise noncyclic exception: a conjugate bank may run from one
global chronology endpoint to the other, because the two absent exterior
edges need no q1 cancellation.  Otherwise one needs at least one of:

1. a third block or a global alternating delta router;
2. explicit q1 colour rehosting/surplus; or
3. a component merge after the conjugate exchange.

The split-core prefix fails even before this topology gate.  At the first
expiry, the two `D^-` source positions have only one valid owner-support
flank; their would-be conjugate flank lies before the global word.  The
local transposition therefore changes exactly `b` owners and `b` colours
on each q1 shore.  Complete four-sector set coverage does not manufacture
the missing source flank.

## 1. The two-position support telescope

Let a source word be

\[
                         A=(A_0,\ldots,A_{n-1})
\]

and let its depth-`h` owner row use windows of length

\[
                              H=h+1,
 \qquad O_i=\bigcup_{k=i}^{i+h}A_k.                  \tag{1.1}
\]

Choose positions `p<q` with

\[
                              s=q-p\le H.             \tag{1.2}
\]

Let `tau=(x y)` be a coordinate transposition and suppose the source edit
at `p,q` interchanges the unique active roles of `x,y`.  A window containing
both edited positions or neither has unchanged union.  The starts of
windows containing `p` but not `q`, and `q` but not `p`, are respectively

\[
 I=[p-h,q-h-1],\qquad J=[p+1,q].                     \tag{1.3}
\]

Both intervals have length `s` and

\[
                              J=I+H.                  \tag{1.4}
\]

Intersect (1.3) with the valid owner-start range when a source position is
within `h` of a global endpoint.

Assume first that both flanks are full and that the exact ordered
conjugacy condition holds:

\[
                         O_{i+H}=\tau O_i
                    \qquad(i\in I).                  \tag{1.5}
\]

Also assume that the source edit really conjugates each affected owner;
equivalently, no unedited occurrence masks the changed `x/y` membership in
an affected window.  Then

\[
 O'_i=O_{i+H},\qquad O'_{i+H}=O_i\qquad(i\in I).     \tag{1.6}
\]

Thus the two owner blocks are exchanged pointwise.  Their owner multiset is
unchanged.  Every internal edge in the first block becomes the
corresponding old edge in the second and conversely, so their complete
internal lower-intersection and upper-union multisets are also unchanged.

Multiset conjugacy without the order in (1.5) is not enough: it preserves
vertices but need not preserve the internal edge deck.  Sections 2--3
assume `s<=h`, so the two blocks have four distinct exterior ports.  When
`s=H` they are adjacent and their mutual seam must first be contracted into
the boundary ledger.

## 2. Exact four-port owner/q1 criterion

Write the conjugate paths as

\[
 P=(X_0,\ldots,X_{s-1}),\qquad
 Q=(Y_0,\ldots,Y_{s-1})=\tau P,                      \tag{2.1}
\]

and their four exterior neighbours as `a,b,c,d`.  Before the exchange the
boundary edges are

\[
 aX_0,\quad X_{s-1}b,\quad cY_0,\quad Y_{s-1}d.     \tag{2.2}
\]

Afterwards they are

\[
 aY_0,\quad Y_{s-1}b,\quad cX_0,\quad X_{s-1}d.     \tag{2.3}
\]

### Theorem 2.1 (exact two-block collar)

At owner plus both-q1 multiset scope, the conjugate exchange is exact if
and only if:

1. all four pairs in (2.3) are Johnson edges;
2. the following lower-colour multisets are equal:

\[
 \{a\cap X_0,X_{s-1}\cap b,c\cap Y_0,Y_{s-1}\cap d\}
 =
 \{a\cap Y_0,Y_{s-1}\cap b,c\cap X_0,X_{s-1}\cap d\}.
                                                               \tag{2.4}
\]

3. the analogous upper-colour multisets are equal:

\[
 \{a\cup X_0,X_{s-1}\cup b,c\cup Y_0,Y_{s-1}\cup d\}
 =
 \{a\cup Y_0,Y_{s-1}\cup b,c\cup X_0,X_{s-1}\cup d\}.
                                                               \tag{2.5}
\]

The owner delta is zero.  The exact signed q1 boundary deltas are the right
side minus the left side in (2.4), respectively (2.5).  Hence (2.4)--(2.5)
are also an exact certificate of every missing and duplicate q1 colour if
closure fails.

#### Proof

Equation (1.6) proves the owner and internal-edge assertions.  Only the
four edges (2.2) are not carried to an old internal or boundary edge.
Johnson legality is therefore exactly condition 1, and taking their
intersections and unions gives (2.4)--(2.5).  \(\square\)

For a literal source word, one more condition is load-bearing.  At an edge
between owner starts `i,i+1`, put

\[
 S_i=\bigcup_{k=i+1}^{i+h}A'_k.                      \tag{2.6}
\]

Then

\[
 O'_i\cap O'_{i+1}
   =S_i\cup(A'_i\cap A'_{i+h+1}).                   \tag{2.7}
\]

Thus the native lower-q1 cell is exact if and only if

\[
 A'_i\cap A'_{i+h+1}\subseteq S_i                  \tag{2.8}
\]

at each new cut.  The `h+2` spanning source letters automatically have OR
\(O'_i\cup O'_{i+1}\); an application with typed source positions must also
retain that spanning interval as an admissible upper cell.

## 3. The sharp socket dichotomy

Let

\[
                    X=C\cup\{x\},\qquad
                    Y=C\cup\{y\},                   \tag{3.1}
\]

where `|X|=|Y|=r`, `x,y notin C`, and `x!=y`.

### Lemma 3.1 (every common Johnson socket has one transparent shore)

A rank-`r` owner `u` is Johnson-adjacent to both `X` and `Y` if and only if
it has exactly one of the following forms:

\[
\begin{array}{ll}
 \text{type 0:}&u=C\cup\{z\},\quad z\notin C\cup\{x,y\};\\[2mm]
 \text{type 2:}&u=(C-\{c_0\})\cup\{x,y\},\quad c_0\in C.
\end{array}                                           \tag{3.2}
\]

At a type-0 socket the lower colour is fixed and the upper colour toggles:

\[
 u\cap X=u\cap Y=C,
 \qquad C\cup\{x,z\}\longleftrightarrow C\cup\{y,z\}.       \tag{3.3}
\]

At a type-2 socket the upper colour is fixed and the lower colour toggles:

\[
 u\cup X=u\cup Y=C\cup\{x,y\},
 \qquad (C-\{c_0\})\cup\{x\}
       \longleftrightarrow(C-\{c_0\})\cup\{y\}.             \tag{3.4}
\]

In particular, no fixed socket is transparent on both q1 shores.

#### Proof

A common neighbour differs from each of `X,Y` by one deletion and one
addition.  It either contains neither of `x,y`, forcing it to retain all of
`C` and add one `z`, or contains both, forcing it to delete one member of
`C`.  Containing exactly one would make it equal to one of `X,Y` or more
than one Johnson step from the other.  Equations (3.3)--(3.4) are direct.
\(\square\)

The nonconstant colour orbit recovers the socket itself:

\[
 u=(C+x+z)\cap(C+y+z)\quad\text{in type 0},          \tag{3.5}
\]

and

\[
 u=((C-c_0)+x)\cup((C-c_0)+y)\quad\text{in type 2}. \tag{3.6}
\]

### Theorem 3.2 (two-block exactness forces a closed cycle)

Suppose `P,Q=\tau P` are disjoint proper internal paths in a simple
degree-at-most-two owner chronology, and every port is **aligned**: its old
and new path endpoints are one conjugate pair `C+x,C+y`.  A simultaneous
reversal of both paths is allowed after reindexing; independent or crossed
endpoint permutations are not asserted here.  Suppose conjugating the
paths preserves both q1 colour multisets exactly and does not rehost colours
outside the four ports.

Every port with direction `x to y` has a nonconstant q1 orbit by Lemma
3.1.  Exact multiset cancellation requires a port with direction `y to x`
in the same orbit.  Equations (3.5)--(3.6) force that opposite port to use
the same physical socket owner.  Degree at most two then makes the two
ports the two incident edges of that socket.

Consequently the four ports pair at two fixed sockets, and

\[
             P+\text{socket}+Q+\text{socket}         \tag{3.7}
\]

is a closed cycle component.  Therefore a two-block conjugation cannot be
an exact transparent proper submove inside a larger Hamilton path or a
connected path forest component.

If a boundary edge is absent, it must be at a global chronology endpoint.
The only noncyclic two-block possibility is consequently an
endpoint-to-endpoint conjugate bank.  With one paired internal socket and
two distinct external sockets, the remaining signed q1 delta contains at
least one negative and one positive colour orbit; it cannot vanish.

## 4. Exact residence collar

Let the required signed residence threshold be `H=h+1`.  Because the two
internal binary traces are exchanged, an old internally resident pair of
blocks can create new defects only in runs meeting one of the four exterior
joins.

For a binary trace fragment `w`, retain its first and last bit and the
lengths of its initial and terminal constant runs, capped at `H`.  At each
new join concatenate:

1. the last `H` trace bits in the fixed left exterior;
2. the complete inserted block trace (or its first/last `H` bits if it is
   longer than `2H`); and
3. the first `H` trace bits in the fixed right exterior.

### Lemma 4.1 (finite residence collar)

Assuming all runs not meeting a changed join were resident before the
exchange, the new chronology is resident if and only if, for each
coordinate moved by `tau`, every maximal constant run meeting one of the
four joins and not meeting a global endpoint has length at least `H` in
the displayed collar concatenation.

This is an exact finite state of capped run ages; old residence alone does
not imply it.  For example, take threshold `H=6` and a two-owner conjugate
block.  Give coordinate `y` a left exterior positive shoulder of exact age
four, preceded by zero, and let the old block begin with two `y`-positive
owners.  Its old joined run has length six.  After conjugation the block
begins with two `y`-zero owners, exposing the interior run of four, which is
illegal.  The other collars can be padded by constant runs of length at
least six.  Owner and q1 collar legality can therefore coexist with a
residence failure.  A residence-safe sector bank must export these four
capped run states in addition to (2.4)--(2.8).

No fixed `h`-collar proves arbitrary-width OR-deck or common-cap
compatibility.  Those remain separate prefix/suffix-screen and typed-cell
conditions.

## 5. Application to the first split-core expiry

Start from disjoint banks at depth `b>=2`.  The first expiry is after
`b+1` jumps, at depth

\[
                              h=2b+1.                 \tag{5.1}
\]

Put `g=gamma_(b+1)` and let

\[
                              \tau_L=(\gamma_1\ g).   \tag{5.2}
\]

In zero-based source coordinates inside `D^-`, the two cells are at

\[
                              p=0,\qquad q=b.         \tag{5.3}
\]

Equations (1.3) give

\[
 I=[-2b-1,-b-2],\qquad J=[1,b].                      \tag{5.4}
\]

The first flank lies strictly before the global source word.  Hence the
two-block antecedent (1.5) is false in the literal prefix packet.  The only
changed owners are

\[
                              L_1,\ldots,L_b.         \tag{5.5}
\]

Writing

\[
 I^L_u=L_u\cap L_{u+1},\qquad
 J^L_u=L_u\cup L_{u+1},                              \tag{5.6}
\]

the exact one-sided signed deltas are

\[
 \Delta\mathcal O_L
   =\sum_{u=1}^{b}([\tau_L L_u]-[L_u]),              \tag{5.7}
\]

\[
 \Delta\mathcal I_L
   =\sum_{u=0}^{b-1}([\tau_L I^L_u]-[I^L_u]),        \tag{5.8}
\]

\[
 \Delta\mathcal J_L
   =\sum_{u=1}^{b}([\tau_L J^L_u]-[J^L_u]).          \tag{5.9}
\]

Every displayed negative atom and every positive atom is distinct.  Thus
the local gamma refresh removes and adds exactly

\[
          b\text{ owners},\qquad b\text{ lower-q1 colours},
          \qquad b\text{ upper-q1 colours}.          \tag{5.10}
\]

It is rank-safe, Johnson, native-q1 literal, and residence-repairing; it is
not owner/palette closed.

The `D^+` old/new transposition has its second support flank only if the
exterior continuation supplies enough source positions and satisfies the
ordered conjugacy (1.5).  Complete four-sector owner coverage proves
neither fact.  Even if remote conjugate flanks are supplied on both shores,
Theorem 3.2 says exact two-block q1 closure makes each internal pair a
cycle, unless the bank is routed between the two global endpoints.

Therefore the proposed whole complementary-sector permutation does not
implement a local shared-bank recurrence refresh.  The weakest surviving
positive gate is an endpoint-bearing conjugate source bank with:

1. ordered physical conjugacy (1.5);
2. Johnson and native-cell conditions (2.3)--(2.8);
3. the four residence collar states of Lemma 4.1; and
4. either global endpoint routing or a third-block/q1-delta router.

Common-cap compilation and arbitrary-width OR guards are still additional
requirements.

## 6. Independent audit and scope

The deterministic audit

`scratch/audit_ad_two_sector_coordinate_conjugation_20260801.py`

replays `b=2,...,12`.  It checks (5.3)--(5.10), literal native q1,
Johnson legality, and that only the alpha-side defect remains after the
one-sided gamma transposition.  It also exhausts the dimension-free socket
classification for `5<=n<=8` and every nontrivial Johnson rank, verifying
(3.2)--(3.6).

This finite replay audits formulas; the proofs above are dimension-free.
No remote conjugate sector, endpoint-to-endpoint bank, common cap, or
global literal OR word is constructed.
