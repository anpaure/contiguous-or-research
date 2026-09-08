# Literal monotone use of the rectangular compiled cube

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The connector states in the rectangular compiled cube are not noise from
the positive-coverage point of view.  They form an exact **vertical Boolean
braid**.

For a carrier-rotor transition, let \(F_h(t)\) be the flag of rank
\(m-Q+h\), \(0\le h\le2Q\).  Then, simultaneously for every admissible
\(h\),

\[
 F_h(t)\cap F_h(t+1)=F_{h-1}(t),
 \qquad
 F_h(t)\cup F_h(t+1)=F_{h+1}(t+1).
 \tag{0.1}
\]

Every \(F_h(t)\) is literally the OR of a contiguous suffix of the compiled
word.  If \(X_t=F_Q(t)\) is the middle owner, iteration of (0.1) gives

\[
 F_{Q-q}(t)=\bigcap_{i=0}^{q}X_{t+i},
 \qquad
 F_{Q+q}(t)=\bigcup_{i=0}^{q}X_{t-i}.
 \tag{0.2}
\]

Thus all connector flags are exactly the lower and upper path-hitting
shadows of the connector-owner chronology.  No signed cancellation theorem
is needed to use them positively.

There is, however, a sharp distinction between two uses of the cube.

1. **Whole-route monotone use is valid.**  Once one compiled route is
   selected, every one of its connector flags is free positive coverage.
   A precise excess-collision condition below is sufficient for a
   \(W+o(W)\) contiguous-OR word.
2. **Bit-by-bit monotone repair is invalid.**  Toggling one static cube bit
   replaces one vertical braid by another.  At each of
   \(\Omega(Q)\) ranks its full incidence difference has both positive and
   negative coordinates.  Hence the toggle is not a coordinatewise
   positive augmentation, even though its two marked endpoints realize a
   rank-isolating rectangle.

The exact remaining problem is therefore an augmented, mixed-frame
near-factor problem for the **complete braid supports**, not a problem of
cancelling connector variance.  Moreover, the connectors are forced to do
almost all of the work: the marked states occupy only \(o(W)\) global
positions, whereas any coefficient-one construction must obtain
\(W-o(W)\) distinct middle owners from connector states.

## 1. Quotient flags and the literal word

Fix a carrier \(U\in\binom{[2m]}M\), where

\[
 M=m+H,
 \qquad n=2Q.
\]

A quotient rotor state is

\[
 \omega=(A;z_1,\ldots,z_n;B),
 \tag{1.1}
\]

where

\[
 |A|=m-Q,
 \qquad |B|=H-Q,
\]

and the displayed blocks partition \(U\).  Put

\[
 F_h(\omega)=A\cup\{z_1,\ldots,z_h\},
 \qquad 0\le h\le n.
 \tag{1.2}
\]

The rotor update with \(x\in A\) and \(y\in B\) is

\[
 (A;z_1,\ldots,z_n;B)
 \longmapsto
 (A-x+y;x,z_1,\ldots,z_{n-1};B-y+z_n).
 \tag{1.3}
\]

Let

\[
 P=(\omega_0,\ldots,\omega_{s-1})
\]

be a directed rotor walk.  Initialize \(\omega_0\) by writing

\[
 R,\{z_n\},\ldots,\{z_1\},A,
 \tag{1.4}
\]

where \(R=B\cup([2m]\setminus U)\), and append the new core at every later
rotor step.  This is the usual literal word of length

\[
 s+2Q+1.
 \tag{1.5}
\]

### Theorem 1.1 (exact suffix-OR column)

At the word position corresponding to \(\omega_t\), every set
\(F_h(\omega_t)\), \(0\le h\le2Q\), is the OR of a contiguous suffix ending
at that position.

More precisely, among the suffix ORs ending there whose ranks lie in

\[
 [m-Q,m+Q],
\]

the distinct sets are exactly

\[
 F_0(\omega_t),F_1(\omega_t),\ldots,F_{2Q}(\omega_t).
 \tag{1.6}
\]

#### Proof

After the letter producing \(\omega_t\) is written, the last-occurrence
partition begins

\[
 A_t,\{z_1(t)\},\ldots,\{z_{2Q}(t)\}.
\]

The ORs of suffixes ending at the current position are precisely the prefix
unions of that last-occurrence partition.  The first block has size
\(m-Q\), and the next \(2Q\) blocks are singletons.  Their prefix unions are
exactly (1.6).  A shorter suffix cannot take a proper subset of the current
letter \(A_t\), and the next tail block produces rank larger than \(m+Q\).
\(\square\)

This is an exact contiguous-OR statement.  It does not discard connector
positions, and it does not infer physical coverage from a marked-state
projection.

## 2. The connector is a vertical Boolean braid

### Theorem 2.1 (one-step braid identities)

Let \(\omega'\) be the successor (1.3) of \(\omega\).  Then

\[
 F_0(\omega')=F_0(\omega)-x+y,
 \tag{2.1}
\]

and, for \(1\le h\le n\),

\[
 \boxed{F_h(\omega')=F_h(\omega)-z_h+y.}
 \tag{2.2}
\]

Consequently every controlled-rank row makes a nonlazy Johnson step.  In
addition,

\[
 \boxed{
 F_h(\omega)\cap F_h(\omega')=F_{h-1}(\omega)}
 \qquad(1\le h\le n),
 \tag{2.3}
\]

and

\[
 \boxed{
 F_h(\omega)\cup F_h(\omega')=F_{h+1}(\omega')}
 \qquad(0\le h<n).
 \tag{2.4}
\]

#### Proof

For \(h\ge1\), the first \(h\) collar labels after the update are

\[
 x,z_1,\ldots,z_{h-1}.
\]

Thus

\[
 F_h(\omega')
 =(A-x+y)+x+z_1+\cdots+z_{h-1}
 =A+y+z_1+\cdots+z_{h-1},
\]

which is (2.2).  Here \(y\notin F_n(\omega)\), while
\(z_h\in F_h(\omega)\), so the step is nonlazy.  Taking the intersection
and union of

\[
 A+z_1+\cdots+z_h
 \quad\hbox{and}\quad
 A+y+z_1+\cdots+z_{h-1}
\]

gives (2.3)--(2.4). \(\square\)

Each physical connector letter therefore advances **all** \(2Q+1\)
controlled ranks at once.  Its local occurrence efficiency is maximal:
one letter produces one new candidate flag at every controlled rank.  The
unresolved issue is distinctness, not literal productivity.

### Corollary 2.2 (iterated path-hitting identities)

Write

\[
 X_t=F_Q(\omega_t).
\]

For every \(0\le q\le Q\), whenever the displayed owner indices belong to
the walk,

\[
 \boxed{
 F_{Q-q}(\omega_t)=\bigcap_{i=0}^{q}X_{t+i}},
 \tag{2.5}
\]

\[
 \boxed{
 F_{Q+q}(\omega_t)=\bigcup_{i=0}^{q}X_{t-i}}.
 \tag{2.6}
\]

At the two ends of a finite walk the same identities hold after any legal
\(Q\)-step rotor extension.  Such an extension is only a certificate for
the identities: it is not appended to the literal word, because Theorem
1.1 already exposes the endpoint flags.

#### Proof

At each forward step, (2.2) deletes the collar label currently in position
\(Q\).  During the next \(q\le Q\) steps these deleted labels are

\[
 z_Q(t),z_{Q-1}(t),\ldots,z_{Q-q+1}(t),
\]

and are distinct.  The arrivals during these \(q\) steps lie outside
\(X_t\): before the first step they lie either in the tail or among collar
positions \(Q+1,\ldots,2Q\).  Intersecting the \(q+1\) consecutive owners
therefore deletes precisely these \(q\) labels from \(X_t\), giving
\(F_{Q-q}(\omega_t)\).  The union formula is the time-reversed statement
for the preceding \(q\) departures.  Regularity of the rotor graph supplies
legal predecessors and successors at a finite endpoint. \(\square\)

For a lower target \(T\) of rank \(m-q\), (2.5) says exactly that the
connector covers \(T\) when its owner chronology contains a consecutive
\((q+1)\)-vertex Johnson segment in the up-set of \(T\), with intersection
\(T\).  Equation (2.6) is the complementary upper statement.  This is the
path-hitting formulation; it makes no singleton-near-Ucycle assumption.

## 3. Exact global hole ledger

Use the calibrated height

\[
 H=\min\left\{h:\frac{W}{N_h}\ge m+h\right\},
 \qquad
 W=\binom{2m}{m},
 \qquad
 N_q=\binom{2m}{m-q},
 \tag{3.1}
\]

and put \(M=m+H\).  Let

\[
 N_H=\binom{2m}{m-H},
 \qquad
 S=MN_H.
 \tag{3.2}
\]

Choose one \(M\)-state compiled rectangular-cube route \(P_U\) for every
carrier \(U\in\binom{[2m]}M\).  Choices may include the cube vertex, cyclic
frame, buffers, and the \(O(Q)\) final padding.  At every controlled rank
\(r=m\pm q\), the complete braid supplies exactly \(S\) flag occurrences.

Let

\[
 D_r=\#\{F_{r-(m-Q)}(\omega):
          \omega\hbox{ is a selected route state}\}
 \tag{3.3}
\]

be the number of distinct selected flags at rank \(r\), and define

\[
 C_r=S-D_r
 \tag{3.4}
\]

to be the collision count.  Since rank \(m\pm q\) has \(N_q\) targets, its
uncovered count is exactly

\[
 h_r=N_q-D_r=N_q-S+C_r.
 \tag{3.5}
\]

It is useful to subtract the collision forced merely by having more
occurrences than targets.  Put

\[
 E_r=C_r-(S-N_q)_+\ge0.
 \tag{3.6}
\]

Then the exact hole identity is

\[
 \boxed{h_r=(N_q-S)_++E_r.}
 \tag{3.7}
\]

The first term is a deterministic occurrence shortage.  The second is the
true excess-collision loss of the selected vertical braids.

### Proposition 3.1 (the deterministic shortage sums to \(o(W)\))

In the calibrated regime,

\[
 \sum_{q=0}^{Q}(2-\mathbf1_{q=0})(N_q-S)_+=o(W).
 \tag{3.8}
\]

#### Proof

Write

\[
 c=\frac{W/N_H}{M},
 \qquad S=\frac Wc.
\]

Minimality of \(H\), together with

\[
 \frac{W/N_H}{W/N_{H-1}}
 =\frac{m+H}{m-H+1},
\]

gives, for all sufficiently large \(m\),

\[
 1\le c\le1+\frac{3H}{m}.
 \tag{3.9}
\]

Also

\[
 \frac W{N_q}
 =\prod_{i=1}^{q}\frac{m+i}{m-i+1}
 \ge1+\sum_{i=1}^{q}\frac{2i-1}{m}
 =1+\frac{q^2}{m}.
 \tag{3.10}
\]

If \(N_q>S\), then \(W/N_q<c\), so (3.9)--(3.10) imply

\[
 q^2<3H.
\]

There are therefore only \(O(\sqrt H)\) depths with positive shortage, and
each shortage is at most

\[
 W-S\le\frac{3WH}{m}.
\]

Consequently the left side of (3.8) is

\[
 O\!\left(\frac{WH^{3/2}}m\right)=o(W),
\]

because \(H\asymp\sqrt{m\log m}\). \(\square\)

### Theorem 3.2 (all-connector positive compiler)

Suppose the selected routes satisfy

\[
 \boxed{
 \sum_{q=0}^{Q}
 \bigl(E_{m-q}+\mathbf1_{q>0}E_{m+q}\bigr)=o(W).}
 \tag{3.11}
\]

Then one literal nonzero contiguous-OR word covers every target in the
rank band \([m-Q,m+Q]\) and has length \(W+o(W)\).

If the already-audited sparse outer-rank reservoir is appended, the same
word covers all nonempty masks with length \(W+o(W)\).

#### Proof

Compile and concatenate the \(N_H\) selected routes.  By (1.5), their total
length is

\[
 S+(2Q+1)N_H
 =W+o(W),
 \tag{3.12}
\]

because \(S=W-o(W)\) and \(QN_H=O(QW/m)=o(W)\).  Every flag counted by
\(D_r\) is a literal contiguous OR by Theorem 1.1.  Append each missing
hard-band target once.  Equations (3.7), (3.8), and (3.11) show that the
number appended is \(o(W)\).  Concatenation cannot destroy any interval
already present inside an individual route word. \(\square\)

Condition (3.11) is an exact integral near-factor gate for the augmented
packet hypergraph whose columns are complete compiled braids.  It is a
support statement, not a covariance statement.  The global choices must
be owner-dependent and must mix cyclic frames/coordinate matchings: the
known fixed-pair Gaussian capacity deficit rules out satisfying this gate
inside one global coordinate pairing.

## 4. The connectors are forced to carry the construction

For the rectangular compilation, \(t\) is maximal subject to

\[
 (2t-1)(4Q+2)\le M.
\]

Hence

\[
 2t=\left(\frac1{4Q}+o\!\left(\frac1Q\right)\right)M.
 \tag{4.1}
\]

There are \(2t\) marked state occurrences per carrier.  The unused padding
is less than \(8Q+4\) states per carrier.  The two cyclic bridge updates
between successive ports contribute \(2(t-1)\) further non-flush states.
Globally,

\[
 2tN_H
 =\left(\frac1{4Q}+o\!\left(\frac1Q\right)\right)W=o(W),
 \tag{4.2}
\]

\[
 O\bigl((Q+t)N_H\bigr)=o(W).
 \tag{4.3}
\]

The reset letters also total \(O(QN_H)=o(W)\).  Thus

\[
 \boxed{
 \text{flush/reload connector states account for }W-o(W)
 \text{ of the }W+o(W)\text{ physical positions}.}
 \tag{4.4}
\]

### Proposition 4.1 (middle-owner necessity)

Any coefficient-one use of these compiled routes which leaves only \(o(W)\)
middle targets for literal completion must obtain \(W-o(W)\) distinct
middle owners from flush/reload connector states.

More generally, for every \(q=o(\sqrt m)\), connector states must provide
\(W-o(W)\) distinct flags separately at each of ranks \(m-q\) and \(m+q\).

#### Proof

Suffix ORs ending at a fixed word position form a nested family, so that
position can produce at most one distinct target of any prescribed rank.
There are \(W\) middle targets, while marked, cyclic-bridge, padding, and
reset positions together number \(o(W)\).  If only \(o(W)\) targets are
completed later, the connector endpoints must supply all but \(o(W)\) of
the distinct middle targets.

For \(q=o(\sqrt m)\),

\[
 N_q=W\exp\!\left(-\frac{q^2}{m}+o(1)\right)=W-o(W),
\]

and the same position count proves the rank-\(m\pm q\) statement. \(\square\)

So the designated marked rectangles cannot be the primary cover, with
connectors treated as harmless overhead.  The logical direction is the
reverse: the connector braids must form the near-factor, and the marked
rectangles can only serve as a sparse adjustment mechanism inside that
near-factor.

## 5. Sharp obstruction to bitwise monotone repair

The positive theorem above selects whole routes.  It does not turn an
individual static cube bit into a monotone coverage increment.

Consider the two coupled flush/reload routes whose source collars differ
by an adjacent transposition in positions \(r,r+1\), with \(r\le Q\).  Let
\(\mu_h^0,\mu_h^1\) be their complete flag-incidence vectors at prefix
length \(h\).  The exact connector audit gives, for every

\[
 r+1\le h\le2Q-1,
\]

\[
 \|\mu_h^1-\mu_h^0\|_2^2=4,
 \tag{5.1}
\]

with two positive and two negative unit coordinates.  In particular,

\[
 \mu_h^1\not\ge\mu_h^0,
 \qquad
 \mu_h^0\not\ge\mu_h^1
 \tag{5.2}
\]

coordinatewise.  This range includes the middle rank for every active row
pair of the rectangular cube.

Thus a bit toggle necessarily removes physical flag multiplicity while it
adds other multiplicity at \(\Omega(Q)\) ranks.  Redundancy elsewhere may
make those removals harmless at the final support level, but that is a
global property and cannot be inferred from the local rectangle identity.
Adding both braid choices would restore monotonicity, but doing so on a
positive proportion of carriers doubles \(W-o(W)\) connector positions and
is coefficient-fatal.

This is the sharp obstruction to a greedy interpretation of the connector
as a rank-isolating monotone absorber.  The connector is beneficial only as
part of the selected whole-route braid.

## 6. Exact reduced lemma

The rectangular compiled-cube line is now reduced to the following purely
combinatorial statement.

> **Mixed-frame rectangular vertical-braid lemma
> \((\mathrm{RVB}_Q)\).**  
> For every \(M\)-carrier \(U\), choose one cyclic frame, one rectangular
> cube vertex, equivariant flush/reload buffers, and an \(M\)-state padded
> compiled route.  The frames and coordinate pairings may depend on \(U\).
> For the complete flag columns of all chosen states, the aggregate excess
> collision (3.11) is \(o(W)\).

By Theorem 3.2, \((\mathrm{RVB}_Q)\) gives the coefficient-one
contiguous-OR theorem after the sparse outer completion.  Proposition 4.1
shows that an owner-only near-transversal is a necessary first part of
\((\mathrm{RVB}_Q)\), but (2.5)--(2.6) identify the additional requirement:
the selected owner chronologies must simultaneously be near-surjective
under all lower intersection and upper union window maps.

The local compiler has no remaining interface toll: its one-reset cost is

\[
 (2Q+1)N_H=o(W),
\]

and all endpoint flags, including the first and last \(Q\) positions of a
route, are retained literally.  The unresolved toll is entirely the
support loss measured by (3.11).

## 7. Disjoint equal-port pairing does not telescope the braid

One natural attempt is to pair adjacent ports and impose

\[
 E_{i,2s}=E_{i,2s+1}.
 \tag{7.1}
\]

The marked projection of the common bit is then

\[
 \rho_{i,2s}+\rho_{i,2s+1},
 \tag{7.2}
\]

so the two desired rectangles are retained.  Moreover, after the two
cyclic steps between ports, the source orientation is complementary and
the active row-pair boundary has moved two collar positions.  At the level
of rank support alone this looks like a telescoping pair.  Exact mask
support shows that it does not telescope.

### 7.1 The cap drift

Consider a flush source

\[
 \omega=(A;z_1,\ldots,z_n;B),
 \qquad n=2Q,
\]

with active row pair

\[
 u=z_r,\qquad v=z_{r+1}.
\]

Let \(b\in B\) be the tail label used for the prescribed core--tail
exchange and define the extended cap

\[
 D=A\cup\{z_1,\ldots,z_n\}\cup\{b\}.
 \tag{7.3}
\]

For the source-collar transposition, the exact audit formulas show that at
prefix length \(h=n-1\) the two transposition-edge bases are

\[
 K=D-\{u,v,z_{r+2}\},
 \tag{7.4}
\]

and, when \(r\ge2\),

\[
 J=D-\{u,v,z_{r-1}\}.
 \tag{7.5}
\]

For \(r=1\), the third deletion in \(J\) is a core buffer rather than
\(z_{r-1}\).  This endpoint variation will not matter below.  In every
case the source trace has squared norm four.

After two genuine cyclic rotor steps, the collar is

\[
 (x_2,x_1,z_1,\ldots,z_{n-2}).
 \tag{7.6}
\]

Thus the old far-collar labels

\[
 \ell_1=z_{n-1},\qquad \ell_2=z_n
\]

have fallen into the tail.  Adding the new active core--tail exchange label
restores the right boundary of the cyclic interval but does not restore
\(\ell_1,\ell_2\).  Consequently the shifted extended cap has the exact
form

\[
 D'=D-\{\ell_1,\ell_2\}+\{\eta_1,\eta_2\},
 \tag{7.7}
\]

where \(\eta_1,\eta_2\) are the two new right-boundary labels.  All four
labels in (7.7) are distinct.  Column swaps do not change this set identity:
the active swap merely exchanges which right-boundary label is in the core
and which is the prescribed tail label, and their union is the same cap.

### Proposition 7.1 (two-step source-pair counterterm)

Couple two source flushes with opposite row orientation, the second starting
after the two cyclic steps.  The row boundary changes from \(r\) to \(r+2\).
Let \(\Delta_h\) be their combined transposition-incidence difference at
prefix length \(h\).  For every

\[
 r+3\le h\le n-1,
\]

\[
 \boxed{\|\Delta_h\|_2^2=8.}
 \tag{7.8}
\]

In particular the residue occupies \(\Omega(Q)\) ranks, not \(O(1)\) seam
ranks.

#### Proof

For \(h\ge r+3\), each of the two source-flush traces has squared norm four
by the exact source-collar calculation.  Every mask in the first trace
contains \(z_n\).  Indeed its moving-boundary base contains the returned
suffix ending in \(z_n\), and its one-step core--tail base contains the
whole suffix \(z_{r+2},\ldots,z_n\).

Every mask in the shifted trace is contained in \(D'\), which omits \(z_n\)
by (7.7).  The two four-coordinate traces therefore have disjoint supports.
Their orientations are opposite, but disjoint support prevents
cancellation, giving squared norm \(4+4=8\).  Target-reload traces cannot
alter (7.8), because a target transposition at boundary \(r\), respectively
\(r+2\), is supported only at prefix lengths at most \(r\), respectively
\(r+2\). \(\square\)

The obstruction is an exact **cap-translation counterterm**.  The active
transposition boundary moves by two, but the Boolean bases also lose two
old coordinates and gain two new ones.  Equality of ranks is therefore not
equality of masks.

### 7.2 Audit of the complete two-port block

A common bit in ports \(j,j+1\) affects all adjacent routed pieces, not only
the route from \(A_j\) to \(B_j\) and the route from \(C_j\) to
\(A_{j+1}\).  At high prefix lengths, target-reload traces vanish, and the
source-flush traces occur in the following order:

\[
 \begin{array}{c|c|c}
 \text{source}&\text{phase}&\text{orientation sign}\\ \hline
 A_j&s_j&+\\
 C_j&s_j+2&-\\
 A_{j+1}&s_j+2&+\\
 C_{j+1}&s_j+4&-
 \end{array}
 \tag{7.9}
\]

With the most favorable common-buffer coupling, the two middle traces in
(7.9) cancel exactly.  Their source cores differ by the active column
exchange, but adjoining the prescribed tail label gives the same extended
cap, and their collar orders agree apart from the reversed row orientation.
The complete paired-port source residue is therefore

\[
 S_r(D_{s_j})-S_{r+4}(D_{s_j+4}).
 \tag{7.10}
\]

Four cyclic steps replace four far-collar labels by four new right-boundary
labels.  Repeating the proof of Proposition 7.1 gives

\[
 \boxed{
 \|\Delta_h^{\mathrm{pair}}\|_2^2=8
 \qquad(r+5\le h\le n-1).}
 \tag{7.11}
\]

Again there are \(\Omega(Q)\) nonzero ranks.  The incoming target reload at
\(A_j\), the three internal target reloads, and the outgoing endpoint terms
are all supported below the corresponding active boundaries and hence
cannot cancel (7.11).

Thus (7.1) does retain the marked sum (7.2), but it does **not** convert the
complete connector braid into an \(O(1)\)-rank seam.  It merely turns the
uncancelled source trace into a phase-four cap derivative.  Any successful
paired-port modification must transport the two (or four) fallen
far-collar labels back into the shifted cap, or use a genuinely nonlocal
multi-top cancellation.  Ordinary cyclic advance plus equal port bits
cannot do so.

## 8. A different four-template coboundary succeeds locally

The failure in Section 7 is specific to phase translates of the
flush-and-reload template.  It is not a universal connector invariant.
The exact successful alternative is proved in
MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md.

Two legal arrival orders in a two-step rotor diamond have common endpoints
and differ by one vertical flag string.  Take two such diamonds whose
saturated base chains differ by one adjacent increment.  The difference of
their vertical strings cancels at every rank except the rank of that
increment swap, where one elementary rectangle remains.

Embedding the two diamonds in two distinct carriers gives a positive
four-path switch, one path per carrier on both sides, with no additional
letters.  At the middle rank its complete physical direction has squared
norm four and zero incidence at all nonmiddle ranks.  The remaining issue
is no longer local connector cancellation but coefficient-scale packing:
synchronize \(\Theta(M)\) such paired diamonds per carrier pair while
retaining the complete-braid near-cover.

This last paired-carrier packing is now known to fail by forced owner
duplication.  The audit and its eight-template owner-separated successor
are in
MATH_AUDIT_PAIRED_DIAMOND_DUPLICATION_AND_EIGHT_TEMPLATE_20260725.md.
The paired conveyor forces \(W/4-o(W)\) middle collision excess; a
four-carrier Johnson cycle removes the local duplication while retaining
the same rank-isolated norm-four rectangle.
