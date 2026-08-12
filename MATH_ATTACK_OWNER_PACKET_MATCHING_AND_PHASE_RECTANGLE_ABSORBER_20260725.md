# Owner-first top packets and a coefficient-safe phase rectangle

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or external search is
used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},\qquad
 \lambda_H={W\over N_H},\qquad M=m+H,
\tag{0.1}
\]

where \(H\) is the least integer with \(\lambda_H\ge M\). Then

\[
 H\sim\sqrt{m\log m},\qquad
 MN_H=W-o(W),\qquad HN_H=o(W).
\tag{0.2}
\]

The corrected order of attack is forced.

1. First choose an owner-only near-transversal of full top packets. The
   corresponding tagged packet hypergraph is asymptotically regular, has
   exact maximum relative owner codegree \(2/m^2\), and packets on distinct
   tops overlap in at most \(H\) owners. A near-perfect matching in this
   hypergraph would cover \(W-o(W)\) middle owners in \(O(W/m)\) promotion
   cycles. This matching is not proved here. The available quantitative
   growing-uniformity matching theorem does not apply at packet size
   \(M=\Theta(m)\).

2. A full four-order rectangle must not be deployed by putting two full
   packets on one top. Either diagonal has at least \(M-4\) repeated
   owners. The resulting \(0/2\)-top construction loses asymptotically half
   of the middle layer.

3. The exact rank selector does survive as a **phase rectangle**. Cut the
   cyclic starts into two complementary contiguous arcs and put one order on
   each arc. Each side then consists of two length-\(\Theta(m)\) promotion
   paths, has only \(O(1)\) repeated owners, changes only \(O(1)\) middle
   owners, and realizes the desired isolated octahedral square up to at most
   eight incidence units in every rank. Its total collateral damage through
   depth \(H\) is \(O(H)\).

Consequently as many as \(R=O(N_H)=O(W/m)\) phase rectangles are
coefficient-safe:

\[
 \text{owner damage}=O(R)=O(W/m),\qquad
 \text{band collateral}=O(HR)=o(W),
\tag{0.3}
\]

and their extra reset cost is also \(O(HR)=o(W)\). They can therefore be a
final absorber for an \(O(W/m)\)-scale point-neutral residual. They cannot
repair a positive-density vertical defect. A larger correction requires a
genuinely nonlocal circuit whose two packet sides are separately
owner-near-disjoint.

## 1. The owner-only tagged packet hypergraph

For a top \(U\in\binom{[2m]}M\), an oriented cyclic order \(\pi\) modulo
rotation gives the packet

\[
 P_m(U,\pi)=\{I_\pi(j,m):j\in\mathbb Z_M\}.
\tag{1.1}
\]

It is the owner set of one promotion cycle. Define the tagged hypergraph
\(\mathcal G_H\) with vertex set

\[
 \binom{[2m]}m\ \sqcup\ \{\tau_U:U\in\binom{[2m]}M\}
\tag{1.2}
\]

and edge

\[
 E(U,\pi)=\{\tau_U\}\cup P_m(U,\pi).
\tag{1.3}
\]

Thus every edge has size \(M+1\) and exactly one tag.

### Proposition 1.1 (exact degrees)

Let

\[
 D=(M-1)!.
\tag{1.4}
\]

Every tag has degree \(D\). Every middle owner has degree

\[
 D_m=\binom mH m!H!={m!^2\over(m-H)!},
\tag{1.5}
\]

and

\[
 {D_m\over D}={M\over\lambda_H}=1-o(1).
\tag{1.6}
\]

#### Proof

There are \((M-1)!\) oriented cyclic orders on one labelled top. A fixed
owner \(X\) lies in \(\binom mH\) tops. In one such top, contracting \(X\)
to one cyclic block gives \(m!H!\) orders in which \(X\) is an interval.
This proves (1.5). Direct factorial cancellation gives (1.6). \(\square\)

### Proposition 1.2 (exact owner codegrees)

For distinct middle owners \(X,Y\), put

\[
 d=|X-Y|=|Y-X|.
\]

If \(1\le d<H\), then

\[
 {\deg(X,Y)\over D_m}={2\over\binom md^2}.
\tag{1.7}
\]

If \(d=H\), then

\[
 {\deg(X,Y)\over D_m}
 ={m-H+1\over\binom mH^2},
\tag{1.8}
\]

and the codegree is zero for \(d>H\). Consequently

\[
 \max_{X\ne Y}{\deg(X,Y)\over D_m}={2\over m^2}.
\tag{1.9}
\]

These are the exact packet counts: for \(d<H\), the complements of \(X,Y\)
inside a common top are two overlapping cyclic \(H\)-intervals; their four
nonempty consecutive blocks may be ordered in two directions. At \(d=H\)
the two \(H\)-intervals are disjoint, giving the boundary factor in (1.8).

### Proposition 1.3 (tag--owner codegree)

If \(X\subset U\), then

\[
 \deg(\tau_U,X)=m!H!,\qquad
 {\deg(\tau_U,X)\over D}={M\over\binom MH}=o(m^{-2});
\tag{1.10}
\]

otherwise the codegree is zero.

Thus \(\mathcal G_H\) is a near-regular tagged \((M+1)\)-graph with

\[
 {\Delta_2(\mathcal G_H)\over D}
 ={2+o(1)\over m^2}.
\tag{1.11}
\]

### Owner packet matching gate

A matching of \(t\) edges in \(\mathcal G_H\) gives \(t\) distinct tops and
\(Mt\) distinct middle owners. Hence

\[
 t=N_H-o(N_H)
\tag{1.12}
\]

would give \(W-o(W)\) owners in \(O(W/m)\) promotion cycles. The omitted
top masks themselves number only \(N_H=o(W)\), and may be appended
literally.

The scalar and codegree data do not by themselves prove (1.12). In
particular the explicit growing-uniformity matching hypothesis

\[
 e^{2(M+1)}\Delta_2\log D=o(D)
\tag{1.13}
\]

fails, since its left-to-right ratio is at least

\[
 e^{2m+o(m)}{\log D\over m^2}\longrightarrow\infty.
\tag{1.14}
\]

This is a limitation of that black-box nibble, not an obstruction to the
matching.

## 2. Direct packet-overlap audit

The codegrees count how often two owners occur together over all packets.
For absorber design one also needs the intersection of two fixed packet
supports.

### Lemma 2.1 (different tops overlap in at most \(H\) owners)

Let \(U,V\in\binom{[2m]}M\), put

\[
 d=|U-V|=|V-U|,
\]

and choose arbitrary cyclic orders \(\pi,\rho\) on them. Then

\[
 |P_m(U,\pi)\cap P_m(V,\rho)|
 \le
 \begin{cases}
 H-d+1,&1\le d\le H,\\
 0,&d>H.
 \end{cases}
\tag{2.1}
\]

In particular two packets on distinct tops share at most \(H\) owners.

#### Proof

A common owner \(X\) is contained in \(U\cap V\), so \(d\le H\). Inside
\(U\), its complement \(A=U-X\) is a cyclic \(H\)-interval containing the
fixed \(d\)-set \(U-V\). If a cyclic \(H\)-interval contains a prescribed
\(d\)-set, the number of possible starts is at most \(H-d+1\), with equality
when those \(d\) points occupy a shortest contiguous block. Every such
complement determines \(X\). \(\square\)

### Lemma 2.2 (nearby orders on one top overlap almost completely)

If cyclic orders \(\pi,\rho\) on the same top have cyclic adjacent-swap
distance \(a\), then

\[
 |P_m(U,\pi)\cap P_m(U,\rho)|\ge M-2a.
\tag{2.2}
\]

#### Proof

One adjacent swap changes exactly the two \(m\)-windows having a boundary
between the swapped positions. Follow a shortest sequence of \(a\) swaps
and use the union bound. \(\square\)

The full rank-isolating rectangle has \(a=2\) on either diagonal, hence at
least \(M-4\) repeated owners. This proves directly why local full-packet
rectangles cannot be used before owner matching.

Changing the top is not a small substitute. If \(V=U-u+v\) and the order
is changed only by replacing \(u\) with \(v\) in the same position, the two
packets share exactly the \(H\) middle windows avoiding that position and
differ on the other \(m\). Thus cross-top separation cures duplicate
owners only by making an order-\(m\) owner change.

## 3. A restricted phase rectangle

The full rectangle can be made coefficient-safe by splitting each diagonal
between two complementary start arcs.

Fix cyclic positions \(0,1,\ldots,M-1\), two disjoint adjacent swaps

\[
 \tau_0=(0\ 1),\qquad \tau_r=(r\ r+1),\qquad2\le r\le M-2,
\tag{3.1}
\]

and four orders

\[
 \pi_{ab}=\tau_0^a\tau_r^b\pi,\qquad a,b\in\{0,1\}.
\tag{3.2}
\]

The critical length-\(r\) start is \(j_*=1\): its interval is the arc
\(1,2,\ldots,r\), whose two boundaries cut the two swapped pairs.

Choose two cyclic intervals \(A,B\subset\mathbb Z_M\) such that

\[
 A\cup B=\mathbb Z_M,\qquad A\cap B=\{j_*\},
\tag{3.3}
\]

and

\[
 |A|,|B|=M/2+O(1).
\tag{3.4}
\]

For a start interval \(J\), write

\[
 \mathcal I_s^J(\sigma)=\sum_{j\in J}e_{I_\sigma(j,s)}.
\tag{3.5}
\]

Define the signed phase rectangle

\[
 Z_s=
 \mathcal I_s^A(\pi_{00})+\mathcal I_s^B(\pi_{11})
 -\mathcal I_s^A(\pi_{10})-\mathcal I_s^B(\pi_{01}).
\tag{3.6}
\]

Each term in (3.6) is one contiguous promotion path of length
\(M/2+O(1)\).

### Theorem 3.1 (rank action and leakage)

Let \(\mathscr R_s\) be the full four-order rectangle. Then, for every
\(1\le s<M\),

\[
 \boxed{\|Z_s-\mathscr R_s\|_1\le8.}
\tag{3.7}
\]

Consequently:

* if \(s\notin\{r,M-r\}\), then \(\|Z_s\|_1\le8\);
* at \(s=r\), \(Z_r\) is the desired elementary octahedral square plus an
  error of \(\ell_1\)-norm at most eight;
* at \(s=M-r\), the same holds for the complementary square; and
* at the middle length \(m\notin\{r,M-r\}\),

  \[
  \|Z_m\|_1\le8.
  \tag{3.8}
  \]

Thus choosing \(r=m-q\) or \(r=m+q\) isolates the requested controlled
rank up to \(O(1)\) leakage in every other band rank. The aggregate leakage
through depths \(0,1,\ldots,H\) is \(O(H)\).

#### Proof

At the common start \(j_*\), (3.6) contains all four rectangle terms. At
every other start in \(A\), it retains the first difference
\(\pi_{00}-\pi_{10}\), and at every other start in \(B\), it retains the
parallel first difference \(\pi_{11}-\pi_{01}\).

Compare this with the full rectangle, which contains both first differences
at every start. For a fixed length \(s\), either first difference is the
effect of one adjacent swap and is nonzero at only two cyclic starts. At
most four omitted start differences remain, each of the form \(e_X-e_Y\).
Their total \(\ell_1\)-norm is at most eight. The full rectangle vanishes
outside \(r,M-r\) and is the octahedral square at those two lengths. \(\square\)

### Theorem 3.2 (owner overlap of each phase side)

At either rank-isolating choice \(r=m-q\) or \(r=m+q\), \(q\ge1\), each
side of (3.6) has \(M+1\) middle-owner occurrences and at least

\[
 \boxed{M-3}
\tag{3.9}
\]

distinct middle owners. Equivalently, its duplicate excess is at most
four.

#### Proof

Consider the positive side. Apart from \(j_*\), the start sets \(A,B\)
are disjoint. The two orders \(\pi_{00},\pi_{11}\) differ by two adjacent
swaps. If a common middle owner comes from starts distinct from \(j_*\),
then at least one of its two windows is among the at most four middle
windows changed by those swaps; otherwise both are unchanged windows of
the base order and equality forces equal starts. Hence there are at most
four such common owners.

At \(j_*\), the two middle windows are distinct. If \(r=m-q\), the
length-\(m\) window beginning at \(j_*\) contains exactly one position from
the first swapped pair and both positions from the second. If \(r=m+q\),
it contains exactly one position from the first pair and neither position
from the second. In either case the first swap changes the owner. Thus
the common start adds no duplicate. Since \(|A|+|B|=M+1\), (3.9) follows.

For the negative side, compare \(\pi_{10}\) and \(\pi_{01}\) with the base
order. Each differs by one adjacent swap, so the same argument gives at
most \(2+2=4\) common owners. \(\square\)

### Corollary 3.3 (coefficient-safe deployment)

Use \(R\) phase rectangles, each on a top assigned to the absorber. Moving
from one side of every rectangle to the other changes at most \(4R\) middle
loads in either sign, creates at most \(O(HR)\) aggregate non-target band
incidences, uses \(2R\) promotion paths on either side, and incurs reset
cost \(O(HR)\).

For

\[
 R=O(N_H)=O(W/m),
\tag{3.10}
\]

all three costs are \(o(W)\). The useful isolated-rank correction supplied
by these rectangles is only \(O(R)=O(W/m)\).

## 4. What a nonlocal full-packet absorber must do

The overlap lemmas leave two possible absorber architectures.

### 4.1 Genuinely nonlocal packet circuits

Every positive and every negative packet family must use each top at most
once, or use same-top orders at cyclic adjacent-swap distance
\(\Omega(M)\). Bounded adjacent-swap diameter gives \(M-O(1)\) duplicate
owners by Lemma 2.2.

Moreover an adjacent-swap middle-change vector determines its top: the four
changed middle owners have union \(U\). Therefore two adjacent-swap change
vectors on distinct tops cannot be negatives of one another. Exact
owner-neutral cancellation needs at least three tops and a genuine circuit;
it cannot be a paired two-top exchange.

### 4.2 Restricted phase absorbers

Theorem 3.2 avoids the same-top overlap by assigning almost disjoint start
arcs to the two orders. It sacrifices exact rank isolation only by \(O(1)\)
incidences per rank. Since \(HN_H=o(W)\), that sacrifice is globally
affordable even on \(O(N_H)\) tops.

The remaining assignment problem is finite-capacity rather than algebraic.
For each desired octahedral correction, choose a top containing its
\(r+2\)-point support, choose a critical start and two half-cycle arcs, and
make all absorber owner defects fall in a common \(o(W)\) reservoir. The
point-marginal lattice theorem guarantees formal decompositions but does not
provide this top-and-owner matching.

## 5. Exact conditional completion statement

The following separates the two remaining gates.

> **Owner-first phase-absorber gate.** Suppose:
>
> 1. the tagged packet hypergraph \(\mathcal G_H\) has a matching covering
>    \(W-o(W)\) middle owners with \(O(N_H)\) packets; and
> 2. after reserving \(R=O(N_H)\) matched tops, the residual vertical
>    discrepancy is a sum of at most \(R\) isolated octahedral squares that
>    can be assigned injectively to those tops as phase rectangles.
>
> Then the selected promotion paths have \(W-o(W)\) distinct middle owners,
> aggregate band collateral \(o(W)\), and total reset toll \(o(W)\).

The second clause is strong enough for only an \(O(W/m)\)-scale final
residual. If the owner near-transversal initially has a vertical defect
\(\omega(W/m)\), boundedly many rank-selector rectangles per top cannot
remove it. One then needs either a multi-top circuit with macroscopic rank
action and separately near-disjoint packet sides, or a new owner matching
which builds the vertical conditions in from the outset.

## 6. Ledger

### Proved here

1. The exact owner-only tagged packet degrees and codegrees.
2. The fixed-packet cross-top overlap bound \(H-d+1\).
3. The same-top adjacent-distance overlap bound \(M-2a\).
4. The failure of the available quantitative matching hypothesis at
   \(M=\Theta(m)\).
5. A two-path-per-side phase rectangle with only \(O(1)\) owner overlap.
6. Its desired octahedral action plus at most eight incidence units of
   leakage per rank.
7. \(O(N_H)\) such absorbers have \(o(W)\) owner, band, and reset cost.

### Still open

1. A near-perfect matching in the owner-only tagged packet hypergraph.
2. A top-reservoir matching for the phase rectangles.
3. A nonlocal multi-top circuit with separately owner-near-disjoint signs.
4. A construction whose pre-absorber vertical residual is \(O(W/m)\), the
   scale the phase rectangles can finish.

