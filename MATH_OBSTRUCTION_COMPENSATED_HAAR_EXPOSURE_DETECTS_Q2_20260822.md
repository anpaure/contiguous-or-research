# Rooted exposure detects the puncture-averaged Haar depth-two current

**Date:** 2026-08-22  
**Status:** exact finite theorem at `r=4`; the displayed integer identities
are independently replayed by the accompanying exhaustive verifier.  This
is an obstruction only for the symmetric-group span of this particular
Haar trade.  It is not a no-go theorem for other compensated trades or for
an adaptive residual.

## 1. The signed puncture average

Put `Omega=[9]` and tag the two central shores

\[
 \mathcal V_M={\Omega\choose4},\qquad
 \mathcal V_L={\Omega\choose3}.
\]

For a word `w=(w_0,...,w_8)`, with subscripts read modulo nine, define its
directed punctured configuration

\[
 E(w)=\{(M,\{w_s,w_{s+1},w_{s+2},w_{s+3}\}):1\le s\le8\}
 \mathbin{\dot\cup}
 \{(L,\{w_s,w_{s+1},w_{s+2}\}):1\le s\le8\}.       \tag{1.1}
\]

The complete labelled catalogue is

\[
                         \mathcal C=\{E(w):w\in S_9\};       \tag{1.2}
\]

the usual containment-path reconstruction makes `w -> E(w)` injective.
Here is the reconstruction explicitly.  Write the retained targets as
`L_s=I_3^w(s)` and `M_s=I_4^w(s)`.  Their containment graph is the path

\[
 L_1-M_1-L_2-M_2-\cdots-L_8-M_8.
\]

Its two endpoints lie on different tagged shores, so its orientation is
intrinsic.  In this order `M_s-L_s={w_(s+3)}` for every `1<=s<=8`;
these differences recover eight word positions, and the unique unused
label recovers the ninth.  Thus no two words give the same configuration.

Use the certified four-for-four Haar orders

```text
negative                                      positive
1 8 6 7 4 5 3 9 2                         1 9 3 5 4 7 6 8 2
1 9 8 6 7 4 5 2 3                         1 5 4 7 6 8 9 2 3
1 5 3 9 8 6 7 2 4                         1 7 6 8 9 3 5 2 4
1 7 3 9 4 5 8 2 6                         1 8 5 4 9 3 7 2 6
```

as step-two orders: if `q` is one printed row, its physical consecutive
order is

\[
                         w(q)_j=q_{2j\bmod9}.                 \tag{1.3}
\]

Write `rho` for cyclic rotation of a physical word and define the signed
puncture average

\[
 \delta=\sum_{q\in\mathcal P}\sum_{a=0}^8[ E(\rho^aw(q))]
       -\sum_{q\in\mathcal N}\sum_{a=0}^8[ E(\rho^aw(q))].   \tag{1.4}
\]

Every target of a full cyclic deck occurs in exactly eight of its nine
punctures.  The Haar certificate has identical rank-four and rank-three
deck multisets on its two sides.  Therefore, for the central incidence
matrix `A`,

\[
                              \boxed{A\delta=0.}              \tag{1.5}
\]

Thus (1.4) is a genuine central-load-null candidate direction for the
compensated Gibbs polytope.

## 2. Rooted duplicate exposure

For a central tagged target `v` and a configuration `G`, use the unnormalised
rooted duplicate exposure

\[
 \widetilde P_{vG}
 =\sum_{F\in\mathcal C:\,v\in F}(|F\cap G|-1)_+.             \tag{2.1}
\]

The matrix `P` in the compensated-rate theorem divides the row indexed by
`v` by its positive complete-catalogue degree.  Hence

\[
                    P\eta=0\quad\Longleftrightarrow\quad
                    \widetilde P\eta=0                       \tag{2.2}
\]

for every signed configuration vector `eta`.

For a function `f` on tagged `s`-sets define its rank-two down projection

\[
 (\partial_{s,2}f)(X)=
       \sum_{V\in{\Omega\choose s}:\,X\subseteq V}f(V),
 \qquad X\in{\Omega\choose2}.                    \tag{2.3}
\]

Finally let `J` be the unpunctured lower depth-two Haar current.  Directly
from the eight printed rows,

\[
 \begin{aligned}
 J={}&-[13]+[23]+[14]-[24]\\
    &+[15]-[25]-[19]+[29],                         \tag{2.4}
 \end{aligned}
\]

where `[ij]` is the basis vector of the pair `{i,j}`.  The relabelling in
(1.3) does not change the set of step-two windows; it only writes them as
ordinary consecutive windows.

### Theorem 2.1 (exact exposure detection)

For the signed puncture average (1.4),

\[
 \boxed{
 \partial_{4,2}(\widetilde P\delta|_{\mathcal V_M})=425J,
 \qquad
 \partial_{3,2}(\widetilde P\delta|_{\mathcal V_L})=8832J.} \tag{2.5}
\]

In particular `P delta != 0`, and its rooted-exposure image determines the
entire nonzero depth-two current.

#### Proof

Incidence cancellation (1.5) was proved above.  It remains only finite
integer arithmetic.  For transparency, after swapping the sums in (2.1),
the two entries in (2.5) at a pair `X` are respectively

\[
 \sum_{G}\delta_G\sum_{F\in\mathcal C}
 (|F\cap G|-1)_+\,
 |\{V\in F\cap\mathcal V_M:X\subseteq V\}|,        \tag{2.6}
\]

and the same expression with `mathcal V_L`.  Here `G` ranges over the 72
explicit signed punctures in (1.4), and `F=E(w)` ranges once over the
`9!` explicit permutations in (1.2).  Thus (2.6) contains no choice,
probability, or numerical approximation.

Evaluating (2.6) gives the following complete 36-pair table:

\[
 \begin{array}{c|c|c|c}
 X&J(X)&\partial_{4,2}\widetilde P\delta(X)
              &\partial_{3,2}\widetilde P\delta(X)\\ \hline
 13,24,25,19&-1&-425&-8832\\
 23,14,15,29&+1&+425&+8832\\
 \text{the other 28 pairs}&0&0&0.
 \end{array}                                                   \tag{2.7}
\]

One short exact replay is included in
`scratch/verify_compensated_haar_exposure_detection_20260822.py`.  It
constructs the sets in (1.1), first checks (1.5), evaluates the integer
sum (2.6), and checks every entry of (2.7).  The three columns of (2.7)
are exactly (2.5).  `square`

## 3. Orbit-span obstruction

Coordinate permutations commute with central incidence, rooted exposure,
the down maps, and the shallow-current map.  Let

\[
                 \Delta=\sum_{g\in S_9}c_g\,g\delta          \tag{3.1}
\]

be any real linear combination of coordinate translates; only finitely
many coefficients need be nonzero.  Applying (2.5) translate by translate
gives

\[
 \partial_{4,2}(\widetilde P\Delta|_{\mathcal V_M})
     =425\sum_gc_g\,gJ.                              \tag{3.2}
\]

Therefore

\[
 \boxed{
 A\Delta=0\ \hbox{ automatically},\qquad
 P\Delta=0\ \Longrightarrow\ \sum_gc_g\,gJ=0.}    \tag{3.3}
\]

So no combination in the full symmetric-group span of the
puncture-averaged Haar trade can both preserve the compensated target and
rooted-exposure constraints and retain a nonzero depth-two Haar current.

This is a precise obstruction to one proposed implementation of the
compensated Gibbs theorem.  It does **not** say that `ker(A) cap ker(P)`
has no shallow-active direction.  A successful direction may use another
trade family, preserve exposure only in a stopped aggregate rather than
rootwise, or arise after the residual has broken complete-catalogue
symmetry.

## 4. Mechanical audit

Run

```text
python3 scratch/verify_compensated_haar_exposure_detection_20260822.py
```

The script uses only the Python standard library and exact integer
arithmetic.
