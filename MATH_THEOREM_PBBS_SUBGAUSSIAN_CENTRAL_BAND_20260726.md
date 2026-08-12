# PBBS gives a coefficient-one sub-Gaussian central-band word

Date: 2026-07-26

## Theorem

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\operatorname {Cat}_m=\frac{W}{n}.
\]

Let \(h=h(m)\) be any integer sequence with

\[
 1\le h,
 \qquad h=o(\sqrt m).
\]

Then there is a literal contiguous-OR word of length

\[
 W+O(Bh\sqrt m)=W\bigl(1+O(h/\sqrt m)\bigr)
 =W+o(W)
\]

which covers every subset of \([2m+1]\) whose rank lies in

\[
 [m-h,m+h+1].
\]

In particular, every half-width \(h=o(\sqrt m)\), including
\(h=\sqrt m/\omega(m)\) for arbitrary \(\omega(m)\to\infty\), is
unconditionally attainable at coefficient one inside the central band.

## Proof

The audited PBBS dominance-staircase compiler gives, for every \(H\),

\[
 \mathcal L_H
 \le W+2HB+2(5H-1)\nu_H(P_m),                 \tag{1}
\]

where \(\nu_H(P_m)\) is the maximum edge-disjoint packing of PBBS
coordinate-residence intervals of length at most \(H\).  The word counted
by \(\mathcal L_H\) covers ranks \(m-H+1,\ldots,m+H+1\).

The reciprocal-height trace theorem at the fixed Gaussian window
\(H_0=\lceil\sqrt m\rceil\), together with the deck inequalities and the
negligibility of short quotient cycles, gives an absolute constant \(C\)
such that

\[
 \nu_{H_0}(P_m)\le C B\sqrt m                         \tag{2}
\]

for all sufficiently large \(m\).  Since the packing number is monotone
in its allowed residence length, (2) implies

\[
 \nu_H(P_m)\le C B\sqrt m                             \tag{3}
\]

for every \(H\le H_0\).  Set \(H=h+1\).  Since
\(h=o(\sqrt m)\), eventually \(H\le H_0\), and this compiler covers
\([m-h,m+h+2]\), hence in particular the displayed band.  Substitution
in (1) yields

\[
 \mathcal L_{h+1}-W
 \le 2(h+1)B+2(5h+4)CB\sqrt m
 =O(Bh\sqrt m).                                      \tag{4}
\]

Finally \(W=(2m+1)B\), so

\[
 \frac{\mathcal L_{h+1}-W}{W}=O(h/\sqrt m)=o(1).
\]

This proves the theorem. \(\square\)

## Exact scope

This is a central-band theorem, not the full constant-one theorem.  The
audited product-SCD exterior word beginning outside this band has length

\[
 L_m(m-h-1)\le C_0W\exp\!\left(-\frac{h^2}{8m}\right).
\]

That estimate is \(o(W)\) only when \(h/\sqrt m\to\infty\), whereas the
theorem above assumes \(h/\sqrt m\to0\).  The two proved mechanisms do not
overlap.  Closing this Gaussian-scale gap still requires either

1. the little-\(o\) PBBS packing estimate \((\mathrm{ST}_A)\) for every
   fixed \(A\), followed by a slowly growing diagonal; or
2. a new tail/central fusion which replaces rather than appends their
   baseline costs.

The theorem does, however, rigorously refute a logarithmic upper limit for
the PBBS factor-blind central compiler: its proved range is already
arbitrarily close to \(\sqrt m\) from below.
