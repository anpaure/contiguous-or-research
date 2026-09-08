# Independent audit: fixed-parameter fine-strip integrality

Date: 2026-07-26

Audited file:
MATH_THEOREM_FINE_STRIP_FIXED_PARAMETER_INTEGRALITY_AND_TU_BOUNDARY_20260726.md.

## Verdict

The fixed-parameter theorem and its slow diagonal are correct:

\[
\boxed{\tau_{m,H,h}=\tau^*_{m,H,h}+o_{H,h}(W)}
\qquad(H,h\text{ fixed},\ 1\le H<h),
\]

and consequently there are arbitrarily slowly growing integer sequences
\(H_m\to\infty\), \(h_m\to\infty\), \(H_m/h_m\to0\) for which

\[
\boxed{\tau_{m,H_m,h_m}=W+o(W).}
\]

The determinant-two minor is valid.  The outer-capacity conclusion is also
valid, but its original proof had one gap: a middle-layer singleton bill of
\((1-o(1))W\) does not by itself exceed the \(W\) baseline in \(\tau^*\).
The corrected first-three-layer calculation gives the stronger bound
\(J\ge(3-o(1))W\) at the target scale.  That correction has been inserted
in the theorem file.

No conclusion here reaches a Gaussian-width diagonal.  The exact
unconditional consequence is only a qualitative, arbitrarily slowly growing
fine-strip band.

## 1. Catalogue, degrees, and codegrees

A physical strip has \(2h\) distinct targets in each of the \(2H+1\)
audited layers, so its hyperedge size is

\[
k=2h(2H+1).
\]

Double-counting strip--target incidences gives

\[
D_q=\frac{(m+q)!(m-q)!}{2(m-h)!^2}.
\]

For fixed \(H,h\),

\[
\log(D_q/D_0)
=\sum_{i=1}^q\log\frac{m+i}{m-i+1}=O_H(m^{-1}),
\]

uniformly for \(q\le H\).  Hence all degrees are
\((1+o(1))D_0\), and \(D_0\to\infty\).

The exact two-target phase count gives

\[
\max_{S\ne T}
\frac{d(S,T)}{\min(d(S),d(T))}
=\frac{2}{m-H+1}.
\]

The maximum is attained by an adjacent nested pair in signed ranks
\(H-1,H\).  Thus, for fixed \(H\),

\[
\Delta_2=O(D_0/m)=o(D_0).
\]

The physical hypergraph is simple.  From the middle support one recovers
the induced Johnson cycle: two support sets are Johnson adjacent exactly
when their strip phases differ by \(\pm1\).  Their common intersection is
the core, and the cyclic succession recovers the active order up to the
rotation/reversal quotient already used in the catalogue.

As a finite guard against a quotient error, a complete census at
\((m,h,H)=(4,2,1)\) gives:

* \(1260\) strips, exactly the catalogue formula;
* \(1260\) distinct hyperedges;
* degrees \(72\) in rank \(4\), \(90\) in ranks \(3,5\), exactly \(D_0,D_1\);
* maximum normalized pair codegree \(36/72=1/2\), exactly
  \(2/(m-H+1)\).

## 2. Applicability of the fixed-uniformity matching theorem

For fixed \(H,h\), \(k\) is fixed, all degrees are
\((1+o(1))D_0\), \(D_0\to\infty\), and
\(\Delta_2=o(D_0)\).  These are exactly the hypotheses of the standard
fixed-uniformity Pippenger--Frankl--Rödl almost-perfect matching theorem.
It produces a matching leaving

\[
Z=o_{H,h}(|\mathcal V_{m,H}|)=o_{H,h}(W)
\]

vertices uncovered.

If its size is \(s\), disjointness gives

\[
2h(2H+1)s=|\mathcal V_{m,H}|-Z.
\]

Selecting the strips and repairing exactly the \(Z\) holes by singleton
columns costs

\[
\begin{aligned}
J
&=(2h+2H)s+Z\\
&=\frac{1+H/h}{2H+1}|\mathcal V_{m,H}|
 +\left(1-\frac{1+H/h}{2H+1}\right)Z.
\end{aligned}
\]

For fixed \(H\),

\[
|\mathcal V_{m,H}|=(2H+1)W+O_H(W/m),
\]

so

\[
J=(1+H/h)W+o_{H,h}(W)
=\tau^*_{m,H,h}+o_{H,h}(W).
\]

Together with \(\tau^*\le\tau\le J\), this proves the fixed-parameter
theorem.

## 3. Slow diagonal

Apply the fixed theorem at \((H,h)=(j,j^2+1)\), choose a threshold \(M_j\)
after which the normalized gap is at most \(1/j\), and make the thresholds
strictly increasing with \(M_j\ge(j^2+2)^4\).  On the block
\(M_j\le m<M_{j+1}\), set \(H_m=j\), \(h_m=j^2+1\).  Then

\[
\frac{H_m}{h_m}\to0,\qquad
\frac{\tau_{m,H_m,h_m}-\tau^*_{m,H_m,h_m}}W\to0,
\]

and therefore \(\tau_{m,H_m,h_m}=W+o(W)\).

This is a valid qualitative diagonal.  It supplies no quantitative growth
rate.  The auxiliary choice of \(M_j\) even ensures
\(H_m\le m^{1/8}\), emphasizing that no Gaussian claim is being made.

## 4. Determinant-two minor

Let \(R\) have size \(m-2\) and let \(a,b,c,d\) be distinct outside \(R\).
Put

\[
S_1=R\cup\{a,b\},\quad
S_2=R\cup\{a,c\},\quad
S_3=R\cup\{a,d\}.
\]

For each pair, say \(S_1,S_2\), take a core \(K\subset S_1\cap S_2\) of
size \(m-h\), arrange the \(h-1\) points of
\((S_1\cap S_2)\setminus K\) between \(b\) and \(c\), and complete the
active cycle with \(h-1\) points outside \(S_1\cup S_2\), avoiding \(d\).
The count \(m-2\ge h-1\) is exactly \(h\le m-1\).
This strip contains \(S_1,S_2\) and cannot contain \(S_3\).
Doing this cyclically gives the minor

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix},
\qquad |\det|=2.
\]

Thus the literal incidence matrix is not totally unimodular for
\(2\le h\le m-1\).  This only rules out direct TU of that matrix; it does
not rule out a larger extended formulation.

## 5. Correct Gaussian capacity obstruction

If the selected strips form a matching in the whole band and
\(s=|\mathcal M|\), the outer layer gives

\[
s\le \frac{N_H}{2h}.
\]

The matching covers \(2hs\) targets in each audited layer.  Looking only at
the middle and the two signed depth-one layers, any singleton completion
has

\[
\begin{aligned}
J
&\ge(2h+2H)s+(W-2hs)+2(N_1-2hs)\\
&\ge W+2N_1-\left(2-\frac Hh\right)N_H.
\end{aligned}
\]

If \(H/\sqrt m\to A\in(0,\infty]\), \(H=o(m^{2/3})\), and \(H/h\to0\),
then

\[
\frac{N_H}{W}\to e^{-A^2},\qquad \frac{N_1}{W}\to1,
\]

and hence

\[
\liminf\frac JW\ge3-2e^{-A^2}>1
=\lim\frac{\tau^*}{W}.
\]

At \(H=\lceil\sqrt{m\log m}\rceil\), \(N_H/W=m^{-1+o(1)}\), so

\[
J\ge(3-o(1))W
\quad\text{while}\quad
\tau^*=(1+o(1))W.
\]

Therefore ordinary all-ranks matching plus singleton repair has a positive
linear gap at every genuine Gaussian or super-Gaussian cutoff in the stated
range.  This is not an obstruction to SCI: SCI must permit the forced
rank-dependent multiplicities rather than require every audited target to
be used at most once.

