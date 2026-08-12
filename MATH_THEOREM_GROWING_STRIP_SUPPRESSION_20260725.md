# Growing-strip suppression for the all-depth MSW energy problem

Date: 2026-07-25

Method: pure mathematics only.

## 1. Purpose

The depth-two MSW collision proof repeatedly ends in one of two analytic
forms: a synchronized critical renewal, or a walk segment trapped in a
fixed height strip.  At growing depth the second alternative remains much
stronger than it first appears.  This note records the uniform estimate
needed for the `q<=m^(1/4)` centered-energy window.

It does **not** prove that every all-depth collision admits this normal
form.  It proves that once a macroscopic `O(q)`-strip segment has been
extracted, all polynomial/exponential-in-`q` decorations are harmless.

## 2. Spectral strip bound

Let `W(L,h;a,b)` be the number of nearest-neighbour walks of length `L`
from height `a` to height `b` which stay in an interval containing `h`
allowed integer heights.

### Lemma 2.1

Uniformly in the endpoints,

\[
 W(L,h;a,b)\le h\left(2\cos{\pi\over h+1}\right)^L
 \le h\,2^L\exp\left(-{cL\over h^2}\right)                 \tag{2.1}
\]

for an absolute `c>0`.

#### Proof

The transition matrix is the adjacency matrix of the path graph on `h`
vertices.  Its spectral radius is `2 cos(pi/(h+1))`; bounding one matrix
entry by the operator norm times the dimension gives the first inequality.
The second follows from `cos x<=exp(-c x^2)` on `0<=x<=pi/2`. \(\square\)

## 3. Decorated collision certificates

Consider certificates built from a binary walk of total length `2m`, at
most `Aq` marked positions, and at most

\[
                         \exp(Aq\log(q+2))                    \tag{3.1}
\]

finite-state labels.  Suppose every certificate contains a contiguous
subinterval of length at least `eta m` on which the walk is confined to at
most `Bq+B` heights, where `A,B,eta>0` are fixed.

### Theorem 3.1 (uniform growing-strip suppression)

For every fixed `A,B,eta`, the number `N_(m,q)` of such certificates obeys

\[
 {N_{m,q}\over {2m\choose m}}
 \le
 \exp\left(
     O(q\log m)-{c_{B,eta}m\over(q+1)^2}
          \right).                                           \tag{3.2}
\]

Consequently, uniformly for

\[
                         1\le q\le m^{1/4},                   \tag{3.3}
\]

one has

\[
                         N_{m,q}=o\!\left({2m\choose m}\right),
                                                                  \tag{3.4}
\]

indeed with an `exp(-Omega(sqrt m))` factor after absorbing the
decorations.

More generally, (3.4) holds whenever

\[
                         q^3\log m=o(m).                       \tag{3.5}
\]

#### Proof

Choose the trapped interval and the marked positions.  This costs at most

\[
                         (2m)^2(2m)^{Aq}.                      \tag{3.6}
\]

Outside the trapped interval use the trivial two choices per step.  On the
trapped interval apply Lemma 2.1 with `h<=Bq+B`.  Multiplying by (3.1)
gives

\[
 N_{m,q}
 \le2^{2m}\exp\left(
       O(q\log m)-{c_{B,eta}m\over(q+1)^2}
                    \right).                                  \tag{3.7}
\]

Finally `binom(2m,m)=Theta(2^(2m)/sqrt m)`, proving (3.2).  Under (3.3)
the negative term is `-Omega(sqrt m)`, while the positive term is
`O(m^(1/4)log m)=o(sqrt m)`.  The same comparison proves the
more general criterion (3.5). \(\square\)

## 4. Exact all-depth gate

For the canonical MSW factor it is therefore enough, through the
constant-strength window `q<=m^(1/4)`, to prove the following structural
dichotomy for a pair of colliding pointed depth-`q` occurrences:

1. their unbounded corridor indices synchronize into a bounded number of
   critical paired-renewal channels whose squared convolution is `O(W)`;
   or
2. after deleting `O(q)` marked pivot steps, a segment of length
   `Omega(m)` is confined to `O(q)` heights.

Theorem 3.1 disposes of the second branch uniformly, including
`exp(O(q log q))` finite-state multiplicity.  Thus the unresolved content
of an all-depth extension is purely the combinatorial extraction of this
dichotomy and a `q`-uniform bound on the number of critical renewal
channels; it is not the growth of the bounded-strip transfer matrix.
