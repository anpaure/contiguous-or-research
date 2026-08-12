# PBBS zero-winding sectors: exact experimental classification, a three-strip generating function, and the remaining packing theorem

Date: 2026-07-28

Status: **the finite census and all displayed algebraic consequences of the
sector condition are proved; the equivalence between the sector condition
and a genuine zero-winding return is a conjecture; the critical packing
lower bound is also a conjecture.**  This distinction is essential.

## 0. Executive statement

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad \tau=\phi^2,
\]

where \(\phi\) is the normalized one-step PBBS map on Dyck words.  The
compiler route asks whether, for every fixed \(A>0\),

\[
 \overline\nu_{\lceil A\sqrt r\rceil}=o_A(B_r/\sqrt r).
 \tag{0.1}
\]

The exact census now points in the opposite direction.  It suggests that
the zero-winding subfamily alone has

\[
 \overline\nu^{(0)}_{\lceil A\sqrt r\rceil}
 =\Theta_A(B_r/\sqrt r)
 \tag{0.2}
\]

for every sufficiently large fixed window \(A\).  The evidence is much
stronger than a fitted exponent:

1. every zero-winding start through \(r=14\) satisfies one explicit set of
   independent sector-height inequalities, with no false positives and no
   false negatives among \(2,674,440\) roots at the last rank;
2. those inequalities give one closed fixed-height generating function;
3. its coefficients agree exactly with the height histogram at every
   \(h\le r\le14\); and
4. exact interval scheduling gives
   \(\overline\nu^{(0)}\sqrt r/B_r\approx0.296\) at ranks \(12,13,14\).

Items 1 and 3 are exhaustive finite results, not asymptotic proofs.  The
classification theorem and the two-point estimate needed for (0.2) remain
to be proved.

## 1. Exact PBBS definitions

For a Dyck word \(D\) of semilength \(r\), let its first step attaining
the global maximum split it as

\[
 D=P1Q,
 \qquad
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P.
 \tag{1.1}
\]

If

\[
 D=P1R0S
 \tag{1.2}
\]

is the canonical first-maximum factorization, then

\[
 \tau D=S1P0R,
 \qquad
 d(D)=|S|+1,
 \qquad
 \delta(D)+\delta(\phi D)=N-d(D).
 \tag{1.3}
\]

For \(D_i=\tau^iD\) of height \(h\), the exact zero-winding equation is

\[
 \boxed{
 \sum_{i=0}^{h-1}d(D_i)=\delta(D_h).
 }
 \tag{1.4}
\]

The audited PBBS height-gap theorem implies that a zero-winding return, if
it exists, has quotient duration exactly \(h\) and ordinary gap \(2h+1\).
Thus (1.4) is the correct literal test used in the census.

## 2. First-deepest-spine sectors

Let the first step attaining height \(h\) determine the first deepest leaf
of the contour plane tree.  Along its root-to-leaf spine write

\[
 D=A_0,1,A_1,1\cdots A_{h-1},1\,
   0,B_{h-1},0\cdots0,B_1,0,B_0.
 \tag{2.1}
\]

Each \(A_i\) is the forest before the spine child at depth \(i\), and each
\(B_i\) is the forest after it.  The choice of the **ancestors of the first
global-maximum step** is important: the first record steps of the Dyck word
need not form this spine.

The ordinary first-deepest condition gives

\[
 \operatorname{ht}(A_i)\le h-i-1,
 \qquad
 \operatorname{ht}(B_i)\le h-i.
 \tag{2.2}
\]

The exhaustive census singles out the following strengthening.

### Conjecture S (exact sector classification)

A height-\(h\) Dyck word starts a genuine zero-winding PBBS return if and
only if

\[
 \boxed{B_0=\varnothing,}
 \tag{2.3}
\]

\[
 \boxed{
 \operatorname{ht}(B_i)\le\min(i,h-i)
 \quad(1\le i<h),
 }
 \tag{2.4}
\]

and

\[
 \boxed{
 \operatorname{ht}(A_i)
 \le
 \min\!\left(h-i-1,\left\lfloor{2h-i\over3}\right\rfloor\right)
 \quad(0\le i<h-1).
 }
 \tag{2.5}
\]

The condition \(B_0=\varnothing\) is the already proved necessity
\(d(D)=1\).  Condition (2.4) is the exact no-preemption cap on the
post-spine forests.  Condition (2.5) is the new part; its factor \(3\) is
the signature of the moving first-maximum chronology and is absent from
the previously retracted static-spine argument.

### Finite verification theorem

Conjecture S is true for every Dyck word of semilength \(r\le14\).
Moreover, the height counts obtained from (2.3)--(2.5) agree with the
coefficient formula in Section 3 for every \(h\le r\le14\).

This is verified independently by

`scratch/verify_pbbs_zero_sector_classification.py`.

The verifier constructs the PBBS maps from (1.1), tests (1.4) literally,
extracts the ancestor spine at the first global maximum, tests every cap,
and independently expands the bounded-height Dyck generating functions.

## 3. The fixed-height generating function

Let \(C_j(z)\) count Dyck forests of height at most \(j\), by semilength:

\[
 C_0(z)=1,
 \qquad
 C_j(z)={1\over1-zC_{j-1}(z)}.
 \tag{3.1}
\]

Put

\[
 2h-2=3q+\rho,
 \qquad \rho\in\{0,1,2\}.
 \tag{3.2}
\]

### Lemma 3.1 (cap multiplicities)

Among the \(2h-2\) free forests in (2.3)--(2.5), cap \(j\) occurs exactly
three times for \(1\le j\le q\), and cap \(q+1\) occurs \(\rho\) times.

#### Proof

The \(B\)-caps are

\[
 \min(i,h-i),\qquad1\le i<h,
\]

and the \(A\)-caps are

\[
 \min\!\left(h-i-1,\left\lfloor{2h-i\over3}\right\rfloor\right),
 \qquad0\le i<h-1.
\]

For an integer \(j\ge1\), count instead how many caps are at least \(j\).
The first list contributes \(h-2j+1\) when positive.  The second contributes
the number of \(i\) satisfying simultaneously
\(i\le h-j-1\) and \(i\le2h-3j\), namely
\(1+\min(h-j-1,2h-3j)\) when positive.  Taking the discrete difference in
\(j\), and separating \(2h-2\) modulo three, gives multiplicity three up
to \(q\) and the stated final multiplicity \(\rho\).  \(\square\)

Consequently Conjecture S implies the exact fixed-height count

\[
 \boxed{
 z_{r,h}
 =[z^{r-h}]
 \left(\prod_{j=1}^{q}C_j(z)^3\right)C_{q+1}(z)^\rho.
 }
 \tag{3.3}
\]

Define continuants

\[
 Q_0(z)=Q_1(z)=1,
 \qquad
 Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z).
 \tag{3.4}
\]

Since \(C_j=Q_j/Q_{j+1}\), (3.3) telescopes to

\[
 \boxed{
 Z_h(z):=\sum_{r\ge h}z_{r,h}z^{r-h}
 ={1\over
 Q_{q+1}(z)^{3-\rho}Q_{q+2}(z)^\rho}.
 }
 \tag{3.5}
\]

For example,

\[
 z_{r,2}=r-1,
 \qquad
 z_{r,3}=2^{r-1}-r,
 \qquad
 z_{r,4}=\binom{r-2}{2}2^{r-4}.
 \tag{3.6}
\]

## 4. Why three strips appear

Let

\[
 A_a(x)={x^a\over Q_a(x^2)}
 \tag{4.1}
\]

be the first-passage kernel for nonnegative walks which first reach height
\(a\) at their last step.  Let \(a_1,a_2,a_3\) consist of \(q+1\) repeated
\(3-\rho\) times and \(q+2\) repeated \(\rho\) times.  Then

\[
 a_1+a_2+a_3=2h+1
 \tag{4.2}
\]

and (3.5) is equivalently

\[
 \boxed{
 z_{r,h}=[x^{2r+1}]A_{a_1}(x)A_{a_2}(x)A_{a_3}(x).
 }
 \tag{4.3}
\]

Thus the conjectured exact class is a product of **three balanced
first-passage strips**.  This is the structural reason the fixed-height
mass is critical rather than exponentially small.

### Proposition 4.1 (conditional Gaussian-window asymptotics)

Assume Conjecture S.  For every fixed \(0<a<b<\infty\),

\[
 z_{r,h}=\Theta_{a,b}(4^r h^{-5})
 \quad\text{uniformly for}\quad
 a\sqrt r\le h\le b\sqrt r.
 \tag{4.4}
\]

Consequently

\[
 \boxed{
 \sum_{a\sqrt r\le h\le b\sqrt r}z_{r,h}
 =\Theta_{a,b}(4^r/r^2)
 =\Theta_{a,b}(B_r/\sqrt r).
 }
 \tag{4.5}
\]

#### Proof

Normalize

\[
 u_a(\ell)=2^{-\ell}[x^\ell]A_a(x).
\]

Finite-path diagonalization gives \(\|u_a\|_1=1/(a+1)\), and the standard
two-barrier local estimate gives, uniformly when \(\ell=\Theta(a^2)\),

\[
 u_a(\ell)=\Theta(a^{-3}).
\]

All three widths in (4.3) are \(\Theta(h)\), their sum is \(2h+1\), and
the target length is \(2r+1=\Theta(h^2)\).  Convolving three kernels gives
total critical mass \(\Theta(h^{-3})\) and a lattice local factor
\(\Theta(h^{-2})\).  Therefore

\[
 [x^{2r+1}]\prod_{j=1}^3A_{a_j}(x)
 =2^{2r+1}\Theta(h^{-5})
 =\Theta(4^rh^{-5}).
\]

The upper and lower constants are uniform on a fixed nondegenerate Gaussian
window by the same finite-path spectral estimates.  Summing over
\(\Theta(\sqrt r)\) heights and using
\(B_r\asymp4^r/r^{3/2}\) proves (4.5).  \(\square\)

The spectral/local estimate in this proof is standard and already appears
in the audited three-strip argument in
`MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md`, Section 7.
The new content is the conjectured exact realization (4.3).

## 5. Exact census

Let \(Z_r\) be the number of literal zero-winding starts over all heights,
and let \(P_r\) be their exact maximum quotient-edge-disjoint circular
interval packing.  The census gives:

| \(r\) | \(B_r\) | \(Z_r\) | \(Z_r\sqrt r/B_r\) | \(P_r\) | \(P_r\sqrt r/B_r\) | \(P_r/Z_r\) |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 16,796 | 6,520 | 1.2276 | 1,639 | 0.3086 | 0.2514 |
| 11 | 58,786 | 21,834 | 1.2318 | 5,326 | 0.3005 | 0.2439 |
| 12 | 208,012 | 74,242 | 1.2364 | 17,807 | 0.2965 | 0.2399 |
| 13 | 742,900 | 255,821 | 1.2416 | 60,938 | 0.2958 | 0.2382 |
| 14 | 2,674,440 | 891,575 | 1.2474 | 212,316 | 0.2970 | 0.2381 |

The complete zero-start sequence for \(r=1,\ldots,14\) is

\[
1,1,3,8,22,64,195,614,1981,6520,21834,74242,255821,891575.
\tag{5.1}
\]

The packings in the table are computed by exact circular interval
scheduling on every \(\tau\)-cycle.  They are evidence for a positive
limiting packing constant; they are not a proof of one.

## 6. The precise remaining theorem

Conjecture S plus Proposition 4.1 proves only that there are
\(\Theta(B_r/\sqrt r)\) zero-winding **starts** in a fixed Gaussian height
window.  It does not by itself prove that a constant fraction of their
length-\(h+2\) quotient intervals are edge-disjoint.

For a fixed height let \(\mathcal Z_{r,h}\) be the zero-start set.  A
sufficient two-point estimate is

\[
 \boxed{
 \sum_{1\le t\le h+1}
 \bigl|\mathcal Z_{r,h}\cap\tau^{-t}\mathcal Z_{r,h}\bigr|
 =O\bigl(|\mathcal Z_{r,h}|\bigr)
 }
 \tag{6.1}
\]

uniformly in a fixed Gaussian window.  Indeed, the conflict graph of the
return intervals then has bounded average degree.  Caro--Wei, or the
elementary greedy bound after deleting high-degree vertices, gives an
independent set of size \(\Omega(|\mathcal Z_{r,h}|)\).  Summing heights
would prove

\[
 \overline\nu^{(0)}_{A\sqrt r}=\Omega_A(B_r/\sqrt r).
 \tag{6.2}
\]

The exact data support (6.1): the forward overlap count per zero start is
about \(3\)--\(5\) in the computed and sampled ranges, while the packing
retains about \(24\%\) of all starts.  No proof of (6.1) is currently
known.  The exact two-start boundary identity in
`PBBS_ST_EXACT_TWO_START_BALANCE_20260726.md` is the natural interface.

## 7. Consequence for the compiler route

The currently proved estimate is

\[
 \overline\nu_{A\sqrt r}=O_A(B_r/\sqrt r),
 \qquad
 \nu_{A\sqrt r}(P_r)=O_A(B_r\sqrt r).
 \tag{7.1}
\]

The linear-seam compiler needs the corresponding little-oh.  If Conjecture
S and the two-point estimate (6.1) are proved, then the zero-winding sector
already satisfies the matching lower bound

\[
 \nu_{A\sqrt r}(P_r)=\Omega_A(B_r\sqrt r)
 \tag{7.2}
\]

for a suitable fixed \(A\).  Hence the PBBS little-oh gate is false, and
the compiler must share seams globally or bypass cutting every short
residence.

At present, (7.2) is **not proved**.  What is now solid is that the former
little-oh target is in serious conflict with an exact finite pattern, an
explicit candidate generating function at the matching critical order,
and stable exact packing constants through the largest exhaustively
enumerated ranks.

## 8. Proof priorities

1. Prove Conjecture S by a moving first-maximum/sector-transport induction;
   the static-spine induction is known to be false and must not be reused.
2. Derive the joint sector inequalities for \(D\) and \(\tau^tD\).
3. Sum those joint generating functions over \(1\le t\le h+1\) to prove
   (6.1).
4. Lift the quotient packing through the exact PBBS rotation deck.

The first two steps are finite-word theorems.  No probabilistic heuristic
is needed in their statements.
