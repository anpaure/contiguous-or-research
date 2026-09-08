# Quantitative seam alternative: repaired theorem

## Status

The universal statement “every nonabsorbing seam has a uniformly cheap
bounded-congestion charge” is stronger than needed and is not proved. The
following aggregate alternative is proved and is sufficient to eliminate the
balanced atomic survivor.

> **Theorem.** In the audited three-box middle-order model, assume
> \(D=o(a^2)\) and
>
> \[
> \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}\Longrightarrow2\delta_x,
> \qquad {4\over3}\le x\le {3\over2},
> \]
>
> where \(P\) ranges over directed internal coordinate-peak plateaux and
> \(\lambda(P)\) is edge length. Then no such sequence of orders exists.

This theorem is conditional on the inherited capped-run lower bound under
\(D=o(a^2)\). It does not exclude mixed profiles or prove the all-\(k\) OR
conjecture.

## 1. Local seam alternative

Let consecutive regular plateaux be

\[
P=[u_-,v],\qquad P'=[u,v'],\qquad
(x-\varepsilon)a\le\lambda(P),\lambda(P')\le(x+\varepsilon)a.
\]

Let \(d\) be the cross-coordinate rising on \(P\), and set

\[
h=T_v(d),\qquad M=\max_{v\le s\le u}T_s(d).
\]

Integer strictness gives

\[
h\ge\lambda(P)-a\ge(x-1-\varepsilon)a,\qquad T_{v-1}(d)<M.
\]

Take a maximal component \(R\) of \(\{s:T_s(d)\ge M\}\) meeting a maximum in
\([v,u]\). If \(T_u(d)<M\), then \(R\subseteq[v,u-1]\). If \(T_u(d)=M\),
then on \(P'\) coordinate \(d\) either falls, is fixed, or rises. Falling
gives \(R\subseteq[v,u]\). Fixed is **high absorption** at level \(M\).
Rising would give

\[
T_{v'}(d)\ge(2x-1-2\varepsilon)a>a,
\]

impossible for \(\varepsilon<x-1\). Thus every regular seam is either
absorbed or supplies an internal threshold run

\[
R\subseteq[v,u],\qquad\lambda(R)\le g+1,\qquad g=u-v-1.
\]

This handles partial successors, intermediate maxima, shared endpoints, and
both word boundaries: the selected plateaux are internal, and in every cheap
case a strict value below \(M\) occurs by \(u+1\).

## 2. How many cheap seams exist

An absorbed successor is fixed on a positive line with

\[
(x-1-\varepsilon)a\le t\le(2-x+\varepsilon)a.
\]

Distinct regular successors cannot occupy the same geometric line: their
vertex sets are disjoint, each has more than \(a+1\) vertices, and a line has
at most \(2a+1\). Hence absorptions number at most

\[
3(3-2x+2\varepsilon)a+O(1).
\]

Atomicity gives \((2+o(1))a\) regular plateaux and complement-gap mass
\((3-2x+o(1))a^2\), so at most \((3-2x+o(1))a\) gaps exceed \(a\). Removing
absorptions, long gaps, exceptional neighbours, and two word ends leaves at
least

\[
C=(8x-10-6\varepsilon-o(1))a
\]

regular nonabsorbing seams with \(g\le a\).

## 3. Exact starts and bounded congestion

Put \(L=4a+2\). For a cheap seam \(P_{j-1}=[u_-,v]\),
\(P_j=[u,v_j]\), define

\[
I_j=[\max\{u_-,v_j-L\},v-1]\cap[1,M_a-L].
\]

For every \(i\in I_j\), \(P_j\) is the first complete dangerous plateau in
\(W_i=[i+1,i+L]\), while \(R\subseteq W_i\) and \(i\notin R\). Hence its
first-dangerous charge may be replaced by \(R\). Moreover

\[
|I_j|\ge\min\{\lambda_{j-1},L-\lambda_j-g-1\}
          \ge(x-\varepsilon)a-O(1).
\]

The intervals \(I_j\) are disjoint because each lies in the edge interior of
a different predecessor plateau. Global truncation deletes only \(O(a)\)
starts. Reusing one run for its starts is valid: every assignment remains in
a length-\(L\) forward window, so the inherited endpoint congestion is at
most \(L+1\).

Each reassigned start saves at least

\[
\lambda_j-\lambda(R)\ge(x-1-\varepsilon)a-O(1).
\]

Therefore the total saving is

\[
S\ge\big((8x-10-6\varepsilon)(x-\varepsilon)
              (x-1-\varepsilon)-o(1)\big)a^3.                 \tag{1}
\]

At \(x=4/3\) the limiting coefficient is \(8/27\).

## 4. Contradiction

Choose \(c=x-\zeta>1\). The audited first-dangerous ledger gives

\[
{Q_{\rm fd}\over a^3}\le3x+(9-2x)\zeta+2\zeta^2+o(1).
\]

At \(\varepsilon=0\), write \(S_0(x)=(8x-10)x(x-1)\). On
\([4/3,3/2]\),

\[
S_0(x)-(3x-4)=8x^3-18x^2+7x+4\ge {8\over27}.
\]

Choose \(\varepsilon\) and then \(\zeta\) small compared with this uniform
margin. Subtracting (1) yields

\[
Q_{\rm mod}\le(4-\eta)a^3
\]

for some fixed \(\eta>0\), contradicting the inherited capped-run lower bound
\(Q\ge(4-o(1))a^3\) under \(D=o(a^2)\).

## 5. Exact remaining gap

The proof uses neither Fable's proposed \(A'/B'\) peak injection nor a
pointwise ceiling on all plateau lengths. Those live-trace claims remain
unproved. The local seam trichotomy of Section 1 is correct and is now
incorporated. What remains genuinely open:

1. **Removing \(D=o(a^2)\).** The hypothesis enters only through the
   capped-run lower bound \(Q\ge(4-o(1))a^3\); without it the saving (1)
   contradicts nothing. Sections 1--3 are unconditional in \(D\).
2. **Broad mixed profiles.** Coupling different thresholds and directions
   strongly enough to exclude the mixed ledgers documented in
   MIXED_PROFILE_SEAM_NEXT.md. The present count uses one regular length
   band; for two-atom or spread spectra the absorption capacity and the
   per-start saving no longer share a single \(x\), and the margin (6.5 of
   the trace audit) is not known to survive.
3. **A larger safe-start interval.** \(I_j=[\max\{u_-,v_j-L\},v-1]\)
   cannot be extended left: past \(u_-\) the predecessor becomes complete
   in the window (the first-dangerous identity fails), and past
   \(v_j-L\) the successor leaves the window (the original charge is no
   longer \(\lambda_j\)). Extending right up to \(p-1\), where \(p\) is the
   run start, stays admissible and keeps span \(\le L+1\), but yields no
   guaranteed gain because only \(p\ge v\) is known. A provably larger
   interval requires new lower control of \(p-v\).

The expanded proof and adversarial audit are
FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md and
FABLE_QUANTITATIVE_SEAM_REPAIR_INDEPENDENT_AUDIT.md (repository root).
