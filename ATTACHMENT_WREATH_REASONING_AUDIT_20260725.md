# Independent audit of the attached wreath/interval-design reasoning

Date: 2026-07-25

Audited source:
`/Users/amir.nuriyev/.codex/attachments/4c0ec6aa-3101-421c-aae2-6f97939073fb/pasted-text.txt`

Method: pure mathematics only.  No computation or web search.

## 0. Overall verdict

The attachment is a 1405-line exploratory transcript, not a completed proof
note.  It does **not** prove the coefficient-one theorem, MWB, MWC, or a new
multi-depth wreath construction.  Its final part is truncated in the middle
of the strip discussion.

It contains three rigorous and useful items:

1. the standard MWC-to-coefficient-one reduction;
2. an exact odd-wreath complementation identity which removes the upper
   shadows as independent constraints; and
3. a genuine arithmetic obstruction to a translation-equivariant algebraic
   factor.  For prime \(n=2m+1\equiv3\pmod4\), no translation-equivariant
   exact middle wreath factor exists.

Its independent-random-order barrier and adjacent-rank codegree calculations
are also correct as calculations, but they do not constitute an impossibility
theorem for correlated integral constructions.

The main incorrect assertion is that arbitrary missing masks at different
ranks can be repaired at cost equal to the largest single-rank defect.
That requires a compatible nested-chain resolution and is not automatic.
The endpoint-throughput theorem gives the corresponding lower-capacity
bound, not this claimed upper bound.

Several other statements are heuristic (random exact-factor behavior,
concentration, strip codegrees, and possible nibble improvements).  None may
be promoted to a theorem.

## 1. MWC reduction

### Claim

Let \(n=2m+1\), \(W=\binom nm\), and let
\(H\ge\sqrt{2m\log m}\), \(H=o(m)\).  Suppose
\((1+o(1))W/n\) cyclic orders cover all but \(o(W)\) masks in the aggregate
band \(m-H,\ldots,m+H+1\).  Then

\[
 \nu(n)\le(1+o(1))W.                                    \tag{1.1}
\]

### Verdict: valid

For a cyclic order \(\pi\), emit

\[
 E_j=I_\pi(j,m-H),\qquad
 E_0,E_1,\ldots,E_{n-1},E_0,\ldots,E_{2H}.              \tag{1.2}
\]

Then

\[
 E_j\cup\cdots\cup E_{j+t-1}
 =I_\pi(j,m-H+t-1),                                     \tag{1.3}
\]

so the block length is \(n+2H+1\).  The total main length is

\[
 (1+o(1))\frac Wn(n+2H+1)=W+o(W).                       \tag{1.4}
\]

Literal repair of the aggregate \(o(W)\) band holes is legal.  The two
binomial tails are \(o(W)\) at the stated \(H\).  The trimmed one-bit lift
then handles the other parity.

This is a correct sufficient reduction, not a construction of the required
cyclic orders.  The newer crossing-top packet theorem in
`TOP_FIBRE_CROSSING_PACKET_REDUCTION_20260725.md` is a more structured even
dimensional sufficient route; the attachment does not solve its packet
matching gate.

## 2. Exact complementation of odd wreath shadows

### Theorem 2.1 (valid new extraction)

Let \({\cal P}\) be any family of cyclic orders on \([2m+1]\).  Let
\(\mu_r(S)\) count occurrences of \(S\) as a cyclic \(r\)-interval in
\({\cal P}\).  Then

\[
 \boxed{\mu_r(S)=\mu_{n-r}(S^c).}                        \tag{2.1}
\]

Consequently, if \(M_q^-\) is the defect at rank \(m-q\) and \(M_q^+\)
the defect at rank \(m+q\), then

\[
 \boxed{M_q^+=M_{q-1}^-\qquad(q\ge1).}                  \tag{2.2}
\]

In particular, an exact middle wreath factor has

\[
 M_1^+=M_0^-=0.                                         \tag{2.3}
\]

#### Proof

In one cyclic order, the complement of a cyclic \(r\)-interval is the
opposite cyclic interval of length \(n-r\), and this is a bijection on
pointed starts.  Since

\[
 n-(m+q)=m+1-q=m-(q-1),
\]

(2.2) follows. \(\square\)

### Verdict

Correct.  Thus in the odd exact-wreath lane the upper band is not an
independent balancing problem.  It is the shifted complement of the lower
band.  This identity is special to full cyclic orders on all \(2m+1\)
coordinates; it does not directly identify the two shadow systems of the
even crossing-top packets, whose cycles live inside proper tops
\(U\subset[2m]\).

## 3. Consecutive-up-set reformulation

### Theorem 3.1

Let

\[
 X_j=I_\pi(j,m).
\]

Then

\[
 \bigcap_{i=0}^{q}X_{j+i}=I_\pi(j+q,m-q).               \tag{3.1}
\]

Hence a rank-\((m-q)\) target \(T\) occurs as a lower window if and only
if the middle necklace contains \(q+1\) consecutive vertices in the
principal up-set

\[
 \{X\in\tbinom{[n]}m:T\subset X\}.                      \tag{3.2}
\]

At \(q=1\), this says that a lower color \(T\) occurs precisely when the
Johnson 2-factor contains an edge in the clique of the \(m+2\) middle
supersets of \(T\).

### Verdict: valid

This is the exact path-hitting formulation already used in the current
project.  It is a reformulation, not an existence proof.

## 4. Independent random cyclic orders

### Proposition 4.1

Take \(N\) independent uniform oriented cyclic orders with

\[
 Nn=CW
\]

for fixed \(C>0\).  At lower depth \(q\), put

\[
 N_q=\binom n{m-q},\qquad \lambda_q=W/N_q.
\]

A fixed target is an interval of one order with probability \(n/N_q\), so

\[
 \Pr(S\text{ missed})
 =\left(1-\frac n{N_q}\right)^N
 =e^{-C\lambda_q+o(1)}.                                 \tag{4.1}
\]

For \(q=u\sqrt m\), \(\lambda_q=e^{u^2+o(1)}\).  Therefore any band
containing a fixed positive multiple of \(\sqrt m\) has expected misses

\[
 \Theta_C\!\left(
 W\sqrt m\int e^{-u^2-Ce^{u^2}}\,du
 \right)
 =\Theta_C(W\sqrt m).                                   \tag{4.2}
\]

### Verdict: valid expectation; overclaimed interpretation

The expectation calculation is correct.  For large \(C\), the integral is
of order \(e^{-C}/\sqrt C\), so independent selection needs roughly
\(C\ge\tfrac12\log m\) before this expectation becomes \(o(W)\).

This rules out i.i.d.-like order selection at constant density.  It does
not rule out a correlated exact factor, a packet matching, or a
design-theoretic construction.  The attachment's statement that
concentration "should hold" is not proved and is unnecessary for the
expectation barrier.

The attachment also says at one point that depth one must have
\(M_1=o(W/\sqrt m)\).  That is false for MWC/MWB.  The aggregate condition
only forces \(M_1=o(W)\).  No equal allocation of the total error over all
depths is required.

## 5. Adjacent nested codegree

### Proposition 5.1

Among oriented cyclic orders modulo rotation, a fixed \(r\)-set has degree

\[
 D_r=r!(n-r)!.                                            \tag{5.1}
\]

If \(S\subset T\), \(|S|=r\), \(|T|=r+1\), their codegree is

\[
 D(S,T)=2r!(n-r-1)!.                                     \tag{5.2}
\]

Thus

\[
 \frac{D(S,T)}{D_r}=\frac2{n-r},\qquad
 \frac{D(S,T)}{D_{r+1}}=\frac2{r+1}.                    \tag{5.3}
\]

### Verdict: valid

For central \(r\), the relative adjacent-rank codegree is
\(\Theta(1/m)\).  If one puts \(n(H+1)\) rank occurrences into one ordinary
hyperedge, the product of edge size with this ratio is \(\Theta(H)\).
This correctly identifies the nested-column clustering.  It explains why
the cited fixed/growing-uniformity black boxes do not directly apply; it is
not an impossibility theorem for a structure-aware argument.

The later strip claims (including the asserted strip value
\(K\Delta_2/D\approx4\)) are not derived in the attachment and should be
treated as speculation.

## 6. Prime translation action and the AP obstruction

The attachment's AP discussion contains a genuine exact obstruction which
can be sharpened.

Assume \(n=2m+1\) is prime, and let translations of \(\mathbb Z_n\) act on
unoriented wreaths.

### Lemma 6.1

A translation-fixed wreath is an arithmetic-progression wreath.  Up to
reversal there are exactly

\[
 \frac{n-1}{2}=m                                         \tag{6.1}
\]

distinct such wreaths.  Every other translation orbit of wreaths has size
\(n\).

#### Proof

The Johnson-adjacency graph on the \(n\) middle windows of one wreath is an
\(n\)-cycle, and hence reconstructs the underlying cyclic order up to the
dihedral ambiguity.  If translation by one fixes the wreath, it induces an
automorphism of this cycle.  Its order divides the odd prime \(n\), so a
nontrivial action is a rotation, not a reflection.  Thus for some nonzero
phase step \(s\),

\[
 x_{i+s}=x_i+1.
\]

Since \(n\) is prime, \(s\) is invertible and the order is an arithmetic
progression.  Reversal identifies differences \(a\) and \(-a\).  A
nonfixed orbit has size \(n\). \(\square\)

### Theorem 6.2 (translation-equivariant factor obstruction)

Let

\[
 B=\frac Wn=\operatorname{Cat}_m
\]

be the number of wreaths in an exact middle factor.  If a
translation-invariant exact factor exists, then

\[
 B=a+nb\qquad\text{for some }0\le a\le m,               \tag{6.2}
\]

where \(a\) is the number of fixed AP wreaths in the factor.

Moreover

\[
 \operatorname{Cat}_m
 \equiv2(-1)^m\pmod n.                                   \tag{6.3}
\]

Hence if \(m\) is odd, equivalently \(n\equiv3\pmod4\), then

\[
 B\equiv n-2>m\pmod n,                                  \tag{6.4}
\]

and no translation-equivariant exact middle factor exists.

#### Proof

An invariant family is a disjoint union of fixed wreaths and free
size-\(n\) orbits, proving (6.2).  Since an exact factor cannot contain both
orientations of the same AP wreath, \(a\le m\).

For the congruence,

\[
 \operatorname{Cat}_m
 =\frac1{m+1}\binom{2m}{m}
 =\frac1{m+1}\binom{n-1}{m}
 \equiv 2(-1)^m\pmod n,                                 \tag{6.5}
\]

because \(2(m+1)=n+1\equiv1\pmod n\).  If \(m\) is odd, the least
nonnegative residue is \(n-2=2m-1>m\), contradicting (6.2). \(\square\)

### Verdict

This is valid and strengthens the attachment's examples \(n=7,11\).  The
AP family itself covers only \(mn=o(W)\) middle sets.  Equivariance alone
also leaves the same mean shadow load and hence does not beat the Poisson
barrier.  The theorem rules out the simplest \(\mathbb Z_n\)-equivariant
completion on every prime \(n\equiv3\pmod4\).

For \(m\) even, (6.3) only says that exactly two fixed AP wreaths modulo
\(n\) are arithmetically compatible; it does not prove existence.

## 7. The false cross-rank repair assertion

The attachment claims that missing masks at different ranks can be chained
so that the repair cost is bounded by the maximum single-rank defect.

### Verdict: false / unsupported

There is no automatic nesting relation among arbitrary hole families in
different ranks.  A chain cover of their union has size equal to the width
of the induced hole poset, which may greatly exceed the largest individual
rank size.  More importantly, an abstract chain cover is not automatically
a contiguous-OR/MTF word.

The exact endpoint-throughput inequality says that \(R\) appended endpoints
can create at most \(R\) new masks at any one rank and at most
\(R|{\cal Q}|\) new rank incidences across \({\cal Q}\).  It supplies a
lower-capacity obstruction, not the claimed upper construction.

Any valid cross-rank repair requires an explicit nested-flow, SCD-tail,
signed-subcube, or other literal factorization theorem.  The attachment
does not provide one.

## 8. Remaining claims

### Exact middle factors

The statement that exact middle wreath factors exist for all \(m\) is
correct, via the known \(C_{2m+1}\)-factor of the odd graph and the explicit
conversion of a shortest odd cycle to a wreath.  It is input, not new work
in the attachment.

### Reservoir threshold

The heuristic threshold

\[
 q\asymp\sqrt{m\log\log m}
\]

for an \(o(W)\)-cost random reservoir is consistent with the already proved
factorial/reservoir transfer, once its density parameter tends to zero at
the calibrated rate.  The attachment does not restate all hypotheses and
therefore is not a replacement proof.

### Finite examples

The \(m=4,n=9\) fully vertical certificate and the quoted canonical MSW
histograms are finite workspace data.  They support plausibility but do not
imply an asymptotic theorem.  One sentence says the canonical factor
"misses rank 4 at depth one"; this is a rank-label typo, since depth one
below the middle is rank three.

### Random exact factors

Claims about the distribution of a uniform random exact factor and its
negative correlations are heuristic.  No measure, switching count, or
conditioning estimate is proved.

### Strip/nibble lane

The final strip discussion is incomplete and ends mid-sentence.  Its mask
and word-length heuristics may be useful for exploration, but the asserted
codegree and economical-cover conclusions are not proved there.  They add
no theorem to the calibrated frontier.

## 9. Net mathematical contribution

The attachment does not move the construction frontier beyond the current
crossing-packet/rectangle work.  The two items worth retaining are

\[
 \boxed{M_q^+=M_{q-1}^-}
\]

for odd full-wreath families, and

\[
 \boxed{
 n=2m+1\text{ prime},\ n\equiv3\pmod4
 \Longrightarrow
 \text{no translation-equivariant exact middle wreath factor}.}
\]

The coefficient-one gate remains integral and correlated: construct the
multi-depth cyclic interval design (odd MWC), or solve the even crossing-top
packet matching plus its shadow balancing.  The attachment proves neither.
