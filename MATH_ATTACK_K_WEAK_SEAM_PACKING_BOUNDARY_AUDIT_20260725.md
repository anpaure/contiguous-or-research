# Independent audit of the Lane K weak-seam packing boundary

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

Audited reports:

* `MATH_ATTACK_K_WEAK_ZERO_WINDING_PACKING_BOUNDARY_20260725.md`;
* `MATH_ATTACK_K_POSITIVE_WINDING_WEAK_SEAM_SCALAR_BOUNDARY_20260725.md`;
* `MATH_ATTACK_K_RPA_PHASE_FUSION_RETRACTION_CROSSAUDIT_20260725.md`.

## 0. Verdict

**Pass after the displayed overlap-dictionary correction and the explicit
even-prefix check now incorporated in the sources.**

The physical/quotient normalization, the (Lambda=0) start bound, the
common-carrier lengths, every weak-composition cardinality in the zero
residue model, the centered positive-winding denominator, the early
terminal-root charge, the parity/gcd construction, and the formal packing
constants all check.

The exact proved boundary is:

\[
 \overline\nu_H^{,0,\Lambda=0}=O(B_r/r)=o_A(B_r/H),
 \qquad H=\lceil A\sqrt r\rceil,
 \tag{0.1}
\]

and, for positive winding,

\[
 \#\{I:w(I)\ge K\}
 =O\!\left(\frac{B_r}{K\sqrt r}\right).
 \tag{0.2}
\]

Thus all diverging winding is (o_A(B_r/H)).  Returns whose terminal
first-maximum position is at most
(r/[K_0(\log r)^2]) are also (o_A(B_r/H)).

Not proved are the (Lambda>0) zero-winding branch and bounded positive
winding with a macroscopic terminal first maximum.  The two formal models
attain (Theta(B_r/H)) only in explicitly relaxed capacitated systems;
neither is a PBBS/Dyck orbit.  Hence they close scalar/marginal proof
architectures, not the desired PBBS theorem.

No argument uses the retracted converse from (d(D)=1).

## 1. Weak-seam and deck normalization

The linear dominance ledger is

\[
 L_H\le W+2HB_r+2(5H-1)\nu_H(P_r),
 \qquad W=NB_r,quad N=2r+1.
 \tag{1.1}
\]

After deleting the short quotient cycles,

\[
 N\overline\nu_H
 \le\nu_H(P_r)
 \le2N\overline\nu_H+NZ_H,
 \qquad HZ_H=o(B_r).
 \tag{1.2}
\]

Therefore

\[
 \overline\nu_H=o_A(B_r/H)
 \tag{1.3}
\]

is sufficient for (L_H=W+o_A(W)).  Conversely, the corresponding
physical scale is

\[
 \nu_H=o_A(W/H)=o_A(B_r\sqrt r).
\]

There is no missing deck factor in either audited report.  The older
(O_A(B_r/N)) quotient gate remains a stronger sufficient condition; it
is not the weakest consequence of (1.1).

## 2. Zero winding

### 2.1 The solved actual PBBS sector

For a genuine zero-winding return, put

\[
 e_j=\delta(D_j),qquad
 \Lambda=e_0+e_s-2r.
\]

The exact killed-path estimate for the (Lambda=0) kernel is

\[
 \sum_{s<H}e_{r,s}le C\frac{4^r}{r^{5/2}}.
 \tag{2.1}
\]

Since distinct packed intervals have distinct starts and

\[
 B_r\asymp4^r/r^{3/2},
\]

equation (2.1) gives

\[
 \overline\nu_H^{,0,\Lambda=0}
 \le C\frac{B_r}{r}
 =o_A(B_r/H).
 \tag{2.2}
\]

This uses start count alone; it does not multiply rarity by interval
length.

### 2.2 Correct carrier dictionary

The forward prefix certificate has length (e_0).  The dual suffix
certificate

\[
 C=(0S_s)(0S_{s-1})\cdots(0S_1)
\]

has length (e_s+|S_s|), not (e_s).  Since the common carrier has
length (2r-1), its literal overlap is

\[
 \boxed{\kappa=\Lambda+|S_s|+1.}
 \tag{2.3}
\]

It follows that

\[
 \kappa=1\Longrightarrow \Lambda=0, S_s=\varnothing,
\]

whereas (Lambda=0) gives only
(kappa=|S_s|+1).  The (Lambda=0) theorem is therefore strictly
more inclusive than the explicitly constructed overlap-one family.

### 2.3 Residue saturation constants

In the relaxed zero model, the exact simplex is

\[
 \Omega=\{(n_0,\ldots,n_{p-1})\ge0:\sum n_a=pq\},
 \qquad
 F=\binom{pq+p-1}{p-1}.
\]

The hyperplane (n_0=z) has size

\[
 K_z=\binom{pq-z+p-2}{p-2}.
\]

Direct cancellation gives

\[
 \frac{K_0}{F}=\frac{p-1}{p(q+1)-1}\ge\frac1{3q},
\]

and, for (0\le z<q),

\[
 K_z\ge K_0(1-1/q)^q\ge F/(12q).
\]

Hence disjoint subsets of size
(lfloor F/(24q)\rfloor) exist.  Assigning them to phase residues modulo
(q) makes the corresponding (q)-edge intervals tile each fibre cycle,
giving at least (mathcal B/(48q)=Theta(mathcal B/H)) intervals.

The model has an exact integral Pascal simplex, one transported slot
hyperplane, profile invariance, bijective transport, and strict scalar
potential (F_j=j-h).  It does not encode every multilevel PBBS fan
equation.  The source now states precisely this limited scope.

## 3. Positive winding

### 3.1 Centered deficit charge

For winding (w\ge1),

\[
 \sum_{j<s}(d(D_j)-1)=Nw+\delta(D_s)-s.
 \tag{3.1}
\]

With

\[
 \mathscr E_r=\sum_D(d(D)-1)=\Theta(B_r\sqrt r),
\]

edge-disjointness of the deficit cores gives

\[
 \sum_I\{Nw(I)+\delta(D_s(I))-s(I)\}\le\mathscr E_r.
 \tag{3.2}
\]

If (w\ge K), (delta(D_s)\ge1), and (s\le H-1), every summand is at
least (KN-H+2).  Thus

\[
 \#\{I:w(I)\ge K\}
 \le\frac{\mathscr E_r}{KN-H+2}
 =O\!\left(\frac{B_r}{K\sqrt r}\right).
 \tag{3.3}
\]

For (K(r)\to\infty), division by (B_r/H) gives
((A+o_A(1))/K(r)\to0).  Floors and cutoff endpoints are exact.

### 3.2 Early terminal maxima

The audited estimate

\[
 \Delta_{r,L}
 \le C_0(L+1)^3 4^r
 \exp[-c_0\sqrt{r/(L+1)}]
 \tag{3.4}
\]

with (L=\lfloor r/[K_0(\log r)^2]\rfloor) and
(c_0\sqrt{K_0/2}>6) yields

\[
 \Delta_{r,L}=O(4^r/r^3)=o_A(B_r/H).
\]

The terminal root is a boundary edge of the complete residence support,
so packed intervals have distinct terminal roots.  This justifies using
the unweighted terminal-root count.

### 3.3 Formal scalar saturation

Let (N=e(2s+1)), with (e) odd and (e/s\to C_A>4/A^2).  For a height
(h\le s), choose (w\in\{1,2\}) so that (s-w\equiv h\pmod2), and put

\[
 a=b=e(s-w),\qquad c=\widehat c=e(2w+1).
 \tag{3.5}
\]

Then

\[
 a+b+c=N,qquad sc=Nw+a,qquad s(c-1)=Nw+a-s.
 \tag{3.6}
\]

Thus both endpoint ledgers, their centered floors, the parity of a
first-maximum position, and zero area increment are exact.

For odd-prefix chronology, put (Y_j=a-jc).  If

\[
 \gcd(2w+1,2s+1)=1,
\]

then (Y_j\equiv0\pmod N) first occurs at (j=s) in
(0\le j<2s+1).  The source chooses
(s\not\equiv1\pmod3) and (s\not\equiv2\pmod5), so this holds for
both (w=1,2).

For even-prefix chronology,

\[
 \gcd(c,N)=e,qquad N/\gcd(c,N)=2s+1.
\]

Hence (jc\not\equiv0\pmod N) for every (1\le j\le s).  This explicit
check was required and is now present in the source.

Using at most the actual height inventory (b_{r,h}), complete formal
cycles lose only (Ns=O(r^{3/2})=o(B_r)) vertices to divisibility.  Starts
spaced (s+2) apart give

\[
 \Omega_A(B_r/s)=\Omega_A(B_r/H)
\]

pairwise edge-disjoint full supports, while total deficit mass is
(O_A(B_r\sqrt r)) and terminal positions tend to (N/2).

The model fails genuine PBBS reconstruction because its voltage visits
only

\[
 N/e=2s+1<N
\]

spatial labels.  This is the exact reason it is a no-go for scalar
inference rather than a PBBS counterexample.

## 4. Final implication scope

The audited package rigorously leaves only:

1. zero winding with (Lambda>0), requiring a PBBS-specific common-base
   cross-phase/multilevel incidence gain or literal block fusion; and
2. bounded positive winding with a macroscopic terminal first maximum,
   requiring genuine voltage reconstruction or the weakened transported-
   sector matching estimate (o_A(B_r/H)).

All diverging positive winding and the whole (Lambda=0) zero-winding
sector are below the weak seam scale.  Global fusion is a fallback, not a
logical consequence of the retracted Catalan-density argument.
