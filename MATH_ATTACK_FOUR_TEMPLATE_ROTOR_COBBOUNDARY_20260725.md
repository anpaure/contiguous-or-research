# A four-template rotor coboundary with one surviving rank

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

The natural phase telescope for the rectangular flush-and-reload compiler
is closed, but there is a genuinely different multi-template cancellation.

An arrival diamond consists of two legal two-step rotor paths with the same
source and endpoint.  Their complete physical incidence difference is one
vertical string

\[
 V(\mathcal C;y,y')
 =
 \bigl(e_{C_{\ell-1}+y}-e_{C_{\ell-1}+y'}\bigr)_\ell,
 \tag{0.1}
\]

where \(\mathcal C=(C_k)\) is a saturated chain of bases.  If
\(\mathcal C'\) is obtained from \(\mathcal C\) by interchanging two
adjacent increments \(a,b\), then

\[
 V(\mathcal C;y,y')-V(\mathcal C';y,y')
 \tag{0.2}
\]

vanishes at every Boolean rank except the one rank at which the two chains
differ.  At that rank it is the elementary rectangle

\[
 \boxed{
 e_{B+a+y}+e_{B+b+y'}
 -e_{B+a+y'}-e_{B+b+y}.}
 \tag{0.3}
\]

Equation (0.2) is a signed sum of four legal path templates.  It can be
made into a positive switch using two distinct carrier tags:

\[
 \{P_{\mathcal C}^{\,y'},P_{\mathcal C'}^{\,y}\}
 \longleftrightarrow
 \{P_{\mathcal C}^{\,y},P_{\mathcal C'}^{\,y'}\}.
 \tag{0.4}
\]

Each side selects exactly one path in each carrier.  The two alternatives
inside a carrier have the same initialization, the same source, the same
two-step endpoint, and the same continuation.  Therefore (0.4) adds no
letters and no reset.

Choosing the adjacent chain swap at the middle gives a nonzero middle-owner
rectangle of squared norm four and **zero incidence at every nonmiddle
rank**, including the extra prefix immediately above the truncated collar.
Thus a legal \(O(1)\)-norm cross-carrier connector coboundary exists.

This does not prove the coefficient-one theorem.  Section 8 packs
\(M/2-o(M)\) independently switchable controlled-band diamonds per carrier
pair, but Section 9 records the fatal global audit: their common
block-boundary owners force \(W/4-o(W)\) middle collision excess.  The
owner-separated successor requires eight paths in four carriers and is
developed in
MATH_AUDIT_PAIRED_DIAMOND_DUPLICATION_AND_EIGHT_TEMPLATE_20260725.md.

## 1. Connector derivatives are cochain boundaries

Fix distinct labels \(u,v\).  For every set \(K\) containing neither,
write

\[
 \Phi_{uv}(K)=e_{K+u}-e_{K+v}.
 \tag{1.1}
\]

The vectors \(\Phi_{uv}(K)\) for distinct \(K\) have disjoint supports and
are therefore linearly independent.

The exact source-flush audit has the form

\[
 C_h(R)=\Phi_{uv}(K_h(R))-\Phi_{uv}(J_h(R)).
 \tag{1.2}
\]

Thus, at every rank \(h\), a routing template \(R\) defines an oriented edge

\[
 J_h(R)\longrightarrow K_h(R)
 \tag{1.3}
\]

in the free graph on transposition bases, and \(C_h(R)\) is its boundary.
For an integer signed family \((c_R)\),

\[
 \sum_Rc_RC_h(R)=0
 \tag{1.4}
\]

if and only if the directed base-edge multigraph is Eulerian after equal
bases are identified.

This is the exact cochain classification.  A three-edge triangle can cancel
algebraically at one rank, and a four-edge cycle can cancel there as well.
The obstruction in the natural phase telescope is not parity: phase advance
changes the actual bases, so its nominal edge endpoints do not meet.

If \(\tau\) is a coordinate permutation implementing a phase shift, then

\[
 C_h(\tau R)=\tau C_h(R).
 \tag{1.5}
\]

The old and shifted edges are translates, not consecutive edges of a
common base cycle.  The far-collar cap flux in the natural-telescope audit
is precisely the failure of their endpoints to match.

The construction below changes the base chain itself by one adjacent
increment.  It therefore makes a genuine cochain square rather than trying
to identify two phase translates.

## 2. Full ordered-state form of one arrival diamond

Put \(n=2Q\).  Start with a full ordered partition

\[
 \Pi=(L,\{z_1\},\ldots,\{z_n\},R),
 \tag{2.1}
\]

where

\[
 |L|=m-Q
\]

and the last block \(R\) is unresolved.  Inside one carrier, choose

\[
 x,x'\in L,\qquad y,y'\in R_U,
 \tag{2.2}
\]

with all four labels distinct.  Consider the two legal update sequences

\[
 (x,y),(x',y')
 \qquad\hbox{and}\qquad
 (x,y'),(x',y).
 \tag{2.3}
\]

Both finish at the same quotient state,

\[
 \left(
 L-\{x,x'\}+\{y,y'\};
 x',x,z_1,\ldots,z_{n-2};
 R_U-\{y,y'\}+\{z_{n-1},z_n\}
 \right).
 \tag{2.4}
\]

At the full ordered-partition level, the two paths differ only at their
intermediate state.  Those two intermediate states are

\[
 \Pi_y=
 (L-x+y,\{x\},\{z_1\},\ldots,\{z_n\},R-y),
 \tag{2.5}
\]

\[
 \Pi_{y'}=
 (L-x+y',\{x\},\{z_1\},\ldots,\{z_n\},R-y').
 \tag{2.6}
\]

Define a saturated base chain by

\[
 C_{m-Q-1}=L-x,
 \tag{2.7}
\]

and successively adjoin

\[
 x,z_1,z_2,\ldots,z_n.
 \tag{2.8}
\]

Thus \(C_k\) is defined for

\[
 m-Q-1\le k\le m+Q.
\]

### Theorem 2.1 (complete diamond cochain)

Let \(I(P)\) denote the complete aggregate multiplicity vector of all
prefix unions exposed by all states of a path, sorted by Boolean rank.  For
the two paths in (2.3), continued identically after their common endpoint,

\[
 \boxed{
 I(P_{\mathcal C}^{\,y})-I(P_{\mathcal C}^{\,y'})
 =
 \bigl(e_{C_{\ell-1}+y}
       -e_{C_{\ell-1}+y'}\bigr)_{
       m-Q\le\ell\le m+Q+1}.}
 \tag{2.9}
\]

The difference is zero at every other Boolean rank.

#### Proof

The source state, the two-step endpoint, and the continuation agree, so
only (2.5)--(2.6) contribute.  Before the final residual block, the prefix
unions of (2.5) are

\[
 C_{\ell-1}+y,
 \qquad m-Q\le\ell\le m+Q+1,
\]

and those of (2.6) are the same sets with \(y'\) in place of \(y\).
Adjoining the final block gives the full ground set in both states.  There
are no prefix ranks below \(m-Q\).  This proves (2.9). \(\square\)

The extra rank \(m+Q+1\) is important.  It comes from the singleton
\(z_n\), which belongs to the refined tail of the truncated quotient.  It
will cancel in the four-template construction because the two base chains
have already coalesced by that rank.

## 3. The second coboundary isolates one rank

Let

\[
 c_1=x,\quad c_2=z_1,\quad\ldots,\quad c_{n+1}=z_n
 \tag{3.1}
\]

be the increments of \(\mathcal C\).  Fix \(2\le j\le n\), put

\[
 a=c_j,\qquad b=c_{j+1},
\]

and let \(\mathcal C'\) be the saturated chain obtained by interchanging
these two adjacent increments.

Concretely, since \(j\ge2\), the increments are
\(a=z_{j-1}\), \(b=z_j\).  The chain \(\mathcal C'\) is realized by the
valid source partition obtained from (2.1) by swapping these two collar
singletons and changing nothing else.

The two chains agree at every base rank except

\[
 k_*=m-Q-1+j.
 \tag{3.2}
\]

Writing \(B\) for their common set just before \(a,b\) are adjoined, one
has

\[
 C_{k_*}=B+a,\qquad C'_{k_*}=B+b.
 \tag{3.3}
\]

### Theorem 3.1 (rank-isolated four-template coboundary)

Define

\[
\begin{aligned}
 \Xi={}&I(P_{\mathcal C}^{\,y})
       -I(P_{\mathcal C}^{\,y'})\\
      &-I(P_{\mathcal C'}^{\,y})
       +I(P_{\mathcal C'}^{\,y'}).
\end{aligned}
 \tag{3.4}
\]

Then \(\Xi\) is zero at every Boolean rank except

\[
 r=k_*+1=m-Q+j.
 \tag{3.5}
\]

At rank \(r\),

\[
 \boxed{
 \Xi_r=
 e_{B+a+y}+e_{B+b+y'}
 -e_{B+a+y'}-e_{B+b+y}.}
 \tag{3.6}
\]

In particular,

\[
 \|\Xi\|_1=4,\qquad \|\Xi\|_2^2=4.
 \tag{3.7}
\]

#### Proof

Subtract (2.9) for \(\mathcal C'\) from (2.9) for \(\mathcal C\).
The base chains agree at every index except \(k_*\), so all other rank
components cancel, including rank \(m+Q+1\).  Substitution of (3.3) at
rank \(k_*+1\) gives (3.6).  Its four masks are distinct because
\(a,b,y,y'\) are distinct and lie outside \(B\). \(\square\)

This is the desired small coboundary.  Its connector incidence is exactly
zero outside the selected rank; it has no \(O(Q)\) cap-drift residue.

## 4. The middle-owner specialization

Assume \(Q\ge2\).  Choose

\[
 j=Q.
\]

Then

\[
 r=m.
\]

In the source notation,

\[
 a=z_{Q-1},\qquad b=z_Q,
\]

and

\[
 B=(L-x)+x+z_1+\cdots+z_{Q-2}
   =L+z_1+\cdots+z_{Q-2},
 \qquad |B|=m-2.
 \tag{4.1}
\]

The survivor is the middle-owner rectangle

\[
 \boxed{
 e_{B+z_{Q-1}+y}
 +e_{B+z_Q+y'}
 -e_{B+z_{Q-1}+y'}
 -e_{B+z_Q+y}.}
 \tag{4.2}
\]

Every lower flag, every nonmiddle upper flag, the prefix at rank
\(m+Q+1\), and the full-set prefix cancel exactly.  Thus the complete
physical connector norm away from the marked middle direction is zero.

The same explicit collar-swap construction works at every rank

\[
 m-Q+2\le r\le m+Q
\]

by choosing the adjacent increment position in (3.5).  In particular it
can retain one of the nonmiddle rank-isolating rectangle directions used
by the static cube while canceling the middle-owner and all other flag
ranks.

## 5. Legal two-carrier realization

Equation (3.4) is a signed four-column identity.  To use it without
violating the one-walk-per-carrier constraint, give the two diamond pairs
different carrier tags.

Let

\[
 V=L\cup\{z_1,\ldots,z_n\}\cup\{y,y'\}.
 \tag{5.1}
\]

Then

\[
 |V|=m+Q+2.
\]

Choose two distinct filler sets

\[
 F_0,F_1\subseteq[2m]\setminus V,
 \qquad
 |F_0|=|F_1|=H-Q-2,
 \tag{5.2}
\]

and put

\[
 U_0=V\cup F_0,\qquad U_1=V\cup F_1.
 \tag{5.3}
\]

For all sufficiently large calibrated parameters these choices exist and
may be made with \(U_0\ne U_1\), since \(Q=o(H)=o(m)\).

Use \(\mathcal C\) as the source collar chain in carrier \(U_0\), and
\(\mathcal C'\) in carrier \(U_1\).  In \(U_0\), let

\[
 P_0^+=P_{\mathcal C}^{\,y},
 \qquad
 P_0^-=P_{\mathcal C}^{\,y'}.
\]

In \(U_1\), reverse the sign convention:

\[
 P_1^+=P_{\mathcal C'}^{\,y'},
 \qquad
 P_1^-=P_{\mathcal C'}^{\,y}.
\]

Each pair has a common source and a common state after two moves.  Continue
the two paths in each carrier identically until each has \(M\) state
occurrences.

### Theorem 5.1 (positive tagged switch)

The exchange

\[
 \boxed{
 \{P_0^-,P_1^-\}
 \longleftrightarrow
 \{P_0^+,P_1^+\}}
 \tag{5.4}
\]

is a legal one-path-per-carrier switch.  Its complete incidence difference
is \(\Xi\) from Theorem 3.1.

Both configurations compile to words of the same length.  Relative to
having one chosen path in each carrier, the switch has zero reset,
initialization, connector, and bridge toll.

#### Proof

The two sides of (5.4) each choose exactly one path tagged by \(U_0\) and
one tagged by \(U_1\).  Inside each carrier, the two alternatives have the
same initialized source and the same continuation after their common
two-step endpoint.  Their pairwise differences are therefore the two
diamond strings in (3.4).  Theorem 3.1 gives the incidence statement.

An \(M\)-state rotor walk has literal length \(M+2Q+1\).  Both alternatives
inside a carrier use the same reverse-block initialization and the same
number of later updates, so switching them changes no length term.
\(\square\)

No formal negative state is being inserted into a word.  The signs in
(3.4) compare two positive two-carrier configurations.

## 6. Why four templates are the first legal size

At any controlled rank, every length-\(M\) carrier path contributes exactly
\(M\) flag occurrences.  Therefore a signed path-column identity which
vanishes at even one such rank must satisfy

\[
 \sum_R c_R=0.
 \tag{6.1}
\]

For a unit switch, \(c_R\in\{-1,+1\}\).  Three path templates cannot satisfy
(6.1).  A formal coefficient pattern \(1+1-2=0\) uses two copies of the
negative template and hence four path occurrences after carrier tags are
restored.

There can be three-edge cycles in the base cochain graph of Section 1, but
each edge is itself a difference of two positive paths.  Such a triangle
uses at least six path occurrences.  It is not a three-column legal switch.

Two path columns can have zero coefficient sum, but changing a single
arrival diamond gives the full vertical string (2.9), not a rank-isolated
direction.  The adjacent-chain second difference requires two diamond
pairs, so the tagged four-column switch (5.4) is minimal within this local
arrival-diamond architecture.

## 7. The paired-diamond gate, subsequently refuted

The local algebraic connector problem posed here is solved: a four-template
cross-carrier coboundary has \(O(1)\) full norm and can isolate the middle
owner or any chosen interior hard rank.

The initially suggested global selection problem was the following.

> **Packed paired-diamond lemma \((\mathrm{PPD}_Q)\).**  
> Pair all but \(o(N_H)\) carriers and use the paired-swap conveyor of
> Section 8 to obtain \(\Theta(M)\) controlled-band directions in every
> pair.  Choose the initial paired states, common departures and arrivals,
> rank parities, and the remaining deterministic continuations so that the
> complete path family has aggregate excess collision \(o(W)\).

The initial collars and their physical adjacent pairs must vary with the
carrier.  A single global coordinate pairing remains excluded by the
positive Gaussian pair-type capacity deficit; the conveyor solves connector
chronology, not mixed-frame owner allocation.

Section 9 proves that \((\mathrm{PPD}_Q)\) is false: independently of the
arrival-order bits, its shared source occurrences create a positive linear
middle-owner collision loss.  Section 8 remains useful as an exact local
chronology theorem, but not as a near-cover architecture.

## 8. A paired-swap conveyor packs linearly many directions

The four-template gadget can be repeated without resetting either carrier.
We work first at the quotient level, which is the level needed for the
controlled band.

Suppose two carrier states have the same lower block \(L\), the same collar
labels, and the same collar order except for one adjacent swap:

\[
\begin{aligned}
 \omega_0&=(L;z_1,\ldots,z_{p-1},a,b,z_{p+2},\ldots,z_n;R_0),\\
 \omega_1&=(L;z_1,\ldots,z_{p-1},b,a,z_{p+2},\ldots,z_n;R_1).
\end{aligned}
 \tag{8.1}
\]

Their carriers may differ.  Assume that \(R_0\cap R_1\) contains two
labels \(y,y'\).  Choose common distinct departures \(x,x'\in L\).
In each carrier use the two legal arrival orders \(y,y'\) and \(y',y\),
and tie the two carrier bits oppositely as in (5.4).

### Lemma 8.1 (transport of the swap)

If \(p\le n-3\), every one of the four two-step paths ends with common lower
block

\[
 L'=L-\{x,x'\}+\{y,y'\},
\]

and the two carrier collars still differ by the same adjacent swap, now in
positions \(p+2,p+3\).

The associated two-carrier switch is zero at every controlled rank except

\[
 r=m-Q+p+1,
 \tag{8.2}
\]

where it is one elementary rectangle of squared norm four.

#### Proof

The common endpoint formula (2.4) gives the new collar

\[
 (x',x,z_1,\ldots,z_{n-2}).
\]

Thus the old positions \(p,p+1\) move to \(p+2,p+3\).  Since
\(p\le n-3\), both remain in the controlled collar.  The lower blocks use
the same removed and added sets and are equal.  The two source base chains
differ only by interchanging the increments \(a,b\), which occur in
positions \(p+1,p+2\) of the increment sequence \(x,z_1,\ldots,z_n\).
Theorem 3.1 therefore isolates rank (8.2). \(\square\)

If the swap begins in positions \(n-1,n\), the same two moves eject both
labels into the unordered quotient tail.  The two quotient states then
coalesce.  This gives a clean odd-position cycle:

\[
 p=1,3,5,\ldots,n-1.
 \tag{8.3}
\]

It contains exactly \(Q\) useful diamond blocks.

### Lemma 8.2 (front-swap injection)

From two coalesced quotient states with common lower block and collar,
choose common arrivals \(y,y'\), but use departure order \(x,x'\) in the
first carrier and \(x',x\) in the second.  After these two deterministic
updates, the lower blocks again agree and the collars differ only by the
adjacent swap

\[
 (x',x)\longleftrightarrow(x,x')
\]

in positions \(1,2\).

#### Proof

Both lower blocks remove the same set \(\{x,x'\}\) and add the same arrival
set \(\{y,y'\}\).  The endpoint collar records the departure order in
reverse chronological order.  All older collar labels shift two positions
identically. \(\square\)

The injection block carries no repair bit.  It is followed by the \(Q\)
useful blocks in (8.3), after which the quotient states coalesce and the
cycle repeats.

### Theorem 8.3 (linear packed paired-diamond cube)

Let two carriers differ by only one filler label outside a common visible
set.  Then their residual-block intersection has size \(H-Q-1\), and the
construction above can be continued for \(M-1\) updates.  It contains

\[
 \boxed{\frac M2-O\!\left(\frac M Q+Q\right)
       =\frac M2-o(M)}
 \tag{8.4}
\]

independently switchable two-carrier bits.  Every bit has complete
controlled-band incidence equal to one elementary rectangle at the rank
(8.2) assigned to its current swap position, and zero at every other
controlled rank.

#### Proof

At a useful block, both carriers remove the same two common lower labels,
remove the same two common residual labels, and add the same two evicted
collar labels to their residual sets.  Hence equality of lower blocks and
the one-label difference of residual blocks are preserved.  In particular
the residual intersection keeps size \(H-Q-1\ge2\), so two common arrivals
are always available.  The common lower block has size \(m-Q\ge2\), so two
common departures are always available.

Every useful or injection block uses two updates.  A cycle has \(Q\) useful
blocks and one injection block.  Apart from an initial and terminal
remainder of \(O(Q)\) updates, the useful-block density is

\[
 \frac{Q}{Q+1}.
\]

This gives (8.4).  Each arrival-order choice has a common endpoint inside
its own carrier, so choices made in disjoint blocks are independent and do
not alter any later source state.  Lemma 8.1 and Theorem 3.1 give the
rank-isolated incidence of each bit. \(\square\)

An even-position conveyor is obtained similarly.  When its swap reaches
positions \(n-2,n-1\), one additional deterministic cleanup update lets
the last collar label fall into the quotient tail before the next
front-swap injection.  Using both parities across different carrier pairs
provides every rank from \(m-Q+2\) through \(m+Q\).  The omitted lowest
interior rank \(m-Q+1\) has \(N_{Q-1}=o(W)\) targets in the calibrated
regime and can be left to the sparse boundary completion.

The word ledger is unchanged: every configuration still chooses one
\(M\)-state walk per carrier and one initialization per walk.  Hence the
packed cube has no additional interface toll.

### 8.1 Exact scope of the packing theorem

Theorem 8.3 is exact for the quotient flags of ranks
\([m-Q,m+Q]\).  In the isolated gadget of Sections 2--5, the physical tail
is one block, and the four-template switch also cancels rank \(m+Q+1\) and
every higher rank.  During a long conveyor, the literal MTF tail becomes
refined.  Arrival-order switches can then affect additional prefix unions
above \(m+Q\), and no all-rank cancellation theorem for those refined-tail
flags is claimed.

This is harmless for the stated hard-band coboundary and for a construction
which handles the sparse outer ranks independently.  It must nevertheless
be included in any future claim about a full-load covariance kernel.

## 9. Global owner-duplication correction

The conveyor of Section 8 is not compatible with the owner near-factor.
The exact audit is in
MATH_AUDIT_PAIRED_DIAMOND_DUPLICATION_AND_EIGHT_TEMPLATE_20260725.md.

Every useful-block source gives an equal owner occurrence across the two
paired carriers unless the traveling swap is precisely at slots
\(Q,Q+1\).  Only one block per \(Q\)-block sweep is exceptional.  Hence a
carrier pair forces \(M/2-o(M)\) equal-owner occurrence pairs, and pairing
almost all carriers forces middle collision excess

\[
 \frac14W-o(W).
\]

Thus Theorem 8.3 remains a correct controlled-band chronology and direction
capacity theorem, but it cannot be used as the primary near-cover.

The successor is an eight-path, four-carrier Johnson-cycle coboundary.
Four diamond vertical strings form a cycle with four distinct source and
endpoint owners.  Perturbing one edge chain at one adjacent increment
leaves one rank rectangle of squared norm four and cancels every other
rank.  Both configurations are owner-disjoint throughout the local
three-state gadget.  Packing these separated cycles globally is the new
open gate.
