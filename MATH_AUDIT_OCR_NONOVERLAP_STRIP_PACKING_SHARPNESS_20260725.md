# Audit of the macroscopic nonoverlap strip-packing sharpness theorem

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, solver, or external input

Audited report:
`MATH_ATTACK_OCR_NONOVERLAP_STRIP_PACKING_SHARPNESS_20260725.md`.

## 0. Verdict

The construction and all four requested quantitative components are
correct:

1. the internal phase indices \(a=q\), \(b=2q-1\) give the literal
   nonoverlap factorization with corridor
   \(Z_Y=0^{2q}Y0^{2q}\);
2. the fixed-phase maps \(Y\mapsto D_j(Y)\) are injective, so the support
   conflict degree is at most \((3q+2)(3q+1)\);
3. the path-graph spectral expansion gives
   \(a_{q,n}\ge c_\gamma2^{2m-8q}/q^3\) for sufficiently small fixed
   \(\gamma\);
4. after the greedy \(q^{-2}\) loss and short-cycle deletion, the packing
   lower bound is \(c_\gamma2^{2m-8q}/q^5\), while the Catalan comparison is
   exactly

   \[
   {\Pi^{\rm strip}_{m,q}\over \operatorname {Cat}_m/\sqrt m}
   \le(\sqrt\pi+o(1))m^2 2^{-8q}=o(1).
   \]

There is no substantive error to patch. Two harmless presentation points
are recorded in Section 5:

* the short-cycle estimate in the report is a deliberate enlargement of
  the slightly sharper direct substitution;
* the positive part in the greedy lower bound is stated in prose in
  Section 4 and explicitly displayed in the theorem statement.

Neither affects any conclusion.

## 1. Literal roots and first-return chronology

The general audited corner roots specialize at

\[
 s=3q,\qquad K=2q,\qquad t=q-1,\qquad u=2q
\]

to

\[
 D_j=1^{2q+j}0^{2q}Y1^{q-j}0^{3q}
 \qquad(0\le j\le q-1),
 \tag{1.1}
\]

\[
 D_{q-1+k}=1^{3q}0^{2q+k-1}Y0^{3q-k+1}
 \qquad(1\le k\le q+1),
 \tag{1.2}
\]

and

\[
 D_{2q+k}=1^{k-1}Y0^{2q}1^{3q-k+1}0^{3q}
 \qquad(1\le k\le q+1).
 \tag{1.3}
\]

These ranges cover exactly \(D_0,\ldots,D_{3q+1}\). Since

\[
 |Y|=2q+2(m-5q)=2m-8q,
\]

each displayed root has length \(2m\). The strip conditions on \(Y\) give
the following exact height checks.

* In (1.1), after the initial \(0^{2q}\), the copy of \(Y\) is based at
  height \(j\), hence stays in \([j,j+2q]\subset[0,3q-1]\); the following
  ones first attain height \(3q\).
* In (1.2), \(Y\) is based at height \(q-k+1\), and its upper height is
  \(3q-k+1\le3q\).
* In (1.3), \(Y\) is based at height \(k-1\), and its upper height is
  \(2q+k-1\le3q\).

Thus every root is Dyck of height exactly \(3q\). The exceptional identity

\[
 (0^{2q}Y)0^{2q}=0^{2q}(Y0^{2q})
\]

is exactly the required block rotation, so
\(\tau D_j=D_{j+1}\) for \(0\le j\le3q\).

Only \(T_{q-1}\) and \(S_{2q}\) are nonempty, both of length

\[
 L=4q+2(m-5q)=2m-6q.
\]

Consequently

\[
 \delta(D_j)=
 \begin{cases}
  3q+L,&0\le j\le q-1,\\
  3q,&q\le j\le2q,\\
  3q+L,&2q+1\le j\le3q,
 \end{cases}
\]

while the accumulated deficit before phase \(j\) is \(j\) for
\(j\le2q\) and \(j+L\) thereafter. Every proper phase is therefore strict,
and at \(j=3q\)

\[
 C_{3q}=3q+L=\delta(D_{3q})<2m+1.
\]

This verifies genuine first return and winding zero. Finally,

\[
 \delta(D_0)+\delta(D_{3q})-2m
 =2(3q+L)-2m=L,
\]

so the reported \(\Lambda=L\) is exact.

## 2. Internal nonoverlap indices

For the middle roots, the terminal word is

\[
 R_{q-1+k}=0^{k-1}\overline T0^{3q-k}.
 \tag{2.1}
\]

At \(a=q\), one has \(k=1\), and at \(b=2q-1\), one has \(k=q\).
Therefore

\[
 R_a=\overline T0^{3q-1},
 \qquad
 R_b=0^{q-1}\overline T0^{2q}.
 \tag{2.2}
\]

Every block strictly between \(a\) and \(b\) is empty, so both transported
collars equal \(0^{q-1}\). With

\[
 Z_Y=\overline T0^{2q}=0^{2q}Y0^{2q},
\]

one gets literally

\[
 R_b=0^{q-1}Z_Y,
 \qquad
 R_a=Z_Y0^{q-1}.
 \tag{2.3}
\]

Thus the pair is nonoverlap. Its phase separation is \(q-1\), and the
corridor height is

\[
 3q-(q-1)-1=2q.
\]

Also

\[
 \operatorname {net}(Z_Y)=-2q,
 \qquad
 |Z_Y|=L+2q=2m-4q.
\]

The outer-ledger check is consistent: the left omitted side has \(q\)
blocks and contains \(T_{q-1}\), while the right omitted side has \(q\)
blocks and contains \(S_{2q}\). Hence

\[
 B_{a,b}=2q+2L,
 \qquad
 B_{a,b}-\Lambda=2q+L=|Z_Y|.
\]

Finally, for \(a\le v\le b\), substituting
\(k=v-(q-1)\) in (2.1) yields exactly

\[
 R_v=0^{v-a}Z_Y0^{b-v}.
\]

Thus every internal third phase telescopes, with every endpoint index
correct.

## 3. Support injectivity and conflict degree

The support is

\[
 Q(Y)=\{e_{D_0(Y)},\ldots,e_{D_{3q+1}(Y)}\},
\]

so it has \(h=3q+2\) edges whenever its cycle length exceeds \(h\).
For each fixed \(j\), formulas (1.1)--(1.3) place the substring \(Y\) at a
position and with a length depending only on \((j,m,q)\). Hence

\[
 Y\mapsto D_j(Y)
\]

is injective. Since quotient edges are indexed by their normalized roots,
one quotient edge can occur in at most one support at each of the \(h\)
phase indices. It therefore lies in at most \(h\) supports total.

After deleting carriers whose \(D_0\) lies on a cycle of length at most
\(h\), every remaining support contains \(h\) distinct edges. For a fixed
remaining support, each of its edges belongs to at most \(h-1\) other
supports. Thus its conflict degree is at most

\[
 h(h-1)=(3q+2)(3q+1).
\]

The greedy bound is consequently

\[
 \alpha(G)\ge
 {\bigl(a_{q,n}-\Xi_m(3q+2)\bigr)_+
  \over(3q+2)(3q+1)+1}
 \ge
 {\bigl(a_{q,n}-\Xi_m(3q+2)\bigr)_+
  \over(3q+2)^2}.
\]

This verifies both the membership bound and the direction of the final
denominator inequality.

The short-cycle theorem with \(h=3q+2\) directly gives the slightly sharper
bound

\[
 \Xi_m(h)\le(6q+4)(2m+1)^{6q+4}.
\]

The report uses

\[
 (6q+6)(2m+1)^{6q+6},
\]

which is a valid harmless enlargement and has the same consequence
\(\log\Xi_m(h)=O(q\log m)\).

## 4. Spectral lower bound

Let \(A\) be the adjacency matrix of the path graph on
\(\{0,1,\ldots,K\}\), where \(K=2q\), and let

\[
 \ell=K+2n=2m-8q,
 \qquad
 \theta={\pi\over K+2}.
\]

The standard sine eigenbasis gives

\[
 (A^\ell)_{0,K}
 ={2\over K+2}
 \sum_{j=1}^{K+1}
 (-1)^{j+1}\sin^2(j\theta)
 \bigl(2\cos(j\theta)\bigr)^\ell.
 \tag{4.1}
\]

The sign follows from
\(\sin((K+1)j\theta)=(-1)^{j+1}\sin(j\theta)\). Since \(K\) and
\(\ell\) are even, the terms \(j\) and \(K+2-j\) are equal; the central
eigenvalue is zero. Hence the factor \(4/(K+2)\) and range
\(1\le j\le K/2\) in the report are exact.

For \(2\le j\le K/2\),

\[
 {\sin^2(j\theta)\over\sin^2\theta}\le j^2
\]

and, because \(j\theta<\pi/2\),

\[
 \log{\cos(j\theta)\over\cos\theta}
 =-\int_\theta^{j\theta}\tan x\,dx
 \le-{(j^2-1)\theta^2\over2}.
\]

Thus the absolute tail divided by the first term is bounded by

\[
 \sum_{j=2}^{\infty}
 j^2\exp\!\left(-{\ell\theta^2\over2}(j^2-1)\right).
\]

For \(q=\lfloor\gamma\sqrt m\rfloor\),

\[
 \ell\theta^2\longrightarrow{\pi^2\over2\gamma^2}.
\]

Choosing fixed \(\gamma\) sufficiently small makes the last series at most
\(1/2\) for all sufficiently large \(m\). Therefore

\[
 a_{q,n}\ge
 {2\over K+2}\sin^2\theta(2\cos\theta)^\ell.
\]

Using \(\sin\theta\ge2/(K+2)\),
\(\cos\theta\ge e^{-\theta^2}\), and
\(\ell\theta^2=O_\gamma(1)\), one obtains

\[
 a_{q,n}\ge c_\gamma{2^{2m-8q}\over q^3}.
\]

Since \(\log\Xi_m(3q+2)=O_\gamma(\sqrt m\log m)=o(m)\), whereas
\(\log a_{q,n}=2m\log2+o(m)\), short-cycle deletion removes an
\(o(1)\) fraction. The greedy denominator contributes \(\Theta(q^2)\),
giving

\[
 \Pi^{\rm strip}_{m,q}
 \ge c_\gamma{2^{2m-8q}\over q^5}.
\]

Every exponent and polynomial factor is therefore correct.

## 5. Catalan comparison and minor presentation points

The elementary upper bound

\[
 \Pi^{\rm strip}_{m,q}\le a_{q,n}\le2^{|Y|}
 =2^{2m-8q}
\]

and

\[
 \operatorname {Cat}_m
 ={4^m\over\sqrt\pi\,m^{3/2}}(1+o(1))
\]

give

\[
 {\Pi^{\rm strip}_{m,q}\over \operatorname {Cat}_m/\sqrt m}
 \le(\sqrt\pi+o(1))m^2 2^{-8q}.
\]

For \(q=\gamma\sqrt m+O(1)\), this is

\[
 \exp\bigl(-8\gamma(\log2)\sqrt m+O(\log m)\bigr)=o(1).
\]

Thus the construction refutes deterministic cross-carrier collision while
remaining exponentially negligible at the coefficient-one scale.

The only minor textual points are:

1. Section 4's displayed greedy fraction omits the positive-part notation,
   but the following sentence says explicitly that positive parts are
   understood, and the main theorem displays it.
2. Equation (4.4) enlarges the direct short-cycle bound from exponents
   \(6q+4\) to \(6q+6\); this is valid and intentionally harmless.

No edit to the audited report is necessary.
