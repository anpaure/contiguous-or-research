# Residence-seam batching by run-occurrence splitting, and the exact integrated no-go boundary

Date: 2026-07-28

Status: pure mathematics. This note proves an exact literal batching
compiler and an exact obstruction to the opposite lower-bound strategy. It
does not prove the PBBS split-complexity estimate isolated below and does not
claim coefficient one.

## 0. Outcome

Let \(F\) be a disjoint union of directed rank-\(k\) Johnson cycles, with
\(W\) owner starts and at most \(B\) cycles. Let \(H\ge1\). For a finite
owner trajectory \(Q\), atomize maximal positive **run occurrences**, not
coordinate names. Write \(\kappa_H(Q)\) for the minimum label-preserving
column-splitting excess which makes all nonempty depth-at-most-\(H\) lower
and upper run-incidence rows consecutive-ones.

If the owner starts are partitioned into \(R\) arcs and \(Q_j\) is the
forward \(H\)-halo of the \(j\)-th arc, then there is an integral nonzero
literal word of length

\[
 \boxed{
 L_H\le W+HR+\sum_{j=1}^{R}
       \bigl(w(Q_j)+\kappa_H(Q_j)\bigr),}
 \tag{0.1}
\]

where

\[
 w(Q)=\left|X_0\setminus\bigcap_{X\in Q}X\right|.
\]

Repeated occurrences of the same coordinate produce repeated singleton
letters and are harmless by idempotence of OR.

Let \(J\) be a residence transversal and group its cuts \(b\) at a time on
each owner cycle. One can choose the start partition with

\[
 R\le B+\frac{J}{b}
 \le B+\frac{\nu_H(F)+B}{b}.                         \tag{0.2}
\]

Consequently the one genuinely new PBBS estimate

\[
 \boxed{
 \sum_j\bigl(w(Q_j)+\kappa_H(Q_j)\bigr)\le C_AHR}
 \tag{SB_{H,b}}
\]

implies

\[
 \boxed{
 L_H\le W+O_A\!\left(HB+\frac{H\nu_H(F)}b\right).}
 \tag{0.3}
\]

Thus \(b=\lceil\sqrt H\rceil\) gives

\[
 L_H\le W+O_A(HB+\sqrt H\,\nu_H),                  \tag{0.4}
\]

and, for fixed \(c>0\) and \(H\ge2\),
\(b=\lceil H/(\log H)^c\rceil\) gives

\[
 L_H\le W+O_{A,c}(HB+\nu_H(\log H)^c).             \tag{0.5}
\]

Either estimate is \(W+o(W)\) at Gaussian height
\(H=\Theta_A(\sqrt m)\) under the already known critical bound
\(\nu_H=O_A(BH)\), since \(W=(2m+1)B=\Theta_A(BH^2)\).

The estimate \((\mathrm{SB}_{H,b})\) is not proved here. It is a
simultaneous lower/upper support condition in one literal word, rather than
a rankwise or marginal condition. It does not assert aligned flag endpoints.

The negative side is sharp. Standalone seam banks whose witnesses are
confined to the bank can require \(J(H-1)\) letters, but there are exact
rank-\((m+1)\) Johnson cycles with
\(J\) separated short residences whose complete integrated lower/upper
compiler has only \(2H\) excess letters. The example has a literal
odd-graph lift. Therefore an integrated \(\Omega(H)\)-per-seam lower bound
cannot follow from residence intervals, endpoint order, nested flag chains,
or odd-graph legality alone. A PBBS negative theorem would have to use
PBBS-specific set-letter content.

## 1. Run occurrences and their exact census

Let

\[
 Q=(X_0,X_1,\ldots,X_S),\qquad X_t\in\binom{\Omega}{k},
\]

be a directed Johnson trajectory. Put

\[
 K=\bigcap_{t=0}^{S}X_t,
 \qquad w=|X_0\setminus K|.
 \tag{1.1}
\]

For every coordinate, split its indicator word on \([0,S]\) into maximal
positive intervals. Omit the full intervals \([0,S]\), whose labels form
\(K\). The remaining objects

\[
 \rho=(x_\rho,[\ell_\rho,r_\rho])
\]

are the noncore run occurrences. Different occurrences may have the same
coordinate label.

### Lemma 1.1 (exact occurrence count)

The number \(N(Q)\) of noncore run occurrences is

\[
 \boxed{N(Q)=S+w.}                                  \tag{1.2}
\]

#### Proof

Exactly \(w\) noncore runs are already active at owner \(0\). Every one of
the \(S\) Johnson transitions inserts one coordinate absent immediately
before that transition, and hence starts exactly one new maximal positive
run. Conversely, every noncore run starts either at owner \(0\) or at one
of these insertions. Re-entry of an old coordinate creates another run and
is already charged to its insertion. This proves (1.2). \(\square\)

For an owner window \(I=[a,b]\subseteq[0,S]\), define two occurrence rows

\[
 C_I=\{\rho:I\subseteq[\ell_\rho,r_\rho]\},
 \qquad
 M_I=\{\rho:I\cap[\ell_\rho,r_\rho]\ne\varnothing\}.
 \tag{1.3}
\]

Coordinatewise,

\[
 \boxed{
 \begin{aligned}
 \bigcap_{t=a}^{b}X_t
   &=K\cup\{x_\rho:\rho\in C_I\},\\
 \bigcup_{t=a}^{b}X_t
   &=K\cup\{x_\rho:\rho\in M_I\}.
 \end{aligned}}
 \tag{1.4}
\]

The braces on the right denote sets of coordinate labels, so repeated run
labels collapse automatically.

## 2. The exact split-consecutive-ones compiler

Fix a requested collection \(\mathcal I\) of owner windows, for example all
windows of at most \(H+1\) owners contained in \(Q\). Empty target sets are
discarded, since a nonzero literal word is required to represent only
nonempty Boolean targets. Form the binary matrix whose rows are the
remaining \(C_I,M_I\), \(I\in\mathcal I\), and whose columns are the run
occurrences.

A **label-preserving split** replaces an occurrence column \(\rho\) by
\(c_\rho\ge1\) copies, all carrying label \(x_\rho\). A row originally
containing \(\rho\) is assigned a nonempty subset of its copies; a row not
containing \(\rho\) is assigned none. The split is consecutive-ones if
the copies admit one common linear order in which every assigned row is an
interval. Define

\[
 \kappa_{\mathcal I}(Q)=
 \min\sum_\rho(c_\rho-1),                           \tag{2.1}
\]

and write \(\kappa_H(Q)\) for the full depth-\(H\) window family.

### Theorem 2.1 (literal split compiler)

For every \(Q\) and every requested window family \(\mathcal I\), there is
a literal word representing all nonempty lower and upper targets in (1.4), of
length at most

\[
 \boxed{S+w+\kappa_{\mathcal I}(Q)+1.}              \tag{2.2}
\]

Every emitted letter is nonempty. If \(K=\varnothing\), the final \(K\)
letter is omitted.

#### Proof

Choose an optimal split and its consecutive-ones order. For every split
copy of \(\rho\), emit

\[
 K\cup\{x_\rho\}.
\]

For a row \(C_I\) or \(M_I\), take its assigned consecutive interval. It
contains at least one copy of every incident original occurrence, no copy
of a nonincident occurrence, and hence its OR is exactly the corresponding
set in (1.4). Repeated coordinate labels do not change an OR. If an empty
row has nonempty target \(K\), append the one letter \(K\). All split-copy
letters are nonempty even when \(K=\varnothing\). Lemma 1.1 gives (2.2).
\(\square\)

The unsplit case is the run-occurrence compiler. Ordering occurrences by
nondecreasing start, it is enough that every exit superlevel set

\[
 \{\rho:r_\rho\ge t\}
\]

be an interval: each row in (1.3) is then a prefix intersected with one of
these intervals.

### Proposition 2.2 (the unsplit interface is exactly FIFO)

Assume \(H\ge1\), and include the owner rows and adjacent upper rows in the
matrix. If \(\kappa_H(Q)=0\), then, in the common occurrence order, the
noncore owner supports are fixed-length intervals which all shift in one
direction by one position at every Johnson transition. Conversely such a
FIFO sliding-window trajectory has \(\kappa_H(Q)=0\).

#### Proof

Every owner contains exactly

\[
 d=k-|K|
\]

active run occurrences. Consecutive owner supports share \(d-1\) atoms.
For \(d\ge2\), two distinct length-\(d\) intervals sharing \(d-1\) positions
differ by a unit left or right shift. If two successive shifts have
opposite signs, the position just vacated is immediately reactivated, so
its run column has pattern \(101\), contradicting maximality of that run.
Thus all shifts have one sign. When \(d=1\), the adjacent upper row forces
the two singleton supports to be adjacent, after which the same reversal
argument applies.

Conversely, intersections and unions of any consecutive family of
monotonically sliding equal-length intervals are intervals. Hence all
rows in (1.3) are consecutive-ones. \(\square\)

Thus ordinary unsplit batching is highly rigid. Column splitting, or
genuinely bundled set letters beyond this interface, is indispensable for
non-FIFO PBBS sectors.

### Proposition 2.3 (exact restricted star cost)

For \(d\ge1\), consider the run-atom rows

\[
 \{z,a_1\},\ldots,\{z,a_d\},                       \tag{2.3}
\]

with one center occurrence and \(d\) distinct leaf occurrences, the exact
center-column split excess is

\[
 \boxed{\left\lceil\frac d2\right\rceil-1.}         \tag{2.4}
\]

#### Proof

One center copy has only two sides and can be adjacent, after deleting
neutral core-only cells, to at most two leaf columns. Hence at least
\(\lceil d/2\rceil\) center copies are necessary. They suffice by arranging

\[
 a_1,z_1,a_2,\quad a_3,z_2,a_4,\quad\ldots
\]

and using the evident two-letter interval for each leaf row. \(\square\)

This is a lower bound only for the singleton run-copy interface. In an
unrestricted literal word, the bundled letters \(K\cup\{z,a_i\}\) realize
all rows (2.3) separately, so the star is not an interval-Boolean-rank lower
bound.

## 3. Global halo composition and the requested rates

Partition the owner-start positions on every cycle into \(R\) consecutive
nonempty base arcs. If base arc \(j\) contains \(s_j\) starts, extend it
forward by \(H\) owner transitions and call the resulting finite trajectory
\(Q_j\). Repetition across a cyclic root is allowed. Then \(Q_j\) has

\[
 S_j=s_j+H-1
\]

transitions, and every owner window of at most \(H+1\) owners is contained
in the unique halo whose base arc contains its start.

### Theorem 3.1 (exact global split ledger)

There is a nonzero literal word representing every requested nonempty lower
and upper window value through depth \(H\), of length

\[
 \boxed{
 L_H\le W+HR+\sum_{j=1}^{R}
       \bigl(w(Q_j)+\kappa_H(Q_j)\bigr).}            \tag{3.1}
\]

#### Proof

Apply Theorem 2.1 to each halo and concatenate the resulting words. Since
\(\sum_js_j=W\),

\[
 \sum_j(S_j+1)=
 \sum_j(s_j+H)=W+HR.
\]

Assign each original owner window to the halo containing its start. Its set
value is unchanged, so every pre-existing nonempty PBBS all-depth target
value remains represented. \(\square\)

The conclusion is support-level literalization in one common word. The
row-dependent split assignments need not give different depths of one
owner-start flag nested representing intervals with common endpoints.
Therefore Theorem 3.1 does not by itself supply a labelled owner/Hall
extension or any downstream interface requiring one aligned physical flag
tower. It supplies exactly what unlabelled contiguous-OR coverage uses:
every unchanged lower and upper set value has a literal interval witness.

Now let \(\mathcal C\) be a transversal of all positive residence intervals
of length at most \(H\). On a cycle with \(J_C\) selected cuts, group
successive cuts \(b\) at a time and use the induced consecutive start arcs;
use one arc on a cycle with no cut. Then

\[
 R\le B+\frac{J}{b},\qquad J=\sum_CJ_C.             \tag{3.2}
\]

The circular interval packing-transversal theorem permits

\[
 J\le\nu_H(F)+B.                                   \tag{3.3}
\]

Equations (3.1)--(3.3) prove (0.3) under
\((\mathrm{SB}_{H,b})\), and hence the rates (0.4)--(0.5).

Notice what has and has not been proved. Grouping the cuts gives (3.2)
unconditionally. It does not control the persistent width \(w(Q_j)\) or
the split cost \(\kappa_H(Q_j)\). Their aggregate estimate is precisely the
new PBBS support-compiler theorem required by this architecture.

Nor is \(w\) controlled by residence alone.  On the cyclic trajectory of
all length-\((m+1)\) intervals in one cyclic order on \(2m+1\) coordinates,
every positive coordinate run has \(m+1>H\) owners, so \(\nu_H=0\).
Nevertheless, a linear halo containing the whole cycle has empty persistent
core and \(w=m+1\).  The ordinary cyclic erosion compiler handles this
trajectory in \(2m+1+2H\) letters, much more efficiently than singleton
run atomization.  Thus \((\mathrm{SB}_{H,b})\) is a sufficient
baseline-replacement interface, not a consequence or reformulation of the
residence bound.  A complete PBBS proof may have to use erosion on good
interiors and the split compiler only on a globally recycled seam sector.

## 4. Why additive collar clustering cannot give the gain

The established multi-cut dominance chart charges a cluster of cut span
\(S\) by \(7H+3S-3\) after the corresponding lower, upper, and erosion
pieces are included. The proved PBBS clustered-span equivalence states,
modulo the audited low-height tail, that the minimum total cost of all such
clusters is \(o(W)\) exactly when the old \(H\nu_H\) term is already
subcritical.

Therefore (0.3) is not an improvement of an append-only chart. Its only
possible gain is the replacement of already mandatory baseline positions
by a single common split-consecutive-ones chronology.

## 5. Standalone banks need \(H\) per seam, integrated words do not

The following family gives both halves of the sharp distinction. Let

\[
 2\le H\le m,\qquad J\ge1,\qquad M=2JH\le m+H.
\]

Choose a set \(G\) of size \(m+1-H\) and distinct coordinates
\(a_0,\ldots,a_{M-1}\), with cyclic indices. Define

\[
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\}.
 \tag{5.1}
\]

This is a rank-\((m+1)\) Johnson cycle.

### Proposition 5.1 (standalone seam lower bound)

There are \(J\) pairwise separated cut collars for which the depth-\(H-1\)
crossing families contain \(J(H-1)\) distinct targets of the common rank
\(m+2-H\). Every standalone word, or auxiliary bank in which all of those
target witnesses are required to lie wholly inside the bank, has at least
\(J(H-1)\) positions.

#### Proof

For \(q=H-1\),

\[
 \bigcap_{h=0}^{H-1}X_{i+h}=G\cup\{a_{i+H-1}\}.     \tag{5.2}
\]

Choose cuts spaced \(2H\) transitions apart. The \(H-1\) starts whose
depth-\(H-1\) windows cross one cut are disjoint from the corresponding
start families at the other cuts, so (5.2) gives \(J(H-1)\) distinct
same-rank sets.

Distinct same-rank interval ORs have distinct left endpoints: two intervals
with one left endpoint are nested, and their ORs are comparable, whereas
distinct sets of one cardinality are incomparable. A standalone bank
therefore needs at least one position per target. \(\square\)

### Theorem 5.2 (integrated \(2H\)-excess compiler)

Put \(E_i=G\cup\{a_i\}\). The word

\[
 E_0,E_1,\ldots,E_{M-1},
 E_0,E_1,\ldots,E_{2H-2},G                         \tag{5.3}
\]

has exact length \(M+2H\) and represents every lower intersection and
upper union of at most \(H+1\) consecutive owners in (5.1).

#### Proof

For \(0\le q<H\),

\[
 \bigcap_{h=0}^{q}X_{i+h}
 =G\cup\{a_{i+q},\ldots,a_{i+H-1}\}
 =\bigcup_{t=i+q}^{i+H-1}E_t.                       \tag{5.4}
\]

At \(q=H\) the intersection is \(G\). For \(0\le q\le H\),

\[
 \bigcup_{h=0}^{q}X_{i+h}
 =G\cup\{a_i,\ldots,a_{i+H+q-1}\}
 =\bigcup_{t=i}^{i+H+q-1}E_t.                       \tag{5.5}
\]

Every displayed cyclic interval has at most \(2H\) letters, so repeating
the first \(2H-1\) \(E\)-letters linearizes it. The last letter represents
the depth-\(H\) core. \(\square\)

Every active coordinate has a positive run of exactly \(H\) owners. The
\(J\) runs beginning at owner positions \(2tH\) have residence edge collars

\[
 [\,2tH-1,(2t+1)H-1\,],\qquad0\le t<J,
\]

which form the separated family used above. In particular \(\nu_H\ge J\),
while the integrated excess in (5.3) is \(2H=o(HJ)\) for \(J\to\infty\).

The example is also literally odd-graph legal. On a ground set of size
\(2m+1\), put

\[
 A_i=\Omega\setminus X_i,\qquad B_i=X_i\cap X_{i+1}.
\]

Then \(A_i,B_i,A_{i+1}\) are rank-\(m\) sets and consecutive pairs are
disjoint, so

\[
 A_0,B_0,A_1,B_1,\ldots
\]

is a literal odd-graph cycle.

Proposition 5.1 and Theorem 5.2 prove that \(\Omega(H)\) per seam is sharp
for a witness-confined standalone bank and false for integrated baseline recycling, even
with exact ranks, complete nested lower/upper chains, separated short
residences, and an odd-graph lift.

## 6. Endpoint geometry and the exact unrestricted parameter

Pure endpoint geometry cannot restore a per-seam lower bound. On a linear
path of \(M\) owner starts, the interval frame

\[
 I_i=[i,i+H]\subseteq[0,M+H-1]                     \tag{6.1}
\]

has

\[
 \bigcap_{h=0}^{q}I_{i+h}=[i+q,i+H],\qquad
 \operatorname{hull}_{h=0}^{q}I_{i+h}=[i,i+H+q].   \tag{6.2}
\]

Thus \(M+H\) abstract positions realize the complete native two-endpoint
and nesting pattern, independently of how many seam collars are declared.
Any stronger lower bound must inspect the content of the intervening set
letters.

For completeness, let \(A\) be the target-by-coordinate incidence matrix
of a desired family. A literal word of \(L\) nonempty cells is exactly a
Boolean factorization

\[
 A=R\odot C,                                       \tag{6.3}
\]

where every row of \(R\) is the indicator of a nonempty integer interval in
\([L]\), and every row \(j\) of \(C\) is a nonzero set-letter. Conversely
every such factorization of nonempty target rows is a literal word. The
minimum \(L\) is the interval Boolean rank \(\operatorname{ibr}(A)\).

The split parameter \(\kappa_H\) fixes \(C\) to singleton-labelled run
copies and is therefore only a constructive upper interface. An
integrated PBBS no-go would require a genuinely unrestricted estimate such
as

\[
 \operatorname{ibr}(A_{\mathrm{PBBS},H})
 \ge W+cH\nu_H,                                    \tag{6.4}
\]

or an equivalent PBBS-specific no-bundling theorem. The sliding family of
Section 5 proves that (6.4) cannot hold for general Johnson or odd-graph
chronologies.

## 7. Exact proved and conditional boundary

Proved:

1. The run-occurrence census is \(S+w\), even with arbitrary coordinate
   re-entry.
2. Label-preserving split C1P gives the exact literal compiler (2.2).
3. The global ledger is (3.1), and the requested square-root/polylog rates
   follow quantitatively from \((\mathrm{SB}_{H,b})\).
4. The unsplit interface is exactly a FIFO sliding-window chronology.
5. Additive collar clustering cannot improve the old \(H\nu_H\) scale.
6. A witness-confined standalone bank may need \(J(H-1)\) cells, but an integrated literal
   odd-graph-legal compiler can use only \(2H\) excess cells for the same
   separated-residence scale.
7. Endpoint and nested-chain geometry alone cannot prove an integrated
   per-seam toll.

Unproved, and now isolated sharply:

\[
 \sum_j(w(Q_j)+\kappa_H(Q_j))=O_A(HR)
\]

for a \(b\)-cut batching of the canonical PBBS factor, after any permitted
negligible exceptional family. A still stronger positive proof may replace
singleton run copies by bundled letters and bound interval Boolean rank
directly. A negative proof must be PBBS-specific and unrestricted; Tucker
stars in the singleton interface are not enough.
