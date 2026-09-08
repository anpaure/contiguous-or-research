# Independent audit: three-efficient threshold-surface closure

**Date:** 2026-08-04  
**Verdict:** **PASS after a typesetting-only repair.**  
**Method:** symbolic Gaussian calculus and exact rational arithmetic only;
no search, SAT/CP solver, H100, or floating-point sign decision was used.

## 1. Frozen source and audit artifact

The submitted theorem

`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_20260804.md`

had SHA-256

`690ddca7f8193bb4c1986661f051ca21a3c1385ebcaef0ab72448bd948a9c2fe`.

The only edit was to restore two missing `\quad` commands in (2.3); no
mathematical statement changed.  The repaired theorem SHA-256 is

`7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b`.

The exact-rational replay is

`scratch/n4_three_eff_threshold_surface_independent_audit_20260804/exact_rational_replay.py`

at SHA-256

`953e02e876facf3030784dcfb95847d98f9c7a573dff0c85cabf9b8f0b4659ef`.

It prints `PASS: exact rational replay`.

## 2. Exact surface parameters

On the `w=y` face one has `y>=2u`.  The period boundary `P+u=A` gives
`P=A-u`, while the inherited three-efficient constraints give

\[
 u\le P/3,qquad A=P+u\ge2y,qquad x\le u.
\]

Therefore

\[
 0\le x\le u\le A/4,
 \qquad2u\le y\le A/2,
\]

exactly as in (0.3).  Conversely these inequalities imply the scalar
ordered-gap bounds needed on this surface: `P>=3u`, `P>=u+y`, and
`y<=2P/3`.  Thus the theorem neither omits a surface variable nor enlarges
the intended face.

## 3. Monotonic Gaussian pair

For `v=At`, put `a=pi/4` and `E(s)=exp(-as^2)`.  The exact train expansion
is

\[
 F_A(At)=1-E(1-t)-\sum_{n\ge0}E(1+t+n).
\]

The sum includes `E(1+t)` at `n=0`; all later terms are the Gaussian-tail
rows `q>=1`.  Hence there is no omitted or duplicated term.

Differentiating the symmetric pair gives

\[
 {d\over dt}\bigl(E(1-t)+E(1+t)\bigr)\ge0
 \quad\Longleftrightarrow\quad
 \tanh(2at)\ge t.
\]

Since `2a=pi/2>3/2`, it suffices to prove
`tanh(3t/2)>=t`.  The difference is concave on `[0,1/4]`, is zero at
zero, and at the other endpoint satisfies

\[
 \tanh(3/8)-1/4
 >{3/8\over1+3/8}-{1\over4}
 ={3\over11}-{1\over4}>0.
\]

The inequality `tanh x>x/(1+x)` follows directly from
`e^(2x)>1+2x`.  Concavity therefore propagates the endpoint signs across
the whole interval.  The monotonic-pair direction used in Lemma 1.1 is
correct.

## 4. Exact proof of `e^(-pi/4)>5/11`

From `pi/4<11/14=1/2+2/7`, it is enough to upper-bound two elementary
exponentials.  Exact geometric-tail estimates give

\[
 \sum_{j=0}^{3}{(1/2)^j\over j!}
 +{(1/2)^4/4!\over1-1/10}
 <{33\over20},
\]

with margin `11/8640`, and

\[
 \sum_{j=0}^{2}{(2/7)^j\over j!}
 +{(2/7)^3/3!\over1-1/14}
 <{4\over3},
\]

with margin `5/1911`.  Thus

\[
 e^{\pi/4}<e^{11/14}
 =e^{1/2}e^{2/7}
 <{33\over20}{4\over3}={11\over5},
\]

which proves the claimed strict inverse bound.

## 5. Small-shift upper bound

The monotonic pair gives

\[
 E(1-t)+E(1+t)\ge2e^{-\pi/4}>{10\over11}.
\]

After removing these two terms from the exact train expansion, the first
remaining tail term is `E(2+t)`.  Since `t<=1/4`,

\[
 E(2+t)\ge E(9/4)=e^{-81\pi/64}>{37\over2000}.
\]

The final Gaussian inequality was independently replayed using
`pi<355/113`, a degree-six positive Taylor polynomial, and its exact
geometric remainder.  The margin in the equivalent exponential upper
bound is

\[
 {5468934762851735834586721954429
  \over17253537991099247881972514553856}>0.
\]

Consequently

\[
 F_A(At)<1-{10\over11}-{37\over2000}
 ={1593\over22000}.
\]

The tail term has the correct orientation and multiplicity.

## 6. Reflected train and its constant

The exact theta completion is

\[
 F_A(v)+F_A(A-v)
 =-4\sum_{m\ge1}e^{-4\pi m^2}
                 \cos(2\pi m v/A).
\]

Its absolute value is below `1/20000`.  Indeed `pi>3` makes the first
term smaller than `e^(-12)` and every successive ratio at most
`e^(-36)`.  The exact positive Taylor bound `e^3>20` gives
`e^12>160000`, while `1-e^(-36)>1/2`.  Hence

\[
 4\sum_{m\ge1}e^{-4\pi m^2}
 <{4e^{-12}\over1-e^{-36}}
 <{8\over160000}={1\over20000}.
\]

Therefore

\[
 F_A(A-v)>-F_A(v)-{1\over20000}
\]

has the correct sign and strict constant.

## 7. Endpoint-period Bellman lower bound

For capacity `m=qn+r`, `0<=r<n`, the configuration of `q` endpoint
generators and one size-`r` generator gives

\[
 V_{qn+r}\ge qA+c_r.
\]

At `q=0`, internal superadditivity gives equality `V_r=c_r`.  At `q>=1`,
both sides lie in `[A,infinity)`, where `K` is increasing.  Thus

\[
 K(V_{qn+r})\ge K(qA+c_r).
\]

Summation over the unique residue decomposition of every capacity proves
(2.4).  Both sides are absolutely summable because repeated endpoint
generators force linear growth.  The lemma is a genuine Bellman lower
bound and does not discard any finite transient.

## 8. Final margin

For the four-slot threshold surface, Lemma 2.1 gives

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(A-u).
\]

The previously audited train bounds apply in exactly the needed ranges:

\[
 C(A)>{1\over25},\quad F_A(x)>{1\over25},
 \quad F_A(y)>0.
\]

Reflection and the small-shift upper bound give

\[
 F_A(A-u)>-{1593\over22000}-{1\over20000}.
\]

Therefore

\[
 {1\over25}+{1\over25}-{1593\over22000}-{1\over20000}
 ={1659\over220000}>0.
\]

The common-denominator arithmetic is exact.

## 9. Verdict and scope

The monotonic-pair argument, rational exponential bounds, reflected-train
constant, Bellman lower bound, surface range, and final margin are all
valid.

**Final independent verdict: PASS.**  The surface `P+u=A` is closed.

The theorem does not close `P+u=2y`, the `w=2u` five-pulse system, all
`n=4`, the universal Bellman inequality, or `nu(k)<=B(k)+O(1)`.
