# Lane U: the column-correlated nibble — exact second-order tail and sequential obstruction

Date: 2026-07-25

## Status

The proposed two-stage proof has one correct analytic input and one exact
integral input, but the advertised inference does not follow from them.

1. After removing every interval pair with
   \(a+c=1\), the intrinsic normalized overlap row sum is
   \(O(m^{-2})\).  This is proved below with a uniform constant.
2. The complete floor-proportional rank profile has an exact integral
   balanced-chain flow.  It leaves precisely
   \(R_q=N_q-pb_q<p\) targets in rank \(m+q\).
3. A one-successor chain flow cannot remove every \(a+c=1\) pair.  The
   two central ranks contain a connected alternating Pascal ladder.  Any
   chain flow internalizes at most a matching from that ladder.  In the
   unrestricted labelled atom hypergraph, the noninternalized pairs retain
   raw normalized codegree \(\Omega(m^{-1})\), with the exact bound in
   Theorem 3.2 below.
4. Contracting all cover edges instead contracts one whole physical atom.
   If a disjoint chain pool is selected first, there is no residual
   \(m^{-2}\) matching problem: the missing theorem becomes a packing of
   long FIFO-compatible paths inside the conditioned chain pool.
5. At the level of fully specified column supervertices, equal-radius
   adjacency does have exact conditional probability \((m-d)^{-2}\).
   One undesignated spacer between consecutive radius blocks removes every
   unequal-radius cover seam at total literal cost \(pH=o(W)\).  This
   splits the cover graph into equal-radius ladder macro-packets and repairs
   the local seam geometry, but not the flow-to-FIFO lift.

Thus this report closes the specific shortcut

\[
 \text{one-successor chain contraction}
 \quad\Longrightarrow\quad
 \text{all remaining target overlap is }O(m^{-2}).
\]

It does **not** disprove the proportional tight-atom matching lemma, nor a
flow-dependent two-stage construction which proves new conditioned-degree
estimates after selecting a global column dictionary.  A simultaneous or
row-aware two-parent Pascal-flow/FIFO theorem remains open.

## 0. Exact parameters

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 b=\lfloor m^{3/4}\rfloor,
\]

\[
 H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,
 \qquad \frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},
\]

and, for \(-H\le q\le H+1\), put

\[
 N_q=\binom{n}{m+q},\qquad
 p=\left\lfloor\frac Wb\right\rfloor,
 \qquad b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\tag{0.1}
\]

For all sufficiently large \(m\),

\[
 b_0=b_1=b,
 \qquad
 0\le R_q:=N_q-pb_q<p.
\tag{0.2}
\]

Define

\[
 a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
 \qquad a_H=b_{-H}.
\tag{0.3}
\]

With

\[
 \rho(q)=\max\{-q,q-1\},
\]

binomial symmetry and telescoping give the exact identity

\[
 \boxed{b_q=\sum_{d=\rho(q)}^H a_d.}
\tag{0.4}
\]

Choose a partition

\[
 [0,b-1]=J_0\sqcup\cdots\sqcup J_H,
 \qquad |J_d|=a_d,
\tag{0.5}
\]

and designate start \(i\in J_d\) in precisely the ranks

\[
 -d,-d+1,\ldots,d+1.
\tag{0.6}
\]

For an injective coordinate word \(x\), the corresponding target is

\[
 A_{i,q}(x)=\{x_i,x_{i+1},\ldots,x_{i+m+q-1}\}.
\tag{0.7}
\]

The arguments below need only

\[
 b+2H=o(m),\qquad b_0=b_1=b,
\tag{0.8}
\]

so the central-ladder obstruction applies beyond the displayed Gaussian
choice whenever (0.8) holds.

## 1. Exact sharpening of the local overlap sum

Let \(P,Q\) be two designated position intervals.  Put

\[
 r=|P|,\qquad
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\tag{1.1}
\]

Condition on the unordered coordinate set in \(P\) being a prescribed
\(r\)-set \(X\).  A prescribed set \(Y\) can occupy \(Q\) only if its
intersection with \(X\) has the position-forced size, and in that case the
exact conditional probability is

\[
 \boxed{
 \theta_r(a,c)=
 \frac1{\binom r a\binom{n-r}c}.}
\tag{1.2}
\]

For a fixed \((a,c)\), at most \(a+c+1\) designated position intervals
have that type relative to \(P\).  The same factor bounds, inside a fixed
test atom, the number of actual target vertices having type \((a,c)\)
relative to a fixed target.  Therefore the intrinsic normalized row sum is
majorized by

\[
 \sum_{a+c\ge1}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c}.
\tag{1.3}
\]

The square is essential: one factor counts possible vertices in the test
atom and the other counts possible slots in a random labelled atom.

### Theorem 1.1 (uniform second-order tail)

There is an absolute \(m_0\) such that, for every \(m\ge m_0\), every
labelled proportional atom \(e\), and every \(v\in e\),

\[
 \boxed{
 \sum_{\substack{w\in e\setminus\{v\}\\
 |v\setminus w|+|w\setminus v|\ge2}}
 \frac{\deg(v,w)}{\deg(v)}
 \le \frac{210}{(m-H)^2}.}
\tag{1.4}
\]

Consequently the complete contribution of all \(a+c\ge2\) types is
\(O(m^{-2})\), uniformly through the Gaussian band.

#### Proof

Put \(M=m-H\) and \(J=b+2H+1\).  Every relevant \(r,n-r\) is at least
\(M\), every relevant \(a,c\) is at most \(J\), and \(J=o(M)\).  For all
sufficiently large \(m\), the successive-term ratio in

\[
 u_j=\frac{(j+1)^2}{\binom Mj}
\]

is at most \(1/2\) for \(1\le j<J\).  Hence

\[
 \sum_{j=1}^J\frac{(j+1)^2}{\binom Mj}
 \le \frac8M,
\tag{1.5}
\]

and

\[
 \sum_{j=2}^J\frac{(j+1)^2}{\binom Mj}
 \le \frac{36}{M(M-1)}
 \le \frac{72}{M^2}.
\tag{1.6}
\]

Split (1.3), subject to \(a+c\ge2\), into the two axes and the proper
overlap region.  The axes contribute at most

\[
 \frac{72}{M^2}+\frac{72}{M^2}.
\tag{1.7}
\]

For \(a,c\ge1\),

\[
 (a+c+1)^2\le(a+1)^2(c+1)^2,
\]

so (1.5) bounds the proper-overlap contribution by

\[
 \frac8M\frac8M=\frac{64}{M^2}.
\tag{1.8}
\]

The total is at most \(208/M^2\), and (1.4) follows from the safe integer
constant \(210\).  The conditional-to-intrinsic passage is exactly the
two-multiplicity argument preceding the theorem. \(\square\)

### Corollary 1.2 (the first-order source is exactly the cover relation)

The only types omitted from Theorem 1.1 are

\[
 (a,c)=(1,0),\qquad (a,c)=(0,1).
\tag{1.9}
\]

They are precisely pairs of interval slots whose target sets differ by one
Boolean cover.  Their contribution to the majorant (1.3) is

\[
 \frac4r+\frac4{n-r}=O(m^{-1}).
\tag{1.10}
\]

Thus every first-order term is a vertical or diagonal cover incidence;
all non-cover terms are second order.

## 2. Stage one succeeds as an abstract integral balanced flow

The floor profile itself has no Hall obstruction.

### Theorem 2.1 (exact proportional chain flow)

There is an integral collection of pairwise vertex-disjoint saturated
Boolean chain segments with exactly \(p a_d\) segments of radius \(d\),
for every \(0\le d\le H\).  It occupies exactly \(p b_q\) targets of
rank \(m+q\) and leaves exactly \(R_q=N_q-pb_q<p\) targets there.

Equivalently, the complete upper and lower rank flow is integral and has
the exact birth/death profile (0.3), with no bundle loss.

#### Proof

Fix a symmetric-chain decomposition \(\mathscr D\) of \(B_n\).  Let
\(\mathscr D_{\ge d}\) be the chains meeting rank \(m-d\).  These families
are nested and

\[
 |\mathscr D_{\ge d}|=N_{-d}.
\tag{2.1}
\]

Choose nested subfamilies

\[
 K_H\subseteq K_{H-1}\subseteq\cdots\subseteq K_0,
 \qquad K_d\subseteq\mathscr D_{\ge d},
\]

with

\[
 |K_d|=p b_{-d}.
\tag{2.2}
\]

Choose \(K_H\) arbitrarily and extend \(K_{d+1}\) inside
\(\mathscr D_{\ge d}\).  This is possible because

\[
 p b_{-(d+1)}\le p b_{-d}\le N_{-d}.
\]

Assign radius \(d<H\) to chains in \(K_d\setminus K_{d+1}\), radius
\(H\) to chains in \(K_H\), and retain the corresponding symmetric
segments.  Their radius counts are exactly \(p a_d\).  At rank \(m+q\),
the number present is, by (0.4),

\[
 p\sum_{d\ge\rho(q)}a_d=p b_q.
\]

The SCD makes all retained targets distinct.  The leave is (0.2).
\(\square\)

The theorem may group the \(p a_d\) chains of each radius into \(p\)
abstract bundles of histogram \((a_0,\ldots,a_H)\).  It does not impose a
common coordinate word, FIFO departure/arrival order, or the tight-window
identities (0.7).  That distinction is decisive below.

## 3. The central Pascal ladder survives every one-chain flow

At the two central ranks every start is designated.  Write

\[
 P_i=[i,i+m-1],\qquad U_i=[i,i+m],
 \qquad 0\le i<b.
\tag{3.1}
\]

The cover incidences are

\[
 P_i\subset U_i\quad(0\le i<b),
\tag{3.2}
\]

and

\[
 P_{i+1}\subset U_i\quad(0\le i<b-1).
\tag{3.3}
\]

Thus the central cover-slot graph is the alternating path

\[
 P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1}.
\tag{3.4}
\]

The edges (3.2) are the same-start vertical-chain edges.  The equally
first-order edges (3.3) join adjacent nominal columns.

### Proposition 3.1 (exact central cover codegree)

For every \(m\)-set \(A\) and every \((m+1)\)-set \(B\supset A\), in the
labelled proportional-atom multihypergraph,

\[
 \boxed{
 \frac{\deg(A,B)}{\deg(A)}
 =\frac{\deg(A,B)}{\deg(B)}
 =\frac{2b-1}{b(m+1)}.}
\tag{3.5}
\]

The same-start slot representations contribute exactly

\[
 \frac1{m+1},
\tag{3.6}
\]

and the adjacent-start representations contribute exactly

\[
 \boxed{
 \frac{b-1}{b(m+1)}.}
\tag{3.7}
\]

#### Proof

An occurrence of \(A\) in a specified \(P_i\) has the same number of word
completions for every \(i\), and the \(b\) events are disjoint.  Conditioned
on that occurrence, a prescribed one-element extension \(B\) occupies
either available containing interval with exact probability \(1/(m+1)\).
There are \(b\) pairs of type (3.2) and \(b-1\) pairs of type (3.3).
Dividing their total by the \(b\) possible slots of \(A\) proves (3.5).
Separating the two types proves (3.6)--(3.7).  The calculation from the
\(B\)-side is identical because \(N_0=N_1=W\). \(\square\)

In the unrestricted labelled-atom accounting, deleting the tagged
same-start representations while retaining the adjacent-start
representations leaves the exact raw contribution (3.7), which is
\((1+o(1))/m\).  This sentence is representation bookkeeping, not a claim
about degrees in a subsequently conditioned chain-owned hypergraph.

### Theorem 3.2 (raw uninternalized cover mass)

Let \(M\) be any matching in the inclusion graph between ranks \(m\) and
\(m+1\).  For every proportional atom \(e\), at least \(b-1\) of the
\(2b-1\) cover incidences in (3.2)--(3.3) are outside \(M\).  Moreover,

\[
 \boxed{
 \frac1b\sum_{A\in e\cap\binom{[n]}m}
 \ \sum_{\substack{B\in e\cap\binom{[n]}{m+1}\\
 A\subset B,\ (A,B)\notin M}}
 \frac{\deg(A,B)}{\deg(A)}
 \ge
 \left(1-\frac1b\right)
 \frac{2b-1}{b(m+1)}.}
\tag{3.8}
\]

Consequently, if the non-\(M\) target pairs are retained with their
**unrestricted** labelled-atom codegrees, some central target in every atom
has raw uninternalized cover row sum \(\Omega(m^{-1})\).

#### Proof

The path (3.4) has \(2b-1\) edges and a matching contains at most \(b\)
of them.  Every uncontracted target pair has the exact normalized codegree
(3.5).  Sum the at least \(b-1\) contributions and divide by the \(b\)
lower central targets. \(\square\)

Every unit-capacity saturated-chain flow, including Theorem 2.1, restricts
at the central transition to such a matching.  Hence merely deleting the
flow-matched pairs from the unrestricted overlap table cannot produce the
hypothesis of the \(O(m^{-2})\) nibble.

This is not a lower bound on codegrees after conditioning the candidate
atom family to be owned by a chosen flow or SCD.  Such conditioning changes
both degrees and codegrees and can make a particular unpaired continuation
impossible.  A valid flow-dependent second stage must prove its conditioned
regularity and expansion anew.

## 4. Contracting all cover edges contracts the whole atom

### Proposition 4.1 (cover-slot connectedness)

The graph on all designated slots of one proportional atom, with an edge
between every pair having \(a+c=1\), is connected.

#### Proof

The central slots form the connected path (3.4).  A start \(i\in J_d\)
is present at every rank \(-d,-d+1,\ldots,d+1\).  Its successive
same-start slots differ by one endpoint coordinate, so its entire vertical
chain attaches to \(P_i\) and \(U_i\).  Every designated slot is on one
of these chains. \(\square\)

Therefore any equivalence contraction which internalizes **every**
\(a+c=1\) slot pair has one equivalence class on the whole atom.  There is
no quotient into \(b\) independent columns with only second-order edges
between the quotient vertices.

For literal pair deletion in the unrestricted atom family this gives the
exact dichotomy:

* contract one successor per target: Theorem 3.2 leaves
  \(\Theta(m^{-1})\) raw cover mass outside the contracted matching;
* contract every cover relation: Proposition 4.1 contracts the complete
  physical row and assumes the desired bundling object.

A third, still-open possibility is to condition on a globally selected
chain dictionary and prove a row-aware compatibility theorem in that
conditioned system.  Section 6 states the resulting gate.

## 5. Conditioning audit: why the unrestricted tail cannot simply be reused

The danger in transferring the unrestricted estimate can also be seen as
loss of one denominator after a vertical cover has been fixed.

Let a uniformly random permutation complete the injective word, and put

\[
 C_q=A_{i,q}=\{x_i,\ldots,x_{i+m+q-1}\},
 \qquad -d\le q\le d+1.
\tag{5.1}
\]

Condition on the complete radius-\(d\) source column

\[
 \mathcal C_i^{(d)}=(C_{-d},C_{-d+1},\ldots,C_{d+1}).
\]

Put

\[
 B=C_{-d},\qquad T=C_{d+1},\qquad M=m-d.
\tag{5.2}
\]

The conditioning reveals \(B\) as an unordered \(M\)-set and reveals
every right-tail increment \(C_{q+1}\setminus C_q\).  It does not reveal
the internal order of \(B\).  Consequently

\[
 z=x_i
\]

is exactly uniform on \(B\).

### Proposition 5.1 (conditional denominator cancellation)

Every compatible specified adjacent middle set has conditional probability

\[
 \boxed{
 \Pr\bigl(A_{i+1,0}=Y\mid\mathcal C_i^{(d)}\bigr)
 =\frac1{m-d}.}
\tag{5.3}
\]

More generally, the rank-shifted adjacent chain

\[
 A_{i+1,q}=C_{q+1}\setminus\{z\},
 \qquad -d-1\le q\le d,
\tag{5.4}
\]

is determined by the single choice of \(z\).  Every compatible specified
subchain of (5.4) which distinguishes \(z\) has probability \(1/(m-d)\).

#### Proof

In particular,

\[
 A_{i+1,0}=C_1\setminus\{z\}.
\]

Different \(z\in B\) give different middle sets.  Uniformity of the
internal order of \(B\) proves (5.3), and the same identity gives (5.4).
\(\square\)

Unconditionally, specifying a same-rank Johnson neighbor requires an
entrant and a departure and has probability

\[
 \frac1{r(n-r)}=\Theta(m^{-2}).
\tag{5.5}
\]

After the cover \(P\subset P\cup\{y\}\) is routed, the entrant \(y\) is
known.  Only the departure remains, giving (5.3).  This is the exact
conditioning step missing from the sequential inference.

For an integer \(t\ge0\), write

\[
 (M)_t=M(M-1)\cdots(M-t+1),\qquad (M)_0=1.
\tag{5.6}
\]

### Proposition 5.2 (exact adjacent full-column law)

The preceding \(m^{-1}\) statement must not be overextended to every
fully specified adjacent column.  Let \(D\) be a fixed compatible full
column of radius \(e\) at start \(i+1\).  Then, with \(M=m-d\),

\[
 \boxed{
 \Pr(D\mid\mathcal C_i^{(d)})=
 \begin{cases}
  M^{-1},&e<d,\\[1mm]
  M^{-2},&e=d,\\[1mm]
  \bigl((M)_{e-d}(M)_{e-d+1}\bigr)^{-1},&e>d.
 \end{cases}}
\tag{5.7}
\]

For a fixed incompatible column the probability is zero.  The same formula
holds for a left neighbor; the two falling-factorial roles are interchanged,
which leaves their product unchanged.

#### Proof

For \(e<d\), all target sets have the form (5.4), so the unique departure
\(z\) is the only unrevealed datum.  For \(e=d\), the sets through rank
\(d\) still have that form, while

\[
 A_{i+1,d+1}=(C_{d+1}\setminus\{z\})\cup\{w\}.
\]

A compatible full specification determines both \(z\) and \(w\).  The
first is uniform on \(B\), while the second is uniform on
\([n]\setminus T\); both sets have size \(M\), and the two orders are
independent.  This proves the middle line of (5.7).

Now let \(e=d+r>d\).  Relative to the source bottom block, the target
column specifies \(r\) ordered boundary coordinates: the departure and
the \(r-1\) source-base coordinates exposed as its first increments.  This
has probability \(1/(M)_r\).  Above the source top it specifies \(r+1\)
ordered complement coordinates, with probability \(1/(M)_{r+1}\).
The two permutations are independent, proving the final line for the right
neighbor.

For a left neighbor of radius \(d+r\), the complete column instead fixes
\(r+1\) terminal positions of the uniform \(B\)-order and \(r\) complement
positions.  Their probabilities are \(1/(M)_{r+1}\) and \(1/(M)_r\), so
the same product results.  When \(e=d\), it fixes one endpoint in each
permutation and gives \(M^{-2}\); when \(e<d\), it is determined by one
exterior coordinate and gives \(M^{-1}\). \(\square\)

For unequal adjacent radii, conditioning in the direction from the larger
radius to the smaller one therefore always has a first-order value

\[
 \frac1{m-\max\{d,e\}}.
\tag{5.8}
\]

Merely arranging the radius blocks monotonically removes that value in one
directed exposure order, but not in the reverse order.  It does not give an
undirected \(O(m^{-2})\) column-overlap hypothesis.

### Proposition 5.3 (the unequal-radius interfaces are not negligible)

Let

\[
 \mathcal R=\{0\le d<H:a_d>0\},\qquad K=|\mathcal R|.
\]

Then

\[
 \boxed{K=\Omega(\sqrt m).}
\tag{5.9}
\]

Consequently even the minimum-interface block ordering has at least
\(K-1=\Omega(\sqrt m)\) unequal-radius adjacencies.  Summed in their
first-order conditioning directions, (5.8) contributes at least

\[
 \frac{K-1}{m}=\Omega(m^{-1/2}),
\tag{5.10}
\]

which is not \(o(m^{-1/2})\).

#### Proof

The exact adjacent-binomial ratio gives

\[
 \begin{aligned}
 a_d
 &\le \frac{N_{-d}-N_{-(d+1)}}p+1\\
 &=\frac{N_{-d}}p\frac{2d+2}{m+d+2}+1.
 \end{aligned}
\tag{5.11}
\]

Also

\[
 \frac{N_{-d}}W
 =\prod_{j=0}^{d-1}\frac{m-j}{m+j+2}
 \le
 \exp\left(-\frac{d(d+1)}{m+H+1}\right).
\tag{5.12}
\]

Since \(W/p=b+o(1)\), maximizing
\((d+1)e^{-d(d+1)/(m+H+1)}/m\) gives, uniformly for \(d\le H\),

\[
 a_d=O(b/\sqrt m)+1=O(b/\sqrt m).
\tag{5.13}
\]

On the other hand,

\[
 \sum_{d=0}^{H-1}a_d=b-b_{-H}=(1-o(1))b,
\tag{5.14}
\]

because \(b_{-H}/b=m^{-\alpha^2+o(1)}=o(1)\).  Equations
(5.13)--(5.14) prove (5.9).  Every ordering of the \(K\) nonempty radius
classes has at least \(K-1\) interfaces, and each has a direction of size
at least \(1/m\) by (5.8). \(\square\)

The sum (5.10) uses different source columns and different conditioning
events; it is not one overlap row sum and is not a lower bound on matching
leave.  Its exact scope is that an analysis which separately charges every
unrouted interface does not obtain an \(o(m^{-1/2})\) bound.  A joint
integral packetization can still absorb these interfaces without paying
that formal sum.

### Proposition 5.4 (one-spacer seam repair)

Let \(K=|\{d:a_d>0\}|\).  Replace the original start interval
\([0,b-1]\) by

\[
 [0,b+K-2],
\]

place the nonempty radius classes in increasing-radius consecutive blocks
\(\widetilde J_d\) of lengths \(a_d\), and leave one start undesignated
between consecutive blocks.  Put

\[
 \widetilde I_q=\bigcup_{d\ge\rho(q)}\widetilde J_d.
\tag{5.15a}
\]

Then:

1. the designated count in every rank remains exactly \(b_q\);
2. every pair of slots in different consecutive radius blocks has
   \(a+c\ge2\); reapplying the proof of Theorem 1.1 with the enlarged
   slot-span bound \(J'=b+3H+O(1)=o(m-H)\) gives the same
   \(210/(m-H)^2\) intrinsic tail bound;
3. conditioned on any complete source column of radius \(d\), every fixed
   compatible complete target column across the seam has probability at
   most

   \[
   \binom{m-d}{2}^{-1}
   =\frac{2}{(m-d)(m-d-1)};
   \tag{5.15}
   \]

4. the number of inserted positions in one atom is at most \(H\), and the
   total extra literal length over at most \(p\) atoms is

   \[
   pH\le \frac{WH}{b}=o(W).
   \tag{5.16}
   \]

#### Proof

Blank starts change no designated rank count.  Across a block boundary the
two designated starts have distance at least two.  If two position
intervals at those starts were related by one Boolean cover, the longer
interval would have length exactly one more and would have to contain the
shorter.  Containment across a displacement of at least two requires at
least two extra endpoint positions, a contradiction.  Hence \(a+c\ge2\).
After the insertions every position difference is at most
\(J'=b+3H+O(1)=o(m-H)\).  The successive-term estimates
(1.5)--(1.8) therefore apply verbatim with \(J'\), proving the claimed
\(210/(m-H)^2\) tail bound.

For the conditional bound, let the target start be \(s\ge2\) positions to
the right.  Its maximum set determines the unordered omitted source-bottom
set

\[
 \{x_i,x_{i+1},\ldots,x_{i+s-1}\}.
\]

It is uniform among the \(\binom{m-d}{s}\) subsets of \(B\), so a fixed
complete target column has probability at most
\(\binom{m-d}{s}^{-1}\).  For a target \(s\) positions to the left, its
complete flag individually identifies any right-exterior additions and
therefore identifies the unordered \(s\)-set of left-exterior coordinates;
the same bound follows from the uniform complement order.  Every relevant
\(s\) is \(o(m)\), so eventually

\[
 2\le s\le\frac{m-d}{2},\qquad
 \binom{m-d}{s}\ge\binom{m-d}{2},
\]

which proves (5.15) for every cross-block pair.

There are at most \(H+1\) nonempty radius classes, proving the position and
length bounds.  The enlarged injective span remains legal because
\(b+3H=o(m)\).  Finally \(H/b=o(1)\) for the parameters in Section 0.
\(\square\)

If \(E'\) denotes the number of labelled spaced atoms, coordinate
transitivity still gives the exact rank degree

\[
 d'_q=\frac{b_qE'}{N_q}.
\tag{5.16a}
\]

One spaced atom emits exactly

\[
 b+2H+K
\tag{5.16b}
\]

base windows, compared with \(b+2H+1\) before spacing.  Every designated
target retains the literal consecutive-union identity; the base window at
a blank start is emitted but is not itself a designated column.  Thus a
matching of at most \(p\) spaced atoms pays at most
\(p(K-1)\le pH=o(W)\) additional letters and has exactly the same rank
coverage and repair ledger.

The spacer repair is a genuine reset-free, \(o(W)\)-cost improvement: it
removes every first-order **radius-interface** seam.  Inside each
equal-radius block, however, the central diagonal cover edges (3.3) remain
at target level.  If complete columns are first chosen from a global
disjoint dictionary, their equal-radius compatibility is indeed second
order by (5.7), but the remaining task is then the long compatibility-path
packing of Section 6.  Pairwise full-column probability is not a Hall or
expansion theorem for those paths.

### Proposition 5.5 (exact spaced macro-packet decomposition)

In the spaced architecture of Proposition 5.4, the \(a+c=1\) slot graph
has exactly one connected component for every nonempty radius class
\(d\).  That component contains

\[
 \boxed{(2d+2)a_d}
\tag{5.17}
\]

target slots: \(a_d\) consecutive starts, each carrying the complete rank
range \(-d,\ldots,d+1\).  Every slot pair in distinct components has
\(a+c\ge2\).

#### Proof

Within one radius-\(d\) block, the rank-\(0/1\) slots form the alternating
central ladder (3.4), with \(b\) replaced by \(a_d\).  It is connected.
Every lower or upper noncentral slot at one of these starts attaches to the
central ladder by successive same-start cover edges.  Hence the whole block
is one component, of the size in (5.17).

Different blocks are separated by at least one undesignated start, so
Proposition 5.4 proves that no cover edge joins them. \(\square\)

This is the strongest valid form of the proposed contraction.  The
first-order object is not an individual vertical chain but a complete
two-parent equal-radius Pascal ladder.  After contracting those ladders,
all inter-packet target geometry is genuinely second order, and the total
blank-start cost is \(o(W)\).

What remains unproved is an **integral spaced macro-packet theorem**:
construct a global target-disjoint dictionary of these physical ladder
packets in the exact proportional counts and join one packet of every
radius class into each of \(p-o(p/\sqrt m)\) common injective FIFO rows
across the blank starts.  The blank is not a reset; the two neighboring
packets must still be compatible with one common coordinate word.  Abstract
SCD flow supplies the chain counts but neither the two-parent packets nor
their distance-two FIFO seam matching.

## 6. What exact chain preselection really leaves

Fix an SCD \(\mathscr D\).  A fully \(\mathscr D\)-owned atom requires
every designated radius column to be the clipped segment of its unique
\(\mathscr D\)-chain.  For a middle owner \(X\), write its lower and upper
flags as \(L_q(X)\) and \(U_q(X)\).

If consecutive middle windows are \(X\to Y\), a common tight coordinate
word forces, wherever the displayed flags exist,

\[
 L_q(Y)=Y\cap L_{q-1}(X),
\tag{6.1}
\]

and

\[
 U_q(X)=X\cup U_{q-1}(Y).
\tag{6.2}
\]

It also forces a two-sided endpoint collar and pairwise disjoint transition
supports.  Call such a path **row-completable**.

### Theorem 6.1 (fixed-pool equivalence)

For every integer \(s\), matchings of \(s\) fully
\(\mathscr D\)-owned proportional atoms are in bijection with \(s\)
vertex-disjoint row-completable directed paths on \(b\) middle owners,
each path carrying exactly \(a_d\) radius-\(d\) owners for every \(d\).

#### Proof

A physical tight row gives (6.1)--(6.2) by the literal consecutive-window
intersection/union identities.  Its designated columns lie in distinct
SCD chains, so disjoint atoms give vertex-disjoint owner paths.

Conversely, row-completability supplies one injective tight coordinate
word realizing every clipped SCD flag.  Distinct owner paths use distinct
SCD chains, and an SCD partitions all Boolean targets, so the resulting
atoms are target-disjoint. \(\square\)

This contraction removes **all** target overlap, not merely the cover
part.  The demanded size

\[
 s=p-o(p/\sqrt m)
\tag{6.3}
\]

requires the paths to cover

\[
 sb=W-o(W/\sqrt m)
\tag{6.4}
\]

middle owners in only \((1+o(1))W/b\) components.  No consequence of the
unrestricted estimate (1.4) supplies this path packing.  Conditioning on an
arbitrary integral chain pool can make a putative physical continuation
sparse, deterministic, or absent.

This is the formal noncommutation:

\[
 \boxed{
 \begin{array}{c}
 \text{row first}\ \Longrightarrow\ \text{all vertical flags are fixed,}\cr
 \text{chain flow first}\ \Longrightarrow\ \text{FIFO row compatibility is not supplied.}
 \end{array}}
\tag{6.5}
\]

## 7. Exact proved/conditional boundary

The following statements are proved.

1. The intrinsic non-cover row sum is at most
   \(210/(m-H)^2\).
2. The exact floor-balanced Boolean chain flow exists with rank leave
   \(R_q=N_q-pb_q<p\).
3. Every one-chain central flow leaves the explicit raw unrestricted mass
   (3.8) outside its central matching.  No claim about conditioned
   post-flow codegrees is made.
4. Absorbing all first-order slot relations contracts the complete atom.
5. The exact adjacent full-column law is (5.7).  Equal radii give
   \(1/(m-d)^2\), while every unequal pair has a first-order conditioning
   direction.
6. There are \(\Omega(\sqrt m)\) nonempty radius classes, so unspaced
   first-order interfaces have aggregate order at least \(m^{-1/2}\).
7. One blank start between radius blocks removes every unequal-radius
   cover seam with total literal cost at most \(pH=o(W)\).
8. After spacing, the first-order slot graph consists exactly of the
   equal-radius ladder macro-packets of size \((2d+2)a_d\); every
   inter-packet slot pair is second order.
9. Preselecting a disjoint SCD pool converts the problem exactly into the
   long row-completable path packing of Theorem 6.1.

The following statement is unproved and is the correct replacement for the
failed unconditioned-deletion shortcut.

> **Joint Pascal-flow/FIFO theorem (OPEN).**  Construct
> \(p-o(p/\sqrt m)\) target-disjoint physical tight rows, each with the
> exact radius histogram \((a_0,\ldots,a_H)\), by resolving both parents of
> every central Pascal diamond simultaneously with all deeper integral
> chain capacities and the common FIFO endpoint chronology.

In the spaced formulation, it is enough to resolve each equal-radius
component of Proposition 5.5 as one integral macro-packet and then prove a
near-perfect distance-two FIFO seam matching between the packets.  The
verified \(O(m^{-2})\) inter-packet overlap is an input to that theorem, not
a proof of it.

Equivalently, one may seek an SCD satisfying the row-completable packing
bound (6.3), but ordinary SCD existence and balanced Hall flow do not imply
it.

An exact middle wreath factor resolves the middle-owner chronology only.
Requiring its deeper flags to have distinct common-owner support is the
strong labelled synchronization condition, not the weaker unlabelled MWB
condition.  No implication from MWB to that labelled statement is used
here.

If the open joint theorem were proved, the existing proportional-atom
literal ledger would give a contiguous-OR word of length \(W+o(W)\).  This
report supplies no such word and makes no constant-one claim.

## 8. Independent audit record

Five independent proof audits were applied to the decisive step.

1. The first audit verified both cover orientations and the connected path
   (3.4).  It independently derived the exact conditional probability
   \(1/(m-d)\) for a central neighbor and corrected an overbroad claim:
   a fully specified equal-radius adjacent column has probability
   \(1/(m-d)^2\), not \(1/(m-d)\).
2. The second audit independently verified denominator cancellation after
   routing \(P\subset P\cup\{y\}\): conditioning reveals \(y\) and leaves
   only a uniform departure from \(P\).  It also verified that contracting
   both cover orientations collapses the central ladder.
3. The third audit rederived (1.2) by exact permutation counting, checked
   that proper overlaps have at most two orientations and containments of
   gap \(k\) have at most \(k+1\) placements, and confirmed that no
   \(a+c\ge2\) type contributes at first order.
4. A fourth audit derived the complete falling-factorial law (5.7), caught
   the reverse-direction first-order dependence between unequal radii, and
   verified the distance-two spacer repair and its exact \(pH\) cost.
5. A final scope audit separated raw unrestricted codegrees from
   flow-conditioned codegrees, and separated the formal multi-interface
   sum (5.10) from any matching-leave lower bound.  Those corrections are
   incorporated in Theorem 3.2 and Proposition 5.3.  It also independently
   passed the spaced macro-packet decomposition of Proposition 5.5.

The audits agree on the implication scope: one-successor contraction does
not by itself expose a uniformly second-order target system.  A
flow-dependent, row-aware two-stage construction and a simultaneous
whole-row construction both remain open.
