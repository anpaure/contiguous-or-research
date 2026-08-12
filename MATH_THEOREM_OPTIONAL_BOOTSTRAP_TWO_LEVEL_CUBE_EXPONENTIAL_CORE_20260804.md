# Two-level cube isoperimetry forces an exponential optional bootstrap core

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional strengthening of the optional-core size bound.  It
does not exclude the core, but improves its required size from quadratic in
the aperture to exponential in the aperture.

## 0. Result

Let

\[
 \mathcal L=\binom{[2m-1]}{m-1},
 \qquad
 \mathcal U=\binom{[2m-1]}m.
\]

Let `B subseteq mathcal L` and `Q subseteq mathcal U`.  Write

\[
 d_B(U)=|\{x\in B:x\subset U\}|.
\]

Assume

\[
 |Q|\ge |B|
 \qquad\hbox{and}\qquad
 d_B(U)\ge D\quad(U\in Q),                         \tag{0.1}
\]

where `D>=1`.  Then

\[
 \boxed{
 |B|+|Q|\ge 2^D
 }
                                                               \tag{0.2}
\]

and, since every member of `B` has only `m` upper neighbours,

\[
 \boxed{
 |B|\ge {2^D\over 1+m/D}.
 }
                                                               \tag{0.3}
\]

Apply this to the minimal positive optional obstruction `B^-` from the
wide-gap bootstrap theorem.  There

\[
 D=d-3,
\]

there are at least `|B^-|+1` positive-capacity owners, and every such owner
contains at least `D` members of `B^-`.  Consequently

\[
 \boxed{
 |B^-|\ge {2^{d-3}\over 1+m/(d-3)}
          = {2^{d-3}\over O(d)}
          =2^{\Omega(\sqrt m)}.
 }
                                                               \tag{0.4}
\]

This uses the literal Boolean two-level embedding.  An abstract
`C_4`-free robust incidence structure need not obey (0.2), which is why
affine-plane examples do not contradict the theorem.

## 1. The cube induced-edge inequality

### Lemma 1.1

For every finite family `S subseteq 2^[N]`, the number `e(S)` of hypercube
edges with both endpoints in `S` satisfies

\[
 \boxed{
 e(S)\le {|S|\log_2|S|\over2}.
 }
                                                               \tag{1.1}
\]

The convention at `S=emptyset` is `0 log 0=0`.

#### Proof

Induct on `N`.  Split `S` according to the last coordinate, and identify
the two sections with families `S_0,S_1 subseteq 2^[N-1]`.  Put

\[
 a=|S_0|,\qquad b=|S_1|,
\]

and assume `a<=b`.  At most `a` cube edges cross between the two sections.
By induction,

\[
 e(S)\le {a\log_2a+b\log_2b\over2}+a.             \tag{1.2}
\]

It remains to compare this with the right side of (1.1).  If `b=0` the
claim is trivial.  Otherwise set `t=a/b in [0,1]`.  After cancelling the
common `log_2 b` terms, the desired inequality is

\[
 t\log_2t+2t\le(1+t)\log_2(1+t).                  \tag{1.3}
\]

In natural logarithms the difference between the right and left sides is

\[
 f(t)=(1+t)\log(1+t)-t\log t-2t\log2.
\]

One has `f(0)=f(1)=0` and

\[
 f''(t)=-{1\over t(1+t)}<0\qquad(0<t<1).
\]

Thus `f` is concave and nonnegative between its two zero endpoints.  This
proves (1.3), hence (1.1).  \(\square\)

## 2. The two-level incidence bound

Let `H` be the graph induced by the vertex set

\[
                         V(H)=B\mathbin{\dot\cup}Q
\]

inside the `(2m-1)`-dimensional hypercube.  Because `B,Q` occupy consecutive
ranks, its edges are exactly the incidences `x subset U` with
`x in B,U in Q`.  Put

\[
 n=|B|,\qquad q=|Q|,\qquad N=n+q,
\]

and let `E` be the number of edges of `H`.

The right-degree hypothesis gives

\[
                         E\ge Dq.                  \tag{2.1}
\]

Since `q>=n`, one has `q>=N/2`; hence

\[
                         E\ge {DN\over2}.          \tag{2.2}
\]

Lemma 1.1 applied to `V(H)` gives

\[
                         E\le {N\log_2N\over2}.    \tag{2.3}
\]

Comparing (2.2) and (2.3) proves

\[
                         N\ge2^D,                  \tag{2.4}
\]

which is (0.2).

Every `(m-1)`-set on `[2m-1]` has exactly `m` rank-`m` supersets.  Therefore

\[
                         E\le mn.                  \tag{2.5}
\]

Combining (2.1) and (2.5),

\[
                         q\le {mn\over D}.         \tag{2.6}
\]

Thus

\[
 2^D\le N=n+q\le n\left(1+{m\over D}\right),
\]

which proves (0.3).

## 3. Optional-core specialization

For the minimal maximizer `B^-`, let `Q` be the positive-capacity owner
set.  The optional bootstrap theorem proves

\[
                         |Q|\ge |B^-|+1             \tag{3.1}
\]

and, with `D=d-3`,

\[
                         |B^-\cap N(U)|\ge D
                         \qquad(U\in Q).            \tag{3.2}
\]

Equations (3.1)--(3.2) are exactly (0.1), so (0.3) gives the first
inequality in (0.4).

The deadline satisfies

\[
                         d=\Theta(\sqrt m).
\]

Hence `m/(d-3)=O(d)`, proving the remaining asymptotic forms in (0.4).

## 4. Exact scope

The theorem proves that a surviving optional obstruction is not merely a
quadratic bouquet.  It occupies exponentially many Boolean lower vertices
in the aperture `d`.

It does **not** prove:

1. that no such exponential core exists;
2. the conjecturally sharper threshold-shadow bound
   `|B|>=binom(2D-1,D-1)`;
3. that a large core contains a safe two-sided subcube or shifted family;
4. that the protected reservoir extends to a factor; or
5. `nu(k)<=B(k)+O(1)`.

The gain is structural: any further no-core argument may now spend a
`2^{Omega(sqrt m)}` lower bound, and the abstract affine-plane obstruction
is eliminated directly by Boolean cube isoperimetry.

## 5. Dependencies

- `MATH_THEOREM_CO_SMALL_WIDE_GAP_BOOTSTRAP_CORE_AND_COMPRESSION_BARRIER_20260804.md`
- the elementary hypercube induced-edge inequality, proved above

