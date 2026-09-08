# Whole Latin tubes: matching, rooted absorption, and the exact omitted-owner ledger

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, search, or web input
is used.

## 0. Outcome

The two-update Latin connector upgrades the local eight-template blocks to
whole legal four-carrier tubes.  The exact global absorption theorem is now
available: once a carrier-disjoint family of whole tubes and a cell-rooted
rectangle decomposition of its owner defect are given, committing the cell
signs produces a genuine owner matching, with no connector or positivity
loss.

The omitted-owner ledger is exact.  If \(t\) whole tubes are used and each
carrier contributes \(M\) designated middle-owner states, then

\[
 \boxed{|\mathcal L|=W-4Mt.}
 \tag{0.1}
\]

If the tubes use all but \(r\) of the
\(N_H=\binom{2m}{m+H}\) carrier tags, so that \(4t=N_H-r\), then

\[
 \boxed{
 |\mathcal L|
 =W-M(N_H-r)
 =(W-MN_H)+Mr.}
 \tag{0.2}
\]

At the calibrated depth,

\[
 W-MN_H=O(WH/m)=o(W).
 \tag{0.3}
\]

Thus \(r=o(N_H)\) gives \(|\mathcal L|=o(W)\).  Initial and terminal
literalization costs are

\[
 O(Qt)=O(QN_H)=O(WQ/M)=o(W),
 \tag{0.4}
\]

so a squarefree tube family with \(r=o(N_H)\) compiles at length
\(W+o(W)\).

There is a stronger necessary ledger.  Let \(\Gamma_a\) be the total number
of designated owner occurrences containing coordinate \(a\) in the unsigned
tube skeleton.  Every Latin rectangle preserves \(\Gamma_a\).  Therefore
the omitted owner family must satisfy

\[
 \boxed{
 d_a(\mathcal L)=\frac W2-\Gamma_a
 \qquad(a\in[2m]).}
 \tag{0.5}
\]

This first-moment condition is exact and cannot be recovered from the scalar
leave (0.1).  In the balanced cyclic-interval case
\(\Gamma_a=2Mt\) for every coordinate, (0.5) becomes

\[
 d_a(\mathcal L)=|\mathcal L|/2.
 \tag{0.6}
\]

Here \(|\mathcal L|\) is even, because
\(W=2\binom{2m-1}{m-1}\) and \(4Mt\) is divisible by four.  A leave with
(0.6) is therefore explicit: take \(|\mathcal L|/2\) distinct complementary
pairs \(\{X,X^c\}\).

There is also a sharp limit on absorption.  The tube contains
\((1/16-o(1))W\) marked flag cells over all ranks, but the transported swap
meets a middle-owner-sensitive cut only \(O(1)\) times per \(\Theta(Q)\)
cells.  Hence only

\[
 O(W/Q+WQ/M)=o(W)
\]

cells can change the middle-owner multiset.  The Latin bank cannot turn a
positive-density or Poisson-scale owner packing into a near-factor; the
whole-tube selection must already have \(o(W)\), in fact absorption-scale,
owner defect.

What is not proved is the unconditional existence of the required whole-tube
matching.  The cyclic-interval near-design ledger starts after a large
matching has been found; it does not supply the cell-rooted rectangle
decomposition needed below.  The remaining theorem is an exact hereditary
Hall statement for marked rectangles in whole tubes.  This note proves the
matching/absorption implication and shows precisely which global input is
still absent; it does not invoke a growing-uniformity nibble as a black box.

## 1. Whole-tube notation

Put

\[
 W=\binom{2m}m,
 \qquad M=m+H,
 \qquad N_H=\binom{2m}M.
 \tag{1.1}
\]

A **whole Latin tube** consists of four distinct carrier tags and four legal
length-\(M\) quotient paths.  Away from \(O(Q)\) boundary states, each group
of four updates consists of

1. one two-update owner-separated Latin block; and
2. the two-update triple-to-singleton transport.

The transport theorem makes the last state of one cell a legal source for
the next cell.  A terminal remainder of at most three updates is continued
deterministically.  Thus every carrier has exactly \(M\) designated states,
whether or not every state belongs to a switchable cell.

For a tube \(T\), let

\[
 \mathcal O_T(\varepsilon)
 \tag{1.2}
\]

be its multiset of \(4M\) middle owners after choosing its cell-sign vector
\(\varepsilon\).  Different cells have common endpoints only in the temporal
sense: each physical state is counted once.  A tube is **squarefree** when
\(\mathcal O_T(\varepsilon)\) has \(4M\) distinct members.

For a carrier-disjoint family \(\mathscr T\) of tubes, put

\[
 \mu_\varepsilon(X)
 =\#\{\hbox{designated occurrences carrying }X\},
 \tag{1.3}
\]

counting over every tube in \(\mathscr T\).  The family is an owner matching
when \(\mu_\varepsilon(X)\le1\) for every \(X\).

## 2. Exact scalar and coordinate ledgers

### Proposition 2.0 (calibrated slot deficit)

Let \(H\) be the least positive integer for which

\[
 \lambda_H:=W/N_H\ge M=m+H.
 \tag{2.0}
\]

Then

\[
 \boxed{
 0\le W-MN_H
 <{2H-2\over M-1}\,W
 =O(WH/m).}
 \tag{2.0a}
\]

#### Proof

Minimality gives \(\lambda_{H-1}<M-1\), while the exact adjacent ratio is

\[
 {\lambda_H\over\lambda_{H-1}}
 ={m+H\over m-H+1}
 ={M\over m-H+1}.
\]

Consequently

\[
 1\le{\lambda_H\over M}
 <{M-1\over m-H+1}.
\]

Since \(MN_H/W=M/\lambda_H\), subtracting its reciprocal from one gives
(2.0a). \(\square\)

### Proposition 2.1 (scalar leave)

If \(|\mathscr T|=t\) and some sign choice makes \(\mathscr T\) an owner
matching, then the omitted owner family

\[
 \mathcal L
 =\binom{[2m]}m\setminus
   \bigcup_{T\in\mathscr T}\mathcal O_T(\varepsilon)
 \tag{2.1}
\]

has size exactly \(W-4Mt\).

If the tubes use \(N_H-r\) carrier tags, then (0.2) holds.
Necessarily

\[
 0\le r\le N_H,\qquad r\equiv N_H\pmod4.
 \tag{2.1a}
\]

#### Proof

An owner matching turns the \(4Mt\) designated occurrences into
\(4Mt\) distinct owners.  This proves the first identity.  Four carrier tags
belong to every tube, so \(4t=N_H-r\), proving the second identity and
(2.1a). \(\square\)

For a coordinate \(a\), define the unsigned skeleton incidence

\[
 \Gamma_a
 =\sum_{T\in\mathscr T}
   \sum_{X\in\mathcal O_T(0)}\mathbf1_{a\in X},
 \tag{2.2}
\]

where one arbitrary base sign is chosen in every cell.

### Proposition 2.2 (first-moment invariance)

The value \(\Gamma_a\) is independent of every cell sign.  If the final
family is an owner matching with leave \(\mathcal L\), then (0.5) holds.

#### Proof

One cell switch changes the owner incidence by a Johnson rectangle

\[
 e_{K+v+a+b}+e_{K+u+a+c}
 -e_{K+v+a+c}-e_{K+u+a+b}.
 \tag{2.3}
\]

Every coordinate occurs equally often with positive and negative sign in
(2.3).  Hence the switch preserves \(\Gamma_a\).  The full middle layer has
coordinate degree

\[
 \binom{2m-1}{m-1}=W/2.
\]

Subtracting the covered degree proves (0.5). \(\square\)

Summing (0.5) over all coordinates gives

\[
 \sum_a d_a(\mathcal L)
 =mW-\sum_a\Gamma_a
 =m(W-4Mt)=m|\mathcal L|,
 \tag{2.4}
\]

so the coordinate ledger is consistent with the scalar ledger.

Because \(\mathcal L\) is a simple family, (0.5) also gives the exact
coordinate feasibility cuts

\[
 \boxed{
 {W\over2}-|\mathcal L|
 \le\Gamma_a\le {W\over2}
 \qquad(a\in[2m]).}
 \tag{2.4a}
\]

If one of these inequalities fails, no choice of Latin cell signs can make
the skeleton owner-disjoint.  This obstruction is visible before any Hall
or absorption argument.

### Cyclic-interval specialization

Suppose every selected carrier path is one complete cyclic promotion packet
on its \(M\)-set.  Every one of its coordinates then occurs in exactly \(m\)
of the \(M\) middle windows.  If \(\mathcal U_0\) is the selected carrier
family, then

\[
 \boxed{
 \Gamma_a=m\,d_a(\mathcal U_0),
 \qquad
 d_a(\mathcal L)=W/2-m\,d_a(\mathcal U_0).}
 \tag{2.5}
\]

If all \(N_H\) carriers are used, coordinate symmetry gives

\[
 d_a(\mathcal U_0)
 =\binom{2m-1}{M-1}
 ={MN_H\over2m},
 \tag{2.6}
\]

and therefore

\[
 d_a(\mathcal L)={W-MN_H\over2}.
 \tag{2.7}
\]

This proves (0.6).  Notice that (2.5), rather than just (0.2), is the exact
omitted-owner ledger required by a cyclic-interval near-design.

## 3. Defect vectors and rooted cells

Fix a base sign in every switchable cell and write

\[
 \mu_0(X)=\mu_{\varepsilon=0}(X).
 \tag{3.1}
\]

Let \(\mathcal L\) be a proposed leave satisfying (0.1) and (0.5), and put

\[
 \mu_*(X)=\mathbf1_{X\notin\mathcal L},
 \qquad
 \delta=\mu_*-\mu_0.
 \tag{3.2}
\]

Then

\[
 \sum_X\delta_X=0,
 \qquad
 \sum_{X\ni a}\delta_X=0
 \quad(a\in[2m]).
 \tag{3.3}
\]

Fix one base alternative in every switchable cell.  Every cell \(c\) has a
set \(\mathcal R(c)\) of directed local Johnson rectangles which it can
realize by changing from that fixed base to another permitted alternative
while preserving its source, endpoint, and two-update transport ports.  A
**rooted rectangle assignment** for \(\delta\) is a choice of distinct cells
\(c_1,\ldots,c_s\) and directed rectangles

\[
 \rho_j\in\mathcal R(c_j)
 \tag{3.4}
\]

such that

\[
 \boxed{\delta=\sum_{j=1}^s\rho_j.}
 \tag{3.5}
\]

For a fully instantiated binary cell, \(\mathcal R(c)\) is normally the
singleton \(\{\rho_c\}\), where \(\rho_c\) is the change from its fixed base
alternative to the other alternative.  It is **not**
\(\{\rho_c,-\rho_c\}\): reversing the orientation also changes the base
owner vector \(\mu_0\).  A larger directed menu may be used only when all
its alternatives have the same fixed base and its port-stability has been
proved before the global matching; changing a cell's labels and silently
changing either \(\mu_0\) or its successor state is not allowed.

## 4. Whole-tube matching/absorption theorem

### Theorem 4.1 (rooted Latin absorption)

Let \(\mathscr T\) be a carrier-disjoint family of whole legal Latin tubes.
Assume:

1. every tube has \(M\) designated states on each of its four carriers;
2. the proposed leave \(\mathcal L\) satisfies (0.1) and (0.5); and
3. the defect vector (3.2) has a rooted rectangle assignment (3.4)--(3.5).

Then one can commit the signs of the assigned cells so that

\[
 \boxed{
 \mu_\varepsilon(X)=\mathbf1_{X\notin\mathcal L}
 \quad\text{for every middle owner }X.}
 \tag{4.1}
\]

In particular, the resulting whole tubes are globally owner-disjoint and
omit exactly \(\mathcal L\).

#### Proof

The two alternatives in one Latin cell have identical source, endpoint,
transport, and continuation.  Switching cell \(c_j\) therefore changes the
complete middle-owner incidence by exactly \(\rho_j\), without changing any
other cell or any physical port.  Distinct assigned cells can be switched
independently.  Starting from \(\mu_0\), switch all assigned cells.  Equation
(3.5) gives

\[
 \mu_\varepsilon=\mu_0+\delta=\mu_*.
\]

The right side is squarefree, so every cross-tube and within-tube owner
collision has disappeared.  Legality follows from the common-endpoint and
two-update transport identities. \(\square\)

This theorem is an absorption theorem for **whole paths**.  It does not cut
tubes into independently matched cells and then assume their ports can be
reassembled.

## 5. Exact word and omitted-owner cost

### Theorem 5.1 (coefficient ledger)

Under Theorem 4.1, suppose \(4t=N_H-r\), with \(r=o(N_H)\), and
\(Q=o(M)\).  Append every member of \(\mathcal L\) literally.  Then the
middle-owner word length is

\[
 \boxed{
 4Mt+|\mathcal L|+O(Qt)
 =W+O(QN_H)=W+o(W).}
 \tag{5.1}
\]

If the selected tubes also satisfy the cyclic-interval near-design ledger
with \(B=o(W)\) omitted nonmiddle targets, appending those targets gives
total length

\[
 W+O(QN_H)+B=W+o(W).
 \tag{5.2}
\]

#### Proof

The designated tube states contribute \(4Mt\) letters.  Literal
initialization and terminal linearization use \(O(Q)\) letters per tube.
Proposition 2.1 gives \(|\mathcal L|=W-4Mt\), proving (5.1).  The final
assertion adds the nonmiddle near-design leave. \(\square\)

The formula has no hidden owner loss: initialization flags may provide extra
witnesses, but their letters are already contained in the explicit
\(O(Qt)\) term.

## 6. The owner-active absorption bank is only \(O(W/Q)\)

Let \(G\) be the number of switchable cells in \(\mathscr T\).  The
two-update construction gives

\[
 G
 =t\left({M\over4}-O(Q)\right)
 ={4Mt\over16}-O(Qt).
 \tag{6.1}
\]

At calibrated full density,

\[
 G=\left({1\over16}-o(1)\right)W.
 \tag{6.2}
\]

This is the number of rank-isolated **flag** directions over all marked
ranks.  It is not the number of directions which change the middle-owner
multiset.

### Lemma 6.1 (owner-active phases)

Let the transported adjacent transposition occupy collar positions
\(p,p+1\) at the source of a complete cell.  Among the four designated
states of that cell, the two carrier traces separated by that transposition
can have different middle owners only if

\[
 \boxed{p\in\{Q,Q-1,Q-2,Q-3\}.}
 \tag{6.2a}
\]

After the cell the same transposition occupies positions \(p+4,p+5\).
Consequently a complete traversal of the \(2Q\)-collar, consisting of
\(\Theta(Q)\) cells, contains only \(O(1)\) owner-active cells.

#### Proof

The middle owner contains exactly the first \(Q\) collar positions.  At the
source, two carrier collars differing only by the transposition at \(p,p+1\) give
different owners exactly when \(p=Q\).  Each physical update prepends one
collar label, shifting the old transposition one position to the right.
At the four successive designated phases its left endpoint is therefore
\(p,p+1,p+2,p+3\).  It straddles the middle cut exactly when one of these
equals \(Q\), which proves (6.2a).  Four updates shift it by four positions,
so only the four displayed starting positions are active during one collar
traversal. \(\square\)

Outside these phases the carrier traces have recoalesced at the middle
observation, so the cell sign has zero middle-owner incidence even though
it may still carry a nonmiddle flag direction.

Initial, terminal, ejection, and incomplete-sweep states will be charged
separately rather than assumed to follow the periodic calculation.

Let \(G_0\) denote the number of owner-active cells.  Tube by tube,

\[
 G_0
 =O\!\left(t\left({M\over Q}+Q\right)\right),
 \tag{6.2b}
\]

where the \(O(Q)\) term safely includes initial, cleanup, and incomplete
sweeps.  In the calibrated central regime, \(t=O(N_H)=O(W/M)\) and
\(1\ll Q=o(M)\), so

\[
 \boxed{G_0=O(W/Q+WQ/M)=o(W).}
 \tag{6.2c}
\]

For \(Q=\Theta(\sqrt m)\), the first term dominates and
\(G_0=O(W/Q)\).

For an integer defect vector put

\[
 h(\delta)=\sum_X(\delta_X)_+={1\over2}\|\delta\|_1.
 \tag{6.3}
\]

Only owner-active cells may occur in a nonzero decomposition (3.5).  One
owner rectangle supplies two positive units, so every rooted assignment
necessarily obeys

\[
 \boxed{h(\delta)\le2G_0
 =O(W/Q+WQ/M)=o(W).}
 \tag{6.4}
\]

The moment identities (3.3) and scalar capacity (6.4) are not sufficient.
Even an unrestricted decomposition of \(\delta\) into Johnson rectangles
would not assign those rectangles to distinct legal cells of the chosen
tubes.  The rooted condition in Theorem 4.1 is therefore genuine.

This is the coefficient-scale obstruction to using the Latin switches to
*create* the global owner near-factor.  A Poisson-scale or any other
positive-density owner defect is far outside (6.4).  The unsigned whole
tubes must already form an owner near-matching with only
\(O(W/Q+WQ/M)\) correctable defect; the Latin bank can then serve as a final
absorber.

### Corollary 6.2 (no owner near-factor from the flag-cell count)

For the present one-braid transported tubes, the estimate
\(G=(1/16-o(1))W\) does not imply an owner absorber of linear capacity.
If a proposed base packing has

\[
 h(\mu_*-\mu_0)=\omega(W/Q+WQ/M),
 \tag{6.5}
\]

then no choice of the available Latin cell signs can turn it into the
target owner matching, even when the scalar and coordinate moment
identities (3.3) hold.

#### Proof

Every non-owner-active cell contributes the zero vector to the middle-owner
ledger, while every owner-active cell contributes one Johnson rectangle
and hence at most two positive units.  Distinct cells can therefore supply
at most \(2G_0\) positive units.  Equations (6.2c) and (6.4) contradict
(6.5). \(\square\)

This is an obstruction to this transported one-braid bank, not an invariant
against every conceivable multi-braid tube.  A different tube architecture
could escape only by supplying \(\Theta(M)\) owner-active cells per carrier
while retaining whole-path legality and owner separation.

## 7. The exact matching statement still required

Let \(\mathscr C\) be the set of all switchable cells in a proposed
carrier-disjoint tube skeleton, and let \(\mathscr R\) be the multiset of
oriented local rectangles in a chosen decomposition of \(\delta\).  Form
the bipartite hosting graph

\[
 \mathfrak H_{\rm host}
 \subseteq\mathscr R\times\mathscr C,
 \qquad
 \rho\sim c\Longleftrightarrow\rho\in\mathcal R(c).
 \tag{7.1}
\]

### Proposition 7.1 (exact rooted Hall criterion)

A chosen rectangle decomposition can be installed in the whole tubes if and
only if

\[
 \boxed{
 |N_{\mathfrak H_{\rm host}}(\mathscr A)|
 \ge|\mathscr A|
 \qquad(\mathscr A\subseteq\mathscr R).}
 \tag{7.2}
\]

#### Proof

This is Hall's theorem: a matching of \(\mathscr R\) into distinct cells is
exactly a rooted rectangle assignment. \(\square\)

Combining Proposition 7.1 with Theorem 4.1 gives a precise whole-tube
matching/absorption theorem.  No port compatibility remains after (7.2):
the ports were fixed before the cell signs were chosen.

### Theorem 7.2 (whole legal tube matching/absorption)

Fix a carrier-disjoint skeleton of \(t\) whole legal four-carrier tubes and
a proposed simple leave \(\mathcal L\).  Suppose:

1. \(|\mathcal L|=W-4Mt\) and
   \(d_a(\mathcal L)=W/2-\Gamma_a\) for every coordinate \(a\);
2. the owner defect \(\delta=\mathbf1_{\binom{[2m]}m\setminus\mathcal L}
   -\mu_0\) is expressed as a multiset \(\mathscr R\) of oriented legal
   cell rectangles; and
3. the hosting graph (7.1) satisfies every Hall inequality (7.2).

Then the rectangles can be assigned to distinct cells, all cell signs can
be committed simultaneously, and the resulting whole tubes are
owner-disjoint with omitted-owner family exactly \(\mathcal L\).  If in
addition \(4t=N_H-r\), \(r=o(N_H)\), and \(Q=o(M)\), literal completion has
length

\[
 \boxed{W+O(QN_H)=W+o(W).}
 \tag{7.3}
\]

#### Proof

Proposition 7.1 matches the prescribed rectangles to distinct port-stable
cells.  Theorem 4.1 commits those cells without changing a source, endpoint,
transport, or continuation, and gives the exact owner incidence
\(\mathbf1_{\binom{[2m]}m\setminus\mathcal L}\).  The scalar leave identity
and Theorem 5.1 give (7.3). \(\square\)

### Proposition 7.3 (auditable degree certificate for the host matching)

In the hosting graph (7.1), suppose there is a number \(d>0\) such that

\[
 \deg_{\mathfrak H_{\rm host}}(\rho)\ge d
 \quad(\rho\in\mathscr R),
 \qquad
 \deg_{\mathfrak H_{\rm host}}(c)\le d
 \quad(c\in\mathscr C).
 \tag{7.4}
\]

Then all Hall inequalities (7.2) hold, so Theorem 7.2 applies.

#### Proof

For \(\mathscr A\subseteq\mathscr R\), count the hosting edges leaving
\(\mathscr A\).  The left inequality in (7.4) gives at least
\(d|\mathscr A|\) edges.  Every one ends in \(N(\mathscr A)\), and the
right inequality gives at most \(d|N(\mathscr A)|\) such edges.  Hence
\(|N(\mathscr A)|\ge|\mathscr A|\). \(\square\)

This criterion is deliberately hereditary: it controls every possible
concentration of requested rectangles, not merely the total numbers
\(|\mathscr R|\) and \(|\mathscr C|\).  No such degree certificate is
currently known for the owner-active cells of a near-perfect tube
prepacking.

The unconditional global theorem would have to construct simultaneously

1. a carrier-disjoint whole-tube skeleton;
2. a leave \(\mathcal L\) satisfying the exact coordinate degrees (0.5);
3. a base owner vector \(\mu_0\) with defect satisfying (6.4); and
4. a local-rectangle decomposition satisfying the hereditary Hall cuts
   (7.2).

Call this statement the **whole-tube absorber matching theorem**
\((\mathrm{WTAM}_8)\).

The already solved carrier-quartet near-factor addresses only the tag part
of item 1: it gives \(r=o(N_H)\) compatible four-tag groups.  It does not
choose the four length-\(M\) paths in those groups with a small owner
defect.  Once the paths are chosen, their \(4M\) owner occurrences are
coupled along the entire tube.  A tag near-factor by itself places no
sublinear bound on \(h(\delta)\); if that defect is \(\Theta(W)\), Corollary
6.2 rules out repair by the present Latin bank.  Thus the needed global
packing theorem is genuinely an owner-path theorem, not another carrier
quarteting theorem.

## 8. Relation to the cyclic-interval near-design theorem

The two-ledger cyclic-interval theorem says that an already constructed
matching of legal geodesic chunks, missing \(r=o(T/Q)\) tags and with
\(o(W)\) exceptional incidence, has only \(o(W)\) protected holes.  It does
not construct the matching.

Likewise, Theorem 5.1 shows that \((\mathrm{WTAM}_8)\) would turn a whole
Latin tube family into the required coefficient-one owner near-factor, with
the exact omitted ledger (0.2)--(0.5).  But the two-ledger theorem supplies
none of items 1--4 above.  In particular:

* a scalar statement \(|\mathcal L|=o(W)\) does not imply the coordinate
  degrees (0.5);
* an unrooted rectangle-lattice decomposition does not imply the Hall cuts
  (7.2); and
* the time-zero cyclic-interval pair-square estimates are not a hereditary
  matching theorem for whole tubes.

Thus the global owner near-factor has not been proved merely by combining
the local transport with the cyclic-interval near-design ledger.  The
strictly smaller exact remaining lemma is \((\mathrm{WTAM}_8)\), with its
coordinate leave and rooted Hall conditions exposed.

## 9. Audited conclusion

The global bookkeeping is closed:

1. whole tubes, not isolated cells, are the matched objects;
2. the exact scalar leave is \(W-M(N_H-r)\);
3. the exact coordinate leave is \(W/2-\Gamma_a\);
4. a rooted rectangle matching commits the signs without changing ports;
5. initialization and literal completion then cost only \(o(W)\).

The remaining obstacle is not local chronology, carrier compatibility, or
an omitted constant in the word length.  It is the hereditary host Hall
theorem \((\mathrm{WTAM}_8)\).  Claiming an unconditional owner near-factor
without proving (7.2) would repeat the same logical error as deriving the
protected-strip integral matching from fractional vertex loads alone.
