# Dense three-top conveyor packing and simultaneous floor-gradient rounding

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and assume \(H\ge2\), \(M\ge8H\).  Let \({\cal P}\) be the three-top
two-base conveyor constructed in
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.

The full coordinate orbit of \({\cal P}\) contains a state-adaptive
family of at least

\[
 \boxed{
 K_*:=\left\lfloor {N_H\over180HM^2}\right\rfloor}
\tag{0.2}
\]

instances with all the following properties.

1. Their three-element top-owner lists are pairwise disjoint: no
   rank-\(M\) top is reused.  This does not mean that the underlying
   \(M\)-subsets are coordinate-disjoint.
2. Their common middle supports are pairwise disjoint.
3. At every protected signed depth \((q,\epsilon)\), \(1\le q\le H\),
   the complete union of the two possible shores of one packet is
   disjoint from the corresponding union for every other packet.
4. Given arbitrary nonnegative external loads \(R_{q,\epsilon}\) with

   \[
       \sum_T R_{q,\epsilon}(T)\le N_q,
   \tag{0.3}
   \]

   every target touched by a selected packet has external load at most

   \[
                         K_0:=24HM.
   \tag{0.4}
   \]

5. There is one integral signing of all \(K_*\) packets for which, at
   every protected signed depth,

   \[
    \left|\sum_{P}\varepsilon_P
       \langle R_{q,\epsilon},\Delta_{P,q,\epsilon}\rangle\right|
       \le 16(2H+1)qK_0\le48HqK_0.
   \tag{0.5}
   \]

   The same signing is nearly cardinality-balanced:

   \[
                    \left|\sum_P\varepsilon_P\right|\le2H+1.
   \tag{0.5b}
   \]

Here \(\Delta_{P,q,\epsilon}\) is new minus old after fixing an arbitrary
reference orientation of \(P\).  In particular, the total positive
part of the aggregate gradient is at most

\[
 \boxed{
 \sum_{q,\epsilon}
 \left(\sum_P\varepsilon_P
 \langle R_{q,\epsilon},\Delta_{P,q,\epsilon}\rangle\right)_+
 \le16(2H+1)K_0H(H+1)
 \le48K_0H^2(H+1).}
\tag{0.5a}
\]

Consequently the selected integral state has floor energy at most the
unbiased two-shore average plus

\[
                         8(2H+1)qK_0
\tag{0.6}
\]

at each signed depth, and its total positive leakage over all protected
depths and both signs is at most

\[
 \boxed{
 8(2H+1)K_0H(H+1)
 \le24K_0H^2(H+1)
 =576M H^3(H+1)=O(MH^4).}
\tag{0.7}
\]

In particular, at the critical promotion scale

\[
 H=\Theta(\sqrt{m\log m}),\qquad M=(1+o(1))m,
\tag{0.8}
\]

the right side of (0.7) is \(O(m^3\log^2m)=o(W)\).  If in addition

\[
                         MN_H=(1+o(1))W,
\tag{0.9}
\]

then

\[
 K_*\ge(1-o(1)){W\over180HM^3}
       ={W\over m^{7/2+o(1)}}.
\tag{0.10}
\]

Thus the local conveyor does admit an
\(\Omega(W/\operatorname {poly}(m))\) owner-legal bank and one common
all-depth signing whose aggregate floor gradient lies in the nonpositive
orthant up to \(o(W)\) total leakage.

This is not a strict descent theorem from every prescribed integral
shore.  Exact coordinatewise nonpositivity is false without an
additional compatibility hypothesis, even for actual conveyors; the
two-coordinate parity example in Section 6 proves this.  What is proved
is the sharp asymptotic statement needed to round the simultaneous
half-old/half-new fractional point.

## 1. Exact packet data used

For a labelled packet \(P\), let

\[
 \Gamma^0_{P,q,\epsilon},\quad
 \Gamma^1_{P,q,\epsilon}
\tag{1.1}
\]

be its old- and new-shore load vectors at signed depth
\((q,\epsilon)\).  Uniformly on both protected physical rows, the
conveyor theorem gives

\[
 \Delta_{P,q,\epsilon}
 :=\Gamma^1_{P,q,\epsilon}-\Gamma^0_{P,q,\epsilon},
\qquad
 \|\Delta_{P,q,\epsilon}\|_1\le16q,
\tag{1.2}
\]

with equality on the active direct/root-complemented row: there are
\(8q\) coefficients of either sign there.  If the opposite
direct/root row is recorded separately, its derivative is zero and the
inequality remains valid.  Thus both protected signs can be included as
rows without a convention ambiguity.  The two shores are
coordinate-conjugate, so

\[
 \|\Gamma^0_{P,q,\epsilon}\|_2
 =\|\Gamma^1_{P,q,\epsilon}\|_2.
\tag{1.3}
\]

Every shore consists of three complete cyclic frames.  Hence, for

\[
 F_{P,q,\epsilon}
 :=\operatorname {supp}\Gamma^0_{P,q,\epsilon}
   \cup\operatorname {supp}\Gamma^1_{P,q,\epsilon},
\tag{1.4}
\]

we have

\[
                         |F_{P,q,\epsilon}|\le6M.
\tag{1.5}
\]

At the middle row, the old and new supports are the same squarefree set

\[
                         F_{P,0},\qquad |F_{P,0}|=3M.
\tag{1.6}
\]

Finally, \(P\) uses three distinct rank-\(M\) tops.  All these statements
are invariant under a coordinate permutation.

The exact derivative away from the protected annulus is not being
discarded.  In the notation of the conveyor theorem, for every interval
length \(h\),

\[
 \Delta_{P,h}
   =d_h(\omega;x,y)+d_h(\omega';x,y),
\tag{1.7}
\]

and a coordinate conjugate has the conjugated derivative.  Thus the
construction below is an actual all-depth frame replacement.  We use
the sharp formula (1.2) only on the protected annulus.

## 2. A general orbit-packing lemma

We record the elementary multihypergraph statement which supplies the
dense bank.

### Lemma 2.1 (good-orbit matching)

Let a finite group act transitively on each of the finite sets

\[
                         X_1,\ldots,X_s.
\]

Let one labelled object have a footprint of size \(r_j\) in \(X_j\).
Take its full group orbit with multiplicity.  Suppose a subcollection
contains at least half of the orbit.  Then this subcollection contains
a family whose footprints are pairwise disjoint in every \(X_j\), of
cardinality at least

\[
                 {1\over2D},\qquad
                 D:=\sum_{j=1}^s{r_j^2\over|X_j|}.
\tag{2.1}
\]

#### Proof

Let \(E\) be the size of the full orbit, counted with multiplicity.
Transitivity gives exact degree

\[
                         {Er_j\over|X_j|}
\tag{2.2}
\]

at every vertex of \(X_j\).  Choose a maximal pairwise-disjoint family
of \(k\) good objects.  Its union in \(X_j\) has \(kr_j\) vertices.
Every good object meets one of these unions, by maximality.  Counting a
good object once for every possible witnessing intersection only
overcounts, and therefore

\[
 {E\over2}
 \le \sum_j kr_j {Er_j\over|X_j|}
 =kED.
\tag{2.3}
\]

Cancel \(E\) to obtain (2.1). \(\square\)

The use of the orbit as a multiset avoids any stabilizer division.  A
disjoint family cannot contain the same geometric object twice, so the
selected packets themselves are distinct.

## 3. Removing heavy-gradient targets and packing the remainder

Let \({\mathfrak S}_{2m}\) act on one fixed labelled conveyor.  For a
uniform orbit element, every one of its footprint positions at signed
depth \((q,\epsilon)\) is uniform on

\[
                 X_{q,\epsilon}=\binom{[2m]}{m+\epsilon q},
                 \qquad |X_{q,\epsilon}|=N_q.
\tag{3.1}
\]

Define

\[
 B_{q,\epsilon}
 :=\{T:R_{q,\epsilon}(T)>K_0\}.
\tag{3.2}
\]

Equation (0.3) implies

\[
                         |B_{q,\epsilon}|<{N_q\over K_0}.
\tag{3.3}
\]

By (1.5) and a union bound, the proportion of orbit packets meeting any
bad target at any protected signed depth is at most

\[
 \sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
 {6M|B_{q,\epsilon}|\over N_q}
 \le {12HM\over K_0}={1\over2}.
\tag{3.4}
\]

Call the remaining packets good.

Apply Lemma 2.1 with the following parts:

* the rank-\(M\) top-owner set, of size \(N_H\), with footprint size
  \(3\);
* the middle-target set, of size \(W\), with footprint size \(3M\);
* the \(2H\) protected signed target sets in (3.1), each with footprint
  size at most \(6M\).

The corresponding \(D\) satisfies

\[
\begin{aligned}
 D
 &\le {9\over N_H}+{9M^2\over W}
      +\sum_{q=1}^H{72M^2\over N_q}\\
 &\le {9\over N_H}+{9M^2\over W}
      +{72HM^2\over N_H}\\
 &\le {90HM^2\over N_H}.
\end{aligned}
\tag{3.5}
\]

Here \(N_q\ge N_H\) and \(W\ge N_H\).  Lemma 2.1 now gives at least

\[
                         {N_H\over180HM^2}
\tag{3.6}
\]

pairwise-disjoint good packets.  Retain exactly \(K_*\) of them.  This
proves assertions 1--4 in Section 0.

Notice that disjointness was imposed on the complete two-shore
footprints, not merely on the support of \(\Delta\).  This is what removes
all cross-packet quadratic floor terms below.

## 4. Exact simultaneous floor identity

Fix one protected signed depth and abbreviate

\[
 \mu_P={\Gamma^0_P+\Gamma^1_P\over2},\qquad
 d_P={\Gamma^1_P-\Gamma^0_P\over2},\qquad
 a_P=\langle R,\Delta_P\rangle.
\tag{4.1}
\]

For a signing \(\varepsilon\in\{-1,1\}^{K_*}\), the chosen packet
load is

\[
                         \mu_P+\varepsilon_Pd_P.
\tag{4.2}
\]

Let the constant-baseline floor energy be

\[
 \Phi_c(L)={1\over2}\sum_T(L_T-c)(L_T-c-1).
\tag{4.3}
\]

The derivative of every packet has total coordinate sum zero.  Equation
(1.3) gives

\[
 \langle\mu_P,d_P\rangle
 ={\|\Gamma^1_P\|_2^2-\|\Gamma^0_P\|_2^2\over4}=0.
\tag{4.4}
\]

For distinct selected packets, every vector in (4.1) has disjoint
support by Section 3.  Expanding (4.3) therefore gives the exact identity

\[
 \boxed{
 \Phi_c\!\left(R+\sum_P(\mu_P+\varepsilon_Pd_P)\right)
 =C+{1\over2}\sum_P\varepsilon_Pa_P,}
\tag{4.5}
\]

where \(C\) is independent of the signing.  Moreover, \(C\) is exactly
the average of the left side over all \(2^{K_*}\) signings.

Because a selected packet is good, (1.2) and (0.4) give

\[
                         |a_P|\le16qK_0.
\tag{4.6}
\]

Thus the simultaneous energy problem is now a literal \(2H\)-row
linear discrepancy problem.  No heat approximation or ignored
restitution remains.

## 5. Deterministic all-depth rounding

### Lemma 5.1 (floating-variable vector balancing)

Let \(a_1,\ldots,a_K\in\mathbb R^d\), and suppose

\[
                         |a_i(j)|\le B_j
\tag{5.1}
\]

for every \(i,j\).  There are signs \(\varepsilon_i\in\{-1,1\}\) such
that

\[
                         \left|\sum_i\varepsilon_i a_i(j)\right|
                         \le dB_j
\tag{5.2}
\]

for every \(j\).

#### Proof

Start at \(x=0\in[-1,1]^K\), so \(\sum_i x_i a_i=0\).  While more than
\(d\) coordinates of \(x\) lie strictly between \(-1\) and \(1\), the
corresponding columns are linearly dependent.  Move \(x\), only in
those coordinates and in a nonzero null direction, until another
coordinate reaches the boundary.  The vector sum stays zero.  After
finitely many steps at most \(d\) coordinates remain unfixed.

Round every remaining coordinate to its nearest sign.  Each rounding
changes that coordinate by at most one.  Hence the error in row \(j\)
is at most \(dB_j\), proving (5.2). \(\square\)

Apply the lemma with \(d=2H+1\): use one row for every signed protected
depth and one additional cardinality row.  On the gradient rows put

\[
                         B_{q,\epsilon}=16qK_0.
\tag{5.3}
\]

On the cardinality row every column is \(1\), so \(B_{\rm card}=1\).
Lemma 5.1 proves (0.5), (0.5b), and hence (0.6) through (4.5).  In
particular, both shores occur

\[
                         {K_*\over2}+O(H)
\tag{5.3a}
\]

times.  The selected signing therefore differs on
\((1/2-o(1))K_*\) packets from either uniform shore.

Summing the positive parts of (0.5) over the two signs and
\(1\le q\le H\) gives

\[
 \sum_{q,\epsilon}
 \left(\sum_P\varepsilon_Pa_{P,q,\epsilon}\right)_+
 \le2\sum_{q=1}^H16(2H+1)qK_0
 =16(2H+1)K_0H(H+1),
\tag{5.4a}
\]

which is (0.5a).  The energy identity (4.5) has the additional factor
one half, so

\[
 \sum_{q,\epsilon}
 \left(\Phi_{q,\epsilon}(\varepsilon)-C_{q,\epsilon}\right)_+
 \le2\sum_{q=1}^H8(2H+1)qK_0
 =8(2H+1)K_0H(H+1),
\tag{5.4}
\]

which is (0.7).

This is a deterministic signing theorem.  It can also be viewed as
integral rounding of the common fractional choice \(x_P=0\), i.e. one
half of each shore, while preserving all \(2H\) floor-gradient rows up
to the displayed error.

### All-depth incidence leakage

At any interval length, the union of the old and new loads of one
three-frame packet has at most \(6M\) target incidences.  Even if direct
and root forms are counted separately at every one of the \(M+1\)
lengths, one packet changes at most

\[
                         12M(M+1)
\tag{5.5}
\]

raw target incidences across the complete all-depth ledger.  The
off-annulus subledger is no larger.  Therefore the entire retained bank
has crude all-depth raw incidence leakage at most

\[
 12K_*M(M+1)
 \le {N_H(M+1)\over15HM}
 =O(N_H/H)=o(W)
\tag{5.6}
\]

whenever \(H\to\infty\).  Equation (1.7), rather than (5.5), remains the
exact action on every such layer; (5.6) is only the universal support
ledger.  In particular, (5.6) is **raw incidence leakage**, not a
load-weighted off-annulus floor-energy estimate.  No such energy bound
is asserted without an off-annulus hypothesis on the external loads.

## 6. Why exact nonpositivity cannot be demanded

The \(o(W)\) allowance in (0.7) is essential at the level of quantifiers.
Take one actual packet and two protected depths \(q_1,q_2\).  Choose a
positive derivative target at \(q_1\) and a negative derivative target
at \(q_2\), and put one unit of external load on each.  Put no other
external load on the two derivative supports.  Then this packet's two
floor-gradient coordinates are

\[
                         (a_{q_1},a_{q_2})=(1,-1).
\tag{6.1}
\]

Either orientation makes one of the two coordinates positive.  The
construction is literal: the existence of the two chosen targets follows
from the \(8q\)-by-\(8q\) signed support in (1.2).  Additional mass needed
to complete a prescribed rank census can be placed outside the packet
footprints and does not alter (6.1).

More generally, on any footprint-disjoint bank one may realize (6.1) on
one chosen packet and zero score on every other packet: assign no load
on the other derivative supports.  The bank occupies fewer than
\(N_q/(30HM)\) targets at every protected row, so there are unused
targets on which any remaining prescribed census mass may be placed.
Hence there is no theorem, uniformly over all admissible external loads,
giving

\[
                         \sum_P\varepsilon_Pa_{P,q,\epsilon}\le0
\tag{6.2}
\]

at every row exactly.  Lemma 5.1 replaces this false demand by an error
which is polynomial in \(m\), hence \(o(W)\), simultaneously in every
row.

## 7. Exact proved boundary

Proved:

1. a state-adaptive bank of
   \(N_H/(180HM^2)=\Omega(W/\operatorname {poly}(m))\) actual
   three-top conveyors;
2. no repeated top owners, literal middle ownership, and disjoint complete
   two-shore footprints at all protected signed depths;
3. exact elimination of every cross-packet quadratic floor term;
4. one deterministic common signing with total positive protected
   floor-gradient leakage \(O(MH^4)=o(W)\);
5. exact all-depth conveyor action and \(O(N_H/H)=o(W)\) crude
   off-annulus raw incidence leakage, with no off-annulus energy claim;
   and
6. a literal two-depth obstruction to replacing asymptotic
   nonpositivity by exact nonpositivity.

Not proved:

1. that an arbitrary pre-existing promotion-ring resolution already
   contains this packet bank as alternating components;
2. strict negative descent from every integral starting shore;
3. completion of the unused roots and middle owners around the bank; or
4. coefficient one.

The next exact statement is therefore an **installation/completion
lemma**: embed the bank into one common-order promotion resolution while
retaining the external mass bound (0.3).  Once installed, the signing
and all-depth floor ledger above are unconditional.
