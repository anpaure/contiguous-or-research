# PBBS sub-Gaussian band and the product-SCD quantifier

Date: 2026-07-26

## Verdict

Two separate assertions must not be conflated.

1. The present PBBS compiler already gives an unconditional
   \((1+o(1))W\)-length literal word for every paired central band of
   half-width

   \[
      h=o(\sqrt m).
   \]

2. A separately appended exterior-tail word cannot have length \(o(W)\)
   at a fixed Gaussian cutoff \(H=A\sqrt m\), and a fortiori cannot do so
   at \(H=o(\sqrt m)\).  For a separate tail, the condition
   \(H/\sqrt m\to\infty\) is not merely an artefact of the product-SCD
   upper bound: it is forced by the boundary antichain.

Thus the sub-Gaussian PBBS theorem is a genuine unconditional advance, but
it does not overlap the product-SCD exterior construction.  Bridging the
strip between the two cutoffs requires a new reuse/strip theorem (or the
open critical little-oh improvement); changing the quantifier in the
existing tail theorem does not close it.

## 1. The unconditional PBBS estimate

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 B=\operatorname {Cat}_m={W\over n}.
\]

The audited reciprocal-height trace at the fixed window
\(H_0=\lceil\sqrt m\rceil\), followed by the deck comparison, gives

\[
 \overline\nu_{H_0}=O(B/\sqrt m),
 \qquad
 \nu_{H_0}(P_m)=O(B\sqrt m).
 \tag{1.1}
\]

Indeed

\[
 \nu_{H_0}(P_m)
 \le 2n\overline\nu_{H_0}+nZ_{H_0},
\]

and the short-cycle term satisfies \(nZ_{H_0}=o(B)\).  Since the residence
packing number is monotone in the cutoff,

\[
 \boxed{\nu_H(P_m)=O(B\sqrt m)\quad(1\le H\le\sqrt m).}
 \tag{1.2}
\]

The linear dominance-seam compiler is unconditional and says

\[
 L_H\le W+2HB+2(5H-1)\nu_H(P_m),                 \tag{1.3}
\]

provided \(2H\le m+1\).  Combining (1.2)--(1.3), uniformly for
\(H\le\sqrt m\),

\[
 \boxed{
 {L_H\over W}
 \le 1+O(H/m)+O(H/\sqrt m).
 }
 \tag{1.4}
\]

Consequently \(H=o(\sqrt m)\) gives \(L_H=(1+o(1))W\).

The compiler with parameter \(H\) covers ranks

\[
 m-H+1,m-H+2,\ldots,m+H+1.                       \tag{1.5}
\]

There is a harmless one-rank asymmetry in (1.5).  In the usual paired
notation, for any integer \(h=o(\sqrt m)\), apply (1.4) with \(H=h+1\).
It gives a word of length \((1+o(1))W\) covering every target in

\[
 \boxed{
 \bigcup_{q=0}^{h}
 \left(
   \binom{[2m+1]}{m-q}
   \cup
   \binom{[2m+1]}{m+1+q}
 \right).
 }
 \tag{1.6}
\]

The word actually covers one additional upper rank.  The standard
one-coordinate lift transfers the same \((1+o(1))\) statement to the
opposite parity, with only the corresponding endpoint shift.

This is a central-band theorem, not yet the full constant-one theorem.

## 2. Why a separate fixed-\(A\) tail cannot be negligible

We use the elementary antichain lower bound for literal words.

### Lemma 2.1 (one endpoint per antichain member)

If a linear literal word of length \(L\) covers every member of an
antichain \(\mathcal A\), then \(L\ge|\mathcal A|\).

#### Proof

Choose one witnessing interval for every member of \(\mathcal A\) and
map it to its right endpoint.  The unions of intervals with a common
right endpoint are nested as the left endpoint moves.  Thus two distinct
incomparable targets cannot have the same right endpoint.  The map is
injective. \(\square\)

In even dimension, the product-SCD exterior word at central cutoff \(H\)
covers, in particular, the whole rank

\[
 r=m-H-1.
\]

Hence every such separate exterior word has length at least

\[
 \binom{2m}{m-H-1}.                                \tag{2.1}
\]

Writing \(k=H+1\),

\[
 {\binom{2m}{m-k}\over\binom{2m}{m}}
 =\prod_{j=0}^{k-1}{m-j\over m+j+1},              \tag{2.2}
\]

and, uniformly for \(k=O(\sqrt m)\),

\[
 \log {\binom{2m}{m-k}\over\binom{2m}{m}}
 =-{k^2\over m}+O(k^3/m^2).                       \tag{2.3}
\]

Therefore, if \(H=A\sqrt m+O(1)\) with fixed \(A\),

\[
 \boxed{
 L_{\rm tail}\ge(e^{-A^2+o(1)})\binom{2m}{m}.
 }
 \tag{2.4}
\]

If \(H=o(\sqrt m)\), the lower bound is \((1-o(1))\binom{2m}{m}\).
The odd-dimensional boundary rank gives the same conclusion, using

\[
 {\binom{2m+1}{m-H}\over\binom{2m+1}{m}}
 =e^{-H(H+1)/m+o(1)}
\]

in the Gaussian range.

The proved product-SCD estimate

\[
 {L_m(m-H-1)\over\binom{2m}{m}}
 \le C_0e^{-H^2/(8m)}                              \tag{2.5}
\]

is therefore correctly quantified:

* fixed \(A\) gives only an \(O_A(W)\) exterior word, and (2.4) shows its
  cost cannot be \(o(W)\);
* \(A\to0\) is worse, with a tail cost at least \((1-o(1))W\);
* \(H/\sqrt m\to\infty\) makes (2.5) \(o(W)\), and the boundary-rank
  lower bound shows that this Gaussian escape is essentially necessary
  for any **separately appended** exterior word.

## 3. Exact remaining gap

The unconditional PBBS word ends at a cutoff \(h=o(\sqrt m)\).  The
factor-blind tail becomes negligible only at a cutoff
\(H=\sqrt m\,\omega(1)\).  Hence these two existing mechanisms leave the
mesoscopic strip

\[
 h<q<H.                                             \tag{3.1}
\]

No choice of a fixed Gaussian constant removes (3.1).  The live options
are therefore:

1. prove the critical residence improvement that lets the PBBS compiler
   reach \(H=\sqrt m\,\omega(1)\);
2. recycle the PBBS baseline nonlocally across the mesoscopic strip; or
3. prove the independent integral fine-strip/owner-recycling theorem.

The standard parity lift and the product-SCD concatenation introduce no
additional obstruction once one of these strip interfaces is supplied.
