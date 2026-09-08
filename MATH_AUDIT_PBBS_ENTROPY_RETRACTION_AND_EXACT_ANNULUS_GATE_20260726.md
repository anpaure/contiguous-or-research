# Audit: PBBS refutes the independent-depth ledger, but the tail does not overlap

Date: 2026-07-26

## Verdict

The revised entropy assessment is correct in its main conclusion:
the independent-depth occupancy ledger is not a valid obstruction to the
constant-one theorem.  The PBBS Johnson factor supplies a sibling object
with complete correct-rank lower support at every depth despite only
logarithmic catalogue entropy per middle set.  The depth tower is therefore
strongly correlated.

The suggested final quantifier check has a definite negative answer.  For
the audited product-SCD exterior word,

\[
 \frac{L_m(m-H-1)}{\binom{2m}{m}}=o(1)
 \quad\Longleftrightarrow\quad
 \frac{H}{\sqrt m}\longrightarrow\infty.
\]

At every fixed Gaussian cutoff \(H=A\sqrt m\), its normalized length tends
to a strictly positive function \(F(A)\); at \(H=o(\sqrt m)\) it tends to
\(2\sqrt2\).  Thus the product-SCD tail cannot be joined directly to the
proved PBBS compiler below \(\sqrt m\).

## 1. Repaired sprinkling theorem

Put

\[
 q_0=\left\lceil\sqrt{2m\log\log m}\right\rceil.
\]

If a family \(\mathcal Q\) of \((1-o(1))C_m\) cyclic orders satisfies the
aggregate shallow bound

\[
 \sum_{q\le q_0}M_q(\mathcal Q)=o(W),
\]

then adding \(C_m/\log m\) independent orders leaves \(o(W)\) holes in all
deeper ranks.  Indeed \(W/N_q\ge \exp(q(q+1)/(m+1))\), so for
\(q>q_0\) the added mean is at least \((1+o(1))\log m\), and

\[
 \sum_{q>q_0}N_q\exp\!\left(-\frac{W}{N_q\log m}\right)
 \le \frac{2^{2m+1}}{m}=O(W/\sqrt m)=o(W).
\]

The aggregate quantifier is essential; pointwise \(M_q=o(W)\) over a
growing number of depths is insufficient.

## 2. What PBBS proves unconditionally

The critical PBBS packing bound and compiler imply, for every
\(h=o(\sqrt m)\), a literal central-band word of length

\[
 W+O(C_mh\sqrt m)=W+o(W).
\]

This covers both central sides through half-width \(h\), after the standard
one-rank parameter shift.  Hence every \(c\log m\) band, and in fact every
\(\sqrt m/\omega(m)\) band, is already a theorem.

The PBBS all-depth support theorem also invalidates the independent-depth
entropy bill as a universal lower bound.  This calibration does not itself
produce cyclic wreaths: PBBS windows are Johnson intersections and its
components need not satisfy cyclic residence.

More precisely, this refutes the claim that ambient catalogue entropy plus
an iid occupancy rate gives a model-independent obstruction.  It does not
exclude a different, wreath-specific counting obstruction coming from
cyclic residence or bundling.  Likewise, comparing the ambient counts of
Johnson 2-factors and wreath families is only a calibration; it is not a
measure-preserving comparison between the two ensembles.

## 3. Exact remaining annulus

The two proved mechanisms leave the Gaussian annulus

\[
 o(\sqrt m)<q<\sqrt m\,\omega(m)
\]

uncovered at coefficient one.  Equivalent sufficient ways to bridge it
include:

1. the fixed-window little-o packing estimate
   \(\nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(C_m\sqrt m)\) for every fixed
   \(A\), followed by diagonalization;
2. an integral fine-strip port matching with total leave \(o(W)\);
3. the weaker aggregate layered Hall deficiency \(o(W)\); or
4. a positive-density nonlocal braid/rethreading of the PBBS endpoint
   skeleton.

The current critical estimate is only \(O_A(C_m\sqrt m)\).  The missing
little-o is therefore real, not bookkeeping.

A hypothetical exterior theorem of cost \(o(W)\) for every fixed
\(A>0\) could be diagonalized with \(A=A_m\downarrow0\) and then joined to
the sub-Gaussian central theorem.  A theorem at only one fixed \(A\),
however, would still leave the interval between \(o(\sqrt m)\) and
\(A\sqrt m\).  For the actual product-SCD exterior neither version is
available: its fixed-window cost tends to the positive constant \(F(A)\).

## 4. New narrowing from packet overlays

Overlaying two exact strip factors reduces a two-choice packet compiler to
a signed graph.  Each target constraint has the form

\[
 x_P\oplus x_Q=1\oplus a\oplus b.
\]

Near coverage is equivalent to signed frustration index \(o(W)\), together
with \(o(W)\) pair-load imbalance.  A parameter-matched abstract construction
has all the correct degree, width, and fractional Hall data but forces a
one-quarter uncovered fraction.  Hence degrees, Hall, and local sparsity do
not suffice by themselves: the physical strip chronology must force an
all-but-\(o(W)\) coboundary identity.

## Bottom line

The entropy pessimism is withdrawn, and a strong sub-Gaussian theorem is
proved.  The full constant-one theorem is not closed by the existing tail.
The live problem is now an explicit Gaussian-annulus integrality/coboundary
statement rather than an entropy question.
