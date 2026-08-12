# Literal splicing of collar-neutral two-top rectangles

## Exact owner census, port-paid installation, and the dense-flow obstruction

Date: 2026-07-27

Scope: constant-one Gaussian-annulus program; pure mathematics only.
No computation, search, solver, or external theorem is used.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,                          \tag{0.1}
\]

and assume \(H\ge3\), \(m\ge6H+4\).  Let

\[
                         L=H+\delta-1,\qquad1\le\delta\le H\tag{0.2}
\]

be the safe ordered-port length.

A collar-neutral rectangle consists of two length-\(d\) promotion paths
on two tops.  Each shore has \(2d\) principal owner occurrences but only

\[
                             2d-2                              \tag{0.3}
\]

distinct owners: the two paths necessarily share the owners at phases
one and three.  An adjacent boundary swap changes exactly \(L+1\)
collared ordered ports on each top, hence

\[
                             P_\square=2(L+1)                  \tag{0.4}
\]

ports per rectangle.

Let a top-disjoint bank contain \(r\) rectangles, choose one shore of
each, and let \(\mu\) be its middle-owner occurrence load.  Define

\[
 K=|\operatorname{supp}\mu|,\qquad
 \operatorname{rep}(\mu)=\sum_D(\mu_D-1)_+=2dr-K.             \tag{0.5}
\]

Using the already proved useful-prefix frame compiler as a black box,
the bank has a literal OR word of exact constructed length

\[
 \boxed{
 |w|=2dr+4Hr
     =K+\operatorname{rep}(\mu)+4Hr.}                          \tag{0.6}
\]

If \(P=2(L+1)r\) is the total changed-port count, then

\[
                         |w|\le K+\operatorname{rep}(\mu)+2P. \tag{0.7}
\]

Consequently the desired word bound for this direct installed-path
compiler,

\[
                         |w|=K+O(P)                            \tag{0.8}
\]

holds precisely when, in its exact ledger, the owner-repeat excess is
\(O(P)\).  This is a sufficient literal construction statement, not a
lower bound against every conceivable word which represents only a
subcollection of the advertised path flags.  In the clean
coefficient-one case the
supports of distinct rectangles are externally disjoint.  Then the only
repeats are the two forced internal owners per rectangle,

\[
                         \operatorname{rep}(\mu)=2r,           \tag{0.9}
\]

and one gets the explicit bound

\[
                         |w|<K+2P.                             \tag{0.10}
\]

This closes the literal word interface for a **static top-disjoint
rectangle bank**.

It does not compose the \(\Omega(W)\) formal rectangle
moves required by the dense-recycling proposal.  A top-disjoint bank has
at most \(\binom{2m}{M}/2\) rectangles, which is \(O(W/m)\) at the
calibrated top scale of the dense-recycling proposal.  To use
\(\Omega(W)\) rectangles, their option changes must telescope on each
top to one initial and one final path, and the paired moves must admit one
common chronological ordering.  More strongly, for the fixed-root
rectangle library the option graph at each top is a disjoint union of
two-vertex components.  Repeated uses merely alternate and cancel, so a
coefficient-one endpoint table retains at most one net swap per top.  At
the calibrated scale this moves only \(O(W/m)=o(W)\) middle mass.  Thus
the proposed \(\Omega(W)\) dense recycling is impossible unless a new
re-rooting or tail-changing primitive is added.

## 1. The two-top rectangle and its retained owners

Fix disjoint data

\[
 |R|=m-2,\qquad a,b,z,z'\notin R,                            \tag{1.1}
\]

with \(a,b,z,z'\) distinct.  Let \(F\) be an ordered \((H-3)\)-set,
let \(x,y\) be two further labels, and put

\[
 \begin{aligned}
 U&=R\cup\{a,b,z,z'\}\cup F\cup\{x\},\\
 U'&=R\cup\{a,b,z,z'\}\cup F\cup\{y\}.
 \end{aligned}                                                \tag{1.2}
\]

For an order \(\rho\) of \(R\), use

\[
 \begin{aligned}
 \pi&=(a,b,x,F,z,z',\rho),\\
 \pi'&=(b,a,y,F,z',z,\rho).
 \end{aligned}                                                \tag{1.3}
\]

Let \(\widehat\pi,\widehat\pi'\) swap the first two letters.  The old
shore is \((U,\pi),(U',\pi')\), and the new shore is
\((U,\widehat\pi),(U',\widehat\pi')\).

For a top order \(\theta\), the retained middle owner at phase \(i\) is

\[
                         X_i(\theta)
 =U(\theta)\setminus\{\theta_i,\ldots,\theta_{i+H-1}\},
 \qquad1\le i\le d.                                          \tag{1.4}
\]

All displayed intervals are nonwrapping in the written order.

### Lemma 1.1 (exact internal owner collisions)

On either shore:

1. each individual path has \(d\) distinct owners;
2. the two paths have exactly two common owners, at equal phases
   \(i=1\) and \(i=3\); and
3. their union therefore has \(2d-2\) owners and repeat excess two.

#### Proof

Different nonwrapping length-\(H\) intervals of one injective order are
different, proving Item 1.

An owner from \(U\) can equal one from \(U'\) only if its deleted
interval contains \(x\), while the other deleted interval contains
\(y\).  These labels occupy position three, so only phases
\(1,2,3\) can participate.  On the old shore, the six relevant owners
are

\[
 \begin{array}{c|ccc}
       &1&2&3\\ \hline
 U    &R+z+z'&R+a+z'&R+a+b\\
 U'   &R+z+z'&R+b+z &R+a+b.
 \end{array}                                                  \tag{1.5}
\]

The four labels are distinct, so the only equalities are in columns one
and three.  On the new shore the phase-two entries become

\[
                         R+b+z',\qquad R+a+z,                  \tag{1.6}
\]

while columns one and three are unchanged.  The same conclusion follows.
\(\square\)

The phase-two difference of new minus old is the collar-neutral
hypersimplex rectangle

\[
 e_{R+a+z}+e_{R+b+z'}-e_{R+a+z'}-e_{R+b+z}.                  \tag{1.7}
\]

At every other protected complementary length the two-top derivative is
zero.  We use this audited identity without reproving it.

## 2. Exact collared-port census

The retained path uses phase starts \(1,\ldots,d\).  Its literal entrance
collar includes the cyclic length-\(L\) port starts

\[
                         2-L,3-L,\ldots,0,                    \tag{2.1}
\]

before the retained phase starts.  Thus every length-\(L\) cyclic port
which contains position one or two belongs to the installed path plus
its entrance collar.

### Lemma 2.1 (one adjacent swap changes \(L+1\) ports)

For two cyclic orders which differ by interchanging adjacent positions
one and two, exactly \(L+1\) phase-indexed ordered length-\(L\) ports
differ.

#### Proof

Each position belongs to \(L\) cyclic length-\(L\) intervals.  Exactly
\(L-1\) such intervals contain both adjacent positions.  Their union
therefore has size

\[
                         L+L-(L-1)=L+1.                       \tag{2.2}
\]

An interval containing neither position is unchanged.  An interval
containing exactly one has a different label in that slot.  An interval
containing both has the same label set but the two labels occur in the
opposite ordered slots, so its ordered port also changes.  Hence all and
only the \(L+1\) intervals in the union change. \(\square\)

### Corollary 2.2 (one rectangle changes \(2(L+1)\) ports)

The two top identities are distinct, so their port changes do not cancel.
Thus one collar-neutral rectangle has the exact changed-port count

\[
                             P_\square=2(L+1).                 \tag{2.3}
\]

This is an ordered splice-port count.  It is separate from the protected
target collateral, which cancels exactly between the two tops.

## 3. Literal word for a static rectangle bank

We use the useful-prefix path compiler proved in
`MATH_THEOREM_CONVEYOR_BANK_LITERAL_OR_SPLICE_AND_DELAY_H_BOUNDARY_20260727.md`.
Its proof applies verbatim after truncating a promotion cycle: a
length-\(d\) promotion path has a literal word with

\[
                         d\text{ principal endpoints}+2H
                         \text{ nonprincipal endpoints}.      \tag{3.1}
\]

No part of that interface theorem is reproved here.

Let \(\mathcal B\) contain \(r\) top-disjoint rectangle macros, and
choose either shore of each.  Let \(\mu\) count all principal owner
occurrences of the resulting \(2r\) paths.

### Theorem 3.1 (literal rectangle-bank compiler)

There is a literal OR word for the bank of length

\[
 \boxed{
 |w|=2r(d+2H)
     =K+\operatorname{rep}(\mu)+4Hr,}                          \tag{3.2}
\]

where \(K,\operatorname{rep}(\mu)\) are defined in (0.5).  Every
principal endpoint has exactly the useful-prefix lower and upper OR
windows of its selected literal path.  The phase-two middle-owner change
is exactly the sum of the selected rectangles (1.7), and all companion
path collateral is present in the same word.

#### Proof

Apply the existing length-\(d\) path compiler independently to the two
paths of every rectangle and concatenate the words.  This gives
\(2dr\) principal and \(4Hr\) nonprincipal endpoints.  Since

\[
                         2dr=K+\operatorname{rep}(\mu),        \tag{3.3}
\]

the length is (3.2).  The compiler's last-occurrence-state theorem gives
all advertised OR windows literally.  The two paths, including the
changed companion top, are both compiled; nothing is represented only
in a signed ledger. \(\square\)

Let

\[
                         P=2(L+1)r                            \tag{3.4}
\]

be the bank's changed-port count.

### Corollary 3.2 (new owners plus changed ports)

For every static top-disjoint bank,

\[
                         |w|\le K+\operatorname{rep}(\mu)+2P.\tag{3.5}
\]

Hence this compiler gives \(|w|=K+O(P)\) exactly when
\(\operatorname{rep}(\mu)=O(P)\).

If different rectangle supports are externally disjoint, then
\(\operatorname{rep}(\mu)=2r\) by Lemma 1.1 and

\[
                         |w|=K+(4H+2)r<K+2P.                  \tag{3.6}
\]

#### Proof

Since \(L\ge H\),

\[
                         4Hr\le4(L+1)r=2P.                   \tag{3.7}
\]

This proves (3.5).  In the externally disjoint case insert
\(\operatorname{rep}(\mu)=2r\); strict inequality in (3.6) follows from
\(4H+2<4L+4\). \(\square\)

The equivalence in the first paragraph is quantitative for this literal
path installation: every advertised path occurrence is a physical word
endpoint.  Owner collisions cannot be removed by renaming them
nonprincipal without leaving their symbols in the word.

## 4. Exact owner/installability condition

Let \(\lambda\in\{0,1\}^{\binom{[2m]}m}\) be the owner load already
installed outside the rectangle bank.  Let \(S=\operatorname{supp}\mu\)
be the owner support of the chosen rectangle shores.

### Theorem 4.1 (static designated-owner installability)

A chosen top-disjoint rectangle bank extends the existing partial owner
factor with one designated occurrence of every owner in \(S\) if and
only if

\[
                         \lambda_D+\mathbf1_{D\in S}\le1
                         \qquad\text{for every }D.             \tag{4.1}
\]

The resulting literal word has coefficient-one length

\[
 |\operatorname{supp}\lambda|+|S|
 +\operatorname{rep}(\mu)+4Hr                              \tag{4.2}
\]

apart from whatever interface excess was already paid for the exterior
word.  In particular the total new excess is \(O(P)\) if and only if the
external-plus-internal repeat mass is \(O(P)\).

#### Proof

Condition (4.1) is plainly necessary for one designated owner occurrence.
If it holds, designate one of the \(\mu_D\) physical endpoints for every
\(D\in S\), and regard the remaining
\(\sum_D(\mu_D-1)_+\) endpoints as nonprincipal.  Theorem 3.1 supplies
one literal word containing all of them and all their OR flags.  Its
length ledger is exactly (4.2). \(\square\)

For a complete middle factor, (4.1) is supplemented by the equality

\[
                 \operatorname{supp}\lambda\ \dot\cup\ S
                 =\binom{[2m]}m.                              \tag{4.3}
\]

Equations (4.1)--(4.3), not merely zero singleton marginals of the signed
rectangle sum, are the exact owner installation gate.

No unpunctured rectangle shore is occurrence-squarefree as a two-path
table: Lemma 1.1 forces multiplicity two at two owners.  Theorem 4.1
instead designates one occurrence and charges the other two endpoints to
word excess.  If literal occurrence-squarefreeness is demanded, the
additional exact condition is

\[
                         \lambda_D+\mu_D\le1\quad\text{for all }D, \tag{4.4a}
\]

which the displayed rectangle violates internally.  Puncturing one copy
would require a new collar audit and is not part of the current macro.

### Corollary 4.2 (ambient literal splice)

Assume (4.1), and insert the rectangle bank between a prefix and suffix
of an existing literal word.  The reset-collared insertion theorem from
the conveyor-bank interface note gives a word whose additional length,
beyond the \(K\) newly designated owners, is at most

\[
                         \operatorname{rep}(\mu)+3P.          \tag{4.4}
\]

It preserves every old OR witness lying wholly outside the chosen cut
and realizes every advertised rectangle-path OR window.

#### Proof

The standalone bank costs
\(\operatorname{rep}(\mu)+4Hr\) beyond its distinct owners.  Reinstalling
the first useful prefix required by the old suffix costs at most
\(2H+1\) further symbols.  For \(r\ge1\),

\[
 4Hr\le2P,
 \qquad
 2H+1\le2(L+1)r=P.                                           \tag{4.5}
\]

The source-blind initialization and OR-window preservation are exactly
the existing reset-collared insertion theorem. \(\square\)

## 5. Dense rectangle composition is a synchronized option flow

The preceding bank is static and top-disjoint.  We now characterize what
is required to compress a much longer formal rectangle decomposition.

For every top \(U\), let \(\mathcal G_U\) be the directed graph whose
vertices are literal retained path options on \(U\), and whose directed
edges are legal boundary swaps \(p\to p'\).  A physical rectangle pairs
one edge of \(\mathcal G_U\) with one oppositely collared edge of
\(\mathcal G_{U'}\).

Let \(\mathcal R\) be a multiset of oriented rectangle occurrences.  At
top \(U\), let \(f_U\) be the resulting multiset of directed option
edges, and put

\[
 \partial f_U=
 \sum_{(p\to p')\in f_U}(e_{p'}-e_p).                         \tag{5.1}
\]

### Theorem 5.1 (static top-one telescoping criterion)

Fix one initial option \(p_U^0\) at every used top.  The formal rectangle
sum compresses to one final literal option per top if and only if, for
every \(U\), there is an option \(p_U^1\) such that

\[
                         \partial f_U=e_{p_U^1}-e_{p_U^0}.    \tag{5.2}
\]

When (5.2) holds, the complete protected deck difference of the final
static table minus the initial table is exactly the sum of the rectangle
differences.  In particular all nonmiddle collar rows still cancel.

#### Proof

Necessity follows because a coefficient-one table has one option at top
\(U\): its exponent difference is
\(e_{p_U^1}-e_{p_U^0}\).

Conversely, apply the linear physical deck map at top \(U\) to (5.2) and
sum over all tops.  The left side is the sum of the option-edge deck
differences in the rectangle occurrences; the right side is the final
option deck minus the initial option deck.  Pairwise rectangle collar
cancellation on the left therefore proves the same cancellation for the
two static endpoint tables. \(\square\)

Condition (5.2) is algebraic endpoint installability.  To realize the
rectangles as an actual sequence of intermediate coefficient-one tables
requires more.

### Theorem 5.2 (exact chronological installability)

The rectangle multiset \(\mathcal R\) has a chronological realization
from \((p_U^0)_U\) to \((p_U^1)_U\), using every occurrence once, if and
only if one can choose, at every top \(U\), an ordering of its incident
edge occurrences which

1. is a directed trail in \(\mathcal G_U\) from \(p_U^0\) to
   \(p_U^1\); and
2. induces, together with the orders at all other tops, an acyclic
   precedence relation on the rectangle occurrences.

A chronological realization admits a coefficient-one designated-owner
set at every time if and only if, in addition, after every prefix of a
common topological ordering its current option table satisfies the owner
capacity condition (4.1).  It is occurrence-squarefree only under the
stronger pointwise condition (4.4a).

#### Proof

In any physical chronology, the moves incident with one top occur in the
order in which the unique current option changes.  They therefore form
the directed trail in Item 1.  Their local orders are all restrictions of
one global chronological order, so their union has no precedence cycle.
Every intermediate table must satisfy (4.1).

Conversely, take a topological ordering of the acyclic precedence
relation.  When a rectangle occurrence is reached, all earlier incident
edges at each of its two tops have already occurred and all later ones
have not.  Item 1 therefore makes its two source options the current
options, so the rectangle is applicable.  Induction realizes the whole
sequence.  The final owner assertion is immediate prefix by prefix.
\(\square\)

The trail condition may equivalently be checked by the usual directed
Euler balance plus weak connectivity at each top.  The acyclic global
precedence condition is the extra synchronization constraint caused by
pairing two top edges into one physical rectangle.

## 6. A minimal installation obstruction

Formal collar cancellation does not imply (5.2).

### Proposition 6.1 (the repeated-source fork)

Suppose two formal rectangles use the same top \(U\) in the same
direction

\[
                         p\to q,qquad p\to q,                \tag{6.1}
\]

where \(p\ne q\).  The two copies may be paired with two different
companion tops.  If no other selected edge at \(U\) is present, then

\[
                         \partial f_U=2e_q-2e_p,               \tag{6.2}
\]

which is not \(e_{p_U^1}-e_p\) for any one final option.  Hence the
formal two-rectangle sum is not statically installable and admits no
chronological coefficient-one realization.

#### Proof

Equation (6.2) is immediate.  Its coefficient at \(p\) is \(-2\), while
every one-option replacement has coefficient \(-1\) at its initial
option.  Chronologically, after either copy is used, the current option
is \(q\), so the second copy of \(p\to q\) is unavailable. \(\square\)

This obstruction is independent of all protected target rows: each
rectangle may be perfectly collar-neutral, yet their option incidences
branch at one top.

There is a stronger obstruction specific to the actual boundary-swap
catalogue.

### Theorem 6.2 (fixed-root option graph is an involution)

Fix a top \(U\) and the retained phase interval \(1,\ldots,d\).  Write a
literal path option as

\[
                         p=(u,v,\tau),                         \tag{6.3}
\]

where \(u,v\) are its first two labels and \(\tau\) is the complete
ordered tail beginning at position three.  Every collar-neutral boundary
swap at this rooted top is

\[
                         (u,v,\tau)\longleftrightarrow(v,u,\tau). \tag{6.4}
\]

Consequently the underlying simple option graph is a disjoint union of
copies of \(K_2\).  Different choices of the companion top can create
parallel rectangle occurrences, but cannot create a new neighbor of
\(p\).

#### Proof

The construction changes only the first two positions and fixes every
label and position in \(\tau\).  Applying it twice restores the original
option.  Conversely, once the rooted literal order \(p\) is fixed, its
first two labels and its tail are fixed, so (6.4) is its unique boundary-
swap option.  The auxiliary label distinguishing the companion top never
belongs to \(U\) and does not alter this focal edge. \(\square\)

### Corollary 6.3 (one net unit transfer per top)

In every statically installable formal sum of fixed-root rectangles, the
initial and final options at a top are either equal or the two endpoints
of one edge (6.4).  Hence the middle-load difference contributed by one
top has \(\ell^1\)-norm at most two, and over all rank-\(M\) tops

\[
                         \|\mu^1-\mu^0\|_1\le2N,
 \qquad N=\binom{2m}{M}.                                     \tag{6.5}
\]

#### Proof

A trail in a two-vertex component alternates its unique edge.  An even
number of uses returns to the initial option and an odd number ends at
the other option.  One boundary swap changes exactly the phase-two owner,
so its one-top middle derivative is \(e_{D'}-e_D\), of norm two.  Sum
over the \(N\) tops. \(\square\)

At the calibrated top scale, \(N=(1+o(1))W/m=o(W)\).  The master-order
state and every \(o(W)\)-collision target are separated by
\(\frac12\ell^1\)-distance \((1-o(1))W\).  Inequality (6.5) therefore
rules out their connection by any statically or chronologically
installable composition of fixed-root collar-neutral rectangles, no
matter how many formal rectangle occurrences are written down.

## 7. The \(\Omega(W)\)-move verdict

Let

\[
                         N=\binom{2m}{M}.                      \tag{7.1}
\]

At the calibrated top scale used by the dense-recycling proposal,
\(N=(1+o(1))W/m\).  There a top-disjoint rectangle bank has at most
\(N/2=O(W/m)=o(W)\) rectangles.  Its principal owner capacity is
nevertheless of order \(dN=\Theta(W)\), and Sections 3--4 show that its
word interface costs only \(O(HN)=o(W)\).

By contrast, the master-order flattening lower bound requires
\(s=\Omega(W)\) boundary swaps.  Literal concatenation of all \(s\)
two-path macros would use \(\Omega(ds)=\Omega(mW)\) principal
occurrences and is irrelevant to coefficient one.  A necessary proposed
escape was **static compression**:

1. reuse each of the \(N\) tops on average \(\Theta(m)\) times in the
   formal rectangle flow;
2. satisfy the single-source/single-sink divergence (5.2) at every top;
3. satisfy the final owner capacity condition (4.1), with repeat excess
   \(o(W)\); and
4. if a physical route rather than only endpoint tables is required,
   satisfy the synchronized trail and prefix-capacity conditions of
   Theorem 5.2.

For a more general option graph, if Items 1--3 hold, the final table is
compiled **once**, so its word
length depends on the \(N\) installed paths and their owner repeats, not
on \(s\).  Explicitly, if its final owner occurrence load is \(\mu^1\),
then the same truncated-path compiler gives

\[
 |w_{\rm final}|=
 |\operatorname{supp}\mu^1|
 +\operatorname{rep}(\mu^1)+2HN.                             \tag{7.2}
\]

Thus \(\operatorname{rep}(\mu^1)=o(W)\) would imply coefficient-one length,
because \(HN=O(HW/m)=o(W)\).  Hence \(\Omega(W)\) formal moves are not
themselves a word-cost obstruction in such an enlarged graph.

For the actual fixed-root rectangle graph, however, Theorem 6.2 makes
every component a \(K_2\), and Corollary 6.3 bounds every compressed
endpoint displacement by \(2N=o(W)\).  It therefore cannot reach the
near-flat target.  The dense-recycling proposal is sharply refuted for
the collar-neutral rectangles alone.  Its only surviving extension must
add a top-local re-rooting or tail-changing move which joins distinct
\(K_2\) components; the all-depth collar action of that new move is not
covered by the rectangle identity.

## 8. Proved versus open

Proved here:

1. the exact two-forced-repeat owner census of one rectangle shore;
2. the exact \(2(L+1)\) collared-port count;
3. a literal word of length
   \(K+\operatorname{rep}(\mu)+4Hr\) for every static top-disjoint bank;
4. the bound new distinct owners plus \(O(P)\) exactly when owner repeats
   are \(O(P)\);
5. the exact static owner condition (4.1);
6. the single-option divergence criterion (5.2);
7. the exact synchronized chronological criterion;
8. a minimal branching obstruction to arbitrary dense composition; and
9. the fixed-root involution theorem and the \(2N=o(W)\) global
   displacement ceiling.

Not proved here:

1. a collar-controlled re-rooting or tail-changing primitive joining
   distinct option components;
2. a final low-collision owner table after adding such a primitive;
3. an acyclic synchronized schedule maintaining capacity at every prefix;
4. coefficient one.

## 9. Dependency ledger

The collar-neutral two-top rectangle and the full zero-marginal rectangle
lattice are in
`MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md`.
The useful-prefix literal frame compiler and delay-\(H\) interface theorem
are in
`MATH_THEOREM_CONVEYOR_BANK_LITERAL_OR_SPLICE_AND_DELAY_H_BOUNDARY_20260727.md`.
