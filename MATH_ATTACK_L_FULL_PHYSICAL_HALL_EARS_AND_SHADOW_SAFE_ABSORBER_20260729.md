# Full physical Hall circuits, chronology ears, and a shadow-safe unit absorber

Date: 2026-07-29

Status: proved all-odd-\(k\) forced-port ear theorem, proved full-physical
unit-circuit theorem, and exact specialization to the authoritative Hall-19
\(k=15\) carrier.  A bounded-seam, one-site common-controller absorber is
already realized by the audited Hall-20-to-Hall-19 transition.  At the Hall-19
endpoint itself, no duplicate-backed native ear is present.  The sharpest
known local root ear preserves residence and every upper support layer but
has an exact two-omission/two-duplication middle-deck defect and loses two
exterior matching units.  Thus it is a near-absorber, not Hall 18.

This note keeps three assertions rigorously separate:

1. weighted Hall on an equivariant orbit quotient;
2. ordinary Hall on the full occurrence-labelled graph; and
3. simultaneous realization by one literal controller word.

The separation is essential.  In particular, the weighted \(18/15\)
exceptional circuit from the preceding report is not one of the canonical
Hall-19 components.

## 1. The full physical graph

For the authoritative \(k=15\) endpoint put

\[
 W={15\choose8}=6435,\qquad L_0=W+3=6438.
\tag{1.1}
\]

The target shore is the complete nonempty lower Boolean ideal

\[
 \mathcal T=\{S\subseteq[15]:1\le |S|\le7\},\qquad
 |\mathcal T|=\sum_{j=1}^{7}{15\choose j}=16383.
\tag{1.2}
\]

The right shore contains all occurrence-labelled cells of depths zero, one,
and two.  Therefore

\[
 |\mathcal C|=6438+6437+6436=19311.
\tag{1.3}
\]

An edge \(S\sim c\) in the incidence graph means that there exists a
nonempty controller word which realizes all central rank-eight windows and
has trace \(S\) on the particular cell \(c\).  This quantifier is
edgewise: two different graph edges may be witnessed by two different
controller words.  Consequently a matching in this graph is a necessary
incidence certificate, not automatically a common-word literal compiler.

For a target set \(X\subseteq\mathcal T\), write

\[
 N(X)=\{c\in\mathcal C:c\sim S\text{ for some }S\in X\},\qquad
 \delta(X)=|X|-|N(X)|.
\tag{1.4}
\]

## 2. Every minimal positive physical obstruction is a unit circuit

The next theorem is independent of equivariance, Boolean ranks, and the
choice of controller architecture.

### Theorem 2.1 (full-physical minimal-circuit theorem)

Let \(G=(L,R,E)\) be a finite bipartite graph with unit capacities.  Let
\(X\subseteq L\) be inclusion-minimal subject to

\[
 \delta(X)=|X|-|N(X)|>0,
\tag{2.1}
\]

and suppose every member of \(X\) has positive degree.  Then:

1. the incidence graph induced by \(X\cup N(X)\) is connected;
2. no cell in \(N(X)\) is private to one target of \(X\); and
3. exactly

\[
                         |X|=|N(X)|+1.
\tag{2.2}
\]

In particular every inclusion-minimal positive-degree physical Hall
obstruction has defect one.

#### Proof

If the induced incidence graph had two target-containing components, their
right neighborhoods would be disjoint and \(\delta(X)\) would be the sum
of the component defects.  One proper target component would have positive
defect, contradicting inclusion-minimality.  This proves connectedness.

For \(x\in X\), let

\[
 p_x=|N(x)\setminus N(X\setminus\{x\})|
\tag{2.3}
\]

be the number of cells private to \(x\) inside \(X\).  Direct
subtraction gives the exact deletion identity

\[
 \delta(X\setminus\{x\})=\delta(X)-1+p_x.
\tag{2.4}
\]

If \(p_x\ge1\), the right side is at least \(\delta(X)>0\), again
contradicting minimality.  Hence \(p_x=0\) for every \(x\).  Equation
(2.4) and minimality now give \(\delta(X)-1\le0\).  Since the defect
is a positive integer, \(\delta(X)=1\).  \(\square\)

### Corollary 2.2 (private-ear exclusion)

If every nonempty connected positive-degree target shore in a unit-capacity
graph has a cell private to one of its targets, then the graph satisfies
Hall after its zero-degree targets are removed.

#### Proof

Otherwise choose an inclusion-minimal deficient shore and apply Theorem
2.1.  It simultaneously has and has no private cell.  \(\square\)

This is the correct full-physical replacement for the weighted defect
\(15,5,3\) classification.  Short-orbit weights disappear from the
minimal-circuit numerical classification after physical unfolding: all
physical demands and all physical cell capacities are one.

## 3. All-odd-\(k\) chronology at a forced port

Let \(k=2m+1\) be odd.  Let \(T=(T_i)\) be a cyclic strict rank-\(r\)
Johnson chronology of length \(W>d+1\), with indices read modulo \(W\),
and write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\tag{3.1}
\]

Fix \(d\ge1\), assume every positive coordinate run in \(T\) has
length at least \(d+1\), and let its maximal \(d\)-erosion be

\[
 P_i=\bigcap_{j=i-d}^{i}T_j.
\tag{3.2}
\]

Assume the erosion is flat of rank \(h=r-d\) and is a strict Johnson
walk.  Define the forced port

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1}).
\tag{3.3}
\]

### Theorem 3.1 (return identity at arbitrary depth)

For every \(i\),

\[
 P_i\setminus P_{i-1}=\{\beta_{i-d-1}\},\qquad
 P_i\setminus P_{i+1}=\{\alpha_i\},
\tag{3.4}
\]

and hence

\[
 F_i=\{\beta_{i-d-1},\alpha_i\}.
\tag{3.5}
\]

In particular,

\[
 |F_i|=1
 \quad\Longleftrightarrow\quad
 \beta_{i-d-1}=\alpha_i.
\tag{3.6}
\]

The corresponding positive coordinate run in (3.6) has exactly
\(d+1\) states and a singleton \(P\)-run at \(i\).  Conversely every
singleton coordinate run of \(P\) gives (3.6).

#### Proof

The coordinate \(\beta_{i-d-1}\) enters in the transition into
\(T_{i-d}\).  The residence hypothesis keeps it through
\(T_{i-d},\ldots,T_i\), so it belongs to \(P_i\); it is absent from
\(T_{i-d-1}\), and hence from \(P_{i-1}\).  Since consecutive
\(P\)-states are rank-\(h\) Johnson neighbors, this is the unique
entering coordinate.  The loss identity is the time reverse: \(\alpha_i\)
belongs to the preceding \(d+1\) middle states, hence to \(P_i\), but
not to \(T_{i+1}\), hence not to \(P_{i+1}\).  This proves
(3.4)--(3.5).  Equality of the entering and leaving labels says that the
coordinate is absent immediately before \(T_{i-d}\), present through
\(T_i\), and absent immediately afterward.  Its run therefore has exact
length \(d+1\), whose depth-\(d\) erosion is the singleton position \(i\).
Conversely a singleton \(P\)-run is absent at both neighboring positions,
so its label is simultaneously the unique entering and leaving difference
in (3.4).  \(\square\)

Thus singleton ports are genuine same-row chronology markers: they are
precisely shortest allowed middle runs.  Residence does not prohibit them.

### Lemma 3.2 (fresh common-neighbor normal form)

Let

\[
 P_{i-1}=A\cup\{a\},\qquad
 P_{i+1}=A\cup\{b\},\qquad |A|=h-1,\qquad a\ne b.
\tag{3.7}
\]

Suppose \(P_i\) is a rank-\(h\) Johnson neighbor of both endpoints
and

\[
 |P_{i-1}\cup P_i\cup P_{i+1}|=h+2.
\tag{3.8}
\]

Then for a unique

\[
 c\notin A\cup\{a,b\}
\tag{3.9}
\]

one has

\[
                         P_i=A\cup\{c\},\qquad F_i=\{c\}.
\tag{3.10}
\]

Conversely every choice in (3.9) gives this strict two-edge portal and
satisfies (3.8).  There are exactly

\[
                         k-h-1
\tag{3.11}
\]

possible portal labels.

#### Proof

A common rank-\(h\) Johnson neighbor of \(A+a\) and \(A+b\) is
of one of two forms:

\[
 A+c,\qquad c\notin A\cup\{a,b\},
\tag{3.12}
\]

or

\[
 (A\setminus\{x\})\cup\{a,b\},\qquad x\in A.
\tag{3.13}
\]

The three-state union in (3.13) has rank \(h+1\), whereas (3.12) has
rank \(h+2\).  Condition (3.8) selects (3.12), and then both boundary
differences in (3.3) equal \(c\).  Counting the complement of the
\(h+1\)-set \(A\cup\{a,b\}\) gives (3.11).  \(\square\)

For \(d\ge2\), condition (3.8) is exactly the local rank condition on
\((D^2P)_{i-1}\).  This is a local triple normal form; by itself it does
not assert that replacing the center extends to a globally legal controller
or exact carrier.

### Proposition 3.3 (one-portal deck-balance obstruction)

Suppose a clean portal \(A+c\) is changed to \(A+c'\), where
\(c\ne c'\), \(c'\notin A+c\), and neither \(c\) nor \(c'\) occurs in any
other \(P_u\) with cyclic distance at most \(d\) from the portal.  For
\(s=i-d,\ldots,i\), define

\[
 B_s=\left(\bigcup_{u=s}^{s+d}P_u\right)\setminus\{c\}.
\tag{3.13a}
\]

Then the \(d+1\) middle states whose windows contain the portal change
from

\[
                         B_s\cup\{c\}
 \quad\text{to}\quad
                         B_s\cup\{c'\}
\tag{3.14}
\]

and their aggregate point-degree vector changes by

\[
             (d+1)(e_{c'}-e_c).
\tag{3.15}
\]

Consequently one isolated portal relabelling cannot preserve an exact
middle deck.  Any exact-deck compound made from clean portal relabellings
with pairwise disjoint affected collars
has balanced directed label flow

\[
 \sum_{c\to c'}(e_{c'}-e_c)=0.
\tag{3.16}
\]

In particular it contains a two-portal opposite flow or a longer directed
coordinate cycle.

#### Proof

Exactly the starts \(s=i-d,\ldots,i\) have dilation windows containing
the changed portal.  Cleanliness removes both labels from their backgrounds,
so (3.14) is literal and summing gives (3.15).  An exact middle deck has a
fixed point-degree vector, forcing the sum of all changes to vanish.  After
division by \(d+1\), this is (3.16).  \(\square\)

This explains why a genuine strict-carrier absorber is necessarily
compound even when the Hall gain itself is one.

### Proposition 3.4 (exact all-declared-row fan criterion)

Fix \(L\ge d\) with \(W>L+1\).  Suppose each portal switch
\(c_j\to c'_j\) at site
\(i_j\) is clean through radius \(L\): neither label occurs in
\(P_u\), \(0<\operatorname{dist}_W(u,i_j)\le L\), and the affected
radius-\(L\) collars of
different switches are disjoint in cyclic distance.  Let \(P'\) differ from
\(P\) only at these listed centers, with every new center retaining the two
strict Johnson adjacencies.  For \(0\le \ell\le L\),
\(0\le t\le\ell\), put

\[
 B_{j,t}^{(\ell)}=
 \left(\bigcup_{u=i_j-t}^{i_j-t+\ell}P_u\right)\setminus\{c_j\}.
\tag{3.17}
\]

The complete \(D^\ell P\) row multiset is preserved exactly if and only if,
for every set \(S\),

\[
 \#\{(j,t):B_{j,t}^{(\ell)}\cup\{c_j\}=S\}
 =
 \#\{(j,t):B_{j,t}^{(\ell)}\cup\{c'_j\}=S\}.
\tag{3.18}
\]

Equivalently, in the free abelian group on subsets of \([k]\),

\[
 \sum_j\sum_{t=0}^{\ell}
 \left(
 [B_{j,t}^{(\ell)}+c'_j]-[B_{j,t}^{(\ell)}+c_j]
 \right)=0.
\tag{3.18a}
\]

Thus (3.16) is only the point-margin projection of the exact fan ledger.
A sufficient special case is a directed label cycle among sites having
identical punctured fans \(B_{j,t}^{(\ell)}\) for every \(\ell,t\); the switch then
merely permutes the affected row cells.

#### Proof

At depth \(\ell\), precisely the \(\ell+1\) windows indexed by
\(t=0,\ldots,\ell\) contain the changed site.  Cleanliness gives the literal
replacements

\[
 B_{j,t}^{(\ell)}+c_j\longrightarrow B_{j,t}^{(\ell)}+c'_j.
\tag{3.19}
\]

Disjoint collars make these the complete signed row change.  Equality of
the old and new multiplicity of each set \(S\) is exactly (3.18).  The
identical-fan cycle pairs every removed cell with an added copy.  \(\square\)

Since \(T=D^dP\), the row \(D^{d+q}P=D^qT\) is the depth-\(q\) upper
interval row.  Therefore (3.18), imposed for every
\(\ell=d,d+1,\ldots,d+q_{\max}\), is the exact simultaneous middle/all-
declared-upper multiset criterion.  It does not by itself supply one common
compiler word, prove maximal-erosion status, or prove that the new chronology
is a legal carrier.  Those remain separate local legality, residence, and
overlap conditions.

### Lemma 3.5 (one-core transport through clean portals)

Let \(C\subseteq P\) satisfy \(DC=DP\).  Under one clean portal switch

\[
                         P_i=A+c\longrightarrow P'_i=A+c',
\tag{3.20}
\]

put

\[
 C'_i=(C_i\setminus\{c\})\cup\{c'\},\qquad C'_u=C_u\quad(u\ne i).
\tag{3.21}
\]

Then

\[
                         C'\subseteq P',\qquad DC'=DP'.
\tag{3.22}
\]

Pairwise clean collar-disjoint switches compose.  Thus, after a
**legal fan-balanced carrier move**--meaning that the substituted \(P'\) is
a valid strict controller for its declared carrier and also passes the
needed fan identities--any occurrence matching of nonempty depth-zero
targets with

\[
                         C'_i\subseteq S\subseteq P'_i
\tag{3.23}
\]

at distinct positions lifts to one graded literal word by putting \(Q_i=S\)
at the assigned positions and \(Q_i=P'_i\) at every unassigned position.

#### Proof

Because \(c\) occurs at \(P_i\) but neither neighboring controller state,
the equality \(DC=DP\) forces \(c\in C_i\).  The new label \(c'\) is absent
from the two neighboring states.  Replacing \(c\) by \(c'\) in both
\(P_i\) and \(C_i\) therefore preserves the two incident derivative
equalities; every other edge is unchanged.  This proves (3.22), and
disjoint switches compose.  The displayed construction has
\(C'\subseteq Q\subseteq P'\) and is pointwise nonempty.  Monotonicity
gives

\[
                         DP'=DC'\subseteq DQ\subseteq DP',
\tag{3.24}
\]

so \(DQ=DP'\), and every assigned letter is literal.  \(\square\)

Lemma 3.5 is scoped to single-position graded targets.  Multi-position pins
still require the full simultaneous overlap test (6.3)--(6.4).

## 4. Forced-port orbit ears and one common core

This section supplies the all-odd-\(k\) sufficient chronology/shadow
condition.  It is stated for a cyclic equivariant controller; it does not
apply automatically to the endpoint-conditioned Hall-19 path.

Assume the cyclic positions have a free \(C_k\)-action.  A right block
orbit \(J\) has \(k\) physical positions.  A physical lower target
\(S\) is **forced-port eligible** at position \(i\) when

\[
                         F_i\subseteq S\subseteq P_i.
\tag{4.1}
\]

An **orbit ear** for a target orbit \(O\) is a right block \(J\)
together with an injection

\[
                         \iota_O:O\hookrightarrow J
\tag{4.2}
\]

such that \(S\) is eligible at \(\iota_O(S)\) for every
\(S\in O\).  For a free target orbit, one eligible phase generates
the bijection (4.2).  For a short top-rank orbit \(O\), equality
\(S=P_i\) and its stabilizer copies give (4.2).

For a chosen ear assignment define the mandatory omission set

\[
 \mathcal Z=\{(i,x):i=\iota_O(S),
                         \ x\in P_i\setminus S
                         \text{ for some assigned }(O,S)\}.
\tag{4.3}
\]

Let \(\overline{\mathcal Z}\) be its full \(C_k\)-orbit closure.  Call the
assignment **orbit-coherent** if, for every selected pair
\(i=\iota_O(S)\),

\[
                  \{x:(i,x)\in\overline{\mathcal Z}\}\cap S
                  =\varnothing.
\tag{4.3a}
\]

Call it **run-compatible** if, for every coordinate \(x\), the closed set
\(\overline{\mathcal Z}\) never
contains two adjacent supported positions \((i,x),(i+1,x)\), including the
cyclic wrap edge.

### Theorem 4.1 (Shadow--Chronology Ear Theorem)

Let \(\mathscr O\) be any family of physical target orbits.  Suppose:

1. every \(O\in\mathscr O\) has an orbit ear \(J_O,\iota_O\);
2. the block orbits \(J_O\) are pairwise distinct; and
3. the combined assignment is orbit-coherent; and
4. its orbit-closed omission set is run-compatible.

Then there is one equivariant nonempty one-core \(C\) such that

\[
                         C_i\subseteq P_i,\qquad DC=DP,
\tag{4.4}
\]

and the assigned physical cells give a matching of every target in every
orbit \(O\in\mathscr O\) under this same core.  The carrier \(T\)
is unchanged.  Hence every residence assertion and every lower or upper
carrier-support assertion determined by the unchanged \(P/T\) tower remains
true.

#### Proof

Delete exactly the orbit-closed occurrences:

\[
 C_i=P_i\setminus\{x:(i,x)\in\overline{\mathcal Z}\}.
\tag{4.5}
\]

We first prove \(DC=DP\) coordinatewise on an edge \(i,i+1\).  If
\(x\) occurs in only one of \(P_i,P_{i+1}\), then it belongs to
the forced port at that endpoint.  Every member of the orbit closure comes
from a translated eligible pair
\(F_{gi}\subseteq gS\subseteq P_{gi}\), so no translated omission deletes
such a forced label.  If \(x\) occurs in both, it disappears from
\(C_i\cup C_{i+1}\) only if both adjacent occurrences are deleted,
which run-compatibility forbids.  Thus every coordinate of
\(P_i\cup P_{i+1}\) survives in \(C_i\cup C_{i+1}\), while the
reverse containment is automatic.  This proves (4.4).

Every \(F_i\) is nonempty and is retained, so every \(C_i\) is
nonempty.  The assigned blocks are distinct, hence their physical
positions are disjoint.  At the position assigned to \(S\), all of
\(P_i\setminus S\) and no member of \(S\) is deleted.  Therefore

\[
                         C_i=S.
\tag{4.6}
\]

The cells in (4.2) consequently realize pairwise distinct targets on
pairwise distinct positions under one \(C\).  The closed deletion set is
\(C_k\)-invariant, so \(C\) is equivariant.

Finally, if the middle carrier is \(T=D^dP\), then applying
\(D^{d-1}\) to \(DC=DP\) gives

\[
                         D^dC=D^dP=T.
\tag{4.7}
\]

Thus (4.4) leaves every prescribed central window unchanged.  Since neither
\(P\) nor \(T\) was rethreaded, all carrier support and residence properties
are untouched.  \(\square\)

### Corollary 4.2 (private-orbit chronology condition)

Suppose every nonempty connected family of positive target orbits has an
orbit ear whose right block is private inside that family.  Then the
forced-port quotient graph has no inclusion-minimal deficient circuit.

If the private ears can be peeled recursively so that their accumulated
assignments are orbit-coherent and their closed omissions are
run-compatible, then the peeled targets admit the integral common-core
matching of Theorem 4.1.

#### Proof

The graph assertion is the weighted analogue of Corollary 2.2.  If a
target orbit has weight at most the right-block capacity \(k\), deleting
it from a minimal deficient family while deleting at least one private
block leaves positive defect.  Hence a minimal circuit has no private
block.  The assumed private ear is a contradiction.

For the compiler assertion, reverse the peeling order.  The ears use
distinct blocks, and the stated coherence and run conditions are exactly
hypotheses 3--4 of Theorem 4.1.  \(\square\)

This is a genuine sufficient Shadow--Chronology condition.  It is stronger
than weighted Hall because it also supplies an integral common-core lift;
it is weaker than asking for independently chosen per-target controller
words.

## 5. The exceptional short-orbit absorber for every odd \(k\)

Let \(E\) be a translation orbit of rank-\(h\) controller states
with stabilizer size \(a>1\).  Its physical size is

\[
                         s=|E|=k/a<k.
\tag{5.1}
\]

Let \(O\) be any free lower target orbit of size \(k\).  Put

\[
 \mathcal E=\{J:P_i\in E\text{ at some phase of }J\},
\tag{5.2}
\]

and let \(\mathcal B_O\) be the forced-port-eligible block set for
\(O\).

### Theorem 5.1 (two-block short-orbit absorber)

Assume both target orbits have positive degree.  Then the two-orbit weighted
shore \(O\cup E\) has demand \(k+s\).  It is a one-block deficient
circuit precisely when

\[
                 \mathcal B_O=\mathcal E=\{J_*\}.
\tag{5.3}
\]

Assume also that the orbit copies of one chosen full-orbit edge are
nonadjacent in the controller chronology.  This is automatic in the strict
middle-layer quotient whenever

\[
                  N={1\over k}{k\choose m+1}>1,
\tag{5.3a}
\]

and hence for every odd \(k\ge5\).  If instead

\[
                         |\mathcal B_O\cup\mathcal E|\ge2,
\tag{5.4}
\]

then two distinct block ears give an integral physical assignment of all
\(k+s\) targets under one equivariant one-core.  No carrier state is
changed, so the repair preserves residence and every upper shadow exactly.

#### Proof

One free right block has physical capacity \(k\), so (5.3) gives defect
\(s\).  Conversely, a one-block neighborhood must be the same singleton
for the two positive target orbits, proving the characterization.

Under (5.4), choose distinct

\[
                         J_O\in\mathcal B_O,\qquad
                         J_E\in\mathcal E.
\tag{5.5}
\]

One eligible phase at \(J_O\) translates through all \(k\) members of
the free target orbit and all \(k\) physical positions.  At \(J_E\),
each member of \(E\) equals the envelope \(P_i\) at \(a\) phases;
choose one phase for each of the \(s\) distinct targets.  The top-orbit
assignments omit nothing.  The phase-bijection for the free orbit makes its
assignment orbit-coherent.  Its orbit-closed omissions occur at
positions separated by the quotient length and therefore contain no
adjacent pair by (5.3a).  Theorem 4.1 applies.
\(\square\)

For \(k=15,h=5\), the exceptional orbit has stabilizer \(a=5\) and
\(s=3\).  The smallest circuit is therefore exactly

\[
                         15+3>15.
\tag{5.6}
\]

For the singleton orbit \(U\), Theorem 3.1 gives the explicit chronology
marker set

\[
 \mathcal B_U=\mathcal L
 =\{J:\beta_{i-4}=\alpha_i\text{ at a phase of }J\}.
\tag{5.7}
\]

Thus the exceptional \(18/15\) circuit is excluded, and locally compiled,
by the exact condition

\[
                         |\mathcal L\cup\mathcal E|\ge2.
\tag{5.8}
\]

For the singleton choice \(O=U\), it unfolds, in the pure depth-zero
forced-port model, into three physical \(6/5\) unit circuits: for each
exceptional five-set \(S\), its five
singleton targets and \(S\) itself compete for the five phases whose
envelope is \(S\).  Indeed, one singleton-port phase in the free block
generates all fifteen singleton-port phases by unit-voltage equivariance.
Inside the stabilizer fibre of a fixed exceptional \(S\), their labels are
the five translates through \(S\), each exactly once.  This \(6/5\) shore
is inclusion-minimal: without
\(S\), the selected singletons have their distinct phase cells; with
\(S\) and at most four singletons, all five cells are available and demand
is at most five; only the full six-target shore is deficient.  The three
exceptional envelopes have disjoint phase fibres.  Additional depth-one or
depth-two cells can add
neighbors, so this unfolding must not be identified with a component of a
larger endpoint-conditioned occurrence graph without a direct audit.

### Exact scope

Theorem 5.1 repairs every two-orbit \(E\)-circuit once chronology or
shadow structure supplies a second eligible block.  Corollary 4.2 excludes
all larger minimal \(E\)-circuits under recursive private-ear expansion.
Neither theorem proves that an exact middle Hamilton deck necessarily has
the required second block.  The support-complete FIFO/hourglass example in
the preceding chronology audit shows that residence and all-rank support
alone do not force it; exact middle-deck/factor injectivity remains the only
available unconditional source of such an implication.

## 6. A full-physical unit-ear absorber

The orbit theorem does not apply to the non-equivariant H19 path.  The
following unit-capacity theorem does.

Let \(P\) be one maximal controller.  A pair \((X,Y),R\), with
\(Y\) a set of physical cells and \(R\subseteq X\), is an
**exposed-root native basis** when the native trace map is a bijection

\[
                         \tau_P:Y\longrightarrow X\setminus R.
\tag{6.1}
\]

### Theorem 6.1 (unit-ear completion)

Assume (6.1).  For each \(\rho\in R_0\subseteq R\), choose a distinct
additional cell \(c_\rho\notin Y\), and suppose one nonempty controller
word \(Q\) simultaneously realizes:

1. every retained native target \(X\setminus R\) on its distinct cell
   in \(Y\); and
2. \(\rho\) on \(c_\rho\) for every \(\rho\in R_0\).

Then these cells give a literal matching of

\[
                         (X\setminus R)\cup R_0
\tag{6.2}
\]

under one word.  It adds exactly \(|R_0|\) matching units relative to
the native basis.  If a disjoint exterior matching survives, the same number
of units is added globally.

#### Proof

The target sets in the two groups are disjoint, and all selected cells are
distinct.  The common word supplies every displayed edge simultaneously.
Their union is the desired matching.  \(\square\)

The common-word premise has an exact coordinatewise test.  Let the retained
or new exact pins be \((I_a,S_a)\).  The unique maximal candidate is

\[
 Q_p=P_p\cap\bigcap_{a:p\in I_a}S_a.
\tag{6.3}
\]

It works if and only if

\[
 I_a\cap\{p:x\in Q_p\}\ne\varnothing
 \quad(a,\ x\in S_a),\qquad
                         Q_p\ne\varnothing\quad(p),
\tag{6.4}
\]

and the prescribed central windows remain exact.  Formula (6.4) is the
positive-witness and nonemptiness test; (6.3) already enforces every
negative pin condition.

### Corollary 6.2 (duplicate-child splitter)

If a legal carrier trade creates a second cell with native child target
\(a\in X\setminus R\), retains one original cell for \(a\), and allows
the second copy to be shrunk to one exposed root \(\rho\) while passing
(6.3)--(6.4), then it adds one shore-local matching unit.  It repairs a
specified inclusion-minimal unit circuit when \(R=\{\rho\}\) and
\((X,Y)\) is that circuit.  It adds one global rank unit when, in addition,
a disjoint exterior matching survives.  If the carrier trade preserves
exact middle deck, residence, and all upper supports, the repair preserves
them as well.

This is an all-odd-\(k\) theorem: no numerical property of \(k=15\) is
used.  The move may be a bounded-collar trade, a bounded number of segment
seams, or any other literal legal rethreading.  What matters is the extra
physical occurrence, the common-word overlap test, and the disjoint exterior
ledger.

## 7. A realized bounded-seam absorber: Hall 20 to Hall 19

The frozen carrier chain is

```text
scratch/k15_segment_braid_hall20_zero6.json
  --RF(180,2764,4210)-->
scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
  --FR(123,722,4710)-->
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

The final SHA-256 is

```text
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

### Theorem 7.1 (explicit three-seam, one-site absorber)

The two braids preserve:

1. the exact \(6435\)-state middle deck;
2. every Johnson adjacency;
3. depth-three residence;
4. every upper support layer of depths \(1,\ldots,7\); and
5. the lower-hole vector \((4,18,11,1,0,0,0)\).

Their incidence matching ranks are

\[
                         16363,\quad16363,\quad16364.
\tag{7.1}
\]

The first braid is a neutral router.  The second repairs the remote
\(161/160\) component formerly exposed at target \(24610\).  In the
final carrier, native child \(25634\) occurs at two depth-zero cells,
\(1212\) and \(4713\).  Shrinking either selected controller letter by

\[
                         25634\longrightarrow24610
\tag{7.2}
\]

retains the other child occurrence and gives one literal root unit.  The
same word preserves all \(6435\) central windows, all \(497\) native pins
of the final positive DM shore, and all \(160\) nonroot pins of the
discharged component.  Hence it realizes

\[
                         497+160+1=658
\tag{7.3}
\]

distinct simultaneous pins on the former \(677\)-target shore.

#### Proof

The exact carrier invariants and rank changes are the frozen direct audits
of the two three-cut transformations.  On the discharged target shore the
new restricted profiles include two copies of
\(\{24610,25634\}\), while one distinct native occurrence remains for
every other nonroot target.  Equation (7.2) deletes the single mask
\(1024\) at one controller position.  The overlap-safe audit checks every
affected central and retained pin window and nonemptiness at all \(6438\)
positions; (6.3)--(6.4) pass for either cell.  Distinctness of the retained
cells gives (7.3).  Independently, complete-profile cancellation gives the
global incidence-rank increase in (7.1).  \(\square\)

This is the requested explicit bounded absorber in the precise sense
currently proved: two bounded-seam carrier moves followed by a one-site
common-controller shrink.  It preserves residence and all upper shadows.
It proves one global incidence-rank unit and one shore-local common-word
unit.  It does **not** prove that all \(16364\) edges of the final global
matching coexist under the word used in (7.2).

## 8. Exact Hall-19 specialization on all \(16383\) targets

The authoritative final carrier has

\[
 \nu=16364,\qquad
 16383-\nu=19,\qquad
 |X|/|Y|=516/497.
\tag{8.1}
\]

Its six zero-degree targets are

\[
 Z=\{5801,13616,13620,17738,21641,29776\}.
\tag{8.2}
\]

They are six isolated \(1/0\) DM components.  Removing them leaves

\[
 |\mathcal T\setminus Z|=16377,\qquad
 16377-\nu=13,\qquad
 |X\setminus Z|/|Y|=510/497.
\tag{8.3}
\]

Thus the exact decomposition is

\[
                         19=6+13.
\tag{8.4}
\]

The canonical DM component census is

\[
\begin{array}{c|c|l}
|X_j|/|Y_j|&\text{number}&\text{exposed native targets}\\ \hline
321/319&1&8217,8218\\
161/160&1&960\\
5/4&2&4213,7504\\
3/2&2&1103,18970\\
2/1&6&2420,2575,2676,9524,17683,19568\\
1/0&6&5801,13616,13620,17738,21641,29776.
\end{array}
\tag{8.5}
\]

The positive-degree part has twelve components, not thirteen: eleven have
gap one and the \(321/319\) component has gap two.  Its thirteen units are

\[
 13=2+1+2+2+6.
\tag{8.6}
\]

Every component in (8.5) has an exposed-root native basis under the maximal
controller.  The \(321/319\) component is genuinely two-rooted:

\[
 \tau_P(Y)=X\setminus\{8217,8218\},\qquad
                         8216=\bigcap_{S\in X}S\notin X.
\tag{8.7}
\]

The other eleven positive components have one exposed root each.  The
\(497\) native cells are disjoint from an exterior incidence matching of
size

\[
                         16383-516=15867.
\tag{8.8}
\]

### Consequences of Theorem 2.1

The whole \(321/319\) component is not inclusion-minimal as a Hall shore:
every inclusion-minimal positive deficient subshore has gap one.  The
artifact does not canonically list the minimal unit subshores inside this
component, and they need not be disjoint.  Likewise, the exposed native
targets in (8.5) are a certified basis complement, not a uniquely forced
set of unmatched vertices for every maximum matching.

The weighted exceptional rank-five orbit at \(k=15\) is

\[
 \{4681,9362,18724\}.
\tag{8.9}
\]

None of these three masks is among the nineteen exposed targets in (8.5).
The two \(5/4\) H19 components are ordinary physical unit components
rooted at rank-six targets \(4213\) and \(7504\); they are not quotient
\(E_5\) circuits.

### Exact current native-ear obstruction

In the frozen H19 carrier:

1. every exposed root in (8.5) has native multiplicity zero;
2. all \(45\) certified root sockets consume a native child of total
   native multiplicity exactly one; and
3. therefore every one-socket root pivot merely exchanges the exposed root
   for its child and is matching-neutral.

The two-root component would require two distinct extra cells and one
simultaneous overlap-safe common-word check.  No such completion is
certified.  The six zeros in (8.2) are more basic: no controller shrink can
serve a target with no incident cell.  A carrier move must first create a
physical candidate for each zero it repairs.

If thirteen positive ears and six zero-target cells could be chosen
distinctly, while retaining the native basis and the exterior matching,
the exact incidence ledger would be

\[
                         497+13+6+15867=16383.
\tag{8.10}
\]

For a literal compiler all \(16383\) selected pins would additionally
have to pass one simultaneous version of (6.3)--(6.4).  Equation (8.10)
alone is not that common-word proof.

## 9. The sharp H19 near-absorber and the forced compound gate

There is one exact local controller rotation at the root \(2420\) which
creates the desired physical ear while preserving the local graded
geometry.  At controller positions \(3782,3783,3784\), it replaces

```text
(2416,18768,2388) by (18768,2416,2388).
```

The new depth-one cell at start \(3783\) has native trace

\[
                         2416\cup2388=2420.
\tag{9.1}
\]

### Theorem 9.1 (exact near-absorber ledger)

The rotated chronology is Johnson, depth-three resident, and complete in
every upper support layer \(q=1,\ldots,7\).  All \(497\) old native
shore pins survive, and the new root ear gives

\[
                         516/498
\tag{9.2}
\]

on the fixed old critical shore.  However, the middle row omits exactly

\[
                         11122,\quad19804
\tag{9.3}
\]

and duplicates exactly

\[
                         27474,\quad3452.
\tag{9.4}
\]

It therefore has only \(6433\) distinct middle states and is not an exact
factor.  The exterior matching rank after reserving the \(498\) critical
cells is

\[
                         15865=15867-2,
\tag{9.5}
\]

with new zero targets

\[
                         10610,\quad19796.
\tag{9.6}
\]

The complete graph rank is consequently \(16363\), not \(16365\).

The theorem is the frozen exact audit of the \(28\) oriented local facet
rotations.  It is quoted here because it identifies the smallest literal
compound gate, not as an H18 claim.

### Corollary 9.2 (two-for-two closed-circulation gate)

An exact continuation of this local route must simultaneously:

1. retain the exact fixed-shore profile
   \(N(X)=Y\mathbin{\dot\cup}\{c_\star\}\), hence precisely the
   root-\(2420\) ear and the other \(497\) native cells;
2. replace the two duplicated middle states (9.4) by the two omitted states
   (9.3), restoring the exact deck;
3. restore the exterior rank \(15867\), including targets (9.6);
4. retain depth-three residence and all upper supports; and
5. restore the protected lower-support ledger.

If these five conditions hold, then

\[
                         498+15867=16365,
\tag{9.7}
\]

and the incidence endpoint is exactly Hall 18: (9.7) is the lower bound and
the retained \(516/498\) shore is the matching upper bound.  A literal
common-word version additionally requires the selected critical and exterior
edges to pass one simultaneous controller test.  A direct replacement at either remote
duplicate middle position fails Johnson boundary distance, so the companion
must be a genuinely multistate two-for-two circulation.

Proposition 3.3 explains the form of this obstruction: a one-portal gain
cannot preserve the exact deck ledger.  The audited near-absorber exhibits
the first balanced object still missing from the H19 fibre.

## 10. Proved boundary

The following conclusions are proved.

1. Under the full \(16383\)-target semantics, every inclusion-minimal
   positive Hall obstruction has defect one and no private physical cell.
2. At arbitrary residence depth, singleton forced ports are exactly
   shortest permitted same-row returns; their local controller geometry is
   (3.10).
3. Recursive private orbit ears, with orbit coherence and the exact
   no-adjacent-omission condition, produce one integral common core.  This is an all-odd-\(k\)
   sufficient Shadow--Chronology compiler theorem.
4. Every two-orbit exceptional short-orbit circuit is repaired by a second
   eligible block under one common core, without changing the carrier.
5. The Hall-20-to-Hall-19 route is an explicit bounded-seam, one-site
   absorber preserving exact middle deck, residence, and all upper shadows.
6. The authoritative H19 deficit is exactly six zeros plus thirteen
   positive-degree units.  Those thirteen units lie in twelve components.
7. No immediate duplicate-backed native ear exists at H19.
8. The root-\(2420\) facet rotation supplies the exact critical-shore ear
   and preserves residence/all upper shadows, but its middle and exterior
   ledgers force the compound gate in Corollary 9.2.

The following statements are not proved.

1. Exact middle-factor injectivity does not yet imply the private-ear or
   two-block condition for every weighted \(E_5\)-type circuit.
2. No Hall-18 exact carrier is produced.
3. No common controller for a full \(16364\)-edge H19 matching, much less
   a perfect \(16383\)-edge matching, is produced.
4. The companion circulation in Corollary 9.2 is an exact finite gate, not
   an existence theorem.

The smallest remaining local hypothesis is therefore not another marginal
or rankwise Hall inequality.  It is a closed, deck-balanced companion to a
physical root ear which retains the exterior occurrence matching and passes
one common-controller overlap test.

## 11. Audited sources

The principal frozen sources used here are:

```text
MATH_ATTACK_L_GRADED_HALL_AFTER_Q3_MINIMAL_CIRCUIT_20260729.md
MATH_ATTACK_L_E5_CHRONOLOGY_AND_LAZY_HALL_CUT_20260729.md
MATH_THEOREM_H19_EXPOSED_ROOT_NATIVE_BASIS_AND_COMMON_Q_UNIT_20260728.md
THREAD_K_H20_REMOTE_ROOT_DISCHARGE_TO_H19_20260728.md
THREAD_H_H19_ROOT_EAR_REBASE_AND_TWO_FOR_TWO_DECK_GATE_20260728.md
THREAD_A_K15_CYCLIC_ZERO_ORBIT_AND_EQUIVARIANT_FACTOR_AUDIT_20260728.md
scratch/audit_k15_h19_root8216_chain_independent.json
scratch/audit_k15_h20_h19_exposed_roots_common_q.py
scratch/audit_k15_h19_root_ear_rotations.py
```

The decisive new steps were independently adversarially audited in three
separate proof passes: the portal/fan identities, the orbit-ear/common-core
lift, and the complete final report.  Their scope corrections--cyclic collar
separation, orbit-closed omission coherence, the distinction between a
shore-local unit and global rank, and the exact retained-shore requirement in
Corollary 9.2--are incorporated above.

No search, SAT call, exhaustive enumeration, or long-running local job was
performed for this note.  The new arguments are the hand proofs in Sections
2--6; all numerical specializations are read-only consequences of the
frozen audits above.
