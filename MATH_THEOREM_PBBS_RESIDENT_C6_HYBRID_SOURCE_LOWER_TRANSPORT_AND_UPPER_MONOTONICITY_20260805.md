# A resident clean C6 has one source realizing both lower transport and upper monotonicity

**Date:** 2026-08-05  
**Method:** explicit source factorization of the resident q-port cycles;
no computation or search  
**Status:** unconditional local/prospective theorem.  The same depth-`d`
antecedent simultaneously realizes the common-history strict-lower
occurrence bijection and the resident-port all-width internal upper-support
monotonicity.

## 1. Data

Let `K` have rank `r-2`.  Choose distinct

\[
                         a_0,a_1,a_2,c\notin K
\]

and put, cyclically in `i`,

\[
 P_i=K+a_i+a_{i+1},
 \qquad
 Q_i=K+a_i+c.                                     \tag{1.1}
\]

The direct old and fused shores are

\[
                         Q_i\to P_i,
 \qquad
                         Q_i\to P_{i-1}.           \tag{1.2}
\]

Fix `d>=1` and assume `|K|>=d+1`.  Choose distinct

\[
                         x_1,\ldots,x_d\in K
\]

and fresh distinct `y_1,...,y_d`.  Partition

\[
                         K=C_1\dot\cup\cdots\dot\cup C_d  \tag{1.3}
\]

so that `x_j in C_j`.  Such a partition exists because the `x_j` are
distinct; distribute the remaining members of `K` arbitrarily.  Put

\[
                         C'_j=(C_j-\{x_j\})+\{y_j\}.        \tag{1.4}
\]

Every source letter in (1.3)--(1.4) is nonempty.

## 2. Exact source factorization of one resident port

For port `i`, define the cyclic source word of length `2d+2`

\[
 \boxed{
W_i=
 (\{c,a_i\},C_1,\ldots,C_d,
  \{a_i,a_{i+1}\},C'_1,\ldots,C'_d).}             \tag{2.1}
\]

The three copies of a displayed `C_j` or `C'_j` have the same set value
but are distinct source **occurrences**, tagged by their port.  The tags are
retained when contexts are rethreaded.

Let `D` denote consecutive union.

### Theorem 2.1 (literal resident-port antecedent)

The owner cycle `D^d W_i`, based at its first source position, is exactly

\[
 Q_i, P_i=P_{i,0},P_{i,1},\ldots,P_{i,d},
 Q_{i,0},Q_{i,1},\ldots,Q_{i,d-1},                 \tag{2.2}
\]

where `P_(i,j),Q_(i,j)` are the resident q-port return-rail owners.  The
next cyclic owner is `Q_i=Q_(i,d)`.

#### Proof

The first two windows are

\[
 \{c,a_i\}\cup C_1\cup\cdots\cup C_d=Q_i,
\]

and

\[
 C_1\cup\cdots\cup C_d\cup\{a_i,a_{i+1}\}=P_i.
\]

For `1<=j<=d`, shifting across the first `j` primed letters replaces
`x_1,...,x_j` by `y_1,...,y_j` and gives

\[
 P_{i,j}=(K-\{x_1,\ldots,x_j\})
          +\{y_1,\ldots,y_j\}+a_i+a_{i+1}.        \tag{2.3}
\]

The next shift drops the right screen and wraps to the left screen,
swapping `a_(i+1)` for `c`; this is

\[
 Q_{i,0}=(K-X)+Y+c+a_i.                           \tag{2.4}
\]

Subsequent shifts replace `C'_1,...,C'_j` by `C_1,...,C_j`, giving

\[
 Q_{i,j}=K-\{x_{j+1},\ldots,x_d\}
             +\{y_{j+1},\ldots,y_d\}+c+a_i.      \tag{2.5}
\]

These are precisely the displayed resident-rail formulas. `square`

Thus the source is not merely known to exist from residence; it is the
specific common-history source needed below.

## 3. Fusion is literally the complete-head rethread

Write

\[
 L_i=\{c,a_i\},
 \qquad
 R_i=\{a_{i-1},a_i\},
 \qquad
 \mathcal C=(C_1,\ldots,C_d),
 \qquad
 \mathcal C'=(C'_1,\ldots,C'_d).                 \tag{3.1}
\]

Then the old port-`i` cycle (2.1) is

\[
                         (L_i,\mathcal C,R_{i+1},\mathcal C'). \tag{3.2}
\]

Cut the three source cycles immediately before their right screens and
cyclically reconnect the three resulting source paths.  The path attached
after `(L_i,\mathcal C)` begins with

\[
                         (R_i,\mathcal C')          \tag{3.3}
\]

and carries its entire old continuation through the next cut.  At the
owner level the first two windows
become

\[
 K+c+a_i=Q_i,
 \qquad
 K+a_{i-1}+a_i=P_{i-1},                           \tag{3.4}
\]

and the following owners traverse the return rail of port `i-1`.

### Theorem 3.1 (hybrid identity)

The source rethread (3.3):

1. changes the three old resident port cycles into the one fused resident
   q-port cycle `H_3`;
2. is exactly the inverse three-hinge common-history rethread with screens
   `L_i,R_i`, common history `\mathcal C`, and the complete moved right
   path whose leading context is `\mathcal C'`;
3. uses the same `6d+6` source positions before and after the move.

#### Proof

Equation (3.4) is the direct fused shore in (1.2).  After `P_(i-1)`, the
primed context in (3.3) traces the return rail of port `i-1` by Theorem
2.1, and its old cyclic continuation reaches `L_(i-1)`.  Hence the port
index decreases by one after every rail.  Since the index group is `Z_3`,
all three old cycles form one cycle.

Although all three primed contexts have equal set-valued letters, their
occurrence tags differ.  The context placed after role `i` is the one cut
from old port `i-1`; it therefore continues to `L_(i-1)`.  Forgetting
these tags would incorrectly make the three displayed set words look like
three closed cycles and would lose the topology assertion.

Ignoring the carried context, the old fragments are

\[
 (L_i,\mathcal C,R_{i+1}),
\]

and the new fragments are `(L_i,\mathcal C,R_i)`.  With

\[
 L_i=\{c,a_i\},
 \qquad
 R_i=\{a_{i-1},a_i\},
\]

these are exactly the two source families in the common-history clean-C6
normal form.  That theorem explicitly permits the complete right context
to move with the screen, which is (3.3).  Rethreading permutes positions
and neither adds nor removes one. `square`

## 4. Simultaneous consequences

### Theorem 4.1 (one packet closes all three local rows)

For the resident fusion `H_2 -> H_3` equipped with the source (2.1):

1. every strict-lower source interval occurrence has a value-, width-, and
   occurrence-preserving image;
2. every occurrence-labelled strict-lower compiler matching transports
   exactly, so a zero-defect gap-section compiler remains zero defect;
3. every nonconstant positive owner run has length at least `d+1`;
4. the complete owner/lower-q1/upper-q1/tail/head signatures are identical;
5. the three old components become one; and
6. for complete **internal cyclic owner intervals**,

   \[
                  Deck_{cyc}(H_2)\subseteq Deck_{cyc}(H_3). \tag{4.1}
   \]

Hence the fusion deletes no last internal upper witness at any width.

#### Proof

Items 1--2 follow from Theorem 3.1 and the common-history occurrence
bijection.  Items 3--6 are the resident q=3 port theorem.  Theorem 2.1
proves that both results concern the same literal source/owner packet,
not two incompatible existential factorizations. `square`

### Corollary 4.2 (serial transport, and the regeneration qualification)

For any finite serial sequence of prospectively planted hybrid moves, the
strict-lower occurrence bijections compose and preserve a transported
zero-defect compiler, even with arbitrary transported contexts.

The internal upper-support inclusions also compose **only when**, at every
step, the three old declared components are the complete closed resident
port cycles of Theorem 2.1 (or an additional theorem protects every added
exterior interval).  In particular, after one fusion its large output
cycle is not automatically a fresh `H_2` port cycle for the next move.

#### Proof

The lower assertion is ordinary composition of the common-history
bijections.  For the upper assertion, Theorem 4.1(6) classifies all cyclic
intervals of the complete displayed port components; it has no statement
about an extra body spliced into one of those cycles.  Under the stated
whole-component hypothesis, support inclusion is transitive. `square`

Thus no commutativity is required for serial lower transport.  A global
upper-monotone loose forest additionally needs regeneration of whole
resident port components, or protected exterior witnesses.  Physical
resource/halo separation is also still required to assert that several
packets coexist as one typed factor.

## 5. Exact remaining boundaries

The hybrid theorem is internal and prospective.  It does not prove:

1. that the canonical PBBS factor already contains the `6d+6`-position
   resident source packet;
2. a Catalan-scale or positive-density packing of such packets;
3. preservation of intervals which cross from a packet into an arbitrary
   fixed exterior;
4. protection of arbitrary-width **owner-upper** intervals after cutting
   the final cyclic owner chronology into a linear word;
5. zero-gap residence;
6. transport of typed/shared common-cap routes beyond the literal lower
   cell; or
7. regeneration of a new packet bank after a same-parity lift.

In particular, (4.1) is an internal cyclic support statement.  The raw
private-prefix counterexample is removed because the return rails replace
the arbitrary local exterior, but a later global opening or overlapping
external context still needs a protected witness/cut theorem.

For clarity, the lower source opening itself is no longer a gate once the
topology has one terminal source cycle: append its first `d` source letters.
The resulting length-`W+d` linear source contains every cyclic source
interval of width at most `d+1`, so all owners and all transported lower
compiler cells survive.  This standard deadline collar does not preserve
an owner interval of arbitrary width crossing the owner cut, which is why
the upper opening remains in the list above.

The former local dichotomy is nevertheless closed: one no longer has to
choose between native lower transport and resident upper monotonicity.
The explicit source (2.1) supplies both in the same resident topology
packet.
