# Strict audit of the claimed domino-twin inverse-stability exponent (1/3)

Date: 2026-07-27

## Verdict

The cell normal form and the complete-cell dihedral alignment are valid in
the annular parameter range, after adding the hypotheses actually used
there.  The claimed bound

\[
 \#\{G:|F\setminus G|\le s\}\le \exp(O(m))n^{s/3}
\]

is **false**.  There is a synchronized two-front re-pairing family with
list exponent (1/2-o(1)).  It is stronger than the one-segment
(1/4-o(1)) construction because the two re-pairing segments have the
same carrier-exception set.  Lemma 2.1 contains precisely the two global
steps left open by the earlier star--top collar audit:

1. alignment of noncomplete edge anchors through a deleted gap; and
2. an injective/amortized accounting of pairings in a zero- or one-point
   gap, including overlapping collars and intact-domino transport.

Neither step follows from the displayed sliding-window identities.  The
second step fails on the construction in Section 4 below.

Moreover, even if the (1/3) list bound is granted, Section 4 does not close
the stopped survivor sum.  It estimates one surviving close neighbour and
omits the number of neighbours in the first allowed overlap shell.  The
current independent thinning theorem controls target and target-pair
degrees, not these conditional overlap-shell degrees.

## 1. Parts that do audit successfully

Let

\[
 A_i=B_i\cup\cdots\cup B_{i+r-1},\qquad
 \mathcal S_i=\{A_i\cup\{x\}:x\in B_{i-1}\cup B_{i+r}\}.
\]

The following steps are correct.

1. The \(m\) four-target star cells are disjoint and partition a simple
   twin support of size \(4m\).
2. If three members of one \(\mathcal S_i(F)\) occur in (G), their common
   intersection has size (R-1), so their Johnson triangle is a canonical
   star triangle of (G), not a top triangle.  The same applies to a
   complete cell.
3. Two common targets form a Johnson edge.  The exact twin clique census
   leaves a star realization and a top realization (both in the mate-edge
   case), so recording a star/top bit is a valid finite local record.
4. If at most (s) targets are missing, at most (s) cells are incomplete.
   Hence for (s=o(m)) there are consecutive complete cells.
5. In the annular range
   \[
     r=(m-q_0-1)/2=(1/2-o(1))m
   \]
   and (s=o(m)), complete cores determine one global dihedral alignment.
   After two consecutive complete cores are aligned, a deleted gap has
   length at most (s<r); distances from two already aligned cores select
   the forward continuation uniquely.

The last item requires (r=\Theta(m)), (r<m/2), and (s<r-O(1)).  The
stated theorem instead assumes only (1<r<m-1).  Formula

\[
 |A_i\cap A_j|=2(r-d)
\]

for cyclic distance (d\le r), and the gap induction based on it, are not
valid under that full stated range.  This is a scope defect, although it is
repairable for the intended annular application.

## 2. The edge-anchor gap

For a two-point top anchor, the record gives the literal carrier

\[
 U=X\cup Y,
\]

which is a union of (r+1) consecutive (G)-dominoes.  It does **not** by
itself give

* the index of this carrier in the (G)-word;
* its two endpoint dominoes; or
* the pairing of the other two endpoint labels.

The earlier exact star--top audit shows why this is substantive.  A fixed
shared edge has \(\Theta(n)\) top continuations with one noncommon target
and \(\Theta(n^2)\) continuations with two noncommon targets.  First-collar
charges remove most of that entropy, but leave two global issues: collars
can overlap and intact old dominoes can be transported through a chain.

Lemma 2.1 replaces those issues by the sentence

> “The phase and the two neighbouring phases tell which ... alternative
> is being used.”

This does not prove that a noncomplete anchor has the aligned (G)-index,
nor that its endpoint pairing is determined.  Lemma 1.5 aligns complete
cells only.  A separate induction is needed which either aligns every
edge anchor across a gap or charges every possible index/endpoint change
to at least three units of defect.  No such induction appears in the
proof.

## 3. The zero-cell zipper gap

The recurrences

\[
 W_{j+1}=(W_j\setminus C_j)\cup C_{j+r},\qquad
 W_{j-r+1}=(W_{j-r}\setminus C_{j-r})\cup C_j
\]

are correct identities once the domino word is known.  They do not imply
that choosing one member of an unknown entering domino forces its mate.
The opposite recurrence identifies the same **whole domino**; it does not
specify its internal pairing.

Already if an exposed boundary determines only a four-label union

\[
 C_j\cup C_{j+1}=\{a,b,c,d\},
\]

there are three unordered pairings (and six ordered pairings) of those
labels.  For a gap of length (u), the corresponding ordered-pairing
count is factorial.  A true proof can still hope to pay for it because a
local re-pairing creates defects at both window fronts; indeed the known
contiguous-segment family has list exponent (1/4+o(1)).  But that is an
amortized global assertion, not a consequence of either recurrence alone.

To establish the claimed (n^w) count, one needs an explicit injective
encoding with at most one freely recorded label per weak cell, after
quotienting all endpoint pairings and intact-domino chains.  The table
(2.3) merely states this encoding; its prose does not construct it or
prove injectivity.  This is exactly the unresolved global residual in
`MATH_AUDIT_DOMINO_FOUR_TARGET_STAR_TOP_COLLAR_CHARGE_20260727.md`.

Therefore the implication

\[
 w\le s/3\quad\Longrightarrow\quad
 \#G\le \exp(O(m))n^{s/3}
\]

is unsupported.

## 4. A synchronized two-front counterexample

Work in the annular range and write

\[
 m=2r+\delta,
 \qquad \delta=m-2r=q_0+1=O(\sqrt m).
\]

Choose

\[
 \delta+3<u=o(m),
\]

and eventually take (u=m/\sqrt{\log m}).  For a domino position (t),
let

\[
 I_t=\{t-r,t-r+1,\ldots,t\}\subseteq\mathbb Z_m
\]

be the set of top-carrier indices whose carrier contains (B_t).  Put

\[
 U=[0,u-1]\ \cup\ [r+1,r+u].                           \tag{4.1}
\]

There are two large classes of domino positions having identical carrier
incidence outside (U):

\[
 P_+=[r,r+u],\qquad |P_+|=u+1,                          \tag{4.2}
\]

and

\[
 P_-=\{m-1\}\cup[0,u-\delta+1],
 \qquad |P_-|=u-\delta+3.                              \tag{4.3}
\]

Indeed

\[
 I_{t+1}\triangle I_t=\{t-r,t+1\}.                    \tag{4.4}
\]

For every consecutive pair in (P_+), both members on the right of
(4.4) lie in the two arcs of (U).  The same holds cyclically along
(P_-): for the step (m-1\to0) the removed index is
(m-r-1=r+\delta-1\in U), and for the remaining steps the removed
indices run through ([r+\delta,r+u]), while the added indices lie in
([0,u-1]).  Therefore

\[
 I_t\setminus U=I_{t'}\setminus U
 \quad(t,t'\in P_+),
 \qquad
 I_t\setminus U=I_{t'}\setminus U
 \quad(t,t'\in P_-).                                   \tag{4.5}
\]

Starting from a fixed packet (F), independently repartition the labels
in the domino positions (P_+) and (P_-).  More precisely, in each
class arbitrarily distribute its (2|P_\pm|) labels into an ordered list
of (|P_\pm|) unordered pairs.  This produces

\[
 N_u=
 \frac{(2|P_+|)!}{2^{|P_+|}}
 \frac{(2|P_-|)!}{2^{|P_-|}}                           \tag{4.6}
\]

paired cyclic words before the final dihedral quotient.

Let (V_j) and (D_j=B_j\cup B_{j+r}) be the carrier and endpoint
four-set of the canonical top cell

\[
 \mathcal T_j=\{V_j\setminus\{x\}:x\in D_j\}.
\]

Equation (4.5) shows that every (V_j) with (j\notin U) is unchanged
under all these re-pairings.  The endpoint set (D_j) is unchanged unless

\[
 j\in P:=P_+\cup P_-
 \quad\hbox{or}\quad j+r\in P.
\]

Consequently every top cell outside

\[
 Z=U\cup P\cup(P-r)                                    \tag{4.7}
\]

is literally unchanged.  The special placement makes (P) almost a
subset of (U): it adds only the two positions (r,m-1), while (P-r)
adds at most two further boundary positions.  Hence

\[
 |Z|\le2u+4.                                           \tag{4.8}
\]

The top cells are disjoint and partition each twin support.  Therefore
every resulting packet (G) satisfies

\[
 |F\setminus G|\le4|Z|\le8u+16.                        \tag{4.9}
\]

A simple twin support recovers its unordered domino partition and cyclic
block order up to dihedral presentation.  Thus at most (2m) of the words
in (4.6) give one support, and

\[
 |B_{8u+16}(F)|\ge \frac{N_u}{2m}.                     \tag{4.10}
\]

Since (u\gg\delta), Stirling's formula gives

\[
 \log N_u=(4+o(1))u\log u.                             \tag{4.11}
\]

Take (u=m/\sqrt{\log m}).  Then (s=8u+16=o(m)), and

\[
 \log |B_s(F)|\ge(4-o(1))u\log m,                     \tag{4.12}
\]

whereas the claimed (1/3) theorem would give

\[
 \log |B_s(F)|\le Cm+\left(\frac83+o(1)\right)u\log m.\tag{4.13}
\]

The difference is ((4/3-o(1))m\sqrt{\log m}\), which cannot be
absorbed by (Cm).  More generally, (4.10)--(4.12) show that any bound

\[
 |B_s(F)|\le e^{O(m)}n^{cs}
\]

valid uniformly for (s=o(m)) must have

\[
 \boxed{c\ge1/2.}                                      \tag{4.14}
\]

Thus the paired-window zipper does not merely lack an injection: two
opposite fronts can share the same weak carrier set and support two
independent factorial re-pairings.  Its claimed one-letter-per-weak-cell
accounting undercounts by an asymptotic factor two.

## 5. The survivor-shell factor missing from Section 4

Write

\[
 L_t(F)=\#\{G:|F\setminus G|\le t\}.
\]

Suppose, only for this calculation, that the claimed inverse estimate

\[
 L_t(F)\le e^{Cm}n^{t/3}
\]

is true.  Thin the catalogue by forbidding overlaps with defect below
(s).  The retained degree furnished by the priority thinning is of order

\[
 D_s\asymp D/\Delta_s,\qquad
 \Delta_s\le e^{Cm}n^{s/3}.
\]

The first allowed shell has defect about (s).  Without an additional
shell-degree theorem, its normalized stopped contribution is bounded by

\[
 \frac{L_s(F)}{D_s}\,z^{-(K-s)},
 \qquad z=m^{-1/2}.
\]

Using \(\log D=2m\log m-O(m)\), the logarithm of this expression is

\[
 \begin{aligned}
 &\left(\frac{s}{3}\log n+O(m)\right)
 +\left(\frac{s}{3}\log n-2m\log m+O(m)\right)\\
 &\hspace{35mm}
 +(2m-s/2)\log m
 =\frac{s}{6}\log m+O(m),
 \end{aligned}
\]

not \(-\frac{s}{6}\log m+O(m)\).  The negative expression in the
current note is the contribution of a **single** surviving neighbour; it
omits (L_s(F)).

Random-priority thinning might conceivably repair this if one proves that,
simultaneously for every retained (F), its retained defect-(t) shell is
smaller than the original shell by the retention factor
(p_s\asymp1/\Delta_s).  The existing concentration argument proves only
near-regular target degrees and target-pair codegrees.  It does not prove
this conditional shell statement, whose indicators have strongly
overlapping priority neighbourhoods.

Thus even a correct inverse exponent (c<1/2) is not by itself sufficient
for the particular conflict-thinning argument as written.  With no
shell preservation, the two list factors require (2c<1/2), i.e.
(c<1/4), which is ruled out (up to lower-order terms) by the contiguous
re-pairing lower bound.  A successful quarantine must therefore exploit
the thinning factor inside each close shell, or use a multiscale method
which charges the list entropy only once.

## 6. Strict status

* Cell normal form: **verified**.
* Complete-cell global alignment in the intended annular range:
  **verified**, after narrowing the hypotheses.
* Star/top local classification: **verified**.
* Paired-window (n^w) decoder: **false**, by the synchronized two-front
  construction.
* Claimed inverse exponent (1/3): **false**; every uniform power bound
  has exponent at least (1/2).
* Claimed macroscopic survivor closure from that exponent: **incorrect as
  written**, due to the omitted shell-count factor.

The lower exponent (1/2) is exactly the stopped survivor threshold.
Therefore no strict (c<1/2) inverse-stability repair exists for this
catalogue.  The theorem must be retracted and must not be used downstream.
