# Independent audit: period-eight functional compression no-go

**Date:** 2026-08-04  
**Status:** independent line-by-line pure-mathematical audit of
`MATH_THEOREM_APERY_PERIOD8_FUNCTIONAL_COMPRESSION_NOGO_AND_SHIFT_TRAIN_DIRECTION_20260804.md`.
The audit reproduces the construction, the honesty and overlap-depth checks,
the endpoint comparison, and the literal periodic derivative estimates.  It
confirms the theorem with no correction.  No numerical search or finite
enumeration is used.

## 1. Family and exact Apéry constraints

Normalize

\[
 a={A\over15},\qquad P=14a,
\]

and compare

\[
 G_0=(a,a,a,a,4a,a,a,4a)
\]

with

\[
 G_\varepsilon=(a,a,a,a+\varepsilon,4a-\varepsilon,a,a,4a),
 \qquad 0<\varepsilon<a.
\tag{1.1}
\]

Both have total \(14a\), first gap \(a\), and exact first-carry threshold
\(P+a=A\).  Relative to the constant baseline, the excess vector of
\(G_\varepsilon\) is

\[
 (0,0,0,\varepsilon,3a-\varepsilon,0,0,3a).
\tag{1.2}
\]

For lengths one through three the distinguished prefix has zero excess, and
every cyclic block has nonnegative excess.  For length four the prefix has
excess \(\varepsilon\).  No four consecutive cyclic positions avoid all of
\(\{4,5,8\}\), so every competing block has excess at least
\(\varepsilon\).  For
lengths five through seven, every cyclic block either contains position 8
or, if it avoids position 8, lies in positions 1 through 7 and contains both
positions 4 and 5.  Its excess is therefore at least \(3a\), equal to the
prefix excess.  Length eight is tautological.  Thus every distinguished
prefix is a minimum cyclic block, which is exactly the cyclic
superadditivity system.

The exact period-eight quantities are

\[
 L=\gamma_2+\gamma_3+\gamma_4=3a+\varepsilon,
 \qquad T=\gamma_8=4a.
\]

Since \(\varepsilon<a\),

\[
 T>L,
 \qquad
 L+\gamma_5=7a>T+\gamma_6+\gamma_7=6a.
\tag{1.3}
\]

These are exactly the two strict conditions for overlap depth \(H=3\).
The shifts are

\[
 a,2a,3a,4a+\varepsilon,8a,9a,10a,
\tag{1.4}
\]

so precisely three shifts exceed \(A/2=15a/2\).  Hence \(u=H=3\), as
claimed.

## 2. Same-marginal canonical family

A same-\((a,P)\) canonical two-spike word has the form

\[
 G_z=(a,a,a,a,7a-z,a,a,a+z).
\tag{2.1}
\]

The total is automatically \(14a\).  The authenticated canonical-domain
conditions are

\[
 t\ge b,\qquad t>3a,\qquad b>t-a.
\]

After inserting \(t=a+z\) and \(b=7a-z\), these reduce exactly to

\[
                         3a\le z<{7a\over2}.
\tag{2.2}
\]

The late shifts are \(11a-z,12a-z,13a-z\); their reflected arguments are

\[
 {2a+z\over A},\qquad {3a+z\over A},\qquad {4a+z\over A}.
\tag{2.3}
\]

On (2.2), all three lie in \([1/3,1/2)\).  Reflection replaces each late
compact term by \(q(y)=g(y)-f(y)\).  The established signs \(g'>0\) and
\(f'<0\) on this interval give \(q'>0\).  Thus the canonical endpoint
comparison is strictly increasing in \(z\), and its minimum is \(z=3a\),
which is exactly \(G_0\).

The perturbed word changes only the fourth shift, from \(4a\) to
\(4a+\varepsilon\).  Both lie strictly inside \([A/4,A/2]\), where the
threshold-period train is strictly decreasing.  Therefore

\[
 \mathscr E(G_\varepsilon)-\mathscr E(G_0)
 =F_A(4a+\varepsilon)-F_A(4a)<0,
\]

while \(\mathscr E(G_0)\le\mathscr E(G_z)\) for every canonical \(G_z\).
This independently proves the endpoint-compression no-go.

## 3. Literal derivative identity

For the literal period \(P=14A/15\), put \(p=14/15\) and

\[
 h(x)=xe^{-\pi x^2/4},
 \qquad F_P(w)=\sum_{q\ge0}K(qP+w).
\]

The compact \(q=0\) derivative contributes one positive and one negative
Rayleigh term; every \(q\ge1\) term lies beyond the threshold and contributes
only a positive Rayleigh term.  Hence, for \(0<u<1\),

\[
 {F_P'(Au)\over2A}
 =\sum_{q\ge0}h(1+u+qp)-h(1-u).
\tag{3.1}
\]

Absolute Gaussian convergence justifies termwise differentiation.

At \(u=4/15\), divide by \(h(11/15)\).  The first two positive ratios are

\[
 {19\over11}e^{-4\pi/15}< {4\over5},
 \qquad
 3e^{-242\pi/225}< {1\over8}.
\tag{3.2}
\]

The first inequality follows from

\[
 e^{4/5}>1+{4\over5}+{8\over25}+{32\over375}
 ={827\over375}>{95\over44};
\]

the second follows from

\[
 e^{242\pi/225}>e^{242/75}
 >\left({19\over7}\right)^3{92\over75}>24.
\]

For every later positive term, starting at \(z=33/15\),

\[
 {h(z+14/15)\over h(z)}
 \le {47\over33}e^{-56\pi/45}< {1\over20}.
\tag{3.3}
\]

Indeed \(e^{56\pi/45}>e^{56/15}>(19/7)^3(26/15)>30\).
Consequently the complete positive/adverse ratio is less than

\[
 {4\over5}+{1/8\over1-1/20}
 ={177\over190}<1.
\tag{3.4}
\]

Thus \(F_P'(4A/15)<0\).  Continuity supplies an
\(\varepsilon_0\in(0,a)\) for which

\[
 F_P(4a+\varepsilon)<F_P(4a)
 \qquad(0<\varepsilon<\varepsilon_0).
\tag{3.5}
\]

Since (1.4) changes no other residue train, (3.5) is exactly
\(\Phi(W_\varepsilon)<\Phi(W_0)\).

## 4. Uniform derivative sign on the canonical moving range

For \(1/2\le u\le2/3\), the first positive/adverse ratio in (3.1) is

\[
 R_0(u)={1+u\over1-u}e^{-\pi u}.
\]

Its logarithm has second derivative

\[
 {4u\over(1-u^2)^2}>0,
\]

so its maximum on the interval occurs at an endpoint.  At the endpoints,

\[
 3e^{-\pi/2}<{7\over10},
 \qquad
 5e^{-2\pi/3}<{7\over10}.
\tag{4.1}
\]

For the first inequality use

\[
 e^{3/2}>1+{3\over2}+{9\over8}+{9\over16}+{27\over128}
 ={563\over128}>{30\over7};
\]

for the second use \(e^2>(19/7)^2>50/7\).

For the first tail term, the prefactor relative to the adverse term is at
most \(39/5\), while the exponent is at least \(319\pi/225\).  Therefore

\[
 R_1<{1\over8},
\tag{4.2}
\]

because

\[
 e^{319\pi/225}>e^{319/75}
 >\left({19\over7}\right)^4{94\over75}>64.
\]

Starting with that tail term, each subsequent ratio has prefactor at most
\(101/73<7/5\) and exponent at least \(203\pi/150>4\).  Since
\((19/7)^4>42\), each is less than \(1/30\).  Thus the full ratio is less
than

\[
 {7\over10}+{1/8\over1-1/30}
 ={481\over580}<1.
\tag{4.3}
\]

This proves \(F_P'(w)<0\) throughout \(A/2\le w\le2A/3\).

For \(G_z\), the three moving shifts are

\[
 11a-z,\quad12a-z,\quad13a-z.
\]

Under (2.2), each lies in \([A/2,2A/3]\).  Hence

\[
 {d\over dz}\Phi(W_z)
 =-\sum_{r=5}^7F_P'(s_r)>0.
\]

The literal canonical family is minimized at \(z=3a\), namely at \(G_0\).
Combining this with (3.5) proves

\[
 \Phi(W_\varepsilon)<\Phi(W_z)
\]

for every same-\((a,P)\) canonical representative and every sufficiently
small positive \(\varepsilon\).

## 5. Scope audit

The theorem proves exactly the following obstruction:

* same-\((a,P)\) canonical two-spike compression is not monotone for either
  the endpoint-period comparison or the literal periodic Bellman functional;
* the failure already occurs inside the first legal \(h=8,H=3\) chamber;
* it is caused by one legal transfer from gap 5 to gap 4.

It does **not** prove that the perturbed word has nonpositive Bellman
functional.  It therefore does not reopen the already proved positivity of
the two-spike family, and it does not settle arbitrary \(h=8,H=3\) positivity.
The remaining proof must retain more than \((a,P)\) or use a genuinely global,
nonmonotone comparison.

## 6. Dependency verification

The audit used the following frozen inputs, whose bytes were rehashed before
this audit:

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_APERY_PERIOD8_FUNCTIONAL_COMPRESSION_NOGO_AND_SHIFT_TRAIN_DIRECTION_20260804.md` | `4656324a6f1c016e1a4409241c58e5a4c751e52f4ce89361b7643939b4feeb21` |
| canonical period-eight theorem | `MATH_THEOREM_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_20260804.md` | `76f1ced69d953d0ed0d6f1b4dd20566fcf5d6a657158c4b6de5b349e155e8e27` |
| independent canonical audit | `MATH_AUDIT_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_INDEPENDENT_20260804.md` | `ed3ba018742e88c7473fa8d8b7f0ea043912c0f5c8b1a09ebc4864700279c0fb` |
| compact-train monotonicity | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |

**Audit verdict:** **PASS**.  The functional compression gate is false on
the explicit honest family (1.1), with both strict comparisons certified by
exact inequalities.
