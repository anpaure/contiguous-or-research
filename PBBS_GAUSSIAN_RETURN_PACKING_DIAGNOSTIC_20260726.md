# Diagnostic census for the Gaussian PBBS residence gate

Date: 2026-07-26

Status: **computation and heuristic evidence only**.  Nothing in this note
is used as a proof of a PBBS asymptotic statement.

Scripts:

* `scratch/pbbs_return_packing_census.py` (exact complete census);
* `scratch/pbbs_short_return_monte_carlo.py` (exact uniform-Dyck sampler,
  Monte Carlo return test).

All local processes were stopped after the runs recorded below.

## 1. Exact objects computed

For semilength \(r\), put

\[
 N=2r+1,
 \qquad B=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil.
\]

Dyck roots are enumerated exactly.  If \(\phi\) is the normalized one-step
PBBS map and \(\delta(D)\) its voltage, the script iterates

\[
 (D,v)\longmapsto(\phi D,v+\delta(D)\bmod N)
\]

and records the first positive odd return gap \(g(D)\) of the omitted
coordinate.  The quotient permutation is \(\tau=\phi^2\).  A root is
eligible when

\[
 g(D)\le2H-1.
\]

If \(g(D)=2s+1\), its quotient trace is represented by the circular edge
interval of length \(s+2\) starting at \(D\).  On every complete
\(\tau\)-cycle, the script computes the exact maximum number of pairwise
edge-disjoint such circular intervals.  It reports separately the cycles
of length greater than \(H+1\), which are precisely the retained long
quotient deck.

The implementation has two exact internal checks:

\[
 \#\{D:g(D)=5\}=r-1,
\]

and

\[
 \#\{D:g(D)=7\}=2^{r-1}-r.
\]

The complete census reproduces both formulas at every tested rank.

## 2. Exact finite census at \(A=2\)

Let \(\overline\nu_H^{\rm long}\) denote the exact long-cycle quotient
packing returned by the census.  The scale relevant to \((ST_A)\) is

\[
 {\sqrt r\,\overline\nu_H^{\rm long}\over B}.
\]

The exact values are:

| \(r\) | \(H\) | \(B\) | eligible starts | long packing | \(\sqrt r\,\overline\nu_H^{\rm long}/B\) | long packing / starts |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 6 | 1,430 | 580 | 96 | 0.190 | 0.166 |
| 9 | 6 | 4,862 | 1,634 | 349 | 0.215 | 0.214 |
| 10 | 7 | 16,796 | 7,374 | 1,551 | 0.292 | 0.210 |
| 11 | 7 | 58,786 | 22,069 | 5,201 | 0.294 | 0.236 |
| 12 | 7 | 208,012 | 66,428 | 17,069 | 0.284 | 0.257 |
| 13 | 8 | 742,900 | 288,115 | 66,888 | 0.324 | 0.232 |
| 14 | 8 | 2,674,440 | 926,163 | 228,091 | 0.319 | 0.246 |

The last column uses all eligible starts in the denominator, including the
negligible short-cycle part, so it slightly understates the retained ratio.

These ranks do **not** establish an asymptotic.  In particular \(H\) is
only \(6,7,8\), and fixed-gap families remain visible.  The observation is
only that the exact packing shows no finite-rank trend toward the vanishing
normalization required by

\[
 \overline\nu_H=o(B/\sqrt r).
\]

## 3. Uniform-Dyck return-start diagnostic

The second script samples a Dyck word exactly uniformly.  At current
height \(h\), with \(a\) up-steps left, the number of legal completions is

\[
 C(a,h)={h+1\over a+h+1}\binom{2a+h}{a}.
\]

The next bit is chosen in exact proportion to the two resulting completion
counts.  The only Monte Carlo step is repeating this exact sampler a finite
number of times.

For \(A=2\), 5,000 samples at each rank gave:

| \(r\) | \(H\) | estimated \(\Pr(g\le2H-1)\) | standard error | \(\sqrt r\,\Pr(g\le2H-1)\) |
|---:|---:|---:|---:|---:|
| 20 | 9 | 0.2434 | 0.00607 | 1.089 |
| 50 | 15 | 0.1608 | 0.00520 | 1.137 |
| 100 | 20 | 0.0842 | 0.00393 | 0.842 |
| 200 | 29 | 0.0584 | 0.00332 | 0.826 |

This is consistent with, but does not prove, a one-point scale

\[
 R_H\asymp_A B/\sqrt r.
\tag{3.1}
\]

## 4. Exact logical interpretation

The diagnostic cannot decide \((ST_A)\).  Even if (3.1) holds, the
maximum packing may be \(o(B/\sqrt r)\) if eligible starts occur in
clusters of diverging size along the actual \(\tau\)-cycles.

The pure-math note
`PBBS_ST_TWO_POINT_CLUSTERING_DICHOTOMY_20260726.md` isolates this issue.
With

\[
 \mathcal C_H=\sum_{t=1}^{H+1}
 |E_H\cap\tau^{-t}E_H|,
\]

it proves

\[
 \overline\nu_H\ge {R_H^2\over R_H+2\mathcal C_H}.
\]

Therefore critical one-point mass (3.1) refutes \((ST_A)\) only together
with the analytic two-point estimate

\[
 \mathcal C_H=O_A(R_H).
\]

Conversely, if \((ST_A)\) is true at the critical one-point scale, then
\(\mathcal C_H/R_H\to\infty\): a typical eligible start must have a
diverging number of eligible neighbours within one Gaussian horizon.

That two-time PBBS correlation, not the finite census, is the theorem still
needed to decide the route.
